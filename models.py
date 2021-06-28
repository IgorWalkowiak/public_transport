from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Cities(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(50), nullable=False)

    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'city_name': self.name
        }

class Routes(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    route_id = db.Column(db.String(10), nullable=False)
    short_name = db.Column(db.String(10), nullable=True)
    description = db.Column(db.String(2000), nullable=False)
    city = db.Column(db.Integer, db.ForeignKey('cities.id'), nullable=False)

    @property
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'route_id': self.id,
            'short_name': self.short_name,
            'description': self.description
        }

