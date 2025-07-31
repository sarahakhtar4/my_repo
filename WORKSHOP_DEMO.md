# Physical Design Scripting Workshop - Demo Guide

## Quick Start Demo

This guide demonstrates how to use the Physical Design Scripting Workshop for interview preparation.

## Workshop Structure

```
workshop/
├── README.md                 # Main documentation
├── WORKSHOP_DEMO.md         # This demo guide
├── python/                  # Python exercises
│   ├── exercises/           # Exercise files to solve
│   │   ├── basic/          # 8 basic exercises
│   │   ├── intermediate/   # 4 intermediate exercises  
│   │   └── advanced/       # 1 advanced exercise
│   ├── solutions/          # Reference solutions
│   └── test_runner.py      # Automated test framework
├── tcl/                    # TCL exercises
│   ├── exercises/          # Exercise files to solve
│   │   ├── basic/         # 2 basic exercises
│   │   ├── intermediate/  # Coming soon
│   │   └── advanced/      # Coming soon
│   ├── solutions/         # Reference solutions
│   └── test_runner.tcl    # Automated test framework
└── data/                  # Sample data files
    └── sample_liberty.lib
```

## Demo: Python Exercises

### 1. List Available Exercises

```bash
cd python
python3 test_runner.py --list
```

Output:
```
Available exercises:
  advanced/advanced_01.py
  basic/basic_01.py
  basic/basic_02.py
  basic/basic_03.py
  basic/basic_04.py
  basic/basic_05.py
  basic/basic_06.py
  basic/basic_07.py
  basic/basic_08.py
  intermediate/intermediate_01.py
  intermediate/intermediate_02.py
  intermediate/intermediate_03.py
  intermediate/intermediate_04.py
```

### 2. Test a Specific Exercise

```bash
python3 test_runner.py --exercise basic_01
```

This will run the tests for the first basic exercise and show results.

### 3. Run All Basic Exercises

```bash
python3 test_runner.py --category basic
```

### 4. Run All Exercises

```bash
python3 test_runner.py
```

## Demo: TCL Exercises

### 1. List TCL Exercises

```bash
cd tcl
tclsh test_runner.tcl --list
```

### 2. Test TCL Exercises

```bash
tclsh test_runner.tcl
```

## Sample Exercise: Python Basic_01

Let's look at the first Python exercise:

**File:** `python/exercises/basic/basic_01.py`

**Problem:** Calculate timing analysis statistics for timing paths.

**Your Task:** Implement the `solve()` function.

**Test Cases:** The exercise includes 5 test cases that automatically validate your solution.

## Exercise Categories

### Python Exercises

#### Basic (8 exercises)
1. **basic_01.py** - Timing Analysis Calculations
2. **basic_02.py** - Power Report Parser  
3. **basic_03.py** - Manhattan Distance Calculator
4. **basic_04.py** - Clock Frequency Analysis
5. **basic_05.py** - Area Utilization Calculator
6. **basic_06.py** - Net Delay Calculator
7. **basic_07.py** - Logic Gate Delay Calculator
8. **basic_08.py** - Pin Connectivity Analyzer

#### Intermediate (4 exercises)
1. **intermediate_01.py** - Liberty File Parser
2. **intermediate_02.py** - DEF Placement Analyzer
3. **intermediate_03.py** - Critical Path Analyzer
4. **intermediate_04.py** - Wirelength Optimizer

#### Advanced (1 exercise)
1. **advanced_01.py** - Clock Tree Synthesis Optimizer

### TCL Exercises

#### Basic (2 exercises)
1. **basic_01.tcl** - Instance List Processor
2. **basic_02.tcl** - Timing Constraint Parser

## Sample Solution Walkthrough

Let's solve `basic_01.py` step by step:

```python
def solve(timing_paths):
    if not timing_paths:
        return {
            'total_delay': 0.0,
            'max_delay': 0.0, 
            'min_delay': 0.0,
            'critical_paths': 0
        }
    
    # Extract delays from path tuples
    delays = [delay for _, delay in timing_paths]
    
    # Calculate statistics
    total_delay = sum(delays)
    max_delay = max(delays)
    min_delay = min(delays)
    
    # Critical paths: >= 90% of max delay
    critical_threshold = 0.9 * max_delay
    critical_paths = sum(1 for delay in delays if delay >= critical_threshold)
    
    return {
        'total_delay': total_delay,
        'max_delay': max_delay,
        'min_delay': min_delay,
        'critical_paths': critical_paths
    }
```

## Testing Your Solution

After implementing your solution, test it:

```bash
python3 test_runner.py --exercise basic_01
```

Expected output:
```
🚀 Physical Design Scripting Workshop - Python Test Runner
============================================================

📝 Testing: basic/basic_01.py
----------------------------------------
[10:30:15] PASS: Basic timing analysis (0.123ms)
[10:30:15] PASS: Small path set (0.098ms)
[10:30:15] PASS: Multiple critical paths (0.145ms)
[10:30:15] PASS: Single path edge case (0.087ms)
[10:30:15] PASS: Empty paths list (0.076ms)
[10:30:15] PASS: Exercise basic_01: 5/5 (100.0%)

============================================================
📊 FINAL SUMMARY
============================================================
Exercises passed: 1/1
Overall success rate: 100.0%
🏆 Congratulations! All exercises completed successfully!
```

## Interview Tips

1. **Time Management**: Aim for 15-30 minutes per exercise
2. **Code Quality**: Write clean, readable code with proper error handling
3. **Edge Cases**: Always handle empty inputs and boundary conditions
4. **Testing**: Use the provided test framework to validate your solutions
5. **Physical Design Knowledge**: Understand the underlying concepts (timing, power, placement, etc.)

## Next Steps

1. Start with basic exercises to build confidence
2. Progress to intermediate exercises for algorithm practice  
3. Tackle advanced exercises for complex optimization problems
4. Practice explaining your solutions verbally
5. Time yourself to simulate interview conditions

## Getting Help

- Read the problem statements carefully
- Look at the expected output format
- Check the hint comments in each exercise
- Review the sample data files in `data/` directory
- Practice similar problems to build pattern recognition

Good luck with your physical design interviews! 🚀