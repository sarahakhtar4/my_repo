"""
Exercise: Intermediate_01 - Liberty File Parser
Difficulty: Intermediate

Problem:
Parse a simplified Liberty (.lib) file format and extract timing information.
Handle nested structures and calculate timing statistics.

Function to implement: solve(liberty_content)

Parameters:
- liberty_content: String containing Liberty file content

Returns:
- Dictionary with parsed timing data

Liberty format example:
library(test_lib) {
  cell(INV_X1) {
    pin(A) {
      capacitance: 0.5;
    }
    pin(Y) {
      timing() {
        cell_rise: 1.2;
        cell_fall: 0.8;
      }
    }
  }
}

Expected output structure:
{
    'library_name': 'test_lib',
    'cells': {
        'INV_X1': {
            'pins': ['A', 'Y'],
            'timing_arcs': 1,
            'rise_time': 1.2,
            'fall_time': 0.8
        }
    },
    'total_cells': 1,
    'avg_rise_time': 1.2
}
"""

def solve(liberty_content):
    """
    Parse Liberty file and extract timing information.
    
    Args:
        liberty_content: String with Liberty file content
        
    Returns:
        Dictionary with parsed timing data
    """
    # TODO: Implement your solution here
    # Hint: Use string parsing, regular expressions, or simple state machine
    # Focus on extracting library name, cell names, pin names, and timing values
    pass

# Test configuration for automated testing
TEST_CONFIG = {
    'function_name': 'solve',
    'test_cases': [
        {
            'input': ["""library(test_lib) {
  cell(INV_X1) {
    pin(A) {
      capacitance: 0.5;
    }
    pin(Y) {
      timing() {
        cell_rise: 1.2;
        cell_fall: 0.8;
      }
    }
  }
}"""],
            'expected': {
                'library_name': 'test_lib',
                'cells': {
                    'INV_X1': {
                        'pins': ['A', 'Y'],
                        'timing_arcs': 1,
                        'rise_time': 1.2,
                        'fall_time': 0.8
                    }
                },
                'total_cells': 1,
                'avg_rise_time': 1.2,
                'avg_fall_time': 0.8
            },
            'description': 'Simple inverter cell'
        },
        {
            'input': ["""library(stdcell_lib) {
  cell(AND2_X1) {
    pin(A) {
      capacitance: 0.6;
    }
    pin(B) {
      capacitance: 0.6;
    }
    pin(Y) {
      timing() {
        cell_rise: 2.1;
        cell_fall: 1.8;
      }
    }
  }
  cell(OR2_X1) {
    pin(A) {
      capacitance: 0.7;
    }
    pin(B) {
      capacitance: 0.7;
    }
    pin(Y) {
      timing() {
        cell_rise: 2.3;
        cell_fall: 2.0;
      }
    }
  }
}"""],
            'expected': {
                'library_name': 'stdcell_lib',
                'cells': {
                    'AND2_X1': {
                        'pins': ['A', 'B', 'Y'],
                        'timing_arcs': 1,
                        'rise_time': 2.1,
                        'fall_time': 1.8
                    },
                    'OR2_X1': {
                        'pins': ['A', 'B', 'Y'],
                        'timing_arcs': 1,
                        'rise_time': 2.3,
                        'fall_time': 2.0
                    }
                },
                'total_cells': 2,
                'avg_rise_time': 2.2,
                'avg_fall_time': 1.9
            },
            'description': 'Multiple cells library'
        },
        {
            'input': ["""library(empty_lib) {
}"""],
            'expected': {
                'library_name': 'empty_lib',
                'cells': {},
                'total_cells': 0,
                'avg_rise_time': 0.0,
                'avg_fall_time': 0.0
            },
            'description': 'Empty library'
        },
        {
            'input': ["""library(complex_lib) {
  cell(NAND2_X2) {
    pin(A) {
      capacitance: 0.8;
    }
    pin(B) {
      capacitance: 0.8;
    }
    pin(Y) {
      timing() {
        cell_rise: 1.5;
        cell_fall: 1.3;
      }
    }
  }
  cell(NOR2_X2) {
    pin(A) {
      capacitance: 0.9;
    }
    pin(B) {
      capacitance: 0.9;
    }
    pin(Y) {
      timing() {
        cell_rise: 1.7;
        cell_fall: 1.4;
      }
    }
  }
  cell(BUF_X4) {
    pin(A) {
      capacitance: 1.2;
    }
    pin(Y) {
      timing() {
        cell_rise: 0.9;
        cell_fall: 0.7;
      }
    }
  }
}"""],
            'expected': {
                'library_name': 'complex_lib',
                'cells': {
                    'NAND2_X2': {
                        'pins': ['A', 'B', 'Y'],
                        'timing_arcs': 1,
                        'rise_time': 1.5,
                        'fall_time': 1.3
                    },
                    'NOR2_X2': {
                        'pins': ['A', 'B', 'Y'],
                        'timing_arcs': 1,
                        'rise_time': 1.7,
                        'fall_time': 1.4
                    },
                    'BUF_X4': {
                        'pins': ['A', 'Y'],
                        'timing_arcs': 1,
                        'rise_time': 0.9,
                        'fall_time': 0.7
                    }
                },
                'total_cells': 3,
                'avg_rise_time': 1.3666666666666667,
                'avg_fall_time': 1.1333333333333333
            },
            'description': 'Complex library with multiple cell types'
        }
    ]
}