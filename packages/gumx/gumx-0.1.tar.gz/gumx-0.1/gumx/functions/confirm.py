import typing
from .. import utils
from ..consts import Color, Flag

class Style(typing.TypedDict):
    affirmative : str    = None
    negative    : str    = None
    show_help   : bool   = None
    prompt      : Color  = None
    selected    : Color  = None
    unselected  : Color  = None

def confirm(
    message  : str,
    default  : Flag[str        ] = None,
    timeout  : Flag[int | float] = None,
    style    : Flag[Style      ] = None,
    __args__ : dict[str        ] = None
) -> bool:
    '''
    Confirm whether to perform an action.
    
    :param message: Message to display.
    :param default: Default confirmation action.
    :param timeout: Timeout for the user to choose an option.
    :param style: Form style and color.
    '''
    
    process = utils.run(confirm, __args__, throw = False)
    
    return process.returncode == 0

# EOF