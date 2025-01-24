'''
    GUMX constants.
'''

import os
import typing
import platform
import platformdirs


# Installation constants
API = 'https://api.github.com/repos/charmbracelet/gum/releases'

OS = platform.system()

ARCH = {'amd64': 'x86_64', 'x86': 'i386', 'aarch64': 'arm64'} \
    [platform.machine().lower()]

DIR = platformdirs.user_data_dir('gumx')
os.makedirs(DIR, exist_ok = True)

INSTALL: str = None


# Type definitions
Flag = typing.Optional

class Error(Exception):
    '''
    An error raised by GUM.
    '''

class Color(typing.TypedDict):
    foreground = None
    background = None

class Cursor(Color):
    mode: typing.Literal['blink'] = None

# EOF