from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Float, Boolean
from sqlalchemy.dialects.postgresql import TIMESTAMP

Base = declarative_base()


class Arduino(Base):
    __tablename__ = 'tb_arduino'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    location = Column(String)
    version = Column(String)
    role = Column(Integer)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'location': self.location,
            'role': self.role,
            'version': self.version
        }
