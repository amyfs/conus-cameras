import xml.etree.ElementTree as ET
from pathlib import Path
import re

directory = Path(__file__).parent.resolve()
tree = ET.parse(str(directory / "cctv.kml"))
root = tree.getroot()

ns = {
    "ns1": "http://www.opengis.net/kml/2.2"
}

def list_cameras():
    for row in root[0].findall("ns1:Placemark",ns):
        xp = lambda x: row.find(f".//ns1:{x}",ns).text
        co = row.find("./ns1:Point/ns1:coordinates",ns).text.split(",")
        yield {
            "description": xp("name"),
            "geo": {"lat": co[0], "lon": co[1]},
            "id": re.sub('[^A-Za-z0-9]+', '', xp("name").lower()),
            "format": xp("description")
        }

if __name__ == "__main__":
    for camera in list_cameras():
        print(camera)