from unittest.mock import Mock


class ProductionClass:
    def closer(self, something):
        something.close()


real = ProductionClass()
mock = Mock()
real.closer(mock)
mock.close.assert_called_with()