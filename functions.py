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
        "Branches": [{"id": 1, "Name": "Abha", "Target": "139,319", "Residual": "- 55,622", "Percentage": "- 40 %"},
                     {"id": 2, "Name": "Albaha", "Target": "67,941", "Residual": "- 10,348", "Percentage": "- 15 %"},
                     {"id": 3, "Name": "Jizan", "Target": "320,384", "Residual": "- 89,865", "Percentage": "- 28 %"},
                     {"id": 4, "Name": "Khamis", "Target": "84,243", "Residual": "- 32,185", "Percentage": "- 38 %"},
                     {"id": 5, "Name": "Najran", "Target": "132,361", "Residual": "- 31,221", "Percentage": "- 24 %"}]}

    save_json(new_data)
