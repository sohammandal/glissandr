# 🎧 Glissandr

> A personal concert-recommender agent that finds shows you'd actually want to attend

Glissandr aggregates upcoming concerts from multiple free data sources (Ticketmaster, Bandsintown etc.), enriches them with artist similarity data and will soon recommend events matched to your music taste - with daily delivery via Telegram or a simple web dashboard

This project is being built iteratively as a full-stack agentic AI system using modern Python tools

---

## Tech Stack

- FastAPI
- Docker
- uv
- Pytest
- Ruff + Pre-commit
- CrewAI (using OpenAI models)
- Streamlit / Telegram (UI)

---

## Local Development

1. Install [uv](https://github.com/astral-sh/uv):
    ```bash
    curl -LsSf https://astral.sh/uv/install.sh | sh
    ```

2. Create a `.env` file (see `.env.example`)

3. Run the app:

    ```bash
    docker compose -f docker/docker-compose.yml up --build
    ```

4. Run tests:

   ```bash
   uv run pytest -v
   ```

---

## Project Structure

```
glissandr/
├── app/                  # FastAPI app code
│   ├── __init__.py
│   ├── config.py         # App settings (via .env)
│   ├── main.py           # App entrypoint
│   └── services/         # External API fetchers (e.g. Ticketmaster)
├── docker/               # Docker setup
│   ├── Dockerfile
│   └── docker-compose.yml
├── tests/                # Test suite
│   └── api_smoke/        # API integration tests
├── uv.lock               # Locked dependencies
├── pyproject.toml        # Project and dev config
├── README.md
├── LICENSE

```

---

## Agentic AI (coming soon)

Glissandr will use **CrewAI agents** for:

* Data fetching
* Taste profiling (via Spotify)
* Event recommendation scoring
* Natural-language explanation
* Digest scheduling and delivery

---

## License

MIT © Soham Mandal