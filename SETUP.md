# Quick Setup Guide

## Environment Setup

Since this workspace may have dependency installation limitations, here's how to get started quickly:

### Option 1: Core Python Only (Recommended for immediate start)
Most tutorials and exercises work with just Python's built-in libraries:

```bash
# Test the main timing comparison script
cd python_learning/timing_analysis
python3 timing_compare.py

# Try the basic Python tutorials
cd ../basics
python3 01_python_for_eda.py
python3 02_file_parsing.py

# Practice with exercises
cd ../exercises
python3 exercise_1_basic_parsing.py
```

### Option 2: Install Dependencies (if possible)
If you can install packages, set up the full environment:

```bash
# Try one of these approaches:
pip install --user -r requirements.txt
# OR
pip install --break-system-packages -r requirements.txt
# OR create virtual environment if available
python3 -m venv learning_env
source learning_env/bin/activate
pip install -r requirements.txt
```

### Option 3: Use Available System Packages
Check what's already available:

```bash
python3 -c "import sys; print(sys.modules.keys())"
```

## TCL Setup

TCL works out of the box:

```bash
# Test TCL fundamentals
cd tcl_learning/basics
tclsh 01_tcl_fundamentals.tcl
tclsh 02_eda_tool_integration.tcl

# Try TCL exercises
cd ../exercises  
tclsh exercise_1_tcl_basics.tcl
```

## Core Features That Work Immediately

- ✅ Python timing report parsing (no dependencies)
- ✅ Basic file I/O and text processing
- ✅ Regular expressions
- ✅ All TCL tutorials and exercises
- ✅ Sample timing reports analysis
- ⚠️ Advanced data analysis (requires pandas)
- ⚠️ Data visualization (requires matplotlib)

## Learning Path

1. **Start with Python basics**: `python_learning/basics/01_python_for_eda.py`
2. **Learn file parsing**: `python_learning/basics/02_file_parsing.py`
3. **Practice timing analysis**: `python_learning/timing_analysis/timing_compare.py`
4. **Master TCL fundamentals**: `tcl_learning/basics/01_tcl_fundamentals.tcl`
5. **Work through exercises**: Complete exercises in both directories

The core interview example (comparing timing reports) works perfectly without any additional dependencies!