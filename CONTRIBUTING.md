# Contributing to Transcript Combiner

Thank you for your interest in contributing to Transcript Combiner! This document provides guidelines and instructions for contributing to the project.

## Table of Contents
- [Development Environment Setup](#development-environment-setup)
- [Making Contributions](#making-contributions)
- [Code Style Guidelines](#code-style-guidelines)
- [Testing Requirements](#testing-requirements)
- [Commit Guidelines](#commit-guidelines)
- [Pull Request Process](#pull-request-process)

## Development Environment Setup

1. **Prerequisites**
   - Python 3.8 or higher
   - pip (Python package installer)
   - git

2. **Setting up your development environment**
   ```bash
   # Fork and clone the repository
   git clone https://github.com/YOUR-USERNAME/transcript-combiner
   cd transcript-combiner

   # Create a virtual environment
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate

   # Install dependencies
   pip install -r requirements.txt
   pip install -r requirements-dev.txt

   # Install spaCy language model
   python -m spacy download en_core_web_sm
   ```

## Making Contributions

1. **Fork the Repository**
   - Click the "Fork" button on the GitHub repository
   - Clone your fork locally
   - Add the upstream repository:
     ```bash
     git remote add upstream https://github.com/ORIGINAL-OWNER/transcript-combiner
     ```

2. **Create a Branch**
   ```bash
   git checkout -b feature/your-feature-name
   # or
   git checkout -b fix/your-fix-name
   ```

3. **Make Your Changes**
   - Write your code
   - Add tests for new functionality
   - Ensure all tests pass
   - Update documentation as needed

## Code Style Guidelines

- Follow PEP 8 style guide
- Use type hints for function arguments and return values
- Maximum line length: 88 characters (Black formatter default)
- Use descriptive variable and function names
- Document functions and classes using docstrings

Example:
```python
def combine_transcripts(
    transcript1: str,
    transcript2: str,
    threshold: float = 0.8
) -> str:
    """
    Combine two transcripts using similarity matching.

    Args:
        transcript1: First source transcript
        transcript2: Second source transcript
        threshold: Similarity threshold for matching

    Returns:
        Combined transcript text
    """
    # Implementation
```

## Testing Requirements

- All new code must include tests
- Maintain or improve code coverage
- Run tests before submitting PR:
  ```bash
  # Run all tests
  pytest

  # Run with coverage
  pytest --cov=src tests/
  ```

- Tests should be placed in the `tests/` directory
- Name test files with `test_` prefix
- Use meaningful test names that describe the behavior being tested

## Commit Guidelines

Format: `<type>(<scope>): <subject>`

Types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Formatting changes
- `refactor`: Code refactoring
- `test`: Adding/modifying tests
- `chore`: Maintenance tasks

Examples:
```
feat(processor): add new transcript alignment algorithm
fix(parser): handle empty transcript files
docs(readme): update installation instructions
```

## Pull Request Process

1. **Before Submitting**
   - Update your branch with upstream changes
   - Ensure all tests pass
   - Update documentation if needed
   - Run linting and formatting checks

2. **PR Description**
   - Use the provided PR template
   - Describe the changes clearly
   - Link related issues
   - Include screenshots for UI changes

3. **Review Process**
   - PRs require at least one approval
   - Address review comments promptly
   - Maintainers may request changes
   - Once approved, maintainers will merge the PR

4. **After Merge**
   - Delete your branch
   - Update your fork
   - Close related issues

## Questions or Problems?

Feel free to open an issue for:
- Bug reports
- Feature requests
- Questions about the codebase
- Contributing guidance

Thank you for contributing to Transcript Combiner!
```