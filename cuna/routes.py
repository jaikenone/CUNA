from flask import request, jsonify
import json
import uuid
from datetime import datetime

from .models import Job, db


def configure_routes(app):
    @app.route('/', methods=['GET'])
    def get():
        return "Hello, world!", 200

    @app.route('/job/request', methods=['POST'])
    def job_request():
        app.logger.debug("Create new job")
        job_uuid = str(uuid.uuid1())
        data = request.get_json()
        if 'body' in data:
            new_job = Job(
                date_created=datetime.now(),
                body=data['body'],
                uuid=job_uuid
            )
            db.session.add(new_job)
            db.session.commit()
            return job_uuid, 200
        else:
            return "Missing body", 400

    @app.route('/job/callback/<job_uuid>', methods=['POST'])
    def job_callback_post(job_uuid):
        app.logger.debug(f"Callback post for {job_uuid}")
        data = request.data.decode("utf-8")
        update_job = Job.query.filter_by(uuid=job_uuid).one_or_none()
        if update_job is not None:
            if data == 'STARTED':
                update_job.status = 'STARTED'
                update_job.date_updated = datetime.now()
                db.session.commit()
            return "", 204
        else:
            return "", 404

    @app.route('/job/callback/<job_uuid>', methods=['PUT'])
    def job_callback_put(job_uuid):
        app.logger.debug(f"Update job status for {job_uuid}")
        data = request.get_json()
        update_job = Job.query.filter_by(uuid=job_uuid).one_or_none()
        if update_job is not None:
            if 'status' in data:
                update_job.status = data['status']
            if 'details' in data:
                update_job.details = data['details']
            update_job.date_updated = datetime.now()
            db.session.commit()
            return "", 204
        else:
            return "Not found", 404

    @app.route('/job/status/<job_uuid>', methods=['GET'])
    def job_status(job_uuid):
        app.logger.debug(f"Get job status, {job_uuid}")
        job = Job.query.filter_by(uuid=job_uuid).one_or_none()
        if job is not None:
            return jsonify(
                {
                    'date_created': job.date_created,
                    'date_updated': job.date_updated,
                    'status': job.status,
                    'details': job.details,
                    'body': job.body
                }
            ), 200
        else:
            return "", 404