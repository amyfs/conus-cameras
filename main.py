from NewEngland import cameras as newengland
from MA import cameras as MA
from NY import cameras as NY
from RI import cameras as RI
from CT import cameras as CT
from PA import cameras as PA
from NJ import cameras as NJ
from MD import cameras as MD
from DE import cameras as DE
from WV import cameras as WV
from VA import cameras as VA
from NC import cameras as NC
from SC import cameras as SC
from GA import cameras as GA
from FL import cameras as FL
from OH import cameras as OH
from KY import cameras as KY
from TN import cameras as TN
from AL import cameras as AL
from MI import cameras as MI
from IN import cameras as IN
from MO import cameras as MO
from MN import cameras as MN
from MS import cameras as MS
from IA import cameras as IA
from IL import cameras as IL
from AR import cameras as AR
from WI import cameras as WI
from LA import cameras as LA
from ND import cameras as ND

def main():
    for entry in [newengland,MA,NY,RI,CT,PA,NJ,MD,DE,WV,VA,NC,SC,GA,FL,OH,KY,TN,AL,MI,IN,MO,MN,MS,IA,IL,AR,WI,LA,ND]:
        print(entry.list_cameras().__next__())

if __name__ == "__main__":
    main()