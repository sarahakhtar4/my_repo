#!/usr/bin/env python3
"""
Exercise 8: Find Duplicate Nets
===============================

🎯 Goal: Identify duplicate net names in netlist files
📝 Skills: File parsing, data structures, duplicate detection

Important for netlist validation and debugging connectivity issues.
"""

from collections import Counter, defaultdict

def find_duplicate_nets(netlist_content):
    """
    Given netlist content, identify and list duplicate net names.
    
    Args:
        netlist_content (str): Netlist file content
        
    Returns:
        list: List of duplicate net names
        
    Sample netlist format:
        net1 U1/A U2/B
        net2 U3/A U4/B  
        net1 U5/C U6/D    # This is a duplicate!
    """
    # TODO: Implement this function
    # Hint: Parse each line to extract net names
    # Hint: Use Counter or dictionary to track occurrences
    pass


def find_duplicate_nets_with_details(netlist_content):
    """
    Advanced version: Return detailed information about duplicates
    
    Returns:
        dict: {
            'duplicates': {net_name: count},
            'connections': {net_name: [list_of_connection_lines]},
            'summary': {
                'total_nets': int,
                'unique_nets': int, 
                'duplicate_nets': int,
                'total_violations': int
            }
        }
    """
    # TODO: Implement this function
    pass


def validate_netlist_format(netlist_content):
    """
    Validate netlist format and find various issues
    
    Returns:
        dict: {
            'duplicate_nets': list,
            'malformed_lines': list,
            'missing_connections': list,  # nets with < 2 connections
            'is_valid': bool
        }
    """
    # TODO: Implement this function
    # Check for: duplicates, malformed lines, incomplete connections
    pass


def generate_netlist_report(netlist_content, output_file=None):
    """
    Generate a comprehensive netlist validation report
    
    Returns:
        str: Formatted report text
    """
    # TODO: Implement this function
    pass


# Test data - Sample netlist with various issues
SAMPLE_NETLIST = """
# Sample netlist with duplicate nets
# Format: net_name pin1 pin2 [pin3 ...]

net1 U1/A U2/B
net2 U3/A U4/B
net3 U5/C U6/D U7/E
net1 U8/F U9/G
net4 U10/H U11/I
net5 U12/J U13/K U14/L
net2 U15/M U16/N
net6 U17/O U18/P
net7 U19/Q
net8 U20/R U21/S U22/T
net1 U23/U U24/V
net9 U25/W U26/X

# Invalid lines for testing
net10
invalid_line_no_connections
net11 U27/Y U28/Z
"""

def test_find_duplicate_nets():
    """Test basic duplicate net detection"""
    result = find_duplicate_nets(SAMPLE_NETLIST)
    expected = ['net1', 'net2']  # These appear multiple times
    
    print("🧪 Testing find_duplicate_nets()...")
    print(f"Expected duplicates: {expected}")
    print(f"Found duplicates: {result}")
    
    if result and set(result) == set(expected):
        print("✅ PASS: Basic duplicate detection works!")
    else:
        print("❌ FAIL: Check your parsing logic")
        print("💡 Tip: Look for net names that appear on multiple lines")
    print()

def test_duplicate_nets_with_details():
    """Test detailed duplicate analysis"""
    result = find_duplicate_nets_with_details(SAMPLE_NETLIST)
    
    print("🧪 Testing find_duplicate_nets_with_details()...")
    
    if result:
        duplicates = result.get('duplicates', {})
        connections = result.get('connections', {})
        summary = result.get('summary', {})
        
        print("Duplicates found:")
        for net, count in duplicates.items():
            print(f"  {net}: appears {count} times")
        
        print("Sample connections:")
        for net in list(connections.keys())[:3]:  # Show first 3
            print(f"  {net}: {connections[net]}")
        
        print(f"Summary: {summary}")
        
        expected_dups = {'net1': 3, 'net2': 2}
        if duplicates == expected_dups:
            print("✅ PASS: Detailed analysis works!")
        else:
            print("❌ FAIL: Check duplicate counting")
    else:
        print("❌ FAIL: Function not implemented")
    print()

def test_netlist_validation():
    """Test comprehensive netlist validation"""
    result = validate_netlist_format(SAMPLE_NETLIST)
    
    print("🧪 Testing validate_netlist_format()...")
    
    if result:
        print(f"Duplicate nets: {result.get('duplicate_nets', [])}")
        print(f"Malformed lines: {result.get('malformed_lines', [])}")
        print(f"Missing connections: {result.get('missing_connections', [])}")
        print(f"Is valid: {result.get('is_valid', False)}")
        
        # Check some expected results
        has_duplicates = 'net1' in result.get('duplicate_nets', [])
        has_malformed = len(result.get('malformed_lines', [])) > 0
        
        if has_duplicates and has_malformed:
            print("✅ PASS: Netlist validation works!")
        else:
            print("❌ FAIL: Check validation logic")
    else:
        print("❌ FAIL: Function not implemented")
    print()

def test_netlist_report():
    """Test report generation"""
    result = generate_netlist_report(SAMPLE_NETLIST)
    
    print("🧪 Testing generate_netlist_report()...")
    
    if result:
        print("Generated report preview:")
        print(result[:300] + "..." if len(result) > 300 else result)
        print("✅ PASS: Report generation works!")
    else:
        print("❌ FAIL: Function not implemented")
    print()

if __name__ == "__main__":
    print("🚀 Exercise 8: Duplicate Net Finder")
    print("=" * 50)
    print()
    
    # Show sample netlist
    print("📄 Sample netlist content:")
    lines = SAMPLE_NETLIST.strip().split('\n')[:15]  # Show first 15 lines
    for i, line in enumerate(lines, 1):
        if line.strip() and not line.strip().startswith('#'):
            print(f"  {i:2}: {line}")
    print("  ... (more lines)")
    print()
    
    # Run tests
    test_find_duplicate_nets()
    test_duplicate_nets_with_details()
    test_netlist_validation()
    test_netlist_report()
    
    print("💡 Hints:")
    print("- Parse each line: line.split() to get [net_name, pin1, pin2, ...]")
    print("- Skip comment lines (start with #) and empty lines")
    print("- Use Counter to count occurrences: Counter(net_names)")
    print("- Filter for counts > 1 to find duplicates")
    print("- Validate: check line has at least 3 parts (net + 2 pins)")
    print()
    print("📚 Useful tools:")
    print("- collections.Counter: counts occurrences")
    print("- collections.defaultdict: automatic list creation")
    print("- str.split(): splits line into parts")
    print("- str.strip(): removes whitespace")
    print()
    print("🎯 Real-world context:")
    print("- Duplicate nets can cause electrical conflicts")
    print("- Validation catches netlist errors early")
    print("- Reports help designers fix connectivity issues")