from django.shortcuts import render
from django import forms
from datetime import datetime
from .api.gptAPI import generateResponse
from .api.airportCodes import city_codes
from .api.serpapigit import getFlightDetails
# Create your views here.
def index(request):
    return render(request, 'geogo/index.html')

def results(request):

    if request.method == 'POST':

        originAirport = request.POST['originAirport']
        destinationAirport = request.POST['destinationAirport']
        getVisa = request.POST['getVisa']

        somedate = request.POST.get('somedate')
        # 'somedate' will contain the date in 'YYYY-MM-DD' format
        formatted_date = ''
        # Now you can convert the date string to a datetime object if needed
        if somedate:
            somedate_obj = datetime.strptime(somedate, '%Y-%m-%d')
            # somedate_obj is a datetime object
            
            # Format the datetime object to 'YYYY-MM-DD' format
            formatted_date = somedate_obj.strftime('%Y-%m-%d')
        else:
            formatted_date = '2024-04-16'
        codes = city_codes()
        origin = 'Unknown'
        destination = 'Unknown'
        visa = 'Unknown'
        if originAirport in codes[0].keys():
            origin = codes[0][originAirport]
        if destinationAirport in codes[0].keys():
            destination = codes[0][destinationAirport]
        if getVisa in codes[1].keys():
            visa = getVisa

        same_airport = False
        invalid_airport = False
        invalid_visa = False

        # Error Case 1 
        if origin == destination:
            same_airport = True
            invalid_airport = False
            invalid_visa = False

            return render(request, 'geogo/index.html', {
                'same_airport': same_airport,
                'invalid_airport':invalid_airport,
                'invalid_visa': invalid_visa
                })



        # response = generateResponse(f'top 10 tourist locations in {origin} in a list with one line descriptions').split('\n')

        # locations = []
        # for i in response:
        #     if i != '':
        #         locations.append(i)
        # Get the selected option from the dropdown menu
        # For demonstration purposes, I'm just returning the selected option as part of the response

        locations = [
    "Eiffel Tower: Iconic wrought-iron lattice tower offering sweeping views of Paris.",
    "Louvre Museum: World's largest art museum and historic monument in Paris.",
    "Notre-Dame Cathedral: Famed Gothic cathedral known for its flying buttresses & gargoyles.",
    "Montmartre: Hill featuring the Basilica of the Sacré-Cœur & artists' square.",
    "Champs-Élysées: Famous avenue lined with shops, theaters, and cafes.",
    "Musée d'Orsay: Museum housed in a Beaux-Arts railway station, known for its Impressionist masterpieces.",
    "Palace of Versailles: Opulent 17th-century palace, the former home of French royalty, surrounded by gardens and fountains.",
    "Seine River Cruise: Scenic boat tours offering views of Paris landmarks such as the Eiffel Tower and Notre-Dame.",
    "Sainte-Chapelle: Gothic chapel known for its stunning stained glass windows.",
    "Musée Rodin: Museum showcasing the works of the French sculptor Auguste Rodin, set in a mansion with gardens."
]
        
        # Error Case 2
        if origin == 'Unknown' or destination == 'Unknown':
            invalid_airport = True
            same_airport = False
            invalid_visa = False
            return render(request, 'geogo/index.html', {
                'invalid_airport':invalid_airport,
                'same_airport':same_airport,
                'invalid_visa':invalid_visa
                })
        
        # Error Case 3
        if visa == 'Unknown':
            invalid_visa = True
            invalid_airport = False
            same_airport = False
            return render(request, 'geogo/index.html', {
                'invalid_airport':invalid_airport,
                'same_airport':same_airport,
                'invalid_visa':invalid_visa
                })

        # no error case

        flightDetails = getFlightDetails(originAirport, destinationAirport, formatted_date)


        return render(request, 'geogo/results.html', {
            'locations': locations, 
            'origin':origin,
            'destination':destination,
            'getVisa': visa,
            'flightDetails': flightDetails
        })
    
