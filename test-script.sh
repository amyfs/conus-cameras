curl 'https://mass511.com/List/GetData/Cameras' \
-H 'User-Agent: Mozilla/5.0 (X11; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0' \
-H 'Accept: application/json, text/javascript, */*; q=0.01' \
-H 'Accept-Language: en-CA,en-US;q=0.7,en;q=0.3' \
--compressed \
-H 'Referer: https://511ny.org/cctv?start=0&length=10&order%5Bi%5D=0&order%5Bdir%5D=asc' \
-H '__RequestVerificationToken: wEIkxICJeiY1yvleSAzt_QWhugb0JHpdvG4tb7eI7qAOjhgQlmLhcA6AGH0CAaOdqrMjr_oY5cRzSWRV0ppGmWOT70g1' \
-H 'Content-Type: application/json' \
-H 'X-Requested-With: XMLHttpRequest' \
-H 'Cookie: _culture=en; session=session; __RequestVerificationToken=x-oJKZ-mmDU75mM-C1h05mk-ycmT0S2WzEPXNqNbyFw3O4WmLFVf09_yfxHc3A-R53EB6yvnLy_vbglw7ow67qhO6YM1; map=%7B%22selectedLayers%22%3A%5B%22TrafficSpeeds%22%2C%22Incidents%22%2C%22SubIncidentClosures%22%5D%2C%22prevZoom%22%3Anull%2C%22prevLatLng%22%3A%5B%5D%7D' \
-H 'Connection: keep-alive' \
-H 'Pragma: no-cache' \
-H 'Cache-Control: no-cache' \
--data '{
    "draw":1,
    "columns":[
        {"data":"sortId",
        "name":"sortId",
        "searchable":true,
        "orderable":true,
        "search":{
            "value":"",
            "regex":false}
        },
        {"data":"region",
        "name":"region",
        "searchable":true,
        "orderable":false,
        "search":{
            "value":"",
            "regex":false}
        },
        {"data":"county",
        "name":"county",
        "searchable":true,
        "orderable":true,
        "search":{
            "value":"",
            "regex":false}
        },
        {"data":"roadway",
        "name":"roadway",
        "searchable":true,
        "orderable":true,
        "search":{
            "value":"",
            "regex":false}
        },
        {"data":"direction",
        "name":"direction",
        "searchable":true,
        "orderable":true,
        "search":{
            "value":"",
            "regex":false}
        },
        {"data":5,
        "name":"description1",
        "searchable":false,
        "orderable":true,
        "search":{
            "value":"",
            "regex":false}
        },
        {"data":6,
        "name":"",
        "searchable":false,
        "orderable":false,
        "search":{
            "value":"",
            "regex":false}
        }],
        "order":[
            {"column":0,
            "dir":"asc"},
            {"column":2,
            "dir":"asc"}],
        "start":0,
        "length":5000,
        "search":{"value":"","regex":false}}'