#!/usr/bin/env python3
"""
Exercise 6: Custom TCL Script Generator
======================================

🎯 Goal: Generate TCL scripts for EDA tools
📝 Skills: String formatting, file I/O, template generation

Common task - generating repetitive EDA tool commands from data.
"""

def generate_dont_use_script(cell_list, output_file=None):
    """
    Create a function that takes a list of cells and generates 
    a set_dont_use TCL script.
    
    Args:
        cell_list (list): List of cell names to mark as dont_use
        output_file (str, optional): Output file path
        
    Returns:
        str: Generated TCL script content
    """
    # TODO: Implement this function
    # Output format should be:
    # set_dont_use "cell1"
    # set_dont_use "cell2" 
    pass


def generate_multi_corner_script(corners, cell_list, script_type='dont_use'):
    """
    Advanced version: Generate multi-corner TCL script
    
    Args:
        corners (list): List of corner names ['ss', 'tt', 'ff']
        cell_list (list): List of cell names
        script_type (str): Type of script ('dont_use', 'dont_touch', 'size_only')
        
    Returns:
        str: Multi-corner TCL script
    """
    # TODO: Implement this function
    # Should generate corner-specific commands
    pass


def generate_constraint_script(constraints_dict, output_file=None):
    """
    Generate TCL script for timing constraints
    
    Args:
        constraints_dict (dict): {
            'clocks': [{'name': 'clk', 'period': 2.0, 'port': 'CLK'}],
            'input_delays': [{'port': 'data_in', 'delay': 0.5, 'clock': 'clk'}],
            'output_delays': [{'port': 'data_out', 'delay': 0.3, 'clock': 'clk'}],
            'false_paths': [{'from': 'reset', 'to': 'all_registers'}]
        }
        output_file (str, optional): Output file path
        
    Returns:
        str: Generated constraint script
    """
    # TODO: Implement this function
    pass


# Test data
TEST_CELLS = [
    'INVX1',
    'NAND2X1', 
    'NOR2X1',
    'AOI21X1',
    'OAI21X1',
    'BUFX2',
    'DFFQX1'
]

TEST_CORNERS = ['ss', 'tt', 'ff']

TEST_CONSTRAINTS = {
    'clocks': [
        {'name': 'clk', 'period': 2.0, 'port': 'CLK'},
        {'name': 'clk2', 'period': 4.0, 'port': 'CLK2'}
    ],
    'input_delays': [
        {'port': 'data_in[*]', 'delay': 0.5, 'clock': 'clk'},
        {'port': 'addr[*]', 'delay': 0.3, 'clock': 'clk'}
    ],
    'output_delays': [
        {'port': 'data_out[*]', 'delay': 0.4, 'clock': 'clk'},
        {'port': 'valid', 'delay': 0.2, 'clock': 'clk'}
    ],
    'false_paths': [
        {'from': 'reset', 'to': 'all_registers'},
        {'from': 'test_mode', 'to': '*'}
    ]
}

def test_generate_dont_use_script():
    """Test the basic TCL script generation"""
    result = generate_dont_use_script(TEST_CELLS)
    
    print("🧪 Testing generate_dont_use_script()...")
    
    if result:
        print("Generated script:")
        print(result)
        
        # Check if script has the right number of lines
        lines = [line.strip() for line in result.split('\n') if line.strip()]
        expected_lines = len(TEST_CELLS)
        
        # Check if all cells are included
        all_cells_included = all(cell in result for cell in TEST_CELLS)
        has_set_dont_use = 'set_dont_use' in result
        
        if (len(lines) == expected_lines and 
            all_cells_included and 
            has_set_dont_use):
            print("✅ PASS: TCL script generation works!")
        else:
            print("❌ FAIL: Check script format")
            print(f"Expected {expected_lines} lines, got {len(lines)}")
            print(f"All cells included: {all_cells_included}")
            print(f"Has set_dont_use: {has_set_dont_use}")
    else:
        print("❌ FAIL: Function not implemented")
    
    print()

def test_multi_corner_script():
    """Test the multi-corner script generation"""
    result = generate_multi_corner_script(TEST_CORNERS, TEST_CELLS[:3])
    
    print("🧪 Testing generate_multi_corner_script()...")
    
    if result:
        print("Generated multi-corner script:")
        print(result[:500] + "..." if len(result) > 500 else result)
        
        # Check if all corners are included
        all_corners_included = all(corner in result for corner in TEST_CORNERS)
        
        if all_corners_included:
            print("✅ PASS: Multi-corner script works!")
        else:
            print("❌ FAIL: Not all corners included")
    else:
        print("❌ FAIL: Function not implemented")
    
    print()

def test_constraint_script():
    """Test the constraint script generation"""
    result = generate_constraint_script(TEST_CONSTRAINTS)
    
    print("🧪 Testing generate_constraint_script()...")
    
    if result:
        print("Generated constraint script:")
        print(result)
        
        # Check for key constraint commands
        has_create_clock = 'create_clock' in result
        has_input_delay = 'set_input_delay' in result
        has_output_delay = 'set_output_delay' in result
        has_false_path = 'set_false_path' in result
        
        if (has_create_clock and has_input_delay and 
            has_output_delay and has_false_path):
            print("✅ PASS: Constraint script generation works!")
        else:
            print("❌ FAIL: Missing constraint commands")
            print(f"create_clock: {has_create_clock}")
            print(f"set_input_delay: {has_input_delay}")
            print(f"set_output_delay: {has_output_delay}")
            print(f"set_false_path: {has_false_path}")
    else:
        print("❌ FAIL: Function not implemented")
    
    print()

if __name__ == "__main__":
    print("🚀 Exercise 6: TCL Script Generator")
    print("=" * 50)
    print()
    
    # Show test data
    print("📋 Test cells:", TEST_CELLS)
    print("📋 Test corners:", TEST_CORNERS)
    print()
    
    # Run tests
    test_generate_dont_use_script()
    test_multi_corner_script()
    test_constraint_script()
    
    print("💡 Hints:")
    print("- Use string formatting: f'set_dont_use \"{cell}\"'")
    print("- Join lines with '\\n': '\\n'.join(lines)")
    print("- For multi-corner: iterate through corners and cells")
    print("- For constraints: different command formats for different types")
    print()
    print("📚 Common TCL commands:")
    print("- set_dont_use \"CELL_NAME\"")
    print("- create_clock -period 2.0 [get_ports CLK]")
    print("- set_input_delay 0.5 -clock clk [get_ports data_in]")
    print("- set_false_path -from [get_ports reset]")
    print()
    print("🎯 Extension: Try saving scripts to files!")