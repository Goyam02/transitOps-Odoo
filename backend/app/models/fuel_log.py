import uuid
from datetime import datetime, date
from sqlalchemy import String, Numeric, Date, ForeignKey, DateTime, func, text
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class FuelLog(Base):
    __tablename__ = "fuel_logs"

    id: Mapped[uuid.UUID] = mapped_column(primary_key=True, default=uuid.uuid4)
    vehicle_id: Mapped[uuid.UUID] = mapped_column(ForeignKey("vehicles.id"), nullable=False, index=True)
    trip_id: Mapped[uuid.UUID | None] = mapped_column(ForeignKey("trips.id"), nullable=True)
    liters: Mapped[float] = mapped_column(Numeric(8, 2), nullable=False)
    cost_per_liter: Mapped[float] = mapped_column(Numeric(8, 2), nullable=False)
    total_cost: Mapped[float] = mapped_column(
        Numeric(10, 2),
        server_default=text("liters * cost_per_liter"),
        nullable=False,
    )
    odometer_at_fill: Mapped[float | None] = mapped_column(Numeric(10, 2), nullable=True)
    filled_at: Mapped[date] = mapped_column(Date, nullable=False, server_default=func.now())
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now())
