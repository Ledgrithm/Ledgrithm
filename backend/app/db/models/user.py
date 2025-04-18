from datetime import datetime
from sqlalchemy import String, Boolean, DateTime
from sqlalchemy.orm import Mapped, mapped_column, relationship
from app.db.database import Base

class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str] = mapped_column(String(255), unique=True, index=True)
    hashed_password: Mapped[str] = mapped_column(String(1024))
    is_active: Mapped[bool] = mapped_column(Boolean, default=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    updated_at: Mapped[datetime] = mapped_column(DateTime, onupdate=datetime.now)

    # Связь с транзакциями (1 пользователь → много транзакций)
#    transactions: Mapped[list["Transaction"]] = relationship(
#       back_populates="user", 
#        cascade="all, delete-orphan"
#    )

    def verify_password(self, password: str) -> bool:
        from app.core.security import pwd_context
        return pwd_context.verify(password, self.hashed_password)
