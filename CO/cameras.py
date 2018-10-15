from .stillCameras import list_cameras as one
from .streamingCameras import list_cameras as two

def list_cameras():
    for cam in one():
        yield cam
    for cam in two():
        yield cam