import csv
from pathlib import Path

directory = Path(__file__).parent.resolve() 

MICRO = 1000000 #latitude and longitude conversion constant (curse you txdot)

def list_cameras():
    with open(str(directory / "cameras.csv")) as f:
        c = csv.reader(f)
        c.__next__()
        for row in c:
            yield {"description": row[0], "geo": [float(row[4])/MICRO,float(row[5])/MICRO], "id": row[1], "format": "PLACEHOLDER"}