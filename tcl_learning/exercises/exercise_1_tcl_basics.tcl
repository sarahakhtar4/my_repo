#!/usr/bin/env tclsh
# Exercise 1: TCL Basics for EDA
# ==============================
#
# Complete the procedures below to practice fundamental TCL concepts.
# Run this script to test your solutions.

puts "=== Exercise 1: TCL Basics for EDA ==="
puts ""

# TODO: Complete these procedures (remove the 'return' statements and implement)

proc calculate_power {voltage current} {
    # Calculate power in watts given voltage (V) and current (A)
    # Formula: P = V * I
    # Return the power value
    return
}

proc convert_frequency {freq_mhz} {
    # Convert frequency in MHz to period in nanoseconds
    # Formula: period_ns = 1000 / freq_mhz
    # Return the period in nanoseconds
    return
}

proc check_timing_violation {slack_list} {
    # Given a list of slack values, return the number of violations (slack < 0)
    # Example: {0.1 -0.05 0.2 -0.15} should return 2
    return
}

proc parse_instance_name {full_path} {
    # Extract the instance name from a full hierarchical path
    # Example: "cpu_core/alu_inst/adder_u1" should return "adder_u1"
    # Hint: Use split and lindex
    return
}

proc generate_pin_list {base_name width} {
    # Generate a list of pin names for a bus
    # Example: generate_pin_list "data" 4 should return {data[0] data[1] data[2] data[3]}
    return
}

proc find_max_slack {timing_data} {
    # Given an array (pass by name) with timing data, find the maximum slack
    # Array format: timing_data(path1) = slack1, timing_data(path2) = slack2, etc.
    # Return the maximum slack value
    # Hint: Use upvar to access the array
    return
}

proc filter_instances {instance_list pattern} {
    # Filter a list of instances to find those matching a pattern
    # Example: filter_instances {alu_u1 mem_u1 alu_u2 ctrl_u1} "*alu*" 
    # should return {alu_u1 alu_u2}
    # Hint: Use string match
    return
}

# Test framework (don't modify below this line)
proc test_function {func_name expected_result args} {
    set result [eval $func_name $args]
    if {$result == $expected_result} {
        puts "✅ $func_name: PASSED"
        return 1
    } else {
        puts "❌ $func_name: FAILED"
        puts "   Expected: $expected_result"
        puts "   Got: $result"
        return 0
    }
}

proc run_tests {} {
    puts "Testing your implementations...\n"
    
    set passed 0
    set total 0
    
    # Test calculate_power
    incr total
    incr passed [test_function calculate_power 24.0 {5.0 4.8}]
    
    # Test convert_frequency  
    incr total
    incr passed [test_function convert_frequency 2.0 {500}]
    
    # Test check_timing_violation
    incr total
    incr passed [test_function check_timing_violation 2 {{0.1 -0.05 0.2 -0.15}}]
    
    # Test parse_instance_name
    incr total
    incr passed [test_function parse_instance_name "adder_u1" {"cpu_core/alu_inst/adder_u1"}]
    
    # Test generate_pin_list
    incr total
    incr passed [test_function generate_pin_list {data[0] data[1] data[2] data[3]} {"data" 4}]
    
    # Test find_max_slack
    incr total
    array set test_timing {
        path1 0.15
        path2 -0.05
        path3 0.25
        path4 -0.10
    }
    incr passed [test_function find_max_slack 0.25 {test_timing}]
    
    # Test filter_instances
    incr total
    incr passed [test_function filter_instances {alu_u1 alu_u2} {{alu_u1 mem_u1 alu_u2 ctrl_u1} "*alu*"}]
    
    puts "\nResults: $passed/$total tests passed"
    
    if {$passed == $total} {
        puts "🎉 Congratulations! All tests passed!"
        puts "You're ready for more advanced TCL exercises!"
    } else {
        puts "💡 Keep working on the failing tests."
        puts "Review the TCL fundamentals tutorial for help."
    }
}

# Instructions
puts "Complete the procedures above, then uncomment the line below to test:"
puts "# run_tests"
puts ""
puts "Hint: Study the test cases to understand what each function should do."
puts "Use the TCL fundamentals tutorial in basics/ for reference."

# Uncomment this line to run tests after implementing the functions:
# run_tests