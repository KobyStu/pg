import sys
import requests
from bs4 import BeautifulSoup #Určená pro analýzu a zpracování HTML a XML dokumentů. Umožňuje snadné vyhledávání a navigaci v těchto dokumentech, což usnadňuje extrakci dat z webových stránek.

def download_url_and_get_all_hrefs(url):
    """
    Funkce stahne url predanou v parametru url pomoci volani response = requests.get(),
    zkontroluje navratovy kod response.status_code, ktery musi byt 200,
    pokud ano, najdete ve stazenem obsahu stranky response.content vsechny vyskyty
    <a href="url">odkaz</a> a z nich nactete url, ktere vratite jako seznam pomoci return
    """
    hrefs = []
    
    try:
        response = requests.get(url)
        response.raise_for_status()  # Zkontroluje, zda je status kód 200
        
        # Použijeme BeautifulSoup pro analýzu HTML
        soup = BeautifulSoup(response.content, 'html.parser') #Hlavní konstruktor, který vytváří objekt Beautiful Soup z HTML nebo XML kódu.
        
        # Najdeme všechny <a> tagy a extrahujeme href atributy
        for link in soup.find_all('a', href=True): #find_all(tag, attrs): Vrátí seznam všech výskytů daného tagu. Opět můžete filtrovat podle atributů
            hrefs.append(link['href'])
    
    except requests.exceptions.RequestException as e:
        print(f"Chyba při stahování URL: {e}")
    
    return hrefs


if __name__ == "__main__":
    try:
        url = sys.argv[1]
        links = download_url_and_get_all_hrefs(url)
        print(links)  # Vytiskne nalezené odkazy
    except Exception as e:
        print(f"Program skoncil chybou: {e}")