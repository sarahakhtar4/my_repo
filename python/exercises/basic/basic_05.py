"""
Exercise: Basic_05 - Area Utilization Calculator
Difficulty: Basic

Problem:
Calculate area utilization metrics for chip floorplanning.
Given block dimensions and chip area, compute utilization statistics.

Function to implement: solve(chip_width, chip_height, blocks)

Parameters:
- chip_width: Total chip width in microns
- chip_height: Total chip height in microns  
- blocks: List of dictionaries with 'name', 'width', 'height' keys

Returns:
- Dictionary with utilization metrics

Example:
Input: chip_width=1000, chip_height=800, blocks=[
    {'name': 'CPU', 'width': 200, 'height': 300},
    {'name': 'MEM', 'width': 150, 'height': 200}
]
Output: {
    'total_chip_area': 800000,
    'total_block_area': 90000,
    'utilization_percent': 11.25,
    'free_area': 710000,
    'largest_block': ('CPU', 60000),
    'block_count': 2
}
"""

def solve(chip_width, chip_height, blocks):
    """
    Calculate area utilization for chip floorplan.
    
    Args:
        chip_width: Chip width in microns
        chip_height: Chip height in microns
        blocks: List of block specifications
        
    Returns:
        Dictionary with area utilization metrics
    """
    # TODO: Implement your solution here
    # Hint: Area = width * height, Utilization = (used_area / total_area) * 100
    pass

# Test configuration for automated testing
TEST_CONFIG = {
    'function_name': 'solve',
    'test_cases': [
        {
            'input': [1000, 800, [
                {'name': 'CPU', 'width': 200, 'height': 300},
                {'name': 'MEM', 'width': 150, 'height': 200}
            ]],
            'expected': {
                'total_chip_area': 800000,
                'total_block_area': 90000,
                'utilization_percent': 11.25,
                'free_area': 710000,
                'largest_block': ('CPU', 60000),
                'block_count': 2
            },
            'description': 'Basic area utilization'
        },
        {
            'input': [500, 400, [
                {'name': 'CORE0', 'width': 100, 'height': 150},
                {'name': 'CORE1', 'width': 100, 'height': 150},
                {'name': 'CACHE', 'width': 200, 'height': 100}
            ]],
            'expected': {
                'total_chip_area': 200000,
                'total_block_area': 50000,
                'utilization_percent': 25.0,
                'free_area': 150000,
                'largest_block': ('CACHE', 20000),
                'block_count': 3
            },
            'description': 'Multi-core design'
        },
        {
            'input': [100, 100, [
                {'name': 'FULL_CHIP', 'width': 100, 'height': 100}
            ]],
            'expected': {
                'total_chip_area': 10000,
                'total_block_area': 10000,
                'utilization_percent': 100.0,
                'free_area': 0,
                'largest_block': ('FULL_CHIP', 10000),
                'block_count': 1
            },
            'description': 'Full utilization'
        },
        {
            'input': [1000, 1000, []],
            'expected': {
                'total_chip_area': 1000000,
                'total_block_area': 0,
                'utilization_percent': 0.0,
                'free_area': 1000000,
                'largest_block': None,
                'block_count': 0
            },
            'description': 'Empty floorplan'
        },
        {
            'input': [600, 500, [
                {'name': 'BLK_A', 'width': 50, 'height': 60},
                {'name': 'BLK_B', 'width': 80, 'height': 70},
                {'name': 'BLK_C', 'width': 30, 'height': 40},
                {'name': 'BLK_D', 'width': 90, 'height': 80}
            ]],
            'expected': {
                'total_chip_area': 300000,
                'total_block_area': 15400,
                'utilization_percent': 5.133333333333334,
                'free_area': 284600,
                'largest_block': ('BLK_D', 7200),
                'block_count': 4
            },
            'description': 'Low utilization design'
        }
    ]
}