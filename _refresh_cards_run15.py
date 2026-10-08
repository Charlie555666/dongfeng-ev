# -*- coding: utf-8 -*-
"""Run 15: refresh the 40 index cards with the new (patched) descriptions."""
import os, re

ROOT = os.path.dirname(os.path.abspath(__file__))
FILES = re.search(r'FILES = """(.*?)""".split\(\)',
                  open(os.path.join(ROOT, '_update_index_run15.py'), encoding='utf-8').read(), re.S).group(1).split()

idx_path = os.path.join(ROOT, 'blog', 'index.html')
idx = open(idx_path, encoding='utf-8').read()

n = 0
for f in FILES:
    h = open(os.path.join(ROOT, 'blog', f + '.html'), encoding='utf-8').read()
    desc = re.search(r'<meta name="description" content="(.*?)">', h).group(1)
    if len(desc) > 120:
        desc = desc[:117].rsplit(' ', 1)[0] + '...'
    pat = re.compile(r'(<li><a href="%s\.html">.*?</a><br><span style="color:#666;font-size:14px;">).*?(</span></li>)' % re.escape(f), re.S)
    assert pat.search(idx), f
    idx = pat.sub(lambda m: m.group(1) + desc + m.group(2), idx, count=1)
    n += 1
open(idx_path, 'w', encoding='utf-8').write(idx)
print('refreshed', n, 'cards')
