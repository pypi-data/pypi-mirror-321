# skleernexample

A Python library for storing and managing scikit-learn code examples.

## Installation

```bash
pip install -e .
```

## Usage

### Saving Code Examples
```python
from skleernexample import CodeExample

# Create an instance to save code
code = CodeExample()

# Save a code example
decision_tree_code = """
y_preddt = dt.predict(x_test)
print(accuracy_score(y_test, y_preddt))
print(classification_report(y_test, y_preddt))
print(confusion_matrix(y_test, y_preddt))
"""
code.save_code("decision_tree", decision_tree_code)
```

### Printing Code Examples
```python
from skleernexample import print_code

# Simply print any saved code example
print_code("decision_tree")
```
