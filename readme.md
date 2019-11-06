# Weatherstation Server

## Installation
___
### Get resources
```git
    git clone https://x.x.x.x/weatherstation_server.git
```

### Install dependencies
```shell
    pip3 install -r requirements.txt
```

## Before first run
___
change [this line](main.py) to your local raspberry pi postgress server where the database exists.
```python
    db_pi_string = "postgresql+psycopg2://xx:xxxx@192.168.2.143:5432/weatherstation"
```

## Run on pi
___
### Run in shell
```shell
    python3 main.py
```

### Run in background
```shell
    nohup python3 main.py &
```

____



## PostMan Collection
Get it from here: [Postman collection](docs/postman_collection.json)

this postman collection represents all implemented http-requests. 
you can test the server without the app.

# [License](license.txt)

Type: MIT