import json
import requests
from datetime import datetime
#pamatovat si -> from dateutil import parser

url = "http://www.cnb.cz/cs/financni_trhy/devizovy_trh/kurzy_devizoveho_trhu/denni_kurz.txt"

def stahni_kurzovni_listek(url):
    """
    Stáhne kurzovní listek z webu České národní banky.
    
    Args:
        url (str): URL kurzovního listku.
    
    Returns:
        str: Text kurzovního listku.
    """
    response = requests.get(url)
    return response.text

def parsi_kurzovni_listek(text):
    """
    Parsuje kurzovní listek a vrátí seznam kurzů.
    
    Args:
        text (str): Text kurzovního listku.
    
    Returns:
        list: Seznam kurzů.
    """
    kurzy = []
    for line in text.splitlines()[2:]:
        if line.strip() == "":
            break
        values = line.split("|")
        kurz = {
            "zeme": values[0].strip(),
            "mena": values[1].strip(),
            "mnozstvi": int(values[2].strip()),
            "kod": values[3].strip(),
            "kurz": float(values[4].strip().replace(",", "."))
        }
        kurzy.append(kurz)
    return kurzy

if __name__ == "__main__":
    url = "http://www.cnb.cz/cs/financni_trhy/devizovy_trh/kurzy_devizoveho_trhu/denni_kurz.txt"
    text = stahni_kurzovni_listek(url)
    kurzy = parsi_kurzovni_listek(text)
    datum = datetime.now().strftime("%Y-%m-%d")
    data = {
        "datum": datum,
        "kurzy": kurzy
    }
    with open("kurzovni_listek.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)

# stahnete kurzovni listek v textove podobe a prevedte ho na json: +vypracovat datum kdy vydáváme
# {
#  "datum": "2024-12-20",
#  "kurzy":[  
#     {
#         "zeme": "USA",
#         "mena": "USD",
#         "mnozstvi": 1,
#         "kod": "USD",
#         "kurz": 22.5
#     },
#     ...
# ]
# }
# kurzovni listek je zde: http://www.cnb.cz/cs/financni_trhy/devizovy_trh/kurzy_devizoveho_trhu/denni_kurz.txt