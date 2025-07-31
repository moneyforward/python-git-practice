import json
import os

def read_json(file_path="data.json"):
    try:
        if not os.path.isfile(file_path):
            print(" Error: Path is not a valid file.")
            return

        with open(file_path, 'r') as file:
            data = json.load(file)

        if not isinstance(data, (dict, list)):
            raise TypeError("Expected JSON to be a list or dict.")

        return data

    except FileNotFoundError:
        print(f" File '{file_path}' not found.")

    except PermissionError:
        print(f" Permission denied to read '{file_path}'.")

    except json.JSONDecodeError as e:
        print(f" Invalid JSON format: {e}")

    except TypeError as e:
        print(f" Type error: {e}")

    except Exception as e:
        print(f" Unexpected error: {e}")

