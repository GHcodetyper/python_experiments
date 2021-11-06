# py 3.8
from unittest.mock import MagicMock
from unittest.mock import patch


class ProductionClass:
    def method(self):
        self.something(1, 2, 3)
    def something(self, a, b, c):
        pass

real = ProductionClass()
real.something = MagicMock()
real.method()
real.something.assert_called_once_with(1, 2, 3)
#real.something.assert_called_once_with(1) # gives exception