from .cams1 import list_cameras as one
from .StreamingCams2 import list_cameras as two

def list_cameras():
    for i in one():
        yield i
    for i in two():
        yield i