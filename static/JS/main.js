let video=document.getElementById("video")
let videocall=document.getElementById("videocall")
let stream=null

videocall.addEventListener("click",async function () {
    stream=await navigator.mediaDevices.getUserMedia({
        video:true,
        audio:false
    })
    console.log(stream)
    console.log(video)
    video.srcObject=stream
})