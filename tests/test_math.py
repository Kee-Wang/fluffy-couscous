"""
Testing for the math.py module
This is called testing framework.
Use
python -c "import pytest"
before running this script.
After scripts are done, use
`py.test -v`
"""
import fluffy_couscous as fc
import pytest

#Using `test_` as function so pytest can recognize.
def test_add():
    assert fc.math.add(5,2) == 7
    assert fc.math.add(2,5) == 7
