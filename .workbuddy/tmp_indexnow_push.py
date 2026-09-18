# -*- coding: utf-8 -*-
"""4号站 dongfengevtrucks.com 每日 IndexNow 推送脚本"""
import json
import re
import urllib.request
import sys

SITEMAP = r"C:\Users\69498\WorkBuddy\20260605101515\dongfeng-ev-repo\sitemap.xml"
KEY = "a53caa61-08c9-4988-868e-c1561233ed50"
HOST = "dongfengevtrucks.com"
API = "https://api.indexnow.org/indexnow"

# 1. 解析 sitemap.xml 提取全部 URL
with open(SITEMAP, "r", encoding="utf-8") as f:
    content = f.read()
urls = re.findall(r"<loc>(.*?)</loc>", content)
urls = [u.strip() for u in urls if u.strip()]
print(f"[INFO] 从 sitemap.xml 提取到 {len(urls)} 条 URL")

# 2. 构建 payload 并 POST
payload = {
    "host": HOST,
    "key": KEY,
    "urlList": urls,
    "keyLocation": f"https://{HOST}/{KEY}.txt",
}
data = json.dumps(payload).encode("utf-8")

def post():
    req = urllib.request.Request(
        API,
        data=data,
        headers={
            "Content-Type": "application/json; charset=utf-8",
            "Accept": "application/json",
        },
        method="POST",
    )
    with urllib.request.urlopen(req, timeout=60) as resp:
        return resp.status, resp.read().decode("utf-8", errors="replace")

try:
    status, body = post()
except Exception as e:
    print(f"[RETRY] 首次请求失败: {e}")
    try:
        status, body = post()
    except Exception as e2:
        print(f"[FAIL] 重试仍失败: {e2}")
        sys.exit(1)

print(f"[RESULT] HTTP {status}")
print(f"[BODY] {body[:500]}")
if status in (200, 202):
    print(f"[OK] 推送成功: {len(urls)} 条 URL")
else:
    print(f"[WARN] 非预期返回码: {status}")
    sys.exit(1)
