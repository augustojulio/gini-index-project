from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class GiniIndex(db.Model):
    __tablename__ = 'gini_index'
    id = db.Column(db.Integer, primary_key=True)
    state = db.Column(db.String(100))
    city = db.Column(db.String(100))
    year = db.Column(db.Integer)
    gini_value = db.Column(db.Float)
