from fastapi import APIRouter
from app.api.v1 import vehicles, drivers, trips, maintenance, fuel_logs, expenses, dashboard, chat, autopilot

api_router = APIRouter()

api_router.include_router(vehicles.router)
api_router.include_router(drivers.router)
api_router.include_router(trips.router)
api_router.include_router(maintenance.router)
api_router.include_router(fuel_logs.router)
api_router.include_router(expenses.router)
api_router.include_router(dashboard.router)
api_router.include_router(chat.router)
api_router.include_router(autopilot.router)

# Auth router owned by Backend Dev 1 — stub included so /auth/* routes don't 404
from fastapi import HTTPException

@api_router.post("/auth/login", tags=["Auth"])
async def auth_login_stub():
    raise HTTPException(status_code=501, detail="Auth owned by Backend Dev 1")


@api_router.get("/auth/me", tags=["Auth"])
async def auth_me_stub():
    raise HTTPException(status_code=501, detail="Auth owned by Backend Dev 1")


@api_router.post("/auth/users", tags=["Auth"])
async def auth_users_stub():
    raise HTTPException(status_code=501, detail="Auth owned by Backend Dev 1")
