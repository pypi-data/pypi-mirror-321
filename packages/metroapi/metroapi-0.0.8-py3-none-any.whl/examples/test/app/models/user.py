from metro.models import *
from metro.auth import UserBase


class User(UserBase):
    name = StringField(required=True)

    meta = {
        "collection": "user",
    }
