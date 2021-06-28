from flask import Flask, jsonify
from data_loader import DataLoader
from models import db, Cities, Routes

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:tajnehaslo@localhost:5555/public_transport'

db.init_app(app)
with app.app_context():
    db.drop_all()
    db.create_all()
    db.session.commit()

    loader = DataLoader(db, 'routes-', 'cities.csv')
    loader.load()

@app.route("/")
def hello():
    return "No hej!<br> Leć do 127.0.0.1:5000/public_transport/city/wroclaw/routes albo <br>127.0.0.1:5000/public_transport/cities"

@app.route("/public_transport/city/<city>/routes")
def city_route(city):
    routes = Routes.query.join(Cities, Routes.city == Cities.id).filter(Cities.name == city).all()
    return jsonify([i.serialize for i in routes])

@app.route("/public_transport/cities")
def cities():
    return jsonify([i.serialize for i in Cities.query.all()])
