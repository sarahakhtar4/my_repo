#!/usr/bin/env python3
"""
Physical Design Scripting Workshop - Python Test Runner
Automated testing framework for all Python exercises
"""

import sys
import os
import time
import traceback
import argparse
import importlib.util
from pathlib import Path
from typing import Dict, List, Any, Callable, Tuple

class TestRunner:
    def __init__(self):
        self.base_path = Path(__file__).parent
        self.exercises_path = self.base_path / "exercises"
        self.solutions_path = self.base_path / "solutions"
        self.results = {}
        
    def load_exercise(self, exercise_file: Path) -> Tuple[Any, Dict]:
        """Load an exercise module and extract its test configuration"""
        spec = importlib.util.spec_from_file_location("exercise", exercise_file)
        module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(module)
        
        # Extract test configuration
        test_config = getattr(module, 'TEST_CONFIG', {})
        return module, test_config
        
    def run_test_case(self, func: Callable, test_case: Dict) -> Dict:
        """Run a single test case and return results"""
        try:
            start_time = time.time()
            
            # Extract test parameters
            inputs = test_case.get('input', [])
            expected = test_case.get('expected')
            description = test_case.get('description', 'Test case')
            
            # Run the function
            if isinstance(inputs, list):
                result = func(*inputs)
            else:
                result = func(inputs)
                
            execution_time = time.time() - start_time
            
            # Compare results
            passed = self._compare_results(result, expected)
            
            return {
                'passed': passed,
                'result': result,
                'expected': expected,
                'time': execution_time,
                'description': description,
                'error': None
            }
            
        except Exception as e:
            return {
                'passed': False,
                'result': None,
                'expected': expected,
                'time': time.time() - start_time,
                'description': description,
                'error': str(e)
            }
    
    def _compare_results(self, result: Any, expected: Any) -> bool:
        """Compare results with tolerance for floating point numbers"""
        if isinstance(result, float) and isinstance(expected, float):
            return abs(result - expected) < 1e-6
        elif isinstance(result, list) and isinstance(expected, list):
            if len(result) != len(expected):
                return False
            return all(self._compare_results(r, e) for r, e in zip(result, expected))
        else:
            return result == expected
    
    def run_exercise_tests(self, exercise_path: Path) -> Dict:
        """Run all tests for a single exercise"""
        try:
            module, config = self.load_exercise(exercise_path)
            
            # Get the main function to test
            function_name = config.get('function_name', 'solve')
            if not hasattr(module, function_name):
                return {'error': f"Function '{function_name}' not found in exercise"}
            
            func = getattr(module, function_name)
            test_cases = config.get('test_cases', [])
            
            if not test_cases:
                return {'error': 'No test cases defined'}
            
            results = []
            for i, test_case in enumerate(test_cases):
                result = self.run_test_case(func, test_case)
                result['case_id'] = i + 1
                results.append(result)
            
            # Calculate summary
            passed_count = sum(1 for r in results if r['passed'])
            total_time = sum(r['time'] for r in results)
            
            return {
                'exercise_name': exercise_path.stem,
                'passed': passed_count,
                'total': len(results),
                'success_rate': passed_count / len(results) * 100,
                'total_time': total_time,
                'results': results,
                'error': None
            }
            
        except Exception as e:
            return {
                'exercise_name': exercise_path.stem,
                'error': f"Failed to load exercise: {str(e)}"
            }
    
    def find_exercises(self, category: str = None) -> List[Path]:
        """Find all exercise files, optionally filtered by category"""
        exercises = []
        
        if category:
            category_path = self.exercises_path / category
            if category_path.exists():
                exercises.extend(category_path.glob("*.py"))
        else:
            for category_dir in ['basic', 'intermediate', 'advanced']:
                category_path = self.exercises_path / category_dir
                if category_path.exists():
                    exercises.extend(category_path.glob("*.py"))
        
        return sorted(exercises)
    
    def run_all_tests(self, category: str = None, exercise_name: str = None) -> None:
        """Run tests for all exercises or specific ones"""
        exercises = self.find_exercises(category)
        
        if exercise_name:
            exercises = [e for e in exercises if e.stem == exercise_name]
            if not exercises:
                print(f"Exercise '{exercise_name}' not found!")
                return
        
        if not exercises:
            print("No exercises found!")
            return
        
        print("🚀 Physical Design Scripting Workshop - Python Test Runner")
        print("=" * 60)
        
        total_exercises = len(exercises)
        total_passed = 0
        total_tests = 0
        
        for exercise in exercises:
            print(f"\n📝 Testing: {exercise.relative_to(self.exercises_path)}")
            print("-" * 40)
            
            result = self.run_exercise_tests(exercise)
            
            if result.get('error'):
                print(f"❌ ERROR: {result['error']}")
                continue
            
            # Display results
            passed = result['passed']
            total = result['total']
            success_rate = result['success_rate']
            exec_time = result['total_time']
            
            print(f"✅ Passed: {passed}/{total} ({success_rate:.1f}%)")
            print(f"⏱️  Time: {exec_time:.3f}s")
            
            if passed == total:
                print("🎉 All tests passed!")
                total_passed += 1
            else:
                print("❌ Some tests failed:")
                for test_result in result['results']:
                    if not test_result['passed']:
                        case_id = test_result['case_id']
                        desc = test_result['description']
                        error = test_result.get('error')
                        if error:
                            print(f"   Case {case_id}: {desc} - ERROR: {error}")
                        else:
                            expected = test_result['expected']
                            actual = test_result['result']
                            print(f"   Case {case_id}: {desc}")
                            print(f"     Expected: {expected}")
                            print(f"     Got: {actual}")
            
            total_tests += total
        
        # Summary
        print("\n" + "=" * 60)
        print("📊 FINAL SUMMARY")
        print("=" * 60)
        print(f"Exercises passed: {total_passed}/{total_exercises}")
        print(f"Overall success rate: {(total_passed/total_exercises*100):.1f}%")
        
        if total_passed == total_exercises:
            print("🏆 Congratulations! All exercises completed successfully!")
        else:
            print("💪 Keep practicing! Review the failed exercises.")

def main():
    parser = argparse.ArgumentParser(description='Physical Design Python Workshop Test Runner')
    parser.add_argument('--exercise', help='Run specific exercise (e.g., basic_01)')
    parser.add_argument('--category', choices=['basic', 'intermediate', 'advanced'], 
                       help='Run exercises from specific category')
    parser.add_argument('--list', action='store_true', help='List all available exercises')
    
    args = parser.parse_args()
    
    runner = TestRunner()
    
    if args.list:
        exercises = runner.find_exercises()
        print("Available exercises:")
        for exercise in exercises:
            rel_path = exercise.relative_to(runner.exercises_path)
            print(f"  {rel_path}")
        return
    
    if args.exercise == 'all':
        runner.run_all_tests()
    elif args.exercise:
        runner.run_all_tests(exercise_name=args.exercise)
    elif args.category:
        runner.run_all_tests(category=args.category)
    else:
        runner.run_all_tests()

if __name__ == "__main__":
    main()