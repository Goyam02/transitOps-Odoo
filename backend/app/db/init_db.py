from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from app.models.user import Role, User
from app.core.security import hash_password

SEED_ROLES = ["fleet_manager", "dispatcher", "safety_officer", "financial_analyst"]

DEFAULT_ADMIN = {
    "full_name": "Admin",
    "email": "admin@transitops.com",
    "password": "secret",
}


async def seed_roles(db: AsyncSession) -> None:
    for role_name in SEED_ROLES:
        exists = await db.execute(select(Role).where(Role.name == role_name))
        if exists.scalar_one_or_none() is None:
            db.add(Role(name=role_name))
    await db.commit()


async def seed_admin(db: AsyncSession) -> None:
    result = await db.execute(select(User).where(User.email == DEFAULT_ADMIN["email"]))
    if result.scalar_one_or_none() is not None:
        return
    role_result = await db.execute(select(Role).where(Role.name == "fleet_manager"))
    fleet_role = role_result.scalar_one()
    user = User(
        full_name=DEFAULT_ADMIN["full_name"],
        email=DEFAULT_ADMIN["email"],
        hashed_password=hash_password(DEFAULT_ADMIN["password"]),
        role_id=fleet_role.id,
    )
    db.add(user)
    await db.commit()


async def init_db(db: AsyncSession) -> None:
    await seed_roles(db)
    await seed_admin(db)
