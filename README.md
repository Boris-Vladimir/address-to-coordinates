# Address to Coordinates Converter (Bing Maps)

A simple Windows tool to convert addresses into geographic coordinates (latitude/longitude) using the Bing Maps API.

## 📋 Prerequisites
- **Windows 10/11**
- **Python 3.8+** ([Download here](https://www.python.org/downloads/))
- Internet connection

---

## 🚀 Quick Start

### 1. Get a Bing Maps API Key
1. Go to the [Bing Maps Portal](https://www.bingmapsportal.com/).
2. Sign in with a Microsoft account.
3. Click **"My keys" > "Create a new key"**.
4. Choose **"Basic"** as the key type and name it (e.g., `AddressConverter`).
5. Copy the generated key (you’ll use it in Step 2).

### 2. Set Up the `.env` File
1. Download the `.env.example` file from the project (or create a new file named `.env`).
2. Open it with a text editor (e.g., Notepad) and add your API key:
   ```ini
   BING_API_KEY=your_api_key_here
   ```
3. Save the file in the **same folder** as the Python script.

### 3. Run the Program
#### **Option A: Via Python (Recommended for testing)**
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Run the script:
   ```bash
   python address_to_coordinates.py
   ```

#### **Option B: Generate an Executable (.exe)**
1. Install `pyinstaller`:
   ```bash
   pip install pyinstaller
   ```
2. Build the executable:
   ```bash
   pyinstaller --onefile --windowed --additional-hooks-dir=. address-to-coordinates.py
   ```
3. Copy the `.env` file to the `dist/` folder (where `main.exe` is located).
4. Double-click `address_to_coordinates.exe` to run.

---

## 🛠 How It Works
1. Launch the program (`address_to_coordinates.exe` or via Python).
2. Enter an address (e.g., `Rua do Beato 13, Lisbon`).
3. Click **"Get Coordinates"**.
4. The coordinates will appear in the window.

---

## ⚠️ Important Notes
- Keep the `.env` file **in the same folder** as the executable.
- Never share your API key publicly.
- For issues, open a [GitHub Issue](https://github.com/your-username/your-repo/issues).

---

## 📄 License
This project is open-source (MIT License). See `LICENSE` for details.

---

Let me know if you'd like to add screenshots or adjust the tone further! 😊