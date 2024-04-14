import json

with open('output.json') as f:
    data = json.load(f)


    
    # Accessing best_flights
    best_flights = data.get("best_flights", [])
    
    # Iterating over each best flight
    for idx, flight in enumerate(best_flights, start=1):
        print(f"Flight {idx}:")
        print("Price:", flight.get("price"))
        print("Type:", flight.get("type"))
        print("Total Duration:", flight.get("total_duration"))

        # Accessing flights details
        for i, flight_details in enumerate(flight.get("flights", []), start=1):
            print(f"\tLeg {i}:")
            print("\tDeparture Airport:", flight_details.get("departure_airport", {}).get("name"))
            print("\tArrival Airport:", flight_details.get("arrival_airport", {}).get("name"))
            print("\tAirline:", flight_details.get("airline"))
            print("\tFlight Number:", flight_details.get("flight_number"))

        # Accessing layovers
        print("\tLayovers:")
        for layover in flight.get("layovers", []):
            print("\tName:", layover.get("name"))

        # Accessing carbon emissions
        # carbon_emissions = flight.get("carbon_emissions", {})
        # print("\tCarbon Emissions:")
        # print("\tThis Flight:", carbon_emissions.get("this_flight"))
        # print("\tTypical For This Route:", carbon_emissions.get("typical_for_this_route"))
        # print("\tDifference Percent:", carbon_emissions.get("difference_percent"))

        # print("\tBooking Token:", flight.get("booking_token"))
        # print()
