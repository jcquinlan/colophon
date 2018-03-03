function handleFileUpload(fileInput, successCallback, errorCallback) {
    fileInput.onchange = function(){
        var files = fileInput.files;

        if (!files.length) {
            return alert("No file selected.");
        }

        if (files.length > 3) {
            if (errorCallback) errorCallback('You may only upload three images');
            return;
        }

        for (var i = 0; i < files.length; i++) {
            getSignedRequest(files[i]);
        }
    };

    function getSignedRequest(file){
        var xhr = new XMLHttpRequest();

        console.log(file.type);

        xhr.open("GET", "/sign_s3?file_name=" +
            encodeURIComponent(file.name) +
            "&file_type=" +
            'application/x-indesign'
        );

        xhr.onreadystatechange = function() {
            if (xhr.readyState === 4) {
                if (xhr.status === 200) {
                    var response = JSON.parse(xhr.responseText);
                    uploadFile(file, response.data, response.url);
                }

                else {
                    errorCallback("Could not get signed URL.");
                }
            }
        };

        xhr.send();
    }

    function uploadFile(file, s3Data, url){
        var xhr = new XMLHttpRequest();
        xhr.open("POST", s3Data.url);

        var postData = new FormData();

        for(key in s3Data.fields){
            postData.append(key, s3Data.fields[key]);
        }

        postData.append('file', file);

        xhr.onreadystatechange = function() {
            if (xhr.readyState === 4) {
                if (xhr.status === 200 || xhr.status === 204) {
                    successCallback(url);
                }

                else {
                    errorCallback("Could not upload file.");
                }
            }
        };

        xhr.send(postData);
    }
}