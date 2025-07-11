#!/usr/bin/env python3
"""
Exercise 3: Summarize a .lib File Snippet
==========================================

🎯 Goal: Count cells and pins in Liberty file format
📝 Skills: Pattern matching, counting, text analysis

Liberty (.lib) files define timing and power characteristics of standard cells.
"""

import re

def summarize_lib(lib_text):
    """
    Count number of 'cell' and 'pin' entries in Liberty file text.
    
    Args:
        lib_text (str): Liberty file content
        
    Returns:
        dict: {'cell_count': X, 'pin_count': Y}
    """
    # TODO: Implement this function
    # Hint: Look for patterns like "cell (CELL_NAME)" and "pin (PIN_NAME)"
    # Hint: Use regex or count occurrences of specific patterns
    pass


def summarize_lib_advanced(lib_text):
    """
    Advanced version: Also count different pin types (input, output, inout)
    
    Returns:
        dict: {
            'cell_count': X, 
            'pin_count': Y,
            'input_pins': Z,
            'output_pins': W,
            'inout_pins': V
        }
    """
    # TODO: Implement this function
    # Hint: Look for "direction : input/output/inout" after pin definitions
    pass


# Test data - Sample Liberty file snippet
SAMPLE_LIB_FILE = """
library(sample_lib) {
    delay_model : table_lookup;
    time_unit : "1ns";
    voltage_unit : "1V";
    current_unit : "1uA";
    capacitive_load_unit(1,pf);
    
    cell (INVX1) {
        area : 2.3;
        pin (A) {
            direction : input;
            capacitance : 0.05;
        }
        pin (Y) {
            direction : output;
            function : "!A";
            timing() {
                related_pin : "A";
                cell_rise(lu_table_template) {
                    values("0.1, 0.2, 0.3");
                }
            }
        }
    }
    
    cell (NAND2X1) {
        area : 3.1;
        pin (A) {
            direction : input;
            capacitance : 0.04;
        }
        pin (B) {
            direction : input;
            capacitance : 0.04;
        }
        pin (Y) {
            direction : output;
            function : "!(A & B)";
        }
    }
    
    cell (DFFQX1) {
        ff(IQ, IQN) {
            next_state : "D";
            clocked_on : "CK";
        }
        area : 8.5;
        pin (D) {
            direction : input;
            capacitance : 0.03;
        }
        pin (CK) {
            direction : input;
            capacitance : 0.02;
        }
        pin (Q) {
            direction : output;
            function : "IQ";
        }
        pin (QN) {
            direction : output;
            function : "IQN";
        }
    }
    
    cell (BUFX2) {
        area : 2.8;
        pin (A) {
            direction : input;
            capacitance : 0.06;
        }
        pin (Y) {
            direction : output;
            function : "A";
        }
    }
    
    cell (TRIBUFX1) {
        area : 4.2;
        pin (A) {
            direction : input;
            capacitance : 0.04;
        }
        pin (EN) {
            direction : input;
            capacitance : 0.03;
        }
        pin (Y) {
            direction : inout;
            function : "A";
            three_state : "EN";
        }
    }
}
"""

def test_summarize_lib():
    """Test the basic lib summarization function"""
    result = summarize_lib(SAMPLE_LIB_FILE)
    expected = {'cell_count': 5, 'pin_count': 13}
    
    print("🧪 Testing summarize_lib()...")
    print(f"Expected: {expected}")
    print(f"Got:      {result}")
    
    if result == expected:
        print("✅ PASS: Basic lib counting works!")
    else:
        print("❌ FAIL: Check your counting logic")
        print("💡 Tip: Count 'cell (' and 'pin (' patterns")
    print()

def test_summarize_lib_advanced():
    """Test the advanced lib summarization function"""
    result = summarize_lib_advanced(SAMPLE_LIB_FILE)
    expected = {
        'cell_count': 5, 
        'pin_count': 13,
        'input_pins': 9,
        'output_pins': 3,
        'inout_pins': 1
    }
    
    print("🧪 Testing summarize_lib_advanced()...")
    print(f"Expected: {expected}")
    print(f"Got:      {result}")
    
    if result == expected:
        print("✅ PASS: Advanced lib analysis works!")
    else:
        print("❌ FAIL: Check pin direction counting")
        print("💡 Tip: Look for 'direction : input/output/inout' patterns")
    print()

if __name__ == "__main__":
    print("🚀 Exercise 3: Liberty File Parser")
    print("=" * 50)
    print()
    
    # Show sample of what we're parsing
    print("📄 Sample .lib content preview:")
    print(SAMPLE_LIB_FILE[:300] + "...")
    print()
    
    # Run tests
    test_summarize_lib()
    test_summarize_lib_advanced()
    
    print("💡 Hints:")
    print("- Look for 'cell (' pattern to count cells")
    print("- Look for 'pin (' pattern to count pins")
    print("- For directions, find 'direction : input/output/inout' after pin definitions")
    print("- Use re.findall() to find all matches")
    print()
    print("📚 Useful regex patterns:")
    print("- r'cell \\(' - matches cell definitions")
    print("- r'pin \\(' - matches pin definitions")
    print("- r'direction\\s*:\\s*(input|output|inout)' - matches pin directions")