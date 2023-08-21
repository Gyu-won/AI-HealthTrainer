var totalSet, doneSet, mins, secs, storeMin, storeSec, interval, camera_interval;
var prev_feedback = "";
let synth = speechSynthesis;
var video = document.getElementById('camera-viewer');
var sets = video.getAttribute('data-sets');
var reps = video.getAttribute('data-reps');
var rest = video.getAttribute('data-rest');
video.src = "/video_feed?set=" + sets + "&reps=" + reps + "&rest=" + rest;

function countdown() {
    if (secs > 0) {
        secs--;
    } else if (mins > 0) {
        mins--;
        secs = 59;
    } else {
        clearInterval(interval);
        console.log("end");
        return;
    }
    document.getElementById("mins").innerText = String(mins);
    document.getElementById("seconds").innerText = String(secs);
}


function fetchFirst() {   
    totalSet = parseInt(sets);
    console.log(totalSet);
    doneSet = 1;
    mins = Math.floor(parseInt(rest) / 60);
    secs = parseInt(rest) % 60;
    storeMin = mins;
    storeSec = secs;

    document.getElementById("set-num").innerText = doneSet + "/" + totalSet;
    document.getElementById("mins").innerText = String(mins);
    document.getElementById("seconds").innerText = String(secs);
}
  

function fetchData() {
    fetch("/get_feedback/")
        .then(response => response.json())
        .then(data => {
            const userInfoElement = document.getElementById("feedback");
            var feedback_text = data.textData
            userInfoElement.innerHTML = `
                ${feedback_text}<br>
            `;
            
            if (feedback_text != prev_feedback){
                prev_feedback = feedback_text;

                if (feedback_text === "Rest") {
                    console.log(feedback_text);
                    interval = setInterval(countdown, 1000);
                } else if (feedback_text === "Rest time is over, Let's workout") {
                    console.log(feedback_text);
                    clearInterval(interval);
                    mins = storeMin;
                    secs = storeSec;
                    document.getElementById("mins").innerText = String(mins);
                    document.getElementById("seconds").innerText = String(secs);

<<<<<<< HEAD
                    var temp = document.getElementById("set-num");
                    temp.innerText =String(parseInt(temp.innerText) + 1) + "/" + totalSet;
=======
                    var currentSet = parseInt(document.getElementById("set-num").innerText.split("/")[0]);
                    document.getElementById("set-num").innerText = (currentSet + 1) + "/" + totalSet;
>>>>>>> 7ceb90ab9000e37cb670af51491bcc3d3db9dcfa
                } else if (feedback_text === "All sets is done, congratulation!") {
                    console.log(feedback_text);
                    reqRedirect();
                }

                return textToSpeech(feedback_text);
            } 

        })
        .catch(error => {
            console.error("Error fetching data:", error);
        });
}

function reqRedirect() {
    fetch('/completion/')
    .then(response => {
        clearInterval(camera_interval);
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        return response.text();
    })
    .then(html => {
        document.open();
        document.write(html);
        document.close();
    })
    .catch(error => console.error('Error:', error));
}

function textToSpeech(text) {
    console.log("call textToSpeech");
    let utterance = new SpeechSynthesisUtterance(text);
    utterance.lang = 'en'
    synth.speak(utterance);
    
}

fetchFirst();
<<<<<<< HEAD
camera_interval = setInterval(fetchData, 100);
=======
console.log(totalSet);
setInterval(fetchData, 300);
>>>>>>> 7ceb90ab9000e37cb670af51491bcc3d3db9dcfa

