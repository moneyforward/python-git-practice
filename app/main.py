import os
import json
from app.jsonReader import read_json

def get_data_dir():
    return os.path.join(os.path.dirname(__file__), 'data')

if __name__ == "__main__":
    data_dir = get_data_dir()

    for filename in os.listdir(data_dir):
        if filename.endswith('.json'):
            file_path = os.path.join(data_dir, filename)
            print(f"Loading: {filename}")
            data = read_json(file_path)

            if data:
                print("JSON Loaded Successfully:")
                print(json.dumps(data, indent=2))
            else:
                print("Failed to load JSON.")
