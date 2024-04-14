import json

# Assuming flights_data contains the JSON data provided
flights_data = """"""



# Parse the JSON data
data = json.loads(flights_data)

# Extract information for the first 3 flights
first_3_flights = data['data'][:3]

# Display the information for the first 3 flights
for idx, flight in enumerate(first_3_flights, start=1):
    print(f"Flight {idx}:")
    print(f"  Departure Airport: {flight['departure_airport']}")
    print(f"  Destination Airport: {flight['destination_airport']}")
    print(f"  Departure Time: {flight['departure_time']}")
    print(f"  Arrival Time: {flight['arrival_time']}")
    print(f"  Price: {flight['price']}")
    print()
