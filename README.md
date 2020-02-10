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


### Start Server
```
$ export FLASK_ENV=development && \
  export POSTGRES_USER=test && \
  export POSTGRES_PASSWORD=password && \
  export POSTGRES_HOST=localhost && \
  export POSTGRES_PORT=5432 && \
  export POSTGRES_DB=cuna && \
  export FLASK_APP=app.py && \
  flask run
```


## Example Use

### Request Job
Request job creation.
```
$ curl -XPOST -H "Content-type: application/json" -d '{"body": "a new body"}'  '127.0.0.1:5000/job/request'
```

### Post Callback
Post START to callback url.
```
$ curl -XPOST -H "Content-type: application/text" -d 'STARTED'  '127.0.0.1:5000/job/callback/1716353a-4c49-11ea-8d39-acde48001122'
```

### Put Callback
Put status to the callback url.
```
$ curl -XPUT -H "Content-type: application/json" -d '{"status": "COMPLETE", "details": "The job has successfully completed in xxx minutes"}'  '127.0.0.1:5000/job/callback/1716353a-4c49-11ea-8d39-acde48001122'
```

### Get Job Status
Get the status of a job via the UUID.
```
$ curl '127.0.0.1:5000/job/status/1716353a-4c49-11ea-8d39-acde48001122'
```


## Test
Run all test.
```
$ py.test
```
Sample results
```

```


## Coverage
Test test coverage.
```
$ coverage run --source cuna -m pytest
$ coverage report
```
Sample results
```

```
