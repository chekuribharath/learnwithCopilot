import pytest
import Err
from io import StringIO
import contextlib

def test_greet_output():
    name = "Alice"
    buf = StringIO()
    with contextlib.redirect_stdout(buf):
        Err.greet(name)
    output = buf.getvalue().strip()
    assert output == f"Hello, {name}"
