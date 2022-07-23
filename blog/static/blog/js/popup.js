var lastFocus;
var delay = 3000; // Pop up delay in seconds
var cookieExpires = 0; // Expiration of cookie in days
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

