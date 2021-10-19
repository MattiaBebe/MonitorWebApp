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

//FUNZIONI PER IL CONTROLLO DEI BOTTONI E DELLA CATEGORIA IN TABELLA 

//FUNZIONE ISO 
  function check(){
    if(document.getElementById("IS2").checked == true){
      document.getElementById("IS2").checked = true;
      document.getElementById("XF").checked = false;
      document.getElementById("AVV").checked = false;
      document.getElementById("KTR").checked = false;
      //modifico il valore del testo categoria in IS2 per fare la selezione sulla tabella 
      var categoria = "IS2";
      document.getElementById("categoria").value = categoria;
      window.location.reload()
    }
  }

// FUNZIONE XF

function check2(){
  document.getElementById("XF").checked = true;
  if(document.getElementById("XF").checked == true){
    document.getElementById("IS2").checked = false;
    document.getElementById("AVV").checked = false;
    document.getElementById("KTR").checked = false;
    //modifico il valore di categoria in XF
    var categoria = "XF";
    document.getElementById("categoria").value = categoria;
    window.location.reload()
  }
}

//FUNZIONE AVVITATI 

function check3(){
  document.getElementById("AVV").checked = true;
  if(document.getElementById("AVV").checked == true){
    document.getElementById("IS2").checked = false;
    document.getElementById("XF").checked = false;
    document.getElementById("KTR").checked = false;
    //modifico il valore di categoria in AVV
    var categoria = "AVV";
    document.getElementById("categoria").value = categoria;
    window.location.reload()
  }
}

//FUNZIONE KTR

function check4(){
  document.getElementById("KTR").checked = true;
  if(document.getElementById("KTR").checked == true){
    document.getElementById("IS2").checked = false;
    document.getElementById("AVV").checked = false;
    document.getElementById("XF").checked = false;
    //modifico il valore di categoria in KTR
    var categoria = "KTR";
    document.getElementById("categoria").innerHTML = "ciao";
    window.location.reload()
  }
}