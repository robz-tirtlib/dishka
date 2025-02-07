import logging

import uvicorn
from fastapi import FastAPI

from dishka.integrations.fastapi import (
    DishkaApp,
)
from myapp.ioc import AdaptersProvider, InteractorProvider
from myapp.presentation_web import router


def create_fastapi_app() -> FastAPI:
    app = FastAPI()
    app.include_router(router)
    return app


def create_app():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s  %(process)-7s %(module)-20s %(message)s',
    )

    return DishkaApp(
        providers=[AdaptersProvider(), InteractorProvider()],
        app=create_fastapi_app(),
    )


if __name__ == "__main__":
    uvicorn.run(create_app(), host="0.0.0.0", port=8000)
