document.body.style.border = "5px solid red";

document.onkeyup = function(e) {
  if (e.which == 192) {
    console.log("clicked")
  }
}
