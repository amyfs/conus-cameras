from .cam import list_cameras as one
from .Ext_Prd import list_cameras as two

def list_cameras():
    '''for camera in one():
        yield camera'''
    for camera in two():
        yield camera