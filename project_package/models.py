import uuid
from datetime import datetime

from sqlalchemy import Column, DateTime, Enum, ForeignKey, String, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy_utils import UUIDType


db_session = scoped_session(sessionmaker(autoflush=True, autocommit=False))
Base = declarative_base()
Base.query = db_session.query_property()


class CreatedAtMixin(object):
    created_at = Column(DateTime, default=datetime.utcnow, index=True)


class UpdatedAtMixin(object):
    updated_at = Column(DateTime, default=datetime.utcnow,
                        onupdate=datetime.utcnow, index=True)


class User(CreatedAtMixin, UpdatedAtMixin, Base):
    id = Column(UUIDType(), default=uuid.uuid4, primary_key=True)
    name = Column(String(50), nullable=False)

    __tablename__ = 'users'

    def __repr__(self):
        return "<User(id='%s', name='%s')>" % (self.id, self.name)
