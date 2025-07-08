import os
import httpx


def test_ticketmaster():
    key = os.getenv("TICKETMASTER_KEY")
    assert key, "Missing API key"
    r = httpx.get(
        "https://app.ticketmaster.com/discovery/v2/events",
        params={
            "apikey": key,
            "city": "Chicago",
            "classificationName": "music",
            "size": 1,
        },
        timeout=10,
    )
    assert r.status_code == 200
    assert isinstance(r.json().get("page", {}).get("totalElements"), int)
