# Frequently Asked Questions

## 🎯 Project Overview

### What is this project?
A Python CLI math practice game that helps users improve algebra skills by solving equations with the unknown variable `x` placed in diverse algebraic positions.

### Why "x shuffling"?
Traditional math games always show equations in the same format (like `ax + b = c`). This project innovates by placing `x` in 10 different algebraic contexts, making practice more varied and educational.

### What's special about this?
- **Maximum variety:** 10 different equation patterns
- **Clean architecture:** Follows SOLID principles
- **Educational focus:** Exposes users to diverse algebraic forms
- **Zero magic numbers:** Everything is configurable
- **Comprehensive docs:** Fully documented development process

## 🚀 Getting Started

### How do I run it?
```bash
python main.py
```

### What are the system requirements?
- Python 3.6+ (uses f-strings)
- No external dependencies (standard library only)
- Works on Linux, macOS, Windows

### How do I quit the game?
Type `quit` at any prompt.

## 🔄 Algorithm Questions

### How does x shuffling work?
The algorithm generates a random solution `x` (1-40), then creates equations in 10 different formats where solving for `x` gives that solution. See [algorithm.md](algorithm.md) for details.

### What are the 10 equation patterns?
1. Standard: `ax ± b = c`
2. Isolated Left: `x = c ± b`
3. Isolated Right: `c ± b = x`
4. Simple Add: `x ± b = c`
5. Simple Subtract: `x ± b = c`
6. Coefficient Isolated: `ax = c ± b`
7. Fractional: `x = (c ± b) / a`
8. Flipped Standard: `c = ax ± b`
9. Middle Term: `b ± ax = c`
10. Nested Operation: `(ax ± b) = c`

### Why 1-40 for x values?
Provides good difficulty range - not too easy (x=1) but not overwhelming (x=100+). Easily configurable via constants.

## 🏗️ Architecture Questions

### Why Single Responsibility Principle?
Each class has one job, making code:
- Easier to test
- Easier to modify
- Less prone to bugs
- More maintainable

### What's dependency injection?
Instead of classes creating their own dependencies, dependencies are "injected" from outside. This makes testing easier and components more flexible.

### Why no magic numbers?
Magic numbers (unexplained numeric literals) make code hard to understand and modify. Named constants are self-documenting and easily changeable.

## 🔧 Technical Questions

### How is mathematical correctness guaranteed?
Equations are constructed backwards: `answer = a*x ± b`, so by definition they're correct. No solving required during generation.

### Why avoid double negatives?
Equations like `x + -5 = 10` are confusing. The code automatically formats to `x - 5 = 10` for clarity.

### How does the game handle invalid input?
Try-catch blocks catch non-numeric input and prompt the user to try again. The game continues running smoothly.

## 📚 Development Questions

### How was this project built?
Incrementally with user guidance:
1. Basic CLI game
2. X shuffling algorithm
3. SRP architecture
4. Documentation

### Why incremental development?
Prevents overwhelming complexity. Each change is small, testable, and reversible. Focuses on core functionality first.

### What's the testing strategy?
- Manual testing of core functionality
- Edge case validation
- Syntax checking
- Import verification
- User experience testing

## 🎮 Gameplay Questions

### How do I know if my answer is correct?
The game immediately tells you "Correct! ✓" or "Not quite. x = [correct answer]".

### Can I see my score?
After quitting, the game shows: "Final Score: X/Y correct (Z.Z% accuracy)".

### What happens if I enter invalid input?
You'll see: "Please enter a number or 'quit'". The game continues.

### Are there different difficulty levels?
Currently one difficulty range (configurable via constants). Future versions may add adaptive difficulty.

## 🔮 Future Questions

### What's planned next?
Quality improvements, smart difficulty adaptation, and learning analytics - all based on user guidance and gradual complexity increases.

### Can I contribute?
Yes! See [contributing.md](contributing.md) for guidelines. Focus on user-requested features and maintain code quality standards.

### How can I request features?
Document your needs clearly. The project follows user-guided development, so feature requests drive the roadmap.

## 🐛 Troubleshooting

### "SyntaxError" when running?
Ensure you're using Python 3.6+. Check with:
```bash
python --version
```

### Game doesn't start?
Try syntax check:
```bash
python -m py_compile main.py
```

### Problems look wrong?
The math is guaranteed correct by construction. If you suspect an issue, check the algorithm documentation.

### Documentation not updating?
After code changes, update the relevant docs in the `docs/` folder.

## 📞 Getting Help

### Where to find more information?
- [README.md](../README.md) - Quick start
- [docs/index.md](index.md) - Documentation hub
- [docs/algorithm.md](algorithm.md) - Technical details
- [docs/architecture.md](architecture.md) - Code structure

### I found a bug?
Document the issue with steps to reproduce. Check if it's already covered in the testing guidelines.

### I want to understand the code better?
Start with the class docstrings in `main.py`, then read the relevant documentation files.

---

*Still have questions? Check the documentation or examine the well-commented code in `main.py`.*</content>
<parameter name="filePath">docs/faq.md