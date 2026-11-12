from . import get_json


def fetch(slug):
    data = get_json(f"https://api.lever.co/v0/postings/{slug}?mode=json")
    return [
        {
            "id": f"lever:{slug}:{j['id']}",
            "title": j["text"],
            "company": slug,
            "location": (j.get("categories") or {}).get("location") or "",
            "url": j["hostedUrl"],
            "text": j.get("descriptionPlain", ""),
        }
        for j in data
    ]
