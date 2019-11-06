from flask import Flask
from routing.user import user_routing
from routing.weather import weather_routing
from routing.config import config_routing
from routing.timer import timer_routing
from routing.arduino import arduino_routing

from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy.orm import sessionmaker

db_local_string = "postgresql+psycopg2://weather:weather@localhost:5432/weather"
db_pi_string = "postgresql+psycopg2://xx:xxxx@192.168.2.143:5432/weatherstation"

db_string = db_local_string
db = create_engine(db_string)
Session = sessionmaker(bind=db)
session = Session()

meta = MetaData(db)

app = Flask(__name__)
user_routing = user_routing(session)
weather_routing = weather_routing(session)
timer_routing = timer_routing(session)
arduino_routing = arduino_routing(session)
config_routing = config_routing()

app.register_blueprint(user_routing)
app.register_blueprint(weather_routing)
app.register_blueprint(config_routing)
app.register_blueprint(timer_routing)
app.register_blueprint(arduino_routing)


def main():
    db.connect()
    app.run(debug=False, host='0.0.0.0')


if __name__ == '__main__':
    main()
