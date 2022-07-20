var lastFocus;
var delay = 3000; // Pop up delay in seconds
var cookieExpires = 1; // Expiration of cookie in days
var popupShown = Cookies.get('popUpSciblog');

if (!!popupShown) {
    console.log("No cookie found, showing pop up")
    setTimeout(function () {
        lastFocus = document.activeElement;
        console.log("Waiting for pop-up...");
        $('#overlay').addClass('blur-in');
        $('.pop-up').fadeIn(1000).css("display", "flex");
        Cookies.set('popUpSciblog', 'yes', {
            expires: cookieExpires
        });
    }, delay);
} else {
    console.log("Cookie found, no pop up shown")
}

$('.close-button').click(function (e) {
    $('.pop-up').fadeOut(700);
    $('#overlay').removeClass('blur-in');
    $('#overlay').addClass('blur-out');
    e.stopPropagation();
});

