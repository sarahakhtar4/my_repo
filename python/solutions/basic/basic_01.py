"""
Reference Solution: Basic_01 - Timing Analysis Calculations
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