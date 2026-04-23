# PDN-AUTO-TEST
# Power Distribution Network Test Automation

This repository contains the automated test suite for qualifying a PDN. 

### Features
- **Instrument Control:** Automated SCPI communication with Keithley PSU/Load and Keysight Oscilloscope.
- **Automated Rail Testing:** Sequential testing of +3.6V, +1.8V, +3.3V, and +2.5V rails.
- **Pass/Fail Logic:** Verifies output ripple (<50mV) and transient stability (±5% tolerance).
- **Production Ready:** Generates a CSV report for unit traceability (e.g., SN-017).

### Hardware Requirements
- Keithley 2230-30-1 (Power Supply)
- Keithley 2380 (Electronic Load)
- Keysight DSOX6004A (Oscilloscope)

