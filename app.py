from flask import Flask, redirect, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://cwkuktrakwieja:016c01c9c5a823a9556c63f0660d9f805aa7b614ab525daf6ad30dead62b2fbb@ec2-3-219-229-143.compute-1.amazonaws.com:5432/d1scl9b4lktjgj'

db = SQLAlchemy(app)


class IPs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ip = db.Column(db.Text)


# Server-Side
@app.route("/", methods=["GET"])
def home():
    x_ip = request.environ.get('HTTP_X_FORWARDED_FOR', request.remote_addr)
    ipTable = IPs(ip=x_ip)

    db.session.add(ipTable)
    db.session.commit()

    return redirect("https://www.youtube.com/", code=302)


def run():
    app.run(host='0.0.0.0', port=8080)
