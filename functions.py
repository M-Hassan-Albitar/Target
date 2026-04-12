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
        "Branches": [{"id": 1, "Name": "Abha", "Target": "31,008", "Residual": "- 6,569", "Percentage": "- 21 %"},
                     {"id": 2, "Name": "Albaha", "Target": "18,837", "Residual": "- 13,738", "Percentage": "- 73 %"},
                     {"id": 3, "Name": "Jizan", "Target": "42,099", "Residual": "- 34,246", "Percentage": "- 81 %"},
                     {"id": 4, "Name": "Khamis", "Target": "14,011", "Residual": "- 7,221", "Percentage": "- 52 %"},
                     {"id": 5, "Name": "Najran", "Target": "26,769", "Residual": "- 17,007", "Percentage": "- 64 %"}]}

    save_json(new_data)
