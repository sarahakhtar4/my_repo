"""
Exercise: Advanced_01 - Clock Tree Synthesis Optimizer
Difficulty: Advanced

Problem:
Design a clock tree structure to minimize skew and insertion delay.
Given clock sinks and their locations, build a balanced binary tree
and calculate timing metrics.

Function to implement: solve(clock_sinks, buffer_delay, wire_delay_per_unit)

Parameters:
- clock_sinks: List of dictionaries with 'name', 'x', 'y', 'load_pf' keys
- buffer_delay: Base buffer delay in ps
- wire_delay_per_unit: Wire delay per unit length in ps/um

Returns:
- Dictionary with clock tree analysis

The algorithm should:
1. Create a balanced binary tree of clock sinks
2. Insert buffers at internal nodes
3. Calculate total insertion delay and skew
4. Optimize buffer sizing based on load

Example:
Input: 
clock_sinks = [
    {'name': 'reg1', 'x': 100, 'y': 100, 'load_pf': 0.5},
    {'name': 'reg2', 'x': 300, 'y': 100, 'load_pf': 0.8},
    {'name': 'reg3', 'x': 100, 'y': 300, 'load_pf': 0.6},
    {'name': 'reg4', 'x': 300, 'y': 300, 'load_pf': 0.7}
]
buffer_delay = 50, wire_delay_per_unit = 0.1

Output: {
    'tree_levels': 2,
    'total_buffers': 3,
    'max_insertion_delay': 165.4,
    'min_insertion_delay': 160.2,
    'clock_skew': 5.2,
    'total_power_mw': 2.1,
    'tree_structure': {...}
}
"""

def solve(clock_sinks, buffer_delay, wire_delay_per_unit):
    """
    Design and optimize clock tree structure.
    
    Args:
        clock_sinks: List of sink specifications
        buffer_delay: Buffer delay in ps
        wire_delay_per_unit: Wire delay coefficient
        
    Returns:
        Dictionary with clock tree metrics
    """
    # TODO: Implement your solution here
    # Hint: Use recursive binary tree construction
    # Calculate Manhattan distances for wire delays
    # Consider load-dependent buffer sizing
    pass

# Test configuration for automated testing
TEST_CONFIG = {
    'function_name': 'solve',
    'test_cases': [
        {
            'input': [
                [
                    {'name': 'reg1', 'x': 100, 'y': 100, 'load_pf': 0.5},
                    {'name': 'reg2', 'x': 300, 'y': 100, 'load_pf': 0.8},
                    {'name': 'reg3', 'x': 100, 'y': 300, 'load_pf': 0.6},
                    {'name': 'reg4', 'x': 300, 'y': 300, 'load_pf': 0.7}
                ],
                50,
                0.1
            ],
            'expected': {
                'tree_levels': 2,
                'total_buffers': 3,
                'max_insertion_delay': 170.0,
                'min_insertion_delay': 170.0,
                'clock_skew': 0.0,
                'total_power_mw': 1.8,
                'sink_count': 4
            },
            'description': 'Balanced 4-sink clock tree'
        },
        {
            'input': [
                [
                    {'name': 'sink1', 'x': 0, 'y': 0, 'load_pf': 1.0},
                    {'name': 'sink2', 'x': 100, 'y': 0, 'load_pf': 1.0}
                ],
                30,
                0.05
            ],
            'expected': {
                'tree_levels': 1,
                'total_buffers': 1,
                'max_insertion_delay': 87.5,
                'min_insertion_delay': 87.5,
                'clock_skew': 0.0,
                'total_power_mw': 1.5,
                'sink_count': 2
            },
            'description': 'Simple 2-sink tree'
        },
        {
            'input': [
                [
                    {'name': 'single', 'x': 50, 'y': 50, 'load_pf': 0.3}
                ],
                40,
                0.08
            ],
            'expected': {
                'tree_levels': 0,
                'total_buffers': 0,
                'max_insertion_delay': 4.0,
                'min_insertion_delay': 4.0,
                'clock_skew': 0.0,
                'total_power_mw': 0.0,
                'sink_count': 1
            },
            'description': 'Single sink (no tree needed)'
        },
        {
            'input': [
                [
                    {'name': 'r1', 'x': 0, 'y': 0, 'load_pf': 0.4},
                    {'name': 'r2', 'x': 200, 'y': 0, 'load_pf': 0.6},
                    {'name': 'r3', 'x': 400, 'y': 0, 'load_pf': 0.5},
                    {'name': 'r4', 'x': 0, 'y': 200, 'load_pf': 0.7},
                    {'name': 'r5', 'x': 200, 'y': 200, 'load_pf': 0.8},
                    {'name': 'r6', 'x': 400, 'y': 200, 'load_pf': 0.9}
                ],
                45,
                0.12
            ],
            'expected': {
                'tree_levels': 3,
                'total_buffers': 5,
                'max_insertion_delay': 183.0,
                'min_insertion_delay': 183.0,
                'clock_skew': 0.0,
                'total_power_mw': 2.85,
                'sink_count': 6
            },
            'description': 'Complex 6-sink clock tree'
        }
    ]
}