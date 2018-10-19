
uniontown = {"px": [203,405], "ll": [46.517271,-117.081126]}
laurier = {"px": [12,336], "ll": [48.998293,-118.224524]}
test = {"px": [276,102]}

def vertical_per_pixel():
    px_bottom = uniontown["px"][0]
    px_top = laurier["px"][0]
    ll_bottom = uniontown["ll"][1]
    ll_top = laurier["ll"][1]
    px,ll = px_bottom-px_top,ll_bottom-ll_top
    o = ll/px
    #print(f"{px} == {ll}")
    #print(f"{ll} / {px} = {o}")
    return o

def horizontal_per_pixel():
    px_right = uniontown["px"][1]
    px_left = laurier["px"][1]
    ll_right = uniontown["ll"][0]
    ll_left = laurier["ll"][0]
    px,ll = px_left-px_right,ll_right-ll_left
    o = ll/px
    print(f"{px} == {ll}")
    print(f"{ll} / {px} = {o}")
    return o

def zero_lat():
    scale_h = horizontal_per_pixel()
    uniontown_x = laurier["px"][1]
    uniontown_lat = laurier["ll"][0]

    zero_lat = uniontown_lat - (uniontown_x*scale_h)
    print(f"{uniontown_lat} - ({uniontown_x}*{scale_h}) = {zero_lat}")
    return zero_lat

def zero_lng():
    scale_v = vertical_per_pixel()
    uniontown_y = laurier["px"][0]
    uniontown_lng = laurier["ll"][1]

    zero_lng = uniontown_lng - uniontown_y*scale_v
    print(f"{uniontown_lng} - {uniontown_y}*{scale_v} = {zero_lng}")

def tz_lat():
    laurier_x = laurier["px"][0]
    laurier_y = laurier["px"][1]
    laurier_lat = laurier["ll"][0]
    laurier_lng = laurier["ll"][1]

    laurier_scale_h = laurier_x / laurier_lng
    laurier_scale_v = laurier_y / laurier_lat

    print(f"scale_h: {laurier_x} / {laurier_lng} = {laurier_scale_h}")
    print(f"scale_v: {laurier_y} / {laurier_lat} = {laurier_scale_v}")
    zero_lat = laurier_lng - laurier_x*laurier_scale_h
    zero_lng = laurier_lat - laurier_y*laurier_scale_v
    print(f"zero_lng: {laurier_lng} - {laurier_x}*{laurier_scale_h} = {zero_lat}")
    print(f"zero_lat: {laurier_lat} - {laurier_y}*{laurier_scale_v} = {zero_lng}")

if __name__ == "__main__":
    tz_lat()



