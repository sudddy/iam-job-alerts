from . import get_json


def fetch(slug):
    data = get_json(f"https://boards-api.greenhouse.io/v1/boards/{slug}/jobs?content=true")
    return [
        {
            "id": f"greenhouse:{slug}:{j['id']}",
            "title": j["title"],
            "company": slug,
            "location": (j.get("location") or {}).get("name", ""),
            "url": j["absolute_url"],
            "text": j.get("content", ""),
        }
        for j in data["jobs"]
    ]
