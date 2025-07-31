#
# Exercise: Basic_01 - Instance List Processor
# Difficulty: Basic
#
# Problem:
# Process a list of instance definitions and extract statistics.
# Each instance is represented as a list: {name cell_type x y}
#
# Function to implement: solve
#
# Parameters:
# - instance_list: List of instance definitions
#
# Returns:
# - Dictionary with statistics: total_instances, cell_types, bounding_box, center
#
# Example:
# Input: {{inst1 INV_X1 100 200} {inst2 AND2_X1 300 400} {inst3 INV_X1 500 600}}
# Output: {total_instances 3 cell_types {INV_X1 AND2_X1} bounding_box {100 200 500 600} center {300.0 400.0}}

proc solve {instance_list} {
    # TODO: Implement your solution here
    # Hint: Use foreach to iterate through instances
    # Extract cell types, calculate bounding box and center of mass
    # Return results as a dictionary
    
    return {}
}

# Test configuration for automated testing
set test_config {
    function_name solve
    test_cases {
        {
            input {{{inst1 INV_X1 100 200} {inst2 AND2_X1 300 400} {inst3 INV_X1 500 600}}}
            expected {total_instances 3 cell_types {INV_X1 AND2_X1} bounding_box {100 200 500 600} center {300.0 400.0}}
            description "Basic instance processing"
        }
        {
            input {{{cpu_reg DFF_X1 0 0} {cpu_mux MUX2_X1 50 100} {cpu_buf BUF_X2 100 50}}}
            expected {total_instances 3 cell_types {DFF_X1 MUX2_X1 BUF_X2} bounding_box {0 0 100 100} center {50.0 50.0}}
            description "CPU components"
        }
        {
            input {{{single_inst NAND2_X1 250 350}}}
            expected {total_instances 1 cell_types {NAND2_X1} bounding_box {250 350 250 350} center {250.0 350.0}}
            description "Single instance"
        }
        {
            input {{}}
            expected {total_instances 0 cell_types {} bounding_box {} center {0.0 0.0}}
            description "Empty instance list"
        }
        {
            input {{{mem0 SRAM_X1 0 0} {mem1 SRAM_X1 200 0} {mem2 SRAM_X1 400 0} {ctrl CTRL_X1 200 300}}}
            expected {total_instances 4 cell_types {SRAM_X1 CTRL_X1} bounding_box {0 0 400 300} center {200.0 75.0}}
            description "Memory array with controller"
        }
    }
}