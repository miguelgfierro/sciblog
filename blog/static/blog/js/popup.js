function onPopupOpen() {
    $("#modal-content").css("display", "flex");
    $("#FirstName").focus();
}

function onPopupClose() {
    $("#modal-content").hide(); //equivalent to CSS display:none
    lastFocus.focus();
}

var lastFocus;
var delay = 3000;

setTimeout(function () {
    lastFocus = document.activeElement;
    onPopupOpen();
}, delay);

$(".close-button").on("click", function () {
    onPopupClose();
});