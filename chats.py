from flask import Flask,render_template,redirect,Blueprint,session,request,url_for
import models
chats=Blueprint("chats",__name__)

@chats.route("/get_chats",methods=["POST","GET"])
def chat():
    if "login" in session:
        login=session["login"]
    else:
        return redirect(url_for("auth.register"))
    chats_user=models.Chat_users.query.filter_by(user_login=login).all()
    if chats_user==None:
        return render_template("chats.html")
    else:
        chats=[]
        for i in chats_user:
            chat_name=models.Chat.query.filter_by(room_id=i.room_id).first()
            chats.append(chat_name)
        return render_template("chats.html",chats=chats)

@chats.route("/predict_login/<string:login>",methods=["POST",])
def predict_login(login):
    logins=models.User.query.all()
    match=[]
    for i in logins:
        if i.login.lower().startswith(login.lower()):
           match.append(i.login)
    return match 