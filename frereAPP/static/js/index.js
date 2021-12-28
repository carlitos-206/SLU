function menu() {
    var x = document.getElementById("myLinks");
    if (x.style.display === "block") {
      x.style.display = "none";
    } else {
      x.style.display = "block";
    }
  }

function missingEmail(){
  alert("Email not available, Call or Text your manager.");
}
function featureNotAvailable(){
  alert("Feature not available yet.");
}