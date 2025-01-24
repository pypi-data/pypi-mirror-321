'''
    GUMX package
    
    https://github.com/egsagon/gumx
'''

import typing
from . import setup
from .consts import Error

# Setup GUM functions
if typing.TYPE_CHECKING:
    from .functions import *

# Run installation setup
setup.run()
__getattr__ = setup.arg_injector

# EOF