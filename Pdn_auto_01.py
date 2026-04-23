import pyvisa  
import time    
import csv     
from datetime import datetime 

# Instrument addresses (Standard VISA format)
PSU_ADDR = "USB0::0x05E6::0x2230::INSTR"   
LOAD_ADDR = "USB0::0x05E6::0x2380::INSTR"  
SCOPE_ADDR = "USB0::0x0957::0x1790::INSTR" 

def run_pdn_test(rail_name, target_v, load_a):
    rm = pyvisa.ResourceManager()
    try:
        psu = rm.open_resource(PSU_ADDR)
        eload = rm.open_resource(LOAD_ADDR)
        scope = rm.open_resource(SCOPE_ADDR)

        # Power Up
        psu.write("VOLT 5.0")  
        psu.write("OUTP ON")   
        time.sleep(1)          

        # Ripple Measurement
        eload.write(f"CURR {load_a}") 
        eload.write("OUTP ON")
        time.sleep(0.5)
        v_pp = float(scope.query(":MEASure:VPP?")) 

        # Transient Measurement
        eload.write("OUTP OFF") 
        scope.write(":SINGle")  
        eload.write("OUTP ON")  
        v_min = float(scope.query(":MEASure:VMIN?")) 

        # Logic: Ripple must be < 50mV and Voltage within +/- 5%
        status = "PASS" if (v_pp < 0.050 and v_min > (target_v * 0.95)) else "FAIL"

        # Save results to a CSV file
        with open('Production_Report.csv', 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([datetime.now(), rail_name, v_pp, v_min, status])

    finally:
        psu.write("OUTP OFF")
        eload.write("OUTP OFF")

if __name__ == "__main__":
    # Create the report header
    with open('Production_Report.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(["Timestamp", "Rail", "Ripple_Vpp", "Transient_Vmin", "Result"])

    # Run tests for each rail from the Annexure
    run_pdn_test("+3V6", 3.6, 2.5)
    run_pdn_test("+1V8", 1.8, 3.0)
    run_pdn_test("+3V3", 3.3, 3.0)
    run_pdn_test("+2V5", 2.5, 1.5)
  
