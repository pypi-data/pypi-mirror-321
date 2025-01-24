'''
    GUMX setup.
'''

import os
import glob
import typing
import inspect
import zipfile

from . import utils
from . import consts
from . import functions


def download() -> str:
    '''
    Download the latest version of the GUM archive to
    the GUM user data dir.
    Returns the extracted folder location.
    '''
    
    print('[GUMX] Fetching latest GUM executable')
    assets = utils.get(consts.API).json()[0]['assets']
    
    # Fetch versions
    versions = list(filter(lambda asset: (
        asset['name'].endswith(('tar.gz', 'zip'))
        and consts.OS in asset['name']
        and consts.ARCH in asset['name']
    ), assets))
    
    assert len(versions), 'Could not find a compatible version'
    version = versions[0] # Most recent version
        
    # Download archive
    archive_path = os.path.join(consts.DIR, version['name'])
    install_path = os.path.join(consts.DIR, 'gum')
    
    print('[GUMX] Downloading release', version['name'])
    utils.download(version['browser_download_url'], archive_path)
    
    # Extract archive
    with zipfile.ZipFile(archive_path) as archive:
        archive.extractall(install_path)
    
    # Cleanup
    os.remove(archive_path)
    return install_path

def find(location: str) -> str:
    '''
    Find GUM executable in a folder.
    '''
    
    pattern = os.path.join(location, '**/gum*')
    
    _, *files = glob.glob(pattern, recursive = True)
    
    return files[0]

def run() -> None:
    '''
    Setup the GUM executable.
    '''
    
    install_link = os.path.join(consts.DIR, 'executable')
    
    if not os.path.exists(install_link):
        consts.INSTALL = find(download())
        print('[GUMX] Installation complete')
        
        with open(install_link, 'w') as file:
            file.write(consts.INSTALL)
            
            print(consts.INSTALL)
    
    else:
        with open(install_link) as file:
            consts.INSTALL = file.read()

def arg_injector(name: str) -> typing.Callable:
    '''
    Append an `__args__` argument on function calls.
    '''
    
    def wrapper(*args, **kwargs) -> None:
        func: typing.Callable = getattr(functions, name)
        arguments = inspect.signature(func).bind(*args, **kwargs).arguments
        
        return func(**(arguments | {'__args__': arguments}))
    
    return wrapper

# EOF