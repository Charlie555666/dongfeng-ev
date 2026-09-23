import re, json, os, sys

BLOG = r"C:\Users\69498\WorkBuddy\20260605101515\dongfeng-ev-repo\blog"
IMG = r"C:\Users\69498\WorkBuddy\20260605101515\dongfeng-ev-repo\images"

files = [
"how-long-does-electric-truck-battery-really-last.html",
"how-much-does-electric-dump-truck-cost-china-fob.html",
"johannesburg-gauteng-electric-truck-freight.html",
"lahore-pakistan-electric-delivery-truck-fleet.html",
"guadalajara-mexico-electric-delivery-truck.html",
"cali-colombia-sugar-corridor-electric-truck.html",
"bangkok-thailand-electric-truck-urban-logistics.html",
"almaty-kazakhstan-electric-truck-distribution.html",
"jeddah-saudi-electric-truck-port-logistics.html",
"abu-dhabi-electric-sanitation-fleet.html",
"davao-philippines-agri-electric-truck.html",
"da-nang-vietnam-electric-truck-port-city.html",
"oran-algeria-electric-truck-port-fleet.html",
"takoradi-ghana-manganese-electric-truck.html",
"eldoret-kenya-tea-highlands-electric-truck.html",
"port-harcourt-nigeria-electric-truck-logistics.html",
"mandalay-myanmar-dry-zone-electric-truck.html",
"tanzania-cashew-corridor-electric-truck.html",
"chile-lithium-triangle-electric-heavy-haul.html",
"vietnam-seafood-cold-chain-electric-truck.html",
"johor-data-center-construction-electric-truck.html",
"solar-farm-construction-electric-truck-fleet.html",
"steel-mill-scrap-inbound-electric-truck.html",
"pantograph-opportunity-charging-electric-truck-port.html",
"electric-truck-battery-swap-station-siting.html",
"ev-truck-battery-theft-depot-security.html",
"ev-truck-battery-second-life-mini-grid-storage.html",
"how-to-read-electric-truck-spec-sheet.html",
"green-finance-development-banks-electric-truck-africa.html",
"kenya-electric-mobility-policy-ev-trucks.html",
"nigeria-electric-vehicle-policy-ev-truck-importers.html",
"ev-truck-driver-recruitment-retention.html",
"scaling-electric-truck-fleet-10-to-100.html",
"6x4-vs-8x4-electric-dump-truck-configuration.html",
"tz3z-vs-tz5e-city-dump-truck-choice.html",
"tz3v-andes-altitude-copper-mine-electric-dump.html",
"saudi-aggregates-giga-project-electric-dump-truck.html",
"kt5m-beverage-plant-distribution-electric.html",
"kt1d-waste-transfer-station-electric.html",
"dominican-republic-tourism-construction-electric-truck.html",
]

typo_pat = re.compile(r"Dongfong|Dongfoto|dongfengevtrucks\.co[^m]|dongfengevtrridge|evtucks|padding:8[^p]|border:1[^p ]|LHD\.\.\. rather")
issues = []
wordcounts = {}
for f in files:
    p = os.path.join(BLOG, f)
    if not os.path.exists(p):
        issues.append(f"{f}: MISSING FILE"); continue
    t = open(p, encoding="utf-8").read()
    fn = f[:-5]
    # 1. keyword in title
    m = re.search(r"<title>(.*?)</title>", t, re.S)
    title = m.group(1) if m else ""
    low = (title + t[:3000]).lower()
    if "electric truck" not in low and "ev truck" not in low:
        issues.append(f"{f}: no electric truck/EV truck in title/head")
    # 2. geo meta
    if 'geo.region' not in t or 'geo.placename' not in t:
        issues.append(f"{f}: missing geo meta")
    # 3. canonical matches filename
    can = re.search(r'canonical" href="https://dongfengevtrucks\.com/blog/([^"]+)"', t)
    if not can or can.group(1) != fn + ".html":
        issues.append(f"{f}: canonical mismatch -> {can.group(1) if can else None}")
    # og:url
    ou = re.search(r'og:url" content="https://dongfengevtrucks\.com/blog/([^"]+)"', t)
    if not ou or ou.group(1) != fn + ".html":
        issues.append(f"{f}: og:url mismatch -> {ou.group(1) if ou else None}")
    # 4. og:image exists
    og = re.search(r'og:image" content="https://dongfengevtrucks\.com(/images/[^"]+)"', t)
    if not og:
        issues.append(f"{f}: no og:image")
    else:
        ip = os.path.join(IMG, og.group(1).replace("/images/", "").split("/")[0]) if False else None
        local = os.path.join(r"C:\Users\69498\WorkBuddy\20260605101515\dongfeng-ev-repo", og.group(1).lstrip("/"))
        if not os.path.exists(local):
            issues.append(f"{f}: og:image file missing: {og.group(1)}")
    # 5. JSON-LD parses + url matches
    for m2 in re.finditer(r'<script type="application/ld\+json">(.*?)</script>', t, re.S):
        try:
            d = json.loads(m2.group(1))
            if d.get("@type") == "BlogPosting":
                if not d.get("url","").endswith(fn + ".html"):
                    issues.append(f"{f}: JSON-LD url mismatch: {d.get('url')}")
                if d.get("datePublished") != "2026-09-23":
                    issues.append(f"{f}: datePublished != 2026-09-23")
        except Exception as e:
            issues.append(f"{f}: JSON-LD parse error: {e}")
    # 6. GEO articles need FAQPage schema
    if f in ("how-long-does-electric-truck-battery-really-last.html","how-much-does-electric-dump-truck-cost-china-fob.html"):
        if '"FAQPage"' not in t:
            issues.append(f"{f}: GEO article missing FAQPage schema")
        if "Quick answer:" not in t:
            issues.append(f"{f}: GEO missing Quick answer")
        if "Frequently Asked Questions" not in t:
            issues.append(f"{f}: GEO missing FAQ block")
    # 7. Our Network line
    if "fenghan-trade.com/" not in t or "sagmoto-trucks.com/" not in t:
        issues.append(f"{f}: missing Our Network links")
    # 8. model + market links
    if "products/models/" not in t:
        issues.append(f"{f}: no model link")
    if "markets/" not in t:
        issues.append(f"{f}: no market link")
    # 9. table + ul
    if "<table" not in t:
        issues.append(f"{f}: no table")
    if "<ul>" not in t and "<ul " not in t:
        issues.append(f"{f}: no ul")
    # 10. typos
    mm = typo_pat.search(t)
    if mm:
        issues.append(f"{f}: typo pattern: {mm.group(0)[:40]}")
    # 11. word count body
    b = re.search(r"<body[^>]*>(.*)</body>", t, re.S)
    if b:
        txt = b.group(1)
        txt = re.sub(r"<script.*?</script>", "", txt, flags=re.S)
        txt = re.sub(r"<style.*?</style>", "", txt, flags=re.S)
        txt = re.sub(r"<[^>]+>", " ", txt)
        words = len(re.findall(r"[A-Za-z0-9$%€£¥.,'\-]+", txt))
        wordcounts[f] = words

print("=== ISSUES ===")
if issues:
    for i in issues: print(i)
else:
    print("NONE - all checks passed")
print("\n=== WORD COUNTS (body) ===")
lo = sorted(wordcounts.items(), key=lambda x: x[1])
for k,v in lo[:12]:
    print(f"{v:5d}  {k}")
print(f"\nmin={min(wordcounts.values()) if wordcounts else 0} max={max(wordcounts.values()) if wordcounts else 0} avg={sum(wordcounts.values())/len(wordcounts):.0f}")
print(f"\nfiles checked: {len(files)}")
