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
        "Branches": [{"id": 1, "Name": "Abha", "Target": "31,008", "Residual": "- 698", "Percentage": "- 2 %"},
                     {"id": 2, "Name": "Albaha", "Target": "18,837", "Residual": "- 3,470", "Percentage": "- 18 %"},
                     {"id": 3, "Name": "Jizan", "Target": "42,099", "Residual": "- 22,043", "Percentage": "- 52 %"},
                     {"id": 4, "Name": "Khamis", "Target": "14,011", "Residual": "+ 3,507", "Percentage": "+ 25 %"},
                     {"id": 5, "Name": "Najran", "Target": "26,769", "Residual": "- 11,399", "Percentage": "- 43 %"}]}

    save_json(new_data)
