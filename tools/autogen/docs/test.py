import unittest
import os
import filecmp

from main import parse_schema_to_markdown

CWD = os.path.dirname(os.path.realpath(__file__))
SCHEMA_DEFINITION_PATH = f"{CWD}/mocks/mock.schema.json"
EXPECTED_MARKDOWN_PATH = f"{CWD}/mocks/expected_output.md"
GENERATED_MARKDOWN_PATH = f"{CWD}/mocks/generated_output.md"


class TestValidation(unittest.TestCase):
    def test_generates_expected_output(self) -> None:
        """
        Test that the function generates the expected output
        """

        parse_schema_to_markdown(SCHEMA_DEFINITION_PATH, GENERATED_MARKDOWN_PATH)

        if not filecmp.cmp(EXPECTED_MARKDOWN_PATH, GENERATED_MARKDOWN_PATH):
            self.fail("Generated markdown file is not as expected")


if __name__ == '__main__':
    unittest.main()
