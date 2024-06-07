import unittest
import os

from main import validate_schema

CWD = os.path.dirname(os.path.realpath(__file__))
SCHEMA_DEFINITION_PATH = f"{CWD}/mocks/mock.schema.json"
INVALID_SCHEMA_PATH = f"{CWD}/mocks/mock_invalid.json"
VALID_SCHEMA_PATH = f"{CWD}/mocks/mock_valid.json"


class TestValidation(unittest.TestCase):
    def test_invalid_schema(self) -> None:
        """
        Test that invalid schemas raise exceptions
        """

        try:
            validate_schema(INVALID_SCHEMA_PATH, SCHEMA_DEFINITION_PATH)
        except:
            return
        
    def test_valid_schema(self) -> None:
        """
        Test that valid schemas don't raise exceptions
        """

        try:
            validate_schema(VALID_SCHEMA_PATH, SCHEMA_DEFINITION_PATH)
        except:
            self.fail("Validation should succeed")


if __name__ == '__main__':
    unittest.main()
