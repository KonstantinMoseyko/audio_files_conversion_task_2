from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, LargeBinary
from datetime import datetime
import uuid

from core.models import Base


class User(Base):
    __tablename__ = "user"
    
    id_user = Column(Integer, primary_key=True)
    username = Column(String(255), nullable=False, default="")
    user_token = Column(String(36), nullable=False, unique=True, default=lambda: str(uuid.uuid4()))


class AudioRecord(Base):
    __tablename__ = 'audiorecord'

    id_record = Column(Integer, primary_key=True)
    id_user = Column(Integer, ForeignKey('user.id_user'), nullable=False)
    record_uuid = Column(String(36), nullable=False, unique=True, default=lambda: str(uuid.uuid4()))
    file_data = Column(LargeBinary, nullable=False)
