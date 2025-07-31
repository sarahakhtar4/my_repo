"""
Exercise: Basic_02 - Power Report Parser
Difficulty: Basic

Problem:
Parse a simple power report format and extract power consumption data.
The report contains lines in the format: "Instance: <name> Power: <value>mW"

Function to implement: solve(report_lines)

Parameters:
- report_lines: List of strings representing power report lines

Returns:
- Dictionary with keys: 'total_power', 'instance_count', 'max_power_instance', 'min_power_instance'

Example:
Input: [
    "Instance: CPU Power: 250.5mW",
    "Instance: GPU Power: 180.2mW", 
    "Instance: RAM Power: 45.8mW"
]
Output: {
    'total_power': 476.5,
    'instance_count': 3,
    'max_power_instance': ('CPU', 250.5),
    'min_power_instance': ('RAM', 45.8)
}
"""

def solve(report_lines):
    """
    Parse power report and extract statistics.
    
    Args:
        report_lines: List of strings with power report data
        
    Returns:
        Dictionary with power statistics
    """
    # TODO: Implement your solution here
    # Hint: Use string methods like split() and regular expressions if needed
    pass

# Test configuration for automated testing
TEST_CONFIG = {
    'function_name': 'solve',
    'test_cases': [
        {
            'input': [[
                "Instance: CPU Power: 250.5mW",
                "Instance: GPU Power: 180.2mW", 
                "Instance: RAM Power: 45.8mW"
            ]],
            'expected': {
                'total_power': 476.5,
                'instance_count': 3,
                'max_power_instance': ('CPU', 250.5),
                'min_power_instance': ('RAM', 45.8)
            },
            'description': 'Basic power report parsing'
        },
        {
            'input': [[
                "Instance: CORE0 Power: 125.0mW",
                "Instance: CORE1 Power: 130.5mW",
                "Instance: CACHE Power: 85.2mW",
                "Instance: IO Power: 65.8mW"
            ]],
            'expected': {
                'total_power': 406.5,
                'instance_count': 4,
                'max_power_instance': ('CORE1', 130.5),
                'min_power_instance': ('IO', 65.8)
            },
            'description': 'Multi-core power analysis'
        },
        {
            'input': [[
                "Instance: SINGLE_BLOCK Power: 100.0mW"
            ]],
            'expected': {
                'total_power': 100.0,
                'instance_count': 1,
                'max_power_instance': ('SINGLE_BLOCK', 100.0),
                'min_power_instance': ('SINGLE_BLOCK', 100.0)
            },
            'description': 'Single instance case'
        },
        {
            'input': [[]],
            'expected': {
                'total_power': 0.0,
                'instance_count': 0,
                'max_power_instance': None,
                'min_power_instance': None
            },
            'description': 'Empty report'
        },
        {
            'input': [[
                "Instance: BLOCK_A Power: 50.0mW",
                "Instance: BLOCK_B Power: 75.5mW",
                "Instance: BLOCK_C Power: 62.3mW",
                "Instance: BLOCK_D Power: 88.7mW",
                "Instance: BLOCK_E Power: 42.1mW"
            ]],
            'expected': {
                'total_power': 318.6,
                'instance_count': 5,
                'max_power_instance': ('BLOCK_D', 88.7),
                'min_power_instance': ('BLOCK_E', 42.1)
            },
            'description': 'Multiple blocks analysis'
        }
    ]
}