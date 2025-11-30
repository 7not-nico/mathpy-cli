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
        """Generate a random solution and create a problem with multiple variables and x shuffled around"""
        # Choose number of variables: 2 to 5
        n_vars = random.randint(2, 5)
        var_names = ["a", "b", "c", "d", "e"][:n_vars]

        # Choose which variable is x (the unknown)
        x_index = random.randint(0, n_vars - 1)
        x_name = var_names[x_index]

        # Assign values to known variables
        var_values = {}
        for i, name in enumerate(var_names):
            if i == x_index:
                var_values[name] = None  # x is unknown
            else:
                var_values[name] = random.randint(X_MIN, X_MAX)

        # Choose problem type: equation or assignment
        problem_types = ["equation", "assignment"]
        problem_type = random.choice(problem_types)

        if problem_type == "equation":
            # Generate linear equation with multiple variables
            problem, x_value = self._generate_equation(var_names, x_name, var_values)
        else:
            # Generate assignment with multiple variables
            problem, x_value = self._generate_assignment(var_names, x_name, var_values)

        # Prepare known variables for display
        known_vars = {name: val for name, val in var_values.items() if val is not None}

        return problem, x_value, known_vars

    def _generate_equation(self, var_names, x_name, var_values):
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
            # var1 + x = var2 or x + var1 = var2
            other_vars = [v for v in var_names if v != x_name]
            var1 = random.choice(other_vars)
            var2 = random.choice([v for v in other_vars if v != var1] or [var1])

            x = var_values[var2] - var_values[var1]

            position = random.choice(["left", "right"])
            if position == "left":
                problem = f"{var1} + x = {var2}"
            else:
                problem = f"x + {var1} = {var2}"

        elif pattern == "coeff_linear":
            # coeff*x + var1 = var2
            coeff = random.randint(A_MIN, A_MAX)
            other_vars = [v for v in var_names if v != x_name]
            var1 = random.choice(other_vars)
            var2 = random.choice(other_vars)
            x = (var_values[var2] - var_values[var1]) // coeff  # Ensure integer
            problem = f"{coeff}x + {var1} = {var2}"

        elif pattern == "multiple_terms":
            # var1 + var2 + x = var3
            other_vars = [v for v in var_names if v != x_name]
            if len(other_vars) >= 3:
                var1, var2, var3 = random.sample(other_vars, 3)
            else:
                var1 = random.choice(other_vars)
                var2 = random.choice(other_vars)
                var3 = random.choice(other_vars)
            x = var_values[var3] - var_values[var1] - var_values[var2]
            problem = f"{var1} + {var2} + x = {var3}"

        elif pattern == "isolated_x":
            # x = var1 + var2
            other_vars = [v for v in var_names if v != x_name]
            if len(other_vars) >= 2:
                var1, var2 = random.sample(other_vars, 2)
            else:
                var1 = var2 = random.choice(other_vars)
            x = var_values[var1] + var_values[var2]
            problem = f"x = {var1} + {var2}"

        else:  # coeff_isolated
            # coeff*x = var1 + var2
            coeff = random.randint(A_MIN, A_MAX)
            other_vars = [v for v in var_names if v != x_name]
            if len(other_vars) >= 2:
                var1, var2 = random.sample(other_vars, 2)
            else:
                var1 = var2 = random.choice(other_vars)
            x = (var_values[var1] + var_values[var2]) // coeff
            problem = f"{coeff}x = {var1} + {var2}"

        return problem, x

    def _generate_assignment(self, var_names, x_name, var_values):
        """Generate tuple assignment with x among multiple variables"""
        # Like: var1 + x, var2 = var3, var4  meaning var1 + x = var3, var2 = var4

        other_vars = [v for v in var_names if v != x_name]

        # Choose variables
        var1 = random.choice(other_vars)
        var2 = random.choice(other_vars)
        var3 = random.choice(other_vars)
        # Choose var4 such that var_values[var4] == var_values[var2] for consistency
        possible_var4 = [v for v in other_vars if var_values[v] == var_values[var2]]
        if possible_var4:
            var4 = random.choice(possible_var4)
        else:
            var4 = var2  # fallback

        # For var1 + x = var3, x = var_values[var3] - var_values[var1]
        x = var_values[var3] - var_values[var1]
        left_exprs = [f"{var1} + x", var2]
        right_exprs = [var3, var4]

        # Format as equations: expr1 = expr2, expr3 = expr4
        eq1 = f"{left_exprs[0]} = {right_exprs[0]}"
        eq2 = f"{left_exprs[1]} = {right_exprs[1]}"
        problem = f"{eq1}, {eq2}"

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
            vars_str = ", ".join(f"{k}={v}" for k, v in known_vars.items())
            print(f"Given {vars_str}: {problem}")
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
