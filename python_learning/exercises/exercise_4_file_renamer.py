#!/usr/bin/env python3
"""
Exercise 4: File Renamer for Reports
====================================

🎯 Goal: Rename all .rpt files by adding _backup before extension
📝 Skills: File I/O, string manipulation, path operations

Common task in EDA workflows - backing up reports before rerunning tools.
"""

import os
import glob
from pathlib import Path

def rename_reports_in_dir(path):
    """
    Rename all .rpt files in a directory by appending _backup before the extension.
    
    Example: setup_report.rpt → setup_report_backup.rpt
    
    Args:
        path (str): Directory path to process
        
    Returns:
        list: List of (old_name, new_name) tuples for renamed files
    """
    # TODO: Implement this function
    # Hint: Use glob.glob() or os.listdir() to find .rpt files
    # Hint: Use os.rename() to rename files
    # Hint: Be careful with file extensions and path handling
    pass


def rename_reports_with_timestamp(path):
    """
    Advanced version: Add both _backup and current timestamp to filename
    
    Example: setup_report.rpt → setup_report_backup_20240115_142530.rpt
    
    Returns:
        list: List of (old_name, new_name) tuples for renamed files
    """
    # TODO: Implement this function
    # Hint: Use datetime.now().strftime() for timestamp formatting
    pass


def create_test_files(test_dir):
    """Helper function to create test .rpt files"""
    import tempfile
    
    test_files = [
        'setup_report.rpt',
        'hold_report.rpt',
        'power_analysis.rpt',
        'area_report.rpt',
        'clock_tree.rpt',
        'other_file.txt'  # This should NOT be renamed
    ]
    
    # Create test directory if it doesn't exist
    os.makedirs(test_dir, exist_ok=True)
    
    # Create test files
    for filename in test_files:
        filepath = os.path.join(test_dir, filename)
        with open(filepath, 'w') as f:
            f.write(f"Test content for {filename}\n")
    
    return test_files


def test_rename_reports():
    """Test the basic file renaming function"""
    import tempfile
    import shutil
    
    # Create temporary test directory
    test_dir = tempfile.mkdtemp(prefix='test_reports_')
    
    try:
        # Create test files
        test_files = create_test_files(test_dir)
        
        print("🧪 Testing rename_reports_in_dir()...")
        print(f"Test directory: {test_dir}")
        
        # Show files before
        before_files = sorted(os.listdir(test_dir))
        print(f"Before: {before_files}")
        
        # Run the function
        result = rename_reports_in_dir(test_dir)
        
        # Show files after
        after_files = sorted(os.listdir(test_dir))
        print(f"After:  {after_files}")
        print(f"Renamed: {result}")
        
        # Expected result
        expected_renames = 5  # 5 .rpt files should be renamed
        expected_files = {
            'setup_report_backup.rpt',
            'hold_report_backup.rpt', 
            'power_analysis_backup.rpt',
            'area_report_backup.rpt',
            'clock_tree_backup.rpt',
            'other_file.txt'  # Should remain unchanged
        }
        
        if (len(result) == expected_renames and 
            set(after_files) == expected_files):
            print("✅ PASS: File renaming works correctly!")
        else:
            print("❌ FAIL: Check your file renaming logic")
            print(f"Expected {expected_renames} renames, got {len(result)}")
            print(f"Expected files: {sorted(expected_files)}")
        
    finally:
        # Clean up
        shutil.rmtree(test_dir)
    
    print()


if __name__ == "__main__":
    print("🚀 Exercise 4: Report File Renamer")
    print("=" * 50)
    print()
    
    # Run test
    test_rename_reports()
    
    print("💡 Hints:")
    print("- Use glob.glob('*.rpt') or os.listdir() + filter")
    print("- Split filename and extension with os.path.splitext()")
    print("- Use os.rename(old_path, new_path) to rename files")
    print("- Handle edge cases like files without extensions")
    print()
    print("📚 Useful functions:")
    print("- os.path.splitext('file.rpt') → ('file', '.rpt')")
    print("- glob.glob('*.rpt') → list of .rpt files")
    print("- os.path.join(dir, filename) → proper path")
    print()
    print("🎯 Extension: Try the timestamp version for extra credit!")