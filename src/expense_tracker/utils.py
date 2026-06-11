import json


def json_to_dict(data: list[dict]) -> str:
    return json.dumps(data, indent=4)
