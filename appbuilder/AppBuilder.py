import base64
import json
import tkinter as tk
from tkinter import filedialog

def file_to_data_url(file_path):
    with open(file_path, "rb") as file:
        file_data = file.read()
        base64_data = base64.b64encode(file_data).decode("utf-8")
        data_url = f"data:{get_mime_type(file_path)};base64,{base64_data}"
        return data_url

def get_mime_type(file_path):
    import mimetypes
    return mimetypes.guess_type(file_path)[0] or "application/octet-stream"

def prompt_for_files():
    root = tk.Tk()
    root.withdraw()
    file_paths = filedialog.askopenfilenames()
    return list(file_paths)

# Prompt the user to select files using the Windows Explorer
file_paths = prompt_for_files()

# Convert each file to a data URL
data_urls = []
for file_path in file_paths:
    data_url = file_to_data_url(file_path)
    data_urls.append('import sprite')
    data_urls.append(data_url)

# Construct the JSON output
json_output = json.dumps(data_urls + ["stop"])

# Ask the user for the filename
filename = input("What would you like to save your app as? ")

# Save the JSON output to a file
output_file_path = f"{filename}.osp"
with open(output_file_path, "w") as file:
    file.write(json_output)

print(f"Build output saved to {output_file_path}")
