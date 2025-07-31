"""
Exercise: Intermediate_04 - Wirelength Optimizer
Difficulty: Intermediate

Problem:
Optimize component placement to minimize total wirelength using iterative improvement.
Given initial placement and net connectivity, calculate improvement opportunities.

Function to implement: solve(placement, nets)

Parameters:
- placement: Dictionary mapping instance names to (x, y) coordinates
- nets: List of dictionaries with 'name' and 'instances' (list of connected instances)

Returns:
- Dictionary with wirelength analysis and optimization suggestions

Wirelength calculation: Half-perimeter wire length (HPWL)
For each net: (max_x - min_x) + (max_y - min_y)

Example:
Input: 
placement = {'A': (0, 0), 'B': (100, 0), 'C': (50, 100)}
nets = [
    {'name': 'net1', 'instances': ['A', 'B']},
    {'name': 'net2', 'instances': ['B', 'C']},
    {'name': 'net3', 'instances': ['A', 'C']}
]
Output: {
    'total_wirelength': 300,
    'net_wirelengths': {'net1': 100, 'net2': 150, 'net3': 150},
    'center_of_mass': (50.0, 33.33),
    'optimization_score': 7.5,
    'worst_net': ('net2', 150)
}
"""

def solve(placement, nets):
    """
    Analyze placement and calculate wirelength metrics.
    
    Args:
        placement: Dictionary of instance positions
        nets: List of net connectivity information
        
    Returns:
        Dictionary with wirelength analysis
    """
    # TODO: Implement your solution here
    # Hint: For each net, find bounding box and calculate HPWL
    # Calculate center of mass and optimization opportunities
    pass

# Test configuration for automated testing
TEST_CONFIG = {
    'function_name': 'solve',
    'test_cases': [
        {
            'input': [
                {'A': (0, 0), 'B': (100, 0), 'C': (50, 100)},
                [
                    {'name': 'net1', 'instances': ['A', 'B']},
                    {'name': 'net2', 'instances': ['B', 'C']},
                    {'name': 'net3', 'instances': ['A', 'C']}
                ]
            ],
            'expected': {
                'total_wirelength': 300,
                'net_wirelengths': {'net1': 100, 'net2': 150, 'net3': 150},
                'center_of_mass': (50.0, 33.333333333333336),
                'optimization_score': 100.0,
                'worst_net': ('net2', 150)
            },
            'description': 'Basic wirelength calculation'
        },
        {
            'input': [
                {'CPU': (0, 0), 'MEM': (200, 0), 'CACHE': (100, 150), 'IO': (300, 100)},
                [
                    {'name': 'clk', 'instances': ['CPU', 'MEM', 'CACHE', 'IO']},
                    {'name': 'data_bus', 'instances': ['CPU', 'MEM']},
                    {'name': 'cache_line', 'instances': ['CPU', 'CACHE']}
                ]
            ],
            'expected': {
                'total_wirelength': 650,
                'net_wirelengths': {'clk': 450, 'data_bus': 200, 'cache_line': 250},
                'center_of_mass': (150.0, 62.5),
                'optimization_score': 162.5,
                'worst_net': ('clk', 450)
            },
            'description': 'Multi-instance system'
        },
        {
            'input': [
                {'INST1': (50, 50), 'INST2': (60, 55)},
                [
                    {'name': 'short_net', 'instances': ['INST1', 'INST2']}
                ]
            ],
            'expected': {
                'total_wirelength': 15,
                'net_wirelengths': {'short_net': 15},
                'center_of_mass': (55.0, 52.5),
                'optimization_score': 55.0,
                'worst_net': ('short_net', 15)
            },
            'description': 'Close placement'
        },
        {
            'input': [
                {'SINGLE': (100, 200)},
                [
                    {'name': 'self_net', 'instances': ['SINGLE']}
                ]
            ],
            'expected': {
                'total_wirelength': 0,
                'net_wirelengths': {'self_net': 0},
                'center_of_mass': (100.0, 200.0),
                'optimization_score': 100.0,
                'worst_net': ('self_net', 0)
            },
            'description': 'Single instance net'
        },
        {
            'input': [
                {'REG0': (0, 0), 'REG1': (100, 0), 'REG2': (200, 0), 'REG3': (300, 0), 'CTRL': (150, 200)},
                [
                    {'name': 'reset', 'instances': ['REG0', 'REG1', 'REG2', 'REG3', 'CTRL']},
                    {'name': 'data0', 'instances': ['REG0', 'CTRL']},
                    {'name': 'data1', 'instances': ['REG1', 'CTRL']},
                    {'name': 'data2', 'instances': ['REG2', 'CTRL']},
                    {'name': 'data3', 'instances': ['REG3', 'CTRL']}
                ]
            ],
            'expected': {
                'total_wirelength': 1300,
                'net_wirelengths': {
                    'reset': 500,
                    'data0': 350,
                    'data1': 250,
                    'data2': 250,
                    'data3': 350
                },
                'center_of_mass': (150.0, 40.0),
                'optimization_score': 130.0,
                'worst_net': ('reset', 500)
            },
            'description': 'Register file with control'
        }
    ]
}