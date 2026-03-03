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
        "Branches": [{"id": 1, "Name": "Abha", "Target": "139,319", "Residual": "60,829 -", "Percentage": "- 44 %"},
                     {"id": 2, "Name": "Albaha", "Target": "67,941", "Residual": "12,867 -", "Percentage": "- 19 %"},
                     {"id": 3, "Name": "Jizan", "Target": "320,384", "Residual": "98,292 -", "Percentage": "- 31 %"},
                     {"id": 4, "Name": "Khamis", "Target": "84,243", "Residual": "36,318 -", "Percentage": "- 43 %"},
                     {"id": 5, "Name": "Najran", "Target": "132,361", "Residual": "33,598 -", "Percentage": "- 25 %"}]}

    save_json(new_data)
