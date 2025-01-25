from metro.models import *
from metro.auth import UserBase


class User(UserBase):
    name: str = StringField(required=True)
    rand_num: int = IntField(required=True)

    meta = {
        "collection": "user",
    }
