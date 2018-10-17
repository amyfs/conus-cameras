import xml.etree.ElementTree as ET
from pathlib import Path

directory = Path(__file__).parent.resolve()
tree = ET.parse(str(directory / "GetFullCameraListXML.xml"))
root = tree.getroot()

ns = {
    "ns1": "http://tempuri.org/"
}

def list_cameras():
    for row in root[0].findall("ns1:camera",ns):
        yield {
            "description": row.get("description"),
            "geo": [i.text for i in row],
            "id": row.get("ID"),
            "format": row.get("CameraImageURL")
        }

if __name__ == "__main__":
    for camera in list_cameras():
        print(camera)