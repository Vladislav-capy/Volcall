from flask import Flask,redirect,render_template,request,Blueprint
views=Blueprint("views","views")
@views.route("/main",methods=["GET",])
def main():
    return render_template("main.html")