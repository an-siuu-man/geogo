from django.shortcuts import render
from django import forms
from datetime import datetime
from .api.gptAPI import generateResponse
from .api.airportCodes import city_codes
from .api.serpapigit import *
from .api.geminiAPI import generateVisaResponse
from .api.embedCodes import embed_codes
# Create your views here.

# adding a random comment for no reason
codes = city_codes()
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
            # if no date is chosen, choose tomorrow
            # IN THEORY, this condition should never occur due to logic update in index.js
            thisday = datetime.today()
            day_t = thisday.day
            month_t = ""
            if int(thisday.month) < 10:
                month_t = str("0" + str(thisday.month))
            else:
                month_t = thisday.month
            year_t = thisday.year
            # choosing tomorrow...
            day_t = day_t + 1
            if day_t < 10:
                day_t = str("0" + str(thisday.day))
            dash_t = "-"
            formatted_date = str(str(year_t) + dash_t + str(month_t) + dash_t + str(day_t))
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
    
