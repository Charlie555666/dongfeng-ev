# -*- coding: utf-8 -*-
"""Run 14 QA: verify all 40 new articles meet spec."""
import os, re, json, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
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

GEO = {'how-many-charging-stations-does-an-ev-truck-fleet-need', 'how-long-does-it-take-to-charge-an-electric-truck'}
errors = []
for f in FILES:
    p = os.path.join(ROOT, 'blog', f + '.html')
    if not os.path.exists(p):
        errors.append(f + ': FILE MISSING'); continue
    h = open(p, encoding='utf-8').read()
    low = h.lower()
    text = re.sub(r'<[^>]+>', ' ', h)
    words = len(text.split())
    if words < 1200: errors.append(f + f': words {words} < 1200')
    if 'geo.region' not in h or 'geo.placename' not in h: errors.append(f + ': geo meta missing')
    if ('electric truck' not in low.split('</h1>')[0]) and ('ev truck' not in low.split('</h1>')[0]):
        first_para = low[:low.find('</p>', low.find('</h1>'))]
        if 'electric truck' not in first_para and 'ev truck' not in first_para:
            errors.append(f + ': no EV keyword in title/first para')
    if f'rel="canonical" href="https://dongfengevtrucks.com/blog/{f}.html"' not in h: errors.append(f + ': canonical mismatch')
    if f'og:url" content="https://dongfengevtrucks.com/blog/{f}.html"' not in h: errors.append(f + ': og:url mismatch')
    m = re.search(r'og:image" content="https://dongfengevtrucks\.com/images/([^"]+)"', h)
    if not m: errors.append(f + ': og:image missing')
    elif not os.path.exists(os.path.join(ROOT, 'images', m.group(1))): errors.append(f + ': og:image not on disk -> ' + m.group(1))
    if 'Our Network' not in h or 'fenghan-trade.com' not in h or 'sagmoto-trucks.com' not in h: errors.append(f + ': Our Network line issue')
    for block in re.findall(r'<script type="application/ld\+json">(.*?)</script>', h, re.S):
        try: json.loads(block)
        except Exception as e: errors.append(f + ': JSON-LD parse error ' + str(e)[:60])
    if h.count('<table') < 1: errors.append(f + ': no table')
    if h.count('<ul>') < 1: errors.append(f + ': no ul')
    if 'products/models/' not in h: errors.append(f + ': no model page link')
    else:
        for mm in re.findall(r'products/models/([a-z0-9-]+\.html)', h):
            if not os.path.exists(os.path.join(ROOT, 'products', 'models', mm)): errors.append(f + ': dead model link ' + mm)
    if 'markets/' not in h: errors.append(f + ': no market page link')
    else:
        for mm in re.findall(r'markets/([a-z0-9-]+\.html)', h):
            if not os.path.exists(os.path.join(ROOT, 'markets', mm)): errors.append(f + ': dead market link ' + mm)
    if '2026-09-25' not in h: errors.append(f + ': date missing')
    if f in GEO:
        if 'Quick answer:' not in h: errors.append(f + ': GEO missing Quick answer')
        if 'Frequently Asked Questions' not in h: errors.append(f + ': GEO missing FAQ block')
        if 'FAQPage' not in h: errors.append(f + ': GEO missing FAQPage schema')
        q_h2 = len(re.findall(r'<h2>[^<]*\?', h))
        if q_h2 < 3: errors.append(f + f': only {q_h2} question H2s')
        if h.count('<h3>') < 5: errors.append(f + ': fewer than 5 FAQ h3')
    for bad in ['Dongfong', 'Dongfoto', 'padding:848', 'padding:8:', 'dongfengevtrtrucks', 'evtucks', 'border:1.0']:
        if bad in h: errors.append(f + ': typo ' + bad)

print('QA checked', len(FILES), 'articles')
if errors:
    print('ERRORS:'); [print(' -', e) for e in errors]; sys.exit(1)
print('ALL CHECKS PASSED')
