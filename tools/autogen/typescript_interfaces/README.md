# TypeScript Interface Autogeneration

This package converts JSON Schema definition files into TypeScript interface files by leveraging the [`json-schema-to-typescript`](https://github.com/bcherny/json-schema-to-typescript) TypeScript package.

## Usage

1. Ensure `yarn` and `node` are installed on your device
2. From the root of this directory, run `yarn install` to install the dependencies
2. From the root of this directory, then run `yarn main` to create the interface files

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

```typescript
/* eslint-disable */
/**
 * This file was automatically generated.
 * Do not modify this file by hand.
 */
 
/**
 * Schema representation of a person.
 */
export interface Person {
  /**
   * Name of the person.
   */
  name: string;
  /**
   * Age of the person in years.
   */
  age?: number;
  /**
   * Email of the person.
   */
  email: string;
}
```
