import json


class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, complex):
            return self.encode_complex(obj)
        elif isinstance(obj, range):
            return self.encode_range(obj)
        return super().default(obj)

    def encode_complex(self, obj):
        return {
            "__complex__": True,
            "real": obj.real,
            "imag": obj.imag
        }

    def encode_range(self, obj):
        return {
            "__range__": True,
            "start": obj.start,
            "stop": obj.stop,
            "step": obj.step
        }


class CustomJSONDecoder(json.JSONDecoder):
    def __init__(self, *args, **kwargs):
        kwargs["object_hook"] = self.object_hook
        super().__init__(*args, **kwargs)

    def object_hook(self, obj):
        if "__complex__" in obj:
            return self.decode_complex(obj)
        elif "__range__" in obj:
            return self.decode_range(obj)
        return obj

    def decode_complex(self, obj):
        return complex(obj["real"], obj["imag"])

    def decode_range(self, obj):
        return range(obj["start"], obj["stop"], obj["step"])


def dumps(obj, *args, **kwargs):
    return json.dumps(obj, cls=CustomJSONEncoder, *args, **kwargs)


def loads(s, *args, **kwargs):
    return json.loads(s, cls=CustomJSONDecoder, *args, **kwargs)


my_data = {
    "hey": complex(1, 2),
    "there": list(range(1, 10, 3)),
    73: False,
}

json_data = dumps(my_data)
print(json_data)

decoded = loads(json_data)
print(decoded)
