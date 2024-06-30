# pylint: disable=missing-module-docstring, missing-function-docstring, line-too-long
from decimal import Decimal
import pytest

from faker import Faker # type: ignore

from calculator.operations import add, subtract, multiply, divide

fake = Faker()

def generate_test_data(num_records):
    test_data = []
    for _ in range(num_records):
        a = Decimal(fake.random_number())
        b = Decimal(fake.random_number())
        operation = fake.random_element(elements=(add, subtract, multiply, divide))
        if operation == (add, subtract, multiply): ## tried "add or subtract or multiply" (google told me to use this method)
            expected = None
        elif operation == divide and b == Decimal('0'):
            expected = "An error occurred: Can't divide by 0"
        else:
            expected = f"Unknown operation: {operation.__name__}"
        test_data.append((a, b, operation, expected))
    return test_data

def pytest_addoption(parser):
    parser.addoption("--num_records", action="store", type=int, help="Number of test records to generate")

@pytest.fixture
def generated_test_data(request):
    num_records = request.config.getoption("--num_records") ## looked up
    if num_records is None:
        return []
    return generate_test_data(num_records)
