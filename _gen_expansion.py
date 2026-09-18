#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Site #4 expansion: 18 model detail pages + 30 market landing pages + index + sitemap."""
import os, re, json

BASE = os.path.dirname(os.path.abspath(__file__))
SITE = "https://dongfengevtrucks.com"
TODAY = "2026-09-18"

# ---------------- MODEL DATA ----------------
# slug, name, category(file), cat_name, drive, gvw, battery, motor, charge, apps[], desc, faq_extra
MODELS = [
 ("te46-electric-tractor", "TE46", "electric-tractor", "Electric Tractor", "4×2", "42 t GCW",
  "CATL 400 kWh LFP", "LvKong 315/510 kW · 4AMT", "GB/T dual-gun, 20–80% ≈40 min (CCS2 as TE4Z)",
  ["Port container shuttling", "Urban & regional distribution", "Warehouse-to-hub line feed"],
  "The TE46 is Dongfeng's 4×2 electric prime mover built on the KL MAX cab — the agile answer for port and urban logistics where a 6×4 is more truck than the route needs. EBS+ESC, LDWS+FCWS, LED headlights and an air-suspended cab come standard."),
 ("te8l-electric-tractor", "TE8L", "electric-tractor", "Electric Tractor", "6×4", "49 t GCW",
  "CATL 400/466/600 kWh LFP", "LvKong 315/510 kW · 4AMT", "GB/T (TE8K variant = CCS2 for Europe)",
  ["Regional line-haul", "Container corridor transport", "Fleet trunk routes"],
  "The TE8L is the workhorse 6×4 line-haul tractor of the range: three battery options to match route length, proven LvKong drive and a full active-safety pack. The TE8K sister model carries CCS2 for European compliance."),
 ("te9l-electric-tractor", "TE9L", "electric-tractor", "Electric Tractor", "6×4", "49–65 t GCW",
  "CATL 400/497/600 kWh LFP", "LvKong 350/520 kW · DF601S/DF162E axles", "600 A dual-gun fast charge",
  ["Efficiency-first line-haul", "High-utilisation fleet trunking", "Payload-sensitive contracts (TE9B 65 t)"],
  "The TE9L strips weight for best-in-class efficiency at 49 t, while the TE9B variant adds headroom to 65 t GCW. Dual-gun 600 A charging keeps 20–80% SOC at roughly 40 minutes."),
 ("te8m-electric-tractor", "TE8M", "electric-tractor", "Electric Tractor", "6×4", "80 t GCW",
  "CATL 466/497/600 kWh LFP", "LvKong 400/550 kW · DF701S/DF485 axles", "Dual-gun DC fast charge",
  ["Coal & ore haulage", "Heavy corridor contracts", "Mining-port trunk routes"],
  "The TE8M is the heavy-haul specialist: reinforced 300×90×8+6 frame, big-battery options and 550 kW peak to keep 80-tonne combinations moving on the hardest earning routes."),
 ("te8p-electric-tractor", "TE8P", "electric-tractor", "Electric Tractor", "6×4", "120 t GCW",
  "CATL 400/600 kWh LFP", "LvKong 400/550 kW · DF300H rear axle", "Dual-gun DC fast charge",
  ["Extreme combination loads", "Heavy equipment transport", "Industrial project logistics"],
  "Maximum pulling power in the Dongfeng EV range: 120 t GCW rating, 9/13 parabolic suspension, DF300H heavy rear axle and 12.00R20 tyres for the combinations other trucks refuse."),
 ("kta1-electric-dump-truck", "KTA1", "electric-dump", "Electric Dump Truck", "8×4", "31 t GVW",
  "CATL 352 kWh LFP", "LvKong 270/450 kW · 4AMT", "DC fast charge",
  ["Urban construction waste", "Sand & stone city haulage", "Municipal earthworks"],
  "The KTA1 pairs the KC PLUS D560KC cab with a compact 8×4 chassis — the city construction tipper that moves sand, stone and muck all shift on one charge, with EBS+ESC standard."),
 ("tz3z-electric-dump-truck", "TZ3Z", "electric-dump", "Electric Dump Truck", "8×4", "55 t GCW",
  "CATL 400 kWh LFP", "LvKong 315/510 kW · 4AMT · HDZ300 axle", "600 A dual-gun, 20–80% ≈40 min",
  ["General construction haulage", "Quarry-to-plant feed", "Infrastructure projects"],
  "The TZ3Z is the versatile construction favourite: 55 t GCW, KC PRO cab, and 600 A dual-gun charging that turns a lunch break into a full afternoon of hauling."),
 ("tz3v-electric-dump-truck", "TZ3V", "electric-dump", "Electric Dump Truck", "8×4", "80 t GCW",
  "CATL 600 kWh LFP", "LvKong 400/550 kW · HDZ300 rear axle", "Dual-gun DC fast charge",
  ["Open-pit mining", "Hard quarry haul roads", "Maximum-payload contracts"],
  "Mining-grade tipper with an 8+8+4 multi-layer frame, 10/10/13 suspension and the biggest battery in the dump range — built for the world's hardest haul roads."),
 ("tz5e-electric-dump-truck", "TZ5E", "electric-dump", "Electric Dump Truck", "6×4", "65 t GCW",
  "CATL 400 kWh LFP", "LvKong 315/510 kW · DF901S/HDZ300 axles", "DC fast charge",
  ["Quarry haul roads", "Mid-size mining", "Dam & highway construction"],
  "The TZ5E brings a 6×4 layout to 65 t quarry work: 8+8+4+10 reinforced frame, 10/13 suspension and the balance of agility and payload for rough access roads."),
 ("kt5m-electric-cargo-truck", "KT5M", "electric-cargo", "Electric Cargo Truck", "4×2", "18 t GVW",
  "CATL 262/310 kWh LFP", "LvKong 150/270 kW e-axle · 4-speed", "DC fast + AC depot charging",
  ["Urban & regional distribution", "Express parcel trunking", "FMCG delivery fleets"],
  "The KT5M is the volume seller of the cargo range: 7,150 mm wheelbase, over 65 m³ of box volume and an e-axle that cuts drivetrain losses — the diesel 18-tonner's direct replacement."),
 ("kt5j-electric-cargo-truck", "KT5J", "electric-cargo", "Electric Cargo Truck", "4×2", "18 t GVW",
  "CATL 262/310 kWh LFP", "LvKong 150/270 kW e-axle (342 hp peak)", "DC fast + AC depot charging",
  ["Last-mile delivery", "Tight city streets", "Urban grocery & retail feed"],
  "The KT5J shortens the KT5M formula to a 5,000 mm wheelbase for tight city work — peak 342 hp, equivalent to a 6-cylinder diesel, with none of the noise or fumes."),
 ("kt5l-electric-cargo-truck", "KT5L", "electric-cargo", "Electric Cargo Truck", "4×2", "18 t GVW",
  "CATL 348 kWh LFP", "LvKong e-axle", "DC fast + AC depot charging",
  ["Express parcel long-body", "Bulk light goods", "Regional distribution hubs"],
  "The KT5L stretches the formula: CATL 348 kWh for extended range and body lengths from 7,700 to 9,800 mm with 65–70 m³ of volume for express and bulk operators."),
 ("kth3-electric-cargo-truck", "KTH3", "electric-cargo", "Electric Cargo Truck", "8×4", "31 t GVW",
  "CATL 400 kWh LFP", "LvKong 450 kW (612 hp)", "DC fast charge",
  ["9.8 m long-box flagship", "Heavy regional distribution", "High-volume contract logistics"],
  "The KTH3 is the 8×4 long-box flagship: 612 hp, a 10.5 m turning radius and a light chassis allowing up to 38 t gross combination — serious volume on electric power."),
 ("kt3f-electric-sprinkler-truck", "KT3F", "electric-special", "Electric Special Vehicle", "4×2", "18 t GVW",
  "CATL 166/200 kWh LFP", "LvKong 128/260 kW", "DC fast + AC depot charging",
  ["Road watering & dust control", "Construction site suppression", "Green-belt irrigation"],
  "The KT3F puts a water-tank sprinkler body on the proven 18 t electric chassis with electric pump drive — motor-direct or 4AMT — for quiet, fume-free watering duty."),
 ("kt1d-electric-sweeper-truck", "KT1D", "electric-special", "Electric Special Vehicle", "4×2", "18 t GVW",
  "CATL 232/266 kWh LFP", "LvKong 128/260 kW direct drive · EBS", "DC fast + AC depot charging",
  ["Urban road sweeping", "Early-morning city-centre shifts", "Airport & port apron cleaning"],
  "The KT1D sweeper-washer combines vacuum and water-spray systems on a near-silent electric chassis — quiet enough for 4 a.m. city-centre work without a single complaint."),
 ("kt3e-electric-garbage-truck", "KT3E", "electric-special", "Electric Special Vehicle", "4×2", "18 t GVW",
  "CATL 166–262 kWh LFP", "LvKong 110–210 kW · 4AMT", "GB/T (KT3Y/KT4Y = CCS2 for EU municipalities)",
  ["Municipal refuse collection", "Rear-loading compaction routes", "Green-city tender fleets"],
  "The KT3E rear-loading garbage compactor is built for municipal stop-start duty: zero tailpipe emissions, below-diesel noise, and CCS2 variants ready for European tenders."),
 ("kt7a-electric-washing-truck", "KT7A", "electric-special", "Electric Special Vehicle", "6×4", "25 t GVW",
  "CATL 232 kWh LFP", "LvKong 164/308 kW", "DC fast charge",
  ["Highway washing", "Port & mine access dust suppression", "Large-area municipal washing"],
  "The KT7A scales washing and dust-suppression duty up to a 6×4 25 t platform — large-capacity tanks and 308 kW peak for highways, ports and mine access roads."),
 ("tz8j-electric-mixer-truck", "TZ8J", "electric-special", "Electric Special Vehicle", "8×4", "45 t GVW",
  "CATL 333 kWh LFP", "LvKong electric drive", "GB/T (KT9X = CCS2, WVTA GSR2 for EU)",
  ["Ready-mix concrete delivery", "Urban construction sites", "Emission-controlled zones"],
  "The TZ8J runs an 8 m³ drum on a 45 t 8×4 electric chassis — concrete delivered emission-free, with the torque to climb site ramps fully loaded. Sister model KT9X adds CCS2 and full EU type approval."),
]

# ---------------- MARKET DATA ----------------
# slug, country, region, port, side, transit, models[], hook, note
MARKETS = [
 ("nigeria", "Nigeria", "West Africa", "Lagos (Apapa / Tin Can Island)", "LHD", "35–40 days",
  ["te8l-electric-tractor", "tz3z-electric-dump-truck", "kt5m-electric-cargo-truck", "kt1d-electric-sweeper-truck"],
  "Africa's largest economy is electrifying port logistics around Lagos, and state governments are writing zero-emission clauses into new municipal tenders.",
  "Lagos congestion rewards regenerative braking; depot AC charging covers most urban duty cycles."),
 ("kenya", "Kenya", "East Africa", "Mombasa", "RHD (factory TE9Y / TZ4Y / KT3Y)", "25–30 days",
  ["kt5m-electric-cargo-truck", "tz3z-electric-dump-truck", "kt3e-electric-garbage-truck"],
  "Kenya's geothermal-rich grid and Nairobi's green-city programme make it East Africa's most EV-ready truck market.",
  "Factory RHD variants ship with dashboard/pedal swap done at the plant, not aftermarket kits."),
 ("ghana", "Ghana", "West Africa", "Tema", "LHD", "35–40 days",
  ["tz3z-electric-dump-truck", "kt5m-electric-cargo-truck", "kt3f-electric-sprinkler-truck"],
  "Tema port expansion and Accra's construction boom are pulling demand for clean construction and distribution fleets.",
  "Tema corridor routes suit 400 kWh dump and cargo configurations with depot charging."),
 ("tanzania", "Tanzania", "East Africa", "Dar es Salaam", "RHD (factory)", "25–30 days",
  ["te8l-electric-tractor", "tz5e-electric-dump-truck", "kt1d-electric-sweeper-truck"],
  "Dar es Salaam port upgrades and the standard-gauge railway build are opening trunk routes ideal for electric haulage pilots.",
  "Factory RHD available across tractor, dump and sanitation lines."),
 ("ethiopia", "Ethiopia", "East Africa", "Djibouti (corridor to Addis Ababa)", "LHD", "30–35 days",
  ["te8l-electric-tractor", "kt5l-electric-cargo-truck", "kt3f-electric-sprinkler-truck"],
  "Ethiopia banned ICE vehicle imports in 2024 — the only African market where electric is not an option but the law.",
  "Djibouti-Addis corridor (750 km) works with 600 kWh tractors and mid-route fast charging."),
 ("egypt", "Egypt", "North Africa", "Alexandria / Damietta", "LHD", "20–25 days",
  ["kt5m-electric-cargo-truck", "kt1d-electric-sweeper-truck", "tz3z-electric-dump-truck"],
  "Cairo's new administrative capital and monorail-era municipal fleets are specifying electric from day one.",
  "Hot-climate battery cooling package recommended for Upper Egypt routes."),
 ("algeria", "Algeria", "North Africa", "Algiers", "LHD", "22–28 days",
  ["tz3v-electric-dump-truck", "te8m-electric-tractor", "kt3e-electric-garbage-truck"],
  "Algeria's south-north construction corridors and municipal modernisation budgets favour heavy electric platforms.",
  "Mining-spec packages (IP67 + reinforced suspension) suit Saharan edge conditions."),
 ("morocco", "Morocco", "North Africa", "Casablanca / Tanger Med", "LHD", "20–25 days",
  ["te8l-electric-tractor", "kt5m-electric-cargo-truck", "kt1d-electric-sweeper-truck"],
  "Tanger Med — Africa's busiest port — is electrifying drayage, and Moroccan cities are tendering clean municipal fleets.",
  "CCS2 variants align with Morocco's European-standard charging rollout."),
 ("south-africa", "South Africa", "Southern Africa", "Durban", "RHD (factory)", "30–35 days",
  ["tz5e-electric-dump-truck", "te8m-electric-tractor", "kt3e-electric-garbage-truck"],
  "Mining majors with net-zero commitments are trialling electric haul fleets, and Nersa wheeling rules make depot solar-plus-EV economics work.",
  "Factory RHD; mining package (IP67, skid plates) recommended for platinum belt conditions."),
 ("saudi-arabia", "Saudi Arabia", "Middle East", "Jeddah / King Abdullah Port", "LHD", "18–22 days",
  ["te8l-electric-tractor", "kt1d-electric-sweeper-truck", "kt7a-electric-washing-truck", "tz8j-electric-mixer-truck"],
  "Vision 2030 giga-projects (NEOM, Red Sea, Qiddiya) write zero-emission site rules into contractor requirements.",
  "Desert package (enhanced cooling + dust-sealed motors) strongly recommended."),
 ("uae", "United Arab Emirates", "Middle East", "Jebel Ali (Dubai)", "LHD", "18–22 days",
  ["te8l-electric-tractor", "kt5m-electric-cargo-truck", "kt1d-electric-sweeper-truck"],
  "Dubai and Abu Dhabi target 30% clean municipal fleets by 2030; Jebel Ali drayage is already electrifying.",
  "Extensive DC fast-charging corridors between Dubai–Abu Dhabi suit 400 kWh tractors."),
 ("qatar", "Qatar", "Middle East", "Hamad Port", "LHD", "18–22 days",
  ["kt5m-electric-cargo-truck", "tz8j-electric-mixer-truck", "kt3e-electric-garbage-truck"],
  "Post-World-Cup Doha keeps building — with sustainability clauses carried over into every new tender.",
  "Compact geography: one depot fast charger covers entire Greater Doha duty cycles."),
 ("jordan", "Jordan", "Middle East", "Aqaba", "LHD", "20–25 days",
  ["kt5m-electric-cargo-truck", "kt3f-electric-sprinkler-truck", "tz3z-electric-dump-truck"],
  "Aqaba's green-port programme and Jordan's solar surplus create low-cost charging economics for early fleets.",
  "Aqaba–Amman corridor (330 km) suits 400 kWh configurations with one mid-route top-up."),
 ("iraq", "Iraq", "Middle East", "Umm Qasr", "LHD", "22–28 days",
  ["tz3z-electric-dump-truck", "kt3f-electric-sprinkler-truck", "kt5m-electric-cargo-truck"],
  "Reconstruction logistics around Basra and Baghdad reward operators who can run independent of diesel supply chains.",
  "Depot charging plus generator-backed DC fast charge recommended for grid-variable regions."),
 ("uzbekistan", "Uzbekistan", "Central Asia", "Rail/truck via Khorgos to Tashkent", "LHD", "12–18 days (land)",
  ["te8l-electric-tractor", "kt5l-electric-cargo-truck", "kt3e-electric-garbage-truck"],
  "Tashkent's green-city programme and Uzbekistan's EV incentives (zero customs duty on EVs) make Central Asia's most accessible market.",
  "Land delivery via Khorgos cuts logistics cost vs sea; winter package (-20°C) available."),
 ("kazakhstan", "Kazakhstan", "Central Asia", "Land route via Khorgos / Altynkol", "LHD", "10–15 days (land)",
  ["te8m-electric-tractor", "tz3v-electric-dump-truck", "kt5l-electric-cargo-truck"],
  "Kazakhstan's mining corridor and Almaty's air-quality rules are pushing fleets toward electric heavy trucks.",
  "Battery heater option recommended for -30°C steppe winters."),
 ("chile", "Chile", "South America", "San Antonio / Valparaíso", "LHD", "38–45 days",
  ["tz3v-electric-dump-truck", "te8m-electric-tractor", "kt1d-electric-sweeper-truck"],
  "The world's copper capital has national electromobility targets and mining houses racing to decarbonise haul fleets.",
  "High-altitude package (4,500 m certified) available for Andean mine sites."),
 ("peru", "Peru", "South America", "Callao", "LHD", "38–45 days",
  ["tz3v-electric-dump-truck", "tz5e-electric-dump-truck", "kt5m-electric-cargo-truck"],
  "Peru's copper and zinc belts plus Lima's congestion charges create pull from both mines and city logistics.",
  "Altitude-rated motor derating curves for 3,500 m+ operations."),
 ("colombia", "Colombia", "South America", "Buenaventura", "LHD", "35–42 days",
  ["kt5m-electric-cargo-truck", "tz3z-electric-dump-truck", "kt3e-electric-garbage-truck"],
  "Bogotá and Medellín run Latin America's most aggressive clean-fleet procurement programmes.",
  "Mountain-grade regenerative braking recovers meaningful energy on Andean descents."),
 ("dominican-republic", "Dominican Republic", "Caribbean", "Río Haina / Caucedo", "LHD", "35–42 days",
  ["kt5m-electric-cargo-truck", "kt5j-electric-cargo-truck", "kt3f-electric-sprinkler-truck"],
  "Santo Domingo's distribution networks and Punta Cana's resort logistics suit compact electric fleets with island-scale range.",
  "Island duty cycles (under 150 km/day) mean overnight AC depot charging is often sufficient."),
 ("mexico", "Mexico", "Latin America", "Manzanillo / Veracruz", "LHD", "30–40 days",
  ["te8l-electric-tractor", "kt5m-electric-cargo-truck", "tz8j-electric-mixer-truck"],
  "Nearshoring-driven freight growth and Mexico City's Hoy No Circula rules reward zero-emission fleets.",
  "Bajío corridor (Mexico City–Guadalajara–Monterrey) fits 600 kWh tractors with corridor fast charging."),
 ("thailand", "Thailand", "Southeast Asia", "Laem Chabang", "RHD (factory)", "10–15 days",
  ["kt5m-electric-cargo-truck", "tz3z-electric-dump-truck", "kt3e-electric-garbage-truck"],
  "Thailand's 30@30 EV policy and Eastern Economic Corridor incentives extend to commercial EVs.",
  "Factory RHD; short sea transit keeps landed cost competitive."),
 ("indonesia", "Indonesia", "Southeast Asia", "Tanjung Priok (Jakarta)", "RHD (factory)", "12–18 days",
  ["tz3z-electric-dump-truck", "kt5m-electric-cargo-truck", "kt1d-electric-sweeper-truck"],
  "Jakarta's low-emission zone plans and nickel-driven industrial parks are opening fleet electrification budgets.",
  "Factory RHD; tropical humidity package available."),
 ("philippines", "Philippines", "Southeast Asia", "Manila", "LHD", "10–15 days",
  ["kt5j-electric-cargo-truck", "kt5m-electric-cargo-truck", "kt3e-electric-garbage-truck"],
  "Metro Manila's jeepney-modernisation mindset is spreading to trucks — LGUs and private fleets piloting electric.",
  "Short inter-city routes suit 262–310 kWh cargo configurations."),
 ("vietnam", "Vietnam", "Southeast Asia", "Hai Phong / Cat Lai (HCMC)", "LHD", "8–12 days",
  ["kt5m-electric-cargo-truck", "te8l-electric-tractor", "tz3z-electric-dump-truck"],
  "Vietnam's manufacturing corridors (Hanoi–Haiphong, HCMC–Binh Duong) run short, dense, perfect-for-EV freight loops.",
  "Shortest sea transit from China — landed cost advantage vs any other export region."),
 ("malaysia", "Malaysia", "Southeast Asia", "Port Klang", "RHD (factory)", "10–15 days",
  ["kt5m-electric-cargo-truck", "kt1d-electric-sweeper-truck", "tz8j-electric-mixer-truck"],
  "Malaysia's Low Carbon Mobility Blueprint and Klang Valley construction keep demand steady for clean commercial fleets.",
  "Factory RHD; CCS2 variants match Malaysia's charging standard."),
 ("pakistan", "Pakistan", "South Asia", "Karachi", "RHD (factory)", "18–25 days",
  ["te8l-electric-tractor", "tz3z-electric-dump-truck", "kt5m-electric-cargo-truck"],
  "CPEC corridor logistics and Karachi–Lahore motorway freight create defined routes where depot-to-depot EV trucking works today.",
  "Factory RHD; high-temperature cooling package recommended."),
 ("bangladesh", "Bangladesh", "South Asia", "Chittagong (Chattogram)", "RHD (factory)", "15–20 days",
  ["kt5m-electric-cargo-truck", "kt3e-electric-garbage-truck", "kt3f-electric-sprinkler-truck"],
  "Dhaka's air-quality crisis is pushing municipal and garment-logistics fleets toward electric alternatives.",
  "Factory RHD; monsoon-sealed electrical connectors available."),
 ("myanmar", "Myanmar", "Southeast Asia", "Yangon", "LHD", "12–18 days",
  ["kt5m-electric-cargo-truck", "tz3z-electric-dump-truck"],
  "Yangon's industrial zones and generator-backed depots make EV fleets a hedge against diesel supply volatility.",
  "Depot charging with generator backup recommended for grid-variable areas."),
 ("cote-divoire", "Côte d'Ivoire", "West Africa", "Abidjan", "LHD", "35–40 days",
  ["tz3z-electric-dump-truck", "kt5m-electric-cargo-truck", "kt1d-electric-sweeper-truck"],
  "Abidjan's port-city growth and cocoa-export logistics create year-round utilisation for clean distribution fleets.",
  "Cocoa-season surge capacity suits 310 kWh cargo with opportunity fast charging."),
]

MD = {m[0]: m for m in MODELS}

HEADER = """<header class="header">
  <div class="header-inner">
    <a href="{P}index.html" class="logo">DONGFENG<span>EV</span></a>
    <div class="mobile-toggle" onclick="document.getElementById('mainNav').classList.toggle('open')"><span></span><span></span><span></span></div>
    <nav class="main-nav" id="mainNav">
  <li><a href="{P}index.html">Home</a></li>
  <li><a href="{P}products/electric-tractor.html">Electric Tractor</a></li>
  <li><a href="{P}products/electric-dump.html">Electric Dump</a></li>
  <li><a href="{P}products/electric-cargo.html">Electric Cargo</a></li>
  <li><a href="{P}products/electric-special.html">Electric Special</a></li>
  <li><a href="{P}markets/index.html">Markets</a></li>
  <li><a href="{P}blog/index.html">Blog</a></li>
  <li><a href="{P}about-us.html">About Us</a></li>
  <li><a href="{P}contact-us.html">Contact</a></li>
</nav>
  </div>
</header>"""

FOOTER = """<footer class="footer">
  <div class="footer-inner">
    <div class="footer-grid">
      <div>
        <h5>Dongfeng EV Export</h5>
        <p style="font-size:14px;color:rgba(255,255,255,0.7);margin-top:8px;">Authorized Dongfeng new energy commercial vehicle exporter. Supplying electric tractors, dump trucks, cargo trucks and special vehicles to 60+ countries.</p>
      </div>
      <div>
        <h5>Products</h5>
        <ul>
          <li><a href="{P}products/electric-tractor.html">Electric Tractor</a></li>
          <li><a href="{P}products/electric-dump.html">Electric Dump Truck</a></li>
          <li><a href="{P}products/electric-cargo.html">Electric Cargo Truck</a></li>
          <li><a href="{P}products/electric-special.html">Electric Special Vehicle</a></li>
        </ul>
      </div>
      <div>
        <h5>Company</h5>
        <ul>
          <li><a href="{P}about-us.html">About Us</a></li>
          <li><a href="{P}faq.html">FAQ</a></li>
          <li><a href="{P}contact-us.html">Contact Us</a></li>
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
    <div class="footer-links">
      <h5 style="font-size:15px;color:#fff;margin:0 0 6px 0;">Our Other Sites</h5>
      <p style="font-size:13px;margin:4px 0;"><a href="https://sagmoto-trucks.com/" style="color:rgba(255,255,255,0.75);text-decoration:none;">Sagmoto Trucks (SAGMOTO)</a></p>
      <p style="font-size:13px;margin:4px 0;"><a href="https://www.fenghan-trade.com/" style="color:rgba(255,255,255,0.75);text-decoration:none;">Fenghan Trade (SHACMAN)</a></p>
    </div>
    <div class="footer-bottom">&copy; 2026 Shaanxi Fenghan Trading Co., Ltd. All rights reserved. | Dongfeng EV Trucks Export</div>
  </div>
</footer>
<script src="{P}js/whatsapp-float.js" async></script>"""

SPEC_CSS = """<style>
.spec-tbl{width:100%;border-collapse:collapse;margin:18px 0;font-size:15px;}
.spec-tbl td{padding:10px 14px;border-bottom:1px solid #e5e9f0;}
.spec-tbl td:first-child{width:32%;font-weight:600;color:var(--primary);background:#f4f8f6;}
.page-hero-sm{background:linear-gradient(135deg,#0a1f2e,#006341);color:#fff;padding:56px 0 44px;}
.page-hero-sm .bc{font-size:13px;opacity:.75;margin-bottom:10px;}
.page-hero-sm .bc a{color:#fff;text-decoration:none;}
.page-hero-sm h1{font-size:34px;margin:0 0 8px;}
.page-hero-sm p{opacity:.85;max-width:820px;}
ul.tick{list-style:none;padding:0;}
ul.tick li{padding:6px 0 6px 26px;position:relative;}
ul.tick li:before{content:"\\2713";position:absolute;left:0;color:var(--accent);font-weight:700;}
</style>"""

def org_jsonld():
    return {"@context":"https://schema.org","@type":"Organization","name":"Shaanxi Fenghan Trading Co., Ltd",
      "url":SITE+"/","logo":SITE+"/images/hero-cover.jpg",
      "contactPoint":{"@type":"ContactPoint","telephone":"+86-15319431311","email":"sales@fenghan-trade.com","contactType":"sales"},
      "sameAs":["https://www.fenghan-trade.com/","https://sagmoto-trucks.com/",SITE+"/"]}

def head(title, desc, kw, url, prefix, extra_ld):
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<meta name="description" content="{desc}">
<meta name="keywords" content="{kw}">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{SITE}/images/hero-tractor.jpg">
<meta property="og:site_name" content="Dongfeng EV Trucks Export">
<meta name="twitter:card" content="summary_large_image">
<link rel="canonical" href="{url}">
<link rel="stylesheet" href="{prefix}css/dongfeng-ev.css">
<link rel="icon" href="{prefix}favicon.ico" type="image/x-icon">
<title>{title}</title>
<script type="application/ld+json">{json.dumps(org_jsonld(), ensure_ascii=False)}</script>
<script type="application/ld+json">{json.dumps(extra_ld, ensure_ascii=False)}</script>
{SPEC_CSS}
</head>
<body>"""

def cta_band(prefix, text):
    return f"""<div class="cta-band" style="background:linear-gradient(135deg,#006341,#00c853);color:#fff;padding:44px 0;text-align:center;margin-top:40px;">
  <div class="section-inner">
    <h2 style="margin:0 0 10px;font-size:26px;">{text}</h2>
    <p style="opacity:.9;margin:0 0 18px;">FOB / CIF quotation within 24 hours. Spec sheet, video and reference orders available on request.</p>
    <a class="btn btn-primary" style="background:#fff;color:#006341;font-weight:700;" href="https://wa.me/8615319431311?text=Hi%2C%20I%27m%20interested%20in%20Dongfeng%20electric%20trucks" target="_blank" rel="noopener">WhatsApp +86 153 1943 1311</a>
    &nbsp;<a class="btn btn-outline" style="border-color:#fff;color:#fff;" href="{prefix}contact-us.html">Email Us</a>
  </div>
</div>"""

# ---------------- MODEL PAGES ----------------
os.makedirs(os.path.join(BASE,'products','models'), exist_ok=True)
model_urls = []
for slug,name,cat,catname,drive,gvw,batt,motor,charge,apps,desc in MODELS:
    P = "../../"
    url = f"{SITE}/products/models/{slug}.html"
    faq = [
      (f"What is the battery warranty on the {name}?", "CATL LFP packs carry an 8-year / 4,500-cycle warranty to 80% state of health, backed by Dongfeng and Fenghan Trading aftersales."),
      (f"Can the {name} be supplied right-hand drive?", "Factory RHD conversion is available on request (4–6 weeks additional lead time) — done at the plant, not aftermarket."),
      (f"What charger does the {name} need?", f"The {name} charges via {charge}. We advise on depot charger selection and grid connection as part of every quotation."),
    ]
    ld = {"@context":"https://schema.org","@type":"Product","name":f"Dongfeng {name} {catname}",
      "brand":"Dongfeng","description":desc,"image":SITE+"/images/hero-tractor.jpg",
      "offers":{"@type":"Offer","priceCurrency":"USD","availability":"https://schema.org/InStock","url":url}}
    faq_ld = {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
      {"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faq]}
    apps_html = "".join(f"<li>{a}</li>" for a in apps)
    faq_html = "".join(f'<div class="faq-item"><h4>{q}</h4><p>{a}</p></div>' for q,a in faq)
    related = [m for m in MODELS if m[2]==cat and m[0]!=slug][:3]
    rel_html = "".join(f'<a class="btn btn-outline" href="{r[0]}.html" style="margin:4px;">{r[1]}</a>' for r in related)
    html = head(f"Dongfeng {name} {catname} — Specs & Export Price | Fenghan",
        f"Dongfeng {name} electric truck: {drive}, {gvw}, {batt}, {motor}. Export specs, applications and FOB/CIF quotation from authorized exporter.",
        f"Dongfeng {name}, {name} electric truck, {name} price, Dongfeng electric {catname.lower()}, {drive} electric truck, CATL {name}, buy {name}",
        url, P, faq_ld)
    html += f"""
{HEADER.replace('{P}',P)}
<div class="page-hero-sm">
  <div class="section-inner">
    <div class="bc"><a href="{P}index.html">Home</a> &rsaquo; <a href="{P}products/{cat}.html">{catname}</a> &rsaquo; {name}</div>
    <h1>Dongfeng {name} — {catname}</h1>
    <p>{drive} · {gvw} · {batt}</p>
  </div>
</div>
<main class="section"><div class="section-inner">
  <div class="section-title"><h2>Overview</h2></div>
  <p style="font-size:16px;line-height:1.8;max-width:900px;">{desc} Every unit is validated over 12,500 km of reliability testing before export, and Fenghan Trading configures battery, charging interface and options to your route, load and climate.</p>
  <div class="section-title" style="margin-top:28px;"><h2>Key Specifications</h2></div>
  <table class="spec-tbl">
    <tr><td>Model</td><td>Dongfeng {name}</td></tr>
    <tr><td>Category</td><td><a href="{P}products/{cat}.html">{catname}</a></td></tr>
    <tr><td>Drive</td><td>{drive}</td></tr>
    <tr><td>Rating</td><td>{gvw}</td></tr>
    <tr><td>Battery</td><td>{batt}</td></tr>
    <tr><td>Motor / Transmission</td><td>{motor}</td></tr>
    <tr><td>Charging</td><td>{charge}</td></tr>
    <tr><td>Safety</td><td>EBS + ESC, LDWS + FCWS (category dependent)</td></tr>
    <tr><td>Price</td><td>FOB / CIF on request — <a href="https://wa.me/8615319431311" target="_blank" rel="noopener">WhatsApp us for 24h quotation</a></td></tr>
  </table>
  <div class="section-title" style="margin-top:28px;"><h2>Built For</h2></div>
  <ul class="tick">{apps_html}</ul>
  <div class="section-title" style="margin-top:28px;"><h2>FAQ — {name}</h2></div>
  {faq_html}
  <div style="margin-top:24px;"><strong>Related models:</strong><br>{rel_html}</div>
</div></main>
{cta_band(P, f"Get the {name} working on your routes")}
{FOOTER.replace('{P}',P)}
</body>
</html>"""
    with open(os.path.join(BASE,'products','models',slug+'.html'),'w',encoding='utf-8') as f:
        f.write(html)
    model_urls.append(url)
print("models:", len(model_urls))

# ---------------- MARKET PAGES ----------------
os.makedirs(os.path.join(BASE,'markets'), exist_ok=True)
market_urls = []
for slug,country,region,port,side,transit,models,hook,note in MARKETS:
    P = "../"
    url = f"{SITE}/markets/{slug}.html"
    cards = ""
    for ms in models:
        m = MD[ms]
        cards += f"""<div class="prod-card" style="border:1px solid #e5e9f0;border-radius:12px;padding:18px;margin:10px 0;">
  <h3 style="margin:0 0 6px;"><a href="../products/models/{m[0]}.html" style="color:var(--primary);text-decoration:none;">Dongfeng {m[1]}</a> <span style="font-size:13px;color:#666;font-weight:400;">· {m[3]}</span></h3>
  <p style="margin:0;font-size:14px;color:#444;">{m[4]} · {m[5]} · {m[6]}</p>
</div>\n"""
    faq = [
      (f"How much does a Dongfeng electric truck cost in {country}?",
       f"Pricing depends on model, battery and options. As a guide, FOB China prices for the recommended {country} range run from USD 45,000 (18 t cargo) to USD 120,000+ (heavy mining tractor). We quote FOB and CIF {port.split('(')[0].strip()} within 24 hours — WhatsApp +86 15319431311."),
      (f"Can Dongfeng electric trucks handle {country}'s roads and climate?",
       f"Yes. Trucks for {country} are configured to local conditions: {note} All export units are validated over 12,500 km reliability testing and rated -20°C to +50°C."),
      (f"How are the trucks shipped to {country} and how long does it take?",
       f"Units ship RoRo or flat-rack container to {port}. Typical transit from China: {transit}. We handle export customs, and your local agent handles import clearance with the documents we provide (B/L, CO, homologation papers)."),
    ]
    faq_ld = {"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
      {"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}} for q,a in faq]}
    faq_html = "".join(f'<div class="faq-item"><h4>{q}</h4><p>{a}</p></div>' for q,a in faq)
    others = [x for x in MARKETS if x[0]!=slug and x[2]==region][:3]
    oth_html = "".join(f'<a class="btn btn-outline" href="{o[0]}.html" style="margin:4px;">{o[1]}</a>' for o in others)
    html = head(f"Electric Trucks for {country} — Dongfeng EV Export | Fenghan",
        f"Dongfeng electric trucks for {country}: battery-electric tractors, dump trucks, cargo trucks and municipal vehicles. Shipping to {port}. FOB/CIF quote in 24h.",
        f"electric trucks {country.lower()}, Dongfeng electric truck {country.lower()}, electric dump truck {country.lower()}, electric cargo truck {country.lower()}, EV truck price {country.lower()}, buy electric truck {country.lower()}, electric truck import {country.lower()}",
        url, P, faq_ld)
    html += f"""
{HEADER.replace('{P}',P)}
<div class="page-hero-sm">
  <div class="section-inner">
    <div class="bc"><a href="{P}index.html">Home</a> &rsaquo; <a href="index.html">Markets</a> &rsaquo; {country}</div>
    <h1>Electric Trucks for {country}</h1>
    <p>{region} · Shipping to {port} · {side}</p>
  </div>
</div>
<main class="section"><div class="section-inner">
  <div class="section-title"><h2>Why {country}, Why Now</h2></div>
  <p style="font-size:16px;line-height:1.8;max-width:900px;">{hook} Fenghan Trading — authorized Dongfeng new-energy exporter based in Xi'an, China — configures each truck for {country}: battery size, charging standard, climate package and ({side}) drive.</p>
  <div class="section-title" style="margin-top:28px;"><h2>Recommended for {country}</h2></div>
  {cards}
  <div class="section-title" style="margin-top:28px;"><h2>Import &amp; Charging Notes — {country}</h2></div>
  <ul class="tick">
    <li>Drive configuration: {side}</li>
    <li>Arrival port: {port}</li>
    <li>Sea transit from China: {transit}</li>
    <li>{note}</li>
    <li>Documents supplied: B/L, commercial invoice, packing list, certificate of origin, homologation papers</li>
    <li>Charging advice, site survey support and driver training available for fleet orders (5+ units)</li>
  </ul>
  <div class="section-title" style="margin-top:28px;"><h2>FAQ — {country}</h2></div>
  {faq_html}
  <div style="margin-top:24px;"><strong>Nearby markets:</strong><br>{oth_html}</div>
</div></main>
{cta_band(P, f"Start your {country} EV fleet quote")}
{FOOTER.replace('{P}',P)}
</body>
</html>"""
    with open(os.path.join(BASE,'markets',slug+'.html'),'w',encoding='utf-8') as f:
        f.write(html)
    market_urls.append(url)
print("markets:", len(market_urls))

# ---------------- MARKETS INDEX ----------------
P = "../"
lis = "".join(f'<li style="margin:6px 0;"><a href="{m[0]}.html" style="color:var(--primary);font-weight:600;">Electric Trucks for {m[1]}</a> <span style="color:#777;font-size:13px;">· {m[2]} · {m[3]}</span></li>' for m in MARKETS)
idx = head("Markets — Dongfeng Electric Trucks Export to 60+ Countries",
  "Dongfeng electric trucks by market: country-specific guides for Africa, Middle East, Central Asia, Latin America and Southeast Asia. Ports, drive side, recommended models.",
  "electric trucks by country, Dongfeng EV export markets, electric truck Africa, electric truck Middle East, electric truck Latin America, electric truck Southeast Asia",
  f"{SITE}/markets/index.html", P,
  {"@context":"https://schema.org","@type":"CollectionPage","name":"Dongfeng EV Export Markets"})
idx += f"""
{HEADER.replace('{P}',P)}
<div class="page-hero-sm">
  <div class="section-inner">
    <div class="bc"><a href="{P}index.html">Home</a> &rsaquo; Markets</div>
    <h1>Markets We Serve</h1>
    <p>Country-by-country guides: recommended models, ports, drive side, transit times and import notes.</p>
  </div>
</div>
<main class="section"><div class="section-inner">
  <ul style="list-style:none;padding:0;columns:2;column-gap:48px;">{lis}</ul>
</div></main>
{cta_band(P, "Your market not listed? We ship to 60+ countries")}
{FOOTER.replace('{P}',P)}
</body>
</html>"""
with open(os.path.join(BASE,'markets','index.html'),'w',encoding='utf-8') as f:
    f.write(idx)
market_urls.append(f"{SITE}/markets/index.html")

# ---------------- SITEMAP ----------------
sm_path = os.path.join(BASE,'sitemap.xml')
sm = open(sm_path,encoding='utf-8').read()
new_entries = ""
for u in model_urls + market_urls:
    new_entries += f'  <url><loc>{u}</loc><lastmod>{TODAY}</lastmod><changefreq>monthly</changefreq><priority>0.8</priority></url>\n'
sm = sm.replace('</urlset>', new_entries + '</urlset>')
open(sm_path,'w',encoding='utf-8').write(sm)
print("sitemap urls:", sm.count('<url>'))

# ---------------- CATEGORY PAGE INTERNAL LINKS ----------------
cat_map = {"electric-tractor":"Electric Tractor","electric-dump":"Electric Dump Truck",
           "electric-cargo":"Electric Cargo Truck","electric-special":"Electric Special Vehicle"}
for cat,cn in cat_map.items():
    path = os.path.join(BASE,'products',cat+'.html')
    h = open(path,encoding='utf-8').read()
    if 'products/models/' in h:
        print(cat, "already linked"); continue
    rel = [m for m in MODELS if m[2]==cat]
    links = "".join(f'<a class="btn btn-outline" href="models/{m[0]}.html" style="margin:4px;">{m[1]}</a>' for m in rel)
    block = f"""<section class="section"><div class="section-inner">
  <div class="section-title"><h2>Model-by-Model Detail Pages</h2></div>
  <p>Full specifications, applications and FAQ for each {cn.lower()} model:</p>
  <div>{links}</div>
</div></section>
"""
    h = h.replace('<footer class="footer">', block + '<footer class="footer">', 1)
    open(path,'w',encoding='utf-8').write(h)
    print(cat, "links injected:", len(rel))

# ---------------- llms.txt ----------------
ll = os.path.join(BASE,'llms.txt')
if os.path.exists(ll):
    t = open(ll,encoding='utf-8').read()
    add = "\n## Model detail pages\n" + "\n".join(f"- {SITE}/products/models/{m[0]}.html — Dongfeng {m[1]} {m[3]}" for m in MODELS)
    add += "\n\n## Market guides\n" + "\n".join(f"- {SITE}/markets/{m[0]}.html — Electric trucks for {m[1]}" for m in MARKETS)
    open(ll,'w',encoding='utf-8').write(t.rstrip()+"\n"+add+"\n")
    print("llms.txt updated")

with open(os.path.join(BASE,'_new_urls.txt'),'w') as f:
    f.write("\n".join(model_urls+market_urls))
print("DONE")
