from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Plant(db.Model, SerializerMixin):
    __tablename__ = 'plants'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    image = db.Column(db.String(100), nullable=False, default='default.jpg')
    price = db.Column(db.Float, nullable=False, default=0.0)

    id = db.Column(db.Integer, primary_key=True)

    def __repr__(self):
      return f"Plant('{self.name}')"