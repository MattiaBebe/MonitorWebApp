/* Toggle between adding and removing the "responsive" class to topnav when the user clicks on the icon */
function myFunction() {
    var x = document.getElementById("myTopnav");
    if (x.className === "topnav") {
      x.className += " responsive";
    } else {
      x.className = "topnav";
    }
  }



  function controlloScaduto(){
    var data = document.getElementById("data");
    data.style.background(red)
    if (data.className === ""){
       data.className += "scaduto";
    }
  }

  function Malert(){
    var data = document.getElementById("data");
    data.className += "scaduto";
    if (data.className === ""){
       data.className += "scaduto";
    }
  }