var sender_id = Date.now();
document.querySelector("#sender-id").textContent = sender_id;
function CreateWebsocket(){
    var receiver_id = document.getElementById("receiver-id").value;
    var currentUrl = window.location.hostname;
    ws = new WebSocket(`ws://${currentUrl}:8000/ws/${sender_id}/${receiver_id}`);
    console.log("This is ws: ", ws)
    ws.onmessage = function(event) {
        var message = event.data
        
        try{
            // Attempt to parse the mesasage as JSON
            var jsonMessage = JSON.parse(message);

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
    document.getElementById("stream-button").style.display = "none";
    document.getElementById("download-button").style.display = "none"
}

// Function to handle the stream button click
function streamFile() {
    // Redirect to the stream link
    window.open(document.getElementById("stream-button").href)
    // window.location.href = 
    document.getElementById("stream-button").style.display = "none";
    document.getElementById("download-button").style.display = "none"
}



function uploadFile() {
    const fileInput = document.getElementById('file');
    const progressBar = document.getElementById('upload-progress');
    const formData = new FormData(document.getElementById('upload-form'));
    const fileName = fileInput.files[0].name;
    console.log('File Name:', fileName);
    const xhr = new XMLHttpRequest();

    xhr.upload.onprogress = function (event) {
        if (event.lengthComputable) {
            const percentComplete = (event.loaded / event.total) * 100;
            progressBar.style.width = percentComplete + '%';
            document.getElementById("progress_number").innerHTML = percentComplete.toFixed(2) + '%';
        }
    };

    xhr.onload = function () {
        if (xhr.status === 200) {
            console.log('File uploaded successfully!');
            // const responseHtml = xhr.responseText;
            // document.body.innerHTML = responseHtml;
            ws.send(fileName);
        } else {
            console.error('Error uploading file:', xhr.statusText);
        }
    };

    xhr.open('POST', '/upload-files', true);
    xhr.send(formData);
}


function cancelUpload() {
    // Add logic to cancel the upload if needed
    if (xhr && xhr.readyState !== 4) {
        // Abort the upload
        xhr.abort();
        console.log('Upload canceled!');
    } else {
        console.log('No upload in progress to cancel.');
    }
    // alert("Upload canceled!");
}
