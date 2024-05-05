
from fastapi import FastAPI
from pizza_delivery.auth_routes import auth_router
from pizza_delivery.order_routes import order_router



app : FastAPI = FastAPI()

app.include_router(auth_router)
app.include_router(order_router)