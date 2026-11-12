import hashlib
import json
import sys
from pathlib import Path

import yaml

import notify
from filter import matches
from sources import ashby, greenhouse, lever

SEEN = Path("seen.json")
SOURCES = {"greenhouse": greenhouse, "lever": lever, "ashby": ashby}


def fetch_all():
    jobs = []
    for source, slugs in yaml.safe_load(Path("companies.yaml").read_text()).items():
        for slug in slugs:
            try:
                jobs += SOURCES[source].fetch(slug)
            except Exception as e:
                print(f"skip {source}:{slug}: {e}", file=sys.stderr)
    return jobs


def main():
    first_run = not SEEN.exists()
    seen = set() if first_run else set(json.loads(SEEN.read_text()))
    new = []
    for job in filter(matches, fetch_all()):
        key = hashlib.sha1(job["id"].encode()).hexdigest()
        if key not in seen:
            seen.add(key)
            new.append(job)
    if new and not first_run:
        notify.send(new)
    SEEN.write_text(json.dumps(sorted(seen)))
    print(f"{len(new)} new ({'seeded, not sent' if first_run else 'sent'})")


if __name__ == "__main__":
    main()
