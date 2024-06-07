# Schema Validation Tool

This package takes a JSON document and validates it against an expected schema structure as defined in a JSON Schema definition file. This is achieved by leveraging the [`jsonschema`](https://python-jsonschema.readthedocs.io/en/stable/) Python package.

## Usage

1. Ensure Python 3 is installed on your device
2. Run `pip3 install -r requirements.txt` from the root of this directory to install the required packages
3. Return to the root of this repository and run `python3 tools/schemas/validation/main.py <path/to/json/document/file> <path/to/schema/definition/file>`

## Example

Sample definition file:

```json
{
  "title": "Person",
  "description": "Schema representation of a person.",
  "type": "object",
  "properties": {
    "name": {
      "type": "string",
      "description": "Name of the person."
    },
    "age": {
      "type": "integer",
      "minimum": 0,
      "description": "Age of the person in years."
    },
    "email": {
      "type": "string",
      "format": "email",
      "description": "Email of the person."
    }
  },
  "required": ["name", "email"]
}
```

### On Valid Schema

Sample valid JSON document:

```json
{
  "name": "Example",
  "age": 100,
  "email": "example@example.com"
}
```

On successful validation, there will be no output to the console by this program.

### On Invalid Schema

Sample invalid JSON document, where the `age` attribute is not the correct type:

```json
{
  "name": "Example",
  "age": "100",
  "email": "example@example.com"
}
```

Validation will fail, and the following will be output to the screen:

```shell
...
jsonschema.exceptions.ValidationError: '100' is not of type 'integer'

Failed validating 'type' in schema['properties']['age']:
    {'description': 'Age of the person in years.',
     'minimum': 0,
     'type': 'integer'}

On instance['age']:
    '100'
```
