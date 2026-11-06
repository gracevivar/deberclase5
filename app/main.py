from fastapi import FastAPI

from app.controller.auth_controller import router as auth_router
from app.controller.producto_controller import router as producto_router
from app.db.database import crear_tablas

app = FastAPI(lifespan=crear_tablas)

app.include_router(producto_router)
app.include_router(auth_router)
