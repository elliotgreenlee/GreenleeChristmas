from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Gift(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    image_url = db.Column(db.String(200), nullable=False)
    product_url = db.Column(db.String(200), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    