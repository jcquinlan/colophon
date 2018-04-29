var fileTypeValidators = {
    image: imageFileValidation,
    asset: assetValidation
};

var fileTypeParams = {
    image: {
        file_type: 'image/jpeg'
    },
    asset: {
        file_type: 'application/x-indesign'
    }
};

function imageFileValidation(files) {
    if (files.length > 3) {
        throw 'You may only upload three images';
    }
}

function assetValidation() {
    return;
}

function handleFileUpload(fileType, fileInput, successCallback, errorCallback) {
    fileInput.onchange = function(){
        var files = fileInput.files;

        if (!files.length) {
            return alert("No file selected.");
        }

        try {
            fileTypeValidators[fileType](files);
        } catch (e) {
            errorCallback(e);
            return;
        }

        for (var i = 0; i < files.length; i++) {
            try {
                getSignedRequest(files[i], files[i].name, fileType, successCallback);
            } catch (error) {
                errorCallback(error)
            }
        }
    };
}

function getSignedRequest(file, fileName, fileType, successCallback) {
    var xhr = new XMLHttpRequest();

    xhr.open("GET", "/sign_s3?file_name=" +
        encodeURIComponent(fileName) +
        buildUrlParams(fileType)
    );

    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4) {
            if (xhr.status === 200) {
                var response = JSON.parse(xhr.responseText);
                try {
                    uploadFile(file, response.data, response.url, successCallback);
                } catch (error) {
                    throw error;
                }
            } else {
                throw "Could not get signed URL.";
            }
        }
    };

    xhr.send();
}

function uploadFile(file, s3Data, url, successCallback){
    var xhr = new XMLHttpRequest();
    xhr.open("POST", s3Data.url);

    var postData = new FormData();

    for(key in s3Data.fields) {
        postData.append(key, s3Data.fields[key]);
    }

    postData.append('file', file);

    xhr.onreadystatechange = function() {
        if (xhr.readyState === 4) {
            if (xhr.status === 200 || xhr.status === 204) {
                successCallback(url);
            }

            else {
                throw "Could not upload file.";
            }
        }
    };

    xhr.send(postData);
}

function buildUrlParams(fileType) {
    var paramObject = fileTypeParams[fileType];
    var esc = encodeURIComponent;
    var formattedParams = Object.keys(paramObject)
        .map(function(key) {
            return esc(key) + '=' + esc(paramObject[key]);
        })
        .join('&');

    return formattedParams ? '&' + formattedParams : '';
}
