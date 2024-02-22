let sender_id = Date.now();
sender_id = sender_id.toString().slice(-5)
document.querySelector("#sender-id").textContent = sender_id;

function CreateWebsocket(){
    let receiver_id = document.getElementById("receiver-id").value;
    let currentUrl = window.location.hostname;

    ws = new WebSocket(`ws://${currentUrl}/ws/${sender_id}/${receiver_id}`);
    console.log("This is ws: ", ws)

    ws.onmessage = function(event) {
        let message = event.data
        console.log("message from sender is", message);
        try{
            var jsonMessage = JSON.parse(message);
            console.log("jsonmessage is", jsonMessage)
            // Show both download and stream buttons
            document.getElementById("stream-button").style.display = "inline-block";
            document.getElementById("download-button").style.display = "inline-block";

            // Set the href attributes for download and stream buttons
            document.getElementById("download-button").href = jsonMessage.download_link;
            document.getElementById("stream-button").href = jsonMessage.stream_link;

            }catch(e){
            // If parsing as JSON fails, treat it as a text message
            // Show only the download button
                document.getElementById("download-button").style.display = "inline-block";
                // Set the href attribute for the download button
                document.getElementById("download-button").href = message;
        }
        }

    };
function downloadFile() {
    // Redirect to the download link
    window.location.href = document.getElementById("download-button").href;
    // document.getElementById("stream-button").style.display = "none";
    // document.getElementById("download-button").style.display = "none"
}

// Function to handle the stream button click
function streamFile() {
    // Redirect to the stream link
    window.open(document.getElementById("stream-button").href)
    // window.location.href = 
    // document.getElementById("stream-button").style.display = "none";
    // document.getElementById("download-button").style.display = "none"
}


let xhr;    

function uploadFile() {
    const formData = new FormData(document.getElementById('upload-form'));
    const fileInput = document.getElementById('file');
    const files = fileInput.files;

    // const fileName = fileInput.files[0].name;
    // console.log('File Name:', fileName);
    const fileNames = Array.from(files).map(file => file.name);
    console.log("files sender is sending", fileNames);
    
    if (files.length === 0){
        alert("Please select a file.");
        return;
    }

    xhr = new XMLHttpRequest();
    xhr.open('POST', '/upload-files', true);

    xhr.upload.onprogress = function (event) {
        
        if (event.lengthComputable) {
            const progressBar = document.getElementById('upload-progress');
            const progressNumber = document.getElementById('progress_number');

            const percentComplete = (event.loaded / event.total) * 100;
            progressBar.style.width = percentComplete + '%';
            progressNumber.innerHTML = percentComplete.toFixed(2) + '%';
        }
    };

    xhr.onload = function () {
        if (xhr.status === 200) {
            alert('Upload successful!');
            resetProgressBarAndPercent();
            ws.send(fileNames);
        } else {
            alert('Upload failed. Status: ' + xhr.status);
        }
    };

    xhr.onerror = function() {
        alert('Error occurred while uploading the file.');
    };

    xhr.send(formData);
}

function resetProgressBarAndPercent(){
    document.getElementById('upload-progress').style.width = "0%";
    document.getElementById('progress_number').innerHTML = "0%";
}

function cancelUpload() {
    if (xhr) {
        xhr.abort();
        alert('Upload canceled.');
        resetProgressBarAndPercent();
    } else {
        alert('No upload in progress.');
    }
}
