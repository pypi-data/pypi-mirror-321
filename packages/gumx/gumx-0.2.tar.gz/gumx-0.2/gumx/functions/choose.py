import typing
from .. import utils
from ..consts import Color, Flag

class Style(typing.TypedDict):
    height            : int   = None
    cursor_prefix     : str   = None
    selected_prefix   : str   = None
    unselected_prexix : str   = None
    show_help         : bool  = None
    item              : Color = None
    cursor            : Color = None
    header            : Color = None
    selected          : Color = None

def choose(
    items    : typing.Iterable,
    header   : Flag[str            ] = None,
    limit    : Flag[int            ] = None,
    ordered  : Flag[bool           ] = None,
    selected : Flag[typing.Iterable] = None,
    timeout  : Flag[int | float    ] = None,
    style    : Flag[Style          ] = None,
    __args__ : dict[str            ] = None
) -> list:
    '''
    Choose an option from a list of choices.
    
    :param items: Iterable of items to choose from.
    :param header: Header to print at the top of the form.
    :param limit: Multiple selection limit. 0 = No limit.
    :param ordered: Wether to keep the order of selected options.
    :param selected: Item(s) selected by default.
    :param timeout: Timeout until for the user to choose an option.
    :param style: Form style and color.
    
    :return: List of selected items.
    '''
    
    raw_items = __args__['items'] = utils.dump(items)
    
    choices = utils.run(choose, __args__).stdout.decode('utf-8').split('\n')
    
    return [i for i, r in zip(items, raw_items) if r in choices]

# EOF