from metro.controllers import (
    Controller,
    Request,
    get,
    post,
    put,
    delete,
    before_request,
    after_request,
)
from metro.exceptions import (
    NotFoundError,
    BadRequestError,
    UnauthorizedError,
    ForbiddenError,
    TooManyRequestsError,
    HTTPException,
)
from metro.auth import current_user, requires_auth


class BaseController(Controller):
    @get("/hello")
    @requires_auth
    async def index(self, request: Request):
        return {"message": "Hello, World!"}
