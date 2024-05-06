from sqlmodel import SQLModel, Field
from typing import Tuple
from sqlalchemy.orm import relationship


class User(SQLModel, table=True):
    __tablename__ = "user"
    user_id:int = Field(default=None, primary_key=True)
    username:str = Field(index=True, min_length=3, max_length=20)
    password:str = Field(min_length=8, max_length=20)
    email:str = Field(index=True, nullable=True, unique=True)  
    is_active:bool = Field(default=False)
    is_staff:bool = Field(default=False)
    orders = relationship("Order", back_populates="user")

    def __repr__(self):
        return f"<User {self.username}>"


class Order(SQLModel, table=True):
    __tablename__ = "orders"

    ORDER_STATUS: Tuple[Tuple[str, str], ...] = (
    ("PENDING", "pending"),
    ("IN-TRANSIT", "in-transit"),
    ("DELIVERED", "delivered")
)

    PIZZA_SIZES=[
        ("S", "small"),
        ("M", "medium"),
        ("L", "large"),
        ("FM", "family large")
    ]

    pizza_id:int = Field(default=None, primary_key=True)
    user_id:int = Field(foreign_key="user.id")
    # pizza_id:int = Field(foreign_key="pizza.id")
    quantity:int = Field(default=0)
    order_status : str = Field(sa_column_kwargs={"default": "PENDING"})
    flavour: str = Field(default="")
    pizaa_siza : str = Field(sa_column_kwargs={"default": "S"})
    user = relationship("User", back_populates="order") 

    def __repr__ (self):
        return f"<Order {self.pizza_id}>"
    
    