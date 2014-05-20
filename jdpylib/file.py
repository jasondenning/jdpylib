"""
File utility methods
"""
import os

from jdpylib.errors import InvalidPath, FileExistsNoOverwrite

def write(path, content, overwrite=False):
    """
    Safe write function - will fail if file exists, unless overwrite=True
    """
    if os.path.lexists and not overwrite:
        raise FileExistsNoOverwrite(path=path)
    else:
        with open(path, 'w') as f:
            f.write(content)

def read(path):
    """
    Opens a file and returns its contents

    raises an InvalidPath exception if the path does not exist
    """
    if not os.path.lexists(path):
        raise InvalidPath(path=path)

    with open(path, 'r') as f:
        return f.read()
