from flask import Flask
from data_loader import DataLoader
from models import db, Cities, Routes

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:tajnehaslo@localhost:5555/public_transport'

db.init_app(app)
with app.app_context():
    db.create_all()
    db.session.commit()

    loader = DataLoader(db, 'routes-', 'cities.csv')
    loader.load()

@app.route("/")
def hello():
    user = Routes(route_id="C", short_name="imie",description='imejl', city=1)
    db.session.add(user)
    db.session.commit()
    return "XXXHddsdadadsaa!"