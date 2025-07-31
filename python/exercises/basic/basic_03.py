"""
Exercise: Basic_03 - Manhattan Distance Calculator
Difficulty: Basic

Problem:
Calculate Manhattan distances between placement coordinates.
Given a list of component coordinates, find the total Manhattan distance
for connecting all components in sequence.

Function to implement: solve(coordinates)

Parameters:
- coordinates: List of tuples (x, y) representing component positions

Returns:
- Dictionary with keys: 'total_distance', 'max_distance', 'component_count'

Manhattan Distance = |x1 - x2| + |y1 - y2|

Example:
Input: [(0, 0), (3, 4), (6, 1), (2, 5)]
Output: {
    'total_distance': 18,  # 7 + 6 + 5 = 18
    'max_distance': 7,     # Max single segment distance
    'component_count': 4
}
"""

def solve(coordinates):
    """
    Calculate Manhattan distances for component placement.
    
    Args:
        coordinates: List of (x, y) tuples
        
    Returns:
        Dictionary with distance statistics
    """
    # TODO: Implement your solution here
    # Hint: Iterate through consecutive pairs and calculate Manhattan distance
    pass

# Test configuration for automated testing
TEST_CONFIG = {
    'function_name': 'solve',
    'test_cases': [
        {
            'input': [[(0, 0), (3, 4), (6, 1), (2, 5)]],
            'expected': {
                'total_distance': 18,
                'max_distance': 7,
                'component_count': 4
            },
            'description': 'Basic Manhattan distance calculation'
        },
        {
            'input': [[(0, 0), (1, 1), (2, 2)]],
            'expected': {
                'total_distance': 4,
                'max_distance': 2,
                'component_count': 3
            },
            'description': 'Diagonal movement'
        },
        {
            'input': [[(5, 5), (5, 10), (10, 10), (10, 5)]],
            'expected': {
                'total_distance': 15,
                'max_distance': 5,
                'component_count': 4
            },
            'description': 'Rectangle path'
        },
        {
            'input': [[(0, 0), (10, 0)]],
            'expected': {
                'total_distance': 10,
                'max_distance': 10,
                'component_count': 2
            },
            'description': 'Horizontal line'
        },
        {
            'input': [[(1, 1)]],
            'expected': {
                'total_distance': 0,
                'max_distance': 0,
                'component_count': 1
            },
            'description': 'Single component'
        },
        {
            'input': [[]],
            'expected': {
                'total_distance': 0,
                'max_distance': 0,
                'component_count': 0
            },
            'description': 'Empty coordinates'
        }
    ]
}