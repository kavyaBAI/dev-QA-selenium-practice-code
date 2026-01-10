# {
#   "id": 101,
#   "username": "tester_john",
#   "email": "john@example.com",
#   "active": true
# }
#above data is return by api in json format we have to validate using jsonscema
import requests
from jsonschema import validate
from jsonschema.exceptions import ValidationError

def test_user_schema():
    user_schema = {
        "type": "object",
        "properties": {
            "id": {"type": "number"},
            "username": {"type": "string", "minLength": 3},
            "email": {"type": "string", "format": "email"},
            "active": {"type": "boolean"}
        },
        "required": ["id", "username", "email"] 
    }
    response = requests.get("https://jsonplaceholder.typicode.com/users/1")
    print(response.status_code)
    actual_data = response.json()
    print("actual_data",actual_data)
    try:
        validate(instance=actual_data, schema=user_schema)
        print("Schema Validation PASSED!")
    except ValidationError as e:
        print(f"Schema Validation FAILED! Message: {e.message}")

test_user_schema()