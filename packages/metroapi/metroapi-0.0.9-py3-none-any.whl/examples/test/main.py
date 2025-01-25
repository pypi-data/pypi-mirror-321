from metro import Metro
from contextlib import asynccontextmanager
from app.controllers import *
from metro import Depends
from metro.auth import requires_auth
from metro.auth.helpers import dummy_requires_auth


@asynccontextmanager
async def lifespan(app: Metro):
    app.connect_db()
    yield


app = Metro(lifespan=lifespan, auto_discover_controllers=True)


@app.get("/app-route", dependencies=[Depends(requires_auth)])
async def app_route():
    return {"message": "Hello, World from app route!"}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
