"""
Exercise: Intermediate_02 - DEF Placement Analyzer
Difficulty: Intermediate

Problem:
Parse a simplified DEF (Design Exchange Format) file and analyze component placement.
Calculate placement density, bounding box, and clustering metrics.

Function to implement: solve(def_content)

Parameters:
- def_content: String containing DEF file content

Returns:
- Dictionary with placement analysis results

DEF format example:
DESIGN test_design ;
COMPONENTS 3 ;
- inst1 INV_X1 + PLACED ( 100 200 ) N ;
- inst2 AND2_X1 + PLACED ( 300 400 ) N ;
- inst3 BUF_X2 + PLACED ( 500 600 ) N ;
END COMPONENTS

Expected output:
{
    'design_name': 'test_design',
    'total_instances': 3,
    'bounding_box': {'min_x': 100, 'max_x': 500, 'min_y': 200, 'max_y': 600},
    'placement_area': 160000,
    'center_of_mass': (300.0, 400.0),
    'instances': [
        {'name': 'inst1', 'cell': 'INV_X1', 'x': 100, 'y': 200},
        {'name': 'inst2', 'cell': 'AND2_X1', 'x': 300, 'y': 400},
        {'name': 'inst3', 'cell': 'BUF_X2', 'x': 500, 'y': 600}
    ]
}
"""

def solve(def_content):
    """
    Parse DEF file and analyze component placement.
    
    Args:
        def_content: String with DEF file content
        
    Returns:
        Dictionary with placement analysis
    """
    # TODO: Implement your solution here
    # Hint: Parse line by line, extract instance names, cell types, and coordinates
    # Calculate bounding box and center of mass
    pass

# Test configuration for automated testing
TEST_CONFIG = {
    'function_name': 'solve',
    'test_cases': [
        {
            'input': ["""DESIGN test_design ;
COMPONENTS 3 ;
- inst1 INV_X1 + PLACED ( 100 200 ) N ;
- inst2 AND2_X1 + PLACED ( 300 400 ) N ;
- inst3 BUF_X2 + PLACED ( 500 600 ) N ;
END COMPONENTS"""],
            'expected': {
                'design_name': 'test_design',
                'total_instances': 3,
                'bounding_box': {'min_x': 100, 'max_x': 500, 'min_y': 200, 'max_y': 600},
                'placement_area': 160000,
                'center_of_mass': (300.0, 400.0),
                'instances': [
                    {'name': 'inst1', 'cell': 'INV_X1', 'x': 100, 'y': 200},
                    {'name': 'inst2', 'cell': 'AND2_X1', 'x': 300, 'y': 400},
                    {'name': 'inst3', 'cell': 'BUF_X2', 'x': 500, 'y': 600}
                ]
            },
            'description': 'Basic DEF placement parsing'
        },
        {
            'input': ["""DESIGN cpu_core ;
COMPONENTS 5 ;
- cpu_reg0 DFF_X1 + PLACED ( 0 0 ) N ;
- cpu_reg1 DFF_X1 + PLACED ( 100 0 ) N ;
- cpu_alu ADD_X2 + PLACED ( 50 100 ) N ;
- cpu_mux MUX2_X1 + PLACED ( 25 150 ) N ;
- cpu_buf BUF_X4 + PLACED ( 75 150 ) N ;
END COMPONENTS"""],
            'expected': {
                'design_name': 'cpu_core',
                'total_instances': 5,
                'bounding_box': {'min_x': 0, 'max_x': 100, 'min_y': 0, 'max_y': 150},
                'placement_area': 15000,
                'center_of_mass': (50.0, 80.0),
                'instances': [
                    {'name': 'cpu_reg0', 'cell': 'DFF_X1', 'x': 0, 'y': 0},
                    {'name': 'cpu_reg1', 'cell': 'DFF_X1', 'x': 100, 'y': 0},
                    {'name': 'cpu_alu', 'cell': 'ADD_X2', 'x': 50, 'y': 100},
                    {'name': 'cpu_mux', 'cell': 'MUX2_X1', 'x': 25, 'y': 150},
                    {'name': 'cpu_buf', 'cell': 'BUF_X4', 'x': 75, 'y': 150}
                ]
            },
            'description': 'CPU core placement'
        },
        {
            'input': ["""DESIGN single_inst ;
COMPONENTS 1 ;
- only_inst INV_X1 + PLACED ( 250 350 ) N ;
END COMPONENTS"""],
            'expected': {
                'design_name': 'single_inst',
                'total_instances': 1,
                'bounding_box': {'min_x': 250, 'max_x': 250, 'min_y': 350, 'max_y': 350},
                'placement_area': 0,
                'center_of_mass': (250.0, 350.0),
                'instances': [
                    {'name': 'only_inst', 'cell': 'INV_X1', 'x': 250, 'y': 350}
                ]
            },
            'description': 'Single instance design'
        },
        {
            'input': ["""DESIGN empty_design ;
COMPONENTS 0 ;
END COMPONENTS"""],
            'expected': {
                'design_name': 'empty_design',
                'total_instances': 0,
                'bounding_box': {'min_x': 0, 'max_x': 0, 'min_y': 0, 'max_y': 0},
                'placement_area': 0,
                'center_of_mass': (0.0, 0.0),
                'instances': []
            },
            'description': 'Empty design'
        },
        {
            'input': ["""DESIGN memory_block ;
COMPONENTS 8 ;
- mem_row0_col0 SRAM_X1 + PLACED ( 0 0 ) N ;
- mem_row0_col1 SRAM_X1 + PLACED ( 200 0 ) N ;
- mem_row0_col2 SRAM_X1 + PLACED ( 400 0 ) N ;
- mem_row0_col3 SRAM_X1 + PLACED ( 600 0 ) N ;
- mem_row1_col0 SRAM_X1 + PLACED ( 0 300 ) N ;
- mem_row1_col1 SRAM_X1 + PLACED ( 200 300 ) N ;
- mem_row1_col2 SRAM_X1 + PLACED ( 400 300 ) N ;
- mem_row1_col3 SRAM_X1 + PLACED ( 600 300 ) N ;
END COMPONENTS"""],
            'expected': {
                'design_name': 'memory_block',
                'total_instances': 8,
                'bounding_box': {'min_x': 0, 'max_x': 600, 'min_y': 0, 'max_y': 300},
                'placement_area': 180000,
                'center_of_mass': (300.0, 150.0),
                'instances': [
                    {'name': 'mem_row0_col0', 'cell': 'SRAM_X1', 'x': 0, 'y': 0},
                    {'name': 'mem_row0_col1', 'cell': 'SRAM_X1', 'x': 200, 'y': 0},
                    {'name': 'mem_row0_col2', 'cell': 'SRAM_X1', 'x': 400, 'y': 0},
                    {'name': 'mem_row0_col3', 'cell': 'SRAM_X1', 'x': 600, 'y': 0},
                    {'name': 'mem_row1_col0', 'cell': 'SRAM_X1', 'x': 0, 'y': 300},
                    {'name': 'mem_row1_col1', 'cell': 'SRAM_X1', 'x': 200, 'y': 300},
                    {'name': 'mem_row1_col2', 'cell': 'SRAM_X1', 'x': 400, 'y': 300},
                    {'name': 'mem_row1_col3', 'cell': 'SRAM_X1', 'x': 600, 'y': 300}
                ]
            },
            'description': 'Memory array placement'
        }
    ]
}