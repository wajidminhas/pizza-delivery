from fastapi import APIRouter

auth_router : APIRouter = APIRouter(
    prefix='/auth',
    tags=["auth"]
)

@auth_router.get("/")
async def hello_auth():
    return {"Message" : "Hello Auth Router"}