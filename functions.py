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
        "Branches": [{"id": 1, "Name": "Abha", "Target": "139,319", "Residual": "- 51,616", "Percentage": "- 37 %"},
                     {"id": 2, "Name": "Albaha", "Target": "67,941", "Residual": "- 7,213", "Percentage": "- 11 %"},
                     {"id": 3, "Name": "Jizan", "Target": "320,384", "Residual": "- 78,842", "Percentage": "- 25 %"},
                     {"id": 4, "Name": "Khamis", "Target": "84,243", "Residual": "- 26,673", "Percentage": "- 32 %"},
                     {"id": 5, "Name": "Najran", "Target": "132,361", "Residual": "- 26,711", "Percentage": "- 20 %"}]}

    save_json(new_data)
