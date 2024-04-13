// Select the group element by its ID
var map = document.getElementById('World');

// Add an event listener to the group element
map.addEventListener('click', function (event) {
    // Access the ID of the specific SVG element that was clicked
    var svgID = event.target.id;
    // Display the ID in the console   
    if (svgID == '')
        console.log("Russia");
    else
        console.log(svgID);
});

// Function to load the Budget Your Trip widget
function loadBudgetYourTripWidget() {
    var script = document.createElement('script');
    script.src = 'https://widget.budgetyourtrip.com/location-widget-js/2643743&hidebudgetstyles=1';
    script.async = true;
    document.getElementById('averageCost').appendChild(script);
}

// Call the function to load the widget
loadBudgetYourTripWidget();