# Math Practice Game

A Python CLI math practice game that helps users improve their algebra skills by solving for `x` in equations with maximum variety in `x` positioning.

## 🎯 Project Overview

This project implements an intelligent math practice game focused on algebraic equation solving. The core innovation is the "x shuffling" algorithm that places the unknown variable `x` in diverse algebraic positions across different equation types.

## 🏗️ Architecture

The project follows **Single Responsibility Principle (SRP)** with a clean, modular architecture:

### Core Classes

#### `ProblemGenerator`
- **Responsibility:** Generate random math problems with `x` in varied positions
- **Key Method:** `generate()` → Returns `(problem_string, solution)`
- **Algorithm:** Uses 10 different equation patterns for maximum `x` variety

#### `GameEngine`
- **Responsibility:** Handle game logic and performance tracking
- **Key Methods:**
  - `check_answer()` → Validate user responses
  - `get_score()` → Calculate performance metrics
  - `should_quit()` → Handle exit conditions

#### `UserInterface`
- **Responsibility:** Manage all user input/output operations
- **Key Methods:** `display_*()` and `get_user_input()` for clean I/O separation

#### `MathGame`
- **Responsibility:** Orchestrate game components and manage game loop
- **Pattern:** Uses dependency injection for clean component wiring

## 🔄 X Shuffling Algorithm

The core innovation places `x` in **10 different algebraic positions**:

### Equation Types
1. **Standard:** `ax ± b = c` (coefficient with x)
2. **Isolated Left:** `x = c ± b` (x alone on left)
3. **Isolated Right:** `c ± b = x` (x alone on right)
4. **Simple Add:** `x ± b = c` (x plus/minus constant)
5. **Simple Subtract:** `x ± b = c` (x minus constant)
6. **Coefficient Isolated:** `ax = c ± b` (coefficient isolated)
7. **Fractional:** `x = (c ± b) / a` (division form)
8. **Flipped Standard:** `c = ax ± b` (equation reversed)
9. **Middle Term:** `b ± ax = c` (x in expression middle)
10. **Nested Operation:** `(ax ± b) = c` (parenthesized expression)

### Algorithm Flow
1. Generate random `x` (1-40)
2. Randomly select equation type
3. Generate appropriate `a` and `b` coefficients
4. Calculate answer: `answer = a*x ± b`
5. Format equation string with clean notation
6. Return `(equation_string, x_solution)`

## 🎮 Game Features

- **Varied Difficulty:** 10 equation patterns prevent repetition
- **Clean Interface:** Simple CLI with clear prompts
- **Score Tracking:** Basic performance metrics
- **Graceful Exit:** Type 'quit' to exit anytime
- **Error Handling:** Validates user input

## 🛠️ Development Approach

### Principles
- **Single Responsibility Principle:** Each class has one reason to change
- **No Magic Numbers:** All configurable values are named constants
- **Incremental Development:** Build core first, enhance gradually
- **Clean Architecture:** Separation of concerns throughout

### Current Status
- ✅ Core game functionality implemented
- ✅ SRP-compliant architecture
- ✅ X shuffling algorithm with 10 patterns
- ✅ No magic numbers
- ✅ Clean, maintainable code
- ✅ Working CLI interface

### Configuration Constants
```python
X_MIN = 1      # Minimum x value
X_MAX = 40     # Maximum x value
A_MIN = 1      # Minimum coefficient
A_MAX = 5      # Maximum coefficient
B_MIN = -20    # Minimum constant term
B_MAX = 20     # Maximum constant term
```

## 🚀 Running the Game

```bash
python main.py
```

### Sample Session
```
Welcome to Math Practice!
Solve for x in each equation. Type 'quit' to exit.

Problem: 3x + 8 = 104
What is x? 32
Correct! ✓

Problem: x = 35 - 19
What is x? 16
Correct! ✓
```

## 📚 Documentation

Detailed documentation available in `/docs/` folder:
- [Development Guide](docs/development.md) - How we built this project
- [Algorithm Details](docs/algorithm.md) - Deep dive into x shuffling
- [Architecture](docs/architecture.md) - SRP implementation details

## 🔮 Future Enhancements

Planned gradual improvements (with user guidance):
- Quality control for problem generation
- Educational progression system
- Smart distribution algorithms
- Learning analytics integration
- Performance optimization

## 📋 Development Notes

- **Language:** Python 3.x
- **Dependencies:** Standard library only (random, sys)
- **Architecture:** Object-oriented with dependency injection
- **Testing:** Manual testing with sample runs
- **Code Style:** Clean, readable, well-documented

---

*Built incrementally with focus on core functionality and clean architecture.*