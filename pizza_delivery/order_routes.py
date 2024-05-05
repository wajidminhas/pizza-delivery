from fastapi import APIRouter

order_router : APIRouter = APIRouter(
    prefix='/order',
    tags=['order']
)

@order_router.get("/")
async def hello_order():
    return {"Message" : "Hello Order Router"}