#!/usr/bin/env tclsh
# EDA Tool Integration with TCL
# =============================
#
# This tutorial shows common patterns for integrating TCL with EDA tools.
# These patterns are used across Synopsys, Cadence, and other EDA vendors.

puts "=== EDA Tool Integration with TCL ==="
puts ""

# 1. DESIGN OBJECT MANIPULATION
puts "1. DESIGN OBJECT MANIPULATION PATTERNS:"

# Simulate common EDA tool object commands
# In real tools, these would be: get_cells, get_pins, get_nets, etc.

proc simulate_get_cells {pattern} {
    # Simulate getting cells matching a pattern
    set all_cells {
        "cpu_core/alu_inst"
        "cpu_core/regfile_inst" 
        "cpu_core/ctrl_inst"
        "cpu_core/alu_inst/add_u1"
        "cpu_core/alu_inst/mult_u1"
        "cpu_core/regfile_inst/reg_0"
        "cpu_core/regfile_inst/reg_1"
    }
    
    set matching_cells {}
    foreach cell $all_cells {
        if {[string match $pattern $cell]} {
            lappend matching_cells $cell
        }
    }
    return $matching_cells
}

# Pattern: Get all cells in a hierarchy
set alu_cells [simulate_get_cells "cpu_core/alu_inst/*"]
puts "  ALU instances: $alu_cells"

# Pattern: Get cells by type (using wildcards)
set reg_cells [simulate_get_cells "*reg*"]
puts "  Register-related instances: $reg_cells"

puts ""

# 2. TIMING ANALYSIS PATTERNS
puts "2. TIMING ANALYSIS INTEGRATION:"

# Simulate timing analysis commands
proc simulate_report_timing {args} {
    # Parse arguments (simplified)
    set from_pin ""
    set to_pin ""
    set path_group ""
    set delay_type "max"
    
    # Process arguments
    for {set i 0} {$i < [llength $args]} {incr i} {
        set arg [lindex $args $i]
        switch -- $arg {
            "-from" {
                incr i
                set from_pin [lindex $args $i]
            }
            "-to" {
                incr i  
                set to_pin [lindex $args $i]
            }
            "-group" {
                incr i
                set path_group [lindex $args $i]
            }
            "-delay_type" {
                incr i
                set delay_type [lindex $args $i]
            }
        }
    }
    
    # Simulate timing report
    puts "    Timing Report ($delay_type delay):"
    if {$from_pin != ""} {puts "      From: $from_pin"}
    if {$to_pin != ""} {puts "      To: $to_pin"}
    if {$path_group != ""} {puts "      Path Group: $path_group"}
    
    # Simulate slack calculation
    set slack [expr rand() * 0.5 - 0.1]  ;# Random slack between -0.1 and 0.4
    puts "      Slack: [format "%.3f" $slack]ns"
    
    return $slack
}

# Pattern: Report timing for specific paths
puts "  Analyzing critical timing paths:"
set slack1 [simulate_report_timing -from "clk" -to "cpu_core/alu_inst/result_reg/D"]
set slack2 [simulate_report_timing -from "cpu_core/regfile_inst" -to "cpu_core/alu_inst"]

puts ""

# 3. CONSTRAINT APPLICATION PATTERNS
puts "3. CONSTRAINT APPLICATION:"

# Pattern: Apply constraints using TCL
proc apply_clock_constraints {clk_pin period} {
    puts "    create_clock -name main_clk -period $period [get_ports $clk_pin]"
    puts "    set_clock_uncertainty 0.1 [get_clocks main_clk]"
    puts "    set_clock_transition 0.05 [get_clocks main_clk]"
}

proc apply_io_constraints {input_delay output_delay} {
    puts "    set_input_delay $input_delay -clock main_clk [get_ports data_in*]"
    puts "    set_output_delay $output_delay -clock main_clk [get_ports data_out*]"
}

proc apply_driving_cells {} {
    puts "    set_driving_cell -lib_cell BUFX4 [get_ports data_in*]"
    puts "    set_load 0.05 [get_ports data_out*]"
}

puts "  Applying design constraints:"
apply_clock_constraints "clk" 1.0
apply_io_constraints 0.2 0.3
apply_driving_cells

puts ""

# 4. MULTI-CORNER ANALYSIS
puts "4. MULTI-CORNER ANALYSIS:"

# Pattern: Define operating conditions
proc setup_operating_corner {corner_name voltage temp process} {
    puts "    Setting up corner: $corner_name"
    puts "      set_operating_conditions \\"
    puts "        -voltage $voltage \\"
    puts "        -temperature $temp \\"
    puts "        -process $process"
}

# Pattern: Analyze all corners
proc analyze_all_corners {} {
    # Define corner conditions
    set corners {
        {worst_case 0.95 125 slow}
        {typical 1.0 25 typical}
        {best_case 1.05 -40 fast}
    }
    
    array set results {}
    
    foreach corner_spec $corners {
        set corner_name [lindex $corner_spec 0]
        set voltage [lindex $corner_spec 1]
        set temp [lindex $corner_spec 2]
        set process [lindex $corner_spec 3]
        
        puts "  Analyzing corner: $corner_name"
        setup_operating_corner $corner_name $voltage $temp $process
        
        # Simulate timing analysis for this corner
        set slack [expr rand() * 0.4 - 0.2]  ;# Random slack
        set results($corner_name) $slack
        
        puts "    Worst slack: [format "%.3f" $slack]ns"
    }
    
    return [array get results]
}

array set corner_results [analyze_all_corners]

puts ""

# 5. REPORT GENERATION AND PARSING
puts "5. REPORT GENERATION AND PARSING:"

# Pattern: Generate and parse reports
proc generate_area_report {output_file} {
    # Simulate generating an area report
    set fp [open $output_file w]
    puts $fp "Area Report"
    puts $fp "==========="
    puts $fp ""
    
    # Simulate area data
    array set areas {
        "Combinational" 1234.5
        "Sequential" 987.6
        "Total" 2222.1
    }
    
    foreach {type area} [array get areas] {
        puts $fp [format "%-15s: %8.1f sq um" $type $area]
    }
    
    close $fp
    puts "    Area report written to: $output_file"
}

proc parse_area_report {report_file} {
    if {![file exists $report_file]} {
        puts "    Error: Report file not found"
        return
    }
    
    set fp [open $report_file r]
    array set parsed_areas {}
    
    while {[gets $fp line] >= 0} {
        # Look for area data lines
        if {[regexp {^(\w+)\s*:\s*([\d.]+)} $line match type area]} {
            set parsed_areas($type) $area
            puts "    Parsed $type area: $area sq um"
        }
    }
    
    close $fp
    return [array get parsed_areas]
}

# Test report generation and parsing
generate_area_report "area_report.txt"
parse_area_report "area_report.txt"

puts ""

# 6. DESIGN MODIFICATION PATTERNS
puts "6. DESIGN MODIFICATION PATTERNS:"

# Pattern: Instance replacement
proc replace_instances {old_cell new_cell instance_list} {
    puts "    Replacing $old_cell with $new_cell:"
    foreach inst $instance_list {
        puts "      replace_cell $inst $new_cell"
        puts "      # Instance $inst updated"
    }
}

# Pattern: Pin assignment
proc assign_pins {pin_list location_list} {
    puts "    Pin assignments:"
    for {set i 0} {$i < [llength $pin_list]} {incr i} {
        set pin [lindex $pin_list $i]
        set loc [lindex $location_list $i]
        puts "      set_location $pin $loc"
    }
}

# Pattern: Clock tree insertion
proc insert_clock_tree {clk_pin} {
    puts "    Clock tree synthesis for $clk_pin:"
    puts "      set_clock_tree_options -target_skew 0.1"
    puts "      synthesize_clock_tree"
    puts "      route_clock_tree"
}

# Test design modifications
set old_instances [simulate_get_cells "*buffer*"]
replace_instances "BUFX1" "BUFX2" $old_instances

set pins {clk reset data_valid}
set locations {A1 B1 C1}
assign_pins $pins $locations

insert_clock_tree "clk"

puts ""

# 7. SCRIPTING FLOW CONTROL
puts "7. SCRIPTING FLOW CONTROL:"

# Pattern: Check and continue flow
proc check_design_rules {} {
    # Simulate design rule checking
    set violations [expr int(rand() * 10)]
    puts "    Design rule violations: $violations"
    return $violations
}

proc run_synthesis_flow {} {
    puts "  Running synthesis flow:"
    
    # Step 1: Check design
    puts "    Step 1: Checking design..."
    if {[check_design_rules] > 0} {
        puts "    Warning: Design has violations, but continuing..."
    }
    
    # Step 2: Synthesize
    puts "    Step 2: Running synthesis..."
    set success [expr rand() > 0.1]  ;# 90% success rate
    
    if {!$success} {
        puts "    Error: Synthesis failed!"
        return 0
    }
    
    # Step 3: Optimize
    puts "    Step 3: Optimizing design..."
    puts "    Step 4: Generating reports..."
    
    return 1
}

# Pattern: Conditional flow execution
if {[run_synthesis_flow]} {
    puts "  Synthesis completed successfully"
    puts "  Proceeding to place and route..."
} else {
    puts "  Synthesis failed - stopping flow"
}

puts ""

# 8. UTILITY PROCEDURES
puts "8. COMMON UTILITY PROCEDURES:"

# Pattern: Hierarchical name utilities
proc get_hierarchy_level {full_name} {
    return [llength [split $full_name "/"]]
}

proc get_parent_instance {full_name} {
    set parts [split $full_name "/"]
    if {[llength $parts] > 1} {
        return [join [lrange $parts 0 end-1] "/"]
    }
    return ""
}

proc get_instance_name {full_name} {
    set parts [split $full_name "/"]
    return [lindex $parts end]
}

# Pattern: Timing utilities
proc ns_to_ps {time_ns} {
    return [expr $time_ns * 1000]
}

proc mhz_to_ns {freq_mhz} {
    return [expr 1000.0 / $freq_mhz]
}

# Test utilities
set full_inst "cpu_core/alu_inst/adder_u1"
puts "  Hierarchy utilities:"
puts "    Full name: $full_inst"
puts "    Hierarchy level: [get_hierarchy_level $full_inst]"
puts "    Parent: [get_parent_instance $full_inst]"
puts "    Instance name: [get_instance_name $full_inst]"

puts "  Timing utilities:"
puts "    500MHz = [mhz_to_ns 500]ns period"
puts "    0.5ns = [ns_to_ps 0.5]ps"

puts ""

# 9. LOGGING AND DEBUG
puts "9. LOGGING AND DEBUG PATTERNS:"

# Pattern: Logging with timestamps
proc log_message {level message} {
    set timestamp [clock format [clock seconds] -format "%Y-%m-%d %H:%M:%S"]
    puts "\[$timestamp\] \[$level\] $message"
}

# Pattern: Debug mode
set DEBUG_MODE 1

proc debug_print {message} {
    global DEBUG_MODE
    if {$DEBUG_MODE} {
        log_message "DEBUG" $message
    }
}

# Test logging
log_message "INFO" "Starting design flow"
debug_print "Debug information: variables initialized"
log_message "WARNING" "Clock uncertainty is high"

puts ""
puts "=== End of EDA Tool Integration ==="
puts "Next: Practice with the exercises in tcl_learning/exercises/"

# Clean up demo files
file delete -force "area_report.txt"