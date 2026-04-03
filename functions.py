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
        "Branches": [{"id": 1, "Name": "Abha", "Target": "31,008", "Residual": "- 29,706", "Percentage": "- 96 %"},
                     {"id": 2, "Name": "Albaha", "Target": "18,837", "Residual": "- 16,270", "Percentage": "- 86 %"},
                     {"id": 3, "Name": "Jizan", "Target": "42,099", "Residual": "- 41,144", "Percentage": "- 98 %"},
                     {"id": 4, "Name": "Khamis", "Target": "14,011", "Residual": "- 12,647", "Percentage": "- 90 %"},
                     {"id": 5, "Name": "Najran", "Target": "26,769", "Residual": "- 25,206", "Percentage": "- 94 %"}]}

    save_json(new_data)
