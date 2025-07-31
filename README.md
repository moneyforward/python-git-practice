# JSON Reader App

This is a simple Python application that reads and displays JSON content from a specified file path. It includes robust error handling for common issues like invalid files, permission errors, and malformed JSON content.

# How to Run the App

From the root directory of the project:
   python -m app.main


When prompted:
   Enter the path to the JSON file: valid.json


# Features

      Accepts file path input from user    
      Loads JSON using json module      
      Pretty-prints JSON content if valid     
      Handles the following errors gracefully:   
      FileNotFoundError: If the file doesn't exist      
      PermissionError: If read permissions are missing      
      json.JSONDecodeError: If JSON is malformed      
      TypeError: If the content is not a dict or list
      Other unexpected exceptions


For protected.json, you can simulate no-permission by running:
      chmod 000 protected.json (on Unix/macOS)



# Requirements

      Python 3.6+
      No external dependencies — only standard library is used
      



