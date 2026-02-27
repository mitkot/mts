from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={
            "user": request.session.get("user"),
            "auth_error": request.query_params.get("auth_error"),
        },
    )


@router.get("/me")
async def me(request: Request):
    return JSONResponse(request.session.get("user") or {"authenticated": False})
