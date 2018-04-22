addCSRFTokenToAJAX();
setBaseUrl();

function addCSRFTokenToAJAX() {
    var csrftoken = getCookie('csrftoken');

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });
}

function setBaseUrl() {
    var baseUrls = {
        DEV: 'http://localhost:8000',
        PROD: 'https://www.colofont.com'
    }

    BASEURL = baseUrls[CONTEXT];
}
