import typing
from .. import utils
from ..consts import Color, Flag

class Style(typing.TypedDict):
    height      : int    = None
    cursor      : str    = None
    show_help   : bool   = None
    cursor      : Color  = None
    symlink     : Color  = None
    directory   : Color  = None
    file        : Color  = None
    permissions : Color  = None
    selected    : Color  = None
    file_size   : Color  = None

def file(
    path      : str,
    all       : Flag[bool       ] = None,
    file      : Flag[bool       ] = None,
    directory : Flag[bool       ] = None,
    timeout   : Flag[int | float] = None,
    style     : Flag[Style      ] = None,
    __args__ : dict[str         ] = None
) -> list[str]:
    '''
    Prompt the user to select a file from the file tree.
    
    :param path: Path to begin traversing.
    :param all: Show hidden files.
    :param file: Allow files selection.
    :param directory: Allow directory selection.
    :param timeout: Timeout for the user to choose an option.
    :param style: Form style and color.
    
    :return: A list of pathes.
    '''
    
    process = utils.run(_file, __args__)
    
    return process.stdout.decode('utf-8').split('\n')


# Hack to differentiate arg and func
_file = file

# EOF