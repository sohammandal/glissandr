from app.services.musicmap import get_similar_artists


def test_musicmap():
    artists = get_similar_artists("Kygo")
    assert isinstance(artists, list)
    assert len(artists) >= 5
