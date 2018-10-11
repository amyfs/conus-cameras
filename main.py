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

def main():
    for entry in [newengland,MA,NY,RI,CT,PA,NJ,MD,DE,WV,VA,NC,SC,GA,FL,OH]:
        print(entry.list_cameras().__next__())

if __name__ == "__main__":
    main()