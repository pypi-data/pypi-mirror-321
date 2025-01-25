from .code_manager import CodeExample
from .built_in_examples import load_built_in_examples

_code_instance = CodeExample()
load_built_in_examples(_code_instance)

def snss(name):
    """Print a code example by name."""
    print(_code_instance(name))
