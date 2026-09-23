# -*- coding: utf-8 -*-
import re, json, os

ROOT = r"C:\Users\69498\WorkBuddy\20260605101515\dongfeng-ev-repo"
BLOG = ROOT + r"\blog"

foreign = [
"algeria-electric-truck-spotlight-te46-port-construction.html",
"egypt-electric-truck-spotlight-kt5j-cairo-giza.html",
"how-long-does-electric-truck-battery-last.html",
"how-much-does-ev-truck-charging-cost-per-km.html",
"kt1d-electric-sweeper-truck-market-outlook-gulf-north-africa.html",
"kt1d-electric-sweeper-truck-municipal-depot-charging.html",
"kt3e-electric-garbage-truck-hotel-resort-waste-collection.html",
"kt3e-electric-garbage-truck-tco-per-tonne.html",
"kt3f-electric-sprinkler-truck-product-deep-dive.html",
"kt5j-electric-delivery-truck-retail-replenishment.html",
"kt5l-electric-cargo-truck-product-deep-dive.html",
"kt5m-electric-box-truck-port-container-yard-transfers.html",
"kt5m-electric-box-truck-urban-depot-charging-strategy.html",
"kt5m-electric-box-truck-zero-emission-zone-compliance.html",
"kt7a-electric-washing-truck-product-deep-dive.html",
"kt7a-electric-washing-truck-tco-per-kilometre.html",
"kta1-electric-dump-truck-asphalt-road-construction.html",
"kta1-electric-dump-truck-cement-plant-raw-material-haulage.html",
"kth3-vs-kt5l-electric-cargo-truck-comparison.html",
"te46-electric-tractor-fleet-operations-shift-planning.html",
"te46-vs-te8l-electric-tractor-terminal-comparison.html",
"te8l-electric-tractor-charging-planning-long-corridors.html",
"te8l-electric-tractor-reefer-cold-chain-line-haul.html",
"te8m-electric-tractor-battery-charging-architecture.html",
"te8m-electric-tractor-steel-scrap-haulage.html",
"te8p-electric-tractor-battery-motor-engineering.html",
"te8p-electric-tractor-heavy-equipment-haulage-permits.html",
"te9l-electric-tractor-driver-route-engineering.html",
"te9l-vs-mercedes-eactros-electric-tractor-comparison.html",
"tz3v-electric-dump-truck-buying-guide-mining-specs.html",
"tz3v-electric-dump-truck-mining-emission-regulations.html",
"tz3z-electric-dump-truck-dam-reservoir-construction.html",
"tz3z-electric-dump-truck-import-guide-latin-america.html",
"tz5e-electric-dump-truck-urban-emission-rules-night-permits.html",
"tz5e-electric-dump-truck-urban-site-fleet-operations.html",
"tz5e-vs-tz3z-electric-dump-truck-urban-comparison.html",
"tz8j-electric-mixer-truck-charging-strategy-batching-plants.html",
"tz8j-electric-mixer-truck-dispatch-fleet-operations.html",
"dominican-republic-electric-truck-spotlight-kt5l.html",
"kth3-electric-cargo-truck-fleet-operations-route-planning.html",
]

typo_pat = re.compile(r"Dongfong|Dongfoto|evtucks|padding:8[^p]|border:1[^p ]")
issues = []
wc = {}
titles = {}
for f in foreign:
    p = os.path.join(BLOG, f)
    if not os.path.exists(p):
        issues.append(f"{f}: MISSING"); continue
    t = open(p, encoding="utf-8").read()
    fn = f[:-5]
    m = re.search(r"<title>(.*?)</title>", t, re.S)
    titles[f] = m.group(1) if m else "?"
    low = (m.group(1) if m else "").lower()
    if "electric truck" not in low and "ev truck" not in low:
        issues.append(f"{f}: keyword missing in title")
    if 'geo.region' not in t:
        issues.append(f"{f}: no geo meta")
    can = re.search(r'canonical" href="https://dongfengevtrucks\.com/blog/([^"]+)"', t)
    if not can or can.group(1) != fn + ".html":
        issues.append(f"{f}: canonical mismatch")
    og = re.search(r'og:image" content="https://dongfengevtrucks\.com(/images/[^"]+)"', t)
    if not og:
        issues.append(f"{f}: no og:image")
    else:
        local = os.path.join(ROOT, og.group(1).lstrip("/"))
        if not os.path.exists(local):
            issues.append(f"{f}: og:image missing file {og.group(1)}")
    nld = 0
    for m2 in re.finditer(r'<script type="application/ld\+json">(.*?)</script>', t, re.S):
        nld += 1
        try: json.loads(m2.group(1))
        except Exception as e: issues.append(f"{f}: JSON-LD parse error")
    if nld == 0:
        issues.append(f"{f}: no JSON-LD")
    if "fenghan-trade.com/" not in t or "sagmoto-trucks.com/" not in t:
        issues.append(f"{f}: Our Network missing")
    # internal link validity
    ok_model = ok_market = False
    for href in re.findall(r'href="\.\./(products/models/[^"]+|markets/[^"]+)"', t):
        if os.path.exists(os.path.join(ROOT, href)):
            if href.startswith("products/models/"): ok_model = True
            else: ok_market = True
        else:
            issues.append(f"{f}: broken internal link {href}")
    if not ok_model: issues.append(f"{f}: no valid model link")
    if not ok_market: issues.append(f"{f}: no valid market link")
    if "<table" not in t: issues.append(f"{f}: no table")
    if "<ul>" not in t and "<ul " not in t: issues.append(f"{f}: no ul")
    mm = typo_pat.search(t)
    if mm: issues.append(f"{f}: typo {mm.group(0)[:30]}")
    b = re.search(r"<body[^>]*>(.*)</body>", t, re.S)
    if b:
        txt = re.sub(r"<script.*?</script>", " ", b.group(1), flags=re.S)
        txt = re.sub(r"<[^>]+>", " ", txt)
        wc[f] = len(re.findall(r"[A-Za-z0-9$%.,'\-]+", txt))

print("=== ISSUES ===")
for i in issues: print(i)
if not issues: print("NONE")
print("\n=== TITLES ===")
for f in foreign: print(f"{wc.get(f,0):5d}  {titles.get(f,'?')[:95]}")
print(f"\nwc min={min(wc.values()) if wc else 0} max={max(wc.values()) if wc else 0}")
