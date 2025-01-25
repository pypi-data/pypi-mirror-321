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

## Usage

```python
from terryology import multiply, power

# Terry multiplication
result = multiply(2, 3)  # Returns 8 (2 + 3*2)

# Terry power
result = power(2, 2)    # Returns 6 (2 + 2*2)
```

## License

MIT License