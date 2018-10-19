import xml.etree.ElementTree as ET
from pathlib import Path

directory = Path(__file__).parent.resolve()
ns = {
    'ns1': 'http://www.opengis.net/kml/2.2'
}
tree = ET.parse(str(directory / "Camera.xml"))
root = tree.getroot()

def list_cameras():
    for row in root[0].iterfind("ns1:Placemark",ns):
        xp = lambda x: row.find(f".//ns1:SimpleData[@name='{x}']",ns).text
        geo = row.find("./ns1:Point/ns1:coordinates",ns).text.split(",")
        yield {
            "description": xp("DisplayName"),
            "geo": {
                "lat": geo[1],
                "lon": geo[0]
            },
            "id": xp("IntId"),
            "format": xp("ImageUrl")
            }

if __name__ == "__main__":
    print(list_cameras().__next__())