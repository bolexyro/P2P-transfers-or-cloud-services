var sender_id = Date.now();
document.querySelector("#sender-id").textContent = sender_id;
function CreateWebsocket(){
    var receiver_id = document.getElementById("receiver-id").value;
    console.log(receiver_id)
    ws = new WebSocket(`ws://localhost:8000/ws/${sender_id}/${receiver_id}`);
    console.log("This is ws: ", ws)
    ws.onmessage = function(event) {
        var messages = document.getElementById('messages')
        var message = document.createElement('li')
        var content = document.createTextNode(event.data)
        message.appendChild(content)
        messages.appendChild(message)
    };
}


function uploadFile() {
    const fileInput = document.getElementById('file');
    const progressBar = document.getElementById('upload-progress');
    const formData = new FormData(document.getElementById('upload-form'));

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
            const responseHtml = xhr.responseText;
            document.body.innerHTML = responseHtml;
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
