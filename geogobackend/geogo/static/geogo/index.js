//var parser = new DOMParser();
//var map = document.getElementById("World");


// Select the group element by its ID
var group = document.getElementById('World');

// Add an event listener to the group element
group.addEventListener('click', function(event) {
    // Access the ID of the specific SVG element that was clicked
    var svgID = event.target.id;
    // Display the ID in the console
    console.log(svgID);
});
