from flask import render_template,redirect,url_for,Blueprint,request,flash,session
import models
from werkzeug.security import generate_password_hash,check_password_hash
import db
import secrets
import datetime
auth=Blueprint("auth",__name__)

@auth.route("/register",methods=["POST","GET"])
def register():
    if request.method=="GET":
        return render_template("register.html")
    else:
        login=request.form.get("login")
        password=request.form.get("password")
        password2=request.form.get("password2")
        if login==None or login.strip()=="":
            flash("Enter login")
            return redirect(url_for("auth.register"))
        if password==None or password.strip()=="":
            flash("Enter password")
            return redirect(url_for("auth.register"))
        if password2!=password:
            flash("Passwords do not match")
            return redirect(url_for("auth.register"))
        if models.User.query.filter_by(login=login).first():
            flash("Login taken")
            return redirect(url_for("auth.register"))
        else:
            hash_pass=generate_password_hash(password)
            session["login"]=login
            new_user=models.User(login=login,password=hash_pass)
            db.db.session.add(new_user)
            db.db.session.commit()
            return redirect(url_for("views.main"))
        
@auth.route("/login",methods=["GET","POST"])
def login():
    if request.method=="GET":
        return render_template("login.html")
    else:
        login=request.form.get("login")
        password=request.form.get("password")
        if login==None or login.strip()=="":
            flash("Enter login")
            return redirect(url_for("auth.login"))
        if password==None or password.strip()=="":
            flash("Enter password")
            return redirect(url_for("auth.login"))
        user=models.User.query.filter_by(login=login).first()
        if not user:
            flash("Wrong login or password")
            return redirect(url_for("auth.login"))
        elif check_password_hash(user.password,password)==False:
            return redirect(url_for("auth.login"))
        else:
            session["login"]=login
            return redirect(url_for("views.main"))