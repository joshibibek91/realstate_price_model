function getBathValue() {
  var uiBathrooms = document.getElementsByName("uiBathrooms");
  for (var i in uiBathrooms) {
    if (uiBathrooms[i].checked) {
      return parseInt(i) + 1;
    }
  }
  return -1; // Invalid Value
}

function getBHKValue() {
  var uiBHK = document.getElementsByName("uiBHK");
  for (var i in uiBHK) {
    if (uiBHK[i].checked) {
      return parseInt(i) + 1;
    }
  }
  return -1; // Invalid Value
}

function onClickedEstimatePrice() {
  console.log("Estimate price button clicked");
  var sqft = document.getElementById("uiSqft");
  var bhk = getBHKValue();
  var bathrooms = getBathValue();
  var location = document.getElementById("uiLocations");
  var estPrice = document.getElementById("uiEstimatedPrice");

  var url = "/predict_home_price"; // Use relative URL for deployment compatibility

  $.post(
    url,
    {
      total_sqft: parseFloat(sqft.value),
      bhk: bhk,
      bath: bathrooms,
      location: location.value,
    },
    function (data, status) {
      console.log(data.estimated_price);
      var priceElement = estPrice.querySelector(".result-price");
      if (priceElement) {
        priceElement.textContent = data.estimated_price.toString() + " Lakh";
        estPrice.classList.add("show");
      } else {
        estPrice.innerHTML =
          '<div class="result-content"><span class="result-label">Estimated Price</span><h2 class="result-price">' +
          data.estimated_price.toString() +
          " Lakh</h2></div>";
        estPrice.classList.add("show");
      }
      console.log(status);
    }
  );
}

function onPageLoad() {
  console.log("document loaded");
  var url = "/get_location_names"; // Use relative URL for deployment compatibility
  $.get(url, function (data, status) {
    console.log("got response for get_location_names request");
    if (data) {
      var locations = data.locations;
      var uiLocations = document.getElementById("uiLocations");
      $("#uiLocations").empty();
      for (var i in locations) {
        var opt = new Option(locations[i]);
        $("#uiLocations").append(opt);
      }
    }
  });
}

window.onload = onPageLoad;
