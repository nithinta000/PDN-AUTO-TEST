# Satellite PDN Automated Test
This repository contains the test automation suite for qualifying a 4-rail satellite payload Power Distribution Network (PDN). It focuses on ensuring flight-readiness by verifying voltage stability under load and checking for high-frequency switching noise.

###  Key Features
- **Instrument Control:** Automated SCPI communication via PyVISA to control test hardware.
- **Interactive Test Flow:** The script pauses between each rail to allow the human operator to safely move the physical test probes, preventing accidental short circuits.
- **Dual Verification:** Measures both steady-state Ripple (<50mV) and Load Transient response (±5% tolerance) for every rail.
- **Production Traceability:** Automatically generates a timestamped `Production_Report.csv` file for batch record keeping (e.g., SN-017).

### 🛠️ Hardware Requirements
- **Power Supply:** Keithley 2230-30-1
- **Electronic Load:** Keithley 2380 Series
- **Oscilloscope:** Keysight DSOX6004A

### 📋 Testing Procedure
1. Connect all test hardware to the computer via USB.
2. Install the required Python libraries:
   ```bash
   pip install -r requirements.txt
   
