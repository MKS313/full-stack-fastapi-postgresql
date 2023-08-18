import uvicorn
from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware

from app.api.api_v1.api import root, api_router
from app.core.config import settings

app = FastAPI(
    title=settings.PROJECT_NAME, openapi_url=f"{settings.API_V1_STR}/openapi.json"
)

# Set all CORS enabled origins
if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

# add routers
app.include_router(root.router, tags=["root"])
app.include_router(api_router, prefix=settings.API_V1_STR)


# if __name__ == "__main__":
#     # uvicorn.run(app="pasaj:app", host='127.0.0.1', port=8000, reload=False, workers=4)
#     uvicorn.run(app="main:app", host='127.0.0.1', port=8000, reload=True)


