from flask import Flask,request
from flask_socketio import emit,join_room,leave_room
from init import app,SocketApp
users=[]

@SocketApp.on("connect")
def socket():
    users.append(request.sid)
    print("dididdidi")
    join_room("room1")
@SocketApp.on("videocall")
def videocall():
    emit("videocall",include_self=False,to="room1")
    print(users)
@SocketApp.on("disconnect")
def disconnect():
    users.remove(request.sid)
    leave_room("room1")
@SocketApp.on("candidate")
def candidate(candidate):
    emit("candidate",candidate,include_self=False,to="room1")
@SocketApp.on("offer")
def offer(offer):
    emit("offer",offer)
@SocketApp.on("answer")
def answer(answer):
    emit("answer",answer)
SocketApp.run(app,debug=True)
