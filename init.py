from flask import session
from flask import Flask,Blueprint
import views
import auth
from db import db
app=Flask("app")
app.config["SECRET_KEY"]="login"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
app.register_blueprint(views.views)
app.register_blueprint(auth.auth)
db.init_app(app)
with app.app_context():
    db.create_all()