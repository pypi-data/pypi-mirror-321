import typing
from .. import utils
from ..consts import Color, Flag, Cursor

class Style(typing.TypedDict):
    width              : int    = None
    height             : int    = None
    show_cursor_line   : bool   = None
    show_line_numbers  : bool   = None
    show_help          : bool   = None
    base               : Color  = None
    header             : Color  = None
    placeholder        : Color  = None
    prompt             : Color  = None
    end_of_buffer      : Color  = None
    line_number        : Color  = None
    cursor_line_number : Color  = None
    cursor_line        : Color  = None
    cursor             : Cursor = None

def write(
    header      : Flag[str  ] = None,
    prompt      : Flag[str  ] = None,
    placeholder : Flag[str  ] = None,
    char_limit  : Flag[int  ] = None,
    value       : Flag[str  ] = None,
    style       : Flag[Style] = None,
    __args__    : dict[str  ] = None
) -> bool:
    '''
    Prompt for some multi-line text (ctrl+d to complete text entry).
    
    :param header: Header to print at the top of the form.
    :param placeholder: Text box placeholder.
    :param char_limit: Limit of characters to write.
    :param prompt: Prompt to display.
    :param value: Initial text box value.
    :param style: Form style and color.
    
    :return: The written content.
    '''
    
    output = utils.run(write, __args__).stdout.decode('utf-8')
    
    return output.strip()

# EOF