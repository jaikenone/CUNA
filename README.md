# CUNA

Timebox: 2 hours
Task: see Mirador.Cuna.Mutual.Back.End.Exercise.txt

## Requirements
* Docker
* Docker-compose
* pip
* python 3.7

## Build and Run

### Postgres container
```
$ docker-compose up --build -d
```

### Virtualenv
```
$ cd cuna
$ python3 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

