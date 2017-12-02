#!env python3

import json
from datetime import date


items = [
            {
                "secret": False
            },
            {
                "name": ["Evgenia Medvedeva"],
                "twitter": ["jannymedvedeva"],
                "wikiLink": ["https://en.wikipedia.org/wiki/Evgenia_Medvedeva"],
                "secret": "EvgeniaMedvedeva.jpeg"
            },
            {
                "name": ["Patrick Chan"],
                "twitter": ["Pchiddy"],
                "wikiLink": ["https://en.wikipedia.org/wiki/Pathick_Chan"],
                "secret": "PatrickChan.png"
            },
            {
                "name": ["Valentina Marchei", "Ondřej Hotàrek"],
                "twitter": ["valemarchei14", "ondrejhotarek"],
                "wikiLink": ["https://en.wikipedia.org/wiki/Valentina_Marchei", "https://en.wikipedia.org/wiki/Ondřej_Hotàrek"],
                "secret": "Marchei+Hotarek.jpeg"
            },
            {
                "name": ["", ""],
                "twitter": ["", ""],
                "wikiLink": ["", ""],
                "secret": ""
            }
        ]

today = date.today()

if today > date(2017, 12, 24):
    day = 25
else:
    day = today.day

print(json.dumps(items[:day+1]))