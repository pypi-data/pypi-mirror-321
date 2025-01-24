import typing
import requests
import subprocess

from . import consts

def get(url: str, **kw) -> requests.Response:
    '''
    GET request wrapper.
    '''
    
    response = requests.get(url, **kw)
    response.raise_for_status()
    return response

def download(url: str, path: str, chunk_size = 8192) -> None:
    '''
    Download a large file.
    '''
    
    with get(url, stream = True) as stream, open(path, 'wb') as file:
        for chunk in stream.iter_content(chunk_size):
            file.write(chunk)

def dump(obj: typing.Any) -> str | list[str]:
    '''
    Dump a single value into string.
    
    If the object is an iterable, objects inside will be dumped.
    '''
    
    if obj is True:
        return ''
    
    if isinstance(obj, str):
        return obj
    
    if isinstance(obj, dict):
        obj = [f'{k} - {v}' for k, v in obj.items()]
    
    if isinstance(obj, tuple | list):
        return list(map(dump, obj))
    
    return repr(obj)

def flatten(obj: dict, t: dict = None, r: str = '') -> dict:
    '''
    Flatten a style dict.
    '''
    
    track = t or {}
    
    for k in obj:
        if isinstance(obj[k], dict):
            flatten(obj[k], track, r + k + '.')
        
        else:
            track[r + k] = obj[k]
    
    return track

def dump_args(func: typing.Callable, args: dict[str, typing.Any]) -> list[str]:
    '''
    Dump arguments into a shell command.
    '''
    
    t = func.__annotations__
    
    # Construct args chain
    output = []
    
    for arg, value in args.items():
        if arg == 'style' or value in (None, False): continue
        
        raw = dump(value)
        
        if 'Optional' in str(t[arg]):
            output.append(f'--{arg}')
        
        if isinstance(raw, list):
            output += raw
        elif raw != '':
            output.append(raw)
    
    for arg, value in flatten(args.get('style', {})).items():
        output.append(f'--{arg}')
        output.append(dump(value))
    
    return output

def run(
    func: typing.Callable,
    args: dict[str, typing.Any],
    throw: bool = True,
    **proc_kwargs
) -> subprocess.CompletedProcess:
    '''
    Run a GUM command.
    '''
    
    cmd = [consts.INSTALL, func.__name__] + dump_args(func, args)
    
    print('[EXEC]', cmd)
    
    process = subprocess.run(**({
        'args': cmd,
        'stdout': subprocess.PIPE
    } | proc_kwargs))
    
    if throw and process.returncode != 0:
        raise consts.Error(f'Error code {process.returncode}')
    
    return process

# EOF