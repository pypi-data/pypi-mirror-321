import typing
from .. import utils
from ..consts import Color, Flag

class Style(typing.TypedDict):
    show_line_numbers : bool   = None
    help              : Color  = None
    line_number       : Color  = None
    match             : Color  = None
    match_highlight   : Color  = None

def pager(
    file      : str,
    soft_wrap : Flag[bool       ] = None,
    timeout   : Flag[int | float] = None,
    style     : Flag[Style      ] = None,
    __args__  : dict[str        ] = None
) -> None:
    '''
    Scroll through a long document.
    
    :param file: File to display.
    :param soft_wrap: Wether to soft wrap file lines.
    :param timeout: Timeout for the user to choose an option.
    :param style: Form style and color.
    '''
    
    # Not fun for large files, but file redirection does
    # not work the same on all platforms and i'm tired
    with open(file) as handle:
        __args__['file'] = handle.read()
    
    utils.run(pager, __args__, stdout = None)

# EOF