# Greeter

A simple Python module providing greeting functionality.

## Features

- `greet(name)` function in `greet.py` returning personalized greeting strings.
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

## Running Tests

To run the unit tests locally using Python's built-in `unittest` runner:

```bash
python3 -m unittest test_greet.py
```

Or run test discovery across the repository:

```bash
python3 -m unittest discover
```
