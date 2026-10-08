# -*- coding: utf-8 -*-
"""Run 15: prepend 40 cards to blog/index.html, add 40 URLs to sitemap.xml."""
import os, re

ROOT = os.path.dirname(os.path.abspath(__file__))
DATE = "2026-10-08"
FILES = """tema-ghana-port-te46-electric-terminal-tractor
cape-town-south-africa-electric-delivery-truck
abuja-nigeria-electric-truck-government-fleet
hawassa-ethiopia-industrial-park-electric-truck
kisumu-kenya-lake-basin-electric-cargo-truck
algiers-algeria-electric-dump-truck-construction
rabat-morocco-electric-municipal-fleet-kt1d
which-electric-truck-is-best-for-mining-operations
neom-saudi-arabia-electric-construction-fleet
sharjah-uae-electric-waste-collection-kt3e
jubail-saudi-industrial-city-electric-cargo-truck
shymkent-kazakhstan-electric-truck-distribution
fergana-uzbekistan-agri-electric-cargo-truck
sulaymaniyah-iraq-electric-dump-truck-reconstruction
aqaba-jordan-port-electric-tractor
fujairah-uae-port-electric-tractor-bunkering
callao-peru-port-electric-tractor-fleet
iquique-chile-mining-electric-dump-truck
cartagena-colombia-port-electric-cargo-truck
puebla-mexico-automotive-electric-truck-logistics
santiago-dominican-agri-electric-cargo-truck
medan-indonesia-palm-oil-electric-truck
penang-malaysia-electronics-electric-cargo-truck
clark-philippines-logistics-hub-electric-truck
te8m-vs-sany-electric-tractor-comparison
tz3z-vs-foton-electric-dump-truck-comparison
kt5l-vs-jac-electric-cargo-truck-comparison
tz8j-vs-zoomlion-electric-mixer-comparison
te9l-vs-volvo-fh-electric-tractor-comparison
ev-truck-tco-latin-america-country-comparison
ev-truck-charging-peak-shaving-battery-buffer
ev-truck-monsoon-season-operations-guide
peru-electric-truck-import-incentives-policy
ready-mix-plant-electric-mixer-fleet-design
ev-truck-battery-swap-network-central-asia
tanzania-electric-truck-import-guide
quarry-loading-cycle-electric-dump-truck-optimization
electric-truck-uptime-guarantee-service-contract-design
how-much-can-fleets-save-switching-to-electric-trucks
valparaiso-chile-port-electric-tractor""".split()

assert len(FILES) == 40, len(FILES)

# --- blog/index.html ---
idx_path = os.path.join(ROOT, 'blog', 'index.html')
idx = open(idx_path, encoding='utf-8').read()

cards = []
for f in FILES:
    h = open(os.path.join(ROOT, 'blog', f + '.html'), encoding='utf-8').read()
    title = re.search(r'<title>(.*?)</title>', h).group(1)
    desc = re.search(r'<meta name="description" content="(.*?)">', h).group(1)
    if len(desc) > 120:
        desc = desc[:117].rsplit(' ', 1)[0] + '...'
    cards.append('<li><a href="%s.html">%s</a><br><span style="color:#666;font-size:14px;">%s</span></li>' % (f, title, desc))

card_html = '\n'.join(cards)
anchor = '<h2>Latest articles</h2>\n<ul>'
assert anchor in idx, 'index anchor not found'
idx = idx.replace(anchor, anchor + '\n' + card_html, 1)
idx = idx.replace('"dateModified": "2026-09-25"', '"dateModified": "2026-10-08"')
open(idx_path, 'w', encoding='utf-8').write(idx)
print('index.html: prepended', len(cards), 'cards')

# --- sitemap.xml ---
sm_path = os.path.join(ROOT, 'sitemap.xml')
sm = open(sm_path, encoding='utf-8').read()
entries = []
for f in FILES:
    loc = 'https://dongfengevtrucks.com/blog/%s.html' % f
    assert loc not in sm, 'duplicate in sitemap: ' + loc
    entries.append('  <url><loc>%s</loc><lastmod>%s</lastmod><changefreq>monthly</changefreq><priority>0.7</priority></url>' % (loc, DATE))
sm = sm.replace('</urlset>', '\n'.join(entries) + '\n</urlset>')
open(sm_path, 'w', encoding='utf-8').write(sm)

# validate XML
import xml.etree.ElementTree as ET
ET.parse(sm_path)
print('sitemap.xml: added', len(entries), 'URLs, XML valid')
