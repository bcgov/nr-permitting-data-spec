import json
import jsonschema2md
import sys


def parse_schema_to_markdown(schema_path: str, destination_path: str) -> None:
    parser = jsonschema2md.Parser(
        show_examples="all",
    )

    with open(schema_path, "r") as input_file:
        parsed_lines = parser.parse_schema(json.load(input_file))

    with open(destination_path, "w") as output_file:
        output_file.write(''.join(parsed_lines))


if __name__ == "__main__":
    parse_schema_to_markdown(sys.argv[1], sys.argv[2])
