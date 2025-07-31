"""
Exercise: Basic_08 - Pin Connectivity Analyzer
Difficulty: Basic

Problem:
Analyze pin connectivity for a netlist and identify connection statistics.
Count pins, nets, and connectivity patterns.

Function to implement: solve(netlist)

Parameters:
- netlist: Dictionary with 'nets' key containing list of net dictionaries
  Each net has 'name' and 'pins' (list of pin names)

Returns:
- Dictionary with connectivity analysis

Example:
Input: {
    'nets': [
        {'name': 'clk', 'pins': ['cpu.clk', 'mem.clk', 'cache.clk']},
        {'name': 'data', 'pins': ['cpu.out', 'mem.in']},
        {'name': 'addr', 'pins': ['cpu.addr', 'mem.addr']}
    ]
}
Output: {
    'total_nets': 3,
    'total_pins': 7,
    'unique_instances': 3,
    'max_fanout_net': ('clk', 3),
    'avg_fanout': 2.33
}
"""

def solve(netlist):
    """
    Analyze pin connectivity in a netlist.
    
    Args:
        netlist: Dictionary containing nets and pin connections
        
    Returns:
        Dictionary with connectivity statistics
    """
    # TODO: Implement your solution here
    # Hint: Extract instance names from pins (part before the dot)
    pass

# Test configuration for automated testing
TEST_CONFIG = {
    'function_name': 'solve',
    'test_cases': [
        {
            'input': [{
                'nets': [
                    {'name': 'clk', 'pins': ['cpu.clk', 'mem.clk', 'cache.clk']},
                    {'name': 'data', 'pins': ['cpu.out', 'mem.in']},
                    {'name': 'addr', 'pins': ['cpu.addr', 'mem.addr']}
                ]
            }],
            'expected': {
                'total_nets': 3,
                'total_pins': 7,
                'unique_instances': 3,
                'max_fanout_net': ('clk', 3),
                'avg_fanout': 2.3333333333333335
            },
            'description': 'Basic netlist analysis'
        },
        {
            'input': [{
                'nets': [
                    {'name': 'reset', 'pins': ['core0.rst', 'core1.rst', 'core2.rst', 'core3.rst', 'ctrl.rst']},
                    {'name': 'enable', 'pins': ['ctrl.en', 'core0.en']},
                    {'name': 'done', 'pins': ['core3.done', 'ctrl.done_in']}
                ]
            }],
            'expected': {
                'total_nets': 3,
                'total_pins': 10,
                'unique_instances': 5,
                'max_fanout_net': ('reset', 5),
                'avg_fanout': 3.3333333333333335
            },
            'description': 'Multi-core reset network'
        },
        {
            'input': [{
                'nets': [
                    {'name': 'single_net', 'pins': ['inst1.out', 'inst2.in']}
                ]
            }],
            'expected': {
                'total_nets': 1,
                'total_pins': 2,
                'unique_instances': 2,
                'max_fanout_net': ('single_net', 2),
                'avg_fanout': 2.0
            },
            'description': 'Single net connection'
        },
        {
            'input': [{
                'nets': []
            }],
            'expected': {
                'total_nets': 0,
                'total_pins': 0,
                'unique_instances': 0,
                'max_fanout_net': None,
                'avg_fanout': 0.0
            },
            'description': 'Empty netlist'
        },
        {
            'input': [{
                'nets': [
                    {'name': 'bus0', 'pins': ['cpu.d0', 'mem.d0', 'io.d0']},
                    {'name': 'bus1', 'pins': ['cpu.d1', 'mem.d1', 'io.d1']},
                    {'name': 'bus2', 'pins': ['cpu.d2', 'mem.d2', 'io.d2']},
                    {'name': 'bus3', 'pins': ['cpu.d3', 'mem.d3', 'io.d3']},
                    {'name': 'ctrl_sig', 'pins': ['cpu.ctrl', 'bridge.ctrl_in']}
                ]
            }],
            'expected': {
                'total_nets': 5,
                'total_pins': 14,
                'unique_instances': 4,
                'max_fanout_net': ('bus0', 3),
                'avg_fanout': 2.8
            },
            'description': 'Bus connections'
        }
    ]
}