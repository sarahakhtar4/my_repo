"""
Exercise: Intermediate_03 - Critical Path Analyzer
Difficulty: Intermediate

Problem:
Analyze timing graphs to find critical paths and calculate arrival times.
Given a directed graph of timing arcs, compute the longest path (critical path).

Function to implement: solve(timing_graph)

Parameters:
- timing_graph: Dictionary with 'nodes' and 'edges' keys
  - nodes: List of node names
  - edges: List of tuples (from_node, to_node, delay)

Returns:
- Dictionary with timing analysis results

Example:
Input: {
    'nodes': ['A', 'B', 'C', 'D'],
    'edges': [('A', 'B', 2.5), ('A', 'C', 1.8), ('B', 'D', 3.2), ('C', 'D', 2.1)]
}
Output: {
    'critical_path': ['A', 'B', 'D'],
    'critical_delay': 5.7,
    'arrival_times': {'A': 0.0, 'B': 2.5, 'C': 1.8, 'D': 5.7},
    'slack_times': {'A': 0.0, 'B': 0.0, 'C': 1.8, 'D': 0.0},
    'total_nodes': 4
}
"""

def solve(timing_graph):
    """
    Analyze timing graph and find critical path.
    
    Args:
        timing_graph: Dictionary with nodes and timing edges
        
    Returns:
        Dictionary with timing analysis results
    """
    # TODO: Implement your solution here
    # Hint: Use topological sort and longest path algorithm
    # Calculate arrival times, then work backwards for slack
    pass

# Test configuration for automated testing
TEST_CONFIG = {
    'function_name': 'solve',
    'test_cases': [
        {
            'input': [{
                'nodes': ['A', 'B', 'C', 'D'],
                'edges': [('A', 'B', 2.5), ('A', 'C', 1.8), ('B', 'D', 3.2), ('C', 'D', 2.1)]
            }],
            'expected': {
                'critical_path': ['A', 'B', 'D'],
                'critical_delay': 5.7,
                'arrival_times': {'A': 0.0, 'B': 2.5, 'C': 1.8, 'D': 5.7},
                'slack_times': {'A': 0.0, 'B': 0.0, 'C': 1.8, 'D': 0.0},
                'total_nodes': 4
            },
            'description': 'Basic critical path analysis'
        },
        {
            'input': [{
                'nodes': ['START', 'REG1', 'LOGIC', 'REG2', 'END'],
                'edges': [
                    ('START', 'REG1', 0.8),
                    ('REG1', 'LOGIC', 2.5),
                    ('LOGIC', 'REG2', 1.2),
                    ('REG2', 'END', 0.6)
                ]
            }],
            'expected': {
                'critical_path': ['START', 'REG1', 'LOGIC', 'REG2', 'END'],
                'critical_delay': 5.1,
                'arrival_times': {'START': 0.0, 'REG1': 0.8, 'LOGIC': 3.3, 'REG2': 4.5, 'END': 5.1},
                'slack_times': {'START': 0.0, 'REG1': 0.0, 'LOGIC': 0.0, 'REG2': 0.0, 'END': 0.0},
                'total_nodes': 5
            },
            'description': 'Linear pipeline path'
        },
        {
            'input': [{
                'nodes': ['IN', 'GATE1', 'GATE2', 'GATE3', 'OUT'],
                'edges': [
                    ('IN', 'GATE1', 1.0),
                    ('IN', 'GATE2', 1.5),
                    ('GATE1', 'GATE3', 2.0),
                    ('GATE2', 'GATE3', 1.8),
                    ('GATE3', 'OUT', 1.2)
                ]
            }],
            'expected': {
                'critical_path': ['IN', 'GATE2', 'GATE3', 'OUT'],
                'critical_delay': 4.5,
                'arrival_times': {'IN': 0.0, 'GATE1': 1.0, 'GATE2': 1.5, 'GATE3': 3.3, 'OUT': 4.5},
                'slack_times': {'IN': 0.0, 'GATE1': 0.3, 'GATE2': 0.0, 'GATE3': 0.0, 'OUT': 0.0},
                'total_nodes': 5
            },
            'description': 'Converging paths with different delays'
        },
        {
            'input': [{
                'nodes': ['SINGLE'],
                'edges': []
            }],
            'expected': {
                'critical_path': ['SINGLE'],
                'critical_delay': 0.0,
                'arrival_times': {'SINGLE': 0.0},
                'slack_times': {'SINGLE': 0.0},
                'total_nodes': 1
            },
            'description': 'Single node graph'
        },
        {
            'input': [{
                'nodes': ['A', 'B', 'C', 'D', 'E', 'F'],
                'edges': [
                    ('A', 'B', 1.2),
                    ('A', 'C', 2.1),
                    ('B', 'D', 1.8),
                    ('C', 'D', 0.9),
                    ('B', 'E', 2.5),
                    ('D', 'F', 1.5),
                    ('E', 'F', 1.0)
                ]
            }],
            'expected': {
                'critical_path': ['A', 'B', 'E', 'F'],
                'critical_delay': 4.7,
                'arrival_times': {'A': 0.0, 'B': 1.2, 'C': 2.1, 'D': 3.0, 'E': 3.7, 'F': 4.7},
                'slack_times': {'A': 0.0, 'B': 0.0, 'C': 0.9, 'D': 0.2, 'E': 0.0, 'F': 0.0},
                'total_nodes': 6
            },
            'description': 'Complex multi-path network'
        }
    ]
}