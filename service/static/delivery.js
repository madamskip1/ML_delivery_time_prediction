var emailArray = [];
var passwordArray = [];

function resetForm(){
  document.getElementById("formsStyle").reset();
}


function predictDelivery() {
    	
  // Get the data from each element on the form.
  const city = document.getElementById('txtCity');
  const delivery_company = document.getElementById('txtDeliveryCompany');
  const purchase_time = document.getElementById('txtPurchaseTime');
  const model = document.getElementById('txtModel');

  var inputs =[city, delivery_company, purchase_time, model];

  var everythingOK = true

  for (var i= 0; i < inputs.length; i++){
    if (inputs[i].value == ''){
      inputs[i].style.border = "3px solid red";
      everythingOK = false;;
    }
  }
  if (everythingOK == true){
    b = '{"city": "'+city.value+'", "delivery_company": '+delivery_company.value+', "purchase_timestamp": "'+purchase_time.value+'", "model": '+model.value+"}"
    window.location = '/delivery?data='+b;
  } 
}
