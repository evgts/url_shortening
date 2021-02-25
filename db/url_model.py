from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from cfg import db_uri

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
db = SQLAlchemy(app)


class Urls(db.Model):
    __tablename__ = 'urls'

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(2500), nullable=False)
    url_code = db.Column(db.String(100), nullable=False)
    short_url = db.Column(db.String(100), nullable=False)


if __name__ == '__main__':
    # To create the DB and the table run:
    # python db\url_model.py
    db.create_all()
