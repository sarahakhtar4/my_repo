# 🧪 CoderPad-Style Exercises for Physical Design Scripting

## 📋 Complete Exercise Collection

Perfect for interview preparation! These exercises simulate real physical design scripting challenges you'll face in interviews and on the job.

## 🎯 Exercise Overview

| Exercise | Skill Level | Focus Area | Key Skills |
|----------|------------|------------|------------|
| [Exercise 1](exercise_1_basic_parsing.py) | ✅ **COMPLETED** | Basic Parsing | File I/O, string processing |
| [Exercise 2](exercise_2_timing_parser.py) | 🔥 **NEW** | Timing Reports | Regex, pattern matching |
| [Exercise 3](exercise_3_lib_parser.py) | 🔥 **NEW** | Liberty Files | Text analysis, counting |
| [Exercise 4](exercise_4_file_renamer.py) | 🔥 **NEW** | File Operations | Path handling, batch operations |
| [Exercise 5](exercise_5_capacitance_violations.py) | 🔥 **NEW** | Design Rules | Data filtering, violation analysis |
| [Exercise 6](exercise_6_tcl_generator.py) | 🔥 **NEW** | TCL Generation | Template generation, EDA scripts |
| [Exercise 7](exercise_7_regex_practice.py) | 🔥 **NEW** | Regex Mastery | Pattern matching, number extraction |
| [Exercise 8](exercise_8_duplicate_nets.py) | 🔥 **NEW** | Netlist Analysis | Duplicate detection, validation |
| [Exercise 9](exercise_9_cell_sorting.py) | 🔥 **NEW** | Data Analysis | Sorting, optimization, reporting |

## 🚀 Quick Start Guide

### For Each Exercise:
1. **Read the problem** in the docstring
2. **Implement the TODO functions**
3. **Run the tests** to check your solution
4. **Study the hints** if you get stuck

### Example Workflow:
```bash
# Start with Exercise 2 (since you completed Exercise 1)
cd python_learning/exercises
python3 exercise_2_timing_parser.py

# The output will show:
# - ✅ PASS if your implementation works
# - ❌ FAIL with hints if there are issues
```

## 📊 Exercise Details

### 🔥 Exercise 2: Parse Timing Reports
**File:** `exercise_2_timing_parser.py`
**Skills:** Regex, string processing, pattern matching
**Challenge:** Extract startpoints from timing reports
```python
# Sample input:
"Startpoint: cpu_inst/reg1 (rising edge-triggered flip-flop)"
# Expected output:
['cpu_inst/reg1']
```

### 🔥 Exercise 3: Summarize Liberty Files
**File:** `exercise_3_lib_parser.py`
**Skills:** Text analysis, counting, data structures
**Challenge:** Count cells and pins in .lib files
```python
# Expected output:
{'cell_count': 5, 'pin_count': 13}
```

### 🔥 Exercise 4: File Renamer for Reports
**File:** `exercise_4_file_renamer.py`
**Skills:** File I/O, path operations, batch processing
**Challenge:** Rename .rpt files to add _backup suffix
```python
# setup_report.rpt → setup_report_backup.rpt
```

### 🔥 Exercise 5: Capacitance Violation Finder
**File:** `exercise_5_capacitance_violations.py`
**Skills:** Data filtering, analysis, violation detection
**Challenge:** Find pins exceeding capacitance limits
```python
# Find pins where cap > 0.1pF
pins = {'U1/A': 0.08, 'U2/B': 0.12}  # U2/B violates
```

### 🔥 Exercise 6: TCL Script Generator
**File:** `exercise_6_tcl_generator.py`
**Skills:** Template generation, string formatting
**Challenge:** Generate EDA tool scripts from data
```python
# Generate: set_dont_use "CELL1"
```

### 🔥 Exercise 7: Regex Practice
**File:** `exercise_7_regex_practice.py`
**Skills:** Regular expressions, number extraction
**Challenge:** Extract floats from EDA reports
```python
# "power=0.15, delay=2.3ns" → [0.15, 2.3]
```

### 🔥 Exercise 8: Duplicate Net Finder
**File:** `exercise_8_duplicate_nets.py`
**Skills:** Data validation, duplicate detection
**Challenge:** Find duplicate nets in netlists
```python
# net1 U1/A U2/B
# net1 U3/C U4/D  ← Duplicate!
```

### 🔥 Exercise 9: Cell Sorting & Analysis
**File:** `exercise_9_cell_sorting.py`
**Skills:** Sorting, data analysis, optimization
**Challenge:** Sort cells by area, analyze libraries
```python
# Sort by area: [('DFFQX1', 8.7), ('BUFX4', 4.1), ...]
```

## 🎯 Recommended Learning Path

### Path A: Sequential (Recommended for beginners)
1. ✅ Exercise 1 (COMPLETED) → Exercise 2 → Exercise 3 → Exercise 4...

### Path B: By Skill Area
- **Text Processing:** Exercises 2, 3, 7, 8
- **File Operations:** Exercises 1, 4, 6
- **Data Analysis:** Exercises 5, 9
- **Real-world Application:** Exercises 2, 5, 6

### Path C: Interview Prep (Focus on common questions)
1. **Exercise 2** (Timing report parsing) - Very common!
2. **Exercise 5** (Violation analysis) - Classic question
3. **Exercise 7** (Regex skills) - Essential skill
4. **Exercise 6** (Script generation) - Shows automation skills

## 💡 Success Tips

### For Each Exercise:
- ✅ **Read the entire file** including test data and hints
- ✅ **Start simple** - get basic functionality working first
- ✅ **Use the test functions** to validate your solution
- ✅ **Study the hints** - they contain valuable patterns
- ✅ **Try the advanced versions** for extra practice

### Common Patterns You'll Learn:
- **File parsing:** `for line in content.split('\n')`
- **Regex matching:** `re.findall(pattern, text)`
- **Dictionary operations:** `{k: v for k, v in dict.items() if condition}`
- **Sorting:** `sorted(items, key=lambda x: x[1], reverse=True)`

## 🏆 Interview Readiness Checklist

After completing these exercises, you should be able to:
- ✅ Parse complex EDA reports and files
- ✅ Use regular expressions for pattern matching
- ✅ Handle file I/O operations efficiently
- ✅ Filter and analyze data sets
- ✅ Generate automated scripts and reports
- ✅ Validate and debug design data
- ✅ Sort and optimize design characteristics

## 🎪 Challenge Mode

### Time Yourself!
- **Exercise 2:** Can you solve it in 10 minutes?
- **Exercise 5:** Can you complete basic + advanced in 15 minutes?
- **Exercise 7:** Master regex in 20 minutes?

### Extend the Exercises:
- Add error handling and edge cases
- Optimize for performance with large datasets
- Add more output formats (JSON, CSV, XML)
- Create GUI versions using tkinter

## 🔧 Getting Help

### If You Get Stuck:
1. **Read the hints** in each exercise file
2. **Study the test data** to understand expected formats
3. **Check the docstrings** for detailed requirements
4. **Look at similar patterns** in other exercises

### Common Issues:
- **Regex not working?** Test your patterns on regex101.com
- **File operations failing?** Check file paths and permissions
- **Tests failing?** Compare your output format exactly with expected

## 🎉 Completion Rewards

### After Each Exercise:
- 🏅 **Master a new skill** useful in physical design
- 🧠 **Build pattern recognition** for similar problems
- 💪 **Increase interview confidence**
- 🚀 **Add practical examples to your portfolio**

### After All Exercises:
- 🎯 **Ready for coding interviews** in physical design roles
- 📚 **Comprehensive scripting skillset** for EDA tools
- 🔧 **Real-world problem-solving experience**
- 💼 **Portfolio of working solutions** to show employers

---

**Start your next exercise now!** You've got this! 🚀

```bash
# Ready for Exercise 2?
python3 exercise_2_timing_parser.py
```