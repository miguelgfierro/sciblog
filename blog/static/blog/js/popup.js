// Cookie functions
function createCookie(name, value, days) {
    if (days) {
        var date = new Date();
        date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
        var expires = "; expires=" + date.toGMTString();
    }
    else var expires = "";
    document.cookie = name + "=" + value + expires + "; path=/";
}

function readCookie(name) {
    var nameEQ = name + "=";
    var ca = document.cookie.split(';');
    for (var i = 0; i < ca.length; i++) {
        var c = ca[i];
        while (c.charAt(0) == ' ') c = c.substring(1, c.length);
        if (c.indexOf(nameEQ) == 0) return c.substring(nameEQ.length, c.length);
    }
    return null;
}

function eraseCookie(name) {
    createCookie(name, "", -1);
}


// Pop up functions
var lastFocus;
var delay = 3000; // Pop up delay in seconds
var cookieExpires = 20; // Expiration of cookie in days
var cookieName = "popUpSciblog";
var popupShown = readCookie(cookieName);

if (popupShown == null) {
    console.log("No cookie found, showing pop up")
    setTimeout(function () {
        lastFocus = document.activeElement;
        console.log("Waiting for pop-up...");
        $('#overlay').addClass('blur-in');
        $('.pop-up').fadeIn(1000).css("display", "flex");
        var date = new Date();
        createCookie(cookieName, date.toGMTString(), 1)
    }, delay);
} else {
    console.log("Cookie found: " + popupShown + " no pop up shown")
}

$('.close-button').click(function (e) {
    $('.pop-up').fadeOut(700);
    $('#overlay').removeClass('blur-in');
    $('#overlay').addClass('blur-out');
    e.stopPropagation();
});

