import random

# Game configuration constants
X_MIN = 1
X_MAX = 40
A_MIN = 1
A_MAX = 5
B_MIN = -20
B_MAX = 20


class ProblemGenerator:
    """Single Responsibility: Generate random math problems with x in different positions"""

    def generate(self):
        """Generate a random solution and create a linear equation problem with maximum x position variety"""
        x = random.randint(X_MIN, X_MAX)  # This is the solution we're looking for

        # Randomly choose equation format - maximum variety!
        equation_types = [
            "standard",
            "isolated_left",
            "isolated_right",
            "simple_add",
            "simple_subtract",
            "coefficient_isolated",
            "fractional",
            "flipped_standard",
            "middle_term",
            "nested_operation",
        ]
        equation_type = random.choice(equation_types)

        if equation_type == "standard":
            # ax + b = c or ax - b = c
            a = random.randint(A_MIN, A_MAX)
            b = random.randint(B_MIN, B_MAX)
            answer = a * x + b

            if b >= 0:
                problem = f"{a}x + {b} = {answer}"
            else:
                problem = f"{a}x - {abs(b)} = {answer}"

        elif equation_type == "isolated_left":
            # x = c ± b
            b = random.randint(B_MIN, B_MAX)
            operation = random.choice(["+", "-"])
            if operation == "+":
                answer = x + b
                if b >= 0:
                    problem = f"x = {answer} - {b}"
                else:
                    problem = f"x = {answer} + {abs(b)}"
            else:
                answer = x - b
                if b >= 0:
                    problem = f"x = {answer} + {b}"
                else:
                    problem = f"x = {answer} - {abs(b)}"

        elif equation_type == "isolated_right":
            # c ± b = x
            b = random.randint(B_MIN, B_MAX)
            operation = random.choice(["+", "-"])
            if operation == "+":
                left_side = x + b
                if b >= 0:
                    problem = f"{left_side} - {b} = x"
                else:
                    problem = f"{left_side} + {abs(b)} = x"
            else:
                left_side = x - b
                if b >= 0:
                    problem = f"{left_side} + {b} = x"
                else:
                    problem = f"{left_side} - {abs(b)} = x"

        elif equation_type == "simple_add":
            # x + b = c
            b = random.randint(B_MIN, B_MAX)
            answer = x + b
            if b >= 0:
                problem = f"x + {b} = {answer}"
            else:
                problem = f"x - {abs(b)} = {answer}"

        elif equation_type == "simple_subtract":
            # x - b = c
            b = random.randint(B_MIN, B_MAX)
            answer = x - b
            if b >= 0:
                problem = f"x - {b} = {answer}"
            else:
                problem = f"x + {abs(b)} = {answer}"

        elif equation_type == "coefficient_isolated":
            # ax = c ± b (x with coefficient isolated)
            a = random.randint(A_MIN, A_MAX)
            b = random.randint(B_MIN, B_MAX)
            operation = random.choice(["+", "-"])
            if operation == "+":
                right_side = a * x + b
                if b >= 0:
                    problem = f"{a}x = {right_side} - {b}"
                else:
                    problem = f"{a}x = {right_side} + {abs(b)}"
            else:
                right_side = a * x - b
                if b >= 0:
                    problem = f"{a}x = {right_side} + {b}"
                else:
                    problem = f"{a}x = {right_side} - {abs(b)}"

        elif equation_type == "fractional":
            # x = (c ± b) / a (fractional form)
            a = random.randint(A_MIN, A_MAX)
            b = random.randint(B_MIN, B_MAX)
            operation = random.choice(["+", "-"])
            if operation == "+":
                numerator = a * x + b
                if b >= 0:
                    problem = f"x = ({numerator} - {b}) / {a}"
                else:
                    problem = f"x = ({numerator} + {abs(b)}) / {a}"
            else:
                numerator = a * x - b
                if b >= 0:
                    problem = f"x = ({numerator} + {b}) / {a}"
                else:
                    problem = f"x = ({numerator} - {abs(b)}) / {a}"

        elif equation_type == "flipped_standard":
            # c = ax ± b (equation flipped)
            a = random.randint(A_MIN, A_MAX)
            b = random.randint(B_MIN, B_MAX)
            left_side = a * x + b
            if b >= 0:
                problem = f"{left_side} = {a}x + {b}"
            else:
                problem = f"{left_side} = {a}x - {abs(b)}"

        elif equation_type == "middle_term":
            # b ± ax = c (x in middle)
            a = random.randint(A_MIN, A_MAX)
            b = random.randint(B_MIN, B_MAX)
            operation = random.choice(["+", "-"])
            if operation == "+":
                answer = b + a * x
                problem = f"{b} + {a}x = {answer}"
            else:
                answer = b - a * x
                problem = f"{b} - {a}x = {answer}"

        else:  # nested_operation
            # (ax ± b) = c or c = (ax ± b)
            a = random.randint(A_MIN, A_MAX)
            b = random.randint(B_MIN, B_MAX)
            operation = random.choice(["+", "-"])
            if operation == "+":
                left_expr = a * x + b
                problem = (
                    f"({a}x + {b}) = {left_expr}"
                    if b >= 0
                    else f"({a}x - {abs(b)}) = {left_expr}"
                )
            else:
                left_expr = a * x - b
                problem = (
                    f"({a}x - {b}) = {left_expr}"
                    if b >= 0
                    else f"({a}x + {abs(b)}) = {left_expr}"
                )

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

    def display_problem(self, problem):
        """Display the math problem"""
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
            problem, solution = self.problem_generator.generate()
            self.user_interface.display_problem(problem)

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
