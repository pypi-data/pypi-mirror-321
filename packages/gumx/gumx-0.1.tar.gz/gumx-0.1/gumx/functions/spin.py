import typing
import subprocess
import contextlib
from .. import utils
from .. import consts
from ..consts import Color, Flag

class Style(typing.TypedDict):
    spinner : Color = None
    title   : Color = None

@contextlib.contextmanager
def spin(
    title    : Flag[str                   ] = None,
    spinner  : Flag[typing.Literal['dot'] ] = None,
    align    : Flag[typing.Literal['left']] = None,
    timeout  : Flag[int | float           ] = None,
    style    : Flag[Style                 ] = None,
    __args__ : dict[str                   ] = None
):
    '''
    Display spinner while running a script.
    
    :param title: Text to display while spining.
    :param spinner: Spinner type.
    :param align: Spinner alignment.
    :param timeout: Timeout until abort.
    :param style: widget type.
    '''
    
    try:
        cmd = [consts.INSTALL, 'spin'] + utils.dump_args(spin, __args__) + ['--']
        
        process = subprocess.Popen()
        
        yield
    
    finally:
        pass

# EOF