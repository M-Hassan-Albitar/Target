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
        "Branches": [{"id": 1, "Name": "Abha", "Target": "31,008", "Residual": "- 20,508", "Percentage": "- 66 %"},
                     {"id": 2, "Name": "Albaha", "Target": "18,837", "Residual": "- 13,738", "Percentage": "- 73 %"},
                     {"id": 3, "Name": "Jizan", "Target": "42,099", "Residual": "- 36,490", "Percentage": "- 87 %"},
                     {"id": 4, "Name": "Khamis", "Target": "14,011", "Residual": "- 10,786", "Percentage": "- 77 %"},
                     {"id": 5, "Name": "Najran", "Target": "26,769", "Residual": "- 21,637", "Percentage": "- 81 %"}]}

    save_json(new_data)
