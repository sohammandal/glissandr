import requests
from bs4 import BeautifulSoup
from urllib.parse import quote


def get_similar_artists(artist: str) -> list[str]:
    url = f"https://www.music-map.com/{quote(artist)}"
    resp = requests.get(url, headers={"User-Agent": "Mozilla/5.0"}, timeout=10)
    resp.raise_for_status()
    soup = BeautifulSoup(resp.text, "html.parser")
    tags = soup.select("div#gnodMap a.S")
    return [t.text.strip() for t in tags if t.text.strip().lower() != artist.lower()]
