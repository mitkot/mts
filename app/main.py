from contextlib import asynccontextmanager

from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware

from app.auth.google import router as google_auth_router
from app.config import settings
from app.db import init_db
from app.routes.web import router as web_router


@asynccontextmanager
async def lifespan(_: FastAPI):
    init_db()
    yield


app = FastAPI(title="MTS Google Login Demo", lifespan=lifespan)
app.add_middleware(
    SessionMiddleware,
    secret_key=settings.session_secret,
    https_only=(settings.app_env == "production"),
    same_site="lax",
)

app.include_router(web_router)
app.include_router(google_auth_router)
