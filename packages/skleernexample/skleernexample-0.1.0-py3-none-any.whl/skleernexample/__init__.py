from .code_manager import CodeExample

_code_instance = CodeExample()

def print_code(name):
    """Print a code example by name."""
    print(_code_instance(name))
