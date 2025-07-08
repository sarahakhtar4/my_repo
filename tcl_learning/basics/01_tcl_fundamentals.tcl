#!/usr/bin/env tclsh
# TCL Fundamentals for EDA and Physical Design
# ============================================
#
# This tutorial covers TCL basics specifically for EDA tool scripting.
# TCL is the primary scripting language for most EDA tools including
# Synopsys, Cadence, and Mentor Graphics tools.

puts "=== TCL Fundamentals for EDA ==="
puts ""

# 1. BASIC SYNTAX AND VARIABLES
puts "1. BASIC SYNTAX AND VARIABLES:"

# Variables in TCL (no declaration needed)
set design_name "cpu_core"
set clock_period 1.0
set voltage 1.8
set temperature 25

puts "  Design: $design_name"
puts "  Clock period: $clock_period ns"
puts "  Voltage: $voltage V"
puts "  Temperature: $temperature C"

# String manipulation
set full_design_name "${design_name}_${voltage}v_${temperature}c"
puts "  Full design name: $full_design_name"

puts ""

# 2. LISTS (Very important in EDA scripting)
puts "2. LISTS (Critical for EDA):"

# Create lists of pins, nets, instances
set input_pins {clk reset data_in[31:0] enable}
set output_pins {data_out[31:0] ready error}
set clock_pins {clk clk_div2 clk_div4}

puts "  Input pins: $input_pins"
puts "  Number of input pins: [llength $input_pins]"

# List operations
lappend input_pins scan_enable
puts "  After adding scan_enable: $input_pins"

# Iterate through lists
puts "  Clock pins:"
foreach pin $clock_pins {
    puts "    - $pin"
}

# List searching
if {[lsearch $input_pins "clk"] >= 0} {
    puts "  Clock pin found in input list"
}

puts ""

# 3. CONTROL STRUCTURES
puts "3. CONTROL STRUCTURES:"

# if-else for design conditions
set current_slack -0.15
if {$current_slack < 0} {
    puts "  Timing violation detected: ${current_slack}ns"
    set needs_optimization 1
} elseif {$current_slack < 0.1} {
    puts "  Timing is marginal: ${current_slack}ns"
    set needs_optimization 1
} else {
    puts "  Timing is good: ${current_slack}ns"
    set needs_optimization 0
}

# for loops for iterating over ranges
puts "  Clock frequency analysis:"
for {set freq 100} {$freq <= 1000} {set freq [expr $freq + 100]} {
    set period [expr 1000.0 / $freq]
    puts "    ${freq}MHz -> ${period}ns period"
}

# while loops for optimization iterations
set iteration 1
set slack $current_slack
puts "  Optimization iterations:"
while {$slack < 0 && $iteration <= 5} {
    puts "    Iteration $iteration: slack = ${slack}ns"
    # Simulate optimization improving slack
    set slack [expr $slack + 0.05]
    incr iteration
}

puts ""

# 4. PROCEDURES (Functions)
puts "4. PROCEDURES (Essential for reusable scripts):"

# Procedure to convert frequency to period
proc freq_to_period {frequency_mhz} {
    set period_ns [expr 1000.0 / $frequency_mhz]
    return $period_ns
}

# Procedure to check timing
proc check_timing_status {slack_value} {
    if {$slack_value < 0} {
        return "VIOLATED"
    } else {
        return "MET"
    }
}

# Procedure to generate corner conditions
proc generate_corner_conditions {} {
    # Return a list of corner conditions
    set corners {}
    foreach voltage {0.95 1.0 1.05} {
        foreach temp {-40 25 125} {
            lappend corners "V${voltage}_T${temp}"
        }
    }
    return $corners
}

# Test the procedures
set freq 500
set period [freq_to_period $freq]
puts "  ${freq}MHz corresponds to ${period}ns"

set status [check_timing_status -0.025]
puts "  Timing status for -0.025ns slack: $status"

set corners [generate_corner_conditions]
puts "  Corner conditions: $corners"

puts ""

# 5. STRING OPERATIONS (Critical for parsing)
puts "5. STRING OPERATIONS:"

# String matching and manipulation
set cell_name "cpu_core/alu_inst/adder_u1/FA_bit_15"
set pin_name "cpu_core/reg_file/Q[15]"

# Extract parts of hierarchical names
if {[regexp {^(.+)/([^/]+)$} $cell_name match hierarchy inst]} {
    puts "  Cell hierarchy: $hierarchy"
    puts "  Instance name: $inst"
}

# Extract bus indices
if {[regexp {\[(\d+)\]} $pin_name match index]} {
    puts "  Pin index: $index"
}

# String substitution (useful for design modifications)
set new_cell_name [string map {"adder" "multiplier"} $cell_name]
puts "  Modified cell name: $new_cell_name"

# Case conversion
set upper_design [string toupper $design_name]
puts "  Uppercase design: $upper_design"

puts ""

# 6. FILE I/O (Reading/writing reports and scripts)
puts "6. FILE I/O:"

# Write configuration file
set config_file "design_config.tcl"
set fp [open $config_file w]
puts $fp "# Auto-generated design configuration"
puts $fp "set_design_name $design_name"
puts $fp "set_clock_period $clock_period"
puts $fp "set_voltage $voltage"
puts $fp "set_temperature $temperature"
close $fp
puts "  Configuration written to $config_file"

# Read and process the file
if {[file exists $config_file]} {
    set fp [open $config_file r]
    puts "  Reading configuration:"
    while {[gets $fp line] >= 0} {
        if {![string match "#*" $line] && [string length $line] > 0} {
            puts "    $line"
        }
    }
    close $fp
}

puts ""

# 7. ARRAYS AND DICTIONARIES
puts "7. ARRAYS (for storing EDA data):"

# Arrays for storing timing data
array set timing_data {}
set timing_data(setup,worst) -0.15
set timing_data(setup,best) 0.25
set timing_data(hold,worst) 0.05
set timing_data(hold,best) 0.18

puts "  Timing summary:"
foreach {key value} [array get timing_data] {
    puts "    $key: ${value}ns"
}

# Multi-dimensional array indexing
array set cell_area {}
set cell_area(NAND2X1) 2.5
set cell_area(INVX1) 1.2
set cell_area(DFF) 8.4

puts "  Cell areas:"
foreach cell [array names cell_area] {
    puts "    $cell: $cell_area($cell) square microns"
}

puts ""

# 8. ERROR HANDLING
puts "8. ERROR HANDLING:"

# Safe file reading with error handling
proc safe_read_file {filename} {
    if {[catch {
        set fp [open $filename r]
        set content [read $fp]
        close $fp
        return $content
    } error]} {
        puts "Error reading file $filename: $error"
        return ""
    }
}

# Safe command execution
proc safe_command {command} {
    if {[catch {
        eval $command
    } result]} {
        puts "Command failed: $command"
        puts "Error: $result"
        return 0
    } else {
        puts "Command succeeded: $command"
        return 1
    }
}

# Test error handling
set result [safe_read_file "nonexistent_file.txt"]
puts "  File read result: [string length $result] characters"

puts ""

# 9. COMMON EDA PATTERNS
puts "9. COMMON EDA SCRIPTING PATTERNS:"

# Pattern: Process all instances of a type
proc process_instances_by_type {instance_type} {
    # This would typically get instances from EDA tool
    # For demo, we'll simulate
    set instances {inst1 inst2 inst3 inst4}
    
    puts "  Processing $instance_type instances:"
    foreach inst $instances {
        puts "    Analyzing $inst..."
        # Here you'd do actual EDA tool commands like:
        # get_attribute $inst area
        # report_timing -from $inst
    }
}

# Pattern: Iterate through design hierarchy
proc traverse_hierarchy {top_level} {
    puts "  Traversing hierarchy from $top_level:"
    # Simulate hierarchy levels
    set levels {
        "cpu_core" 
        "cpu_core/alu" 
        "cpu_core/regfile" 
        "cpu_core/control"
    }
    
    foreach level $levels {
        set depth [expr [llength [split $level "/"]] - 1]
        set indent [string repeat "  " $depth]
        puts "  $indent- $level"
    }
}

# Pattern: Generate reports for multiple corners
proc generate_corner_reports {} {
    set corners [generate_corner_conditions]
    puts "  Generating reports for all corners:"
    
    foreach corner $corners {
        puts "    Report for corner $corner:"
        puts "      - Setting up corner conditions..."
        puts "      - Running timing analysis..."
        puts "      - Generating timing report..."
        puts "      - Report saved to timing_${corner}.rpt"
    }
}

# Test the patterns
process_instances_by_type "DFF"
traverse_hierarchy "cpu_core"
generate_corner_reports

puts ""
puts "=== End of TCL Fundamentals ==="
puts "Next: Study 02_eda_tool_integration.tcl for tool-specific commands"

# Clean up demo files
file delete -force $config_file