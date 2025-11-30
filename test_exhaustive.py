#!/usr/bin/env python3
"""
Exhaustive test for the math game problem generator.
Tests all patterns, variable counts, and verifies solutions.
"""

import random
from main import ProblemGenerator
from sympy import symbols, solve, Eq, sympify
import sympy as sp


def solve_equation(problem_str):
    """
    Use sympy to solve the linear equation for x.
    """
    import re

    x = symbols("x")
    try:
        # Parse the equation
        # For assignments like "38 + x = 8 and 8 = 8", take first part
        if " and " in problem_str:
            problem_str = problem_str.split(" and ")[0]

        # Insert * between number and x, like 2x -> 2*x
        problem_str = re.sub(r"(\d)(x)", r"\1*x", problem_str)

        # Replace = with - ( ) to make it = 0
        left, right = problem_str.split("=", 1)
        equation_str = left + " - (" + right + ")"

        # Parse the expression
        eq_expr = sympify(equation_str)
        solutions = solve(Eq(eq_expr, 0), x)
        if solutions:
            sol = solutions[0]
            # Check if integer
            if sol.is_integer:
                return int(sol)
            else:
                return float(sol)
        else:
            return None
    except Exception as e:
        print(f"Error solving {problem_str}: {e}")
        return None
    except Exception as e:
        print(f"Error solving {problem_str}: {e}")
        return None
    except Exception as e:
        print(f"Error solving {problem_str}: {e}")
        return None


def test_exhaustive():
    """Run exhaustive tests on problem generation."""
    gen = ProblemGenerator()
    test_count = 1000  # Test many generations

    passed = 0
    failed = 0

    for i in range(test_count):
        problem = ""
        x_correct = None
        substituted = ""
        try:
            problem, x_correct, known_vars = gen.generate()

            # Substitute the problem
            substituted = problem
            for var, value in known_vars.items():
                substituted = substituted.replace(var, str(value))

            # Solve the substituted problem
            x_computed = solve_equation(substituted)

            if x_computed is not None and x_computed == x_correct:
                passed += 1
            else:
                failed += 1
                print(
                    f"FAIL: {substituted} | Expected x={x_correct}, Got x={x_computed}"
                )

        except Exception as e:
            failed += 1
            print(f"ERROR in test {i}: {e} | Problem: {substituted}, x={x_correct}")

    print(f"\nTest Results: {passed} passed, {failed} failed out of {test_count}")

    # Test edge cases
    print("\nTesting edge cases...")

    # Test with specific seeds for reproducibility
    test_cases = [
        (42, "Test seed 42"),
        (123, "Test seed 123"),
        (999, "Test seed 999"),
    ]

    for seed, desc in test_cases:
        random.seed(seed)
        problem, x_correct, known_vars = gen.generate()
        x_computed = solve_equation(problem)
        if x_computed == x_correct:
            print(f"PASS {desc}: {problem} -> x={x_correct}")
        else:
            print(f"FAIL {desc}: {problem} -> Expected {x_correct}, Got {x_computed}")


if __name__ == "__main__":
    test_exhaustive()
