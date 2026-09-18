# -*- coding: utf-8 -*-
"""4号站 dongfengevtrucks.com 每日IndexNow推送"""
import json
import re
import urllib.request

SITEMAP = r"C:\Users\69498\WorkBuddy\20260605101515\dongfeng-ev-repo\sitemap.xml"
API_URL = "https://api.indexnow.org/indexnow"
KEY = "a53caa61-08c9-4988-868e-c1561233ed50"
HOST = "dongfengevtrucks.com"

with open(SITEMAP, "r", encoding="utf-8") as f:
    content = f.read()

urls = re.findall(r"<loc>(.*?)</loc>", content)
urls = [u.strip() for u in urls if u.strip()]
print("URL count:", len(urls))

payload = {
    "host": HOST,
    "key": KEY,
    "urlList": urls,
    "keyLocation": "https://dongfengevtrucks.com/" + KEY + ".txt",
}

data = json.dumps(payload).encode("utf-8")
req = urllib.request.Request(
    API_URL,
    data=data,
    headers={"Content-Type": "application/json", "Accept": "application/json"},
    method="POST",
)

for attempt in (1, 2):
    try:
        with urllib.request.urlopen(req, timeout=30) as resp:
            body = resp.read().decode("utf-8", errors="replace")
            print("Attempt", attempt, "-> HTTP", resp.status)
            print("Response:", body[:500])
            if resp.status in (200, 202):
                print("RESULT: SUCCESS", len(urls), "urls, HTTP", resp.status)
                break
    except urllib.error.HTTPError as e:
        print("Attempt", attempt, "-> HTTP", e.code, e.read().decode("utf-8", errors="replace")[:500])
    except Exception as e:
        print("Attempt", attempt, "-> ERROR:", e)
