# -*- coding: utf-8 -*-
import re, os

ROOT = r"C:\Users\69498\WorkBuddy\20260605101515\dongfeng-ev-repo"
BLOG = ROOT + r"\blog"

FOREIGN = [
"algeria-electric-truck-spotlight-te46-port-construction.html",
"egypt-electric-truck-spotlight-kt5j-cairo-giza.html",
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
"tz8j-electric-mixer-truck-charging-strategy-batching-plants.html",
"tz8j-electric-mixer-truck-dispatch-fleet-operations.html",
"dominican-republic-electric-truck-spotlight-kt5l.html",
"kth3-electric-cargo-truck-fleet-operations-route-planning.html",
]

cards = []
sm_entries = []
for fn in FOREIGN:
    p = os.path.join(BLOG, fn)
    t = open(p, encoding="utf-8").read()
    m = re.search(r"<title>(.*?)</title>", t, re.S)
    title = m.group(1).strip() if m else fn
    m2 = re.search(r'<meta name="description" content="([^"]+)"', t)
    desc = m2.group(1).strip() if m2 else ""
    cards.append(f'<li><a href="{fn}">{title}</a><br><span style="color:#666;font-size:14px;">{desc}</span></li>')
    sm_entries.append(f'  <url><loc>https://dongfengevtrucks.com/blog/{fn}</loc><lastmod>2026-09-23</lastmod><changefreq>monthly</changefreq><priority>0.7</priority></url>')

# --- index.html: insert after my run's last card ---
idx = BLOG + r"\index.html"
t = open(idx, encoding="utf-8").read()
anchor_card = 'href="dominican-republic-tourism-construction-electric-truck.html"'
pos = t.find(anchor_card)
assert pos > 0, "my last card not found"
line_end = t.find("</li>", pos)
assert line_end > 0
insert_at = line_end + len("</li>")
block = "\n" + "\n".join(cards)
t = t[:insert_at] + block + t[insert_at:]
open(idx, "w", encoding="utf-8", newline="\n").write(t)
print(f"index.html: {len(cards)} foreign cards inserted after this run's 40")

# --- sitemap ---
sm = ROOT + r"\sitemap.xml"
s = open(sm, encoding="utf-8").read()
s = s.replace("</urlset>", "\n".join(sm_entries) + "\n</urlset>", 1)
open(sm, "w", encoding="utf-8", newline="\n").write(s)
import xml.etree.ElementTree as ET
ET.parse(sm)
print(f"sitemap.xml: {len(sm_entries)} URLs added, total {s.count('<url>')} <url> entries, XML OK")
