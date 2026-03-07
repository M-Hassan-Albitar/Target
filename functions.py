import json


def read_json():
    with open('data.json', 'r') as f:
        data = json.load(f)
    return data


def save_json(new_data):
    with open('data.json', 'w') as f:
        json.dump(new_data, f, indent=2)


if __name__ == '__main__':
    new_data = {
        "Branches": [{"id": 1, "Name": "Abha", "Target": "139,319", "Residual": "- 47,277", "Percentage": "- 34 %"},
                     {"id": 2, "Name": "Albaha", "Target": "67,941", "Residual": "- 4,522", "Percentage": "- 7 %"},
                     {"id": 3, "Name": "Jizan", "Target": "320,384", "Residual": "- 60,836", "Percentage": "- 19 %"},
                     {"id": 4, "Name": "Khamis", "Target": "84,243", "Residual": "- 24,293", "Percentage": "- 29 %"},
                     {"id": 5, "Name": "Najran", "Target": "132,361", "Residual": "- 17,515", "Percentage": "- 13 %"}]}

    save_json(new_data)
