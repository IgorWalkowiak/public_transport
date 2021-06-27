from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:tajnehaslo@localhost:5555/public_transport'
db = SQLAlchemy(app)

class Routes(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    short_name = db.Column(db.String(10), nullable=False)
    description = db.Column(db.String(2000), nullable=False)
    city = db.Column(db.Integer, nullable=False)


db.create_all()
db.session.commit()

@app.route("/")
def hello():
    user = Routes(short_name="imie",description='imejl', city=1)
    db.session.add(user)
    db.session.commit()
    return "XXXHddsdadadsaa!"