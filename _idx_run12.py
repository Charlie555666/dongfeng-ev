# -*- coding: utf-8 -*-
import re

ROOT = r"C:\Users\69498\WorkBuddy\20260605101515\dongfeng-ev-repo"

# (filename, title, description)
ARTICLES = [
("how-long-does-electric-truck-battery-really-last.html",
 "How Long Does an Electric Truck Battery Really Last? LFP Cycle Life, Warranties and Degradation Explained",
 "The straight answer on EV truck battery life: CATL LFP packs warranted 8 years/4,500 cycles to 70-80% SOH, 3-5% annual degradation, the habits that stretch pack life and how certificates protect resale value."),
("how-much-does-electric-dump-truck-cost-china-fob.html",
 "How Much Does an Electric Dump Truck Cost from China? FOB Price Guide 2026",
 "Electric dump truck FOB prices from $95,000 to $180,000: TZ5E, KTA1 and TZ3V price bands, battery cost drivers, landed-cost math, swap finance and the 2-4 year payback arithmetic."),
("johannesburg-gauteng-electric-truck-freight.html",
 "Johannesburg and Gauteng Freight: How Electric Dump Trucks and EV Truck Rigids Are Cutting Costs in South Africa's Industrial Heart",
 "Gauteng EV truck strategy: TZ3Z and KTA1 electric dump trucks on Reef aggregates and construction loops, Eskom tariffs, load-shedding-proof depots and a 12-truck TCO for South Africa."),
("lahore-pakistan-electric-delivery-truck-fleet.html",
 "Lahore Distribution Fleets Go Electric: KT5J and KT5M Electric Delivery Truck Economics in Pakistan's Second City",
 "Lahore EV truck economics: KT5J and KT5M electric delivery trucks on Punjab distribution, 1% EV import duty, BESS-buffered depots and a 15-truck TCO with 18-month infrastructure payback."),
("guadalajara-mexico-electric-delivery-truck.html",
 "Guadalajara's Next Fleet: Why Jalisco Manufacturers and Distributors Are Trial-Running the KT5J Electric Delivery Truck",
 "Guadalajara EV truck strategy: KT5J electric delivery trucks for Jalisco manufacturing loops, Mexico EV tariff treatment, CFE night tariffs and a 12-truck metro TCO."),
("cali-colombia-sugar-corridor-electric-truck.html",
 "Cali and the Cauca Sugar Corridor: Electric Dump Trucks and the EV Truck Case for Colombia's Valle del Cauca",
 "Cali sugar-corridor EV truck economics: TZ5E electric dump trucks on 24/7 mill haulage, bagasse-power charging under $0.02/kWh effective, Colombia EV tariffs and 24-month fleet payback."),
("bangkok-thailand-electric-truck-urban-logistics.html",
 "Bangkok's Delivery Grid: KT5M Electric Box Trucks and the EV Truck Economics of Thailand's Mega-City Distribution",
 "Bangkok EV truck strategy: KT5M electric box trucks on 20 km/h delivery grids, MEA time-of-use tariffs, reefer bodies and the flood-season depot spec for Thai distribution fleets."),
("almaty-kazakhstan-electric-truck-distribution.html",
 "Almaty Distribution: KTH3 Electric Cargo Trucks and the EV Truck Opportunity in Kazakhstan's Commercial Capital",
 "Almaty EV truck analysis: KTH3 electric cargo trucks on Kazakh distribution duty, the -25 C winter file with pack pre-heating, EAEU import mechanics and a 10-truck TCO."),
("jeddah-saudi-electric-truck-port-logistics.html",
 "Jeddah Port and the Red Sea Corridor: TE46 and TE8M Electric Tractors as the EV Truck Play for Saudi Arabia's Western Gateway",
 "Jeddah drayage electrification: TE46 and TE8M electric tractors on Red Sea container duty, 45 C heat engineering, SASO import compliance and solar-PPA paybacks under 24 months."),
("abu-dhabi-electric-sanitation-fleet.html",
 "Abu Dhabi's Municipal Mandate: KT3E Garbage Trucks and KT1D Sweepers as the EV Truck Backbone of Emirate Sanitation",
 "Abu Dhabi sanitation EV trucks: KT3E electric garbage trucks and KT1D sweepers on Tadweer duty, electric compactor PTO economics, desert-heat spec and tender-scoring advantages."),
("davao-philippines-agri-electric-truck.html",
 "Davao and Mindanao Agri-Logistics: KTH3 and KT5J Electric Trucks Carrying the Southern Philippines' Harvest",
 "Davao agri-logistics EV trucks: KTH3 and KT5J electric trucks on Mindanao banana and fruit corridors, EVIDA duty exemptions, cheap Mindanao power and a 10-truck TCO."),
("da-nang-vietnam-electric-truck-port-city.html",
 "Da Nang's Port City Boom: KT5M and TE8M Electric Trucks on Vietnam's Central Coast Growth Corridor",
 "Da Nang EV truck strategy: KT5M electric box trucks and TE8M tractors on Tien Sa port and Central Vietnam logistics, ACFTA duty and Vietnam's 75-80% energy saving window."),
("oran-algeria-electric-truck-port-fleet.html",
 "Oran and Algeria's Second Coast: TZ5E and KTA1 Electric Dump Trucks for the West Algerian Construction Revival",
 "Oran EV truck analysis: TZ5E and KTA1 electric dump trucks on West Algerian duty, the subsidised-diesel paradox priced honestly, maintenance savings and import structuring."),
("takoradi-ghana-manganese-electric-truck.html",
 "Takoradi's Export Rails: TE46 Electric Tractors and KTA1 Tippers on Ghana's Manganese and Bauxite Corridor",
 "Takoradi corridor EV trucks: TE46 electric tractors on Ghana's manganese runs, KTA1 quarry tippers, duty-exempt EV imports and 14-22 month heavy-fleet payback."),
("eldoret-kenya-tea-highlands-electric-truck.html",
 "Eldoret and the Tea Highlands: KT5M Electric Box Trucks on Kenya's Rift Valley Agri-Corridor",
 "Eldoret EV truck strategy: KT5M and KTH3 electric cargo trucks on Rift Valley tea, dairy and grain corridors, altitude torque advantages, regen on the grades and Kenya duty exemptions."),
("port-harcourt-nigeria-electric-truck-logistics.html",
 "Port Harcourt and the Niger Delta: KT5M and KTH3 Electric Trucks Rethinking Oil-Country Logistics",
 "Niger Delta EV truck strategy: KT5M and KTH3 electric trucks on Port Harcourt oil-services and distribution duty, fuel-independence security economics and Nigeria's new EV tariff lines."),
("mandalay-myanmar-dry-zone-electric-truck.html",
 "Mandalay and the Dry Zone: KTH3 Electric Cargo Trucks on Myanmar's Upper Country Grain Corridor",
 "Mandalay EV truck analysis: KTH3 electric cargo trucks on dry-zone grain corridors, hydropower economics, Muse border-trade import mechanics and an honest risk framework."),
("tanzania-cashew-corridor-electric-truck.html",
 "Tanzania's Cashew Corridor: KT5M Electric Box Trucks from Mtwara's Grove Gates to the Indian Ocean Ports",
 "Tanzania cashew EV truck strategy: KT5M electric box trucks on the Mtwara-Lindi corridor, seasonal duty sizing, TANESCO off-peak charging and the processing-plant anchor model."),
("chile-lithium-triangle-electric-heavy-haul.html",
 "The Lithium Triangle Needs Trucks: TE8P Electric Tractors on Chile's Atacama Brine and Battery-Metal Corridors",
 "Atacama EV truck strategy: TE8P electric tractors on Chile's lithium corridors, sub-$0.05/kWh solar PPAs, altitude torque and the green-lithium supply-chain story miners now bid on."),
("vietnam-seafood-cold-chain-electric-truck.html",
 "Vietnam's Seafood Cold Chain: KT5L Electric Reefer Trucks from Mekong Ponds to Cat Lai's Freezer Gates",
 "Vietnam seafood cold chain EV trucks: KT5L electric reefers on Mekong Delta duty, the two-engine cost structure eliminated, EVN tariffs and 20-26 month fleet payback."),
("johor-data-center-construction-electric-truck.html",
 "Johor's Data Center Boom: TZ8J Electric Mixers and KTA1 Tippers Building Southeast Asia's AI Backbone",
 "Johor DC construction EV trucks: TZ8J electric mixers and KTA1 tippers on hyperscale data center pours, night-shift concrete duty, NETR incentives and ESG tender scoring."),
("solar-farm-construction-electric-truck-fleet.html",
 "Solar Farm Construction Fleets: KTA1 Electric Tippers and TE8M Tractors Building the Gulf and Africa's Gigawatt Sites",
 "Utility-scale PV construction EV trucks: KTA1 tippers and TE8M tractors on gigawatt sites, construction-substation charging, zero-exhaust site mandates and relocatable depot economics."),
("steel-mill-scrap-inbound-electric-truck.html",
 "Steel Mill Inbound Logistics: TE8M Electric Tractors and KTA1 Tippers on the Scrap and Raw Materials Loop",
 "Steel mill EV truck strategy: TE8M electric tractors on scrap loops and KTA1 tippers on stockyard duty, arc-furnace energy synergy, cheap night-tariff charging and green-steel accounting."),
("pantograph-opportunity-charging-electric-truck-port.html",
 "Pantograph Opportunity Charging at Ports: The EV Truck Technology That Turns Yard Queues into Range",
 "Pantograph opportunity charging for EV truck port fleets: how 350-600 kW overhead top-ups convert gate and crane queues into range, the dwell-time study and battery-versus-infrastructure math."),
("electric-truck-battery-swap-station-siting.html",
 "Siting a Battery Swap Station: The Civil, Grid and Permitting Engineering Behind 5-Minute EV Truck Swaps",
 "EV truck battery swap station siting: the five-gate engineering review — duty-cycle math, grid connection, land geometry, safety and permitting, and the honest operator economics."),
("ev-truck-battery-theft-depot-security.html",
 "Battery Theft and Depot Security: Protecting Six-Figure EV Truck Packs in Emerging Market Fleets",
 "EV truck battery theft prevention: the threat model, telematics and remote lockout, pack lockout hardware, custody procedures, depot layering and the insurance file that gets fleets quoted."),
("ev-truck-battery-second-life-mini-grid-storage.html",
 "Retired Packs, Second Lives: Turning EV Truck Batteries into Mine-Site and Village Mini-Grid Storage",
 "Second-life EV truck batteries: retired CATL packs as mine-site and micro-grid storage, SOH economics worth $25,000-45,000 per pack, repurposing engineering and contract lines that preserve value."),
("how-to-read-electric-truck-spec-sheet.html",
 "How to Read an EV Truck Spec Sheet: The Twelve Numbers That Actually Predict Fleet Performance",
 "EV truck spec-sheet literacy: usable kWh, loaded consumption, continuous power, gradeability, warranty structure and charge curve — the twelve numbers that decide fleet economics."),
("green-finance-development-banks-electric-truck-africa.html",
 "Green Finance for African EV Truck Fleets: How Development Bank Credit Lines Actually Get Drawn",
 "Green finance for African EV truck fleets: IFC and AfDB climate credit lines, 150-400 basis point pricing advantages, eligibility paperwork, monitoring covenants and a $2M fleet structure."),
("kenya-electric-mobility-policy-ev-trucks.html",
 "Kenya's Electric Mobility Policy: What the Framework Means for Commercial EV Truck Importers and Fleet Buyers",
 "Kenya EV policy for truck importers: duty exemptions worth $12,000-17,000 per truck, KEBS PVoC mechanics, charging standards and the importer's checklist for the current window."),
("nigeria-electric-vehicle-policy-ev-truck-importers.html",
 "Nigeria's National EV Policy: What New Tariff Lines Mean for Electric Truck Importers",
 "Nigeria EV policy analysis: new EV tariff lines worth $15,000-22,000 per truck, SONCAP conformity, buffered-depot charging strategy and the fiscal window for Nigerian fleet importers."),
("ev-truck-driver-recruitment-retention.html",
 "Recruiting the Electric Fleet's Drivers: Why EV Truck Adoption Starts With HR, Not Hardware",
 "EV truck driver recruitment and retention: why electric fleets attract better applicants, the five-day training economics, regen-based incentives that avoid mission gaming and adoption tactics."),
("scaling-electric-truck-fleet-10-to-100.html",
 "Scaling From Ten to a Hundred EV Trucks: The Operations Playbook for Multi-Stage Fleet Growth",
 "EV truck fleet scaling playbook: energy-based charger sizing, two-tier technician structures, min-max spares, range-aware dispatch and the stage-by-stage systems that replace pilot-era memory."),
("6x4-vs-8x4-electric-dump-truck-configuration.html",
 "6x4 or 8x4? Choosing the Right Electric Dump Truck Configuration for Your Haul Duty",
 "6x4 vs 8x4 electric dump truck decision guide: payload and GVW headroom, battery as fixed tare, energy per tonne, tyre budgets and the mission-backward method for buyers."),
("tz3z-vs-tz5e-city-dump-truck-choice.html",
 "TZ3Z vs TZ5E: Which Dongfeng Electric Dump Truck Wins City Construction Duty?",
 "Dongfeng TZ3Z vs TZ5E comparison: 8x4 city construction specialist against the 6x4 hauler — payload, cost, manoeuvrability and the fleet-mix answer most construction operators need."),
("tz3v-andes-altitude-copper-mine-electric-dump.html",
 "TZ3V at 4,500 Metres: Field Notes on Dongfeng's 8x4 Electric Dump Truck in High-Andean Copper Service",
 "High-altitude EV truck engineering: why electric torque ignores thin air, TZ3V thermal management at 4,500 m, regenerative haul descents and the Andean mining fleet pilot design."),
("saudi-aggregates-giga-project-electric-dump-truck.html",
 "Feeding the Giga-Projects: Electric Dump Truck Aggregates Strategy for Saudi Arabia's Construction Supercycle",
 "Saudi giga-project aggregates EV trucks: TZ3V and KTA1 electric dump trucks on NEOM and Qiddiya quarry corridors, 50 C desert spec, SASO compliance and solar-PPA fleet economics."),
("kt5m-beverage-plant-distribution-electric.html",
 "Bottling Plants and the Electric Box Truck: KT5M Fleet Economics for Beverage Distribution in Hot Climates",
 "Beverage distribution EV trucks: KT5M electric box trucks on bottling plant outbound duty, plant-gate charging at industrial tariffs, reefer options and driver retention in tropical heat."),
("kt1d-waste-transfer-station-electric.html",
 "The Waste Transfer Station Opportunity: KT1D Electric Garbage Trucks on Second-Shift Compaction and Haul-Out",
 "Transfer station EV truck strategy: KT1D electric garbage trucks on compaction and landfill haul-out, night-shift quiet advantages, TCO per tonne transferred and concession bidding."),
("dominican-republic-tourism-construction-electric-truck.html",
 "Building for Tourists: TZ5E Electric Tippers and KT5M Box Trucks on the Dominican Republic's Hotel Construction Boom",
 "Dominican Republic tourism construction EV trucks: TZ5E electric tippers on Punta Cana hotel builds, KT5M resort supply, DR import mechanics and the ESG scoring that wins resort tenders."),
]

# ---- 1. Update blog/index.html ----
idx_path = ROOT + r"\blog\index.html"
t = open(idx_path, encoding="utf-8").read()

cards = "\n".join(
    f'<li><a href="{fn}">{title}</a><br><span style="color:#666;font-size:14px;">{desc}</span></li>'
    for fn, title, desc in ARTICLES
)

anchor = '<h2>Latest articles</h2>\n<ul>'
if anchor not in t:
    # try variations
    m = re.search(r'<h2>Latest articles</h2>\s*<ul>', t)
    assert m, "anchor not found"
    t = t[:m.end()] + "\n" + cards + t[m.end():]
else:
    t = t.replace(anchor, anchor + "\n" + cards, 1)

# update dateModified
t = re.sub(r'"dateModified": "[^"]+"', '"dateModified": "2026-09-23"', t, count=1)
open(idx_path, "w", encoding="utf-8", newline="\n").write(t)
print("index.html updated: 40 cards prepended, dateModified -> 2026-09-23")

# ---- 2. Update sitemap.xml ----
sm_path = ROOT + r"\sitemap.xml"
s = open(sm_path, encoding="utf-8").read()
entries = "\n".join(
    f'  <url><loc>https://dongfengevtrucks.com/blog/{fn}</loc><lastmod>2026-09-23</lastmod><changefreq>monthly</changefreq><priority>0.7</priority></url>'
    for fn, _, _ in ARTICLES
)
assert "</urlset>" in s
s = s.replace("</urlset>", entries + "\n</urlset>", 1)
open(sm_path, "w", encoding="utf-8", newline="\n").write(s)
n = s.count("<url>")
print(f"sitemap.xml updated: 40 URLs added, total {n} <url> entries")

# ---- 3. XML validity check ----
import xml.etree.ElementTree as ET
ET.parse(sm_path)
print("sitemap XML parse: OK")
