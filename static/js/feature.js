

function myFunction(id) {
  var panel = document.getElementById(id);
  console.log(id)
  if (panel.style.display == "block") {
    panel.style.display = "none";
  } else {
    panel.style.display = "block";
  }
}