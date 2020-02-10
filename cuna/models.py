import flask_sqlalchemy

db = flask_sqlalchemy.SQLAlchemy()

class Job(db.Model):
    __tablename__ = 'jobs'
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime)
    date_updated = db.Column(db.DateTime)
    body = db.Column(db.Text)
    uuid = db.Column(db.Text)
    status = db.Column(db.Text)
    details = db.Column(db.Text)
