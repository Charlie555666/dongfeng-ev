# -*- coding: utf-8 -*-
"""Genera la version espanola (es/) del sitio Dongfeng EV — lote piloto.
Fuente de verdad del diseno: paginas EN existentes (mismas clases CSS).
Salida: es/**, parchea hreflang + selector de idioma en las paginas EN,
y anade las URLs es al sitemap.xml.
"""
import os, re, io

BASE = os.path.dirname(os.path.abspath(__file__))
SITE = "https://dongfengevtrucks.com"
TODAY = "2026-10-10"

def w(rel, content):
    p = os.path.join(BASE, rel)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with io.open(p, "w", encoding="utf-8", newline="\n") as f:
        f.write(content)
    print("  wrote", rel, len(content))

# ---------------------------------------------------------------- shared chrome
NAV = [
    ("/es/", "Inicio"),
    ("/es/products/electric-tractor.html", "Tractocami\u00f3n El\u00e9ctrico"),
    ("/es/products/electric-dump.html", "Volquete El\u00e9ctrico"),
    ("/es/products/electric-cargo.html", "Cami\u00f3n de Carga"),
    ("/es/products/electric-special.html", "Veh\u00edculos Especiales"),
    ("/es/markets/index.html", "Mercados"),
    ("/es/about-us.html", "Nosotros"),
    ("/es/contact-us.html", "Contacto"),
]

def nav_html(active, en_url="/"):
    li = []
    for href, label in NAV:
        cls = ' class="on"' if href == active else ""
        li.append('<li><a href="%s"%s>%s</a></li>' % (href, cls, label))
    li.append('<li class="lang-switch"><a href="%s" hreflang="en" lang="en">EN</a></li>' % en_url)
    return (
        '<header class="header">\n'
        '  <div class="header-inner">\n'
        '    <a href="/es/" class="logo">DONGFENG<span>EV</span></a>\n'
        '    <div class="mobile-toggle" onclick="document.getElementById(\'mainNav\').classList.toggle(\'open\')"><span></span><span></span><span></span></div>\n'
        '    <nav class="main-nav" id="mainNav">\n  ' + "\n  ".join(li) + '\n</nav>\n'
        '  </div>\n'
        '</header>\n'
    )

FOOTER = '''<footer class="footer">
  <div class="footer-inner">
    <div class="footer-grid">
      <div>
        <h5>Dongfeng EV Export</h5>
        <p style="font-size:14px;color:rgba(255,255,255,0.7);margin-top:8px;">Exportador autorizado de vehiculos comerciales de nueva energia Dongfeng. Tractocamiones, volquetes, camiones de carga y vehiculos especiales electricos a mas de 60 paises.</p>
      </div>
      <div>
        <h5>Productos</h5>
        <ul>
          <li><a href="/es/products/electric-tractor.html">Tractocami\u00f3n El\u00e9ctrico</a></li>
          <li><a href="/es/products/electric-dump.html">Volquete El\u00e9ctrico</a></li>
          <li><a href="/es/products/electric-cargo.html">Cami\u00f3n de Carga El\u00e9ctrico</a></li>
          <li><a href="/es/products/electric-special.html">Veh\u00edculos Especiales</a></li>
        </ul>
      </div>
      <div>
        <h5>Empresa</h5>
        <ul>
          <li><a href="/es/about-us.html">Nosotros</a></li>
          <li><a href="/es/markets/index.html">Mercados</a></li>
          <li><a href="/es/contact-us.html">Contacto</a></li>
        </ul>
      </div>
      <div>
        <h5>Contacto</h5>
        <ul>
          <li>WhatsApp: +86 15319431311</li>
          <li>Email: sales@fenghan-trade.com</li>
          <li>Xi'an, Shaanxi, China</li>
        </ul>
      </div>
    </div>
    <div class="footer-links">
      <h5 style="font-size:15px;color:#fff;margin:0 0 6px 0;">Nuestros otros sitios</h5>
      <p style="font-size:13px;margin:4px 0;"><a href="https://sagmoto-trucks.com/" style="color:rgba(255,255,255,0.75);text-decoration:none;">Sagmoto Trucks (SAGMOTO)</a></p>
      <p style="font-size:13px;margin:4px 0;"><a href="https://www.fenghan-trade.com/" style="color:rgba(255,255,255,0.75);text-decoration:none;">Fenghan Trade (SHACMAN)</a></p>
      <p style="font-size:13px;margin:4px 0;"><a href="https://dongfengevtrucks.com/" style="color:rgba(255,255,255,0.75);text-decoration:none;">English site</a></p>
    </div>
    <div class="footer-bottom">&copy; 2026 Shaanxi Fenghan Trading Co., Ltd. Todos los derechos reservados. | Dongfeng EV Trucks Export</div>
  </div>
</footer>
<script src="/js/whatsapp-float.js" async></script>
'''

WA_LINK = "https://wa.me/8615319431311?text=Hola%2C%20me%20interesan%20los%20camiones%20electricos%20Dongfeng"

def cta_band_es(h2, p):
    return (
        '<div class="cta-band" style="background:linear-gradient(135deg,#006341,#00c853);color:#fff;padding:44px 0;text-align:center;margin-top:40px;">\n'
        '  <div class="section-inner">\n'
        '    <h2 style="margin:0 0 10px;font-size:26px;">' + h2 + '</h2>\n'
        '    <p style="opacity:.9;margin:0 0 18px;">' + p + '</p>\n'
        '    <a class="btn btn-primary" style="background:#fff;color:#006341;font-weight:700;" href="' + WA_LINK + '" target="_blank" rel="noopener">WhatsApp +86 153 1943 1311</a>\n'
        '    &nbsp;<a class="btn btn-outline" style="border-color:#fff;color:#fff;" href="/es/contact-us.html">Escribir un email</a>\n'
        '  </div>\n'
        '</div>\n'
    )

ORG_SCHEMA = '''{"@context":"https://schema.org","@type":"Organization","@id":"https://dongfengevtrucks.com/#organization","name":"Shaanxi Fenghan Trading Co., Ltd","alternateName":["Fenghan Trading","Dongfeng EV Export"],"url":"https://dongfengevtrucks.com/","logo":"https://dongfengevtrucks.com/images/hero-cover.jpg","description":"Exportador autorizado de camiones de nueva energia Dongfeng y camiones pesados SAGMOTO (SHACMAN) desde Xi'an, China.","address":{"@type":"PostalAddress","streetAddress":"Room 603A, Floor 6, Building B, Chanba Free Trade Center","addressLocality":"Xi'an","addressRegion":"Shaanxi","postalCode":"710000","addressCountry":"CN"},"contactPoint":{"@type":"ContactPoint","telephone":"+86-15319431311","email":"sales@fenghan-trade.com","contactType":"sales","availableLanguage":["Spanish","English","Chinese","Russian","French"]},"sameAs":["https://www.fenghan-trade.com/","https://sagmoto-trucks.com/","https://dongfengevtrucks.com/","https://www.wikidata.org/wiki/Q141531675"],"knowsAbout":["camiones electricos Dongfeng","camiones SAGMOTO","camiones SHACMAN","vehiculos comerciales de nueva energia","baterias CATL","exportacion de camiones desde China"],"areaServed":["America Latina","Caribe","Africa","Medio Oriente","Sudeste Asiatico","Asia Central","Europa"]}'''

def faq_schema_es(pairs):
    items = []
    for q, a in pairs:
        items.append('{"@type":"Question","name":%s,"acceptedAnswer":{"@type":"Answer","text":%s}}' % (json_str(q), json_str(a)))
    return '{"@context":"https://schema.org","@type":"FAQPage","inLanguage":"es","mainEntity":[' + ",".join(items) + ']}'

def json_str(s):
    import json
    return json.dumps(s, ensure_ascii=False)

def faq_html_es(pairs, heading="Preguntas frecuentes"):
    out = ['<div class="section-title" style="margin-top:28px;"><h2>' + heading + '</h2></div>']
    for q, a in pairs:
        out.append('<div class="faq-item"><h4>' + q + '</h4><p>' + a + '</p></div>')
    return "\n".join(out)

def page(es_rel, en_rel, title, desc, kw, body, extra_schema="", active="", hero=None):
    """hero = (h1, sub) para paginas internas; si es None se asume home."""
    es_url = SITE + "/" + es_rel
    if es_rel == "es/index.html":
        es_url = SITE + "/es/"
    en_url = SITE + "/" + en_rel
    if en_rel == "index.html":
        en_url = SITE + "/"
    head = ['<!DOCTYPE html>', '<html lang="es">', '<head>', '<meta charset="UTF-8">',
            '<meta name="viewport" content="width=device-width, initial-scale=1.0">',
            '<meta name="description" content="%s">' % desc,
            '<meta name="keywords" content="%s">' % kw,
            '<meta name="robots" content="index, follow, max-image-preview:large">',
            '<meta property="og:title" content="%s">' % title,
            '<meta property="og:description" content="%s">' % desc,
            '<meta property="og:type" content="website">',
            '<meta property="og:url" content="%s">' % es_url,
            '<meta property="og:image" content="https://dongfengevtrucks.com/images/hero-tractor.jpg">',
            '<meta property="og:site_name" content="Dongfeng EV Trucks Export">',
            '<meta property="og:locale" content="es_ES">',
            '<meta name="twitter:card" content="summary_large_image">',
            '<link rel="canonical" href="%s">' % es_url,
            '<link rel="alternate" hreflang="es" href="%s">' % es_url,
            '<link rel="alternate" hreflang="en" href="%s">' % en_url,
            '<link rel="alternate" hreflang="x-default" href="%s">' % en_url,
            '<link rel="stylesheet" href="/css/dongfeng-ev.css">',
            '<link rel="icon" href="/favicon.ico" type="image/x-icon">',
            '<title>%s</title>' % title,
            '<script type="application/ld+json">' + ORG_SCHEMA + '</script>']
    if extra_schema:
        head.append('<script type="application/ld+json">' + extra_schema + '</script>')
    head.append('<style>\n.page-hero-sm{background:linear-gradient(135deg,#0a1f2e,#006341);color:#fff;padding:56px 0 44px;}\n'
                '.page-hero-sm .bc{font-size:13px;opacity:.75;margin-bottom:10px;}\n'
                '.page-hero-sm .bc a{color:#fff;text-decoration:none;}\n'
                '.page-hero-sm h1{font-size:34px;margin:0 0 8px;}\n'
                '.page-hero-sm p{opacity:.85;max-width:820px;}\n'
                '.spec-tbl{width:100%;border-collapse:collapse;margin:18px 0;font-size:15px;}\n'
                '.spec-tbl td{padding:10px 14px;border-bottom:1px solid #e5e9f0;}\n'
                '.spec-tbl td:first-child{width:34%;font-weight:600;color:var(--primary);background:#f4f8f6;}\n'
                'ul.tick{list-style:none;padding:0;}\n'
                'ul.tick li{padding:6px 0 6px 26px;position:relative;}\n'
                'ul.tick li:before{content:"\\2713";position:absolute;left:0;color:var(--accent);font-weight:700;}\n'
                '.prod-card{border:1px solid #e5e9f0;border-radius:12px;padding:18px;margin:10px 0;}\n'
                '.main-nav li.lang-switch a{font-weight:800;color:var(--primary);}\n'
                '.main-nav li.on > a{color:var(--primary);}\n'
                '</style>')
    head.append('</head>')
    head.append('<body>')
    head.append(nav_html(active, en_url))
    head.append(body)
    head.append(FOOTER)
    head.append('</body>')
    head.append('</html>')
    return "\n".join(head)
