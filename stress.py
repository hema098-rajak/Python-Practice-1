"""
StressSense - Server
=====================
Reads heart rate (HR) and SpO2 from Arduino over USB Serial,
classifies stress level, and serves it to the dashboard webpage.

SETUP (one-time):
    pip install pyserial flask

RUN:
    python stress_server.py

Then open dashboard.html in your browser (double-click the file).
"""

import serial
import threading
import time
from flask import Flask, jsonify
from flask_cors import CORS

# ----------------------------------------------------------
# CONFIG — change these two values for your setup
# ----------------------------------------------------------
SERIAL_PORT = "COM7"     # <-- change to your Arduino's COM port
BAUD_RATE = 115200       # <-- must match Serial.begin() in your Arduino code

# ----------------------------------------------------------
# Shared data (updated by the serial-reading thread,
# read by the web server thread)
# ----------------------------------------------------------
latest_data = {
    "heartRate": 0,
    "spo2": 0,
    "stressLevel": "Low",
    "badge": "Calm",
    "className": "low",
    "suggestion": "Waiting for sensor data..."
}

lock = threading.Lock()


def classify_stress(hr, spo2):
    """
    Simple threshold-based stress classification.
    Tune these numbers based on real readings from your sensor.
    """
    if hr == 0:
        return {
            "stressLevel": "No Data",
            "badge": "Place Finger",
            "className": "medium",
            "suggestion": "Place your finger gently on the sensor to begin monitoring."
        }

    if hr < 75:
        return {
            "stressLevel": "Low",
            "badge": "Calm",
            "className": "low",
            "suggestion": "Great rhythm. Stay hydrated and keep up the good pace."
        }
    elif hr < 95:
        return {
            "stressLevel": "Medium",
            "badge": "Moderate",
            "className": "medium",
            "suggestion": "Heart rate is rising. Try 5 slow breaths — in for 4 seconds, out for 6."
        }
    else:
        return {
            "stressLevel": "High",
            "badge": "Elevated",
            "className": "high",
            "suggestion": "Stress detected. Pause for 2 minutes, step away from your screen, and breathe deeply."
        }


def read_serial():
    """
    Background thread: continuously reads lines from Arduino.
    Expected Arduino output format (from your existing sketch):
        Heart rate: 78 SpO2: 97
    """
    while True:
        try:
            ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout=2)
            print(f"[OK] Connected to {SERIAL_PORT}")

            while True:
                line = ser.readline().decode("utf-8", errors="ignore").strip()
                if not line:
                    continue

                # Expecting something like: "Heart rate: 78 SpO2: 97"
                if "Heart rate:" in line and "SpO2:" in line:
                    try:
                        hr_part = line.split("Heart rate:")[1].split("SpO2:")[0].strip()
                        spo2_part = line.split("SpO2:")[1].strip()

                        hr = int(float(hr_part))
                        spo2 = int(float(spo2_part))

                        result = classify_stress(hr, spo2)

                        with lock:
                            latest_data["heartRate"] = hr
                            latest_data["spo2"] = spo2
                            latest_data.update(result)

                        print(f"HR={hr} SpO2={spo2} -> {result['stressLevel']}")

                    except (ValueError, IndexError):
                        # Ignore lines that don't parse cleanly
                        pass

        except serial.SerialException as e:
            print(f"[ERROR] Could not open {SERIAL_PORT}: {e}")
            print("Retrying in 3 seconds...")
            time.sleep(3)


# ----------------------------------------------------------
# Web server
# ----------------------------------------------------------
app = Flask(_name_)
CORS(app)  # allows dashboard.html (opened as a file) to fetch this data


@app.route("/data")
def get_data():
    with lock:
        return jsonify(latest_data)


if _name_ == "_main_":
    # Start the serial reader in the background
    t = threading.Thread(target=read_serial, daemon=True)
    t.start()

    print("Server running at http://127.0.0.1:5000/data")
    print("Open dashboard.html in your browser now.")
    app.run(port=5000)