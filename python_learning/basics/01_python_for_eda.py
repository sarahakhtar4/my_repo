#!/usr/bin/env python3
"""
Python Basics for EDA and Physical Design
=========================================

This tutorial covers Python fundamentals specifically useful for EDA scripting,
timing analysis, and physical design tasks.
"""

# 1. IMPORTS AND MODULES
# Always organize imports at the top
import os
import re
import sys
from pathlib import Path
from collections import defaultdict, Counter
# Note: pandas is optional - remove this import if not available
# import pandas as pd

print("=== Python Basics for EDA ===\n")

# 2. STRING PROCESSING (Critical for parsing reports)
print("1. STRING PROCESSING:")

# Common EDA file parsing scenarios
timing_line = "slack (MET)             :    0.142ns  (required time - arrival time)"
setup_line = "  Data Arrival Time      :   2.858ns"
hold_line = "  Data Required Time     :   2.900ns"

# Extract numbers using regular expressions
import re

def extract_timing_value(line):
    """Extract timing value from a line - common EDA task"""
    # Look for numbers followed by time units
    match = re.search(r'([-+]?\d*\.?\d+)\s*(ns|ps)', line)
    if match:
        value = float(match.group(1))
        unit = match.group(2)
        return value, unit
    return None, None

# Test the function
for line in [timing_line, setup_line, hold_line]:
    value, unit = extract_timing_value(line)
    if value is not None:
        print(f"  Line: {line[:40]}...")
        print(f"  Extracted: {value} {unit}")

print()

# 3. DATA STRUCTURES FOR TIMING ANALYSIS
print("2. DATA STRUCTURES:")

# Dictionaries for storing timing data
timing_data = {
    'path_name': 'clk_to_output_path',
    'slack': 0.142,
    'required_time': 2.900,
    'arrival_time': 2.858,
    'clock_period': 3.000
}

# Lists for multiple paths
critical_paths = [
    {'path': 'path1', 'slack': -0.050, 'endpoint': 'reg1/D'},
    {'path': 'path2', 'slack': -0.030, 'endpoint': 'reg2/D'},
    {'path': 'path3', 'slack': 0.020, 'endpoint': 'reg3/D'},
]

# Find failing paths (negative slack)
failing_paths = [path for path in critical_paths if path['slack'] < 0]
print(f"  Found {len(failing_paths)} failing paths:")
for path in failing_paths:
    print(f"    {path['path']}: {path['slack']}ns at {path['endpoint']}")

print()

# 4. FILE I/O PATTERNS
print("3. FILE I/O PATTERNS:")

# Reading configuration files
def read_config_file(filename):
    """Read key-value configuration - common in EDA"""
    config = {}
    try:
        with open(filename, 'r') as f:
            for line in f:
                line = line.strip()
                if line and not line.startswith('#'):
                    if '=' in line:
                        key, value = line.split('=', 1)
                        config[key.strip()] = value.strip()
    except FileNotFoundError:
        print(f"  Config file {filename} not found - would create default")
        config = {'clock_period': '1.0', 'voltage': '1.0', 'temperature': '25'}
    
    return config

# Example usage
config = read_config_file('design.cfg')  # This file doesn't exist, will use defaults
print(f"  Configuration loaded: {config}")

print()

# 5. ERROR HANDLING FOR ROBUST SCRIPTS
print("4. ERROR HANDLING:")

def safe_parse_timing(filename):
    """Safely parse timing report with error handling"""
    results = {'paths': [], 'errors': []}
    
    try:
        with open(filename, 'r') as f:
            for line_num, line in enumerate(f, 1):
                try:
                    # Process each line
                    if 'slack' in line.lower():
                        value, unit = extract_timing_value(line)
                        if value is not None:
                            results['paths'].append({
                                'line': line_num,
                                'slack': value,
                                'unit': unit
                            })
                except Exception as e:
                    results['errors'].append(f"Line {line_num}: {str(e)}")
                    
    except FileNotFoundError:
        results['errors'].append(f"File {filename} not found")
    
    return results

# Example - file doesn't exist, but script handles it gracefully
result = safe_parse_timing('nonexistent_timing.rpt')
print(f"  Parse result: {len(result['paths'])} paths, {len(result['errors'])} errors")
if result['errors']:
    print(f"  Errors: {result['errors']}")

print()

# 6. LIST COMPREHENSIONS FOR DATA FILTERING
print("5. LIST COMPREHENSIONS (Data Filtering):")

# Sample timing data
all_paths = [
    {'name': 'clk_path1', 'slack': -0.100, 'type': 'setup'},
    {'name': 'clk_path2', 'slack': 0.050, 'type': 'setup'}, 
    {'name': 'data_path1', 'slack': -0.020, 'type': 'hold'},
    {'name': 'data_path2', 'slack': 0.080, 'type': 'hold'},
]

# Filter violations by type
setup_violations = [p for p in all_paths if p['type'] == 'setup' and p['slack'] < 0]
hold_violations = [p for p in all_paths if p['type'] == 'hold' and p['slack'] < 0]

print(f"  Setup violations: {len(setup_violations)}")
print(f"  Hold violations: {len(hold_violations)}")

# Get worst violations
worst_setup = min(setup_violations, key=lambda x: x['slack']) if setup_violations else None
if worst_setup:
    print(f"  Worst setup: {worst_setup['name']} with {worst_setup['slack']}ns")

print("\n=== End of Python Basics Tutorial ===")
print("Next: Run 02_file_parsing.py to learn advanced file processing")