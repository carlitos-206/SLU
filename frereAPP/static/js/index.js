function missingEmail(){
  alert("Email not available, Call or Text your manager.");
}
function featureNotAvailable(){
  alert("Feature Unavailable.");
}

function scheduleLimits(){
  var cafeName = document.getElementById("cafeNameJS").textContent;
  var blocked = document.getElementById("schedule_js");
  if(cafeName != "Bluebill"){
    blocked.setAttribute("href", "javascript:void(0)");
    alert("Schedule not available for this cafe. Contact your manager.");
  }
}

function menuLimits(){
  var cafeName = document.getElementById("cafeNameJS").textContent;
  var blocked = document.getElementById("menu_drop_js");
  var dropMenu = document.getElementById("drop-1"); 
  console.log(cafeName);
  if(cafeName != "Bluebill"){
      blocked.setAttribute("href", "javascript:void(0)");
      dropMenu.setAttribute("style", "display:none");
      alert("Menu not available for this cafe.");
      }
  }