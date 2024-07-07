import json


def extract_json_string(s: str) -> dict:
    start_index = s.index("{")
    end_index = s.rindex("}") + 1
    json_str = s[start_index:end_index]
    json_str = json_str.replace("\n", " ")
    json_dict = json.loads(json_str)

    return json_dict
