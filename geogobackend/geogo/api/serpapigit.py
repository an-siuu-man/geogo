from serpapi import GoogleSearch
import json

def getFlightDetails (departure_id, arrival_id, date):
  params = {
    "api_key": "72111e0bcf0cbe8826ecd4aeb75f5e60c640cf15864ae3dfdd9867dc5bc55d5c",
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
      flightDetails = []
      dictTest = {}
      # Iterating over each best flight
      for idx, flight in enumerate(best_flights, start=1):
          # print(f"Flight {idx}:")
          # print("Price:", flight.get("price"))
          flightDetails.append(f"Flight {idx}")
          dictTest[f'Flight_no_{idx}'] = f'{idx}'
          flightDetails.append(flight.get("price"))
          dictTest[f'price{idx}'] = str(flight.get('price'))

          # Accessing flights details
          for i, flight_details in enumerate(flight.get("flights", []), start=1):
              # print(f"\tLeg {i}:")
              # print("\tDeparture Airport:", flight_details.get("departure_airport", {}).get("name"))
              # print("\tArrival Airport:", flight_details.get("arrival_airport", {}).get("name"))
              # print("\tAirline:", flight_details.get("airline"))
              # print("\tFlight Number:", flight_details.get("flight_number"))

              flightDetails.append(f"Leg {i}")
              dictTest[f'Leg_{i}_for_flight_no_{idx}'] = f'{i}'
              flightDetails.append(flight_details.get("departure_airport", {}).get("name"))
              dictTest[f'departure_airport{i}_for_flight_no_{idx}'] = str(flight_details.get('departure_airport', {}).get('name'))
              flightDetails.append(flight_details.get("arrival_airport", {}).get("name"))
              dictTest[f'arrival_airport{i}_for_flight_no_{idx}'] = str(flight_details.get("arrival_airport", {}).get("name"))
              flightDetails.append(flight_details.get("airline"))
              dictTest[f'airline{i}_for_flight_no_{idx}'] = str(flight_details.get("airline"))
              flightDetails.append(flight_details.get("flight_number"))
              dictTest[f'flight_number{i}_for_flight_no_{idx}'] = str(flight_details.get("flight_number"))

          # Accessing layovers
          # print("\tLayovers:")
          flightDetails.append('Layovers')
          for layover in flight.get("layovers", []):
              # print("\tName:", layover.get("name"), layover.get("id"))
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
      return dictTest
      # print('='*30)
      # for i in flightDetails:
          # if 'Leg' in str(i):
          #     print(i.split()[1])
          # else:
        # print(type(i))
      # return flightDetails
print(getFlightDetails('MCI','DEL', '2024-05-01'))