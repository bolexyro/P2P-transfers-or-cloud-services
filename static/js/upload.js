// let xhr = new XMLHttpRequest();
function uploadFile() {
    const fileInput = document.getElementById('file');
    const progressBar = document.getElementById('upload-progress');

    const formData = new FormData();
    formData.append('file', fileInput.files[0]);

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
