"""
Exercise: Basic_06 - Net Delay Calculator  
Difficulty: Basic

Problem:
Calculate net delays based on wire length and load capacitance.
Use simplified RC delay model for interconnect analysis.

Function to implement: solve(nets)

Parameters:
- nets: List of dictionaries with 'name', 'length_um', 'capacitance_pf' keys

Returns:
- Dictionary with delay analysis results

RC Delay (ps) = length_um * 0.1 + capacitance_pf * 50

Example:
Input: [
    {'name': 'clk_net', 'length_um': 100, 'capacitance_pf': 2.0},
    {'name': 'data_net', 'length_um': 50, 'capacitance_pf': 1.5}
]
Output: {
    'total_nets': 2,
    'delays_ps': [110.0, 80.0],
    'max_delay_net': ('clk_net', 110.0),
    'min_delay_net': ('data_net', 80.0),
    'avg_delay': 95.0
}
"""

def solve(nets):
    """
    Calculate RC delays for interconnect nets.
    
    Args:
        nets: List of net specifications with length and capacitance
        
    Returns:
        Dictionary with delay analysis results
    """
    # TODO: Implement your solution here
    # Hint: RC Delay = length * 0.1 + capacitance * 50
    pass

# Test configuration for automated testing
TEST_CONFIG = {
    'function_name': 'solve',
    'test_cases': [
        {
            'input': [[
                {'name': 'clk_net', 'length_um': 100, 'capacitance_pf': 2.0},
                {'name': 'data_net', 'length_um': 50, 'capacitance_pf': 1.5}
            ]],
            'expected': {
                'total_nets': 2,
                'delays_ps': [110.0, 80.0],
                'max_delay_net': ('clk_net', 110.0),
                'min_delay_net': ('data_net', 80.0),
                'avg_delay': 95.0
            },
            'description': 'Basic RC delay calculation'
        },
        {
            'input': [[
                {'name': 'short_net', 'length_um': 10, 'capacitance_pf': 0.5},
                {'name': 'long_net', 'length_um': 1000, 'capacitance_pf': 5.0},
                {'name': 'med_net', 'length_um': 200, 'capacitance_pf': 2.5}
            ]],
            'expected': {
                'total_nets': 3,
                'delays_ps': [26.0, 350.0, 145.0],
                'max_delay_net': ('long_net', 350.0),
                'min_delay_net': ('short_net', 26.0),
                'avg_delay': 173.66666666666666
            },
            'description': 'Mixed net lengths'
        },
        {
            'input': [[
                {'name': 'zero_length', 'length_um': 0, 'capacitance_pf': 1.0}
            ]],
            'expected': {
                'total_nets': 1,
                'delays_ps': [50.0],
                'max_delay_net': ('zero_length', 50.0),
                'min_delay_net': ('zero_length', 50.0),
                'avg_delay': 50.0
            },
            'description': 'Zero length net'
        },
        {
            'input': [[]],
            'expected': {
                'total_nets': 0,
                'delays_ps': [],
                'max_delay_net': None,
                'min_delay_net': None,
                'avg_delay': 0.0
            },
            'description': 'No nets'
        },
        {
            'input': [[
                {'name': 'net1', 'length_um': 25, 'capacitance_pf': 0.8},
                {'name': 'net2', 'length_um': 30, 'capacitance_pf': 0.6},
                {'name': 'net3', 'length_um': 40, 'capacitance_pf': 1.2},
                {'name': 'net4', 'length_um': 35, 'capacitance_pf': 0.9}
            ]],
            'expected': {
                'total_nets': 4,
                'delays_ps': [42.5, 33.0, 64.0, 48.5],
                'max_delay_net': ('net3', 64.0),
                'min_delay_net': ('net2', 33.0),
                'avg_delay': 47.0
            },
            'description': 'Multiple similar nets'
        }
    ]
}