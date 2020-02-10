from flask import Flask
import json
from datetime import datetime
import uuid

from cuna.models import Job, db
from cuna.routes import configure_routes


def test_route__success(client):
    response = client.get("/")

    assert response.get_data() == b'Hello, world!'
    assert response.status_code == 200

def test_route__success__status_get(client):
    job_uuid = str(uuid.uuid1())
    new_job = Job(
        date_created=datetime.now(),
        date_updated=datetime.now(),
        body="the body",
        uuid=job_uuid,
        status="STARTED",
        details=""
    )
    db.session.add(new_job)
    db.session.commit()

    rs = client.get(f"/job/status/{job_uuid}")

    assert rs.status_code == 200

def test_route__success__job_callback_put(client):
    job_uuid = str(uuid.uuid1())
    new_job = Job(
        date_created=datetime.now(),
        date_updated=datetime.now(),
        body="the body",
        uuid=job_uuid,
        status="STARTED",
        details=""
    )
    db.session.add(new_job)
    db.session.commit()

    mock_request_data = {
        "status": "COMPLETE",
        "details": "Details of job"
    }

    rs = client.put(
        f"/job/callback/{job_uuid}",
        content_type='application/json',
        data=json.dumps(mock_request_data)
    )

    assert rs.status_code == 204

def test_route__success__job_callback_post(client):
    job_uuid = str(uuid.uuid1())
    new_job = Job(
        date_created=datetime.now(),
        date_updated=datetime.now(),
        body="the body",
        uuid=job_uuid,
        status="",
        details=""
    )
    db.session.add(new_job)
    db.session.commit()

    rs = client.post(
        f"/job/callback/{job_uuid}",
        content_type='application/json',
        data="STARTED"
    )

    assert rs.status_code == 204

def test_route__success__job_post(client):
    mock_request_data = {
        "body": "the body"
    }

    rs = client.post(
        f"/job/request",
        content_type='application/json',
        data=json.dumps(mock_request_data)
    )

    job_uuid = rs.data.decode("utf-8")
    def validate_uuid(uuid_string):
        try:
            val = uuid.UUID(uuid_string, version=1)
        except ValueError:
            return False
        return True

    assert validate_uuid(job_uuid) == True
    assert rs.status_code == 200