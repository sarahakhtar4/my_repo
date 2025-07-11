#!/usr/bin/env python3
"""
Exercise 9: Sort Cells by Area and Other Attributes
===================================================

🎯 Goal: Sort and analyze cell data by various criteria
📝 Skills: Sorting, data analysis, custom sort keys

Common task in physical design - analyzing cell usage and characteristics.
"""

def sort_cells_by_area(cells):
    """
    Given a dict of cell names and their area, sort them in descending order.
    
    Args:
        cells (dict): {cell_name: area_value}
        
    Returns:
        list: List of tuples (cell_name, area) sorted by area (largest first)
        
    Example:
        {'INVX1': 1.2, 'NAND2X2': 3.5, 'MUX2X1': 2.8} 
        → [('NAND2X2', 3.5), ('MUX2X1', 2.8), ('INVX1', 1.2)]
    """
    # TODO: Implement this function
    # Hint: Use sorted() with key parameter
    # Hint: Set reverse=True for descending order
    pass


def analyze_cell_library(cell_data):
    """
    Advanced analysis of cell library data
    
    Args:
        cell_data (dict): {
            cell_name: {
                'area': float,
                'power': float,
                'drive_strength': str (e.g., 'X1', 'X2', 'X4'),
                'cell_type': str (e.g., 'inv', 'nand2', 'dff')
            }
        }
        
    Returns:
        dict: {
            'by_area': [(cell, area), ...],          # Sorted by area
            'by_power': [(cell, power), ...],        # Sorted by power  
            'by_type': {type: [cells]},              # Grouped by type
            'by_drive': {drive: [cells]},            # Grouped by drive strength
            'summary': {
                'total_cells': int,
                'avg_area': float,
                'avg_power': float,
                'largest_cell': (name, area),
                'most_power_hungry': (name, power)
            }
        }
    """
    # TODO: Implement this function
    pass


def find_optimal_cells(cell_data, optimization='area'):
    """
    Find optimal cells for different optimization criteria
    
    Args:
        cell_data: Same format as analyze_cell_library
        optimization: 'area', 'power', 'area_power_product'
        
    Returns:
        dict: {cell_type: best_cell_name} for each cell type
    """
    # TODO: Implement this function
    # For each cell type, find the cell that's best for the optimization criteria
    pass


def generate_cell_utilization_report(cell_usage, cell_data):
    """
    Generate a report showing which cells are used most in a design
    
    Args:
        cell_usage (dict): {cell_name: instance_count}
        cell_data: Cell library data
        
    Returns:
        str: Formatted report
    """
    # TODO: Implement this function
    pass


# Test data
TEST_CELLS_SIMPLE = {
    'INVX1': 1.2,
    'NAND2X2': 3.5,
    'MUX2X1': 2.8,
    'BUFX4': 4.1,
    'DFFQX1': 8.7,
    'AOI21X1': 2.1
}

TEST_CELL_LIBRARY = {
    'INVX1': {
        'area': 1.2,
        'power': 0.05,
        'drive_strength': 'X1',
        'cell_type': 'inv'
    },
    'INVX2': {
        'area': 1.8,
        'power': 0.08,
        'drive_strength': 'X2', 
        'cell_type': 'inv'
    },
    'INVX4': {
        'area': 3.2,
        'power': 0.15,
        'drive_strength': 'X4',
        'cell_type': 'inv'
    },
    'NAND2X1': {
        'area': 2.1,
        'power': 0.06,
        'drive_strength': 'X1',
        'cell_type': 'nand2'
    },
    'NAND2X2': {
        'area': 3.5,
        'power': 0.12,
        'drive_strength': 'X2',
        'cell_type': 'nand2'
    },
    'DFFQX1': {
        'area': 8.7,
        'power': 0.25,
        'drive_strength': 'X1',
        'cell_type': 'dff'
    },
    'DFFQX2': {
        'area': 12.3,
        'power': 0.35,
        'drive_strength': 'X2',
        'cell_type': 'dff'
    },
    'BUFX2': {
        'area': 2.4,
        'power': 0.07,
        'drive_strength': 'X2',
        'cell_type': 'buf'
    }
}

TEST_CELL_USAGE = {
    'INVX1': 1250,
    'INVX2': 890,
    'NAND2X1': 445,
    'NAND2X2': 120,
    'DFFQX1': 2340,
    'BUFX2': 234
}

def test_sort_cells_by_area():
    """Test basic cell sorting"""
    result = sort_cells_by_area(TEST_CELLS_SIMPLE)
    
    expected = [
        ('DFFQX1', 8.7),
        ('BUFX4', 4.1), 
        ('NAND2X2', 3.5),
        ('MUX2X1', 2.8),
        ('AOI21X1', 2.1),
        ('INVX1', 1.2)
    ]
    
    print("🧪 Testing sort_cells_by_area()...")
    print(f"Input cells: {TEST_CELLS_SIMPLE}")
    print(f"Expected: {expected}")
    print(f"Got:      {result}")
    
    if result == expected:
        print("✅ PASS: Cell sorting works!")
    else:
        print("❌ FAIL: Check your sorting logic")
    print()

def test_analyze_cell_library():
    """Test library analysis"""
    result = analyze_cell_library(TEST_CELL_LIBRARY)
    
    print("🧪 Testing analyze_cell_library()...")
    
    if result:
        # Check some key results
        by_area = result.get('by_area', [])
        by_type = result.get('by_type', {})
        summary = result.get('summary', {})
        
        print(f"Cells by area (top 3): {by_area[:3] if by_area else 'None'}")
        print(f"Cell types: {list(by_type.keys()) if by_type else 'None'}")
        print(f"Summary: {summary}")
        
        # Basic validation
        if (by_area and by_type and summary and 
            summary.get('total_cells') == len(TEST_CELL_LIBRARY)):
            print("✅ PASS: Library analysis works!")
        else:
            print("❌ FAIL: Check your analysis logic")
    else:
        print("❌ FAIL: Function not implemented")
    print()

def test_find_optimal_cells():
    """Test optimal cell selection"""
    result_area = find_optimal_cells(TEST_CELL_LIBRARY, 'area')
    result_power = find_optimal_cells(TEST_CELL_LIBRARY, 'power')
    
    print("🧪 Testing find_optimal_cells()...")
    print(f"Optimal by area: {result_area}")
    print(f"Optimal by power: {result_power}")
    
    # Basic validation - should find smallest area/power for each type
    if result_area and result_power:
        # For inverters, INVX1 should be optimal for both area and power
        if (result_area.get('inv') == 'INVX1' and 
            result_power.get('inv') == 'INVX1'):
            print("✅ PASS: Optimal cell finding works!")
        else:
            print("❌ FAIL: Check optimization logic")
    else:
        print("❌ FAIL: Function not implemented")
    print()

def test_utilization_report():
    """Test utilization report generation"""
    result = generate_cell_utilization_report(TEST_CELL_USAGE, TEST_CELL_LIBRARY)
    
    print("🧪 Testing generate_cell_utilization_report()...")
    
    if result:
        print("Generated report preview:")
        print(result[:400] + "..." if len(result) > 400 else result)
        print("✅ PASS: Report generation works!")
    else:
        print("❌ FAIL: Function not implemented")
    print()

if __name__ == "__main__":
    print("🚀 Exercise 9: Cell Sorting and Analysis")
    print("=" * 55)
    print()
    
    # Show test data
    print("📊 Sample cell data:")
    for cell, area in sorted(TEST_CELLS_SIMPLE.items()):
        print(f"  {cell:10} {area:5.1f}")
    print()
    
    # Run tests
    test_sort_cells_by_area()
    test_analyze_cell_library()
    test_find_optimal_cells()
    test_utilization_report()
    
    print("💡 Hints:")
    print("- Use sorted(dict.items(), key=lambda x: x[1], reverse=True)")
    print("- For grouping: use defaultdict(list) or loop through data")
    print("- For min/max: use min()/max() with key parameter")
    print("- Calculate averages: sum(values) / len(values)")
    print("- Format reports with proper alignment and headers")
    print()
    print("📚 Sorting examples:")
    print("- By value: sorted(dict.items(), key=lambda x: x[1])")
    print("- By nested value: sorted(dict.items(), key=lambda x: x[1]['area'])")
    print("- Multiple criteria: key=lambda x: (x[1]['area'], x[1]['power'])")
    print()
    print("🎯 Real-world applications:")
    print("- Cell selection for area optimization")
    print("- Power analysis and optimization")
    print("- Library characterization and comparison")
    print("- Design utilization analysis")