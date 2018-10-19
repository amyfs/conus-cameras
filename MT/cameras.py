from requests_html import HTMLSession

session = HTMLSession()

cameras = [
 {"description": "Lookout Pass", "geo": [47.45357298,-115.6950595], "id": "150000", "url": "http://rwis.mdt.mt.gov/scanweb/Camera.asp?Pageid=Camera&Units=English&Groupid=150000&Siteid=150000&DisplayClass=Java&SenType=All"},
 
 {"description": "Greenough Hill", "geo": [46.90820055,-113.422989], "id": "150004", "url": "http://rwis.mdt.mt.gov/scanweb/Camera.asp?Pageid=Camera&Units=English&Groupid=150000&Siteid=150004&DisplayClass=Java&SenType=All"},

 {"description": "Ninemile", "geo": [47.02299397,-114.3886779], "id": "150005", "url": "http://rwis.mdt.mt.gov/scanweb/Camera.asp?Pageid=Camera&Units=English&Groupid=150000&Siteid=150005&DisplayClass=Java&SenType=All"},

 {"description": "Trout Creek", "geo": [47.824111,-115.572], "id": "150003", "url": "http://rwis.mdt.mt.gov/scanweb/Camera.asp?Pageid=Camera&Units=English&Groupid=150000&Siteid=150003&DisplayClass=Java&SenType=All"},

 {"description": "Yellowstone River", "geo": [45.79376126,-108.4679891], "id": "263000", "url": "http://rwis.mdt.mt.gov/scanweb/Camera.asp?Pageid=Camera&Units=English&Groupid=263000&Siteid=263000&DisplayClass=Java&SenType=All"},

 {"description": "Reedpoint", "geo": [45.71005632,-109.5783019], "id": "263001", "url": "http://rwis.mdt.mt.gov/scanweb/Camera.asp?Pageid=Camera&Units=English&Groupid=263000&Siteid=263001&DisplayClass=Java&SenType=All"},

 {"description": "Roscoe Hill", "geo": [45.33857742,-109.4936168], "id": "263002", "url": "http://rwis.mdt.mt.gov/scanweb/Camera.asp?Pageid=Camera&Units=English&Groupid=263000&Siteid=263002&DisplayClass=Java&SenType=All"},

 {"description": "Arrow Creek", "geo": [45.77999929,-108.163406], "id": "263003", "url": "http://rwis.mdt.mt.gov/scanweb/Camera.asp?Pageid=Camera&Units=English&Groupid=263000&Siteid=263003&DisplayClass=Java&SenType=All"},

 {"description": "Aberdeen", "geo": [45.0283938,-107.3172887], "id": "263004", "url": "http://rwis.mdt.mt.gov/scanweb/Camera.asp?Pageid=Camera&Units=English&Groupid=263000&Siteid=263004&DisplayClass=Java&SenType=All"},

 {"description": "Hysham", "geo": [46.1649161,-107.3092735], "id": "263005", "url": "http://rwis.mdt.mt.gov/scanweb/Camera.asp?Pageid=Camera&Units=English&Groupid=263000&Siteid=263005&DisplayClass=Java&SenType=All"},

 {"description": "Monida", "geo": [44.55766953,-112.3136955], "id": "267001", "url": "http://rwis.mdt.mt.gov/scanweb/Camera.asp?Pageid=Camera&Units=English&Groupid=267000&Siteid=267001&DisplayClass=Java&SenType=All"},

 {"description": "MacDonald Pass", "geo": [46.56147997,-112.3093051], "id": "267002", "url": "http://rwis.mdt.mt.gov/scanweb/Camera.asp?Pageid=Camera&Units=English&Groupid=267000&Siteid=267002&DisplayClass=Java&SenType=All"},

 {"description": "Boulder", "geo": [46.32329873,-112.0689089], "id": "267003", "url": "http://rwis.mdt.mt.gov/scanweb/Camera.asp?Pageid=Camera&Units=English&Groupid=267000&Siteid=267003&DisplayClass=Java&SenType=All"},

 {"description": "Garrison", "geo": [46.52361378,-112.8084327], "id": "267004", "url": "http://rwis.mdt.mt.gov/scanweb/Camera.asp?Pageid=Camera&Units=English&Groupid=267000&Siteid=267004&DisplayClass=Java&SenType=All"},

 {"description": "Big Hole Pass", "geo": [45.31544733,-113.3097337], "id": "267005", "url": "http://rwis.mdt.mt.gov/scanweb/Camera.asp?Pageid=Camera&Units=English&Groupid=267000&Siteid=267005&DisplayClass=Java&SenType=All"},

 {"description": "Elk Park", "geo": [46.13589,-112.39799], "id": "267006", "url": "http://rwis.mdt.mt.gov/scanweb/Camera.asp?Pageid=Camera&Units=English&Groupid=267000&Siteid=267006&DisplayClass=Java&SenType=All"},

 {"description": "Avon", "geo": [46.69679,-112.65944], "id": "267007", "url": "http://rwis.mdt.mt.gov/scanweb/Camera.asp?Pageid=Camera&Units=English&Groupid=267000&Siteid=267007&DisplayClass=Java&SenType=All"},

 {"description": "Georgetown Lake", "geo": [46.190806,-113.265306], "id": "267009", "url": "http://rwis.mdt.mt.gov/scanweb/Camera.asp?Pageid=Camera&Units=English&Groupid=267000&Siteid=267009&DisplayClass=Java&SenType=All"},

 {"description": "Homestake", "geo": [45.918889,-112.401944], "id": "267008", "url": "http://rwis.mdt.mt.gov/scanweb/Camera.asp?Pageid=Camera&Units=English&Groupid=267000&Siteid=267008&DisplayClass=Java&SenType=All"},

 {"description": "East of  Denton", "geo": [47.30022671,-109.8511746], "id": "268000", "url": "http://rwis.mdt.mt.gov/scanweb/Camera.asp?Pageid=Camera&Units=English&Groupid=268000&Siteid=268000&DisplayClass=Java&SenType=All"},

{"description": "Judith Gap", "geo": [46.68765404,-109.7502125], "id": "268001", "url": "http://rwis.mdt.mt.gov/scanweb/Camera.asp?Pageid=Camera&Units=English&Groupid=268000&Siteid=268001&DisplayClass=Java&SenType=All"},

 {"description": "Bull Mountain", "geo": [46.24743675,-108.4612106], "id": "268003", "url": "http://rwis.mdt.mt.gov/scanweb/Camera.asp?Pageid=Camera&Units=English&Groupid=268000&Siteid=268003&DisplayClass=Java&SenType=All"},

 {"description": "Hays", "geo": [47.91928257,-108.7261054], "id": "268004", "url": "http://rwis.mdt.mt.gov/scanweb/Camera.asp?Pageid=Camera&Units=English&Groupid=268000&Siteid=268004&DisplayClass=Java&SenType=All"},

 {"description": "Lewistown", "geo": [47.06180057,-109.1844339], "id": "268005", "url": "http://rwis.mdt.mt.gov/scanweb/Camera.asp?Pageid=Camera&Units=English&Groupid=268000&Siteid=268005&DisplayClass=Java&SenType=All"},

 {"description": "Geyser", "geo": [47.242694,-110.469556], "id": "268006", "url": "http://rwis.mdt.mt.gov/scanweb/Camera.asp?Pageid=Camera&Units=English&Groupid=268000&Siteid=268006&DisplayClass=Java&SenType=All"},

 {"description": "Malta", "geo": [47.96112732,-108.3055539], "id": "269000", "url": "http://rwis.mdt.mt.gov/scanweb/Camera.asp?Pageid=Camera&Units=English&Groupid=269000&Siteid=269000&DisplayClass=Java&SenType=All"},

 {"description": "McDonalds", "geo": [48.42732302,-105.4423371], "id": "269001", "url": "http://rwis.mdt.mt.gov/scanweb/Camera.asp?Pageid=Camera&Units=English&Groupid=269000&Siteid=269001&DisplayClass=Java&SenType=All"},
 
 {"description": "Navajo", "geo": [48.8184514,-104.9971444], "id": "269002", "url": "http://rwis.mdt.mt.gov/scanweb/Camera.asp?Pageid=Camera&Units=English&Groupid=269000&Siteid=269002&DisplayClass=Java&SenType=All"},
 
 {"description": "Comertown", "geo": [48.8099966,-104.2528984], "id": "269003", "url": "http://rwis.mdt.mt.gov/scanweb/Camera.asp?Pageid=Camera&Units=English&Groupid=269000&Siteid=269003&DisplayClass=Java&SenType=All"},

 {"description": "US2", "geo": [48.13764491,-104.0468714], "id": "269004", "url": "http://rwis.mdt.mt.gov/scanweb/Camera.asp?Pageid=Camera&Units=English&Groupid=269000&Siteid=269004&DisplayClass=Java&SenType=All"},

 {"description": "Saco", "geo": [48.451389,-107.301667], "id": "269005", "url": "http://rwis.mdt.mt.gov/scanweb/Camera.asp?Pageid=Camera&Units=English&Groupid=269000&Siteid=269005&DisplayClass=Java&SenType=All"},
 
 {"description": "Monarch Canyon", "geo": [47.14289771,-110.8230922], "id": "301000", "url": "http://rwis.mdt.mt.gov/scanweb/Camera.asp?Pageid=Camera&Units=English&Groupid=301000&Siteid=301000&DisplayClass=Java&SenType=All target=_top"},

 {"description": "Pendroy", "geo": [48.07321688,-112.3341821], "id": "301001", "url": "http://rwis.mdt.mt.gov/scanweb/Camera.asp?Pageid=Camera&Units=English&Groupid=301000&Siteid=301001&DisplayClass=Java&SenType=All"},

 {"description": "Bowmans", "geo": [47.29219699,-112.151831], "id": "301002", "url": "http://rwis.mdt.mt.gov/scanweb/Camera.asp?Pageid=Camera&Units=English&Groupid=301000&Siteid=301002&DisplayClass=Java&SenType=All"},

 {"description": "Helmville", "geo": [46.9682615,-112.9748725], "id": "301003", "url": "http://rwis.mdt.mt.gov/scanweb/Camera.asp?Pageid=Camera&Units=English&Groupid=301000&Siteid=301003&DisplayClass=Java&SenType=All"},

 {"description": "Gary Cooper Bridge", "geo": [47.13947959,-111.8590804], "id": "301004", "url": "http://rwis.mdt.mt.gov/scanweb/Camera.asp?Pageid=Camera&Units=English&Groupid=301000&Siteid=301004&DisplayClass=Java&SenType=All"},

 {"description": "Sieben", "geo": [46.88748267,-112.1111196], "id": "301005", "url": "http://rwis.mdt.mt.gov/scanweb/Camera.asp?Pageid=Camera&Units=English&Groupid=301000&Siteid=301005&DisplayClass=Java&SenType=All"},

 {"description": "Prickley Pear", "geo": [46.91392183,-112.1167054], "id": "301006", "url": "http://rwis.mdt.mt.gov/scanweb/Camera.asp?Pageid=Camera&Units=English&Groupid=301000&Siteid=301006&DisplayClass=Java&SenType=All"},

 {"description": "Rogers Pass", "geo": [47.0877,-112.372317], "id": "301007", "url": "http://rwis.mdt.mt.gov/scanweb/Camera.asp?Pageid=Camera&Units=English&Groupid=301000&Siteid=301007&DisplayClass=Java&SenType=All"},

 {"description": "Lufborough", "geo": [47.07813042,-107.5720063], "id": "302000", "url": "http://rwis.mdt.mt.gov/scanweb/Camera.asp?Pageid=Camera&Units=English&Groupid=302000&Siteid=302000&DisplayClass=Java&SenType=All"},

 {"description": "Cow Creek", "geo": [47.68836679,-105.4918552], "id": "302001", "url": "http://rwis.mdt.mt.gov/scanweb/Camera.asp?Pageid=Camera&Units=English&Groupid=302000&Siteid=302001&DisplayClass=Java&SenType=All"},

 {"description": "Lindsay", "geo": [47.28293547,-105.2938704], "id": "302002", "url": "http://rwis.mdt.mt.gov/scanweb/Camera.asp?Pageid=Camera&Units=English&Groupid=302000&Siteid=302002&DisplayClass=Java&SenType=All"},

 {"description": "Beaver Hill", "geo": [47.02197621,-104.3300043], "id": "302003", "url": "http://rwis.mdt.mt.gov/scanweb/Camera.asp?Pageid=Camera&Units=English&Groupid=302000&Siteid=302003&DisplayClass=Java&SenType=All"},

 {"description": "Sioux", "geo": [47.91972733,-104.3261866], "id": "302004", "url": "http://rwis.mdt.mt.gov/scanweb/Camera.asp?Pageid=Camera&Units=English&Groupid=302000&Siteid=302004&DisplayClass=Java&SenType=All"},

 {"description": "Lame Deer", "geo": [45.62885913,-106.5112452], "id": "563000", "url": "http://rwis.mdt.mt.gov/scanweb/Camera.asp?Pageid=Camera&Units=English&Groupid=563000&Siteid=563000&DisplayClass=Java&SenType=All"},
 
 {"description": "Sweeney", "geo": [46.26670992,-106.3078849], "id": "563001", "url": "http://rwis.mdt.mt.gov/scanweb/Camera.asp?Pageid=Camera&Units=English&Groupid=563000&Siteid=563001&DisplayClass=Java&SenType=All"},
 
 {"description": "Rock Springs", "geo": [46.83370217,-106.2713308], "id": "563002", "url": "http://rwis.mdt.mt.gov/scanweb/Camera.asp?Pageid=Camera&Units=English&Groupid=563000&Siteid=563002&DisplayClass=Java&SenType=All"},

 {"description": "Baker", "geo": [46.08358891,-104.4355227], "id": "563003", "url": "http://rwis.mdt.mt.gov/scanweb/Camera.asp?Pageid=Camera&Units=English&Groupid=563000&Siteid=563003&DisplayClass=Java&SenType=All"},
 
 {"description": "Alzada", "geo": [45.00274858,-104.3736231], "id": "563004", "url": "http://rwis.mdt.mt.gov/scanweb/Camera.asp?Pageid=Camera&Units=English&Groupid=563000&Siteid=563004&DisplayClass=Java&SenType=All"},

{"description": "Government Hill", "geo": [46.41,-105.67], "id": "563005", "url": "http://rwis.mdt.mt.gov/scanweb/Camera.asp?Pageid=Camera&Units=English&Groupid=563000&Siteid=563005&DisplayClass=Java&SenType=All"},
 
 {"description": "Ingomar", "geo": [46.583528,-107.376], "id": "563006", "url": "http://rwis.mdt.mt.gov/scanweb/Camera.asp?Pageid=Camera&Units=English&Groupid=563000&Siteid=563006&DisplayClass=Java&SenType=All"},

 {"description": "Ekalaka", "geo": [45.312,-104.46657], "id": "563007", "url": "http://rwis.mdt.mt.gov/scanweb/Camera.asp?Pageid=Camera&Units=English&Groupid=563000&Siteid=563007&DisplayClass=Java&SenType=All"},

 {"description": "Biddle", "geo": [45.012976,-105.376985], "id": "563008", "url": "http://rwis.mdt.mt.gov/scanweb/Camera.asp?Pageid=Camera&Units=English&Groupid=563000&Siteid=563008&DisplayClass=Java&SenType=All"},

 {"description": "Raynolds", "geo": [44.72814115,-111.4701211], "id": "564000", "url": "http://rwis.mdt.mt.gov/scanweb/Camera.asp?Pageid=Camera&Units=English&Groupid=564000&Siteid=564000&DisplayClass=Java&SenType=All"},
 
 {"description": "Karst", "geo": [45.34534328,-111.1726064], "id": "564001", "url": "http://rwis.mdt.mt.gov/scanweb/Camera.asp?Pageid=Camera&Units=English&Groupid=564000&Siteid=564001&DisplayClass=Java&SenType=All"},
 
 {"description": "Bozeman Pass", "geo": [45.66681641,-110.8039548], "id": "564002", "url": "http://rwis.mdt.mt.gov/scanweb/Camera.asp?Pageid=Camera&Units=English&Groupid=564000&Siteid=564002&DisplayClass=Java&SenType=All"},
 
 {"description": "E Livingston", "geo": [45.6855379,-110.5044463], "id": "564003", "url": "http://rwis.mdt.mt.gov/scanweb/Camera.asp?Pageid=Camera&Units=English&Groupid=564000&Siteid=564003&DisplayClass=Java&SenType=All"},
 
 {"description": "Norris Hill", "geo": [45.49959623,-111.6961793], "id": "564004", "url": "http://rwis.mdt.mt.gov/scanweb/Camera.asp?Pageid=Camera&Units=English&Groupid=564000&Siteid=564004&DisplayClass=Java&SenType=All"},
 
 {"description": "Deep Creek", "geo": [46.35146,-111.06681], "id": "564005", "url": "http://rwis.mdt.mt.gov/scanweb/Camera.asp?Pageid=Camera&Units=English&Groupid=564000&Siteid=564005&DisplayClass=Java&SenType=All"},

 {"description": "Essex", "geo": [48.28175578,-113.6065696], "id": "628000", "url": "http://rwis.mdt.mt.gov/scanweb/Camera.asp?Pageid=Camera&Units=English&Groupid=628000&Siteid=628000&DisplayClass=Java&SenType=All"},

 {"description": "Dickey Lake", "geo": [48.69452866,-114.7843654], "id": "628001", "url": "http://rwis.mdt.mt.gov/scanweb/Camera.asp?Pageid=Camera&Units=English&Groupid=628000&Siteid=628001&DisplayClass=Java&SenType=All"},

 {"description": "Flathead", "geo": [48.21907646,-114.2379324], "id": "628002", "url": "http://rwis.mdt.mt.gov/scanweb/Camera.asp?Pageid=Camera&Units=English&Groupid=628000&Siteid=628002&DisplayClass=Java&SenType=All"},

 {"description": "Yaak", "geo": [48.58339724,-115.9840606], "id": "628003", "url": "http://rwis.mdt.mt.gov/scanweb/Camera.asp?Pageid=Camera&Units=English&Groupid=628000&Siteid=628003&DisplayClass=Java&SenType=All"},

 {"description": "Swan Lake", "geo": [47.59102693,-113.7557434], "id": "628005", "url": "http://rwis.mdt.mt.gov/scanweb/Camera.asp?Pageid=Camera&Units=English&Groupid=628000&Siteid=628005&DisplayClass=Java&SenType=All"},

 {"description": "Inverness", "geo": [48.55321455,-110.6482198], "id": "629000", "url": "http://rwis.mdt.mt.gov/scanweb/Camera.asp?Pageid=Camera&Units=English&Groupid=629000&Siteid=629000&DisplayClass=Java&SenType=All"},

 {"description": "Sweetgrass", "geo": [48.96016563,-111.9407131], "id": "629001", "url": "http://rwis.mdt.mt.gov/scanweb/Camera.asp?Pageid=Camera&Units=English&Groupid=629000&Siteid=629001&DisplayClass=Java&SenType=All"},

 {"description": "Two Medicine", "geo": [48.45265138,-113.1950716], "id": "629002", "url": "http://rwis.mdt.mt.gov/scanweb/Camera.asp?Pageid=Camera&Units=English&Groupid=629000&Siteid=629002&DisplayClass=Java&SenType=All"},

 {"description": "Loma", "geo": [47.95102703,-110.5047682], "id": "629003", "url": "http://rwis.mdt.mt.gov/scanweb/Camera.asp?Pageid=Camera&Units=English&Groupid=629000&Siteid=629003&DisplayClass=Java&SenType=All"},
 
 {"description": "Sunburst", "geo": [48.88015,-111.89871], "id": "629004", "url": "http://rwis.mdt.mt.gov/scanweb/Camera.asp?Pageid=Camera&Units=English&Groupid=629000&Siteid=629004&DisplayClass=Java&SenType=All"},

 {"description": "Browning", "geo": [48.53523,-112.98130], "id": "629005", "url": "http://rwis.mdt.mt.gov/scanweb/Camera.asp?Pageid=Camera&Units=English&Groupid=629000&Siteid=629005&DisplayClass=Java&SenType=All"},

 {"description": "Livingston Wind", "geo": [45.64792329,-110.5992737], "id": "564006", "url": "http://rwis.mdt.mt.gov/scanweb/Camera.asp?Pageid=Camera&Units=English&Groupid=564000&Siteid=564006&DisplayClass=Java&SenType=All"}
]

def pull_camera_urls(rwis_url):
    r = session.get(rwis_url)
    out = []
    for el in r.html.find("td.Phantom > a > img"):
        out.append("http://rwis.mdt.mt.gov"+el.attrs["src"])
    return out

def list_cameras():
    for camera in cameras:
        yield {"description": camera["description"], "geo": {"lat": camera["geo"][0], "lon": camera["geo"][1]}, "id": camera["id"], "format": pull_camera_urls(camera["url"])}