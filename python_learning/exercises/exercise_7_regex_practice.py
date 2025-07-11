#!/usr/bin/env python3
"""
Exercise 7: Regex Practice - Extract Float Numbers
==================================================

🎯 Goal: Extract all floating-point values from strings
📝 Skills: Regular expressions, pattern matching, number parsing

Essential skill for parsing EDA reports with numerical data.
"""

import re

def extract_floats(text):
    """
    Extract all floating-point values from a string.
    
    Args:
        text (str): Input string containing numbers
        
    Returns:
        list: List of float values found in the string
    
    Example:
        "cell U1: power=0.15, delay=2.3ns, slew=0.09" → [0.15, 2.3, 0.09]
    """
    # TODO: Implement this function
    # Hint: Use re.findall() with a regex pattern for floating point numbers
    # Hint: Pattern should match: 123.45, .45, 123., 1.23e-4, etc.
    pass


def extract_floats_with_units(text):
    """
    Advanced version: Extract floats along with their units
    
    Args:
        text (str): Input string
        
    Returns:
        list: List of tuples (value, unit) where unit might be None
        
    Example:
        "delay=2.3ns, power=0.15mW" → [(2.3, 'ns'), (0.15, 'mW')]
    """
    # TODO: Implement this function
    # Hint: Use capturing groups in regex to get both number and unit
    pass


def extract_scientific_notation(text):
    """
    Extract numbers in scientific notation (e.g., 1.23e-4, 5.67E+2)
    
    Args:
        text (str): Input string
        
    Returns:
        list: List of float values in scientific notation
    """
    # TODO: Implement this function
    # Hint: Pattern should match: 1.23e-4, 5E+2, 1.5e10, etc.
    pass


def parse_timing_report_line(line):
    """
    Parse a timing report line and extract all timing values
    
    Args:
        line (str): Line from timing report
        
    Returns:
        dict: Dictionary with extracted timing information
    
    Example input:
        "U15/Y (INVX2)                            0.07       0.25 f"
    Expected output:
        {
            'cell': 'U15/Y',
            'cell_type': 'INVX2', 
            'incr_delay': 0.07,
            'path_delay': 0.25,
            'transition': 'f'
        }
    """
    # TODO: Implement this function
    # Hint: Use multiple regex patterns or one complex pattern with groups
    pass


# Test data
TEST_STRINGS = [
    "cell U1: power=0.15, delay=2.3ns, slew=0.09",
    "capacitance: 1.23e-3pF, resistance: 45.67ohm",
    "Setup slack: -0.142ns, Hold slack: 0.089ns",
    "Area: 156.78um2, Power: 2.34e-4W",
    "Frequency: 500.0MHz, Period: 2.0ns",
    "Temperature: 25.5C, Voltage: 1.1V",
    "scientific: 1.23e-4, 5.67E+2, 8.9e10, 1E-6"
]

TIMING_REPORT_LINES = [
    "clock clk (rise edge)                    0.00       0.00",
    "clock network delay (ideal)              0.00       0.00",
    "cpu_inst/reg1/CK (DFFQX1)                0.00       0.00 r",
    "cpu_inst/reg1/Q (DFFQX1)                 0.18       0.18 r",
    "U15/Y (INVX2)                            0.07       0.25 f",
    "U16/Y (NAND2X1)                          0.09       0.34 r",
    "cpu_inst/reg2/D (DFFQX1)                 0.00       0.34 r",
    "data arrival time                                   0.34",
    "library setup time                      -0.05       0.95"
]

def test_extract_floats():
    """Test basic float extraction"""
    print("🧪 Testing extract_floats()...")
    
    for i, test_str in enumerate(TEST_STRINGS[:4]):  # Test first 4 strings
        result = extract_floats(test_str)
        print(f"Text {i+1}: {test_str}")
        print(f"Extracted: {result}")
        
        if result:
            print(f"✅ Found {len(result)} numbers")
        else:
            print("❌ No numbers found - check your regex")
        print()

def test_extract_floats_with_units():
    """Test float extraction with units"""
    print("🧪 Testing extract_floats_with_units()...")
    
    test_str = "delay=2.3ns, power=0.15mW, cap=1.5pF"
    result = extract_floats_with_units(test_str)
    expected = [(2.3, 'ns'), (0.15, 'mW'), (1.5, 'pF')]
    
    print(f"Text: {test_str}")
    print(f"Result: {result}")
    print(f"Expected: {expected}")
    
    if result == expected:
        print("✅ PASS: Unit extraction works!")
    else:
        print("❌ FAIL: Check your regex pattern")
    print()

def test_scientific_notation():
    """Test scientific notation extraction"""
    print("🧪 Testing extract_scientific_notation()...")
    
    test_str = TEST_STRINGS[6]  # Scientific notation string
    result = extract_scientific_notation(test_str)
    expected = [1.23e-4, 5.67e2, 8.9e10, 1e-6]
    
    print(f"Text: {test_str}")
    print(f"Result: {result}")
    print(f"Expected: {expected}")
    
    if result and len(result) == len(expected):
        # Check if values are approximately equal
        all_close = all(abs(a - b) < 1e-10 for a, b in zip(result, expected))
        if all_close:
            print("✅ PASS: Scientific notation works!")
        else:
            print("❌ FAIL: Values don't match expected")
    else:
        print("❌ FAIL: Wrong number of values extracted")
    print()

def test_timing_report_parsing():
    """Test timing report line parsing"""
    print("🧪 Testing parse_timing_report_line()...")
    
    test_line = "U15/Y (INVX2)                            0.07       0.25 f"
    result = parse_timing_report_line(test_line)
    
    expected = {
        'cell': 'U15/Y',
        'cell_type': 'INVX2',
        'incr_delay': 0.07,
        'path_delay': 0.25,
        'transition': 'f'
    }
    
    print(f"Line: {test_line}")
    print(f"Result: {result}")
    print(f"Expected: {expected}")
    
    if result == expected:
        print("✅ PASS: Timing line parsing works!")
    else:
        print("❌ FAIL: Check your parsing logic")
    print()

if __name__ == "__main__":
    print("🚀 Exercise 7: Regex Practice - Float Extraction")
    print("=" * 60)
    print()
    
    # Run tests
    test_extract_floats()
    test_extract_floats_with_units()
    test_scientific_notation()
    test_timing_report_parsing()
    
    print("💡 Hints:")
    print("- Basic float pattern: r'\\d+\\.\\d+' or r'\\d*\\.\\d+|\\d+\\.'")
    print("- Scientific notation: r'\\d+\\.?\\d*[eE][+-]?\\d+'")
    print("- With units: r'(\\d+\\.\\d+)([a-zA-Z]+)'")
    print("- Use re.findall() to get all matches")
    print("- Convert strings to float: float(match)")
    print()
    print("📚 Regex patterns:")
    print("- \\d+ : one or more digits")
    print("- \\d* : zero or more digits") 
    print("- \\. : literal dot (escaped)")
    print("- [eE] : e or E")
    print("- [+-]? : optional + or -")
    print("- () : capturing group")
    print()
    print("🎯 Challenge: Try parsing complex timing report formats!")