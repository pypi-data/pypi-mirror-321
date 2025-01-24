"""
Wrapper around Azure Functions HTTP request handlers that provides:
- Automatic parsing and validation of query parameters and request body.
  Invalid request data will result in a 400 response with a descriptive error
  message generated from Pydantic validation.
- Automatic handling of return values when your handler returns something other
  than an HttpResponse object. If your handler returns anything other than an
  HttpResponse, it will be treated as a successful request (200) and your return value
  will be serialized to JSON (if it's a dict or Pydantic model) and included as
  the response body of a 200 response.


EXAMPLE 1 (before):

```
import json

def main(req: func.HttpRequest) -> func.HttpResponse:
    response_data = {"message": "Requst successful"}
    return func.HttpResponse(json.dumps(response_data), status_code=200)
```

EXAMPLE 1 (after):

```
from azure.functions_parser import validate_request

@validate_request
def main(req: func.HttpRequest):
    return {"message": "Requst successful"}
```

EXAMPLE 2 (before):

```
def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        body = req.get_json()
        arg1 = body["arg1"]
        arg2 = body.get("arg2", "default-value")

        param1 = req.params["param1"]
        param2 = req.params.get("param2", "default-value")
    except Exception as e:
        return func.HttpResponse(f"Bad arguments. Error: {e}", status_code=400)

    print("required stuff", arg1, param1)
    print("optional stuff", arg2, param2)

    response_data = {"message": "Requst successful"}
    return func.HttpResponse(json.dumps(response_data), status_code=200)
```

EXAMPLE 2 (after):

```
from azure.functions_parser import validate_request
from pydantic import BaseModel

class RequestBody(BaseModel):
    arg1: str
    arg2: str = "default-value"


@validate_request
def main(req: func.HttpRequest, body: RequestBody, param1: str, param2: str = "default-value"):
    print("required stuff", body.arg1, param1)
    print("optional stuff", body.arg2, param2)

    return {"message": "Requst successful"}
```
"""

import json
import inspect
from typing import Awaitable, Callable, Protocol, Any, overload, cast, TypeGuard
import pydantic
from pydantic import BaseModel
from pydantic_core import ErrorDetails
from functools import wraps
from dataclasses import dataclass
from azure.functions import HttpRequest, HttpResponse


HandlerResultData = HttpResponse | str | bytes | dict | BaseModel | None


class RequestHandler(Protocol):
    def __call__(
        self, req: HttpRequest, *args: Any, **kwargs: Any
    ) -> HandlerResultData: ...


class AsyncRequestHandler(Protocol):
    async def __call__(
        self, req: HttpRequest, *args: Any, **kwargs: Any
    ) -> HandlerResultData: ...


WrappedRequestHandler = Callable[[HttpRequest], HttpResponse]
AsyncWrappedRequestHandler = Callable[[HttpRequest], Awaitable[HttpResponse]]


@overload
def validate_request(handler: RequestHandler) -> WrappedRequestHandler: ...


@overload
def validate_request(handler: AsyncRequestHandler) -> AsyncWrappedRequestHandler: ...


def validate_request(
    handler: RequestHandler | AsyncRequestHandler,
) -> WrappedRequestHandler | AsyncWrappedRequestHandler:

    body_spec, query_params_model = _validate_handler_signature(handler)

    # Dynamically generate a request parser based on the handler's validated
    # signature. The parser should return a dict with valid keyword arguments
    # for the handler function if the request data is valid. Otherwise, it
    # should return an HttpResponse with a 400 status and error message.

    if query_params_model and body_spec:

        def parse_request(req: HttpRequest) -> HttpResponse | dict:
            params = dict(req.params) or {}
            body_bytes = req.get_body() or b"{}"

            kwargs: dict[str, Any] = {}
            errors: list[ErrorDetails] = []
            try:
                valid_params = query_params_model.model_validate(params)
                kwargs.update(valid_params.model_dump(exclude_unset=True))
            except pydantic.ValidationError as e:
                errors.extend(e.errors())

            try:
                valid_body = body_spec.model.model_validate_json(body_bytes)
                kwargs[body_spec.param_name] = valid_body
            except pydantic.ValidationError as e:
                errors.extend(e.errors())

            if errors:
                return _response_from_validation_error(errors)
            return kwargs

    elif query_params_model:

        def parse_request(req: HttpRequest) -> HttpResponse | dict:
            params = dict(req.params) or {}
            try:
                valid_params = query_params_model.model_validate(params)
            except pydantic.ValidationError as e:
                return _response_from_validation_error(e.errors())
            return valid_params.model_dump(exclude_unset=True)

    elif body_spec:

        def parse_request(req: HttpRequest) -> HttpResponse | dict:
            body_bytes = req.get_body() or b"{}"
            try:
                valid_body = body_spec.model.model_validate_json(body_bytes)
            except pydantic.ValidationError as e:
                return _response_from_validation_error(e.errors())
            return {body_spec.param_name: valid_body}

    else:

        parse_request = lambda req: {}

    # The wrapped handler will parse the request and return an HttpResponse with
    # a 400 if the request data failed validation. If parsing is successful, then
    # call the handler, unpacking the parsed request data into keyword arguments.

    if _is_async_handler(handler):

        @wraps(handler)
        async def async_wrapper(req: HttpRequest) -> HttpResponse:
            kwargs_or_response = parse_request(req)

            if isinstance(kwargs_or_response, HttpResponse):
                return kwargs_or_response

            result = await handler(req, **kwargs_or_response)
            return _response_from_result(result)

        return async_wrapper

    handler = cast(RequestHandler, handler)

    @wraps(handler)
    def wrapper(req: HttpRequest) -> HttpResponse:
        kwargs_or_response = parse_request(req)

        if isinstance(kwargs_or_response, HttpResponse):
            return kwargs_or_response

        result = handler(req, **kwargs_or_response)
        return _response_from_result(result)

    return wrapper


def _is_async_handler(
    handler: RequestHandler | AsyncRequestHandler,
) -> TypeGuard[AsyncRequestHandler]:
    return inspect.iscoroutinefunction(handler)


_ArgParser = type[BaseModel]


@dataclass
class _BodyParserSpec:
    param_name: str
    model: _ArgParser


class InvalidRequestHandlerError(Exception):
    pass


def _validate_handler_signature(
    handler: RequestHandler | AsyncRequestHandler,
) -> tuple[_BodyParserSpec | None, _ArgParser | None]:
    """
    A request handler's signature, in addition to the HttpRequest, can accept
    zero or many of the following arguments:
    - Zero or one paramter, of any name, annotated as a Pydantic model. If present,
      this model will be used to parse the request's JSON body.
    - Zero or many parameters, annotated as any URL-serializable type (str, int, etc),
      to represent query parameters, by name. If these are present, a Pydantic model
      will be constructed to parse them.

    Returns a tuple of two values:
    - The parameter name and Pydantic model for the JSON body, if present, or None.
    - The Pydantic model for the query parameters, if present, or None.

    Raises an InvalidRequestHandlerError if the handler's signature is invalid.
    """
    sig = inspect.signature(handler)
    params = list(sig.parameters.values())
    if not params:
        raise InvalidRequestHandlerError(f"Handler must accept a request argument.")

    first_annotation = params[0].annotation
    if first_annotation is not inspect._empty and first_annotation is not HttpRequest:
        raise InvalidRequestHandlerError(
            f"Handler's first param must be an HttpRequest."
        )

    params = params[1:]

    if not params:
        return None, None

    body_params = [p for p in params if _is_pydantic_model(p.annotation)]
    if body_params:
        if len(body_params) > 1:
            raise InvalidRequestHandlerError(
                "Handler must accept at most one BaseModel parameter for the request body"
            )
        body_param = body_params[0]
        body_spec = _BodyParserSpec(body_param.name, body_param.annotation)
        query_params = [p for p in params if p.name != body_param.name]
    else:
        body_spec = None
        query_params = params

    def model_field_from_param(param: inspect.Parameter) -> Any:
        annotation = param.annotation if param.annotation is not inspect._empty else Any
        default = ... if param.default is inspect._empty else param.default
        return (annotation, default)

    if query_params:
        query_params_model = pydantic.create_model(
            "QueryParams",
            **{p.name: model_field_from_param(p) for p in query_params},
            __config__=pydantic.ConfigDict(strict=False, coerce_numbers_to_str=True)
        )
    else:
        query_params_model = None

    return body_spec, query_params_model


def _is_pydantic_model(obj: Any) -> bool:
    """
    Returns True if the object is a Pydantic model class.
    """
    return isinstance(obj, type) and issubclass(obj, BaseModel)


def _response_from_result(result: HandlerResultData) -> HttpResponse:
    """
    Creates an HttpResponse from the return value of a request handler function.
    """
    if isinstance(result, HttpResponse):
        return result
    if isinstance(result, dict):
        return HttpResponse(json.dumps(result), mimetype="application/json")
    if isinstance(result, BaseModel):
        return HttpResponse(result.model_dump_json(), mimetype="application/json")
    return HttpResponse(result or "Operation successful", status_code=200)


def _response_from_validation_error(errors: list[ErrorDetails]) -> HttpResponse:
    """
    Create an HttpResponse from a Pydantic ValidationError encountered while
    parsing request data.
    """

    def format_loc(loc: tuple[int | str, ...]) -> str:
        loc_strs = [f"[{x}]" if isinstance(x, int) else str(x) for x in loc]
        return ".".join(loc_strs)

    response_payload = {
        "errors": [
            {
                "param": format_loc(detail["loc"]),
                "reason": detail["msg"],
                "type": detail["type"],
                "input": detail["input"],
            }
            for detail in errors
        ]
    }
    return HttpResponse(json.dumps(response_payload), status_code=400)


