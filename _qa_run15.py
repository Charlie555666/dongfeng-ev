# -*- coding: utf-8 -*-
"""Run 15 QA: validate all 40 new articles."""
import os, re

FILES = re.search(r'FILES = """(.*?)""".split\(\)', open('_update_index_run15.py', encoding='utf-8').read(), re.S).group(1).split()
errs = []
for f in FILES:
    p = 'blog/%s.html' % f
    h = open(p, encoding='utf-8').read()
    m = re.search(r'<p><img src="\.\./(images/[^"]+)"', h)
    if not m or not os.path.exists(m.group(1)): errs.append((f, 'img missing'))
    models = re.findall(r'href="\.\./products/models/([a-z0-9-]+\.html)"', h)
    if not models: errs.append((f, 'no model link'))
    for x in models:
        if not os.path.exists('products/models/' + x): errs.append((f, 'dead model link ' + x))
    mkts = re.findall(r'href="\.\./markets/([a-z0-9-]+\.html)"', h)
    if not mkts: errs.append((f, 'no market link'))
    for x in mkts:
        if not os.path.exists('markets/' + x): errs.append((f, 'dead market link ' + x))
    for g in ('geo.region', 'geo.placename'):
        if g not in h: errs.append((f, 'missing ' + g))
    if 'EV truck' not in h and 'electric truck' not in h: errs.append((f, 'no EV truck term'))
    na = set(c for c in h if ord(c) > 127)
    if na: errs.append((f, 'non-ascii: %r' % list(na)[:5]))
    if 'fenghan-trade.com' not in h or 'sagmoto-trucks.com' not in h: errs.append((f, 'missing network links'))
    body = h.split('</h1>', 1)[1] if '</h1>' in h else h
    w = len(re.sub(r'<[^>]+>', ' ', body).split())
    if w < 1150: errs.append((f, 'short body ~%d words' % w))
    if '<table' not in h: errs.append((f, 'no table'))
    if '<ul>' not in h: errs.append((f, 'no ul'))
    d = re.search(r'<meta name="description" content="(.*?)">', h).group(1)
    if not (140 <= len(d) <= 165): errs.append((f, 'desc len %d' % len(d)))
    if 'datePublished": "2026-10-08"' not in h: errs.append((f, 'wrong date'))

for g in ('which-electric-truck-is-best-for-mining-operations', 'how-much-can-fleets-save-switching-to-electric-trucks'):
    h = open('blog/%s.html' % g, encoding='utf-8').read()
    if 'Quick answer:' not in h: errs.append((g, 'no Quick answer'))
    if 'FAQPage' not in h: errs.append((g, 'no FAQPage schema'))
    if 'Frequently Asked Questions' not in h: errs.append((g, 'no FAQ block'))
    if len(re.findall(r'<h2>[^<]*\?', h)) < 3: errs.append((g, 'question h2 < 3'))
    if h.count('<h3>') < 5: errs.append((g, 'faq h3 < 5'))

print('checked', len(FILES), 'files')
if errs:
    for f, e in errs: print('ERR', f, '::', e)
    print('TOTAL ERRORS:', len(errs))
else:
    print('ALL QA PASSED')
