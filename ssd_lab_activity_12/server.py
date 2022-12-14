import os
from flask import Flask, render_template, request, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import (
    login_required,
    login_user,
    UserMixin,
    LoginManager,
    logout_user,
    login_required,
)
from sqlalchemy.sql import func

basedir = os.path.abspath(os.path.dirname(__file__))
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///" + os.path.join(
    basedir, "database.db"
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SECRET_KEY"] = "login-secret"
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)


class User(UserMixin, db.Model):
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(80), primary_key=True, unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __repr__(self):
        return f"<User {self.name}>"

    def get_id(self):
        return self.email


@app.route("/user/signup", methods=["POST"])
def signup():
    if request.method == "POST":
        req = request.get_json()
        name = req["name"]
        password = req["password"]
        email = req["email"]
        check = User.query.filter_by(email=email).first()
        if check is None:
            db.session.add(User(name=name, email=email, password=password))
            db.session.commit()
            return "SIGNUP SUCCESSFULL"
        else:
            return "ALREADY PRESENT"


@app.route("/user/signin", methods=["POST"])
def signin():
    if request.method == "POST":
        req = request.get_json()
        password = req["password"]
        email = req["email"]
        check = User.query.filter_by(email=email).first()
        if check is not None:
            if check.password == password:
                login_user(check)
                return "LOGGED SUCCESSFULLY"
            else:
                return "INCORRECT PASSWORD"
        else:
            return "NO USER"


@app.route("/user/signout", methods=["POST"])
@login_required
def signout():
    if request.method == "POST":
        logout_user()
        return "LOGGED OUT SUCCESFFULLY"


if __name__ == "__main__":
    app.run(host="127.0.0.1", port="5000", debug=True)
