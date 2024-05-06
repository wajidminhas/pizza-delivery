
from sqlmodel import SQLModel
from pizza_delivery.pizza_db import engine, Session
from pizza_delivery.models import User, Order



SQLModel.metadata.create_all(engine)