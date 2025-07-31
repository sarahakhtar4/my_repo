#!/usr/bin/tclsh
#
# Physical Design Scripting Workshop - TCL Test Runner
# Automated testing framework for all TCL exercises
#

package require Tcl 8.5

# Global test statistics
set total_exercises 0
set passed_exercises 0
set total_tests 0
set passed_tests 0

# Test runner configuration
set test_config {}

proc log_message {level message} {
    set timestamp [clock format [clock seconds] -format "%H:%M:%S"]
    set colors {
        "INFO"  "\033\[32m"
        "WARN"  "\033\[33m" 
        "ERROR" "\033\[31m"
        "PASS"  "\033\[32m"
        "FAIL"  "\033\[31m"
    }
    set reset "\033\[0m"
    
    if {[dict exists $colors $level]} {
        set color [dict get $colors $level]
        puts "${color}\[$timestamp\] $level: $message${reset}"
    } else {
        puts "\[$timestamp\] $level: $message"
    }
}

proc compare_results {result expected {tolerance 1e-6}} {
    # Compare results with tolerance for floating point numbers
    if {[string is double -strict $result] && [string is double -strict $expected]} {
        return [expr {abs($result - $expected) < $tolerance}]
    } elseif {[llength $result] == [llength $expected]} {
        # Compare lists element by element
        for {set i 0} {$i < [llength $result]} {incr i} {
            set r_elem [lindex $result $i]
            set e_elem [lindex $expected $i]
            if {![compare_results $r_elem $e_elem $tolerance]} {
                return 0
            }
        }
        return 1
    } else {
        return [expr {$result eq $expected}]
    }
}

proc run_test_case {exercise_proc test_case} {
    global passed_tests total_tests
    
    set description [dict get $test_case description]
    set input_args [dict get $test_case input]
    set expected [dict get $test_case expected]
    
    incr total_tests
    
    set start_time [clock microseconds]
    
    try {
        # Call the exercise procedure with input arguments
        set result [eval $exercise_proc $input_args]
        set exec_time [expr {([clock microseconds] - $start_time) / 1000.0}]
        
        # Compare result with expected output
        if {[compare_results $result $expected]} {
            log_message "PASS" "$description (${exec_time}ms)"
            incr passed_tests
            return 1
        } else {
            log_message "FAIL" "$description - Expected: $expected, Got: $result"
            return 0
        }
    } on error {err} {
        set exec_time [expr {([clock microseconds] - $start_time) / 1000.0}]
        log_message "ERROR" "$description - $err (${exec_time}ms)"
        return 0
    }
}

proc run_exercise_tests {exercise_file} {
    global total_exercises passed_exercises
    
    incr total_exercises
    
    # Source the exercise file
    if {[catch {source $exercise_file} err]} {
        log_message "ERROR" "Failed to load $exercise_file: $err"
        return
    }
    
    # Check if test configuration exists
    if {![info exists ::test_config]} {
        log_message "ERROR" "No test configuration found in $exercise_file"
        return
    }
    
    set exercise_name [file tail [file rootname $exercise_file]]
    set function_name [dict get $::test_config function_name]
    set test_cases [dict get $::test_config test_cases]
    
    log_message "INFO" "Testing $exercise_name (function: $function_name)"
    puts "----------------------------------------"
    
    # Check if the function exists
    if {![llength [info procs $function_name]]} {
        log_message "ERROR" "Function '$function_name' not found"
        return
    }
    
    set exercise_passed 0
    set exercise_total 0
    
    foreach test_case $test_cases {
        incr exercise_total
        if {[run_test_case $function_name $test_case]} {
            incr exercise_passed
        }
    }
    
    set success_rate [expr {$exercise_total > 0 ? ($exercise_passed * 100.0 / $exercise_total) : 0}]
    
    if {$exercise_passed == $exercise_total} {
        log_message "PASS" "Exercise $exercise_name: $exercise_passed/$exercise_total (${success_rate}%)"
        incr passed_exercises
    } else {
        log_message "FAIL" "Exercise $exercise_name: $exercise_passed/$exercise_total (${success_rate}%)"
    }
    
    puts ""
    
    # Clean up test configuration
    unset ::test_config
}

proc find_exercises {category} {
    set exercise_files {}
    
    if {$category ne ""} {
        set category_dir "exercises/$category"
        if {[file exists $category_dir]} {
            set pattern "$category_dir/*.tcl"
            set exercise_files [glob -nocomplain $pattern]
        }
    } else {
        foreach cat {basic intermediate advanced} {
            set category_dir "exercises/$cat"
            if {[file exists $category_dir]} {
                set pattern "$category_dir/*.tcl"
                lappend exercise_files {*}[glob -nocomplain $pattern]
            }
        }
    }
    
    return [lsort $exercise_files]
}

proc print_usage {} {
    puts "Physical Design TCL Workshop Test Runner"
    puts "Usage: tclsh test_runner.tcl \[options\]"
    puts ""
    puts "Options:"
    puts "  --exercise <name>    Run specific exercise"
    puts "  --category <cat>     Run exercises from category (basic/intermediate/advanced)"
    puts "  --list              List all available exercises"
    puts "  --help              Show this help message"
    puts ""
}

proc main {argv} {
    global total_exercises passed_exercises total_tests passed_tests
    
    # Parse command line arguments
    set exercise_name ""
    set category ""
    set list_exercises 0
    set show_help 0
    
    for {set i 0} {$i < [llength $argv]} {incr i} {
        set arg [lindex $argv $i]
        switch -- $arg {
            "--exercise" {
                if {$i + 1 < [llength $argv]} {
                    set exercise_name [lindex $argv [incr i]]
                }
            }
            "--category" {
                if {$i + 1 < [llength $argv]} {
                    set category [lindex $argv [incr i]]
                }
            }
            "--list" {
                set list_exercises 1
            }
            "--help" {
                set show_help 1
            }
        }
    }
    
    if {$show_help} {
        print_usage
        return
    }
    
    # Find available exercises
    set exercises [find_exercises $category]
    
    if {$list_exercises} {
        puts "Available exercises:"
        foreach exercise $exercises {
            puts "  [file tail $exercise]"
        }
        return
    }
    
    # Filter by exercise name if specified
    if {$exercise_name ne ""} {
        set filtered_exercises {}
        foreach exercise $exercises {
            if {[file tail [file rootname $exercise]] eq $exercise_name} {
                lappend filtered_exercises $exercise
            }
        }
        set exercises $filtered_exercises
    }
    
    if {[llength $exercises] == 0} {
        log_message "ERROR" "No exercises found!"
        return
    }
    
    # Print header
    puts "🚀 Physical Design Scripting Workshop - TCL Test Runner"
    puts "============================================================"
    
    # Run all exercises
    foreach exercise $exercises {
        run_exercise_tests $exercise
    }
    
    # Print summary
    puts "============================================================"
    puts "📊 FINAL SUMMARY"
    puts "============================================================"
    puts "Exercises passed: $passed_exercises/$total_exercises"
    puts "Tests passed: $passed_tests/$total_tests"
    
    set exercise_rate [expr {$total_exercises > 0 ? ($passed_exercises * 100.0 / $total_exercises) : 0}]
    set test_rate [expr {$total_tests > 0 ? ($passed_tests * 100.0 / $total_tests) : 0}]
    
    puts "Exercise success rate: ${exercise_rate}%"
    puts "Test success rate: ${test_rate}%"
    
    if {$passed_exercises == $total_exercises} {
        log_message "PASS" "🏆 Congratulations! All exercises completed successfully!"
    } else {
        log_message "WARN" "💪 Keep practicing! Review the failed exercises."
    }
}

# Run main if this script is executed directly
if {[info exists argv0] && $argv0 eq [info script]} {
    main $argv
}