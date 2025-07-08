#!/usr/bin/env python3
"""
Exercise 1: Basic Timing Report Parsing
=======================================

Practice extracting key information from timing report snippets.
This builds the fundamental skills you'll need for the interview example.

Instructions:
1. Complete the functions below
2. Run this script to test your solutions
3. All tests should pass when implemented correctly
"""

import re

# Sample timing report data for practice
sample_data = """
Startpoint: cpu_core/alu_inst/reg_15
            (rising edge-triggered flip-flop clocked by clk)
Endpoint: memory_ctrl/addr_reg_7
          (rising edge-triggered flip-flop clocked by clk)
Path Group: clk
Path Type: max

Point                           Incr       Path
---------------------------------------------
clock clk (rise edge)           0.00       0.00
clock network delay (ideal)     0.00       0.00
cpu_core/alu_inst/reg_15/CK     0.00       0.00 r
cpu_core/alu_inst/reg_15/Q      0.145      0.145 r
U123/Y (INVX1)                  0.042      0.187 f
U124/Y (NAND2X1)                0.058      0.245 r
memory_ctrl/addr_reg_7/D        0.000      0.245 r
data arrival time                          0.245

clock clk (rise edge)           1.000      1.000
clock network delay (ideal)     0.000      1.000
memory_ctrl/addr_reg_7/CK       0.000      1.000 r
library setup time             -0.085      0.915
data required time                         0.915

slack (VIOLATED)                          -0.670
"""

# TODO: Complete these functions (remove 'pass' and implement)

def extract_startpoint(report_text):
    """
    Extract the startpoint from timing report text.
    
    Expected output for sample_data: "cpu_core/alu_inst/reg_15"
    """
    # HINT: Use re.search() to find the pattern after "Startpoint:"
    # Remove the description in parentheses for cleaner output
    pass

def extract_endpoint(report_text):
    """
    Extract the endpoint from timing report text.
    
    Expected output for sample_data: "memory_ctrl/addr_reg_7"
    """
    # HINT: Similar to startpoint, but look for "Endpoint:"
    pass

def extract_slack(report_text):
    """
    Extract the slack value from timing report text.
    
    Expected output for sample_data: -0.670
    """
    # HINT: Look for "slack" followed by numbers, handle negative values
    pass

def extract_timing_values(report_text):
    """
    Extract arrival time and required time.
    
    Expected output for sample_data: (0.245, 0.915)
    """
    # HINT: Look for "data arrival time" and "data required time"
    # Return as tuple: (arrival_time, required_time)
    pass

def count_logic_levels(report_text):
    """
    Count the number of logic levels in the path.
    
    Expected output for sample_data: 2 (U123 and U124)
    """
    # HINT: Count lines that contain gate names like "U123/Y"
    pass

def find_critical_gate(report_text):
    """
    Find the gate with the largest delay contribution.
    
    Expected output for sample_data: "U124/Y"
    """
    # HINT: Parse the path section and find the gate with max "Incr" value
    pass

# Test framework (don't modify)
def run_tests():
    """Test your implementations"""
    print("Testing your solutions...\n")
    
    tests = [
        ("extract_startpoint", extract_startpoint, "cpu_core/alu_inst/reg_15"),
        ("extract_endpoint", extract_endpoint, "memory_ctrl/addr_reg_7"),
        ("extract_slack", extract_slack, -0.670),
        ("extract_timing_values", extract_timing_values, (0.245, 0.915)),
        ("count_logic_levels", count_logic_levels, 2),
        ("find_critical_gate", find_critical_gate, "U124/Y"),
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, func, expected in tests:
        try:
            result = func(sample_data)
            if result == expected:
                print(f"✅ {test_name}: PASSED")
                passed += 1
            else:
                print(f"❌ {test_name}: FAILED")
                print(f"   Expected: {expected}")
                print(f"   Got: {result}")
        except Exception as e:
            print(f"❌ {test_name}: ERROR - {e}")
    
    print(f"\nResults: {passed}/{total} tests passed")
    
    if passed == total:
        print("🎉 Congratulations! All tests passed!")
        print("You're ready for Exercise 2!")
    else:
        print("💡 Keep working on the failing tests.")
        print("Hint: Check the sample data above and use regex patterns.")

if __name__ == "__main__":
    print("=== Exercise 1: Basic Timing Report Parsing ===")
    print("Complete the functions above, then run this script to test.")
    print("Sample data is provided - study it to understand the patterns.\n")
    
    run_tests()