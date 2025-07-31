"""
Exercise: Basic_07 - Logic Gate Delay Calculator
Difficulty: Basic

Problem:
Calculate propagation delays through logic gates based on gate type and fan-out.
Use standard cell library delay models.

Function to implement: solve(gates)

Parameters:
- gates: List of dictionaries with 'name', 'type', 'fanout' keys

Returns:
- Dictionary with gate delay analysis

Gate delays (ps):
- 'and': 20 + fanout * 2
- 'or': 18 + fanout * 2  
- 'inv': 10 + fanout * 1.5
- 'nand': 15 + fanout * 1.8
- 'nor': 16 + fanout * 1.8

Example:
Input: [
    {'name': 'gate1', 'type': 'and', 'fanout': 3},
    {'name': 'gate2', 'type': 'inv', 'fanout': 2}
]
Output: {
    'total_gates': 2,
    'delays_ps': [26.0, 13.0],
    'slowest_gate': ('gate1', 26.0),
    'fastest_gate': ('gate2', 13.0),
    'total_delay': 39.0
}
"""

def solve(gates):
    """
    Calculate propagation delays for logic gates.
    
    Args:
        gates: List of gate specifications
        
    Returns:
        Dictionary with gate delay analysis
    """
    # TODO: Implement your solution here
    # Use the delay formulas provided above
    pass

# Test configuration for automated testing
TEST_CONFIG = {
    'function_name': 'solve',
    'test_cases': [
        {
            'input': [[
                {'name': 'gate1', 'type': 'and', 'fanout': 3},
                {'name': 'gate2', 'type': 'inv', 'fanout': 2}
            ]],
            'expected': {
                'total_gates': 2,
                'delays_ps': [26.0, 13.0],
                'slowest_gate': ('gate1', 26.0),
                'fastest_gate': ('gate2', 13.0),
                'total_delay': 39.0
            },
            'description': 'Basic gate delay calculation'
        },
        {
            'input': [[
                {'name': 'inv1', 'type': 'inv', 'fanout': 1},
                {'name': 'nand1', 'type': 'nand', 'fanout': 4},
                {'name': 'or1', 'type': 'or', 'fanout': 2},
                {'name': 'nor1', 'type': 'nor', 'fanout': 3}
            ]],
            'expected': {
                'total_gates': 4,
                'delays_ps': [11.5, 22.2, 22.0, 21.4],
                'slowest_gate': ('nand1', 22.2),
                'fastest_gate': ('inv1', 11.5),
                'total_delay': 77.1
            },
            'description': 'Multiple gate types'
        },
        {
            'input': [[
                {'name': 'high_fanout', 'type': 'and', 'fanout': 10}
            ]],
            'expected': {
                'total_gates': 1,
                'delays_ps': [40.0],
                'slowest_gate': ('high_fanout', 40.0),
                'fastest_gate': ('high_fanout', 40.0),
                'total_delay': 40.0
            },
            'description': 'High fanout gate'
        },
        {
            'input': [[]],
            'expected': {
                'total_gates': 0,
                'delays_ps': [],
                'slowest_gate': None,
                'fastest_gate': None,
                'total_delay': 0.0
            },
            'description': 'No gates'
        },
        {
            'input': [[
                {'name': 'inv_chain1', 'type': 'inv', 'fanout': 1},
                {'name': 'inv_chain2', 'type': 'inv', 'fanout': 1},
                {'name': 'inv_chain3', 'type': 'inv', 'fanout': 1},
                {'name': 'inv_chain4', 'type': 'inv', 'fanout': 1}
            ]],
            'expected': {
                'total_gates': 4,
                'delays_ps': [11.5, 11.5, 11.5, 11.5],
                'slowest_gate': ('inv_chain1', 11.5),
                'fastest_gate': ('inv_chain1', 11.5),
                'total_delay': 46.0
            },
            'description': 'Inverter chain'
        }
    ]
}