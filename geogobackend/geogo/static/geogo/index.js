document.addEventListener('DOMContentLoaded', function () {
    form = document.getElementById('formsub');
    form.reset();

    // Select the group element by its ID
    var map = document.getElementById('World');

    var origin = document.getElementById('originAirportInput');
    var destination = document.getElementById('destinationAirportInput');
    var visa = document.getElementById('visaInput');
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

    document.getElementById('formsub').addEventListener('submit', function () {
        // Display the loading overlay when the form is submitted
        document.getElementById('loading').style.display = 'inline-block';

});
    // Get today's date
const today = new Date();

// Set the minimum value of the date input to today
document.getElementById('getDepartDate').setAttribute('min', today.toISOString().split('T')[0]);

// Create a new Date object representing tomorrow
const tomorrow = new Date(today);
tomorrow.setDate(today.getDate() + 1);

// Format the date to 'YYYY-MM-DD' (required by input type="date")
const tomorrowFormatted = tomorrow.toISOString().split('T')[0];

// Set the value of the date input to tomorrow's date
document.getElementById('getDepartDate').value = tomorrowFormatted;

})