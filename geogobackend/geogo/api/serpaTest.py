import json

with open('output.json') as f:
    data = json.load(f)


    
    # Accessing best_flights
    best_flights = data.get("best_flights", [])
    flightDetails = []

    # Iterating over each best flight
    for idx, flight in enumerate(best_flights, start=1):
        print(f"Flight {idx}:")
        print("Price:", flight.get("price"))
        flightDetails.append(f"Flight {idx}")
        flightDetails.append(flight.get("price"))

        # Accessing flights details
        for i, flight_details in enumerate(flight.get("flights", []), start=1):
            print(f"\tLeg {i}:")
            print("\tDeparture Airport:", flight_details.get("departure_airport", {}).get("name"))
            print("\tArrival Airport:", flight_details.get("arrival_airport", {}).get("name"))
            print("\tAirline:", flight_details.get("airline"))
            print("\tFlight Number:", flight_details.get("flight_number"))

            flightDetails.append(f"Leg {i}")
            flightDetails.append(flight_details.get("departure_airport", {}).get("name"))
            flightDetails.append(flight_details.get("arrival_airport", {}).get("name"))
            flightDetails.append(flight_details.get("airline"))
            flightDetails.append(flight_details.get("flight_number"))

        # Accessing layovers
        print("\tLayovers:")
        flightDetails.append('Layovers')
        for layover in flight.get("layovers", []):
            print("\tName:", layover.get("name"), layover.get("id"))
            flightDetails.append(layover.get('name'))
            flightDetails.append(layover.get('id'))

        # Accessing carbon emissions
        # carbon_emissions = flight.get("carbon_emissions", {})
        # print("\tCarbon Emissions:")
        # print("\tThis Flight:", carbon_emissions.get("this_flight"))
        # print("\tTypical For This Route:", carbon_emissions.get("typical_for_this_route"))
        # print("\tDifference Percent:", carbon_emissions.get("difference_percent"))

        # print("\tBooking Token:", flight.get("booking_token"))
        # print()

    # print(flightDetails)
    print('='*30)
    for i in flightDetails:
        if 'Leg' in str(i):
            print(i.split()[1])
        else:
            print(i)


