import tkinter as tk
from tkinter import messagebox
import requests
from dotenv import load_dotenv
import os

# get API Key from .env
load_dotenv()
API_KEY = os.getenv("BING_API_KEY")

def copy_to_clipboard(coords):
    if coords:
        window.clipboard_clear()
        window.clipboard_append(coords)
        messagebox.showinfo("Copied!", "Coordinates copied to clipboard.")
    else:
        messagebox.showerror("Error!", "No coordinates to copy.")

def get_coordinates():
    address = input_address.get()

    if not address:
        messagebox.showerror("Error!", "Please insert an address.")
        return

    if not API_KEY:
        messagebox.showerror("Error!", "API Key not configured")
        return

    try:
        # Query to Bing Maps API
        url = "http://dev.virtualearth.net/REST/v1/Locations"
        params = {"q": address, "key": API_KEY, "maxResults": 1}
        response = requests.get(url, params=params)
        data = response.json()

        if response.status_code == 200 and data["resourceSets"]:
            coordinates = data["resourceSets"][0]["resources"][0]["point"]["coordinates"]
            result = f"{coordinates[0], coordinates[1]}"
            label_result.config(text=result)

            # Create button dinamicaly
            if hasattr(window, 'copy_btn'):
                window.copy_btn.destroy()

            window.copy_btn = tk.Button(
                window,
                text="Copy",
                command=lambda: copy_to_clipboard(coordinates)
            )
            window.copy_btn.pack(pady=5)
        else:
            messagebox.showerror("Error!", "Address not found.")
            if hasattr(window, "copy_btn"):
                window.copy_btn.destroy()
    except Exception as ex:
        messagebox.showerror("Error!", f"Connection failure: {ex}")
        if hasattr(window, "copy_btn"):
            window.copy_btn.destroy()

# Window configuration
window = tk.Tk()
window.title("Address to Coordinates")
window.geometry("400x220")

# Interface elements
tk.Label(window, text="Insert an address:", font=("Arial", 12)).pack(pady=10)
input_address = tk.Entry(window, width=50)
input_address.pack(pady=5)

button = tk.Button(window, text="Get Coordinates", command=get_coordinates)
button.pack(pady=10)

label_result = tk.Label(window, text="", font=("Arial", 10))
label_result.pack(pady=10)

window.mainloop()

