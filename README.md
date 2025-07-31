# Physical Design Scripting Workshop

## Overview
This workshop provides comprehensive Python and TCL scripting exercises designed for physical design interviews. Each exercise includes built-in testing functions to validate your solutions.

## Workshop Structure
```
workshop/
├── python/
│   ├── exercises/
│   │   ├── basic/          # Fundamental programming concepts
│   │   ├── intermediate/   # Data structures & algorithms
│   │   └── advanced/       # Complex physical design problems
│   ├── solutions/          # Reference solutions
│   └── test_runner.py      # Automated testing framework
├── tcl/
│   ├── exercises/
│   │   ├── basic/          # TCL fundamentals
│   │   ├── intermediate/   # EDA tool scripting
│   │   └── advanced/       # Complex automation scripts
│   ├── solutions/          # Reference solutions
│   └── test_runner.tcl     # Automated testing framework
└── data/                   # Sample data files for exercises
```

## Getting Started

### Python Exercises
```bash
cd python
python test_runner.py --help
python test_runner.py --exercise all
python test_runner.py --exercise basic_01
```

### TCL Exercises
```bash
cd tcl
tclsh test_runner.tcl
```

## Exercise Categories

### Python Exercises (25 exercises)
1. **Basic (8 exercises)**: Data types, loops, functions, file I/O
2. **Intermediate (10 exercises)**: Data structures, algorithms, parsing
3. **Advanced (7 exercises)**: Complex physical design problems

### TCL Exercises (20 exercises)
1. **Basic (6 exercises)**: TCL syntax, variables, procedures
2. **Intermediate (8 exercises)**: EDA tool commands, data processing
3. **Advanced (6 exercises)**: Complex automation and optimization

## Key Topics Covered
- Liberty file parsing
- LEF/DEF file processing
- Timing analysis
- Placement optimization
- Clock tree synthesis
- Power analysis
- Design rule checking
- Constraint handling
- Report generation
- Data visualization

## Testing Framework
Each exercise includes:
- Clear problem statement
- Sample input/output
- Automated test cases
- Performance benchmarks
- Solution validation

## Interview Preparation Tips
1. Practice time management (15-30 minutes per exercise)
2. Focus on code clarity and efficiency
3. Handle edge cases properly
4. Write testable, modular code
5. Understand physical design concepts

Happy coding!