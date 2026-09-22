import re, json, os, html as ihtml

FILES = """mombasa-kenya-port-electric-truck-corridor
kumasi-ghana-electric-truck-construction-market
kano-ibadan-nigeria-electric-truck-distribution
durban-south-africa-electric-truck-port-fleet
mwanza-tanzania-lake-zone-electric-mining-truck
san-pedro-cote-divoire-timber-electric-truck
barranquilla-colombia-electric-truck-construction
antofagasta-chile-copper-port-electric-truck
cebu-philippines-island-electric-delivery-truck
hai-phong-vietnam-electric-cargo-truck-port
monterrey-mexico-electric-truck-manufacturing-logistics
surabaya-indonesia-electric-truck-municipal-fleet
alexandria-egypt-electric-truck-port-logistics
tashkent-uzbekistan-electric-truck-city-logistics
agadir-morocco-agri-export-electric-truck
cashew-corridor-west-africa-electric-truck
uzbekistan-cotton-corridor-electric-cargo-truck
kalimantan-timber-electric-truck-haulage
west-africa-shea-corridor-electric-truck
thar-pakistan-coal-electric-heavy-haul-truck
ethiopia-coffee-corridor-electric-truck-export
ev-truck-charging-contract-negotiation-guide
ev-truck-driver-incentive-scheme-design
ev-truck-battery-insurance-underwriting-guide
ev-truck-depot-layout-design-queuing
ev-truck-charging-station-operations-maintenance
ev-truck-fleet-change-management-workforce
kt1d-lagos-solid-waste-electric-sweeper
kt3e-santo-domingo-electric-garbage-truck-tender
kt3f-vietnam-quarry-haul-road-dust-control
kt7a-lima-peru-electric-washing-truck
tz8j-riyadh-metro-electric-mixer-concrete
te8p-uzbekistan-copper-heavy-haul-electric
te9l-kazakhstan-cross-border-electric-tractor
te8l-myanmar-yangon-mandalay-electric-corridor
te8m-basra-iraq-electric-truck-reconstruction
kta1-dodoma-tanzania-capital-electric-dump-truck
tz3z-chattogram-bangladesh-electric-dump-truck
kt5l-vs-kt5m-electric-box-truck-comparison
tz5e-jordan-amman-electric-dump-truck-construction""".split()

os.chdir(r"C:\Users\69498\WorkBuddy\20260605101515\dongfeng-ev-repo\blog")
issues = []
for f in FILES:
    fn = f + ".html"
    if not os.path.exists(fn):
        issues.append(f"{fn}: MISSING"); continue
    t = open(fn, encoding="utf-8").read()
    title = re.search(r"<title>(.*?)</title>", t).group(1)
    # keyword in title
    if not re.search(r"EV truck|electric truck", title, re.I):
        issues.append(f"{fn}: keyword missing in title")
    # geo meta
    for g in ['meta name="geo.region"', 'meta name="geo.placename"']:
        if g not in t: issues.append(f"{fn}: missing {g}")
    # canonical
    can = re.search(r'rel="canonical" href="https://dongfengevtrucks\.com/blog/' + f + r'\.html"', t)
    if not can: issues.append(f"{fn}: canonical mismatch")
    # og:image exists
    og = re.search(r'og:image" content="https://dongfengevtrucks\.com(/images/[^"]+)"', t)
    if not og: issues.append(f"{fn}: no og:image")
    elif not os.path.exists(".." + og.group(1)): issues.append(f"{fn}: og:image not on disk {og.group(1)}")
    # JSON-LD
    m = re.search(r'<script type="application/ld\+json">\s*(\{.*?\})\s*</script>', t, re.S)
    if not m: issues.append(f"{fn}: no JSON-LD")
    else:
        try: json.loads(m.group(1))
        except Exception as e: issues.append(f"{fn}: JSON-LD parse error {e}")
    # date
    if '"datePublished": "2026-09-22"' not in t: issues.append(f"{fn}: wrong datePublished")
    # our network
    if "Our Network" not in t: issues.append(f"{fn}: no Our Network line")
    if "fenghan-trade.com" not in t or "sagmoto-trucks.com" not in t: issues.append(f"{fn}: network links incomplete")
    # model + market links
    if "../products/models/" not in t: issues.append(f"{fn}: no model page link")
    if "../markets/" not in t: issues.append(f"{fn}: no market page link")
    # table + ul
    if "<table" not in t: issues.append(f"{fn}: no table")
    if "<ul>" not in t: issues.append(f"{fn}: no ul")
    # first para keyword (text before first h2, after h1)
    body = t.split("<h1>", 1)[1].split("<h2>", 1)[0]
    body_txt = ihtml.unescape(re.sub(r"<[^>]+>", " ", body))
    if not re.search(r"EV truck|electric truck", body_txt, re.I):
        issues.append(f"{fn}: keyword missing in opening")
    # word count of full body text
    b = t.split("<body", 1)[1]
    txt = ihtml.unescape(re.sub(r"<[^>]+>", " ", b))
    txt = re.sub(r"\s+", " ", txt).strip()
    wc = len(txt.split())
    if wc < 1150: issues.append(f"{fn}: word count {wc} < 1150")
    # typos
    for bad in ["Dongfong", "dongfeway", "evtucks", "~ccc", "evtrtrucks", "Dongfoto", "drivetrian", "customsduties"]:
        if bad in t: issues.append(f"{fn}: typo {bad}")
    # stray CJK in body (outside geo placename which is before body)
    bodypart = t.split("<body", 1)[1]
    cjk = re.findall(r"[\u4e00-\u9fff]", bodypart)
    if cjk: issues.append(f"{fn}: CJK chars in body {''.join(cjk)}")
    print(f"{fn}: OK ({wc} words)" if not any(x.startswith(fn) for x in issues) else f"{fn}: see issues")

print()
if issues:
    print("ISSUES:")
    for i in issues: print(" -", i)
else:
    print("ALL 40 PASS")
