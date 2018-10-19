import xml.etree.ElementTree as ET
from pathlib import Path

directory = Path(__file__).parent.resolve()
ns = {
    'ns1': 'http://services.511nj.org/'
}
tree = ET.parse(str(directory / "TestGetCamerasByRoute"))
root = tree.getroot()


def list_cameras():
    #print(ET.tostring(root[0]))
    for child in root:
        yield {"description": child.find('ns1:Description',ns).text,
               "geo": {
                   "lat": child.find('ns1:Lat',ns).text,
                   "lon": child.find('ns1:Lon',ns).text
               },
               "id": child.find('ns1:ID',ns).text,
               "format": child.find('ns1:CameraImageURL',ns).text
            }