# Greeter

A simple Python module providing greeting functionality.

## Features

- `greet(name)` function in `greet.py` returning personalized greeting strings.
- Code linting using `pylint`.
- Automated testing using Python's built-in `unittest` framework.
- Continuous Integration via GitHub Actions.

## Prerequisites

- Python 3.8+ (no third-party dependencies required)

## Usage

You can import and use the `greet` function in your Python code:

```python
from greet import greet

print(greet("Alice"))  # Output: Hello, Alice!
```

Or run it directly from the command line:

```bash
python3 -c "from greet import greet; print(greet('World'))"
```

## Linting

Linting is the automated process of analyzing source code without executing it to detect programmatic bugs, stylistic violations, syntax issues, and deviations from coding standards (such as PEP 8). It helps maintain high code quality, consistency, and readability across the project.

This project uses **Pylint** as its linter.

### Running the Linter Locally

To run the linter locally, first install the dependencies from `requirements.txt`:

```bash
pip install -r requirements.txt
```

Then run `pylint` on the project source and test files:

```bash
pylint greet.py test_greet.py
```

## Running Tests

To run the unit tests locally using Python's built-in `unittest` runner:

```bash
python3 -m unittest test_greet.py
```

Or run test discovery across the repository:

```bash
python3 -m unittest discover
```
