from serpapi import GoogleSearch
import json

def getFlightDetails (departure_id, arrival_id, date):
  params = {
    "api_key": "8eeacf205b31c7f05395d408e6488b6354d747d8ab30ff611882c7a1e9e1fac8",
    "engine": "google_flights",
    "hl": "en",
    "gl": "us",
    "departure_id": departure_id,
    "arrival_id": arrival_id,
    "outbound_date": date,
    "currency": "USD",
    "adults": "1",
    "type": "2"
  }

  search = GoogleSearch(params)
  results = search.get_dict()

  # Write results to output.json file
  with open('output.json', 'w') as f:
      json.dump(results, f)

  # Read the contents of the output.json file
  with open('output.json', 'r') as file:
      data = file.read()

  # Parse the contents as JSON
  parsed_data = json.loads(data)

  # Write the parsed data back to the output.json file
  with open('output.json', 'w') as file:
      json.dump(parsed_data, file, indent=4)

  # ==============================================================================================

  with open('output.json') as f:
      data = json.load(f)


      
      # Accessing best_flights
      best_flights = data.get("best_flights", [])

      #accessing other flights if best flights dont return any flights
      if not best_flights:
          best_flights = data.get('other_flights', [])
      dictTest = {}
      idxCounter = 0
      # Iterating over each best flight
      for idx, flight in enumerate(best_flights, start=1):
          dictTest[f'Flight_no_{idx}'] = f'{idx}'
          dictTest[f'price{idx}'] = str(flight.get('price'))
          idxCounter += 1

          # Accessing flights details
          for i, flight_details in enumerate(flight.get("flights", []), start=1):

              dictTest[f'Leg_{i}_for_flight_no_{idx}'] = f'{i}'
              dictTest[f'departure_airport{i}_for_flight_no_{idx}'] = str(flight_details.get('departure_airport', {}).get('name'))
              dictTest[f'arrival_airport{i}_for_flight_no_{idx}'] = str(flight_details.get("arrival_airport", {}).get("name"))
              dictTest[f'airline{i}_for_flight_no_{idx}'] = str(flight_details.get("airline"))
              # dictTest[f'flight_number_for_flight_no_{idx}'] = str(flight_details.get("flight_number"))

      # print(flightDetails)
      return dictTest
      # print('='*30)
      # for i in flightDetails:
          # if 'Leg' in str(i):
          #     print(i.split()[1])
          # else:
        # print(type(i))
      # return flightDetails
flight1_details = (getFlightDetails('MCI', 'DEL', '2024-04-20'))
def formatFlights(flight_details):
  noOfFlights = 0
  for i in flight_details.keys():
    if 'Flight_no_' in i:
      noOfFlights += 1
  flights = []

  for i in range(noOfFlights):
    flights.append([])

  for i in range(noOfFlights):
    for j in flight_details.keys():
        if j[-1] == str(i+1):
          flights[i].append(flight_details[j])
  formatted_flights = []

  for flight in flights:
      itinerary = []
      for i in range(2, len(flight), 4):  # Start from index 2 to skip the flight number and flight code
          leg = flight[i:i+4]
          itinerary.append(leg)
      formatted_flights.append(itinerary)
  return formatted_flights

