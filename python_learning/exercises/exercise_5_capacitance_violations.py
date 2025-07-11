#!/usr/bin/env python3
"""
Exercise 5: Max Capacitance Violation Finder
============================================

🎯 Goal: Find pins that violate maximum capacitance limits
📝 Skills: Dictionary operations, filtering, data analysis

Common task in physical design - identifying design rule violations.
"""

def find_cap_violations(pins, max_cap):
    """
    Given a dictionary of pins and their capacitance, 
    return only those that violate max capacitance.
    
    Args:
        pins (dict): {pin_name: capacitance_value}
        max_cap (float): Maximum allowed capacitance
        
    Returns:
        dict: {pin_name: capacitance_value} for violating pins only
    """
    # TODO: Implement this function
    # Hint: Filter dictionary items where value > max_cap
    pass


def find_violations_with_margin(pins, max_cap, margin_percent=10):
    """
    Advanced version: Find violations with a safety margin
    
    Args:
        pins (dict): {pin_name: capacitance_value}
        max_cap (float): Maximum allowed capacitance
        margin_percent (float): Safety margin percentage
        
    Returns:
        dict: {
            'hard_violations': {pin: cap},  # cap > max_cap
            'soft_violations': {pin: cap},  # cap > max_cap * (1 - margin/100)
            'summary': {
                'total_pins': int,
                'hard_violations': int,
                'soft_violations': int,
                'worst_violation': (pin, cap, percentage_over)
            }
        }
    """
    # TODO: Implement this function
    pass


def generate_violation_report(violations, max_cap, output_file=None):
    """
    Generate a formatted violation report
    
    Args:
        violations (dict): Result from find_cap_violations()
        max_cap (float): Maximum allowed capacitance
        output_file (str, optional): If provided, write report to file
        
    Returns:
        str: Formatted report text
    """
    # TODO: Implement this function
    # Hint: Create a nicely formatted text report
    # Hint: Include violation percentage, sort by severity
    pass


# Test data
TEST_PINS = {
    'cpu_inst/reg1/D': 0.08,
    'cpu_inst/reg2/CK': 0.12,  # Violation
    'memory_ctrl/addr[0]': 0.15,  # Violation
    'memory_ctrl/addr[1]': 0.09,
    'io_ctrl/data_out[7]': 0.11,  # Violation
    'io_ctrl/data_out[6]': 0.07,
    'clk_gen/pll_out': 0.25,  # Major violation
    'power_ctrl/enable': 0.05,
    'debug_port/tdo': 0.13,  # Violation
    'debug_port/tdi': 0.06,
}

MAX_CAPACITANCE = 0.10  # 100fF limit

def test_find_cap_violations():
    """Test the basic violation finder"""
    result = find_cap_violations(TEST_PINS, MAX_CAPACITANCE)
    
    expected = {
        'cpu_inst/reg2/CK': 0.12,
        'memory_ctrl/addr[0]': 0.15,
        'io_ctrl/data_out[7]': 0.11,
        'clk_gen/pll_out': 0.25,
        'debug_port/tdo': 0.13,
    }
    
    print("🧪 Testing find_cap_violations()...")
    print(f"Max capacitance limit: {MAX_CAPACITANCE}")
    print(f"Total pins: {len(TEST_PINS)}")
    print(f"Expected violations: {len(expected)}")
    print(f"Found violations: {len(result) if result else 0}")
    
    if result == expected:
        print("✅ PASS: Violation detection works!")
        print("Violating pins:")
        for pin, cap in sorted(result.items(), key=lambda x: x[1], reverse=True):
            violation_pct = ((cap - MAX_CAPACITANCE) / MAX_CAPACITANCE) * 100
            print(f"  {pin}: {cap:.3f} ({violation_pct:.1f}% over limit)")
    else:
        print("❌ FAIL: Check your filtering logic")
        if result:
            print(f"Got: {result}")
        print(f"Expected: {expected}")
    
    print()

def test_advanced_violations():
    """Test the advanced violation finder with margins"""
    result = find_violations_with_margin(TEST_PINS, MAX_CAPACITANCE, margin_percent=10)
    
    print("🧪 Testing find_violations_with_margin()...")
    
    if result:
        print("Hard violations (> limit):")
        for pin, cap in result.get('hard_violations', {}).items():
            print(f"  {pin}: {cap:.3f}")
        
        print("Soft violations (> 90% of limit):")
        for pin, cap in result.get('soft_violations', {}).items():
            print(f"  {pin}: {cap:.3f}")
            
        summary = result.get('summary', {})
        print(f"Summary: {summary}")
        
        if summary.get('total_pins') == len(TEST_PINS):
            print("✅ PASS: Advanced analysis works!")
        else:
            print("❌ FAIL: Check summary calculations")
    else:
        print("❌ FAIL: Function not implemented")
    
    print()

def test_violation_report():
    """Test the report generation"""
    violations = find_cap_violations(TEST_PINS, MAX_CAPACITANCE)
    
    if violations:
        report = generate_violation_report(violations, MAX_CAPACITANCE)
        
        print("🧪 Testing generate_violation_report()...")
        if report:
            print("Generated report:")
            print(report)
            print("✅ PASS: Report generation works!")
        else:
            print("❌ FAIL: Report generation not implemented")
    else:
        print("⚠️  SKIP: Can't test report without working violation finder")
    
    print()

if __name__ == "__main__":
    print("🚀 Exercise 5: Capacitance Violation Finder")
    print("=" * 60)
    print()
    
    # Show test data
    print("📊 Test pin data:")
    for pin, cap in sorted(TEST_PINS.items()):
        status = "VIOLATION" if cap > MAX_CAPACITANCE else "OK"
        print(f"  {pin:25} {cap:.3f}  [{status}]")
    print()
    
    # Run tests
    test_find_cap_violations()
    test_advanced_violations()
    test_violation_report()
    
    print("💡 Hints:")
    print("- Use dictionary comprehension: {k: v for k, v in pins.items() if condition}")
    print("- Sort violations by severity: sorted(dict.items(), key=lambda x: x[1], reverse=True)")
    print("- Calculate violation percentage: ((actual - limit) / limit) * 100")
    print("- For margins: soft_limit = max_cap * (1 - margin/100)")
    print()
    print("📚 Real-world context:")
    print("- Capacitance violations can cause timing failures")
    print("- Safety margins help catch problems early")
    print("- Reports should be sorted by severity for triage")