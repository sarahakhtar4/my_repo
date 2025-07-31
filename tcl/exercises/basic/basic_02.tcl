#
# Exercise: Basic_02 - Timing Constraint Parser
# Difficulty: Basic
#
# Problem:
# Parse timing constraint commands and extract constraint information.
# Process SDC-like commands and build constraint database.
#
# Function to implement: solve
#
# Parameters:
# - sdc_commands: List of constraint command strings
#
# Returns:
# - Dictionary with parsed constraints
#
# SDC Commands to handle:
# - create_clock -period <period> <clock_name>
# - set_input_delay -clock <clock> <delay> <port>
# - set_output_delay -clock <clock> <delay> <port>
#
# Example:
# Input: {
#   "create_clock -period 10.0 clk"
#   "set_input_delay -clock clk 2.0 data_in"
#   "set_output_delay -clock clk 1.5 data_out"
# }
# Output: {
#   clocks {clk 10.0}
#   input_delays {{clk data_in 2.0}}
#   output_delays {{clk data_out 1.5}}
#   total_constraints 3
# }

proc solve {sdc_commands} {
    # TODO: Implement your solution here
    # Hint: Use string manipulation and regular expressions
    # Parse each command type and extract parameters
    # Build result dictionary with constraint information
    
    return {}
}

# Test configuration for automated testing  
set test_config {
    function_name solve
    test_cases {
        {
            input {{
                "create_clock -period 10.0 clk"
                "set_input_delay -clock clk 2.0 data_in"
                "set_output_delay -clock clk 1.5 data_out"
            }}
            expected {clocks {clk 10.0} input_delays {{clk data_in 2.0}} output_delays {{clk data_out 1.5}} total_constraints 3}
            description "Basic constraint parsing"
        }
        {
            input {{
                "create_clock -period 5.0 sys_clk"
                "create_clock -period 20.0 slow_clk"
                "set_input_delay -clock sys_clk 1.0 addr_bus"
                "set_input_delay -clock sys_clk 1.2 ctrl_sig"
                "set_output_delay -clock slow_clk 3.0 status"
            }}
            expected {clocks {sys_clk 5.0 slow_clk 20.0} input_delays {{sys_clk addr_bus 1.0} {sys_clk ctrl_sig 1.2}} output_delays {{slow_clk status 3.0}} total_constraints 5}
            description "Multiple clocks and constraints"
        }
        {
            input {{
                "create_clock -period 2.5 fast_clk"
            }}
            expected {clocks {fast_clk 2.5} input_delays {} output_delays {} total_constraints 1}
            description "Clock only constraint"
        }
        {
            input {{}}
            expected {clocks {} input_delays {} output_delays {} total_constraints 0}
            description "Empty constraint list"
        }
        {
            input {{
                "create_clock -period 8.0 cpu_clk"
                "create_clock -period 4.0 mem_clk" 
                "set_input_delay -clock cpu_clk 0.8 cpu_data"
                "set_input_delay -clock mem_clk 0.5 mem_addr"
                "set_output_delay -clock cpu_clk 1.2 cpu_result"
                "set_output_delay -clock mem_clk 0.7 mem_data"
            }}
            expected {clocks {cpu_clk 8.0 mem_clk 4.0} input_delays {{cpu_clk cpu_data 0.8} {mem_clk mem_addr 0.5}} output_delays {{cpu_clk cpu_result 1.2} {mem_clk mem_data 0.7}} total_constraints 6}
            description "CPU-Memory system constraints"
        }
    }
}