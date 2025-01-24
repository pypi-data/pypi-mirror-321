import typing
from .. import utils
from ..consts import Color, Flag, Cursor

class Style(typing.TypedDict):
    cursor      : Cursor = None
    width       : int    = None
    show_help   : bool   = None
    prompt      : Color  = None
    placeholder : Color  = None
    cursor      : Color  = None
    header      : Color  = None

def input(
    prompt      : Flag[str  ] = None,
    header      : Flag[str  ] = None,
    value       : Flag[str  ] = None,
    placeholder : Flag[str  ] = None,
    char_limit  : Flag[str  ] = None,
    password    : Flag[bool ] = None,
    style       : Flag[Style] = None,
    __args__    : dict[str  ] = None
) -> typing.Any:
    '''
    Prompt the user for input.
    
    :param prompt: Input field prompt.
    :param header: Input field header.
    :param value: Default input value.
    :param placeholder: Input field placeholder.
    :param char_limit: Max characters limit of the input.
    :param password: Wether to mask the input characters.
    :param style: Form style and color.
    
    :return: The written content.
    '''
    
    return utils.run(input, __args__).stdout.decode('utf-8').strip()

# EOF