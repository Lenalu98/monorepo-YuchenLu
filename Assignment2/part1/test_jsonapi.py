import json
import pytest
from jsonapi import CustomJSONEncoder, CustomJSONDecoder, dumps, loads

# To run this test file,
# please enter "pytest test_jsonapi.py" in the terminal


def test_encode_complex():
    encoder = CustomJSONEncoder()
    obj = complex(1, 2)
    expected_result = {"__complex__": True, "real": 1.0, "imag": 2.0}
    assert encoder.encode_complex(obj) == expected_result


def test_encode_range():
    encoder = CustomJSONEncoder()
    obj = range(1, 10, 3)
    expected_result = {"__range__": True, "start": 1, "stop": 10, "step": 3}
    assert encoder.encode_range(obj) == expected_result


def test_decode_complex():
    decoder = CustomJSONDecoder()
    obj = {"__complex__": True, "real": 1.0, "imag": 2.0}
    expected_result = complex(1, 2)
    assert decoder.decode_complex(obj) == expected_result


def test_decode_range():
    decoder = CustomJSONDecoder()
    obj = {"__range__": True, "start": 1, "stop": 10, "step": 3}
    expected_result = range(1, 10, 3)
    assert decoder.decode_range(obj) == expected_result


def test_dumps_and_loads():
    my_data = {
        "complex_number": complex(1, 2),
        "range_object": range(1, 10, 3),
        "boolean_value": False
    }

    # Serialize using custom encoder
    json_data = dumps(my_data)
    decoded = loads(json_data)

    # Ensure the original and decoded data match
    assert decoded["complex_number"] == my_data["complex_number"]
    assert list(decoded["range_object"]) == list(my_data["range_object"])
    assert decoded["boolean_value"] == my_data["boolean_value"]


if __name__ == '__main__':
    pytest.main()
