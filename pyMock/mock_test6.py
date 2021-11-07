# py 3.8
from unittest.mock import MagicMock, call
from unittest.mock import patch


mock = MagicMock()
mock.method()

mock.attribute.method(10, x=53)

print(mock.mock_calls)

expected = [call.method(), call.attribute.method(10, x=53)]
assert mock.mock_calls == expected