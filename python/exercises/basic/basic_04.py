"""
Exercise: Basic_04 - Clock Frequency Analysis
Difficulty: Basic

Problem:
Given clock specifications, perform frequency and period conversions.
Calculate derived timing parameters used in physical design.

Function to implement: solve(clock_specs)

Parameters:
- clock_specs: List of dictionaries with 'name', 'frequency_mhz' keys

Returns:
- Dictionary with clock analysis results

Example:
Input: [
    {'name': 'clk_core', 'frequency_mhz': 100},
    {'name': 'clk_mem', 'frequency_mhz': 200}
]
Output: {
    'total_clocks': 2,
    'periods_ns': [10.0, 5.0],
    'fastest_clock': ('clk_mem', 200),
    'slowest_clock': ('clk_core', 100),
    'avg_frequency': 150.0
}
"""

def solve(clock_specs):
    """
    Analyze clock specifications and calculate timing parameters.
    
    Args:
        clock_specs: List of dictionaries with clock information
        
    Returns:
        Dictionary with clock analysis results
    """
    # TODO: Implement your solution here
    # Hint: Period (ns) = 1000 / frequency (MHz)
    pass

# Test configuration for automated testing
TEST_CONFIG = {
    'function_name': 'solve',
    'test_cases': [
        {
            'input': [[
                {'name': 'clk_core', 'frequency_mhz': 100},
                {'name': 'clk_mem', 'frequency_mhz': 200}
            ]],
            'expected': {
                'total_clocks': 2,
                'periods_ns': [10.0, 5.0],
                'fastest_clock': ('clk_mem', 200),
                'slowest_clock': ('clk_core', 100),
                'avg_frequency': 150.0
            },
            'description': 'Basic clock analysis'
        },
        {
            'input': [[
                {'name': 'clk_cpu', 'frequency_mhz': 2400},
                {'name': 'clk_bus', 'frequency_mhz': 400},
                {'name': 'clk_io', 'frequency_mhz': 100}
            ]],
            'expected': {
                'total_clocks': 3,
                'periods_ns': [0.4166666666666667, 2.5, 10.0],
                'fastest_clock': ('clk_cpu', 2400),
                'slowest_clock': ('clk_io', 100),
                'avg_frequency': 966.6666666666666
            },
            'description': 'Multi-clock system'
        },
        {
            'input': [[
                {'name': 'clk_single', 'frequency_mhz': 500}
            ]],
            'expected': {
                'total_clocks': 1,
                'periods_ns': [2.0],
                'fastest_clock': ('clk_single', 500),
                'slowest_clock': ('clk_single', 500),
                'avg_frequency': 500.0
            },
            'description': 'Single clock system'
        },
        {
            'input': [[]],
            'expected': {
                'total_clocks': 0,
                'periods_ns': [],
                'fastest_clock': None,
                'slowest_clock': None,
                'avg_frequency': 0.0
            },
            'description': 'No clocks defined'
        },
        {
            'input': [[
                {'name': 'clk_high', 'frequency_mhz': 1000},
                {'name': 'clk_med', 'frequency_mhz': 250},
                {'name': 'clk_low', 'frequency_mhz': 50},
                {'name': 'clk_very_low', 'frequency_mhz': 10}
            ]],
            'expected': {
                'total_clocks': 4,
                'periods_ns': [1.0, 4.0, 20.0, 100.0],
                'fastest_clock': ('clk_high', 1000),
                'slowest_clock': ('clk_very_low', 10),
                'avg_frequency': 327.5
            },
            'description': 'Wide frequency range'
        }
    ]
}