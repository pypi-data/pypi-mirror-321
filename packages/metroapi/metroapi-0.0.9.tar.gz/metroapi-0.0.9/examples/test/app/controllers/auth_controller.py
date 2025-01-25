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
from metro import Body

from app.models.user import User


class AuthController(Controller):
    @post("/login")
    @requires_auth
    async def login(self, request: Request, username: str = Body(...), password: str = Body(...)):
        user = User.authenticate(username, password)

        if not user:
            raise UnauthorizedError("Invalid username or password")

        user.get_auth_token()
        return {"message": "Hello, World!"}
