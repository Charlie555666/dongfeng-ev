# -*- coding: utf-8 -*-
import os, re, io, glob, sys
BASE = os.path.abspath(os.path.dirname(__file__))
os.chdir(BASE)

es_files = sorted(glob.glob('es/**/*.html', recursive=True))
print("ES pages:", len(es_files))
bad_links, missing = [], {}
for f in es_files:
    rel = f.replace(os.sep, '/')
    h = io.open(f, encoding='utf-8').read()
    can = re.search(r'<link rel="canonical" href="([^"]+)"', h)
    hl = re.findall(r'<link rel="alternate" hreflang="([^"]+)" href="([^"]+)"', h)
    if not can or can.group(1) != 'https://dongfengevtrucks.com/' + rel:
        missing.setdefault('canonical', []).append((rel, can.group(1) if can else None))
    if len(hl) != 3:
        missing.setdefault('hreflang', []).append((rel, hl))
    if 'lang="es"' not in h:
        missing.setdefault('lang', []).append(rel)
    if '@type":"FAQPage' not in h and 'FAQPage' not in h:
        missing.setdefault('nofaq', []).append(rel)
    for m in re.finditer(r'href="(/[^"#?]*)"', h):
        u = m.group(1)
        if u.startswith('/es/'):
            t = u.lstrip('/')
            if u.endswith('/'):
                t += 'index.html'
            if not os.path.exists(t):
                bad_links.append((rel, u))
        elif u.startswith(('/images/', '/css/', '/js/')):
            if not os.path.exists(u.lstrip('/')):
                bad_links.append((rel, u))
    for m in re.finditer(r'src="(/[^"]*)"', h):
        u = m.group(1)
        if u.startswith('/') and not os.path.exists(u.lstrip('/')):
            bad_links.append((rel, u))

print("issues:", {k: len(v) for k, v in missing.items()})
for k, v in missing.items():
    for x in v[:6]:
        print("   ", k, x)
print("broken refs:", len(set(bad_links)))
for x in sorted(set(bad_links))[:25]:
    print("   ", x)

print("--- EN patch check ---")
for f in ['index.html', 'products/electric-tractor.html', 'products/models/te46-electric-tractor.html',
          'markets/chile.html', 'markets/index.html', 'about-us.html', 'contact-us.html']:
    h = io.open(f, encoding='utf-8').read()
    can = re.search(r'<link rel="canonical" href="([^"]+)"', h).group(1)
    print("  %-46s hreflang_en=%s hreflang_es=%s switch=%s lang=%s" % (
        f, 'hreflang="en"' in h, 'hreflang="es"' in h, 'lang-switch' in h, re.search(r'<html lang="([a-z]+)"', h).group(1)))
    print("      canonical:", can)

s = io.open('sitemap.xml', encoding='utf-8').read()
print("sitemap locs:", s.count('<loc>'), "| es locs:", len(re.findall(r'<loc>https://dongfengevtrucks.com/es/', s)))
print("sitemap xhtml ns:", 'xmlns:xhtml' in s, "| xhtml:link count:", s.count('xhtml:link'))
