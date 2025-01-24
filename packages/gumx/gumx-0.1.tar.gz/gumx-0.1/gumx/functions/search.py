import typing
from .. import utils
from ..consts import Color, Flag

class Style(typing.TypedDict):
    indicator          : Color  = None
    selected_indicator : Color  = None
    unselected_prefix  : Color  = None
    header             : Color  = None
    text               : Color  = None
    cursor_text        : Color  = None
    match              : Color  = None
    prompt             : Color  = None
    placeholder        : Color  = None

def search(
    items       : typing.Iterable,
    prompt      : Flag[str        ] = None,
    header      : Flag[str        ] = None,
    placeholder : Flag[str        ] = None,
    value       : Flag[str        ] = None,
    reverse     : Flag[bool       ] = None,
    fuzzy       : Flag[bool       ] = None,
    sort        : Flag[bool       ] = None,
    timeout     : Flag[int | float] = None,
    style       : Flag[Style      ] = None,
    __args__ : dict[str           ] = None
) -> typing.Any:
    '''
    Search in a list of values with fuzzy matching.
    
    :param items: Items to filter.
    :param header: Header to print at the top of the form.
    :param placeholder: Form placeholder.
    :param prompt: Text to display on top of the form.
    :param value: Initial filter value.
    :param reverse: Wether to reverse filtering order.
    :param fuzzy: Wether to allow fuzzy sorting.
    :param sort: Wether to sort the results.
    :param timeout: Timeout for the user to interact.
    :param style: Form style and color.
    
    :return: List of filtered items.
    '''
    
    raw_items = __args__['items'] = utils.dump(items)
    
    output = utils.run(search, __args__).stdout.decode('utf-8').strip()
    
    for i, r in zip(items, raw_items):
        if r == output:
            return i

# EOF