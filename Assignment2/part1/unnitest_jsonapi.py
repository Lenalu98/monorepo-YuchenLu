import json
import unittest
from jsonapi import CustomJSONEncoder, CustomJSONDecoder, dumps, loads

# to run this test file,
# please enter "python unnitest_jsonapi.py" in the terminal


class TestCustomJSONEncoder(unittest.TestCase):
    def test_encode_complex(self):
        encoder = CustomJSONEncoder()
        obj = complex(2, 5)
        expected_result = {"__complex__": True, "real": 2.0, "imag": 5.0}
        self.assertEqual(encoder.encode_complex(obj), expected_result)

    def test_encode_range(self):
        encoder = CustomJSONEncoder()
        obj = range(1, 10, 2)
        expected_result = {"__range__": True, "start": 1,
                           "stop": 10, "step": 2}
        self.assertEqual(encoder.encode_range(obj), expected_result)


class TestCustomJSONDecoder(unittest.TestCase):
    def test_decode_complex(self):
        decoder = CustomJSONDecoder()
        obj = {"__complex__": True, "real": 4.0, "imag": 5.0}
        expected_result = complex(4, 5)
        self.assertEqual(decoder.decode_complex(obj), expected_result)

    def test_decode_range(self):
        decoder = CustomJSONDecoder()
        obj = {"__range__": True, "start": 1, "stop": 10, "step": 2}
        expected_result = range(1, 10, 2)
        self.assertEqual(decoder.decode_range(obj), expected_result)


class TestDumpsAndLoads(unittest.TestCase):
    def test_dumps_and_loads(self):
        my_data = {
            "complex_number": complex(3, 4),
            "range_object": range(1, 10, 2),
            "boolean_value": False
        }

        # Serialize using custom encoder
        json_data = dumps(my_data)
        decoded = loads(json_data)

        # Ensure the original and decoded data match
        self.assertEqual(decoded["complex_number"], my_data["complex_number"])
        self.assertEqual(list(decoded["range_object"]),
                         list(my_data["range_object"]))
        self.assertEqual(decoded["boolean_value"], my_data["boolean_value"])


if __name__ == '__main__':
    unittest.main()
