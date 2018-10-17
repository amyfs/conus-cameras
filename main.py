import sys
from AL import cameras as AL
from AR import cameras as AR
from AZ import cameras as AZ
from CA import cameras as CA
from CO import cameras as CO
from CT import cameras as CT
from DE import cameras as DE
from FL import cameras as FL
from GA import cameras as GA
from IA import cameras as IA
from ID import cameras as ID
from IL import cameras as IL
from IN import cameras as IN
from KS import cameras as KS
from KY import cameras as KY
from LA import cameras as LA
from MA import cameras as MA
from MD import cameras as MD
from MI import cameras as MI
from MN import cameras as MN
from MO import cameras as MO
from MS import cameras as MS
from MT import cameras as MT
from NC import cameras as NC
from ND import cameras as ND
from NE import cameras as NE
from NewEngland import cameras as newengland
from NJ import cameras as NJ
from NM import cameras as NM
from NV import cameras as NV
from NY import cameras as NY
from OH import cameras as OH
from OK import cameras as OK
from OR import cameras as OR
from PA import cameras as PA
from RI import cameras as RI
from SC import cameras as SC
from SD import cameras as SD
from TN import cameras as TN
from TX import cameras as TX
from UT import cameras as UT
from VA import cameras as VA
from WI import cameras as WI
from WV import cameras as WV
from WY import cameras as WY

def main():
    print("id,lat,lon,description,format")
    for entry in [AL,AZ,CO,DE,GA,ID,IN,KY,MA,MD,MN,MS,NC,NE,NJ,NV,OH,OR,RI,SD,TN,UT,WV,AR,CA,CT,FL,IA,IL,KS,LA,MI,MO,MT,ND,newengland,NM,NY,OK,PA,SC,TX,VA,WI,WY]:
        sys.stderr.write(entry.__name__.split(".")[0])
        for camera in entry.list_cameras():
            if not isinstance(camera["format"],list):
                camera["format"] = [camera["format"]]
            print("{},{},{},{},{}".format(camera["id"],camera["geo"][0],camera["geo"][1],camera["description"],camera["format"]))

if __name__ == "__main__":
    main()