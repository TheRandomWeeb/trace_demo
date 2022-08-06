from flask import Flask, redirect, request, render_template
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://mrgofcieaevokn:79860ece3e6520c0b1637a789dbc877de7dfc07d414b81170815d514d28e8b2a@ec2-18-214-35-70.compute-1.amazonaws.com:5432/d2dr62o56dm2h8'

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

    # return redirect("https://www.youtube.com/watch?v=dQw4w9WgXcQ", code=302)
    return render_template('page.html')


def run():
    app.run(host='0.0.0.0', port=8080)
