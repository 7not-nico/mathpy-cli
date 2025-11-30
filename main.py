import random

# Game configuration constants
X_MIN = 1
X_MAX = 40
A_MIN = 1
A_MAX = 5
B_MIN = -20
B_MAX = 20


class ProblemGenerator:
    """Single Responsibility: Generate random math problems with x in different positions among multiple variables"""

    def generate(self):
        """Generate a random solution and create a problem with x in various positions"""
        # Choose problem type: equation or assignment
        problem_types = ["equation", "assignment"]
        problem_type = random.choice(problem_types)

        if problem_type == "equation":
            # Generate linear equation
            problem, x_value = self._generate_equation()
        else:
            # Generate assignment
            problem, x_value = self._generate_assignment()

        return problem, x_value, {}

    def _generate_equation(self):
        """Generate a linear equation with x among multiple variables"""
        # Choose equation pattern
        patterns = [
            "simple_linear",  # var1 + x = var2
            "coeff_linear",  # coeff*x + var = target
            "multiple_terms",  # var1 + var2 + x = var3
            "isolated_x",  # x = var1 + var2
            "coeff_isolated",  # coeff*x = var1 + var2
        ]
        pattern = random.choice(patterns)

        x = random.randint(X_MIN, X_MAX)  # The solution

        if pattern == "simple_linear":
            # val1 + x = val2 or x + val1 = val2
            val1 = random.randint(X_MIN, X_MAX)
            x = random.randint(X_MIN, X_MAX)
            position = random.choice(["left", "right"])
            if position == "left":
                val2 = val1 + x
                problem = f"{val1} + x = {val2}"
            else:
                val2 = x + val1
                problem = f"x + {val1} = {val2}"

        elif pattern == "coeff_linear":
            # coeff*x + val1 = val2
            coeff = random.randint(A_MIN, A_MAX)
            val1 = random.randint(X_MIN, X_MAX)
            x = random.randint(X_MIN, X_MAX)
            val2 = coeff * x + val1
            problem = f"{coeff}x + {val1} = {val2}"

        elif pattern == "multiple_terms":
            # val1 + val2 + x = val3
            val1 = random.randint(X_MIN, X_MAX)
            val2 = random.randint(X_MIN, X_MAX)
            x = random.randint(X_MIN, X_MAX)
            val3 = val1 + val2 + x
            problem = f"{val1} + {val2} + x = {val3}"

        elif pattern == "isolated_x":
            # x = val1 + val2
            val1 = random.randint(X_MIN, X_MAX)
            val2 = random.randint(X_MIN, X_MAX)
            x = val1 + val2
            problem = f"x = {val1} + {val2}"

        else:  # coeff_isolated
            # coeff*x = val1 + val2
            coeff = random.randint(A_MIN, A_MAX)
            val1 = random.randint(X_MIN, X_MAX)
            val2 = random.randint(X_MIN, X_MAX)
            x = (val1 + val2) // coeff
            problem = f"{coeff}x = {val1} + {val2}"

        return problem, x

    def _generate_assignment(self):
        """Generate tuple assignment with x"""
        # Like: val1 + x, val2 = val3, val2  meaning val1 + x = val3, val2 = val2 (always true)

        val1 = random.randint(X_MIN, X_MAX)
        val2 = random.randint(X_MIN, X_MAX)
        x = random.randint(X_MIN, X_MAX)
        val3 = val1 + x

        problem = f"{val1} + x = {val3} and {val2} = {val2}"

        return problem, x


class GameEngine:
    """Single Responsibility: Handle game logic and state"""

    def __init__(self):
        self.correct_answers = 0
        self.total_questions = 0

    def check_answer(self, user_answer, correct_answer):
        """Check if user's answer is correct"""
        self.total_questions += 1
        if user_answer == correct_answer:
            self.correct_answers += 1
            return True
        return False

    def get_score(self):
        """Get current score statistics"""
        if self.total_questions == 0:
            return 0, 0, 0.0
        accuracy = (self.correct_answers / self.total_questions) * 100
        return self.correct_answers, self.total_questions, accuracy

    def should_quit(self, user_input):
        """Check if user wants to quit"""
        return user_input.lower() == "quit"


class UserInterface:
    """Single Responsibility: Handle all user input/output"""

    def display_welcome(self):
        """Display welcome message"""
        print("Welcome to Math Practice!")
        print("Solve for x in each equation. Type 'quit' to exit.\n")

    def display_problem(self, problem, known_vars=None):
        """Display the math problem"""
        if known_vars:
            # Substitute known values into the problem
            substituted = problem
            for var, value in known_vars.items():
                substituted = substituted.replace(var, str(value))
            print(f"Problem: {substituted}")
        else:
            print(f"Problem: {problem}")

    def get_user_input(self):
        """Get input from user"""
        return input("What is x? ").strip()

    def display_correct(self):
        """Display correct answer message"""
        print("Correct! ✓\n")

    def display_incorrect(self, correct_answer):
        """Display incorrect answer message"""
        print(f"Not quite. x = {correct_answer}\n")

    def display_invalid_input(self):
        """Display invalid input message"""
        print("Please enter a number or 'quit'\n")

    def display_goodbye(self):
        """Display goodbye message"""
        print("Thanks for playing!")

    def display_final_score(self, correct, total, accuracy):
        """Display final score"""
        print(f"\nFinal Score: {correct}/{total} correct ({accuracy:.1f}% accuracy)")


class MathGame:
    """Single Responsibility: Orchestrate the game components"""

    def __init__(self, problem_generator, game_engine, user_interface):
        self.problem_generator = problem_generator
        self.game_engine = game_engine
        self.user_interface = user_interface

    def run(self):
        """Run the main game loop"""
        self.user_interface.display_welcome()

        while True:
            # Generate and display problem
            problem, solution, known_vars = self.problem_generator.generate()
            self.user_interface.display_problem(problem, known_vars)

            # Get user input
            user_input = self.user_interface.get_user_input()

            # Check if user wants to quit
            if self.game_engine.should_quit(user_input):
                break

            # Process answer
            try:
                user_answer = int(user_input)
                if self.game_engine.check_answer(user_answer, solution):
                    self.user_interface.display_correct()
                else:
                    self.user_interface.display_incorrect(solution)
            except ValueError:
                self.user_interface.display_invalid_input()

        # Display final score
        correct, total, accuracy = self.game_engine.get_score()
        self.user_interface.display_final_score(correct, total, accuracy)
        self.user_interface.display_goodbye()


def main():
    """Create game components and start the game"""
    problem_generator = ProblemGenerator()
    game_engine = GameEngine()
    user_interface = UserInterface()

    game = MathGame(problem_generator, game_engine, user_interface)
    game.run()


if __name__ == "__main__":
    main()
