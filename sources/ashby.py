from . import get_json


def fetch(slug):
    data = get_json(f"https://api.ashbyhq.com/posting-api/job-board/{slug}")
    return [
        {
            "id": f"ashby:{slug}:{j['id']}",
            "title": j["title"],
            "company": slug,
            "location": ("Remote " if j.get("isRemote") else "") + (j.get("location") or ""),
            "url": j["jobUrl"],
            "text": j.get("descriptionPlain", ""),
        }
        for j in data["jobs"]
    ]
