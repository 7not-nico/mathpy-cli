# Examples & Usage

## 🎮 Game Examples

### Sample Game Session
```
Welcome to Math Practice!
Solve for x in each equation. Type 'quit' to exit.

Problem: 3x + 8 = 104
What is x? 32
Correct! ✓

Problem: x = 35 - 19
What is x? 16
Correct! ✓

Problem: 17 + 10 = x
What is x? 27
Correct! ✓

Problem: x - 4 = 15
What is x? 19
Correct! ✓

Problem: 2x = 37 + 11
What is x? 24
Correct! ✓

quit
Thanks for playing!
Final Score: 5/5 correct (100.0% accuracy)
```

## 📝 Equation Pattern Examples

### 1. Standard Form
```
Problem: 3x + 8 = 104
Math: 3x + 8 = 104
Solution: 3x = 96 → x = 32
```

### 2. Isolated Left
```
Problem: x = 35 - 19
Math: x = 35 - 19
Solution: x = 16
```

### 3. Isolated Right
```
Problem: 17 + 10 = x
Math: 17 + 10 = x
Solution: x = 27
```

### 4. Simple Addition
```
Problem: x + 6 = 28
Math: x + 6 = 28
Solution: x = 22
```

### 5. Simple Subtraction
```
Problem: x - 4 = 15
Math: x - 4 = 15
Solution: x = 19
```

### 6. Coefficient Isolated
```
Problem: 2x = 37 + 11
Math: 2x = 48
Solution: x = 24
```

### 7. Fractional Form
```
Problem: x = (13 - 8) / 5
Math: x = 5 / 5
Solution: x = 1
```

### 8. Flipped Standard
```
Problem: 94 = 4x + 6
Math: 94 = 4x + 6
Solution: 4x = 88 → x = 22
```

### 9. Middle Term
```
Problem: 11 + 4x = 147
Math: 11 + 4x = 147
Solution: 4x = 136 → x = 34
```

### 10. Nested Operation
```
Problem: (2x - 5) = 15
Math: 2x - 5 = 15
Solution: 2x = 20 → x = 10
```

## 🔧 Configuration Examples

### Default Settings
```python
# Current configuration
X_MIN = 1      # Minimum x value
X_MAX = 40     # Maximum x value
A_MIN = 1      # Minimum coefficient
A_MAX = 5      # Maximum coefficient
B_MIN = -20    # Minimum constant
B_MAX = 20     # Maximum constant
```

### Easy Mode Example
```python
# Easier difficulty
X_MIN = 1
X_MAX = 20     # Smaller x range
A_MIN = 1
A_MAX = 3      # Simpler coefficients
B_MIN = -10
B_MAX = 10     # Smaller constants
```

### Hard Mode Example
```python
# Harder difficulty
X_MIN = 10
X_MAX = 100    # Larger x range
A_MIN = 2
A_MAX = 10     # Complex coefficients
B_MIN = -50
B_MAX = 50     # Larger constants
```

## 🧪 Testing Examples

### Basic Functionality Test
```bash
# Test problem generation
python -c "
from main import ProblemGenerator
gen = ProblemGenerator()
for i in range(5):
    problem, x = gen.generate()
    print(f'{problem} → x = {x}')
"
```

### Game Engine Test
```bash
# Test scoring system
python -c "
from main import GameEngine
engine = GameEngine()
engine.check_answer(5, 5)  # Correct
engine.check_answer(3, 7)  # Incorrect
correct, total, accuracy = engine.get_score()
print(f'Score: {correct}/{total} ({accuracy:.1f}%)')
"
```

### Full Integration Test
```bash
# Test all components together
python -c "
from main import ProblemGenerator, GameEngine, UserInterface, MathGame

# Create components
gen = ProblemGenerator()
engine = GameEngine()
ui = UserInterface()
game = MathGame(gen, engine, ui)

# This would run the full game (commented out for demo)
# game.run()
print('Components created successfully!')
print('Run python main.py to play the full game.')
"
```

## 📊 Performance Examples

### Generation Speed
```bash
# Test how fast problems are generated
python -c "
import time
from main import ProblemGenerator

gen = ProblemGenerator()
start = time.time()
for i in range(1000):
    problem, x = gen.generate()
end = time.time()
print(f'Generated 1000 problems in {end-start:.3f} seconds')
print(f'Average: {(end-start)/1000:.6f} seconds per problem')
"
```

### Memory Usage
```bash
# Check memory efficiency
python -c "
import sys
from main import ProblemGenerator, GameEngine, UserInterface, MathGame

# Create all components
gen = ProblemGenerator()
engine = GameEngine()
ui = UserInterface()
game = MathGame(gen, engine, ui)

# Check memory usage
size = sys.getsizeof(gen) + sys.getsizeof(engine) + sys.getsizeof(ui) + sys.getsizeof(game)
print(f'Memory usage: {size} bytes ({size/1024:.2f} KB)')
"
```

## 🔍 Debugging Examples

### Problem Validation
```python
# Verify mathematical correctness
def validate_problem(problem, x):
    # Parse and verify the equation equals the expected x
    # This would be a more complex parsing function
    return True  # Placeholder

# Test validation
problems = [
    ('3x + 8 = 104', 32),
    ('x = 35 - 19', 16),
    ('17 + 10 = x', 27)
]

for problem, expected_x in problems:
    is_valid = validate_problem(problem, expected_x)
    status = '✓' if is_valid else '✗'
    print(f'{status} {problem} → x = {expected_x}')
```

## 🎯 Educational Examples

### Learning Progression
```
Level 1 (Simple): x + 5 = 10
Level 2 (Rearranged): 5 + x = 10
Level 3 (Coefficients): 2x + 3 = 13
Level 4 (Complex): (3x - 2) = 16
Level 5 (Advanced): x = (8 - 3) / 2
```

### Skill Reinforcement
- **Basic operations:** Addition, subtraction
- **Variable isolation:** Moving terms across equals
- **Coefficients:** Multiplication/division with variables
- **Order of operations:** Parentheses and complex expressions
- **Fractional solutions:** Division in algebraic contexts

---

*These examples demonstrate the game's versatility and educational value across different algebraic concepts.*</content>
<parameter name="filePath">docs/examples.md