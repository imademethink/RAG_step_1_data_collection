import json
from jsonschema import validate, ValidationError

# tell top 10 operations to be done on json file using Python

# 1. Read from a File
# 2. Write to a File
# 3. Parse a JSON String
# 4. Convert Objects to Strings
# 5. Prettify for Readability
# 6. Sort Keys Alphabetically
# 7. Validate JSON schema
# 8. Handle Nested Data
# 9. Filter and Modify






# 1. Read from a File (json.load):
#       Open a .json file and parse its content directly into a Python dictionary or list.
# 2. Write to a File (json.dump):
#       Save a Python dictionary or list into a .json file for storage or data exchange.
# 3. Parse a JSON String (json.loads):
#       Convert a JSON-formatted string (often received from a web API) into a Python object.

data = {"name": "Alice", "role": "Engineer", "active": True}
with open("data.json", "w") as f:
    json.dump(data, f)
with open("data.json", "r") as f:
    loaded_data = json.load(f)


# 4. Convert Objects to Strings (json.dumps):
#       Transform a Python dictionary into a JSON string, which is useful for sending data over a network.
json_string = '{"id": 101, "status": "success"}'
data_dict = json.loads(json_string)
new_json_string = json.dumps(data_dict)
print(new_json_string)



# 5. Prettify for Readability:
#       Use the indent parameter in dump or dumps to add whitespace and newlines, making the JSON human-readable.
# 6. Sort Keys Alphabetically:
#       Use sort_keys=True to ensure dictionary keys are saved in alphabetical order, making version control diffs easier to read.
complex_data = {"c": 3, "a": 1, "b": {"z": 26, "y": 25}}
pretty_json = json.dumps(complex_data, indent=4, sort_keys=True)
print(pretty_json)


# 7. Validate JSON schema:
# Define what the JSON should look like
required_schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "age": {"type": "number"}
    },
    "required": ["name"]
}

def validate_data(json_data):
    try:
        validate(instance=json_data, schema=required_schema)
        print("Data matches the schema!")
    except ValidationError as e:
        print(f"Schema Validation Error: {e.message}")

# Example usage
user_data = {"name": "Bob", "age": 30}
validate_data(user_data)
user_data = {"name": "Jon", "age": "thirty"} # Error: 'thirty' is not a number
validate_data(user_data)
user_data = {"name": "Jon"} # Ok: name is mandatory field, others not
validate_data(user_data)
user_data = {"age": 26} # Error: mandatory field missing
validate_data(user_data)


# 8. Handle Nested Data:
#       Access deeply nested values by chaining keys or indices (e.g., data['user']['address']['zip']) after loading the file.
user_data = {"user": {"profile": {"name": "Bob"}}}
name = user_data["user"]["profile"]["name"]
print(name)


# 9. Filter and Modify:
#       After loading a JSON file as a Python object, you can filter specific records or update values before writing them back to the file.
users = [
    {"name": "Alice", "active": True},
    {"name": "Bob", "active": False}
]
# Filter only active users
active_users = [u for u in users if u["active"]]
print(users)
print(active_users)



