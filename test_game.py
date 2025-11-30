#!/usr/bin/env python3
"""
Test script for the math game.
Runs the game with simulated user inputs and checks for correct behavior.
"""

import sys
from io import StringIO
from unittest.mock import patch
from main import MathGame, ProblemGenerator, GameEngine, UserInterface


def test_game_session():
    """Test a full game session with some answers."""
    # Capture stdout
    captured_output = StringIO()

    # Simulated user inputs: some answers and quit
    user_inputs = ["5", "10", "15", "quit"]

    with patch("sys.stdout", captured_output), patch(
        "builtins.input", side_effect=user_inputs
    ):
        # Create game components
        problem_generator = ProblemGenerator()
        game_engine = GameEngine()
        user_interface = UserInterface()

        game = MathGame(problem_generator, game_engine, user_interface)
        game.run()

    output = captured_output.getvalue()

    # Check for expected outputs
    assert "Welcome to Math Practice!" in output
    assert "Solve for x in each equation. Type 'quit' to exit." in output
    assert "Thanks for playing!" in output
    assert "Final Score:" in output

    print("✓ Game session test passed")


def test_incorrect_answer():
    """Test handling of incorrect answers."""
    captured_output = StringIO()

    # Simulated inputs: wrong answer, then quit
    user_inputs = ["0", "quit"]

    with patch("sys.stdout", captured_output), patch(
        "builtins.input", side_effect=user_inputs
    ):
        problem_generator = ProblemGenerator()
        game_engine = GameEngine()
        user_interface = UserInterface()

        game = MathGame(problem_generator, game_engine, user_interface)
        game.run()

    output = captured_output.getvalue()

    assert "Not quite." in output
    assert "Final Score:" in output

    print("✓ Incorrect answer handling test passed")


def test_invalid_input():
    """Test handling of invalid inputs."""
    captured_output = StringIO()

    # Invalid input, then quit
    user_inputs = ["abc", "quit"]

    with patch("sys.stdout", captured_output), patch(
        "builtins.input", side_effect=user_inputs
    ):
        problem_generator = ProblemGenerator()
        game_engine = GameEngine()
        user_interface = UserInterface()

        game = MathGame(problem_generator, game_engine, user_interface)
        game.run()

    output = captured_output.getvalue()

    assert "Please enter a number or 'quit'" in output

    print("✓ Invalid input handling test passed")


def test_quit_immediately():
    """Test quitting immediately."""
    captured_output = StringIO()

    user_inputs = ["quit"]

    with patch("sys.stdout", captured_output), patch(
        "builtins.input", side_effect=user_inputs
    ):
        problem_generator = ProblemGenerator()
        game_engine = GameEngine()
        user_interface = UserInterface()

        game = MathGame(problem_generator, game_engine, user_interface)
        game.run()

    output = captured_output.getvalue()

    assert "Thanks for playing!" in output
    assert "Final Score: 0/0 correct" in output

    print("✓ Quit immediately test passed")


def test_problem_generation():
    """Test that problems are generated correctly."""
    gen = ProblemGenerator()

    for _ in range(10):
        problem, x, known = gen.generate()
        assert isinstance(problem, str)
        assert isinstance(x, int)
        assert isinstance(known, dict)
        assert "x" in problem  # x should be in the problem
        assert "=" in problem  # Should be an equation

    print("✓ Problem generation test passed")


if __name__ == "__main__":
    print("Running math game tests...")

    test_game_session()
    test_incorrect_answer()
    test_invalid_input()
    test_quit_immediately()
    test_problem_generation()

    print("\n🎉 All tests passed! The math game is working correctly.")
