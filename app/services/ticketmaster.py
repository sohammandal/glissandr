import httpx
from app.config import settings

TM_URL = "https://app.ticketmaster.com/discovery/v2/events"


def fetch_ticketmaster(city: str = "Chicago", size: int = 1):
    params = {
        "apikey": settings.TICKETMASTER_KEY,
        "city": city,
        "classificationName": "music",
        "size": size,
    }
    resp = httpx.get(TM_URL, params=params, timeout=10)
    resp.raise_for_status()
    return resp.json()
