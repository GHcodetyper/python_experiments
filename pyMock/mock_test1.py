#import pytest

# py 3.8
from unittest.mock import MagicMock
from unittest.mock import patch

# py 2.7
#from mock import Mock
#from mock import mock
#from mock import MagicMock


class SomeClass:
    def method(self):
        print("real method output")

real = SomeClass()

real.method() # real call

#mock a real method
real.method = MagicMock(name='method')
real.method(3, 4, 5, key='value')
#mock a real method

real.method() # already mocked, no any print


#if __name__ == '__main__':
#        test_case_01()