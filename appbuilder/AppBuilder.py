import base64
import json
import tkinter as tk
from tkinter import filedialog, messagebox, ttk

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
    file_paths = filedialog.askopenfilenames(filetypes=[("Sprite Files", "*.sprite3")])
    return list(file_paths)

def prompt_for_extensions(file_paths):
    def save_extensions():
        extensions = extension_text.get("1.0", "end").strip().split("\n")
        root.destroy()
        process_files_and_extensions(file_paths, extensions)

    root = tk.Tk()
    root.title("Extension Links")
    root.resizable(False, False)
    root.geometry("400x300")

    label = tk.Label(root, text="Paste the links to your extensions (one link per line):")
    label.pack(pady=10)

    extension_text = tk.Text(root, height=10, width=40)
    extension_text.pack(pady=5)

    save_button = ttk.Button(root, text="Save", command=save_extensions)
    save_button.pack(pady=10)

    root.mainloop()

def process_files_and_extensions(file_paths, extensions):
    # Convert each file to a data URL
    data_urls = []
    for file_path in file_paths:
        data_url = file_to_data_url(file_path)
        data_urls.append('import sprite')
        data_urls.append(data_url)

    # Append extension links to the data URLs if extensions are provided
    if extensions:
        for extension in extensions:
            data_urls.append('import extension')
            data_urls.append(extension.strip())

    # Construct the JSON output
    json_output = json.dumps(data_urls + ["stop"])

    # Ask the user for the filename
    filename = filedialog.asksaveasfilename(
        defaultextension=".tpkg", filetypes=[("Turbox Package", "*.tpkg")]
    )
    if filename:
        # Save the JSON output to a file
        with open(filename, "w") as file:
            file.write(json_output)
        messagebox.showinfo("Build Output", f"Build output saved to {filename}")

# Prompt the user to select files using the Windows Explorer
file_paths = prompt_for_files()

# Prompt the user for extension links
prompt_for_extensions(file_paths)
