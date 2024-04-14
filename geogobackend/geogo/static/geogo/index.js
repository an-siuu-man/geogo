// Select the group element by its ID
var map = document.getElementById('World');

var origin = document.getElementById('originAirportInput');
var destination = document.getElementById('destinationAirportInput');
var visa = document.getElementById('visaInput');

document.addEventListener('DOMContentLoaded', function () {
    form = document.getElementById('formsub');
    form.reset();
})
// Add an event listener to the group element
map.addEventListener('click', function (event) {
    // Access the ID of the specific SVG element that was clicked
    var svgID = event.target.id;
    // Display the ID in the console 
    if (svgID == '') {
        console.log("Russia");
        if(origin.value == ''){
            origin.value = "Russia";
            visa.value = "Russia";
        }
        else {
            destination.value = "Russia";
        }
    }
    else {
        console.log(svgID);
        if(origin.value == ''){
            origin.value = svgID;
            visa.value = svgID;
        }
        else {
            destination.value = svgID;
        }
    }
});

const today = new Date().toISOString().split('T')[0];
document.getElementById('getDepartDate').setAttribute('min', today);

document.getElementById('formsub').addEventListener('submit', function () {
    // Display the loading overlay when the form is submitted
    document.getElementById('loading').style.display = 'inline-block';

});