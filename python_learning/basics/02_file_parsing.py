#!/usr/bin/env python3
"""
Advanced File Parsing for EDA Reports
=====================================

Learn to parse complex EDA reports including timing reports, power reports,
and area reports using Python.
"""

import re
import os
from pathlib import Path
from collections import defaultdict

print("=== Advanced File Parsing for EDA ===\n")

# 1. TIMING REPORT PARSING PATTERNS
print("1. TIMING REPORT PARSING PATTERNS:")

# Simulate timing report content
sample_timing_report = """
Startpoint: cpu_inst/reg1 (rising edge-triggered flip-flop clocked by clk)
Endpoint: cpu_inst/reg2 (rising edge-triggered flip-flop clocked by clk)
Path Group: clk
Path Type: max

Point                    Incr       Path
------------------------------------------
clock clk (rise edge)    0.00       0.00
clock network delay      0.10       0.10
cpu_inst/reg1/CK (DFF)   0.00       0.10 r
cpu_inst/reg1/Q (DFF)    0.15       0.25 r
cpu_inst/add1/A (ADD)    0.05       0.30 r
cpu_inst/add1/Y (ADD)    0.20       0.50 r
cpu_inst/reg2/D (DFF)    0.00       0.50 r
data arrival time                   0.50

clock clk (rise edge)    1.00       1.00
clock network delay      0.10       1.10
cpu_inst/reg2/CK (DFF)   0.00       1.10 r
library setup time      -0.05       1.05
data required time                  1.05

slack (MET)                         0.55
"""

def parse_timing_path(report_text):
    """Parse timing path from report text"""
    path_info = {}
    
    # Extract startpoint and endpoint
    startpoint_match = re.search(r'Startpoint:\s+(.+)', report_text)
    endpoint_match = re.search(r'Endpoint:\s+(.+)', report_text)
    
    if startpoint_match:
        path_info['startpoint'] = startpoint_match.group(1).strip()
    if endpoint_match:
        path_info['endpoint'] = endpoint_match.group(1).strip()
    
    # Extract timing values
    arrival_match = re.search(r'data arrival time\s+([-+]?\d*\.?\d+)', report_text)
    required_match = re.search(r'data required time\s+([-+]?\d*\.?\d+)', report_text)
    slack_match = re.search(r'slack.*?([-+]?\d*\.?\d+)', report_text)
    
    if arrival_match:
        path_info['arrival_time'] = float(arrival_match.group(1))
    if required_match:
        path_info['required_time'] = float(required_match.group(1))
    if slack_match:
        path_info['slack'] = float(slack_match.group(1))
    
    # Extract path elements
    path_elements = []
    lines = report_text.split('\n')
    in_path_section = False
    
    for line in lines:
        if 'Point' in line and 'Incr' in line and 'Path' in line:
            in_path_section = True
            continue
        elif line.startswith('data arrival time') or line.startswith('clock'):
            if 'arrival' in line:
                in_path_section = False
            continue
        
        if in_path_section and line.strip() and not line.startswith('-'):
            # Parse path line: cell_name (cell_type) delay total_time transition
            match = re.search(r'(\S+.*?)\s+([-+]?\d*\.?\d+)\s+([-+]?\d*\.?\d+)', line)
            if match:
                element = {
                    'cell': match.group(1).strip(),
                    'incr_delay': float(match.group(2)),
                    'path_delay': float(match.group(3))
                }
                path_elements.append(element)
    
    path_info['path_elements'] = path_elements
    return path_info

# Test the parser
parsed_path = parse_timing_path(sample_timing_report)
print(f"  Startpoint: {parsed_path.get('startpoint', 'Not found')}")
print(f"  Endpoint: {parsed_path.get('endpoint', 'Not found')}")
print(f"  Slack: {parsed_path.get('slack', 'Not found')}ns")
print(f"  Path elements: {len(parsed_path.get('path_elements', []))}")

print()

# 2. MULTI-FILE PROCESSING
print("2. MULTI-FILE PROCESSING:")

def process_timing_directory(directory_path):
    """Process all timing reports in a directory"""
    timing_summary = {
        'total_files': 0,
        'total_paths': 0,
        'violations': 0,
        'worst_slack': float('inf'),
        'files_processed': []
    }
    
    # In real scenario, you'd scan for .rpt files
    # For demo, we'll simulate multiple files
    simulated_files = ['setup.rpt', 'hold.rpt', 'recovery.rpt']
    
    for filename in simulated_files:
        # Simulate different slack values for each file
        if 'setup' in filename:
            slack = -0.025  # Setup violation
        elif 'hold' in filename:
            slack = 0.150   # Hold passing
        else:
            slack = 0.005   # Marginal recovery
        
        timing_summary['total_files'] += 1
        timing_summary['total_paths'] += 1  # Simplified: 1 path per file
        
        if slack < 0:
            timing_summary['violations'] += 1
        
        if slack < timing_summary['worst_slack']:
            timing_summary['worst_slack'] = slack
        
        timing_summary['files_processed'].append({
            'file': filename,
            'slack': slack,
            'status': 'VIOLATION' if slack < 0 else 'PASS'
        })
    
    return timing_summary

# Test multi-file processing
summary = process_timing_directory('.')
print(f"  Processed {summary['total_files']} files")
print(f"  Found {summary['violations']} violations")
print(f"  Worst slack: {summary['worst_slack']}ns")

print()

# 3. REGULAR EXPRESSIONS FOR EDA
print("3. ADVANCED REGEX FOR EDA:")

def extract_all_timing_info(text):
    """Extract comprehensive timing information using regex"""
    patterns = {
        'clock_period': r'clock period\s*[:\s]\s*([-+]?\d*\.?\d+)\s*(ns|ps)',
        'setup_time': r'setup time\s*[:\s]\s*([-+]?\d*\.?\d+)\s*(ns|ps)',
        'hold_time': r'hold time\s*[:\s]\s*([-+]?\d*\.?\d+)\s*(ns|ps)',
        'instance_names': r'(\w+/\w+(?:/\w+)*)\s+\([^)]+\)',
        'cell_delays': r'(\w+)\s+\([^)]+\)\s+([-+]?\d*\.?\d+)\s+([-+]?\d*\.?\d+)',
        'slack_values': r'slack.*?([-+]?\d*\.?\d+)',
    }
    
    extracted = {}
    
    for key, pattern in patterns.items():
        matches = re.findall(pattern, text, re.IGNORECASE)
        extracted[key] = matches
    
    return extracted

# Test with sample data
sample_text = """
Library setup time: 0.05 ns
Hold time requirement: 0.02 ns
cpu_inst/reg1 (DFF_X1) 0.15 0.25
memory_ctrl/addr_reg (DFF_X2) 0.12 0.37
slack (VIOLATED): -0.025 ns
"""

extracted_info = extract_all_timing_info(sample_text)
for key, values in extracted_info.items():
    if values:
        print(f"  {key}: {values}")

print()

# 4. DATA VALIDATION AND CLEANSING
print("4. DATA VALIDATION:")

def validate_timing_data(timing_dict):
    """Validate parsed timing data for consistency"""
    errors = []
    warnings = []
    
    # Check required fields
    required_fields = ['slack', 'arrival_time', 'required_time']
    for field in required_fields:
        if field not in timing_dict:
            errors.append(f"Missing required field: {field}")
    
    # Validate slack calculation if all fields present
    if all(field in timing_dict for field in required_fields):
        calculated_slack = timing_dict['required_time'] - timing_dict['arrival_time']
        reported_slack = timing_dict['slack']
        
        if abs(calculated_slack - reported_slack) > 0.001:  # 1ps tolerance
            warnings.append(f"Slack mismatch: calculated={calculated_slack:.3f}, "
                          f"reported={reported_slack:.3f}")
    
    # Check for reasonable values
    if 'slack' in timing_dict:
        slack = timing_dict['slack']
        if slack < -10:  # More than 10ns violation seems unrealistic
            warnings.append(f"Extremely large violation: {slack}ns")
        elif slack > 10:  # More than 10ns positive slack might indicate issue
            warnings.append(f"Unusually large positive slack: {slack}ns")
    
    return {'errors': errors, 'warnings': warnings}

# Test validation
test_data = {
    'slack': 0.55,
    'arrival_time': 0.50,
    'required_time': 1.05
}

validation_result = validate_timing_data(test_data)
print(f"  Validation errors: {len(validation_result['errors'])}")
print(f"  Validation warnings: {len(validation_result['warnings'])}")

print("\n=== End of Advanced File Parsing ===")
print("Next: Check out the timing_analysis/ directory for real-world examples")