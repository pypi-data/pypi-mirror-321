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
from app.models import User


class BaseController(Controller):
    @get("/hello")
    # @requires_auth
    async def index(self, request: Request):
        users = [user.to_dict() for user in User.find_all_by_name_or_email("ricky", "rgon@seas.upenn.edu")]
        user = User.find_by_email_or_name("rgon@seas.upenn.edu", "bob")

        return {"message": "Hello, World!", "users": users, "user": user.to_dict() if user else None}
