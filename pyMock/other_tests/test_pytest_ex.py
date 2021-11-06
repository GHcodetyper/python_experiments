# usage:
# py -m pytest -v
# py -m pytest -v -k 'test_s' #filter on test name
# py -m pytest -v -lf #last-failed
# py -m pytest -v -sw #stepwise
# py -m pytest -v --collect-only
# py -m pytest -s #print to console/stdout

# different coverage options:
# coverage run -m pytest -v
# py -m coverage html --omit="*test*"
# py -m coverage run -m pytest -v
# py -m coverage report
# py -m coverage annotate

# codestyle:
# pycodestyle .
# py -m flake8


from Calculator import Calculator

#Each test method starts with the keyword test_
#to run: py -m pytest -v

import sys
import pytest

print('\n' + sys.platform + '\n')

def test_subtract():
    calculator = Calculator()

    assert calculator.subtract(28,24) == 4


#@pytest.mark.skipif(sys.platform == 'darwin', reason = 'don\'t need for macos')
@pytest.mark.skipif(sys.platform.startswith("win"), reason = 'don\'t need for win')
def test_divide():
    calculator = Calculator()

    assert calculator.divide(28,7) == 4


@pytest.mark.xfail()
#@pytest.mark.skip(reason="no way of currently testing this")
def test_add():
    calculator = Calculator()

    assert calculator.add(4,7) == 11
