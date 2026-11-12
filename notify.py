import os
import urllib.parse
import urllib.request


def send(jobs):
    lines = [f"🔐 {len(jobs)} new IAM jobs"]
    lines += [f"{j['title']} - {j['company']} - {j['location']}\n{j['url']}" for j in jobs]
    query = urllib.parse.urlencode(
        {
            "phone": os.environ["CALLMEBOT_PHONE"],
            "apikey": os.environ["CALLMEBOT_APIKEY"],
            "text": "\n\n".join(lines),
        }
    )
    urllib.request.urlopen(f"https://api.callmebot.com/whatsapp.php?{query}", timeout=30).read()
