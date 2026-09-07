#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Generate Dongfeng EV export site (Site #4)"""
import os, shutil

BASE = os.path.dirname(os.path.abspath(__file__))

def mkdir(p):
    os.makedirs(os.path.join(BASE, p), exist_ok=True)

def write(path, content):
    with open(os.path.join(BASE, path), 'w', encoding='utf-8') as f:
        f.write(content)

# ── Move selected images ──
mkdir('images')
src = os.path.join(BASE, 'images', 'web')
dst = os.path.join(BASE, 'images')
selection = {
    'p01_00.jpg': 'hero-cover.jpg',
    'p04_09.jpg': 'hero-tractor.jpg',
    'p05_20.jpg': 'hero-cargo.jpg',
    'p12_50.jpg': 'cat-dump.jpg',
    'p13_52.jpg': 'cat-dump2.jpg',
    'p15_62.jpg': 'cat-special.jpg',
    'p16_64.jpg': 'cat-mixer.jpg',
}
for s, d in selection.items():
    sp = os.path.join(src, s)
    dp = os.path.join(dst, d)
    if os.path.exists(sp):
        shutil.copy2(sp, dp)

# ── CSS ──
css = r"""/* Dongfeng EV Export Site — Site #4 */
:root {
  --primary: #006341;
  --accent: #00c853;
  --dark: #0a1f2e;
  --text: #1a1a2e;
  --muted: #5a6578;
  --bg: #f8fafc;
  --card: #ffffff;
  --radius: 12px;
  --shadow: 0 4px 24px rgba(0,0,0,0.08);
  --shadow-hover: 0 12px 40px rgba(0,0,0,0.14);
}
* { box-sizing: border-box; margin:0; padding:0; }
html { scroll-behavior: smooth; }
body {
  font-family: 'Segoe UI', system-ui, -apple-system, sans-serif;
  color: var(--text);
  background: var(--bg);
  line-height: 1.6;
}
img { max-width:100%; height:auto; display:block; }
a { color: var(--primary); text-decoration:none; }

/* Header */
.header {
  position: sticky; top:0; z-index:1000;
  background: rgba(255,255,255,0.95);
  backdrop-filter: blur(10px);
  border-bottom: 1px solid rgba(0,0,0,0.06);
}
.header-inner {
  max-width: 1280px; margin:0 auto; padding: 0 24px;
  display:flex; align-items:center; justify-content:space-between; height:72px;
}
.logo { font-size: 22px; font-weight:800; color: var(--primary); letter-spacing:-0.5px; }
.logo span { color: var(--accent); }
.main-nav { display:flex; gap:28px; list-style:none; }
.main-nav a { font-size:14px; font-weight:600; color: var(--text); transition: color .2s; }
.main-nav a:hover { color: var(--primary); }
.mobile-toggle { display:none; flex-direction:column; gap:5px; cursor:pointer; }
.mobile-toggle span { display:block; width:24px; height:2px; background: var(--text); }

@media(max-width:900px){
  .main-nav { display:none; position:absolute; top:72px; left:0; right:0; background:#fff; flex-direction:column; padding:16px 24px; gap:12px; box-shadow: var(--shadow); }
  .main-nav.open { display:flex; }
  .mobile-toggle { display:flex; }
}

/* Hero */
.hero {
  position:relative; min-height: 80vh; display:flex; align-items:center;
  background: var(--dark) url('../images/hero-tractor.jpg') center/cover no-repeat;
}
.hero::before {
  content:''; position:absolute; inset:0;
  background: linear-gradient(90deg, rgba(10,31,46,0.88) 0%, rgba(10,31,46,0.4) 100%);
}
.hero-inner { position:relative; z-index:1; max-width:1280px; margin:0 auto; padding: 80px 24px; width:100%; }
.hero h1 { font-size: clamp(32px,5vw,56px); color:#fff; line-height:1.15; font-weight:800; max-width:700px; }
.hero p { color:rgba(255,255,255,0.85); font-size: clamp(16px,2vw,20px); max-width:620px; margin-top:16px; }
.hero-btns { margin-top:32px; display:flex; gap:16px; flex-wrap:wrap; }
.btn {
  display:inline-flex; align-items:center; gap:8px; padding:14px 28px; border-radius:8px;
  font-weight:700; font-size:15px; transition: transform .15s, box-shadow .2s;
}
.btn-primary { background: var(--accent); color:#fff; box-shadow: 0 4px 16px rgba(0,200,83,0.35); }
.btn-primary:hover { transform: translateY(-2px); box-shadow: 0 8px 24px rgba(0,200,83,0.45); }
.btn-outline { background: transparent; color:#fff; border: 2px solid rgba(255,255,255,0.5); }
.btn-outline:hover { border-color:#fff; }

/* Sections */
.section { padding: 80px 24px; }
.section-inner { max-width:1280px; margin:0 auto; }
.section-title { font-size: clamp(26px,3vw,36px); font-weight:800; color: var(--dark); margin-bottom:12px; }
.section-sub { color: var(--muted); font-size:17px; max-width:640px; margin-bottom:48px; }

/* Cards */
.card-grid { display:grid; grid-template-columns: repeat(auto-fit, minmax(260px,1fr)); gap:24px; }
.card {
  background: var(--card); border-radius: var(--radius); overflow:hidden;
  box-shadow: var(--shadow); transition: transform .2s, box-shadow .2s;
  display:flex; flex-direction:column;
}
.card:hover { transform: translateY(-6px); box-shadow: var(--shadow-hover); }
.card-img { height:200px; object-fit:cover; width:100%; }
.card-body { padding:24px; flex:1; display:flex; flex-direction:column; }
.card-body h3 { font-size:20px; margin-bottom:8px; }
.card-body p { color: var(--muted); font-size:14px; flex:1; }
.card-body .btn { margin-top:16px; align-self:flex-start; padding:10px 20px; font-size:13px; }

/* Value props */
.value-grid { display:grid; grid-template-columns: repeat(auto-fit, minmax(220px,1fr)); gap:28px; }
.value-item { text-align:center; padding:32px 20px; background: var(--card); border-radius: var(--radius); box-shadow: var(--shadow); }
.value-item .num { font-size:40px; font-weight:800; color: var(--accent); line-height:1; }
.value-item h4 { margin-top:12px; font-size:18px; }
.value-item p { color: var(--muted); font-size:14px; margin-top:6px; }

/* FAQ */
.faq-item { background: var(--card); border-radius: var(--radius); padding:24px; margin-bottom:16px; box-shadow: var(--shadow); }
.faq-item h4 { font-size:17px; margin-bottom:8px; }
.faq-item p { color: var(--muted); font-size:14px; }

/* Product table */
.spec-table { width:100%; border-collapse: collapse; margin-top:24px; font-size:14px; }
.spec-table th, .spec-table td { padding:12px 16px; text-align:left; border-bottom:1px solid #e8ecf1; }
.spec-table th { background: #f1f5f9; font-weight:700; color: var(--dark); }
.spec-table tr:hover td { background: #f8fafc; }

/* Contact */
.contact-grid { display:grid; grid-template-columns: repeat(auto-fit, minmax(260px,1fr)); gap:24px; }
.contact-card { background: var(--card); border-radius: var(--radius); padding:28px; box-shadow: var(--shadow); }
.contact-card h4 { font-size:18px; margin-bottom:8px; }
.contact-card p { color: var(--muted); font-size:14px; }

/* Footer */
.footer { background: var(--dark); color:rgba(255,255,255,0.7); padding: 48px 24px 24px; margin-top:60px; }
.footer-inner { max-width:1280px; margin:0 auto; }
.footer-grid { display:grid; grid-template-columns: repeat(auto-fit, minmax(200px,1fr)); gap:32px; margin-bottom:32px; }
.footer-grid h5 { color:#fff; font-size:16px; margin-bottom:16px; }
.footer-grid ul { list-style:none; }
.footer-grid li { margin-bottom:8px; font-size:14px; }
.footer-grid a { color:rgba(255,255,255,0.7); }
.footer-grid a:hover { color:#fff; }
.footer-bottom { border-top:1px solid rgba(255,255,255,0.1); padding-top:20px; font-size:13px; text-align:center; }

/* Breadcrumb */
.breadcrumb { font-size:13px; color: var(--muted); margin-bottom:24px; }
.breadcrumb a { color: var(--muted); }
.breadcrumb a:hover { color: var(--primary); }

/* Tag */
.tag { display:inline-block; padding:4px 10px; border-radius:20px; background: #e8f5e9; color: var(--primary); font-size:12px; font-weight:700; margin-bottom:10px; }
"""
write('css/dongfeng-ev.css', css)

# ── Shared fragments ──
NAV = """<nav class="main-nav" id="mainNav">
  <li><a href="index.html">Home</a></li>
  <li><a href="products/electric-tractor.html">Electric Tractor</a></li>
  <li><a href="products/electric-dump.html">Electric Dump</a></li>
  <li><a href="products/electric-cargo.html">Electric Cargo</a></li>
  <li><a href="products/electric-special.html">Electric Special</a></li>
  <li><a href="blog/index.html">Blog</a></li>
  <li><a href="about-us.html">About Us</a></li>
  <li><a href="contact-us.html">Contact</a></li>
</nav>"""

HEADER = lambda rel="": f"""<header class="header">
  <div class="header-inner">
    <a href="{rel}index.html" class="logo">DONGFENG<span>EV</span></a>
    <div class="mobile-toggle" onclick="document.getElementById('mainNav').classList.toggle('open')"><span></span><span></span><span></span></div>
    {NAV.replace('href="', 'href="'+rel).replace('href="'+rel+'products/', 'href="'+rel+'products/')}
  </div>
</header>"""

FOOTER = lambda rel="": f"""<footer class="footer">
  <div class="footer-inner">
    <div class="footer-grid">
      <div>
        <h5>Dongfeng EV Export</h5>
        <p style="font-size:14px;color:rgba(255,255,255,0.7);margin-top:8px;">Authorized Dongfeng new energy commercial vehicle exporter. Supplying electric tractors, dump trucks, cargo trucks and special vehicles to 60+ countries.</p>
      </div>
      <div>
        <h5>Products</h5>
        <ul>
          <li><a href="{rel}products/electric-tractor.html">Electric Tractor</a></li>
          <li><a href="{rel}products/electric-dump.html">Electric Dump Truck</a></li>
          <li><a href="{rel}products/electric-cargo.html">Electric Cargo Truck</a></li>
          <li><a href="{rel}products/electric-special.html">Electric Special Vehicle</a></li>
        </ul>
      </div>
      <div>
        <h5>Company</h5>
        <ul>
          <li><a href="{rel}about-us.html">About Us</a></li>
          <li><a href="{rel}faq.html">FAQ</a></li>
          <li><a href="{rel}contact-us.html">Contact Us</a></li>
        </ul>
      </div>
      <div>
        <h5>Contact</h5>
        <ul>
          <li>WhatsApp: +86 15319431311</li>
          <li>Email: sales@fenghan-trade.com</li>
          <li>Xi'an, Shaanxi, China</li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">&copy; {2026} Shaanxi Fenghan Trading Co., Ltd. All rights reserved. | Dongfeng EV Trucks Export</div>
  </div>
</footer>"""

SCHEMA_ORG = """{
  "@context": "https://schema.org",
  "@type": "Organization",
  "name": "Shaanxi Fenghan Trading Co., Ltd",
  "alternateName": "Dongfeng EV Export",
  "url": "https://dongfeng-ev.fenghan-trade.com/",
  "logo": "https://dongfeng-ev.fenghan-trade.com/images/hero-cover.jpg",
  "description": "Authorized Dongfeng new energy commercial vehicle exporter. Electric tractors, dump trucks, cargo trucks and special vehicles.",
  "address": {
    "@type": "PostalAddress",
    "streetAddress": "Room 603A, Floor 6, Building B, Chanba Free Trade Center",
    "addressLocality": "Xi'an",
    "addressRegion": "Shaanxi",
    "postalCode": "710000",
    "addressCountry": "CN"
  },
  "contactPoint": {
    "@type": "ContactPoint",
    "telephone": "+86-15319431311",
    "email": "sales@fenghan-trade.com",
    "contactType": "sales",
    "availableLanguage": ["English", "Chinese", "Russian"]
  },
  "sameAs": ["https://www.fenghan-trade.com/"]
}"""

SCHEMA_WEBSITE = """{
  "@context": "https://schema.org",
  "@type": "WebSite",
  "name": "Dongfeng EV Trucks Export",
  "url": "https://dongfeng-ev.fenghan-trade.com/",
  "description": "Authorized Dongfeng new energy commercial vehicle exporter. Electric tractors, dump trucks, cargo trucks and special vehicles.",
  "inLanguage": "en",
  "publisher": { "@type": "Organization", "name": "Shaanxi Fenghan Trading Co., Ltd" }
}"""

def page(title, desc, keywords, body, rel="", extra_schema=""):
    canonical = f"https://dongfeng-ev.fenghan-trade.com/{rel}".rstrip("/") + "/"
    og_title = title.split("|")[0].strip()
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="description" content="{desc}">
<meta name="keywords" content="{keywords}">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta name="geo.region" content="CN"/>
<meta name="geo.placename" content="Xi'an, Shaanxi, China"/>
<meta name="geo.position" content="34.3416;108.9398"/>
<meta name="ICBM" content="34.3416, 108.9398"/>
<meta property="og:title" content="{og_title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:url" content="{canonical}">
<meta property="og:image" content="https://dongfeng-ev.fenghan-trade.com/images/hero-tractor.jpg">
<meta property="og:site_name" content="Dongfeng EV Trucks Export">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{og_title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="https://dongfeng-ev.fenghan-trade.com/images/hero-tractor.jpg">
<link rel="canonical" href="{canonical}">
<link rel="alternate" hreflang="x-default" href="https://dongfeng-ev.fenghan-trade.com/">
<link rel="alternate" hreflang="en" href="https://dongfeng-ev.fenghan-trade.com/">
<link rel="stylesheet" href="{rel}css/dongfeng-ev.css">
<link rel="icon" href="{rel}favicon.ico" type="image/x-icon">
<title>{title}</title>
<script type="application/ld+json">{SCHEMA_ORG}</script>
<script type="application/ld+json">{SCHEMA_WEBSITE}</script>
{extra_schema}
</head>
<body>
{HEADER(rel)}
<main>
{body}
</main>
{FOOTER(rel)}
</body>
</html>"""

# ── index.html ──
index_body = """
<section class="hero" style="background-image:url('images/hero-tractor.jpg');">
  <div class="hero-inner">
    <h1>Dongfeng New Energy Commercial Vehicles — Electric Trucks for Global Export</h1>
    <p>Authorized exporter of Dongfeng electric tractors, dump trucks, cargo trucks and special vehicles. CATL batteries, LvKong motors, charging &amp; swap-ready. Serving Africa, Middle East, Southeast Asia, Europe and Latin America.</p>
    <div class="hero-btns">
      <a href="products/electric-tractor.html" class="btn btn-primary">Explore Products</a>
      <a href="contact-us.html" class="btn btn-outline">Request a Quote</a>
    </div>
  </div>
</section>

<section class="section" style="background:#fff;">
  <div class="section-inner">
    <h2 class="section-title">Electric Truck Categories</h2>
    <p class="section-sub">Four product lines built on Dongfeng's KL / KR / KC platforms — engineered for zero-emission logistics, mining, municipal and long-haul applications.</p>
    <div class="card-grid">
      <div class="card">
        <img src="images/hero-tractor.jpg" alt="Dongfeng Electric Tractor Truck" class="card-img" loading="lazy">
        <div class="card-body">
          <h3>Electric Tractor Trucks</h3>
          <p>4x2 and 6x4 electric prime movers with CATL 400–600 kWh batteries. TE46 / TE8L / TE9L / TE8M / TE8P series. Up to 707 hp, 120 t GCW.</p>
          <a href="products/electric-tractor.html" class="btn btn-primary">View Models</a>
        </div>
      </div>
      <div class="card">
        <img src="images/cat-dump.jpg" alt="Dongfeng Electric Dump Truck" class="card-img" loading="lazy">
        <div class="card-body">
          <h3>Electric Dump Trucks</h3>
          <p>Heavy-duty electric tippers for mining and construction. 6x4 and 8x4 with 352–600 kWh packs. TZ3Z / TZ5E / TZ3V / TZ5Y RHD.</p>
          <a href="products/electric-dump.html" class="btn btn-primary">View Models</a>
        </div>
      </div>
      <div class="card">
        <img src="images/hero-cargo.jpg" alt="Dongfeng Electric Cargo Truck" class="card-img" loading="lazy">
        <div class="card-body">
          <h3>Electric Cargo Trucks</h3>
          <p>Urban and regional distribution EVs with 262–400 kWh. Box, flatbed and livestock configurations. KT5M / KT5J / KTH3.</p>
          <a href="products/electric-cargo.html" class="btn btn-primary">View Models</a>
        </div>
      </div>
      <div class="card">
        <img src="images/cat-special.jpg" alt="Dongfeng Electric Special Vehicle" class="card-img" loading="lazy">
        <div class="card-body">
          <h3>Electric Special Vehicles</h3>
          <p>Sanitation, mixer, sprinkler and garbage trucks. KT3F / KT1D / TZ8J / KT9X. WVTA GSR2 compliant options available.</p>
          <a href="products/electric-special.html" class="btn btn-primary">View Models</a>
        </div>
      </div>
    </div>
  </div>
</section>

<section class="section">
  <div class="section-inner">
    <h2 class="section-title">Why Partner With Us</h2>
    <p class="section-sub">End-to-end export solutions from factory gate to your port.</p>
    <div class="value-grid">
      <div class="value-item">
        <div class="num">20+</div>
        <h4>Years Export Experience</h4>
        <p>Deep expertise in African, Middle Eastern, Southeast Asian and Latin American markets.</p>
      </div>
      <div class="value-item">
        <div class="num">60+</div>
        <h4>Countries Served</h4>
        <p>Full after-sales and parts support network covering Russia, Nigeria, UAE, Peru, Vietnam and more.</p>
      </div>
      <div class="value-item">
        <div class="num">600</div>
        <h4>kWh Max Battery</h4>
        <p>CATL lithium-iron-phosphate packs with 8-year / 4500-cycle warranty and dual-gun fast charging.</p>
      </div>
      <div class="value-item">
        <div class="num">RHD</div>
        <h4>Right-Hand Drive</h4>
        <p>TE9Y, TEAY, TZ4Y and TZ5Y models available in right-hand drive for Commonwealth markets.</p>
      </div>
    </div>
  </div>
</section>

<section class="section" style="background:#fff;">
  <div class="section-inner">
    <h2 class="section-title">Frequently Asked Questions</h2>
    <p class="section-sub">Quick answers to common buyer questions.</p>
    <div class="faq-item">
      <h4>Which charging standard do you support?</h4>
      <p>We offer both GB/T (China standard) and CCS2 (European standard) charging interfaces. Dual-gun 500–600 A fast charging is standard on most models, delivering 20–80% SOC in ~40 minutes.</p>
    </div>
    <div class="faq-item">
      <h4>Can you supply right-hand drive (RHD) electric trucks?</h4>
      <p>Yes. TE9Y, TEAY, TZ4Y and TZ5Y are purpose-built RHD variants for Nigeria, Kenya, South Africa, Australia, India and other right-hand traffic markets.</p>
    </div>
    <div class="faq-item">
      <h4>What is the typical delivery time and shipping method?</h4>
      <p>Standard configuration: 20–25 days production lead time. We ship primarily by sea (RoRo, bulk carrier or container). 30% T/T deposit, 70% before shipment or against B/L copy.</p>
    </div>
    <div class="faq-item">
      <h4>Do you offer swap-battery models?</h4>
      <p>Yes. Select dump and engineering models support CATL standard swap batteries for fleet operators requiring 24/7 uptime.</p>
    </div>
    <div style="margin-top:24px;"><a href="faq.html" class="btn btn-primary">View All FAQs</a></div>
  </div>
</section>
"""
write('index.html', page(
    "Dongfeng EV Trucks — New Energy Commercial Vehicle Export | Fenghan Trading",
    "Authorized Dongfeng electric truck exporter. Buy electric tractor, dump, cargo and special trucks with CATL batteries. Export to Africa, Middle East, Southeast Asia, Europe.",
    "Dongfeng electric truck, Dongfeng EV, Dongfeng new energy commercial vehicle, Dongfeng electric tractor, Dongfeng electric dump truck, Dongfeng electric cargo truck, Dongfeng EV export, China electric truck factory, CATL battery truck, buy electric truck from China, Dongfeng TE8L, Dongfeng TE9L, Dongfeng TZ3Z, Dongfeng KT5M, electric truck Africa, electric truck Middle East, Fenghan Trading",
    index_body
))

# ── Product pages ──

# Electric Tractor
tractor_body = """
<div class="section" style="background: linear-gradient(180deg,#0a1f2e 0%,#0d2b3f 100%); color:#fff; padding:60px 24px 40px;">
  <div class="section-inner">
    <div class="breadcrumb"><a href="../index.html">Home</a> &rsaquo; Electric Tractor Trucks</div>
    <h1 style="font-size:clamp(28px,4vw,44px);font-weight:800;">Electric Tractor Trucks</h1>
    <p style="color:rgba(255,255,255,0.8);max-width:700px;margin-top:12px;">Dongfeng KL MAX platform electric prime movers. LvKong PMSM motors, CATL LFP batteries, 4-speed AMT. Configurations from 4x2 urban distribution to 6x4 heavy-haul mining tractors.</p>
  </div>
</div>

<div class="section" style="background:#fff;">
  <div class="section-inner">
    <h2 class="section-title">4x2 Light-Duty Tractor</h2>
    <div class="card-grid" style="margin-bottom:48px;">
      <div class="card">
        <div class="card-body">
          <span class="tag">GB/T Charging</span>
          <h3>TE46</h3>
          <p>KL MAX cab, 4x2, 42 t GCW. CATL 400 kWh, LvKong 315/510 kW motor, 4AMT. EBS+ESC, LDWS+FCWS, LED headlights, air-suspended cab. Ideal for port and urban logistics.</p>
        </div>
      </div>
      <div class="card">
        <div class="card-body">
          <span class="tag">CCS2 / Euro</span>
          <h3>TE4Z</h3>
          <p>KL MAX cab, 4x2, 42 t GCW. CATL 400 kWh, LvKong 315/510 kW motor, 4AMT. CCS2 charging for European compliance. Same chassis and comfort as TE46.</p>
        </div>
      </div>
    </div>

    <h2 class="section-title">6x4 Heavy-Duty Tractor</h2>
    <div class="card-grid" style="margin-bottom:48px;">
      <div class="card">
        <div class="card-body">
          <span class="tag">Lightweight</span>
          <h3>TE9L</h3>
          <p>KL MAX cab, 6x4, 49 t GCW. CATL 400/497/600 kWh options. LvKong 350/520 kW. 4AMT, DF601S/DF162E axles. 600 A dual-gun fast charge. Best-in-class weight reduction.</p>
        </div>
      </div>
      <div class="card">
        <div class="card-body">
          <span class="tag">Heavy Load</span>
          <h3>TE8M</h3>
          <p>KL MAX cab, 6x4, 80 t GCW. CATL 466/497/600 kWh. LvKong 400/550 kW. Reinforced 300x90x8+6 frame, DF701S/DF485 axles. For coal and ore transport.</p>
        </div>
      </div>
      <div class="card">
        <div class="card-body">
          <span class="tag">Ultra Heavy</span>
          <h3>TE8P</h3>
          <p>KL MAX cab, 6x4, 120 t GCW. CATL 400/600 kWh. LvKong 400/550 kW. 9/13 parabolic suspension, DF300H rear axle, 12.00R20 tyres. Maximum pulling power for extreme loads.</p>
        </div>
      </div>
      <div class="card">
        <div class="card-body">
          <span class="tag">RHD</span>
          <h3>TE9Y</h3>
          <p>KL MAX cab, 6x4, right-hand drive. CATL 600 kWh, LvKong 400/550 kW. Built for Nigeria, Kenya, South Africa, Australia and other RHD markets.</p>
        </div>
      </div>
      <div class="card">
        <div class="card-body">
          <span class="tag">RHD Heavy</span>
          <h3>TEAY</h3>
          <p>KL MAX cab, 6x4 RHD, heavy haul. CATL 400 kWh, LvKong 400/550 kW. Same reinforced chassis as TE8M, mirrored for right-hand traffic.</p>
        </div>
      </div>
    </div>

    <h2 class="section-title">Technical Specifications Summary</h2>
    <table class="spec-table">
      <tr><th>Model</th><th>Drive</th><th>Battery</th><th>Motor</th><th>GCW</th><th>Charging</th></tr>
      <tr><td>TE46</td><td>4x2</td><td>CATL 400 kWh</td><td>LvKong 315/510 kW</td><td>42 t</td><td>GB/T dual 500 A</td></tr>
      <tr><td>TE4Z</td><td>4x2</td><td>CATL 400 kWh</td><td>LvKong 315/510 kW</td><td>42 t</td><td>CCS2 dual 500 A</td></tr>
      <tr><td>TE8L</td><td>6x4</td><td>CATL 400/466/600 kWh</td><td>LvKong 315/510 kW</td><td>49 t</td><td>GB/T</td></tr>
      <tr><td>TE8K</td><td>6x4</td><td>CATL 466/600 kWh</td><td>LvKong 315/510 kW</td><td>49 t</td><td>CCS2</td></tr>
      <tr><td>TE9L</td><td>6x4</td><td>CATL 400/497/600 kWh</td><td>LvKong 350/520 kW</td><td>49 t</td><td>GB/T dual 600 A</td></tr>
      <tr><td>TE9B</td><td>6x4</td><td>CATL 400/497/600 kWh</td><td>LvKong 350/520 kW</td><td>65 t</td><td>GB/T dual 600 A</td></tr>
      <tr><td>TE8M</td><td>6x4</td><td>CATL 466/497/600 kWh</td><td>LvKong 400/550 kW</td><td>80 t</td><td>GB/T dual 600 A</td></tr>
      <tr><td>TE8P</td><td>6x4</td><td>CATL 400/600 kWh</td><td>LvKong 400/550 kW</td><td>120 t</td><td>GB/T dual 600 A</td></tr>
      <tr><td>TE9Y</td><td>6x4 RHD</td><td>CATL 600 kWh</td><td>LvKong 400/550 kW</td><td>—</td><td>GB/T</td></tr>
      <tr><td>TEAY</td><td>6x4 RHD</td><td>CATL 400 kWh</td><td>LvKong 400/550 kW</td><td>—</td><td>GB/T</td></tr>
    </table>
  </div>
</div>
"""
write('products/electric-tractor.html', page(
    "Electric Tractor Trucks | Dongfeng EV Export — TE46 TE8L TE9L TE8M TE8P TE9Y",
    "Dongfeng electric tractor trucks: TE46, TE8L, TE9L, TE8M, TE8P, TE9Y RHD. CATL 400–600 kWh, LvKong motors, 4AMT. Export to Africa, Middle East, Europe.",
    "Dongfeng electric tractor, Dongfeng EV tractor, TE46, TE8L, TE9L, TE8M, TE8P, TE9Y, electric prime mover, electric semi truck, CATL battery tractor, LvKong motor, 4x2 electric tractor, 6x4 electric tractor, RHD electric tractor, buy electric tractor China",
    tractor_body, rel="../"
))

# Electric Dump
dump_body = """
<div class="section" style="background: linear-gradient(180deg,#0a1f2e 0%,#0d2b3f 100%); color:#fff; padding:60px 24px 40px;">
  <div class="section-inner">
    <div class="breadcrumb"><a href="../index.html">Home</a> &rsaquo; Electric Dump Trucks</div>
    <h1 style="font-size:clamp(28px,4vw,44px);font-weight:800;">Electric Dump Trucks</h1>
    <p style="color:rgba(255,255,255,0.8);max-width:700px;margin-top:12px;">Zero-emission tippers for mining, quarry and construction. 6x4 and 8x4 platforms with reinforced frames, high-torque LvKong motors and swap-battery options.</p>
  </div>
</div>

<div class="section" style="background:#fff;">
  <div class="section-inner">
    <h2 class="section-title">6x4 Dump Truck</h2>
    <div class="card-grid" style="margin-bottom:48px;">
      <div class="card">
        <div class="card-body">
          <span class="tag">Mining</span>
          <h3>TZ5E</h3>
          <p>KC PRO cab, 6x4, 65 t GCW. CATL 400 kWh, LvKong 315/510 kW, 4AMT. 10/13 suspension, DF901S/HDZ300 axles. Reinforced 8+8+4+10 frame for quarry haul.</p>
        </div>
      </div>
    </div>

    <h2 class="section-title">8x4 Dump Truck</h2>
    <div class="card-grid" style="margin-bottom:48px;">
      <div class="card">
        <div class="card-body">
          <span class="tag">Standard</span>
          <h3>TZ3Z</h3>
          <p>KC PRO cab, 8x4, 55 t GCW. CATL 400 kWh, LvKong 315/510 kW, 4AMT. DF601S/HDZ300 axles. Versatile for urban construction and sand/stone transport.</p>
        </div>
      </div>
      <div class="card">
        <div class="card-body">
          <span class="tag">Heavy</span>
          <h3>TZ3V</h3>
          <p>KC PRO cab, 8x4, 80 t GCW. CATL 600 kWh, LvKong 400/550 kW. 10/10/13 suspension, HDZ300 rear axle. Maximum payload for open-pit mining.</p>
        </div>
      </div>
      <div class="card">
        <div class="card-body">
          <span class="tag">RHD</span>
          <h3>TZ4Y</h3>
          <p>KC PRO D320KC RHD cab, 8x4, 55 t GCW. CATL 600 kWh, LvKong 350/520 kW. CCS2 charging for European and Commonwealth compliance.</p>
        </div>
      </div>
      <div class="card">
        <div class="card-body">
          <span class="tag">RHD Heavy</span>
          <h3>TZ5Y</h3>
          <p>KC PRO D320KC RHD, 8x4, 80 t GCW. CATL 600 kWh, LvKong 400/550 kW. 12.00R24 tyres, 10/10/13 suspension. Built for heavy-duty RHD markets.</p>
        </div>
      </div>
    </div>

    <h2 class="section-title">Specifications</h2>
    <table class="spec-table">
      <tr><th>Model</th><th>Drive</th><th>Battery</th><th>Motor</th><th>GCW</th><th>Suspension</th></tr>
      <tr><td>TZ5E</td><td>6x4</td><td>CATL 400 kWh</td><td>LvKong 315/510 kW</td><td>65 t</td><td>10/13</td></tr>
      <tr><td>TZ3Z</td><td>8x4</td><td>CATL 400 kWh</td><td>LvKong 315/510 kW</td><td>55 t</td><td>9/9/13</td></tr>
      <tr><td>TZ4Y</td><td>8x4 RHD</td><td>CATL 600 kWh</td><td>LvKong 350/520 kW</td><td>55 t</td><td>9/9/13</td></tr>
      <tr><td>TZ3V</td><td>8x4</td><td>CATL 600 kWh</td><td>LvKong 400/550 kW</td><td>80 t</td><td>10/10/13</td></tr>
      <tr><td>TZ5Y</td><td>8x4 RHD</td><td>CATL 600 kWh</td><td>LvKong 400/550 kW</td><td>80 t</td><td>10/10/13</td></tr>
    </table>
  </div>
</div>
"""
write('products/electric-dump.html', page(
    "Electric Dump Trucks | Dongfeng EV Export — TZ3Z TZ5E TZ3V TZ4Y TZ5Y",
    "Dongfeng electric dump trucks: TZ3Z, TZ5E, TZ3V, TZ4Y RHD, TZ5Y RHD. 6x4 and 8x4 with CATL 400–600 kWh. Mining and construction zero-emission tippers.",
    "Dongfeng electric dump truck, Dongfeng EV dumper, TZ3Z, TZ5E, TZ3V, TZ4Y, TZ5Y, electric tipper truck, electric mining truck, CATL dump truck, 8x4 electric dump, RHD electric dump, buy electric dump truck China",
    dump_body, rel="../"
))

# Electric Cargo
cargo_body = """
<div class="section" style="background: linear-gradient(180deg,#0a1f2e 0%,#0d2b3f 100%); color:#fff; padding:60px 24px 40px;">
  <div class="section-inner">
    <div class="breadcrumb"><a href="../index.html">Home</a> &rsaquo; Electric Cargo Trucks</div>
    <h1 style="font-size:clamp(28px,4vw,44px);font-weight:800;">Electric Cargo Trucks</h1>
    <p style="color:rgba(255,255,255,0.8);max-width:700px;margin-top:12px;">Urban and regional distribution EVs with LvKong e-axle drive, CATL 262–400 kWh batteries and box volumes up to 65–70 m³. Low TCO for fleet operators.</p>
  </div>
</div>

<div class="section" style="background:#fff;">
  <div class="section-inner">
    <h2 class="section-title">4x2 Distribution Trucks</h2>
    <div class="card-grid" style="margin-bottom:48px;">
      <div class="card">
        <div class="card-body">
          <span class="tag">Box / Flatbed</span>
          <h3>KT5M / KT5J</h3>
          <p>KR D560e cab, 4x2, 18 t GCW. CATL 262/310 kWh, LvKong 150/270 kW e-axle. 4-speed e-axle transmission. 6800–9800 mm body lengths. For urban logistics and regional delivery.</p>
        </div>
      </div>
      <div class="card">
        <div class="card-body">
          <span class="tag">Long Body</span>
          <h3>KT5L / KTH3</h3>
          <p>KR D560e cab, 4x2. CATL 348/400 kWh, LvKong 450 kW. 9800 mm max body length. 65–70 m³ box volume. Ideal for express and bulk goods transport.</p>
        </div>
      </div>
      <div class="card">
        <div class="card-body">
          <span class="tag">Livestock / Feed</span>
          <h3>KTH1 / KTH2 / KTH3</h3>
          <p>Multi-purpose cargo chassis for livestock, feed and refrigerated bodies. CATL 264–400 kWh, LvKong 450 kW. Flexible upfit configurations.</p>
        </div>
      </div>
    </div>

    <h2 class="section-title">Specifications</h2>
    <table class="spec-table">
      <tr><th>Model</th><th>Body</th><th>Battery</th><th>Motor</th><th>GCW</th><th>Volume</th></tr>
      <tr><td>KT5M / KT5J</td><td>Box/Flatbed</td><td>CATL 262/310 kWh</td><td>LvKong 150/270 kW</td><td>18 t</td><td>65 m³</td></tr>
      <tr><td>KT5L</td><td>Box</td><td>CATL 348 kWh</td><td>LvKong 450 kW</td><td>18 t</td><td>65–70 m³</td></tr>
      <tr><td>KTH3</td><td>Box/Flatbed</td><td>CATL 400 kWh</td><td>LvKong 450 kW</td><td>18 t</td><td>70 m³</td></tr>
      <tr><td>KTH1/KTH2</td><td>Livestock/Feed</td><td>CATL 264/352/400 kWh</td><td>LvKong 450 kW</td><td>18 t</td><td>—</td></tr>
    </table>
  </div>
</div>
"""
write('products/electric-cargo.html', page(
    "Electric Cargo Trucks | Dongfeng EV Export — KT5M KT5J KTH3",
    "Dongfeng electric cargo trucks: KT5M, KT5J, KTH3. 4x2 urban distribution with CATL 262–400 kWh, LvKong e-axle. Box volume up to 70 m³. Export to Africa, Southeast Asia.",
    "Dongfeng electric cargo truck, Dongfeng EV cargo, KT5M, KT5J, KTH3, electric box truck, electric delivery truck, electric logistics truck, CATL cargo truck, 4x2 electric truck, buy electric cargo truck China",
    cargo_body, rel="../"
))

# Electric Special
special_body = """
<div class="section" style="background: linear-gradient(180deg,#0a1f2e 0%,#0d2b3f 100%); color:#fff; padding:60px 24px 40px;">
  <div class="section-inner">
    <div class="breadcrumb"><a href="../index.html">Home</a> &rsaquo; Electric Special Vehicles</div>
    <h1 style="font-size:clamp(28px,4vw,44px);font-weight:800;">Electric Special Vehicles</h1>
    <p style="color:rgba(255,255,255,0.8);max-width:700px;margin-top:12px;">Municipal sanitation and construction-specialized EVs. Sprinklers, sweepers, garbage trucks and concrete mixers with zero emissions and low noise.</p>
  </div>
</div>

<div class="section" style="background:#fff;">
  <div class="section-inner">
    <h2 class="section-title">Sanitation Trucks</h2>
    <div class="card-grid" style="margin-bottom:48px;">
      <div class="card">
        <div class="card-body">
          <span class="tag">Sprinkler</span>
          <h3>KT3F</h3>
          <p>KR cab, 4x2, 18 t GCW. CATL 166/200 kWh, LvKong 128/260 kW. Water tank sprinkler with electric pump drive. Motor-direct or 4AMT.</p>
        </div>
      </div>
      <div class="card">
        <div class="card-body">
          <span class="tag">Sweeper</span>
          <h3>KT1D</h3>
          <p>KR cab, 4x2, 18 t GCW. CATL 232/266 kWh, LvKong 128/260 kW. Road sweeper with vacuum and water-spray system. Low noise for city centers.</p>
        </div>
      </div>
      <div class="card">
        <div class="card-body">
          <span class="tag">Garbage</span>
          <h3>KT3E / KT3Y / KT4Y</h3>
          <p>KR cab, 4x2, 18 t GCW. CATL 166–262 kWh, LvKong 110–156 kW. Rear-loading garbage compactor. KT3Y/KT4Y available with CCS2 for Europe.</p>
        </div>
      </div>
      <div class="card">
        <div class="card-body">
          <span class="tag">Heavy Sprinkler</span>
          <h3>KT7A</h3>
          <p>KR cab, 6x4, 25 t GCW. CATL 232 kWh, LvKong 164/308 kW. Large-capacity road washing and dust suppression for highways and mines.</p>
        </div>
      </div>
    </div>

    <h2 class="section-title">Mixer & Refuse Trucks</h2>
    <div class="card-grid" style="margin-bottom:48px;">
      <div class="card">
        <div class="card-body">
          <span class="tag">Garbage KL</span>
          <h3>TZ2E</h3>
          <p>KL cab, 8x4, 31 t GCW. CATL 252 kWh, LvKong 270/450 kW. Heavy-duty refuse collection for municipal fleets. 4AMT for smooth stop-start.</p>
        </div>
      </div>
      <div class="card">
        <div class="card-body">
          <span class="tag">Mixer</span>
          <h3>TZ8J</h3>
          <p>KC PRO cab, 8x4, 45 t GCW. CATL 333 kWh, LvKong 350/520 kW. 8 m³ concrete mixer drum. Charging standard GB/T. For urban construction sites.</p>
        </div>
      </div>
      <div class="card">
        <div class="card-body">
          <span class="tag">Mixer Euro</span>
          <h3>KT9X</h3>
          <p>KC PLUS cab, 8x4, 44 t GCW. CATL 410 kWh, LvKong 350/520 kW. EBS+AEBS+ESC, WVTA GSR2 compliant. CCS2 charging for EU markets.</p>
        </div>
      </div>
    </div>

    <h2 class="section-title">Specifications</h2>
    <table class="spec-table">
      <tr><th>Model</th><th>Type</th><th>Drive</th><th>Battery</th><th>Motor</th><th>GCW</th></tr>
      <tr><td>KT3F</td><td>Sprinkler</td><td>4x2</td><td>CATL 166/200 kWh</td><td>LvKong 128/260 kW</td><td>18 t</td></tr>
      <tr><td>KT1D</td><td>Sweeper</td><td>4x2</td><td>CATL 232/266 kWh</td><td>LvKong 128/260 kW</td><td>18 t</td></tr>
      <tr><td>KT3E</td><td>Garbage</td><td>4x2</td><td>CATL 232 kWh</td><td>LvKong 156/310 kW</td><td>18 t</td></tr>
      <tr><td>KT3Y/KT4Y</td><td>Garbage/Sprinkler</td><td>4x2</td><td>CATL 166–262 kWh</td><td>LvKong 110–210 kW</td><td>18 t</td></tr>
      <tr><td>KT7A</td><td>Sprinkler</td><td>6x4</td><td>CATL 232 kWh</td><td>LvKong 164/308 kW</td><td>25 t</td></tr>
      <tr><td>TZ2E</td><td>Garbage</td><td>8x4</td><td>CATL 252 kWh</td><td>LvKong 270/450 kW</td><td>31 t</td></tr>
      <tr><td>TZ8J</td><td>Mixer</td><td>8x4</td><td>CATL 333 kWh</td><td>LvKong 350/520 kW</td><td>45 t</td></tr>
      <tr><td>KT9X</td><td>Mixer Euro</td><td>8x4</td><td>CATL 410 kWh</td><td>LvKong 350/520 kW</td><td>44 t</td></tr>
    </table>
  </div>
</div>
"""
write('products/electric-special.html', page(
    "Electric Special Vehicles | Dongfeng EV Export — Sanitation Mixer",
    "Dongfeng electric special vehicles: KT3F sprinkler, KT1D sweeper, TZ8J mixer, KT9X Euro mixer. Zero-emission municipal and construction trucks with CATL batteries.",
    "Dongfeng electric special vehicle, Dongfeng EV mixer, Dongfeng electric garbage truck, Dongfeng electric sprinkler, KT3F, KT1D, TZ8J, KT9X, electric sanitation truck, electric concrete mixer, WVTA GSR2, buy electric special truck China",
    special_body, rel="../"
))

# ── About Us ──
about_body = """
<div class="section" style="background:#fff;">
  <div class="section-inner">
    <div class="breadcrumb"><a href="index.html">Home</a> &rsaquo; About Us</div>
    <h1 class="section-title">About Dongfeng Vehicle Export</h1>
    <p class="section-sub">Shaanxi Fenghan Trading Co., Ltd — your authorized partner for Dongfeng new energy commercial vehicles.</p>
    <div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(280px,1fr)); gap:32px; margin-top:32px;">
      <div>
        <h3 style="font-size:22px; margin-bottom:12px;">Company Overview</h3>
        <p style="color:var(--muted); margin-bottom:16px;">Founded in Xi'an, Shaanxi Province, we are an authorized export trading company specializing in Dongfeng new energy commercial vehicles. We integrate overseas vehicle development, complete-vehicle and parts sales, after-sales service guarantee, and financial product expansion.</p>
        <p style="color:var(--muted); margin-bottom:16px;">Our business started with overseas after-sales service. Through integrity and excellent support, we have gained a strong reputation among overseas Chinese-funded enterprises and local fleet operators. We now promote Dongfeng Commercial Vehicles, Dongfeng Xinjiang, Dongfeng Liuzhou and Dongfeng New Energy Vehicles across Africa, South America, the Middle East and Europe.</p>
        <p style="color:var(--muted);">With an annual sales volume exceeding 1,000 units and a team of 50+ employees (including 30+ staff in our Nigerian branch), we provide localized support from inquiry to delivery.</p>
      </div>
      <div>
        <h3 style="font-size:22px; margin-bottom:12px;">Our Advantage</h3>
        <ul style="color:var(--muted); line-height:2; padding-left:20px;">
          <li><strong>High-quality products</strong> tailored to local emission and road regulations</li>
          <li><strong>Flexible finance</strong> — T/T 30% deposit + 70% before shipment or against B/L</li>
          <li><strong>Professional logistics</strong> — 90% by sea: container, RoRo or bulk carrier</li>
          <li><strong>After-sales guarantee</strong> — R&D support, spare parts centers, remote diagnostics</li>
          <li><strong>Product customization</strong> — RHD, paint, body type, battery capacity, charging standard</li>
        </ul>
      </div>
    </div>

    <div style="margin-top:48px; display:grid; grid-template-columns: repeat(auto-fit, minmax(200px,1fr)); gap:24px; text-align:center;">
      <div style="padding:24px; background:var(--bg); border-radius:var(--radius);">
        <div style="font-size:36px; font-weight:800; color:var(--accent);">20+</div>
        <div style="color:var(--muted); font-size:14px;">Years Export Experience</div>
      </div>
      <div style="padding:24px; background:var(--bg); border-radius:var(--radius);">
        <div style="font-size:36px; font-weight:800; color:var(--accent);">60+</div>
        <div style="color:var(--muted); font-size:14px;">Countries with Service Network</div>
      </div>
      <div style="padding:24px; background:var(--bg); border-radius:var(--radius);">
        <div style="font-size:36px; font-weight:800; color:var(--accent);">1,000+</div>
        <div style="color:var(--muted); font-size:14px;">Annual Unit Sales</div>
      </div>
      <div style="padding:24px; background:var(--bg); border-radius:var(--radius);">
        <div style="font-size:36px; font-weight:800; color:var(--accent);">10</div>
        <div style="color:var(--muted); font-size:14px;">Overseas Parts Centers</div>
      </div>
    </div>
  </div>
</div>
"""
write('about-us.html', page(
    "About Us | Dongfeng EV Export — Shaanxi Fenghan Trading",
    "Learn about Shaanxi Fenghan Trading Co., Ltd, authorized Dongfeng new energy commercial vehicle exporter. 20+ years experience, 60+ countries, 1000+ units/year.",
    "Dongfeng EV exporter, Dongfeng electric truck dealer, Shaanxi Fenghan Trading, about Dongfeng export, Dongfeng new energy vehicles company, China electric truck exporter",
    about_body
))

# ── Contact ──
contact_body = """
<div class="section" style="background:#fff;">
  <div class="section-inner">
    <div class="breadcrumb"><a href="index.html">Home</a> &rsaquo; Contact Us</div>
    <h1 class="section-title">Contact Us</h1>
    <p class="section-sub">Get a quote, schedule a video factory tour, or discuss your fleet electrification project.</p>
    <div class="contact-grid" style="margin-top:32px;">
      <div class="contact-card">
        <h4>WhatsApp</h4>
        <p>+86 15319431311<br>Fastest response for quotes and photos.</p>
      </div>
      <div class="contact-card">
        <h4>Email</h4>
        <p>sales@fenghan-trade.com<br>Send specs, quantities and destination port for formal quotation.</p>
      </div>
      <div class="contact-card">
        <h4>Phone</h4>
        <p>+86 719 8128 128<br>Office hours: Mon–Fri 09:00–18:00 (GMT+8)</p>
      </div>
      <div class="contact-card">
        <h4>Address</h4>
        <p>Room 603A, Floor 6, Building B<br>Chanba Free Trade Center<br>Xi'an, Shaanxi, China 710000</p>
      </div>
    </div>
    <div style="margin-top:40px; padding:32px; background:var(--bg); border-radius:var(--radius);">
      <h3 style="margin-bottom:12px;">Request a Quote</h3>
      <p style="color:var(--muted);">Tell us your target models, quantity, destination port and preferred charging standard. We typically reply within 24 hours with CIF/FOB pricing and delivery schedule.</p>
      <a href="https://wa.me/8615319431311" class="btn btn-primary" style="margin-top:16px;">Message on WhatsApp</a>
      <a href="mailto:sales@fenghan-trade.com?subject=Dongfeng EV Quote Request" class="btn btn-outline" style="margin-top:16px; color:var(--text); border-color:var(--muted);">Send Email</a>
    </div>
  </div>
</div>
"""
write('contact-us.html', page(
    "Contact Us | Dongfeng EV Export — Quote & Inquiry",
    "Contact Shaanxi Fenghan Trading for Dongfeng electric truck quotes. WhatsApp +86 15319431311, email sales@fenghan-trade.com. CIF/FOB pricing, factory tours, video inspection.",
    "Dongfeng EV contact, Dongfeng electric truck quote, buy Dongfeng EV, Dongfeng EV WhatsApp, Dongfeng EV email, Fenghan Trading contact, China electric truck supplier",
    contact_body
))

# ── FAQ ──
faq_body = """
<div class="section" style="background:#fff;">
  <div class="section-inner">
    <div class="breadcrumb"><a href="index.html">Home</a> &rsaquo; FAQ</div>
    <h1 class="section-title">Frequently Asked Questions</h1>
    <p class="section-sub">Everything you need to know about buying Dongfeng electric trucks from China.</p>

    <div class="faq-item">
      <h4>How do I purchase a Dongfeng electric truck from your company?</h4>
      <p>Choose the model from our website, then tell our sales manager your specific requirements (drive mode, battery capacity, charging standard, body type). We will recommend the suitable model and send a formal quotation. After you confirm the model and price, we sign the contract and begin production.</p>
    </div>
    <div class="faq-item">
      <h4>How do you ensure product quality?</h4>
      <p>Firstly, Dongfeng holds international quality system certifications (ISO 9001, CCC). Secondly, you are welcome to visit our company and factory in China. Finally, you can entrust a third-party inspection organization (such as SGS or BV) to inspect the vehicles before delivery.</p>
    </div>
    <div class="faq-item">
      <h4>Can you offer customized configurations?</h4>
      <p>Yes. We can customize paint color, body dimensions, battery capacity, charging interface (GB/T or CCS2), right-hand drive conversion, and special-purpose upfits (mixer drum, garbage compactor, sprinkler tank, etc.).</p>
    </div>
    <div class="faq-item">
      <h4>What is the warranty on batteries and vehicles?</h4>
      <p>CATL batteries carry an 8-year or 4,500-cycle warranty. The complete vehicle warranty is 12 months or 100,000 km, whichever comes first. Extended warranty packages are available for fleet customers.</p>
    </div>
    <div class="faq-item">
      <h4>Do you supply spare parts?</h4>
      <p>Yes. We operate 10 overseas parts centers and can ship genuine Dongfeng EV parts (motors, battery modules, controllers, axles, cabin parts) within 7 days.</p>
    </div>
    <div class="faq-item">
      <h4>What payment terms do you accept?</h4>
      <p>For new clients: 30% T/T deposit in advance, 70% balance before shipment. For repeat clients: 30% deposit, 70% against copy of original B/L. L/C at sight is negotiable for large orders.</p>
    </div>
    <div class="faq-item">
      <h4>Which countries do you export to?</h4>
      <p>We currently export to 60+ countries including Nigeria, Kenya, South Africa, UAE, Saudi Arabia, Russia, Peru, Chile, Mexico, Vietnam, Indonesia, Australia and European markets.</p>
    </div>
  </div>
</div>
"""
write('faq.html', page(
    "FAQ | Dongfeng EV Export — Buying Electric Trucks from China",
    "Frequently asked questions about Dongfeng electric trucks: charging standards, RHD, warranty, spare parts, payment terms, shipping, customization. Read before you buy.",
    "Dongfeng EV FAQ, buy electric truck from China, Dongfeng electric truck warranty, CATL battery warranty, Dongfeng EV spare parts, electric truck payment terms, electric truck shipping",
    faq_body
))

print("Done. Files generated:")
for root, dirs, files in os.walk(BASE):
    for f in files:
        if f.endswith(('.html','.css')):
            p = os.path.relpath(os.path.join(root,f), BASE)
            print(" ", p)
