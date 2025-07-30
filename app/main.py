from app.jsonReader import read_json
import json

if __name__ == "__main__":
    data = read_json("data.json")
    if data:
        print("JSON Loaded:")
        print(json.dumps(data, indent= 2))