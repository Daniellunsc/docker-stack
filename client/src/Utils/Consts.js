function getCookie(cookieName){
    var value = "; " + document.cookie;
    var parts = value.split("; " + cookieName + "=");
    if (parts.length == 2) return parts.pop().split(";").shift();
}

export const csrf_cookie = getCookie('csrf_access_token')