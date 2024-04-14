import json


# Read the contents of the output.json file
with open('/Users/ronaldheminway/geogo/geogobackend/geogo/api/output.json', 'r') as file:
    data = file.read()

# Parse the contents as JSON
parsed_data = json.loads(data)

# Write the parsed data back to the output.json file
with open('/Users/ronaldheminway/geogo/geogobackend/geogo/api/output.json', 'w') as file:
    json.dump(parsed_data, file, indent=4)