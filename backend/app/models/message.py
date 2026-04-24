from sqlalchemy import ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.models.base import Base, TimestampMixin, UUIDMixin


class Message(Base, UUIDMixin, TimestampMixin):
    """A single message within a spiritual guidance session."""

    __tablename__ = "messages"

    session_id: Mapped[str] = mapped_column(ForeignKey("sessions.id"), index=True)
    role: Mapped[str] = mapped_column(String(20))  # "user" | "assistant" | "system"
    content: Mapped[str] = mapped_column(Text)
    emotion_detected: Mapped[str | None] = mapped_column(String(50), nullable=True)
    intent_category: Mapped[str | None] = mapped_column(String(50), nullable=True)

    session = relationship("Session", back_populates="messages")
