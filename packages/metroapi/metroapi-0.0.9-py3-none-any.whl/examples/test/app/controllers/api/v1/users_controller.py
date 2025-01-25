from fastapi.params import Body

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
from pydantic import BaseModel


from app.models.user import User
from app.controllers.base_controller import BaseController


class UserCreate(BaseModel):
    name: str


class UserUpdate(BaseModel):
    name: str


class UsersController(BaseController):
    @get("/users")
    async def index(self, request: Request):
        """List all Users.

        Returns:
            list: List of User objects
        """
        items = User.find()
        return [item.to_dict() for item in items]

    @get("/users/{id}")
    async def show(self, request: Request, id: str):
        """Get a specific User by ID.

        Args:
            request (Request): The request object
            id (str): The User ID

        Returns:
            dict: The User object

        Raises:
            NotFoundError: If User is not found
        """
        item = User.find_by_id(id=id)
        if item:
            return item.to_dict()
        raise NotFoundError("User not found")

    @post("/users")
    async def create(self, request: Request, num: int = Body(...), num2: int = Body(...)):
        """Create a new User.

        Args:
            request (Request): The request object
            data (UserCreate): The creation data

        Returns:
            dict: The created User object
        """
        item = User(**data.dict()).save()
        return item.to_dict()

    @put("/users/{id}")
    async def update(self, request: Request, id: str, data: UserUpdate):
        """Update a specific User.

        Args:
            request (Request): The request object
            id (str): The User ID
            data (UserUpdate): The update data

        Returns:
            dict: The updated User object

        Raises:
            NotFoundError: If User is not found
        """
        item = User.find_by_id_and_update(id=id, **data.dict(exclude_unset=True))
        if item:
            return item.to_dict()
        raise NotFoundError("User not found")

    @delete("/users/{id}")
    async def destroy(self, request: Request, id: str):
        """Delete a specific User.

        Args:
            request (Request): The request object
            id (str): The User ID to delete

        Returns:
            dict: A success message

        Raises:
            NotFoundError: If User is not found
        """
        item = User.find_by_id_and_delete(id=id)
        if item is None:
            raise NotFoundError("User not found")
        return {"detail": "User deleted"}
