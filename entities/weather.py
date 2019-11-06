from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey, Float
from sqlalchemy.dialects.postgresql import TIMESTAMP

Base = declarative_base()


class Weather(Base):
    __tablename__ = 'tb_weather'

    id = Column(Integer, primary_key=True, autoincrement=True)
    altitude = Column(Float)
    pressure = Column(Float)
    date = Column(TIMESTAMP)
    temperature = Column(Float)
    realAltitude = Column(Float)
    sealevel = Column(Float)
    humidity = Column(Float)


    @property
    def serialize(self):
        return {
            'id': self.id,
            'altitude': self.altitude,
            'pressure': self.pressure,
            'date': self.date.strftime('%H:%M:%S %d.%m.%Y'),
            'temperature': self.temperature,
            'sealevel': self.sealevel,
            'realAltitude': self.realAltitude,
            'humidity': self.humidity
        }
