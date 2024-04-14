from serpapi import GoogleSearch
import json

params = {
  "api_key": "72111e0bcf0cbe8826ecd4aeb75f5e60c640cf15864ae3dfdd9867dc5bc55d5c",
  "engine": "google_flights",
  "hl": "en",
  "gl": "us",
  "departure_id": "CDG",
  "arrival_id": "AUS",
  "outbound_date": "2024-04-15",
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