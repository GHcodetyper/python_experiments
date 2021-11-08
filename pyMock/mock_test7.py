# py 3.8
from unittest.mock import Mock, call
from unittest.mock import patch

m = Mock()
m.factory(important=True).deliver()

print(m.mock_calls[-1] == call.factory(important=False).deliver())