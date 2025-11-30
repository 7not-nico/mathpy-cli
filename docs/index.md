# API Reference

## 📚 Class Interfaces

This document describes the public APIs of all classes in the Math Practice Game.

## ProblemGenerator

**Purpose:** Generate random math problems with varied x positions

### Constructor
```python
ProblemGenerator()
```
No parameters required. Uses global configuration constants.

### Methods

#### `generate() -> tuple[str, int]`
Generate a random math problem and its solution.

**Returns:**
- `problem` (str): The equation string (e.g., "3x + 8 = 104")
- `solution` (int): The correct value for x

**Example:**
```python
generator = ProblemGenerator()
problem, x = generator.generate()
print(f"{problem} → x = {x}")
# Output: "3x + 8 = 104 → x = 32"
```

## GameEngine

**Purpose:** Handle game logic and performance tracking

### Constructor
```python
GameEngine()
```
Initializes scoring counters to zero.

### Methods

#### `check_answer(user_answer: int, correct_answer: int) -> bool`
Validate user's answer and update score.

**Parameters:**
- `user_answer` (int): The user's submitted answer
- `correct_answer` (int): The correct solution

**Returns:**
- `bool`: True if answer is correct, False otherwise

**Side Effects:**
- Increments total_questions counter
- Increments correct_answers counter if correct

**Example:**
```python
engine = GameEngine()
is_correct = engine.check_answer(32, 32)  # True
is_correct = engine.check_answer(25, 32)  # False
```

#### `get_score() -> tuple[int, int, float]`
Get current performance statistics.

**Returns:**
- `correct` (int): Number of correct answers
- `total` (int): Total questions answered
- `accuracy` (float): Percentage accuracy (0.0 to 100.0)

**Example:**
```python
correct, total, accuracy = engine.get_score()
print(f"Score: {correct}/{total} ({accuracy:.1f}%)")
# Output: "Score: 1/2 (50.0%)"
```

#### `should_quit(user_input: str) -> bool`
Check if user wants to exit the game.

**Parameters:**
- `user_input` (str): The user's input string

**Returns:**
- `bool`: True if input is "quit" (case-insensitive), False otherwise

**Example:**
```python
quit_game = engine.should_quit("quit")      # True
quit_game = engine.should_quit("QUIT")      # True
quit_game = engine.should_quit("32")        # False
```

## UserInterface

**Purpose:** Handle all user input and output operations

### Constructor
```python
UserInterface()
```
No parameters required.

### Methods

#### `display_welcome() -> None`
Display the game welcome message and instructions.

**Example:**
```python
ui.display_welcome()
# Output:
# Welcome to Math Practice!
# Solve for x in each equation. Type 'quit' to exit.
```

#### `display_problem(problem: str) -> None`
Display a math problem to the user.

**Parameters:**
- `problem` (str): The equation string to display

**Example:**
```python
ui.display_problem("3x + 8 = 104")
# Output: "Problem: 3x + 8 = 104"
```

#### `get_user_input() -> str`
Get input from the user with a prompt.

**Returns:**
- `str`: The user's input (stripped of whitespace)

**Example:**
```python
user_input = ui.get_user_input()
# Displays: "What is x? "
# Returns: user's typed response
```

#### `display_correct() -> None`
Display correct answer feedback.

**Example:**
```python
ui.display_correct()
# Output: "Correct! ✓"
```

#### `display_incorrect(correct_answer: int) -> None`
Display incorrect answer feedback with the correct solution.

**Parameters:**
- `correct_answer` (int): The correct value for x

**Example:**
```python
ui.display_incorrect(32)
# Output: "Not quite. x = 32"
```

#### `display_invalid_input() -> None`
Display invalid input error message.

**Example:**
```python
ui.display_invalid_input()
# Output: "Please enter a number or 'quit'"
```

#### `display_goodbye() -> None`
Display game exit message.

**Example:**
```python
ui.display_goodbye()
# Output: "Thanks for playing!"
```

#### `display_final_score(correct: int, total: int, accuracy: float) -> None`
Display final game statistics.

**Parameters:**
- `correct` (int): Number of correct answers
- `total` (int): Total questions answered
- `accuracy` (float): Percentage accuracy

**Example:**
```python
ui.display_final_score(4, 5, 80.0)
# Output: "\nFinal Score: 4/5 correct (80.0% accuracy)"
```

## MathGame

**Purpose:** Orchestrate all game components and manage the main game loop

### Constructor
```python
MathGame(problem_generator: ProblemGenerator,
         game_engine: GameEngine,
         user_interface: UserInterface)
```

**Parameters:**
- `problem_generator`: Instance of ProblemGenerator
- `game_engine`: Instance of GameEngine
- `user_interface`: Instance of UserInterface

**Pattern:** Dependency injection - components are provided rather than created internally.

### Methods

#### `run() -> None`
Execute the main game loop until user quits.

**Game Flow:**
1. Display welcome message
2. Loop:
   - Generate problem
   - Display problem
   - Get user input
   - Check for quit command
   - Validate answer
   - Display feedback
3. Display final score
4. Display goodbye message

**Example:**
```python
game = MathGame(generator, engine, ui)
game.run()  # Starts interactive game
```

## Configuration Constants

### Game Parameters
```python
X_MIN = 1      # Minimum value for x
X_MAX = 40     # Maximum value for x
A_MIN = 1      # Minimum coefficient value
A_MAX = 5      # Maximum coefficient value
B_MIN = -20    # Minimum constant term
B_MAX = 20     # Maximum constant term
```

### Usage
These constants control problem generation difficulty and can be modified to adjust game parameters.

## Error Handling

### Input Validation
- **Non-numeric input:** Caught by `try/except` in MathGame.run()
- **Invalid commands:** Only "quit" is recognized as exit command
- **Empty input:** Handled by string stripping

### Mathematical Guarantees
- **Correctness:** All equations are mathematically correct by construction
- **Integer solutions:** All parameters chosen to ensure integer results
- **Range compliance:** x always falls within X_MIN to X_MAX

## Testing Interfaces

### Mock Components
For testing, components can be replaced with mock implementations:

```python
class MockProblemGenerator:
    def generate(self):
        return ("2x + 4 = 10", 3)

class MockUserInterface:
    def display_welcome(self): pass
    def display_problem(self, problem): pass
    def get_user_input(self): return "3"
    def display_correct(self): pass
    def display_incorrect(self, answer): pass
    def display_invalid_input(self): pass
    def display_goodbye(self): pass
    def display_final_score(self, c, t, a): pass
```

### Component Isolation
Each class can be tested independently due to SRP and dependency injection.

---

*This API reference provides the complete interface for extending or testing the Math Practice Game components.*</content>
<parameter name="filePath">docs/api.md