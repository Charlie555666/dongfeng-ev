# -*- coding: utf-8 -*-
"""Run 14: prepend 40 cards to blog/index.html, add 40 URLs to sitemap.xml."""
import os, re

ROOT = os.path.dirname(os.path.abspath(__file__))
DATE = "2026-09-25"
FILES = """san-salvador-el-salvador-electric-dump-truck-construction
tegucigalpa-honduras-electric-cargo-truck-logistics
san-pedro-sula-honduras-electric-delivery-truck
kingston-jamaica-electric-delivery-truck-fleet
port-of-spain-trinidad-electric-port-tractor
yaounde-cameroon-electric-cargo-truck-corridor
lome-togo-electric-truck-port-logistics
cotonou-benin-electric-delivery-truck-fleet
kinshasa-drc-electric-truck-city-logistics
bamako-mali-gold-mining-electric-truck
conakry-guinea-bauxite-electric-mining-truck
ouagadougou-burkina-faso-electric-dump-truck
asuncion-paraguay-electric-cargo-truck-corridor
montevideo-uruguay-electric-truck-renewable-grid
te46-vs-sany-electric-port-tractor-comparison
tz3v-vs-yutong-electric-mining-dump-truck
kt5j-vs-xcmg-light-electric-truck-comparison
te9l-vs-scania-45r-electric-tractor-comparison
ev-truck-insurance-renewal-negotiation-guide
eu-battery-passport-implementation-guide-ev-truck-exporters
ev-truck-charging-roaming-ocpp-network-interoperability
ev-truck-fleet-manager-hiring-org-design
ev-truck-warranty-claims-export-fleet-process
ev-truck-energy-procurement-ppa-fleet-charging
ev-truck-fleet-kpi-dashboard-metrics
uzbekistan-ev-assembly-policy-electric-truck-imports
ev-truck-charging-connector-standards-gbt-ccs2-mcs
kta1-senegal-phosphate-electric-dump-truck
kt9x-egypt-new-capital-electric-mixer
tz8j-kenya-affordable-housing-electric-mixer
te8p-tanzania-sgr-heavy-haul-electric
kth1-pakistan-textile-cargo-electric-truck
kt7a-qatar-lusail-electric-washing-truck
kt3e-vietnam-heritage-cities-electric-sweeper
te9l-mexico-bajio-electric-corridor
tz5e-astana-kazakhstan-electric-dump-truck
tz8j-cycle-time-vs-diesel-mixer-comparison
ethiopia-ice-import-ban-electric-truck-opportunity
how-many-charging-stations-does-an-ev-truck-fleet-need
how-long-does-it-take-to-charge-an-electric-truck""".split()

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
idx = idx.replace('"dateModified": "2026-09-24"', '"dateModified": "2026-09-25"')
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
total = sm.count('<url>')
print('sitemap.xml: +40 URLs, total', total, '- XML valid')
