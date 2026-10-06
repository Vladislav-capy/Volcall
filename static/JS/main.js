let socket=io()
let myvideo=document.getElementById("video")
let videocall=document.getElementById("videocall")
let stream=null
let othervideo=document.getElementById("video2")
let otherstream=null
let peerconnection=null
let callsound=new Audio("static/media/call.mp3")
let accept=document.getElementById("accept")
callsound.loop=true

videocall.addEventListener("click",async function () {
    socket.emit("videocall")
    await camera_on()
    //await callsound.play()
    await create_peerconnection()
})


async function create_peerconnection(){
    peerconnection=new RTCPeerConnection({
        iceServers:[{
            urls:"stun:stun.l.google.com:19302"
        }]
    })
    for(let track of stream.getTracks()){
        peerconnection.addTrack(track,stream)
    }
    peerconnection.ontrack=function(bytes){
        
        othervideo.srcObject=bytes.streams[0]
    }
    peerconnection.onicecandidate=function(bytes){
        if(bytes.candidate){
            socket.emit("candidate",bytes.candidate)
        }
    }
}
async function create_offer(){
    let offer=await peerconnection.createOffer()
    await peerconnection.setLocalDescription(offer)
    socket.emit("offer",offer)
}

async function camera_on(){
        stream=await navigator.mediaDevices.getUserMedia({
        video:true,
        audio:true
    })
    myvideo.srcObject=stream
}

socket.on("videocall",function(){

    accept.hidden=false
})
accept.addEventListener("click",async function() {
    await camera_on()
    await create_peerconnection()
    await create_offer()
    accept.hidden=true
    
})
socket.on("candidate",async function(candidate){
    try{
        await peerconnection.addIceCandidate(candidate)
    }
    catch(e){
        console.log(e)
    }
})
socket.on("offer",async function (offer) {
    await peerconnection.setRemoteDescription(offer)
    let answer=peerconnection.createAnswer()
    await peerconnection.setLocalDescription(answer)
    socket.emit("answer",answer)
})
socket.on("answer",async function (answer) {
    await peerconnection.setRemoteDescription(answer)
})