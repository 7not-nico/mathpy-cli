# Contributing Guide

## 🤝 How to Contribute

This project welcomes contributions! Since we're following an **incremental, user-guided development approach**, contributions should align with the project's philosophy of **core focus with gradual complexity**.

## 📋 Contribution Principles

### Core Philosophy
- **User-guided development:** Features added based on user needs/requests
- **Incremental complexity:** Small, manageable enhancements
- **Quality over quantity:** Well-tested, clean code only
- **Documentation first:** Document before implementing

### Code Standards
- **SRP compliance:** Each class/function has single responsibility
- **No magic numbers:** All configurable values named as constants
- **Clean architecture:** Maintain dependency injection pattern
- **Comprehensive docs:** Document all changes

## 🚀 Contribution Process

### 1. Understand the Project
```bash
# Read the documentation
cat README.md
cat docs/architecture.md
cat docs/algorithm.md

# Run the current code
python main.py
```

### 2. Identify Enhancement Area
- **Bug fixes:** Report and fix any issues
- **User-requested features:** Implement based on user guidance
- **Quality improvements:** Enhance existing functionality
- **Documentation:** Improve or add documentation

### 3. Plan Your Changes
- **Document intent:** What problem are you solving?
- **Design approach:** How does it fit with SRP architecture?
- **Test plan:** How will you verify the changes?
- **Documentation:** What docs need updating?

### 4. Implement Changes
```python
# Follow existing patterns
class NewFeature:
    """Single responsibility: [clear description]"""

    def __init__(self, dependency1, dependency2):
        # Dependency injection pattern
        pass

    def method_name(self):
        """Clear docstring explaining responsibility"""
        pass
```

### 5. Test Thoroughly
```bash
# Syntax check
python -m py_compile main.py

# Manual testing
python main.py  # Test various scenarios

# Edge case testing
# Test with different inputs, boundary conditions
```

### 6. Update Documentation
```markdown
# Update relevant docs
- docs/architecture.md (if changing structure)
- docs/algorithm.md (if changing algorithm)
- docs/development.md (if changing process)
- README.md (if changing usage)
```

### 7. Submit Changes
- **Clear commit messages:** Explain what and why
- **Reference issues:** Link to user requests/discussions
- **Documentation included:** All changes documented

## 🎯 Enhancement Guidelines

### Feature Requests
- **Must align with core mission:** Math practice with x shuffling
- **User-requested:** Based on actual user needs
- **Incremental:** Small, focused enhancements
- **Testable:** Clear success criteria

### Code Quality
- **PEP 8 compliant:** Standard Python formatting
- **Type hints:** Optional but encouraged
- **Error handling:** Graceful failure with clear messages
- **Performance:** No unnecessary complexity

### Testing Requirements
- **Manual testing:** Verify functionality works
- **Edge cases:** Test boundary conditions
- **Error conditions:** Test invalid inputs
- **Regression testing:** Ensure existing features still work

## 📝 Specific Contribution Areas

### Algorithm Enhancements
```python
# Adding new equation patterns
def add_new_pattern(self):
    # Must maintain mathematical correctness
    # Follow existing formatting patterns
    # Add to equation_types list
    pass
```

### UI Improvements
```python
# Enhancing user interface
class EnhancedUI(UserInterface):
    # Must maintain SRP (only I/O)
    # Can add new display methods
    # Should be backward compatible
    pass
```

### Quality Improvements
```python
# Adding validation/trivial detection
def is_quality_equation(self, problem, x):
    # Prevent obvious equations
    # Ensure mathematical variety
    # Return boolean quality assessment
    pass
```

### Documentation
```markdown
# Adding new documentation
## New Feature Guide

### Overview
[Explain the feature]

### Implementation
[Technical details]

### Usage
[How to use]

### Examples
[Code examples]
```

## 🚫 What NOT to Contribute

### Without User Guidance
- **Unrequested features:** Don't add features "because they're cool"
- **Major rewrites:** Don't change architecture without discussion
- **Scope creep:** Don't add unrelated functionality

### Quality Compromises
- **Magic numbers:** Never add unexplained numeric literals
- **Complex code:** Avoid over-engineering simple problems
- **Undocumented changes:** All changes must be documented

### Breaking Changes
- **API changes:** Don't break existing interfaces
- **File structure:** Don't reorganize without discussion
- **Dependencies:** Don't add external dependencies

## 🧪 Testing Your Contributions

### Required Tests
```bash
# 1. Syntax validation
python -m py_compile main.py

# 2. Import testing
python -c "import main; print('Import successful')"

# 3. Basic functionality
python -c "
from main import ProblemGenerator
gen = ProblemGenerator()
for i in range(5):
    prob, x = gen.generate()
    print(f'{prob} → x={x}')
"

# 4. Full game test (manual)
python main.py  # Test with various inputs
```

### Edge Case Testing
- **Boundary values:** x=1, x=40, negative coefficients
- **Invalid inputs:** Non-numeric, empty strings, special characters
- **Quit functionality:** Ensure graceful exit
- **Error recovery:** Test behavior after invalid inputs

## 📚 Documentation Standards

### Code Documentation
```python
class NewClass:
    """Single line description of responsibility.

    Detailed explanation of what this class does,
    why it exists, and how it fits into the architecture.
    """

    def method_name(self, param1, param2):
        """Single line description of what method does.

        Args:
            param1: Description of param1
            param2: Description of param2

        Returns:
            Description of return value

        Raises:
            ExceptionType: When this exception occurs
        """
        pass
```

### Commit Message Format
```
feat: add new equation pattern for fractions

- Add fractional equation type to x shuffling algorithm
- Includes proper formatting for division notation
- Maintains mathematical correctness
- Updates algorithm documentation

Closes #issue-number
```

## 🎉 Recognition

Contributors will be:
- **Acknowledged in documentation**
- **Listed in project credits**
- **Included in version release notes**
- **Recognized for quality contributions**

## 📞 Getting Help

- **Review existing docs:** Check `docs/` folder first
- **Examine the code:** Read `main.py` with comments
- **Run examples:** Test current functionality
- **Ask questions:** Document areas needing clarification

---

*Remember: This project values **quality over quantity** and **incremental progress over big changes**. Let's build something excellent together! 🚀*</content>
<parameter name="filePath">docs/contributing.md