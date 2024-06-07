# Markdown Autogeneration

This package converts JSON Schema definition files into markdown files by leveraging the [`jsonschema2md`](https://github.com/sbrunner/jsonschema2md) Python package.

## Usage

1. Ensure Python 3 is installed on your device
2. From the root of the repository run `python3 tools/autogen/docs/main.py <path/to/schema/definition/file> <path/to/output/filename>`

## Example

Sample input schema file:

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

Sample output file:

```markdown
# Person
 
*Schema representation of a person.*
 
## Properties
 
- **`name`** *(string)*: Name of the person.
- **`age`** *(integer)*: Age of the person in years. Minimum: `0`.
- **`email`** *(string, format: email)*: Email of the person.
```
