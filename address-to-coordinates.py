import tkinter as tk
from tkinter import messagebox
import request
from dotenv import load_dotenv
import os

# get API Key from .env
load_dotenv()
API_KEY = os.getenv("BING_API_KEY")

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
        params = {"q": address, "key": API_KEY, "max_results": 1}
        response = request.get(url, params=params)
        data = response.json()

        if response.status_code == 200 and data["resourceSets"]:
            coordinates = data["resourceSets"][0]["resources"][0]["point"]["coordinates"]
            result = = f"{coordinates[0], coordinates[1]}"
            label_result.config(text=result)
        else:
            messagebox.showerror("Error!", "Address not found.")
    except Exception as ex:
        messagebox.showerror("Error!", "Connection failure: {ex}")

# Window configuration
window = tk.Tk()
window.title("Address to Coordinates")
window.geometry("400x200")

# Interface elements
tk.Label(window, text="Insert an address:", font=("Arial", 12)).pack(pady=10)
input_address = tk.Entry(window, width=50)
input_address.pack(pady=5)

button = tk.Button(window, text="Get Coordinate", command=get_coordinates)
button.pack(pady=10)

label_result = tk.Label(window, text="", font=("Arial", 10))
label_result.pack(pady=10)

window.mainloop()

