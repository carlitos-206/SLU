function missingEmail(){
  alert("Email not available, Call or Text your manager.");
}
function featureNotAvailable(){
  alert("Feature Unavailable.");
}
function menuLimits(){
  var cafeName = document.getElementById("cafeName").textContent;
  console.log(cafeName);
  if(cafeName != "Bluebill"){
    alert("Menu not available for this cafe.")
    document.getElementsByClassName("nav-link").setAttribute("href", "javascript:void(0)");

  }else{
    var route_name = getElementsByClassName("nav-link").textContent.toLowerCase();
    var route = document.getElementsByClassName("nav-link");
    route.href = String(route_name);
  } 
}
function dontDrop(){
  var cafeName = document.getElementById("cafeName").textContent;
  var dropMenu = document.getElementById("drop-1");
  if(cafeName != "Bluebill"){
    dropMenu.style.display = "none";
  }
}