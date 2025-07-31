from app.jsonReader import read_json
import json

if __name__ == "__main__":
    file_path = input("Enter the path to the JSON file: ").strip()
    data = read_json(file_path)

    if data:
        print("JSON Loaded Successfully:")
        print(json.dumps(data, indent=2))
