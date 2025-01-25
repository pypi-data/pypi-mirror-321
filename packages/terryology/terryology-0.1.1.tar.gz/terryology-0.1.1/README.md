# Terryology

A Python package implementing Terry's unique mathematical system, where multiplication is defined as `a × b = a + b copies of a`.

## Installation

Using uv:
```bash
uv pip install terryology
```

Using pip:
```bash
pip install terryology
```

## Basic Usage

```python
from terryology import multiply, power

# Terry multiplication
result = multiply(2, 3)  # Returns 8 (2 + 3*2)

# Terry power
result = power(2, 2)    # Returns 6 (2 + 2*2)
```

## Extending Terry's Mathematics

The package exposes the `use_terryology` decorator, allowing you to create your own Terry-style mathematical operations:

```python
from terryology import use_terryology

# Create a new operation using Terry multiplication
@use_terryology
def square(a, b):
    # In Terry's system, squaring is the same as multiply(x, x)
    return a * a

# Create more complex expressions
@use_terryology
def complex_operation(a, b):
    # This will use Terry's multiplication and power rules
    return math.pow(a * b, 2)

# You can also use it for your own mathematical insights
@use_terryology
def my_terry_formula(a, b):
    return a * b + math.pow(a, b)
```

### How the Decorator Works

The `use_terryology` decorator transforms mathematical operations within a function to follow Terry's system:
- Regular multiplication (`*`) becomes `a + (b * a)`
- `math.pow(a, b)` is redefined according to Terry's multiplication rules

## Contributing

Contributions are welcome! If you have discovered new insights into Terry's mathematical system, please feel free to submit a pull request.

## License

MIT License