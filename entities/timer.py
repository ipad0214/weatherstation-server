from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.dialects.postgresql import TIMESTAMP

Base = declarative_base()


class Timer(Base):
    __tablename__ = 'tb_timer'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    starttime = Column(String)
    duration = Column(Integer)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'starttime': self.starttime,
            'duration': self.duration
        }
