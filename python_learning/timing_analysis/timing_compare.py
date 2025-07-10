#!/usr/bin/env python3
"""
Timing Report Comparison Tool
============================

This script demonstrates the exact example mentioned in your interview:
taking two timing reports and outputting the difference between them
in a readable manner using Python.

This is a practical, real-world script that you might use in a physical
design role for comparing timing across different PVT corners.
"""

import re
import sys
import argparse
from pathlib import Path
from collections import defaultdict
import pandas as pd

class TimingPath:
    """Represents a single timing path from a timing report"""
    def __init__(self):
        self.startpoint = ""
        self.endpoint = ""
        self.path_group = ""
        self.slack = None
        self.arrival_time = None
        self.required_time = None
        self.path_elements = []
        self.status = ""  # "MET" or "VIOLATED"

class TimingReportParser:
    """Parse timing reports and extract timing paths"""
    
    def __init__(self):
        self.paths = []
        self.summary = {}
    
    def parse_file(self, filepath):
        """Parse a timing report file"""
        print(f"Parsing timing report: {filepath}")
        
        with open(filepath, 'r') as f:
            content = f.read()
        
        # Split into individual path sections
        path_sections = self._split_paths(content)
        
        for section in path_sections:
            path = self._parse_path_section(section)
            if path:
                self.paths.append(path)
        
        # Parse summary information
        self._parse_summary(content)
        
        print(f"  Found {len(self.paths)} timing paths")
        return self.paths
    
    def _split_paths(self, content):
        """Split content into individual path sections"""
        # Look for startpoint markers to split paths
        lines = content.split('\n')
        sections = []
        current_section = []
        
        for line in lines:
            if line.strip().startswith('Startpoint:') and current_section:
                # Start of new path, save current section
                sections.append('\n'.join(current_section))
                current_section = [line]
            else:
                current_section.append(line)
        
        # Add the last section
        if current_section:
            sections.append('\n'.join(current_section))
        
        return sections
    
    def _parse_path_section(self, section):
        """Parse a single timing path section"""
        path = TimingPath()
        
        # Extract startpoint
        startpoint_match = re.search(r'Startpoint:\s+(.+)', section)
        if startpoint_match:
            # Remove the description in parentheses for cleaner comparison
            startpoint = startpoint_match.group(1).split('(')[0].strip()
            path.startpoint = startpoint
        
        # Extract endpoint
        endpoint_match = re.search(r'Endpoint:\s+(.+)', section)
        if endpoint_match:
            endpoint = endpoint_match.group(1).split('(')[0].strip()
            path.endpoint = endpoint
        
        # Extract path group
        group_match = re.search(r'Path Group:\s+(.+)', section)
        if group_match:
            path.path_group = group_match.group(1).strip()
        
        # Extract timing values
        arrival_match = re.search(r'data arrival time\s+([-+]?\d*\.?\d+)', section)
        if arrival_match:
            path.arrival_time = float(arrival_match.group(1))
        
        required_match = re.search(r'data required time\s+([-+]?\d*\.?\d+)', section)
        if required_match:
            path.required_time = float(required_match.group(1))
        
        slack_match = re.search(r'slack \((\w+)\)\s+([-+]?\d*\.?\d+)', section)
        if slack_match:
            path.status = slack_match.group(1)
            path.slack = float(slack_match.group(2))
        
        # Only return valid paths (with required information)
        if path.startpoint and path.endpoint and path.slack is not None:
            return path
        return None
    
    def _parse_summary(self, content):
        """Parse summary information from the report"""
        # Extract operating conditions
        conditions_match = re.search(r'Operating Conditions:\s+(\w+)', content)
        if conditions_match:
            self.summary['operating_conditions'] = conditions_match.group(1)
        
        # Extract summary statistics
        violations_match = re.search(r'Setup violations:\s+(\d+)', content)
        if violations_match:
            self.summary['setup_violations'] = int(violations_match.group(1))
        
        worst_slack_match = re.search(r'Worst setup slack:\s+([-+]?\d*\.?\d+)', content)
        if worst_slack_match:
            self.summary['worst_slack'] = float(worst_slack_match.group(1))

class TimingComparator:
    """Compare timing reports and generate readable differences"""
    
    def __init__(self, report1_paths, report2_paths, corner1_name, corner2_name):
        self.report1_paths = report1_paths
        self.report2_paths = report2_paths
        self.corner1_name = corner1_name
        self.corner2_name = corner2_name
        
        # Create lookup dictionaries for fast comparison
        self.report1_dict = self._create_path_dict(report1_paths)
        self.report2_dict = self._create_path_dict(report2_paths)
    
    def _create_path_dict(self, paths):
        """Create dictionary with endpoint as key for fast lookup"""
        path_dict = {}
        for path in paths:
            key = f"{path.startpoint} -> {path.endpoint}"
            path_dict[key] = path
        return path_dict
    
    def compare_reports(self):
        """Compare the two timing reports"""
        comparison_results = {
            'improved_paths': [],
            'degraded_paths': [],
            'new_violations': [],
            'fixed_violations': [],
            'unchanged_paths': [],
            'missing_paths': []
        }
        
        # Compare common paths
        common_paths = set(self.report1_dict.keys()) & set(self.report2_dict.keys())
        
        for path_key in common_paths:
            path1 = self.report1_dict[path_key]
            path2 = self.report2_dict[path_key]
            
            slack_diff = path2.slack - path1.slack
            
            # Categorize the change
            if abs(slack_diff) < 0.001:  # Essentially unchanged (within 1ps)
                comparison_results['unchanged_paths'].append({
                    'path': path_key,
                    'slack1': path1.slack,
                    'slack2': path2.slack,
                    'difference': slack_diff
                })
            elif slack_diff > 0:  # Improved (more positive slack)
                comparison_results['improved_paths'].append({
                    'path': path_key,
                    'slack1': path1.slack,
                    'slack2': path2.slack,
                    'improvement': slack_diff
                })
            else:  # Degraded (more negative slack)
                comparison_results['degraded_paths'].append({
                    'path': path_key,
                    'slack1': path1.slack,
                    'slack2': path2.slack,
                    'degradation': abs(slack_diff)
                })
            
            # Check for new violations or fixes
            if path1.status == "MET" and path2.status == "VIOLATED":
                comparison_results['new_violations'].append({
                    'path': path_key,
                    'slack1': path1.slack,
                    'slack2': path2.slack,
                    'degradation': abs(slack_diff)
                })
            elif path1.status == "VIOLATED" and path2.status == "MET":
                comparison_results['fixed_violations'].append({
                    'path': path_key,
                    'slack1': path1.slack,
                    'slack2': path2.slack,
                    'improvement': slack_diff
                })
        
        # Find paths that exist in only one report
        only_in_report1 = set(self.report1_dict.keys()) - set(self.report2_dict.keys())
        only_in_report2 = set(self.report2_dict.keys()) - set(self.report1_dict.keys())
        
        for path_key in only_in_report1:
            comparison_results['missing_paths'].append({
                'path': path_key,
                'location': f"Only in {self.corner1_name}",
                'slack': self.report1_dict[path_key].slack
            })
        
        for path_key in only_in_report2:
            comparison_results['missing_paths'].append({
                'path': path_key,
                'location': f"Only in {self.corner2_name}",
                'slack': self.report2_dict[path_key].slack
            })
        
        return comparison_results
    
    def generate_readable_report(self, comparison_results):
        """Generate a human-readable comparison report"""
        report = []
        report.append("=" * 80)
        report.append(f"TIMING COMPARISON REPORT")
        report.append(f"{self.corner1_name} vs {self.corner2_name}")
        report.append("=" * 80)
        report.append("")
        
        # Summary statistics
        total_common = (len(comparison_results['improved_paths']) + 
                       len(comparison_results['degraded_paths']) + 
                       len(comparison_results['unchanged_paths']))
        
        report.append("SUMMARY:")
        report.append(f"  Total common paths analyzed: {total_common}")
        report.append(f"  Improved paths: {len(comparison_results['improved_paths'])}")
        report.append(f"  Degraded paths: {len(comparison_results['degraded_paths'])}")
        report.append(f"  New violations: {len(comparison_results['new_violations'])}")
        report.append(f"  Fixed violations: {len(comparison_results['fixed_violations'])}")
        report.append(f"  Paths only in one report: {len(comparison_results['missing_paths'])}")
        report.append("")
        
        # Detailed sections
        if comparison_results['new_violations']:
            report.append("🚨 NEW VIOLATIONS (Critical!):")
            report.append("-" * 40)
            for item in sorted(comparison_results['new_violations'], 
                             key=lambda x: x['slack2']):
                report.append(f"  {item['path']}")
                report.append(f"    {self.corner1_name}: {item['slack1']:+.3f}ns (MET)")
                report.append(f"    {self.corner2_name}: {item['slack2']:+.3f}ns (VIOLATED)")
                report.append(f"    Degradation: {item['degradation']:.3f}ns")
                report.append("")
        
        if comparison_results['fixed_violations']:
            report.append("✅ FIXED VIOLATIONS:")
            report.append("-" * 40)
            for item in sorted(comparison_results['fixed_violations'], 
                             key=lambda x: x['improvement'], reverse=True):
                report.append(f"  {item['path']}")
                report.append(f"    {self.corner1_name}: {item['slack1']:+.3f}ns (VIOLATED)")
                report.append(f"    {self.corner2_name}: {item['slack2']:+.3f}ns (MET)")
                report.append(f"    Improvement: {item['improvement']:.3f}ns")
                report.append("")
        
        if comparison_results['degraded_paths']:
            report.append("⚠️  MOST DEGRADED PATHS (Top 10):")
            report.append("-" * 40)
            degraded_sorted = sorted(comparison_results['degraded_paths'], 
                                   key=lambda x: x['degradation'], reverse=True)
            for item in degraded_sorted[:10]:  # Top 10 worst
                report.append(f"  {item['path']}")
                report.append(f"    {self.corner1_name}: {item['slack1']:+.3f}ns")
                report.append(f"    {self.corner2_name}: {item['slack2']:+.3f}ns")
                report.append(f"    Degradation: {item['degradation']:.3f}ns")
                report.append("")
        
        if comparison_results['improved_paths']:
            report.append("📈 MOST IMPROVED PATHS (Top 5):")
            report.append("-" * 40)
            improved_sorted = sorted(comparison_results['improved_paths'], 
                                   key=lambda x: x['improvement'], reverse=True)
            for item in improved_sorted[:5]:  # Top 5 best
                report.append(f"  {item['path']}")
                report.append(f"    {self.corner1_name}: {item['slack1']:+.3f}ns")
                report.append(f"    {self.corner2_name}: {item['slack2']:+.3f}ns")
                report.append(f"    Improvement: {item['improvement']:.3f}ns")
                report.append("")
        
        report.append("=" * 80)
        return "\n".join(report)

def main():
    """Main function demonstrating timing report comparison"""
    # For this demo, we'll use the sample reports we created
    sample_dir = Path(__file__).parent / "../sample_data"
    
    # Parse both timing reports
    parser1 = TimingReportParser()
    parser2 = TimingReportParser()
    
    report1_file = sample_dir / "timing_report_corner1.rpt"
    report2_file = sample_dir / "timing_report_corner2.rpt"
    
    if not report1_file.exists() or not report2_file.exists():
        print("Error: Sample timing reports not found!")
        print(f"Looking for:")
        print(f"  {report1_file}")
        print(f"  {report2_file}")
        return 1
    
    # Parse the reports
    paths1 = parser1.parse_file(report1_file)
    paths2 = parser2.parse_file(report2_file)
    
    # Compare the reports
    comparator = TimingComparator(paths1, paths2, "TYPICAL", "WORST")
    comparison_results = comparator.compare_reports()
    
    # Generate readable report
    readable_report = comparator.generate_readable_report(comparison_results)
    
    # Output to console
    print("\n" + readable_report)
    
    # Save to file
    output_file = "timing_comparison_report.txt"
    with open(output_file, 'w') as f:
        f.write(readable_report)
    
    print(f"\nDetailed report saved to: {output_file}")
    
    # Create a CSV for spreadsheet analysis
    csv_data = []
    for result_type, items in comparison_results.items():
        if result_type not in ['missing_paths']:
            for item in items:
                csv_data.append({
                    'path': item['path'],
                    'corner1_slack': item.get('slack1', ''),
                    'corner2_slack': item.get('slack2', ''),
                    'difference': item.get('improvement', item.get('degradation', item.get('difference', ''))),
                    'category': result_type
                })
    
    if csv_data:
        df = pd.DataFrame(csv_data)
        csv_file = "timing_comparison.csv"
        df.to_csv(csv_file, index=False)
        print(f"CSV data saved to: {csv_file}")
    
    return 0

if __name__ == "__main__":
    """
    This script demonstrates exactly what your interviewer mentioned:
    
    Usage:
        python timing_compare.py
    
    This will:
    1. Parse two sample timing reports (TYPICAL vs WORST corner)
    2. Compare all timing paths between them
    3. Generate a readable summary showing:
       - New violations
       - Fixed violations  
       - Most degraded paths
       - Most improved paths
    4. Save results to both text and CSV files
    
    This is the kind of practical script you'd write in a physical design role!
    """
    sys.exit(main())