from serpapi import GoogleSearch

params = {
  "api_key": "72111e0bcf0cbe8826ecd4aeb75f5e60c640cf15864ae3dfdd9867dc5bc55d5c",
  "engine": "google_flights",
  "hl": "en",
  "gl": "us",
  "departure_id": "CDG",
  "arrival_id": "AUS",
  "outbound_date": "2024-04-14",
  "currency": "USD",
  "type": "2"
}

search = GoogleSearch(params)
results = search.get_dict()

# print(results['best_flights'][0]['flights'])

for i in results['best_flights']:
  print(i['flights']['departure_airport']['name'],
        '\n',
        i['flights']['departure_airport']['id'],
        '\n',
        i['flights']['arrival_airport']['name'],
        '\n',
        i['flights']['arrival_airport']['id'],
        '\n',
        i['flights']['airline'],
        '\n',
        i['flights']['flight_number']
        )
  print(i['layovers'])
  print(i['price'])
