#!/usr/bin/env python3
"""
Exercise 2: Parse a Timing Report - Extract Startpoints
=======================================================

🎯 Goal: Extract all startpoints from a timing report
📝 Skills: String processing, regex, text parsing

This is a common interview question for physical design roles!
"""

import re

def extract_startpoints(report_text):
    """
    Given a multiline string representing a timing report,
    extract the names of startpoints (like 'cpu_inst/reg1').
    
    Sample format:
    Startpoint: cpu_inst/reg1 (rising edge-triggered flip-flop)
    Startpoint: memory_ctrl/addr_reg[0] (falling edge-triggered flip-flop)
    
    Args:
        report_text (str): Multiline timing report content
        
    Returns:
        list: List of startpoint names
    """
    # TODO: Implement this function
    # Hint: Look for lines starting with "Startpoint:" and extract the name
    # Hint: Use regex or string methods
    pass


def extract_startpoints_advanced(report_text):
    """
    Advanced version: Also extract the flip-flop type (rising/falling edge)
    
    Returns:
        list: List of tuples (startpoint_name, edge_type)
        Example: [('cpu_inst/reg1', 'rising'), ('memory_ctrl/addr_reg[0]', 'falling')]
    """
    # TODO: Implement this function
    pass


# Test data
SAMPLE_TIMING_REPORT = """
Information: Updating design information... (UID-85)
 
****************************************
Report : timing
        -path full
        -delay max
        -max_paths 10
Design : top_module
Version: P-2019.03-SP4
Date   : Mon Jan 15 14:23:45 2024
****************************************

Startpoint: cpu_inst/reg1 (rising edge-triggered flip-flop clocked by clk)
Endpoint: cpu_inst/reg2 (rising edge-triggered flip-flop clocked by clk)
Path Group: clk
Path Type: max

Point                                    Incr       Path
-----------------------------------------------------------
clock clk (rise edge)                    0.00       0.00
clock network delay (ideal)              0.00       0.00
cpu_inst/reg1/CK (DFFQX1)                0.00       0.00 r
cpu_inst/reg1/Q (DFFQX1)                 0.18       0.18 r
U15/Y (INVX2)                            0.07       0.25 f
U16/Y (NAND2X1)                          0.09       0.34 r
cpu_inst/reg2/D (DFFQX1)                 0.00       0.34 r
data arrival time                                   0.34

clock clk (rise edge)                    1.00       1.00
clock network delay (ideal)              0.00       1.00
cpu_inst/reg2/CK (DFFQX1)                0.00       1.00 r
library setup time                      -0.05       0.95
data required time                                  0.95
-----------------------------------------------------------
data required time                                  0.95
data arrival time                                  -0.34
-----------------------------------------------------------
slack (MET)                                         0.61


Startpoint: memory_ctrl/addr_reg[0] (falling edge-triggered flip-flop clocked by clk)
Endpoint: memory_ctrl/data_out[7] (rising edge-triggered flip-flop clocked by clk)
Path Group: clk
Path Type: max

Point                                    Incr       Path
-----------------------------------------------------------
clock clk (fall edge)                    0.50       0.50
clock network delay (ideal)              0.00       0.50
memory_ctrl/addr_reg[0]/CK (DFFQX1)      0.00       0.50 f
memory_ctrl/addr_reg[0]/Q (DFFQX1)       0.19       0.69 f
U20/Y (INVX1)                            0.12       0.81 r
U21/Y (AOI21X1)                          0.15       0.96 f
memory_ctrl/data_out[7]/D (DFFQX1)       0.00       0.96 f
data arrival time                                   0.96

Startpoint: io_ctrl/input_buf[3] (rising edge-triggered flip-flop clocked by clk)
Endpoint: io_ctrl/output_reg[1] (rising edge-triggered flip-flop clocked by clk)
Path Group: clk
Path Type: max
"""

def test_extract_startpoints():
    """Test the basic startpoint extraction function"""
    result = extract_startpoints(SAMPLE_TIMING_REPORT)
    expected = [
        'cpu_inst/reg1',
        'memory_ctrl/addr_reg[0]',
        'io_ctrl/input_buf[3]'
    ]
    
    print("🧪 Testing extract_startpoints()...")
    print(f"Expected: {expected}")
    print(f"Got:      {result}")
    
    if result == expected:
        print("✅ PASS: Basic startpoint extraction works!")
    else:
        print("❌ FAIL: Check your regex/string parsing")
    print()

def test_extract_startpoints_advanced():
    """Test the advanced startpoint extraction function"""
    result = extract_startpoints_advanced(SAMPLE_TIMING_REPORT)
    expected = [
        ('cpu_inst/reg1', 'rising'),
        ('memory_ctrl/addr_reg[0]', 'falling'),
        ('io_ctrl/input_buf[3]', 'rising')
    ]
    
    print("🧪 Testing extract_startpoints_advanced()...")
    print(f"Expected: {expected}")
    print(f"Got:      {result}")
    
    if result == expected:
        print("✅ PASS: Advanced startpoint extraction works!")
    else:
        print("❌ FAIL: Check edge type extraction")
    print()

if __name__ == "__main__":
    print("🚀 Exercise 2: Timing Report Parser")
    print("=" * 50)
    print()
    
    # Run tests
    test_extract_startpoints()
    test_extract_startpoints_advanced()
    
    print("💡 Hints:")
    print("- Look for lines containing 'Startpoint:'")
    print("- Extract the name between 'Startpoint:' and the first parenthesis")
    print("- For edge type, look for 'rising' or 'falling' in the same line")
    print("- Use regex pattern matching or string.split() methods")
    print()
    print("📚 Common regex patterns:")
    print("- r'Startpoint: (\\S+)' - captures the startpoint name")
    print("- r'(rising|falling) edge' - captures the edge type")