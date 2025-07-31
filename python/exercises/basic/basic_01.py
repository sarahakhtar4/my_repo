"""
Exercise: Basic_01 - Timing Analysis Calculations
Difficulty: Basic

Problem:
You are given a list of timing paths with their delays (in nanoseconds).
Calculate the total delay, maximum delay, minimum delay, and critical path count
(paths with delay >= 90% of max delay).

Function to implement: solve(timing_paths)

Parameters:
- timing_paths: List of tuples (path_name, delay) where delay is in nanoseconds

Returns:
- Dictionary with keys: 'total_delay', 'max_delay', 'min_delay', 'critical_paths'

Example:
Input: [("path1", 2.5), ("path2", 3.2), ("path3", 2.8), ("path4", 3.1)]
Output: {
    'total_delay': 11.6,
    'max_delay': 3.2,
    'min_delay': 2.5,
    'critical_paths': 2
}
"""

def solve(timing_paths):
    """
    Calculate timing analysis statistics for given paths.
    
    Args:
        timing_paths: List of tuples (path_name, delay)
        
    Returns:
        Dictionary with timing statistics
    """
    if not timing_paths:
        return {
            'total_delay': 0.0,
            'max_delay': 0.0,
            'min_delay': 0.0,
            'critical_paths': 0
        }
    
    # Extract delays from the path tuples
    delays = [delay for _, delay in timing_paths]
    
    # Calculate basic statistics
    total_delay = sum(delays)
    max_delay = max(delays)
    min_delay = min(delays)
    
    # Critical paths are those with delay >= 90% of max delay
    critical_threshold = 0.9 * max_delay
    critical_paths = sum(1 for delay in delays if delay >= critical_threshold)
    
    return {
        'total_delay': total_delay,
        'max_delay': max_delay,
        'min_delay': min_delay,
        'critical_paths': critical_paths
    }

# Test configuration for automated testing
TEST_CONFIG = {
    'function_name': 'solve',
    'test_cases': [
        {
            'input': [[("path1", 2.5), ("path2", 3.2), ("path3", 2.8), ("path4", 3.1)]],
            'expected': {
                'total_delay': 11.6,
                'max_delay': 3.2,
                'min_delay': 2.5,
                'critical_paths': 2
            },
            'description': 'Basic timing analysis'
        },
        {
            'input': [[("clk_path", 1.5), ("data_path", 2.0), ("setup_path", 0.8)]],
            'expected': {
                'total_delay': 4.3,
                'max_delay': 2.0,
                'min_delay': 0.8,
                'critical_paths': 1
            },
            'description': 'Small path set'
        },
        {
            'input': [[("path_a", 5.0), ("path_b", 4.5), ("path_c", 4.6), ("path_d", 4.8), ("path_e", 4.9)]],
            'expected': {
                'total_delay': 23.8,
                'max_delay': 5.0,
                'min_delay': 4.5,
                'critical_paths': 3
            },
            'description': 'Multiple critical paths'
        },
        {
            'input': [[("single_path", 1.0)]],
            'expected': {
                'total_delay': 1.0,
                'max_delay': 1.0,
                'min_delay': 1.0,
                'critical_paths': 1
            },
            'description': 'Single path edge case'
        },
        {
            'input': [[]],
            'expected': {
                'total_delay': 0.0,
                'max_delay': 0.0,
                'min_delay': 0.0,
                'critical_paths': 0
            },
            'description': 'Empty paths list'
        }
    ]
}