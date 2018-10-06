from NewEngland import cameras as newengland
from MA import cameras as MA
from NY import cameras as NY
from RI import cameras as RI
from CT import cameras as CT
from PA import cameras as PA
from NJ import cameras as NJ

def main():
    for entry in [newengland,MA,NY,RI,CT,PA,NJ]:
        print(entry.list_cameras().__next__())

if __name__ == "__main__":
    main()