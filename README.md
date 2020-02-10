# CUNA

Timebox: 2 hours
Task: see Mirador.Cuna.Mutual.Back.End.Exercise.txt

## Requirements
* Docker
* Docker-compose
* pip
* python 3.7
* postgres (for running the test)

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
$ export POSTGRES_USER=test && \
  export POSTGRES_PASSWORD=password && \
  export POSTGRES_HOST=localhost && \
  export POSTGRES_PORT=5432 && \
  export POSTGRES_DB=cuna && \
  py.test -vvv
```
Sample results
```
================================+==================== test session starts ==========================================================
platform darwin -- Python 3.7.6, pytest-5.3.5, py-1.8.1, pluggy-0.13.1 -- /usr/local/opt/python/bin/python3.7
cachedir: .pytest_cache
rootdir: /Users/pwong/Code/CUNA/cuna
collected 5 items

test/test_routes.py::test_route__success PASSED                                                                               [ 20%]
test/test_routes.py::test_route__success__status_get PASSED                                                                   [ 40%]
test/test_routes.py::test_route__success__job_callback_put PASSED                                                             [ 60%]
test/test_routes.py::test_route__success__job_callback_post PASSED                                                            [ 80%]
test/test_routes.py::test_route__success__job_post PASSED                                                                     [100%]

====================================================== 5 passed in 3.37s ===========================================================
```


## Coverage
Test test coverage.
```
$ coverage run --source cuna -m pytest
$ coverage report
```
Sample results
```
Name                  Stmts   Miss  Cover
-----------------------------------------
__init__.py              22      0   100%
app.py                   21     21     0%
config.py                 7      0   100%
models.py                11      0   100%
routes.py                48      4    92%
test/__init__.py          0      0   100%
test/conftest.py         23      0   100%
test/test_routes.py      44      2    95%
-----------------------------------------
TOTAL                   176     27    85%
```
