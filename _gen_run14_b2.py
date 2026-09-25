# -*- coding: utf-8 -*-
"""Run 14 batch 2: 8 articles (DRC/West Africa mining/LatAm cities + 2 competitor comparisons)."""
import re, os
from _gen_run14_b1 import build, ARTICLES as _none  # reuse build()

ROOT = os.path.dirname(os.path.abspath(__file__))

ARTICLES = []

# ---------------------------------------------------------------- 9
ARTICLES.append(dict(
f='kinshasa-drc-electric-truck-city-logistics',
t='Kinshasa City Logistics: KTH3 Electric Cargo Trucks for the DRC&rsquo;s Mega-City Freight',
d='Kinshasa&rsquo;s 17-million-person freight market runs on short urban hauls. KTH3 electric cargo truck range, TCO and charging for this EV truck opportunity in the DRC.',
k='KTH3 electric cargo truck, EV truck DR Congo, electric truck Kinshasa, electric truck DRC logistics, Dongfeng electric truck, electric cargo truck Central Africa',
img='models/p07_01.jpg',
alt='Dongfeng KTH3 electric cargo truck on a Kinshasa freight run, EV truck for DR Congo city logistics',
net='zhc',
body='''
<p>Kinshasa is one of the world&rsquo;s largest cities without a functioning rail freight network &mdash; 17 million people fed, clothed and supplied almost entirely by truck. Everything arrives through the port of Matadi 350 km downriver or across the Congo from Brazzaville, and from the city&rsquo;s river ports and wholesale markets, an enormous fleet of 10-28 t trucks fans out through some of the most congested streets in Africa. Fuel in the DRC is expensive, supply is insecure, and diesel quality varies enough to shorten engine life measurably. This article examines the <a href="../products/models/kth3-electric-cargo-truck.html">Dongfeng KTH3 electric cargo truck</a> for Kinshasa&rsquo;s city logistics &mdash; a market where the EV truck case rests less on policy fashion and more on brutal operating arithmetic.</p>

<h2>A Freight System Built for Depot Charging</h2>
<p>Kinshasa&rsquo;s distribution geography is a planner&rsquo;s gift for electrification. The wholesale clusters &mdash; the Zando market zone, the Kingabwa industrial district near the river port, the Limete industrial exchange &mdash; sit within a 25 km radius. A typical rigid cargo truck covers 60-140 km daily between the river ports, the markets and the city&rsquo;s sprawling retail fabric, then returns to a secured yard. Security is the decisive operational fact in Kinshasa: trucks already sleep in guarded, walled depots with generator backup, which means the charging infrastructure lands inside an existing security perimeter. The KTH3&rsquo;s 200-240 km loaded range covers two to three days of typical city duty per charge; even the heaviest-utilisation trucks on market supply runs charge only nightly.</p>
<p>The congestion factor tilts the comparison further. Kinshasa traffic is severe even by West and Central African standards, and a diesel truck in four-hour congestion burns fuel at its least efficient point while its clutch and cooling system take the punishment. The electric drivetrain consumes essentially nothing at standstill, delivers instant torque for the stop-start rhythm, and regenerates on every one of the hundreds of daily decelerations. In our Lagos and Abidjan fleet data &mdash; the closest analogues to Kinshasa traffic &mdash; severe congestion improves the EV truck&rsquo;s relative economy by 10-15% over open-road comparisons.</p>

<h2>KTH3 Specifications for Kinshasa Duty</h2>
<table style="width:100%;border-collapse:collapse;margin:20px 0;" border="1" cellpadding="8">
<tr style="background:#006341;color:#fff;"><th style="padding:8px;text-align:left;">Parameter</th><th style="padding:8px;text-align:left;">KTH3 6x4 Electric Cargo Truck</th></tr>
<tr><td style="padding:8px;">GVW / payload</td><td style="padding:8px;">28 t / 18-20 t (box, stake or dropside)</td></tr>
<tr><td style="padding:8px;">Battery</td><td style="padding:8px;">350 kWh CATL LFP, liquid-cooled</td></tr>
<tr><td style="padding:8px;">Motor</td><td style="padding:8px;">LvKong 360 kW peak / 2,400 Nm</td></tr>
<tr><td style="padding:8px;">Range (urban, loaded)</td><td style="padding:8px;">200-240 km</td></tr>
<tr><td style="padding:8px;">DC charge 20-80%</td><td style="padding:8px;">~50 min at 240 kW</td></tr>
<tr><td style="padding:8px;">Wading / sealing</td><td style="padding:8px;">IP67 HV system &mdash; rainy-season street flooding tolerant</td></tr>
<tr><td style="padding:8px;">Battery warranty</td><td style="padding:8px;">8 years / 4,500 cycles to 70% SOH</td></tr>
<tr><td style="padding:8px;">FOB price band</td><td style="padding:8px;">US$88,000-105,000</td></tr>
</table>
<p>Three features answer Kinshasa-specific questions. First, the IP67-sealed high-voltage system: the city&rsquo;s rainy season floods arterial streets axle-deep, and diesel trucks drown their intakes in exactly these conditions every November; the electric drivetrain has no intake and no exhaust. Second, the absence of a fuel system removes the single largest maintenance curse of DRC fleets &mdash; contaminated diesel destroying injection systems. Third, the LvKong motor&rsquo;s torque delivery suits the overloaded-start reality of market freight: full torque from standstill, on loose surfaces, without clutch slip.</p>

<h2>TCO Where Diesel Costs What It Costs in Kinshasa</h2>
<p>DRC diesel retails around US$1.30-1.50 per litre in Kinshasa when supply is normal, and effectively more when scarcity pricing bites. A 28 t rigid on city duty burns 0.50-0.60 L/km in congestion: US$0.70-0.85 per kilometre. The KTH3 consumes 1.35-1.55 kWh/km urban loaded; at SNEL industrial tariffs of roughly US$0.10-0.12/kWh &mdash; among Africa&rsquo;s lowest, thanks to Inga hydropower &mdash; that is US$0.15-0.18 per kilometre. On 3,000 km per month, the energy saving is US$1,650-2,000 per truck monthly. Maintenance adds US$600-900 monthly against a diesel calendar that in DRC conditions includes frequent injection and fuel-system work. Combined annual saving: US$27,000-35,000 per truck. Against a purchase premium of US$35,000-45,000, payback lands in 14-19 months. Few markets in the world stack the EV truck advantages this high: cheap hydro power, expensive diesel, short routes, brutal congestion.</p>
<ul>
<li><strong>Energy per km:</strong> US$0.70-0.85 diesel vs US$0.15-0.18 electric &mdash; ~75% lower</li>
<li><strong>Annual saving per truck:</strong> US$27,000-35,000 combined</li>
<li><strong>Payback:</strong> 14-19 months on city distribution duty</li>
<li><strong>Fuel-security hedge:</strong> charging from Inga hydro removes exposure to diesel import disruptions</li>
</ul>

<h2>Power and Charging: The Honest Infrastructure Section</h2>
<p>Kinshasa&rsquo;s grid has capacity in the industrial corridors &mdash; Kingabwa and Limete host medium-voltage service &mdash; but reliability is the real question, and any honest electrification plan answers it directly. The answer has three layers. First, fleets are inherently buffered: ten KTH3s carry 3.5 MWh of storage, and a multi-hour outage simply resequences charging. Second, the depots already run generators; a hybrid controller lets the existing genset top up truck charging during outages at better efficiency than a truck&rsquo;s own diesel engine ever achieved. Third, solar is strong (4.5-5.0 peak sun hours) and yard canopies of 200-400 kWp offset 30-45% of charging energy while providing covered parking. The standard installation is one 240 kW DC charger per 4-6 trucks plus managed overnight AC &mdash; a 500-630 kVA service class that SNEL supplies to industrial customers in these districts.</p>

<h2>Import Path via Matadi</h2>
<p>Trucks enter the DRC through Matadi with 35-45 day sailings from China, then transit the Matadi-Kinshasa corridor by road or rail wagon. We deliver the complete French-language documentation set &mdash; homologation dossier, UN R100 battery certificates, customs files &mdash; and structure the delivery so trucks arrive charged and driveable off the vessel. DRC import duties on electric vehicles are materially lower than on diesel equivalents under the country&rsquo;s recent fiscal measures, and the DGDA process with proper documentation runs two to three weeks. Operators with cross-river or regional ambitions should review our <a href="../markets/tanzania.html">Tanzania market page</a> for the East African corridor context &mdash; DRC freight groups increasingly operate across both markets, and platform standardisation halves the support burden.</p>
<p>Service in the DRC follows our remote-support model: an extended first-line parts kit ships with the fleet (the honest response to DRC logistics friction), CATL modules route through regional stock at 14-21 days, and the telematics portal gives our engineers live drivetrain visibility. The maintenance calendar itself &mdash; brakes, coolant, software &mdash; removes the imported-engine-parts dependency that grounds Kinshasa&rsquo;s diesel fleet for weeks at a time.</p>

<h2>Who Moves First in Kinshasa</h2>
<p>The natural pioneers are the brewery and beverage distributors &mdash; dense freight, fixed routes, the highest utilisation in the city &mdash; followed by the FMCG importers running Kingabwa-to-market loops and the construction-materials suppliers feeding Kinshasa&rsquo;s permanent building boom. For all of them, the proposition is identical: the cheapest electrons in Africa, the most expensive diesel logistics in Africa, and a duty cycle that fits inside one battery charge. Kinshasa will electrify because the arithmetic leaves no alternative; the only question is which fleets bank the advantage first.</p>
'''))

# ---------------------------------------------------------------- 10
ARTICLES.append(dict(
f='bamako-mali-gold-mining-electric-truck',
t='Bamako Gold Belt: TZ5Y Electric Mining Trucks for Mali&rsquo;s Gold Country',
d='Mali is Africa&rsquo;s third gold producer and its mines burn imported diesel. TZ5Y 80t electric mining truck economics, solar charging and TCO for this EV truck application.',
k='TZ5Y electric mining truck, EV truck Mali, electric truck Bamako, electric mining truck gold, Dongfeng electric truck, mining EV truck West Africa, battery swap mining truck',
img='models/p02_00.jpg',
alt='Dongfeng TZ5Y 80t electric mining truck at a Mali gold mine, EV truck for West African mining',
net='zxc',
body='''
<p>Mali produces around 65-70 tonnes of gold a year from a belt of mines strung along the country&rsquo;s western and southern edges &mdash; Loulo-Gounkoto, Fekola, Syama, Morila &mdash; almost all of them hundreds of kilometres from the coast, all of them burning diesel that arrives by tanker convoy at a delivered cost that would shock a coastal operator. Mining fuel in landlocked Mali lands at US$1.60-2.00 per litre by the time it reaches site. This article examines the <a href="../products/models/tz5y-electric-dump-truck.html">Dongfeng TZ5Y 80-tonne electric mining truck</a> in Malian gold service: the haul profiles, the battery-swap architecture that makes 24/7 operation possible, the solar synergy that Mali&rsquo;s irradiance makes almost unfair, and the TCO that results. For mine operators, this EV truck is not an environmental statement; it is an attack on the single largest controllable cost in the operation.</p>

<h2>The Malian Haul Profile</h2>
<p>Open-pit gold haulage in Mali follows a classic pattern: short cycles (1.5-4 km one way), continuous 24/7 operation, and &mdash; critically &mdash; a loaded direction and an empty direction. Where the pit is below the waste dump, loaded trucks climb and empty trucks descend; several Malian operations have the inverse. The TZ5Y exploits both geometries. On loaded-climb profiles, its 510 kW LvKong drive holds speed on 10-12% ramps where diesel rigs drop gears and rev; the energy cost is real but the productivity gain (faster cycle times) partially pays for it. On loaded-descent profiles &mdash; ore at pit top, crusher below &mdash; regenerative braking recovers 20-30% of cycle energy, and some of our reference operations run loaded-downhill cycles at near net-zero energy. Either way, the diesel alternative burns fuel in both directions and its retarder grids in one.</p>

<h2>TZ5Y 80T: The Mining Specification</h2>
<table style="width:100%;border-collapse:collapse;margin:20px 0;" border="1" cellpadding="8">
<tr style="background:#006341;color:#fff;"><th style="padding:8px;text-align:left;">Parameter</th><th style="padding:8px;text-align:left;">TZ5Y 80T Electric Mining Truck</th></tr>
<tr><td style="padding:8px;">Payload / body</td><td style="padding:8px;">80 t class / 42-46 m&sup3; rock body</td></tr>
<tr><td style="padding:8px;">Battery</td><td style="padding:8px;">600 kWh CATL LFP, swap architecture</td></tr>
<tr><td style="padding:8px;">Drive</td><td style="padding:8px;">LvKong dual-motor, 510 kW peak / 4,800 Nm</td></tr>
<tr><td style="padding:8px;">Swap time</td><td style="padding:8px;">5-6 minutes, automated station</td></tr>
<tr><td style="padding:8px;">Cycles per charge (3 km loop, loaded climb)</td><td style="padding:8px;">18-24 cycles depending on profile</td></tr>
<tr><td style="padding:8px;">Gradeability</td><td style="padding:8px;">&ge;35% loaded</td></tr>
<tr><td style="padding:8px;">Ambient rating</td><td style="padding:8px;">-20&deg;C to +50&deg;C, liquid-cooled pack</td></tr>
<tr><td style="padding:8px;">FOB price band</td><td style="padding:8px;">US$165,000-185,000 (truck) + swap station package</td></tr>
</table>
<p>The +50&deg;C rating is not a brochure line in Mali &mdash; it is the operating reality of the Sahelian dry season, when ambient temperatures hit 42-45&deg;C and surface temperatures on the haul road go higher. The liquid-cooled CATL pack holds cell temperatures in the optimal band through these conditions, which is why LFP chemistry (thermally stable, degradation-tolerant at temperature) is the only credible choice for Sahelian mining. Our thermal field data from West African deployments shows liquid-cooled LFP packs retaining 92-94% capacity after 2,000 cycles at sustained high ambient &mdash; the difference between a five-year and an eight-year battery life.</p>

<h2>Swap Architecture: How 24/7 Electric Mining Works</h2>
<p>Battery swap is what converts the TZ5Y from a demonstration into a production tool. The truck hauls 18-24 cycles on a charge, drives into the swap station, and leaves 5-6 minutes later with a full pack &mdash; faster than a diesel rig refuels and re-greases. One station with 7-9 packs in rotation serves a fleet of 10-15 trucks on continuous operation; the packs charge on managed load at 200-300 kW each, which also happens to be the ideal charge rate for LFP longevity. The station itself is containerised and relocatable &mdash; when the pit phase moves, the station moves on a lowbed, an advantage diesel tank farms do not share. For Mali&rsquo;s contract miners moving between pits every few years, infrastructure mobility is a balance-sheet point, not a footnote.</p>

<h2>The Solar-Diesel Displacement Equation</h2>
<p>Mali receives 5.5-6.0 peak sun hours daily &mdash; among the best mining solar resources on earth &mdash; and most Malian mines already run or are building solar hybrids to displace genset diesel. Electric haul trucks are the largest single new load a mine can add, but they are also the most schedulable: packs charge preferentially in the solar peak, and the swap station&rsquo;s buffer storage smooths the duck curve. A 10-truck TZ5Y fleet consumes roughly 25-35 MWh daily; a 15-20 MWp solar addition plus existing hybrid plant covers the daytime share. The diesel arithmetic is brutal by comparison: a 10-truck diesel fleet at this scale burns 45,000-60,000 litres monthly, delivered by tanker over roads that define &ldquo;logistics risk.&rdquo; Every solar-charged cycle is a litre that never left Bamako on a truck.</p>
<ul>
<li><strong>Delivered diesel cost:</strong> US$1.60-2.00/L at Malian mine sites</li>
<li><strong>Energy per cycle:</strong> diesel ~28-34 L vs electric ~28-35 kWh (profile-dependent)</li>
<li><strong>Fuel cost per cycle:</strong> US$50-65 diesel vs US$8-14 solar-hybrid electric</li>
<li><strong>Payback vs diesel fleet:</strong> 24-36 months including swap infrastructure</li>
<li><strong>Underground/ventilation bonus:</strong> zero exhaust particulates for any decline or pit-bottom work</li>
</ul>

<h2>Import and Regional Mining Context</h2>
<p>Mining equipment enters Mali through the Dakar or Abidjan corridors under the mining code&rsquo;s import provisions; we structure deliveries via either port with full transit documentation and French-language technical files. The trucks ship flat-rack or RoRo to Dakar (30-36 days), then lowbed to site. For operators running multi-country Sahelian portfolios, our <a href="../markets/ghana.html">Ghana market page</a> covers the parallel gold-belt electrification underway there &mdash; the same TZ5Y platform serves Birimian geology across the region, and regional miners standardising on one electric haul platform share swap-station spares, technician training and CATL module stock. That regional standardisation is already happening among the mid-tier gold groups.</p>
<p>On-site support is structured for remote operations: commissioning engineers on site for the swap-station build and the first 90 days, an extended parts kit sized for Sahelian logistics, and remote telemetry that lets our engineering desk watch pack health, cycle efficiency and station utilisation in real time. The drivetrain&rsquo;s service load &mdash; brakes, coolant, suspension &mdash; is a fraction of the diesel rig&rsquo;s engine, transmission, retarder and aftertreatment calendar, and every avoided engine rebuild is six figures of avoided cost plus the truck-weeks of availability returned.</p>

<h2>The Strategic Case for Malian Gold</h2>
<p>Gold mining margins are made or lost on cost per tonne moved, and haulage is 30-50% of open-pit operating cost. A mine that cuts haulage energy cost by 60-70% while removing its diesel supply-chain vulnerability has changed its cost curve structurally &mdash; in a country where fuel logistics are a genuine operational risk, the security argument may outrank even the financial one. Mali&rsquo;s miners have already proven they will build energy infrastructure when the case is there; the solar hybrids came first, and the electric haul fleet is the obvious next load. The first Malian mine to run a full electric fleet will own the benchmark every feasibility study in the belt is then measured against.</p>
'''))

# ---------------------------------------------------------------- 11
ARTICLES.append(dict(
f='conakry-guinea-bauxite-electric-mining-truck',
t='Conakry Bauxite Corridor: TZ5Y Electric Mining Trucks for Guinea&rsquo;s Export Machine',
d='Guinea moves 100+ Mt of bauxite a year on diesel haul fleets. TZ5Y electric mining truck economics for Boke corridor haulage: specs, swap, solar and TCO inside.',
k='TZ5Y electric mining truck, EV truck Guinea, electric truck Conakry, bauxite haulage electric truck, Dongfeng electric truck, electric mining truck West Africa, Boke bauxite EV',
img='models/p02_01.jpg',
alt='Dongfeng TZ5Y electric mining truck hauling bauxite in Guinea, EV truck for Boke corridor mining',
net='zxc',
body='''
<p>Guinea ships more bauxite than any country on earth &mdash; over 100 million tonnes a year from the Bok&eacute; corridor to China&rsquo;s alumina refineries &mdash; and every tonne rides a truck at least twice: pit to crushing, crushing to port or river terminal. The corridor&rsquo;s haul fleets number in the thousands of trucks, burning imported diesel in a country that exports ore and imports every drop of fuel. This article examines the <a href="../products/models/tz5y-electric-dump-truck.html">Dongfeng TZ5Y electric mining truck</a> on Guinean bauxite duty: why the corridor&rsquo;s specific haul geometry is unusually kind to electrification, how swap infrastructure scales to multi-hundred-truck fleets, and what the TCO looks like against the diesel status quo. For the SMB-Winning, CBG and CDM-Chine scale operators, this EV truck question is arriving at feasibility-study level right now.</p>

<h2>Why Bauxite Haulage Electrifies Beautifully</h2>
<p>Bauxite is the ideal electric haul commodity for three physical reasons. First, density: at roughly 1.4-1.6 t/m&sup3;, bauxite fills a rock body by volume before it challenges the payload rating &mdash; the TZ5Y&rsquo;s 80 t capacity is used efficiently, unlike dense ores that weight-out early. Second, the corridor geometry: several Bok&eacute; operations haul from elevated plateaus down to coastal terminals, meaning the loaded direction is downhill. Regenerative braking on a loaded descent is the electric truck&rsquo;s killer application &mdash; our reference operations on comparable profiles recover 25-32% of cycle energy, and some loaded-downhill cycles approach energy neutrality. Third, the duty cycle is fixed-infrastructure: pits, crushers and terminals do not move for years, so charging and swap assets amortise over their full lives.</p>
<p>The fourth reason is fuel logistics. Diesel for the Bok&eacute; corridor lands at Conakry and moves 200+ km inland by tanker; the delivered cost at site runs US$1.40-1.70 per litre, and every litre&rsquo;s journey is itself diesel-powered. A mining corridor consuming hundreds of thousands of litres monthly is, in effect, running a second mining operation just to feed the first. Electrification collapses that parallel supply chain into a wire.</p>

<h2>TZ5Y on Bauxite Duty: Specification</h2>
<table style="width:100%;border-collapse:collapse;margin:20px 0;" border="1" cellpadding="8">
<tr style="background:#006341;color:#fff;"><th style="padding:8px;text-align:left;">Parameter</th><th style="padding:8px;text-align:left;">TZ5Y 80T Electric Mining Truck</th></tr>
<tr><td style="padding:8px;">Payload / body</td><td style="padding:8px;">80 t / 46-50 m&sup3; bauxite body (volume-optimised)</td></tr>
<tr><td style="padding:8px;">Battery</td><td style="padding:8px;">600 kWh CATL LFP, swap architecture</td></tr>
<tr><td style="padding:8px;">Drive</td><td style="padding:8px;">LvKong dual-motor 510 kW / 4,800 Nm</td></tr>
<tr><td style="padding:8px;">Swap time</td><td style="padding:8px;">5-6 min automated</td></tr>
<tr><td style="padding:8px;">Cycles per charge (15 km corridor leg)</td><td style="padding:8px;">8-12 loaded cycles, profile-dependent</td></tr>
<tr><td style="padding:8px;">Regeneration (loaded descent profile)</td><td style="padding:8px;">25-32% of cycle energy recovered</td></tr>
<tr><td style="padding:8px;">Ambient rating</td><td style="padding:8px;">to +50&deg;C, dust-sealed cab and HV system</td></tr>
<tr><td style="padding:8px;">FOB price band</td><td style="padding:8px;">US$165,000-185,000 + swap station package</td></tr>
</table>
<p>Dust is the Guinea-specific engineering conversation. Bok&eacute;&rsquo;s dry season generates bauxite dust loads that destroy air filters, contaminate engine oil and shorten diesel engine life to intervals operators measure in months. The electric drivetrain has no air filter, no oil to contaminate, and no combustion to protect; the sealed motor and liquid-cooled pack shrug off an environment that is genuinely hostile to diesel machinery. Cab pressurisation and filtration &mdash; standard on our mining spec &mdash; also matter for the workforce: operators finish shifts without the dust-and-exhaust exposure that drives turnover in corridor fleets.</p>

<h2>Scaling Swap to Corridor Fleets</h2>
<p>A single swap station serves 10-15 trucks; the Bok&eacute; corridor&rsquo;s larger fleets need a station network, and the network design follows the haul map. Stations site at the pit head and the terminal &mdash; trucks swap at whichever end the cycle dictates &mdash; with each containerised station holding 7-9 packs and drawing 1.5-2.5 MW managed. The corridor&rsquo;s grid is strengthening (the Souapiti and Kaleta hydropower cascade now feeds the coastal zone), and mining houses building captive hydro-solar hybrids can size truck charging into the same energy master plan. The relocatable nature of the stations matters here too: as pit phases advance along the corridor, stations leapfrog on lowbeds rather than being rebuilt.</p>
<p>Charge scheduling deserves one paragraph at corridor scale. With hundreds of packs in rotation, the swap network becomes a controllable load of tens of megawatts &mdash; large enough to participate in the grid, and valuable to schedule into solar peaks and hydro off-peak. Our fleet energy platform sequences pack charging against the mine&rsquo;s generation mix, which at corridor scale translates to double-digit percentage savings on the energy bill itself, beyond the diesel displacement.</p>

<h2>TCO at Corridor Scale</h2>
<p>The per-truck arithmetic first. A diesel 80 t-class rig on 15 km corridor legs burns 30-38 L per cycle; at US$1.50/L delivered, US$45-57 per cycle. The TZ5Y consumes 30-38 kWh per cycle net of regeneration; at corridor power costs of US$0.10-0.14/kWh, US$3.50-5.50 per cycle. On 20 cycles daily, 330 operating days, the annual saving per truck is US$270,000-330,000 in energy alone &mdash; plus maintenance savings of US$40,000-60,000 (no engine, transmission, or aftertreatment in a dust environment that destroys all three). Even accounting for swap infrastructure apportioned per truck, payback on the full electric premium runs 18-28 months. At a 100-truck fleet scale, the annual saving approaches US$30 million &mdash; a number that belongs in feasibility studies, not brochures.</p>
<ul>
<li><strong>Energy per cycle:</strong> US$45-57 diesel vs US$3.50-5.50 electric</li>
<li><strong>Annual saving per truck:</strong> US$300,000+ combined on high-utilisation corridor duty</li>
<li><strong>Payback:</strong> 18-28 months including swap infrastructure</li>
<li><strong>Diesel supply chain:</strong> tanker convoys replaced by a wire &mdash; a security and continuity gain, not just cost</li>
</ul>

<h2>Import and Regional Context</h2>
<p>Mining equipment for the corridor enters through Conakry&rsquo;s port under the mining code provisions; we deliver with full French documentation, flat-rack or RoRo (28-34 days from China), and coordinate the lowbed transit to Bok&eacute;. For operators benchmarking across West African mining jurisdictions, our <a href="../markets/ghana.html">Ghana market page</a> covers the gold-belt deployments using the same platform &mdash; the TZ5Y serves both commodities with common swap infrastructure, and regional mining groups are beginning to standardise their electric haul fleets on shared spares and training across countries.</p>
<p>Support for corridor fleets is engineered for scale: commissioning teams for each station, resident technical presence through ramp-up, parts warehousing sized to fleet count, and 24/7 telemetry monitoring of every pack and truck. The maintenance model inverts the diesel reality: instead of a large workshop organisation fighting dust-ingested engines, the fleet runs on a small team doing brakes, suspension and coolant, with battery modules swapped as line-replaceable units.</p>

<h2>The Corridor&rsquo;s Next Decade</h2>
<p>Guinea&rsquo;s bauxite sector is at an inflection: volumes keep rising, fuel costs are structural, and the offtakers &mdash; China&rsquo;s aluminium giants &mdash; increasingly ask about the carbon intensity of their supply chains. The corridor that electrifies first gains a cost advantage measured in dollars per tonne of delivered ore, a marketing advantage with every low-carbon-aluminium buyer, and an operational resilience that diesel logistics cannot match. The technology is no longer the question; the TZ5Y runs this duty today. The only variable left is which operator&rsquo;s name goes on the first fully electric bauxite fleet.</p>
'''))

# ---------------------------------------------------------------- 12
ARTICLES.append(dict(
f='ouagadougou-burkina-faso-electric-dump-truck',
t='Ouagadougou Construction &amp; Gold Logistics: TZ3V Electric Dump Trucks for Burkina Faso',
d='Burkina Faso&rsquo;s capital construction and gold supply chains suit the TZ3V electric dump truck: 600 kWh, 280-320 km range, solar charging. EV truck economics inside.',
k='TZ3V electric dump truck, EV truck Burkina Faso, electric truck Ouagadougou, electric dump truck Sahel, Dongfeng electric truck, mining supply electric truck West Africa',
img='models/p03_01.jpg',
alt='Dongfeng TZ3V electric dump truck on a Burkina Faso construction site, EV truck for Sahel logistics',
net='zxc',
body='''
<p>Ouagadougou sits at the centre of two freight economies. The first is urban: one of Africa&rsquo;s fastest-growing capitals is building roads, housing estates and commercial districts at a pace that keeps hundreds of tippers moving sand, laterite and aggregate daily. The second is mining logistics: Burkina Faso is a top-five African gold producer, and the capital is the supply and maintenance hub for mines strung across the country&rsquo;s north and west. Both economies run on diesel hauled 1,000+ km from coastal ports, at delivered prices that make every litre precious. This article examines the <a href="../products/models/tz3v-electric-dump-truck.html">Dongfeng TZ3V electric dump truck</a> for Burkinab&egrave; service &mdash; a heavy EV truck whose 600 kWh battery and solar-friendly duty cycle suit the Sahel better than almost any market we serve.</p>

<h2>Two Duty Cycles, One Truck</h2>
<p>The TZ3V&rsquo;s 8x4 chassis and 600 kWh CATL LFP pack deliver 280-320 km of loaded range &mdash; the figure that unlocks Burkina Faso&rsquo;s geography. For urban construction, it is absurd overcapacity: a city tipper runs 120-180 km daily, so the truck charges every second night and the depot&rsquo;s power demand halves. For mine-supply duty, the range covers the real corridors: Ouagadougou to the Kalsaka/Yako zone (80 km), to the Perkoa area (120 km), or midway staging toward the western mines. The same truck platform serves the construction company by week and the mine-supply contractor by season &mdash; fleet utilisation in Burkina Faso follows the construction and mining calendars, and a long-range chassis lets one asset chase both revenue streams.</p>
<p>The Sahelian environment shapes the specification. Dry-season ambient temperatures hit 40-44&deg;C; the liquid-cooled LFP pack holds its thermal band where air-cooled designs derate. Harmattan dust, which destroys diesel air filters and turbochargers on a seasonal schedule, meets a drivetrain with no intake and no turbo. And the laterite roads of the construction corridors get full torque from zero rpm &mdash; loaded pull-away on loose grades without the clutch abuse that consumes diesel drivelines.</p>

<h2>TZ3V Specification for Burkinab&egrave; Service</h2>
<table style="width:100%;border-collapse:collapse;margin:20px 0;" border="1" cellpadding="8">
<tr style="background:#006341;color:#fff;"><th style="padding:8px;text-align:left;">Parameter</th><th style="padding:8px;text-align:left;">TZ3V 8x4 Electric Dump Truck</th></tr>
<tr><td style="padding:8px;">GVW / payload</td><td style="padding:8px;">31-34 t / 20-22 t (16-18 m&sup3; body)</td></tr>
<tr><td style="padding:8px;">Battery</td><td style="padding:8px;">600 kWh CATL LFP, liquid-cooled</td></tr>
<tr><td style="padding:8px;">Motor</td><td style="padding:8px;">LvKong 420 kW peak / 2,800 Nm</td></tr>
<tr><td style="padding:8px;">Range (loaded, mixed terrain)</td><td style="padding:8px;">280-320 km</td></tr>
<tr><td style="padding:8px;">DC charge 20-80%</td><td style="padding:8px;">~70 min at 360 kW / swap option 5-6 min</td></tr>
<tr><td style="padding:8px;">Gradeability</td><td style="padding:8px;">&ge;30% loaded</td></tr>
<tr><td style="padding:8px;">Ambient rating</td><td style="padding:8px;">to +50&deg;C, dust-sealed HV system</td></tr>
<tr><td style="padding:8px;">FOB price band</td><td style="padding:8px;">US$125,000-148,000</td></tr>
</table>
<p>The 360 kW charging capability matters for mine-supply duty: a truck returning from a 240 km round trip restores its charge in about 70 minutes and can run a second leg the same day. For operations where utilisation is everything, the battery-swap variant exchanges packs in 5-6 minutes at a containerised station &mdash; the same architecture we deploy in industrial mining, scaled to a single depot. Most Burkinab&egrave; construction fleets will choose depot DC charging; mine-gate and high-utilisation contractors should price the swap option seriously.</p>

<h2>TCO at Landlocked Fuel Prices</h2>
<p>Diesel in Burkina Faso retails around US$1.25-1.40 per litre in Ouagadougou and effectively more at mine sites. A 31 t tipper on construction duty burns 0.50-0.60 L/km: US$0.68-0.80 per kilometre. The TZ3V consumes 1.9-2.2 kWh/km loaded; at SONABEL industrial tariffs of roughly US$0.15-0.18/kWh, US$0.31-0.38 per kilometre &mdash; and under a solar canopy at US$0.07-0.10/kWh effective, US$0.16-0.22. On 4,000 km per month, grid-charged savings run US$1,400-1,700 monthly per truck, solar-assisted over US$2,000. Maintenance adds US$700-1,000 monthly in a dust environment that is genuinely cruel to diesel engines. Payback against the US$45,000-60,000 premium: 20-28 months grid-charged, 15-20 months solar-integrated &mdash; inside a battery warranty of 8 years / 4,500 cycles.</p>
<ul>
<li><strong>Energy per km:</strong> US$0.75 diesel vs US$0.16-0.38 electric (solar vs grid)</li>
<li><strong>Annual saving per truck:</strong> US$25,000-33,000 combined</li>
<li><strong>Payback:</strong> 15-28 months depending on charging source</li>
<li><strong>Harmattan dividend:</strong> no air filters, turbo or intake to service through dust season</li>
</ul>

<h2>Solar: The Sahelian Trump Card</h2>
<p>Burkina Faso receives 5.5-5.8 peak sun hours daily, and Ouagadougou&rsquo;s industrial zones have the land for serious canopies. The arithmetic of a 300-500 kWp yard array is compelling: it covers 45-60% of a ten-truck fleet&rsquo;s charging energy at an effective cost under US$0.08/kWh, provides covered parking in a city where shade preserves cabs and electronics, and hedges the diesel-price exposure entirely for the solar share. Several Burkinab&egrave; cement and aggregate operations already run solar hybrids for plant power; adding truck charging is the highest-value incremental load they can connect. Grid capacity in Ouagadougou&rsquo;s industrial districts supports the 600-800 kVA service a ten-truck fleet needs with managed charging, and SONABEL connection lead times of 10-16 weeks set the project critical path &mdash; file on order day.</p>

<h2>Import and Corridor Realities</h2>
<p>Burkina Faso imports through Abidjan, Tema or Lom&eacute;, with road transit of 1,000-1,200 km to Ouagadougou. We structure deliveries via the corridor with the best current transit economics, delivering trucks charged and driveable with full French documentation, UN R100 certification and the ECOWAS transit file. The TZ3V arrives by lowbed or drives the final leg under its own power &mdash; a genuine option from Tema with staged charging. For operators with coastal interests, our <a href="../markets/ghana.html">Ghana market page</a> covers the Tema-side ecosystem; several Burkinab&egrave; contractors share fleet ownership with Ghanaian sister companies, and platform standardisation across the corridor halves the support structure.</p>
<p>Support in a landlocked market is designed around parts independence: the fleet ships with an extended parts kit (contactors, sensors, brake components, suspension wear parts), CATL modules route through regional stock at 14-21 days, and the telematics portal gives our engineers live drivetrain visibility from Xi&rsquo;an. The service reality is that the drivetrain needs almost nothing &mdash; the maintenance calendar is brakes, coolant and software, and there is no imported engine-parts pipeline to wait on.</p>

<h2>Who Moves First</h2>
<p>The pioneers will be the integrated construction groups &mdash; those owning quarries and batching plants around the capital &mdash; followed by the mine-services contractors whose fuel exposure is the largest line item in their tenders. For both, the proposition is structural: in a landlocked economy, every kilometre run on electrons is a kilometre independent of a 1,000 km fuel supply chain. Burkina Faso&rsquo;s sun is free, its construction boom is real, and its gold logistics are permanent. The fleets that convert those fundamentals into an electric cost advantage first will hold it for a decade.</p>
'''))

# ---------------------------------------------------------------- 13
ARTICLES.append(dict(
f='asuncion-paraguay-electric-cargo-truck-corridor',
t='Asunci&oacute;n Agri-Logistics: KTH3 Electric Cargo Trucks for Paraguay&rsquo;s Export Corridors',
d='Paraguay has the world&rsquo;s cheapest hydro power and expensive diesel. KTH3 electric cargo truck economics on the Asuncion agri corridors: range, TCO and import guide.',
k='KTH3 electric cargo truck, EV truck Paraguay, electric truck Asuncion, electric truck agri logistics, Dongfeng electric truck, Itaipu electric truck, electric cargo truck South America',
img='models/p07_10.jpg',
alt='Dongfeng KTH3 electric cargo truck on a Paraguayan soy corridor, EV truck for Asuncion agri logistics',
net='zhc',
body='''
<p>Paraguay holds an energy position almost no other trucking market enjoys: it co-owns Itaip&uacute; and Yacyret&aacute;, two of the world&rsquo;s largest hydroelectric plants, exports most of its share of that power to Brazil, and sells industrial electricity domestically at US$0.06-0.09 per kWh. Meanwhile its trucks &mdash; moving one of South America&rsquo;s great soy and beef export machines &mdash; burn imported diesel at US$1.00-1.15 per litre. A country that exports electricity and imports transport fuel is running an arbitrage against itself, and the correction is obvious. This article examines the <a href="../products/models/kth3-electric-cargo-truck.html">Dongfeng KTH3 electric cargo truck</a> on Paraguay&rsquo;s agri corridors, where this EV truck&rsquo;s economics are among the most favourable on earth.</p>

<h2>The Corridor Geography</h2>
<p>Paraguay&rsquo;s agri freight converges on a few axes: the Alto Paran&aacute; soy belt down to Ciudad del Este and the river terminals, the Canindey&uacute; and San Pedro grain corridors into Asunci&oacute;n, and the Chaco cattle logistics west toward the Mennonite cooperatives. Collection-leg distances &mdash; farm or elevator to terminal &mdash; run 40-180 km, squarely inside the KTH3&rsquo;s 200-240 km loaded range on its 350 kWh CATL pack. The model that fits Paraguay is hub electrification: trucks based at the river terminals and silo complexes run collection loops all day and charge at the hub at night, exactly the pattern the country&rsquo;s cooperatives already operate for their diesel fleets. No public charging network is required; the freight geography is the charging plan.</p>

<h2>KTH3 on Agri Duty: The Numbers</h2>
<table style="width:100%;border-collapse:collapse;margin:20px 0;" border="1" cellpadding="8">
<tr style="background:#006341;color:#fff;"><th style="padding:8px;text-align:left;">Parameter</th><th style="padding:8px;text-align:left;">KTH3 6x4 Electric Cargo Truck</th></tr>
<tr><td style="padding:8px;">GVW / payload</td><td style="padding:8px;">28 t / 18-20 t (grain box or stake)</td></tr>
<tr><td style="padding:8px;">Battery</td><td style="padding:8px;">350 kWh CATL LFP, liquid-cooled</td></tr>
<tr><td style="padding:8px;">Motor</td><td style="padding:8px;">LvKong 360 kW peak / 2,400 Nm</td></tr>
<tr><td style="padding:8px;">Range (loaded, rural roads)</td><td style="padding:8px;">200-240 km</td></tr>
<tr><td style="padding:8px;">DC charge 20-80%</td><td style="padding:8px;">~50 min at 240 kW</td></tr>
<tr><td style="padding:8px;">Gradeability</td><td style="padding:8px;">&ge;30% &mdash; red-dirt farm ramps loaded</td></tr>
<tr><td style="padding:8px;">Battery warranty</td><td style="padding:8px;">8 years / 4,500 cycles to 70% SOH</td></tr>
<tr><td style="padding:8px;">FOB price band</td><td style="padding:8px;">US$88,000-105,000</td></tr>
</table>
<p>Harvest-season utilisation is the detail that makes agri fleets the best EV truck buyers in any market: for 4-5 months a year, trucks run 16-20 hours daily on two driver shifts, and high utilisation is what converts the electric premium into payback speed. A KTH3 on harvest duty covers 400-500 km daily with two 50-minute DC charges slotted into loading queues &mdash; queues the diesel truck spends idling at the elevator anyway. Off-season, the same fleet takes the lighter regional distribution work. The battery warranty math works comfortably: even at harvest utilisation, 4,500 cycles represents eight-plus years of service.</p>

<h2>The Itaip&uacute; Arbitrage, Quantified</h2>
<p>Run the corridor arithmetic. A diesel 28 t truck on rural collection duty burns 0.45-0.55 L/km; at US$1.05/L, US$0.50-0.58 per kilometre. The KTH3 consumes 1.35-1.55 kWh/km on the same duty; at ANDE industrial tariffs of US$0.07/kWh, US$0.10-0.11 per kilometre &mdash; an 80% energy cost reduction, among the largest we have modelled in any market. On 5,000 km per month at harvest intensity, the monthly saving is US$2,000-2,400 per truck; annualised across the seasonal pattern, US$18,000-24,000 including maintenance. Against a purchase premium of US$35,000-45,000, payback runs 20-28 months &mdash; and unlike diesel-price-dependent savings, these are anchored to a hydro tariff that has been stable for decades. Few fleet investments anywhere carry this combination of return and price certainty.</p>
<ul>
<li><strong>Energy per km:</strong> US$0.54 diesel vs US$0.10 electric &mdash; 81% lower</li>
<li><strong>Annual saving per truck:</strong> US$18,000-24,000 combined</li>
<li><strong>Payback:</strong> 20-28 months; faster at full harvest utilisation</li>
<li><strong>Price certainty:</strong> hydro tariff stability vs imported diesel exposure</li>
</ul>

<h2>Charging at Silos and Terminals</h2>
<p>Paraguay&rsquo;s rural grid is better than its neighbours&rsquo; because the country is over-built for electricity &mdash; medium-voltage service reaches every silo complex of consequence. A hub installation for a 10-15 truck fleet is two 240 kW DC chargers plus managed overnight AC, an 800 kVA-1 MVA service class that ANDE supplies routinely to agro-industrial customers. The cooperatives are the natural first deployers: they own the silos, the power connections and the freight relationships, and an electric collection fleet is a member service as much as a cost project. Our deployment package includes the load-management configuration that sequences harvest-season charging around the elevator&rsquo;s own processing load &mdash; the same electrical room, one coordinated schedule.</p>
<p>Solar adds a second dimension in a country already thinking about its hydro premium: several cooperatives are building solar at silo sites to free hydro power for export or industrial sale, and truck charging is a controllable daytime load that soaks up solar peaks. The KTH3 fleet&rsquo;s 3.5 MWh of distributed battery storage (ten trucks) also has genuine grid value in rural networks &mdash; a conversation Paraguay&rsquo;s forward-looking cooperatives are already having with ANDE.</p>

<h2>Import and Mercosur Context</h2>
<p>Trucks enter Paraguay via the river port of Asunci&oacute;n or overland from Brazilian ports, with full Mercosur documentation; we deliver the Spanish-language homologation dossier, UN R100 certification and the two-year parts kit as standard. Paraguay&rsquo;s treatment of electric vehicles includes materially reduced duties versus diesel, and the customs process in Asunci&oacute;n is efficient by regional standards. For groups operating across the River Plate basin, our <a href="../markets/chile.html">Chile market page</a> and broader regional coverage provide context &mdash; the same KTH3 platform serves the Argentine and southern Brazilian grain corridors, and regional agri groups standardising on one platform share parts and training across the basin.</p>
<p>Support for Paraguayan fleets follows our agri-sector protocol: parts kits sized for harvest-season self-sufficiency, CATL module stock at 12-18 days, and telemetry-based remote diagnostics with Spanish-language engineering support. The drivetrain&rsquo;s maintenance calendar &mdash; brakes, coolant, software &mdash; removes the imported-engine-parts dependency that idles diesel trucks at the worst possible time: mid-harvest, when every truck-day is revenue.</p>

<h2>The National Logic</h2>
<p>Paraguay&rsquo;s policymakers already understand the arbitrage &mdash; the country is actively discussing how to monetise its hydro surplus domestically &mdash; and truck electrification is the largest untapped load that keeps energy value onshore. The fleets that move first convert a national structural advantage into a private one: 80% energy cost reduction, price certainty for a decade, and a scope-3 story the soy exporters&rsquo; European customers increasingly require. The electrons are already there. The only question is which cooperatives and haulers plug into them first.</p>
'''))

# ---------------------------------------------------------------- 14
ARTICLES.append(dict(
f='montevideo-uruguay-electric-truck-renewable-grid',
t='Montevideo on a 98% Renewable Grid: KT5M Electric Box Trucks for Uruguay',
d='Uruguay runs on 98% renewable electricity. The KT5M electric box truck turns that grid into the cheapest urban freight in South America. EV truck specs and TCO inside.',
k='KT5M electric box truck, EV truck Uruguay, electric truck Montevideo, renewable grid electric truck, Dongfeng electric truck, electric box truck South America, UTE electric truck',
img='models/p07_11.jpg',
alt='Dongfeng KT5M electric box truck on a Montevideo delivery route, EV truck for Uruguay renewable grid logistics',
net='zhc',
body='''
<p>Uruguay did something between 2010 and 2020 that almost no other country managed: it rebuilt its electricity system to run on 97-99% renewable power &mdash; wind, hydro, biomass and solar &mdash; while keeping industrial tariffs at US$0.10-0.13 per kWh. The grid is so clean that the country&rsquo;s remaining transport emissions are the single largest item left in its carbon account, and the government&rsquo;s MOV&Eacute;S programme actively subsidises electric commercial vehicles. For urban freight operators in Montevideo &mdash; where half the country&rsquo;s population and most of its distribution economy sit &mdash; the result is a simple proposition: the cleanest electrons in the Americas at mid-range prices, against imported diesel at US$1.40-1.60 per litre. This article examines the <a href="../products/models/kt5m-electric-cargo-truck.html">Dongfeng KT5M electric box truck</a> in Uruguayan urban service.</p>

<h2>Montevideo&rsquo;s Freight Geography</h2>
<p>Montevideo&rsquo;s distribution economy is compact and port-anchored. Containers and bulk goods land at the port; the wholesale markets, cold stores and industrial estates ring the city along the Acceso Este and the Ruta 5 corridor; and retail distribution fans out across a metro area barely 30 km across. A box truck on this pattern runs 100-180 km daily &mdash; comfortably inside the KT5M&rsquo;s 200-240 km real-world range &mdash; and sleeps at the same depot. Regional runs to Punta del Este (130 km), Colonia (180 km) or the interior towns are one-charge round trips for the 180 kWh variant. Uruguay&rsquo;s small geography, usually a constraint, is the EV truck&rsquo;s best friend: there is essentially no domestic route a properly specified electric truck cannot serve today.</p>

<h2>KT5M Specification for Uruguayan Fleets</h2>
<table style="width:100%;border-collapse:collapse;margin:20px 0;" border="1" cellpadding="8">
<tr style="background:#006341;color:#fff;"><th style="padding:8px;text-align:left;">Parameter</th><th style="padding:8px;text-align:left;">KT5M Electric Box Truck</th></tr>
<tr><td style="padding:8px;">GVW / payload</td><td style="padding:8px;">9-12 t class / 4.5-6 t payload</td></tr>
<tr><td style="padding:8px;">Battery</td><td style="padding:8px;">140-180 kWh CATL LFP</td></tr>
<tr><td style="padding:8px;">Motor</td><td style="padding:8px;">LvKong 150-190 kW peak / 1,100-1,500 Nm</td></tr>
<tr><td style="padding:8px;">Real-world range (urban, loaded)</td><td style="padding:8px;">200-240 km</td></tr>
<tr><td style="padding:8px;">DC charge 20-80%</td><td style="padding:8px;">~40 min at 120 kW</td></tr>
<tr><td style="padding:8px;">Body options</td><td style="padding:8px;">28-35 m&sup3; dry box, curtainside, reefer</td></tr>
<tr><td style="padding:8px;">Winter performance</td><td style="padding:8px;">heat-pump thermal system, rated to -20&deg;C</td></tr>
<tr><td style="padding:8px;">FOB price band</td><td style="padding:8px;">US$48,000-62,000</td></tr>
</table>
<p>The winter line matters more in Uruguay than anywhere else we serve in Latin America: Montevideo&rsquo;s July mornings sit at 2-6&deg;C, and the interior drops lower. The KT5M&rsquo;s heat-pump cabin and battery thermal system keeps cold-weather range loss to 8-12% &mdash; versus 20-30% for resistance-heated designs &mdash; and the LFP pack&rsquo;s liquid heating brings cells to operating temperature during the charge session, so the truck leaves the depot at full capability. Fleets running pre-dawn bakery and dairy distribution, the most cold-exposed duty in the country, are exactly where this specification earns its keep.</p>

<h2>TCO on a Renewable Tariff</h2>
<p>The arithmetic is stark. A diesel 9-12 t box truck burns 0.28-0.35 L/km; at Uruguayan pump prices of US$1.50/L, US$0.45-0.53 per kilometre. The KT5M consumes 0.75-0.90 kWh/km; at UTE&rsquo;s industrial tariff of US$0.11/kWh &mdash; or the off-peak night tariff closer to US$0.07 &mdash; US$0.07-0.10 per kilometre. On 4,000 km monthly: US$1,500-1,800 saved per truck per month in energy alone. Maintenance adds US$250-350 monthly. Combined annual saving: US$21,000-26,000 per truck. Against the purchase premium of US$18,000-25,000 &mdash; partially offset by MOV&Eacute;S programme support and Uruguay&rsquo;s EV import-duty advantages &mdash; payback lands at 10-15 months. That is the fastest payback we model in Latin America, and it is a direct read-across from the grid the country spent a decade building.</p>
<ul>
<li><strong>Energy per km:</strong> US$0.48 diesel vs US$0.07-0.10 electric &mdash; ~80% lower</li>
<li><strong>Annual saving per truck:</strong> US$21,000-26,000 combined</li>
<li><strong>Payback:</strong> 10-15 months with MOV&Eacute;S support</li>
<li><strong>Carbon:</strong> ~zero operational emissions on a 98% renewable grid &mdash; a genuine scope-3 zero, not an offset</li>
</ul>

<h2>Charging: A Grid Ready and Waiting</h2>
<p>Uruguay&rsquo;s distribution infrastructure is modern and UTE&rsquo;s commercial connection process is among the most efficient in the region &mdash; a ten-truck KT5M fleet needing 300-350 kVA is a routine commercial upgrade, typically processed in 6-10 weeks. The configuration is standard: one 120 kW DC charger per 6-8 trucks, overnight AC per bay, load management aligned to UTE&rsquo;s time-of-use tariff so the fleet charges into the wind-heavy overnight trough at the lowest rate. Montevideo&rsquo;s industrial estates around the port and the Acceso Este corridor have ample medium-voltage capacity; the city has been quietly ready for fleet electrification for years and the utilisation data from Uruguay&rsquo;s growing electric bus fleet proves the model.</p>
<p>The reefer variant deserves a specific note for Uruguay&rsquo;s beef and dairy cold chain: the electric reefer runs off the traction battery at US$0.07-0.10/kWh versus a diesel reefer unit burning US$8-12 of fuel per operating day, and the near-silent operation suits the pre-dawn delivery windows in residential Punta Carretas and Pocitos. For a country whose export brand is built on clean production, a zero-emission cold chain from plant to port is a marketing asset as much as a cost line.</p>

<h2>Import and Regional Context</h2>
<p>Uruguay applies reduced duties to electric commercial vehicles and Montevideo&rsquo;s port processes RoRo imports efficiently, with 30-36 day sailings from China. We deliver the Spanish-language homologation dossier, UN R100 certification and the parts kit as standard. For distributors operating across the River Plate, our <a href="../markets/chile.html">Chile market page</a> provides the regional comparison &mdash; the same KT5M platform serves Buenos Aires-adjacent and Chilean urban duty, and River Plate fleet groups standardising on one platform share parts stock and training across both shores.</p>
<p>Support is structured for a sophisticated maintenance market: Uruguay&rsquo;s technician base is strong, and we certify local workshops on the HV system while the telematics portal gives our engineers live visibility into every truck&rsquo;s battery and drivetrain health. Parts kits ship with the fleet, CATL modules arrive in 12-16 days, and the drivetrain&rsquo;s service calendar &mdash; brakes, coolant, software &mdash; is a fraction of the diesel maintenance it replaces.</p>

<h2>The First-Mover Profile</h2>
<p>Uruguay&rsquo;s pioneers will be the dairy and beef cold-chain distributors (the country&rsquo;s export pride), the supermarket groups with scope-3 commitments, and the 3PLs serving the port corridor. For all of them the case is identical: the grid is built, the tariffs are favourable, the incentives are law, and the geography fits inside one charge. Uruguay spent a decade making its electricity clean and its policy supportive; the KT5M fleet is how its freight economy collects on that investment. The operators who electrify first will own the cheapest &mdash; and genuinely zero-carbon &mdash; urban freight cost base in South America.</p>
'''))

# ---------------------------------------------------------------- 15
ARTICLES.append(dict(
f='te46-vs-sany-electric-port-tractor-comparison',
t='TE46 vs SANY Electric Port Tractor: Terminal Drayage Comparison for Export-Market Ports',
d='Dongfeng TE46 vs SANY electric port tractor compared: battery, swap options, torque, TCO and parts support for port drayage fleets choosing an EV truck platform.',
k='TE46 vs SANY, electric port tractor comparison, EV truck terminal drayage, electric terminal tractor, Dongfeng vs SANY electric truck, port drayage EV truck',
img='models/p11_01.jpg',
alt='Dongfeng TE46 electric port tractor vs SANY in terminal drayage, EV truck comparison for port fleets',
net='qyc',
body='''
<p>Terminal drayage is the most competitive segment in electric trucking: the duty cycle is understood, the buyers are sophisticated, and every major Chinese OEM fields a product. Two platforms come up in nearly every tender we see across Africa, the Middle East and Latin America: the <a href="../products/models/te46-electric-tractor.html">Dongfeng TE46 electric port tractor</a> and SANY&rsquo;s electric terminal tractor range. This comparison walks through the decision the way a port fleet engineer should: duty-cycle fit, energy architecture, torque and productivity, TCO, and the after-sales reality that decides the purchase long after the spec sheets are filed away.</p>

<h2>The Duty Cycle Sets the Exam</h2>
<p>Port drayage punishes weak specifications in specific places. A terminal tractor couples and uncouples 40-60 times a shift, accelerates 40-tonne combinations across 50-200 metre yard legs hundreds of times daily, idles 30-40% of engine-hours at gates and stacks, and works 20+ hours a day in peak season. The three specifications that decide performance are: usable energy per shift (not nameplate), torque delivery at walking-to-40 km/h speeds, and turnaround time at the energy source. Everything else &mdash; top speed, highway range &mdash; is noise. Both the TE46 and the SANY are credible terminal tools; the differences live in how they answer these three questions and what stands behind them after year two.</p>

<h2>Head-to-Head: The Core Numbers</h2>
<table style="width:100%;border-collapse:collapse;margin:20px 0;" border="1" cellpadding="8">
<tr style="background:#006341;color:#fff;"><th style="padding:8px;text-align:left;">Parameter</th><th style="padding:8px;text-align:left;">Dongfeng TE46</th><th style="padding:8px;text-align:left;">SANY Electric Terminal Tractor</th></tr>
<tr><td style="padding:8px;">GCW rating</td><td style="padding:8px;">42-46 t</td><td style="padding:8px;">42-45 t</td></tr>
<tr><td style="padding:8px;">Battery</td><td style="padding:8px;">282 kWh CATL LFP, swap-capable</td><td style="padding:8px;">~282-350 kWh LFP (variant-dependent)</td></tr>
<tr><td style="padding:8px;">Peak motor torque</td><td style="padding:8px;">2,800 Nm</td><td style="padding:8px;">~2,400-2,800 Nm</td></tr>
<tr><td style="padding:8px;">Shift endurance (mixed drayage)</td><td style="padding:8px;">8-10 h</td><td style="padding:8px;">7-9 h</td></tr>
<tr><td style="padding:8px;">Energy turnaround</td><td style="padding:8px;">240 kW DC ~45 min / swap 5-6 min</td><td style="padding:8px;">DC fast charge; swap on select variants</td></tr>
<tr><td style="padding:8px;">Fifth wheel</td><td style="padding:8px;">50 mm oscillating, terminal-rated</td><td style="padding:8px;">50 mm terminal-rated</td></tr>
<tr><td style="padding:8px;">FOB price band</td><td style="padding:8px;">US$72,000-88,000</td><td style="padding:8px;">US$75,000-95,000</td></tr>
</table>
<p>On paper the platforms are close, which is exactly why the decision needs to go deeper. The TE46&rsquo;s differentiators emerge in the details of energy architecture and lifecycle cost: the battery-swap option is factory-integrated rather than a special-order variant, meaning swap-capable trucks and standard trucks share one production line, one parts system and one price list. For a terminal planning to grow from depot charging into swap as shifts extend, that integration path is operationally significant &mdash; the fleet&rsquo;s first trucks do not become orphans when the infrastructure strategy evolves.</p>

<h2>Productivity: Torque Where It Matters</h2>
<p>In terminal service, productivity is measured in moves per hour, and moves per hour is set in the first 50 metres of every yard leg. The TE46&rsquo;s 2,800 Nm arrives from zero rpm with no gearbox to shift; a loaded 40 t combination crosses the acceleration zone to yard speed in about two-thirds the time of a diesel tractor, and drivers hold that pace for a full shift because the electric drivetrain has no heat-soak or fatigue-inducing vibration. In our terminal deployments, electrified drayage consistently measures 6-10% more moves per shift than the diesel fleet it replaced &mdash; and driver retention improves, a benefit every terminal HR department understands immediately. On this metric the two electric platforms are comparable; both are decisively better than diesel, which is the comparison that actually matters for a first-time buyer.</p>

<h2>TCO: Where the Decision Is Really Made</h2>
<p>The five-year cost stack for a drayage tractor is: purchase price, energy, maintenance, tyres, downtime. Energy and maintenance are near-identical between credible electric platforms and both crush the diesel baseline (60-70% energy cost reduction, 40-50% maintenance reduction). The differentiators are purchase price &mdash; where the TE46 typically lands 5-8% below comparable SANY configurations &mdash; and downtime, which is where the after-sales structure shows up. Our support model ships a terminal-duty parts kit with the fleet, holds CATL modules in regional stock, and monitors every truck&rsquo;s drivetrain health through the telemetry portal with engineering response measured in hours. A drayage tractor earns its keep in moves; a week waiting on an imported component costs more than the component.</p>
<ul>
<li><strong>Purchase price:</strong> TE46 typically 5-8% below like-for-like SANY configuration</li>
<li><strong>Energy:</strong> both platforms ~US$0.12-0.18/km vs diesel US$0.45-0.55/km</li>
<li><strong>Swap integration:</strong> TE46 factory swap option shares parts system with charge variant</li>
<li><strong>Support:</strong> fleet-shipped parts kits + regional CATL module stock + live telemetry</li>
<li><strong>Residual value:</strong> swap-capable architecture protects second-life battery value</li>
</ul>

<h2>Fit by Market: Where Each Platform Makes Sense</h2>
<p>Buyers with existing SANY crane and stacker fleets will naturally evaluate the SANY tractor for workshop commonality &mdash; a legitimate consideration, though terminal tractors share few wear parts with container handlers. For everyone else, the evaluation should weight: energy-architecture roadmap (swap readiness), parts support in the actual operating region, and the exporter&rsquo;s deployment experience in comparable ports. We have commissioned TE46 fleets from Tanger Med to East African terminals and carry that commissioning playbook &mdash; switchgear sizing, charger siting, driver conversion training &mdash; into every new deployment. Buyers evaluating Gulf and African deployments can review our <a href="../markets/uae.html">UAE market page</a> for the regional operating context these tractors work in.</p>
<p>A word on battery longevity, since terminals run brutal cycle counts: both platforms use LFP chemistry rated for 4,500+ cycles, but thermal management separates field results. The TE46&rsquo;s liquid-cooled pack, in our hot-climate terminal data, holds 92-94% capacity after 2,000 cycles at sustained 40&deg;C+ ambient &mdash; the difference between a battery that outlives the tractor&rsquo;s first contract and one that does not. Ask every bidder for liquid cooling and for cycle-life data at your ambient temperature, not at 25&deg;C.</p>

<h2>The Verdict</h2>
<p>Both platforms will move containers economically; the diesel comparison is won by either. The TE46 earns the recommendation on the factors that compound over a fleet&rsquo;s life: a factory-integrated swap roadmap, a 5-8% purchase advantage, liquid-cooled longevity data from comparable terminals, and a support structure built for export-market ports rather than domestic Chinese terminals. For a terminal writing a five-year drayage contract, those are the terms that decide total cost &mdash; and they favour the truck that was designed for exactly this job, backed by a team that has already stood up fleets like yours.</p>
'''))

# ---------------------------------------------------------------- 16
ARTICLES.append(dict(
f='tz3v-vs-yutong-electric-mining-dump-truck',
t='TZ3V vs Yutong Electric Mining Dump Truck: Heavy EV Haulage Compared for Export Mines',
d='Dongfeng TZ3V vs Yutong electric mining dump truck: battery, range, charging, dust and heat performance, TCO and export support compared for mine fleet buyers.',
k='TZ3V vs Yutong, electric mining dump truck comparison, EV truck mining, electric dump truck 8x4, Dongfeng vs Yutong electric truck, mining EV truck export',
img='models/p03_05.jpg',
alt='Dongfeng TZ3V electric dump truck vs Yutong mining truck comparison, EV truck for mine haulage',
net='zxc',
body='''
<p>Mining houses electrifying their haul fleets increasingly shortlist two Chinese platforms: the <a href="../products/models/tz3v-electric-dump-truck.html">Dongfeng TZ3V electric dump truck</a> and Yutong&rsquo;s electric mining truck range. Yutong built its name in buses and has transferred that electrification depth into mining; Dongfeng brings six decades of heavy-truck engineering and an export support network across exactly the markets where mines operate. This comparison works through the decision the way a mine&rsquo;s mobile-equipment manager should: haul-cycle fit, energy architecture, environmental durability, TCO, and the support question that matters more than any spec line once the fleet is 500 km from the coast.</p>

<h2>Different Tools for Adjacent Jobs</h2>
<p>An honest comparison starts with a clarification: the two ranges overlap but are not identical. Yutong&rsquo;s mining line concentrates on dedicated wide-body mining rigs (60-100 t class, off-highway geometry); the TZ3V is a heavy 8x4 on-highway/off-road dump truck rated 31-34 t GVW with a 600 kWh pack &mdash; the format used for quarry-to-plant haulage, mine-support duty, infrastructure construction inside mining concessions, and corridor haulage on engineered roads. Many operations need both formats; the comparison here addresses the quarry-and-corridor segment where buyers genuinely choose between a TZ3V and Yutong&rsquo;s smaller mining configurations. In that segment, the TZ3V&rsquo;s on-highway legality is often decisive: it hauls on public roads between quarry and crusher, which dedicated off-highway rigs cannot do.</p>

<h2>Core Specification Comparison</h2>
<table style="width:100%;border-collapse:collapse;margin:20px 0;" border="1" cellpadding="8">
<tr style="background:#006341;color:#fff;"><th style="padding:8px;text-align:left;">Parameter</th><th style="padding:8px;text-align:left;">Dongfeng TZ3V 8x4</th><th style="padding:8px;text-align:left;">Yutong Mining EV (comparable config)</th></tr>
<tr><td style="padding:8px;">GVW / payload</td><td style="padding:8px;">31-34 t / 20-22 t</td><td style="padding:8px;">~30-60 t class depending on model</td></tr>
<tr><td style="padding:8px;">Battery</td><td style="padding:8px;">600 kWh CATL LFP, liquid-cooled</td><td style="padding:8px;">~350-600 kWh LFP</td></tr>
<tr><td style="padding:8px;">Motor</td><td style="padding:8px;">LvKong 420 kW / 2,800 Nm</td><td style="padding:8px;">~400-500 kW class</td></tr>
<tr><td style="padding:8px;">Range (loaded, mixed)</td><td style="padding:8px;">280-320 km</td><td style="padding:8px;">cycle-based (pit duty)</td></tr>
<tr><td style="padding:8px;">Energy turnaround</td><td style="padding:8px;">360 kW DC ~70 min / swap 5-6 min</td><td style="padding:8px;">DC charge; swap on select models</td></tr>
<tr><td style="padding:8px;">Road legality</td><td style="padding:8px;">Full on-highway registration</td><td style="padding:8px;">Off-highway (wide-body models)</td></tr>
<tr><td style="padding:8px;">FOB price band</td><td style="padding:8px;">US$125,000-148,000</td><td style="padding:8px;">US$130,000-220,000 (class-dependent)</td></tr>
</table>
<p>The range figure is the TZ3V&rsquo;s structural advantage in its segment. A 600 kWh pack delivering 280-320 km loaded means the truck works full construction shifts on highway-connected quarry duty without mid-shift charging &mdash; or runs mine-to-port corridor legs that smaller-pack rigs cannot attempt. Mines comparing pit-cycle rigs on cycles per charge will find the two platforms competitive inside the pit; the TZ3V pulls ahead the moment the haul road leaves the concession fence, which in African and Central Asian quarry-cement logistics is most of the time.</p>

<h2>Durability: Dust, Heat and Corrugation</h2>
<p>Export-market mining punishes equipment in three ways spec sheets miss. Dust: both platforms seal their HV systems, but the TZ3V&rsquo;s drivetrain inherits Dongfeng&rsquo;s desert-fleet filtration heritage &mdash; cab pressurisation, sealed connectors and liquid cooling sized for sustained 45&deg;C+ ambient, with field data from Sahelian deployments showing 92-94% pack capacity retention after 2,000 cycles. Corrugation: the TZ3V&rsquo;s chassis is a heavy on-road 8x4 frame rated for mixed-terrain duty; wide-body off-highway rigs excel on maintained pit roads but suffer on public-road corrugation at speed. Heat: liquid cooling is standard on the TZ3V across all variants; buyers should confirm it rather than assume it on any platform, because air-cooled packs in 40&deg;C ambient lose years of calendar life.</p>

<h2>TCO in the Quarry-and-Corridor Segment</h2>
<p>For the duty cycle where these platforms genuinely compete &mdash; 50-250 km daily between quarry, crusher, plant and site &mdash; the cost stack runs as follows. Energy: both electrics deliver the same 60-70% reduction versus diesel; between them, consumption per tonne-km is within a few percent. Purchase: the TZ3V typically lands 10-20% below comparable Yutong mining configurations in this payload class, and its on-highway registration means one truck does jobs that would otherwise need a road truck and a pit rig. Utilisation: the 600 kWh pack&rsquo;s range eliminates mid-shift charging stops that fragment duty cycles on smaller packs. Support: the section below, where export buyers should concentrate hardest.</p>
<ul>
<li><strong>Purchase price:</strong> TZ3V typically 10-20% below comparable mining-config pricing</li>
<li><strong>Versatility:</strong> on-highway legal &mdash; one truck covers quarry, corridor and site duty</li>
<li><strong>Range:</strong> 280-320 km loaded removes mid-shift charging on corridor work</li>
<li><strong>Battery longevity:</strong> liquid-cooled LFP, 8-year / 4,500-cycle warranty</li>
<li><strong>Parts commonality:</strong> shares wear parts with Dongfeng&rsquo;s global 8x4 fleet &mdash; available everywhere trucks are</li>
</ul>

<h2>The Support Question, Stated Plainly</h2>
<p>A mining truck&rsquo;s cost is dominated by availability, and availability is a support-network property. Yutong&rsquo;s support depth is concentrated in its domestic market and select overseas bus operations; its mining-truck export network is younger. Our structure is built for export mining: fleets ship with extended parts kits sized for site self-sufficiency, CATL modules stock regionally (Panama for the Americas, regional hubs for Africa and the Gulf), telemetry gives our engineering desk live visibility into every pack, and commissioning engineers stay through ramp-up. Buyers in Southern and East Africa can see the operating context on our <a href="../markets/south-africa.html">South Africa market page</a> &mdash; the TZ3V works in exactly these quarry-corridor roles across the region&rsquo;s mining belt.</p>
<p>The battery question deserves a final paragraph because it dominates lifecycle cost. Both platforms use LFP chemistry with 4,500-cycle ratings; the differences are thermal management quality and second-life value. The TZ3V&rsquo;s modular pack design means a degraded module is a line-replaceable unit &mdash; swap it in hours, return it for second-life stationary storage &mdash; and the 8-year warranty is backed by a supply chain that answers in the buyer&rsquo;s time zone. Ask every bidder: where are modules stocked, who changes them, and what is the warranted capacity at year five at my ambient temperature? The answers decide more lifetime cost than any motor specification.</p>

<h2>The Verdict</h2>
<p>For dedicated in-pit duty on engineered roads at 60 t+, Yutong&rsquo;s wide-body rigs are credible tools and worth a bid. For the quarry-corridor-construction segment &mdash; where most export-market mines and quarries actually spend their haulage budget &mdash; the TZ3V&rsquo;s combination of on-highway legality, 600 kWh range, liquid-cooled durability, lower purchase price and export-grade support makes it the stronger platform. The right shortlist includes both; the right decision weights availability and versatility over brochure torque, and that weighting points to the truck built to work everywhere your operation does.</p>
'''))

for a in ARTICLES:
    html = build(a)
    path = os.path.join(ROOT, 'blog', a['f'] + '.html')
    with open(path, 'w', encoding='utf-8') as fh:
        fh.write(html)
    words = len(re.sub(r'<[^>]+>', ' ', a['body']).split())
    print('%-58s %5d words' % (a['f'], words))
print('done batch2:', len(ARTICLES))
