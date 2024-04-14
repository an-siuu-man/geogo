from django.shortcuts import render
from django import forms
from datetime import datetime
from .api.gptAPI import generateResponse
from .api.airportCodes import city_codes
from .api.serpapigit import *
from .api.geminiAPI import generateVisaResponse
from .api.embedCodes import embed_codes
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
        response = generateResponse(f'top 10 tourist locations in {destination} in a list with one line descriptions').split('\n')

        locations = []
        for i in response:
            if i != '':
                locations.append(i)
        
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

        finalFlights = formatFlights(flightDetails)

        embeddedCodes = embed_codes()
        visaReq = generateVisaResponse([originAirport, destinationAirport], destinationAirport, getVisa)
        try:
            required = embeddedCodes[destination]
        except:
            return render(request, 'geogo/results.html', {
                'locations': locations,
                'origin': origin,
                'destination': destination,
                'getVisa': visa,
                'flightDetails': finalFlights,
                'visaReq': visaReq
            })
        return render(request, 'geogo/results.html', {
            'locations': locations, 
            'origin':origin,
            'destination':destination,
            'getVisa': visa,
            'flightDetails': finalFlights,
            'visaReq': visaReq,
            'code':required
        })
    
