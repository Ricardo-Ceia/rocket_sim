const WebSocket = require('ws');


//Get the rocket element 
const rocket = document.getElementById("rocketship")

// Create WebSocket connection.
const socket = new WebSocket("ws://localhost:65432");
const pixels_per_meter = 2

//Signal on Connection
socket.onopen = ()=>{
    console.log("Connected to Websocket Server");
} 


// Listen for messages
socket.addEventListener("message", (event) => {
    message = event.data.toString();
    height = parseFloat(message)
    if(!isNaN){
        const rocketship_position = height*pixels_per_meter

        rocket.style.bottom = `&{rocketship_position}px`
        console.log("Altitude:",height)
    }
});