var lastFocus;
var delay = 3000;

setTimeout(function () {
    lastFocus = document.activeElement;
    console.log("Waiting for pop-up...");
    $('#overlay').addClass('blur-in');
    $('.pop-up').fadeIn(1000).css("display", "flex");
}, delay);


$('.close-button').click(function (e) {
    $('.pop-up').fadeOut(700);
    $('#overlay').removeClass('blur-in');
    $('#overlay').addClass('blur-out');
    e.stopPropagation();
});

