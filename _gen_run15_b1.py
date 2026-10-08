# -*- coding: utf-8 -*-
"""Run 15 batch 1: 8 articles (Africa spotlights + GEO mining question)."""
import re, os
import _gen_run14_b1 as G
G.DATE = "2026-10-08"
build = G.build

ROOT = os.path.dirname(os.path.abspath(__file__))
ARTICLES = []

# ---------------------------------------------------------------- 1
ARTICLES.append(dict(
f='tema-ghana-port-te46-electric-terminal-tractor',
t='Tema Port, Ghana: TE46 Electric Terminal Tractors for West Africa&rsquo;s Busiest Gateway',
d='Tema Port container shuttle suits the TE46 electric terminal tractor: 262-350 kWh CATL LFP, 5-6 min battery swap and a 65% lower energy cost per km than diesel. EV truck specs, TCO and import guide.',
k='TE46 electric terminal tractor, EV truck Ghana, electric truck Tema Port, electric port tractor West Africa, Dongfeng electric truck, port drayage EV truck, Tema container shuttle',
img='models/p11_04.jpg',
alt='Dongfeng TE46 electric terminal tractor hauling containers at Tema Port, Ghana, EV truck for West African port duty',
net='qyc',
body='''
<p>Tema Port is the gateway that carries the majority of Ghana&rsquo;s import and export tonnage, and after the Meridian Port Services expansion it is also one of the deepest and most efficient container terminals on the West African coast. Every container that lands at the new Terminal 3 still moves its final metres across the yard and onto the road by tractor &mdash; and those tractors burn diesel at roughly US$1.10 per litre while idling in terminal queues for a third of every shift. This article looks at how the <a href="../products/models/te46-electric-tractor.html">Dongfeng TE46 electric terminal tractor</a> fits Tema&rsquo;s container-shuttle duty, with real numbers on energy cost, payload, battery swap and import logistics. For terminal operators, 3PLs and the haulage groups serving the <a href="../markets/ghana.html">Ghana market</a>, an EV truck tractor fleet is no longer a pilot; it is a margin decision driven by fuel price and idle time.</p>

<h2>Tema Port&rsquo;s Expansion and the Drayage Bottleneck</h2>
<p>The Tema expansion nearly tripled the port&rsquo;s container capacity and pulled shipping lines away from the congested Lagos corridor, which means more yard moves per hour and longer tractor shifts than the old port ever ran. A container terminal tractor works a brutal, repetitive cycle: short loaded pulls of 0.5-3 km between the quay, the stacking yard and the gate, 400-800 moves per shift, and 25-40% of engine hours spent idling in queues while a diesel engine burns fuel to make heat and noise. That idle fraction is where the diesel economics collapse, because a Tema diesel tractor burns 3-4 litres per hour at the queue producing nothing, while the TE46&rsquo;s electric drivetrain draws essentially zero at standstill. Across a 10-hour shift, queue time alone is 25-35% of the diesel tractor&rsquo;s fuel bill and under 2% of the EV truck&rsquo;s energy bill.</p>
<p>The second structural factor is utilisation. Higher port volumes mean two-shift and round-the-clock tractor operation, which doubles annual kilometres and therefore halves the payback period on the electric premium. Terminal duty is also captive: every tractor sleeps in the same fenced, powered yard, which is the single easiest place in the transport world to install charging. Tema&rsquo;s terminal geography &mdash; quay, yard and gate all inside a 2 km footprint &mdash; sits comfortably inside the TE46&rsquo;s shift endurance without any public charging.</p>

<h2>TE46 Specifications for Ghanaian Terminal Duty</h2>
<table style="width:100%;border-collapse:collapse;margin:20px 0;" border="1" cellpadding="8">
<tr style="background:#006341;color:#fff;"><th style="padding:8px;text-align:left;">Parameter</th><th style="padding:8px;text-align:left;">TE46 4x2 Electric Terminal Tractor</th></tr>
<tr><td style="padding:8px;">GCW rating</td><td style="padding:8px;">42-46 t (container drayage spec)</td></tr>
<tr><td style="padding:8px;">Battery</td><td style="padding:8px;">262-350 kWh CATL LFP, liquid-cooled</td></tr>
<tr><td style="padding:8px;">Motor</td><td style="padding:8px;">LvKong permanent magnet, 250-300 kW peak / 2,800 Nm</td></tr>
<tr><td style="padding:8px;">Shift endurance</td><td style="padding:8px;">8-10 h mixed drayage duty per charge</td></tr>
<tr><td style="padding:8px;">DC charge 20-80%</td><td style="padding:8px;">~45 min at 240 kW dual-gun</td></tr>
<tr><td style="padding:8px;">Battery swap time</td><td style="padding:8px;">5-6 min (swap variant)</td></tr>
<tr><td style="padding:8px;">Fifth wheel</td><td style="padding:8px;">50 mm oscillating, terminal-rated</td></tr>
<tr><td style="padding:8px;">Gradeability</td><td style="padding:8px;">&ge;30% at full load</td></tr>
<tr><td style="padding:8px;">Battery warranty</td><td style="padding:8px;">8 years / 4,500 cycles to 70% SOH</td></tr>
<tr><td style="padding:8px;">FOB price band</td><td style="padding:8px;">US$78,000-95,000</td></tr>
</table>
<p>Two specification points matter specifically for Tema. First, the 2,800 Nm of near-instant torque means a loaded 40 ft container combination pulls away from the stack with full power from zero rpm &mdash; no clutch slip and no turbo lag &mdash; so the tractor is faster across the first 50 metres, which is the distance that decides yard throughput. Second, the CATL LFP chemistry tolerates Tema&rsquo;s 30-34&deg;C dry-season ambient without the degradation penalties of NMC packs, and the liquid-cooled pack holds cell temperature in the safe band through back-to-back shift cycles. Operators running the swap variant keep one spare pack per three tractors and never lose a tractor to charging downtime.</p>

<h2>The Energy Case at Ghanaian Diesel Prices</h2>
<p>Ghanaian diesel retails around US$1.05-1.15 per litre at the industrial pump. A 42 t diesel terminal tractor on Tema stop-start duty burns 0.55-0.65 L/km equivalent once idling is included, which is US$0.60-0.70 per kilometre. The TE46 consumes 1.5-1.8 kWh/km at 45 t GCW; at ECG industrial tariffs of roughly US$0.11-0.13/kWh, that is US$0.18-0.23 per kilometre. On 180 km of yard moves per shift, 300 shifts a year, the annual energy saving is about US$14,000-17,000 per tractor. Add maintenance &mdash; no engine, transmission or diesel particulate filter &mdash; at another US$4,000-6,000 per year, and the combined annual saving reaches US$20,000-23,000. Against the US$25,000-40,000 purchase premium over a diesel terminal tractor, payback lands at 16-22 months, inside the first battery-warranty window.</p>
<ul>
<li><strong>Energy cost per km:</strong> diesel ~US$0.65 vs EV truck ~US$0.20 &mdash; a 68% reduction</li>
<li><strong>Queue idling:</strong> roughly 30% of the diesel fuel bill eliminated entirely</li>
<li><strong>Annual saving per tractor:</strong> US$20,000-23,000 (energy + maintenance)</li>
<li><strong>Payback:</strong> 16-22 months at Ghanaian fuel and power prices</li>
<li><strong>Terminal air quality:</strong> zero NOx and particulates inside the gate &mdash; an emerging GPHA requirement</li>
</ul>

<h2>Battery Swap vs Depot Charging at Tema</h2>
<p>Tema operators have two proven charging strategies. Depot DC fast charging is simplest: one 240 kW dual-gun unit restores 20-80% in about 45 minutes, matched to the shift-change break, and serves 6-10 tractors on rotation with managed overnight AC for the balance. The battery-swap configuration changes the math for two-shift operations: a single swap station serves 15-20 tractors, holds 6-8 packs on managed charge, and exchanges a pack in 5-6 minutes &mdash; faster than a diesel refuel and from a footprint that fits inside a container beside the terminal gate. We specify swap for fleets above ten tractors or any operation running two shifts, and depot charging below that. Both ship as a coordinated package with switchgear and load-management software preconfigured to the terminal&rsquo;s shift pattern.</p>
<p>Reliability is the honest question for a port that cannot tolerate a stalled tractor. The EV truck&rsquo;s sealed HV system has no air intake to clog with dust, no fuel-water separator to freeze, and no turbo to fail in the humid Accra climate. The maintenance calendar is brake inspection and coolant check every 40,000 km &mdash; a rounding error beside the diesel terminal tractor&rsquo;s engine and DPF load &mdash; and CATL modules stocked in the region reach Tema in 10-14 days.</p>

<h2>Import, Homologation and Ghana&rsquo;s EV Incentives</h2>
<p>Ghana applies preferential duty treatment to electric commercial vehicles under its EV policy framework, against the standard 20% levy on diesel trucks, and Tema&rsquo;s own RoRo facilities are the most efficient on the coast for truck imports, with 30-36 day sailings from China and fast customs clearance for documented vehicles. We supply the full export pack: bill of lading, UN R100 battery safety certification, charger compliance papers and French/English manuals. Terminal operators running multi-port West African networks should also review our <a href="../markets/ghana.html">Ghana market page</a> alongside the Lom&eacute; and Abidjan equivalents &mdash; the same TE46 platform serves the region&rsquo;s major terminals with one parts stock and one training standard, which is exactly how the large 3PLs we work with structure their coastal fleets.</p>

<h2>Who Moves First at West Africa&rsquo;s Gateway</h2>
<p>The natural first adopters are the terminal concessionaires and the large drayage groups with captive yard routes and captive depots &mdash; they control both ends of the duty cycle, run the highest utilisation, and report directly to a port authority that is increasingly measuring gate emissions. The fleets that electrify Tema&rsquo;s final-leg first bank a cost advantage their diesel competitors cannot answer, while locking in the scope-3 reporting that multinational shipping lines now demand from their terminal partners. The arithmetic above is not a projection; it is the same architecture already running in ports from Tanger Med to Dar es Salaam, and Tema&rsquo;s expansion has simply made the duty cycle busier and the case sharper.</p>
'''))

# ---------------------------------------------------------------- 2
ARTICLES.append(dict(
f='cape-town-south-africa-electric-delivery-truck',
t='Cape Town Urban Freight: KT5J Electric Delivery Trucks for South Africa&rsquo;s Mother City',
d='Cape Town last-mile freight suits the KT5J electric delivery truck: 106-130 kWh CATL LFP, 180-220 km range and solar-resilient depot charging against load-shedding. EV truck specs, TCO and import guide.',
k='KT5J electric delivery truck, EV truck South Africa, electric truck Cape Town, electric delivery truck load shedding, Dongfeng electric truck, last mile EV truck Cape Town, urban freight electric truck',
img='models/p07_08.jpg',
alt='Dongfeng KT5J electric delivery truck on a Cape Town urban freight route, EV truck for South Africa last-mile delivery',
net='zhc',
body='''
<p>Cape Town is South Africa&rsquo;s legislative and tourism heart, and its urban freight network &mdash; supermarkets, FMCG distribution, e-commerce and the goods moving between the Cape Town International Convention Centre district, the Athlone and Epping industrial areas, and the southern suburbs &mdash; runs on 3-8 t delivery trucks that idle in traffic and pay for diesel at some of the highest pump prices in the region. It is also a city defined by load-shedding, which makes depot-based solar charging not a nice-to-have but a resilience strategy. This article examines the <a href="../products/models/kt5j-electric-cargo-truck.html">Dongfeng KT5J electric delivery truck</a> in Cape Town service, with real numbers on range, cost per kilometre, and charging that keeps running when the grid does not. For Cape Town distributors and 3PLs watching the <a href="../markets/south-africa.html">South Africa market</a>, an EV truck fleet is both a cost play and a continuity plan.</p>
<p>Cape Town&rsquo;s freight profile is shifting in ways that favour electric trucks precisely now. E-commerce volumes in the Western Cape have grown at double-digit rates since the pandemic, the constrained Atlantic Seaboard and City Bowl road network pushes more deliveries into early-morning and evening windows where silent operation avoids resident complaints, and the Cape Flats industrial belt &mdash; Epping, Montague Gardens and Philippi &mdash; concentrates the return-to-base depots that make depot charging trivial. The airport cargo precinct and the foreshore convention district add a premium, time-sensitive layer of urban freight that values predictable movement over raw speed. The Cape Town municipality has also signalled tighter inner-city air-quality and noise rules, which reward operators who can demonstrate zero-tailpipe running on the CBD approaches. None of this alters the underlying physics &mdash; short routes, paid descents, depot nights and expensive diesel remain what makes an EV truck cheaper to own &mdash; but it raises the urgency, because the city&rsquo;s delivery density is climbing exactly as its grid gets cleaner and its outages get more frequent, the rare case where the cost and resilience stories point the same way.</p>

<h2>Why the Mother City Is Built for Electric Delivery</h2>
<p>Urban delivery in Cape Town is short, dense and return-to-base. A typical KT5J route is 70-140 km per day: a morning run from an Epping or Montague Gardens DC to the southern suburbs and the CBD, afternoon backhauls from the docks, or metro-scale e-commerce drops. That distance sits inside the KT5J&rsquo;s 180-220 km real-world range with a 30% reserve, so no public charging is required. The stop-start profile also pays the EV truck back directly: every traffic-light stop and every descent from the Cape Flats ridge returns energy through regenerative braking, and our fleet data from comparable hilly coastal cities shows 12-18% energy recovery on routes with sustained grades. A diesel truck burns those decelerations into brake dust and heat.</p>

<h2>KT5J Specifications for Cape Town Duty</h2>
<table style="width:100%;border-collapse:collapse;margin:20px 0;" border="1" cellpadding="8">
<tr style="background:#006341;color:#fff;"><th style="padding:8px;text-align:left;">Parameter</th><th style="padding:8px;text-align:left;">KT5J Electric Delivery Truck</th></tr>
<tr><td style="padding:8px;">GVW / payload</td><td style="padding:8px;">7.5-9 t class / 3.5-4.5 t payload</td></tr>
<tr><td style="padding:8px;">Battery</td><td style="padding:8px;">106-130 kWh CATL LFP, liquid-cooled</td></tr>
<tr><td style="padding:8px;">Motor</td><td style="padding:8px;">LvKong 120-150 kW peak / 950-1,200 Nm</td></tr>
<tr><td style="padding:8px;">Real-world range (urban, loaded)</td><td style="padding:8px;">180-220 km</td></tr>
<tr><td style="padding:8px;">DC charge 20-80%</td><td style="padding:8px;">~35 min at 90-120 kW</td></tr>
<tr><td style="padding:8px;">Body volume</td><td style="padding:8px;">22-28 m&sup3; box, side-door, tail-lift options</td></tr>
<tr><td style="padding:8px;">Gradeability</td><td style="padding:8px;">&ge;25% at full load</td></tr>
<tr><td style="padding:8px;">Battery warranty</td><td style="padding:8px;">8 years / 4,500 cycles to 70% SOH</td></tr>
<tr><td style="padding:8px;">FOB price band</td><td style="padding:8px;">US$45,000-56,000</td></tr>
</table>
<p>The 25% gradeability figure is the first thing Cape Town operators ask about, because the city&rsquo;s topography is not gentle: the climbs to Constantia, the eastern suburbs and the Tygerberg all exceed 10%. The KT5J&rsquo;s permanent-magnet motor delivers peak torque from zero rpm, so it pulls away on a 12% grade at full load without clutch slip or rollback. Drivers transitioning from diesel report the hill starts as the biggest daily quality-of-life change, followed by the silent cab during the city&rsquo;s long summer traffic jams.</p>

<h2>The TCO Against High South African Diesel Prices</h2>
<p>South African diesel runs around US$1.00-1.10 per litre at the commercial pump (roughly R19-21/L), and a 7.5-9 t box truck on Cape Town stop-start duty burns 0.26-0.32 L/km &mdash; about US$0.30 per kilometre. The KT5J consumes 0.60-0.75 kWh/km on the same routes; at City of Cape Town / Eskom commercial tariffs of roughly US$0.13-0.16/kWh, that is US$0.10-0.12 per kilometre. On 3,500 km per month, the energy saving is about US$630 per truck per month, and maintenance &mdash; no oil, no clutch, no injectors, no DPF, and brake pads lasting 2-3x longer &mdash; adds another US$150-250. Total: roughly US$9,500 per truck per year. Against a purchase premium of US$15,000-20,000, payback arrives in 18-24 months, inside a battery warranty that runs 8 years or 4,500 cycles.</p>
<ul>
<li><strong>Energy cost per km:</strong> US$0.30 diesel vs US$0.11 electric &mdash; a 63% saving</li>
<li><strong>Monthly saving per truck:</strong> ~US$780 including maintenance</li>
<li><strong>Payback:</strong> 18-24 months at Cape Town energy prices</li>
<li><strong>Load-shedding resilience:</strong> solar-plus-battery depot keeps chargers running through stage 4-6 outages</li>
</ul>

<h2>Charging Through Load-Shedding</h2>
<p>Cape Town&rsquo;s grid reality makes the charging plan different from a European or North American deployment. A first-wave fleet of 5-10 KT5Js needs one 90-120 kW DC charger for daytime rotation plus 22 kW AC posts per bay overnight &mdash; about 250-350 kVA of connected load, well within commercial service in Epping and Montague Gardens. The critical design choice is a solar canopy over the depot with battery storage: Cape Town averages 4.5-5.0 peak sun hours daily, so a 100-150 kWp array covers 35-50% of annual charging energy and, paired with a hybrid inverter, keeps the chargers alive through load-shedding stages. We file the municipal and Eskom connection application on purchase-order day, because the 8-14 week connection lead time always exceeds the 30-35 day vessel transit from China to the Cape Town port.</p>
<p>The fleet&rsquo;s own batteries are a second buffer. Ten KT5Js carry over 1,000 kWh of storage; a two-hour outage is absorbed by resequencing charge sessions with zero operational impact. Fleets wanting hard resilience add a modest stationary battery that also powers the depot office and cold-room during outages, turning the truck fleet into the site&rsquo;s uninterruptible power supply.</p>

<h2>Import and South African Fleet Strategy</h2>
<p>South Africa&rsquo;s electric commercial vehicle tariff framework is more favourable than the diesel equivalent, and the Cape Town and Durban RoRo terminals handle truck imports routinely, with 28-34 day sailings from China&rsquo;s east coast. We supply the complete homologation dossier, UN R100 battery certification and the two-year parts kit, with English documentation throughout. National fleets running Cape Town and Gauteng operations should note our <a href="../markets/south-africa.html">South Africa market page</a> &mdash; the KT5J serves both metros with one parts stock and one training standard, and a Cape Town pilot feeding a Johannesburg rollout is the playbook several retail groups are already running. Support ships with the trucks: CATL module stock reachable in 10-14 days, telematics-based remote diagnostics, and a terminal-duty maintenance calendar that removes the diesel workshop dependency.</p>

<h2>The Cape Town First-Mover Case</h2>
<p>The strongest candidates are the supermarket and FMCG distributors with captive Cape Town metro routes, the e-commerce fulfilment fleets whose dense urban drops suit the 7.5-9 t class, and the 3PLs serving the tourism and convention corridor. Cape Town&rsquo;s diesel prices are not falling, its load-shedding is not ending, and its municipal air-quality rules are tightening. The fleets that electrify their metro routes first bank a cost advantage their diesel competitors cannot match, while gaining a resilience story &mdash; trucks that charge through stage 6 &mdash; that no diesel fleet can tell.</p>
'''))

# ---------------------------------------------------------------- 3
ARTICLES.append(dict(
f='abuja-nigeria-electric-truck-government-fleet',
t='Abuja Government Fleet Electrification: Electric Trucks for Nigeria&rsquo;s Federal Capital',
d='Abuja ministry and municipal fleets can cut operating cost 55% with the KT5M electric box truck: 180-220 kWh CATL LFP, tender-ready specs and lower energy cost per km. EV truck procurement guide.',
k='KT5M electric box truck, EV truck Nigeria, electric truck Abuja, government fleet electric truck, Dongfeng electric truck, electric truck procurement tender, Abuja municipal fleet',
img='models/p07_05.jpg',
alt='Dongfeng KT5M electric box truck in Abuja government fleet service, EV truck for Nigeria federal capital logistics',
net='gen',
body='''
<p>Abuja was planned as a low-density federal capital, which makes it a surprisingly good city for electric trucks: ministries and agencies run fixed, predictable routes between the Central Business District, the Maitama and Asokoro districts, the Kubwa and Gwagwalada corridors, and the Giri and Idu industrial clusters. As Nigeria&rsquo;s federal government pushes fleet modernisation and scope-3 reporting, the boxes and service trucks ferrying documents, equipment and municipal cargo are a natural first wave. This article works through the <a href="../products/models/kt5m-electric-cargo-truck.html">Dongfeng KT5M electric box truck</a> as an Abuja government fleet vehicle &mdash; tender-ready specifications, operating cost, charging on the FCT grid, and the procurement path. For ministries, the <a href="../markets/nigeria.html">Nigeria market</a> case is both a budget story and a public-sector leadership statement, and the visible zero-emission federal fleet that results is itself a policy asset the administration can demonstrate to development partners and citizens alike, while the operating saving frees budget that would otherwise be locked in diesel imports.</p>
<p>Abuja&rsquo;s federal structure creates a procurement environment that is unusually friendly to fleet electrification. Ministries and agencies purchase against multi-year budgets with lifecycle-cost scoring, which means the higher upfront price of an EV truck is weighed against the lower operating cost over the contract &mdash; exactly the comparison diesel wins on price but loses on total cost. The Federal Capital Territory Administration has also set public-sector emissions and local-content expectations that favour electric commercial vehicles, and several ministries now require scope-3 reporting on their logistics, a criterion a diesel box truck simply cannot meet. The fixed geography helps: the capital&rsquo;s radial plan keeps most trips inside a 30 km radius, the Giri and Idu industrial clusters host the maintenance and body-building capacity needed to support a fleet locally, and the FCT&rsquo;s own power and water boards run service bodies that suit the KT5M platform directly. Training is another advantage &mdash; government drivers and mechanics can be brought through a single centralized programme, and the telematics portal gives fleet managers the audit-ready battery and drivetrain health reports that public procurement increasingly demands. For ministries, the EV truck is therefore not a leap of faith but a documented, scored, budgeted line item. The Kubwa and Gwagwalada corridors, the Gwarinpa and Bwari districts and the constant shuttle between the Central Business District and the Maitama and Asokoro enclaves give the KT5M a duty cycle so predictable that charging can be scheduled around the disco&rsquo;s time-of-use windows, shaving the already-low energy cost further. Abuja&rsquo;s strong solar resource &mdash; over 5.5 peak sun hours &mdash; lets agency depots add canopies that cover a large share of annual charging from self-generated power, turning a budget line into a near-fixed, predictable cost.</p>

<h2>Why Government Fleets Electrify First</h2>
<p>Public-sector fleets are the lowest-risk EV truck entry point in almost any market because the duty cycle is controlled. Routes are fixed and short, schedules are daytime and predictable, and every vehicle returns to a government depot at night. Abuja&rsquo;s geography reinforces this: the city&rsquo;s radial layout keeps most ministry trips inside 10-30 km, so a KT5M covering 80-140 km per day sits well inside its 200-240 km real-world range. The second driver is procurement policy. As more federal and state tenders include emissions and local-content criteria, an electric box truck is no longer a novelty line item but a compliance advantage &mdash; and the operating-cost saving funds the premium within the first contract term.</p>

<h2>KT5M Specifications for Abuja Fleets</h2>
<table style="width:100%;border-collapse:collapse;margin:20px 0;" border="1" cellpadding="8">
<tr style="background:#006341;color:#fff;"><th style="padding:8px;text-align:left;">Parameter</th><th style="padding:8px;text-align:left;">KT5M Electric Box Truck</th></tr>
<tr><td style="padding:8px;">GVW / payload</td><td style="padding:8px;">9-12 t class / 4.5-6 t payload</td></tr>
<tr><td style="padding:8px;">Battery</td><td style="padding:8px;">180-220 kWh CATL LFP, liquid-cooled</td></tr>
<tr><td style="padding:8px;">Motor</td><td style="padding:8px;">LvKong 150-190 kW peak / 1,100-1,500 Nm</td></tr>
<tr><td style="padding:8px;">Real-world range (urban, loaded)</td><td style="padding:8px;">200-240 km</td></tr>
<tr><td style="padding:8px;">DC charge 20-80%</td><td style="padding:8px;">~40 min at 120 kW</td></tr>
<tr><td style="padding:8px;">Body volume</td><td style="padding:8px;">28-35 m&sup3; dry box, insulated, or utility body</td></tr>
<tr><td style="padding:8px;">Gradeability</td><td style="padding:8px;">&ge;25% at full load</td></tr>
<tr><td style="padding:8px;">Battery warranty</td><td style="padding:8px;">8 years / 4,500 cycles to 70% SOH</td></tr>
<tr><td style="padding:8px;">FOB price band</td><td style="padding:8px;">US$52,000-66,000</td></tr>
</table>
<p>The 28-35 m&sup3; body suits the range of Abuja government work: records and archive shuttles, municipal workshop equipment, FCT water-board service bodies, and the utility configurations used by power and telecommunications agencies. Gradeability matters because the city&rsquo;s districts sit on broken terrain; the KT5M&rsquo;s motor holds torque to rated speed and climbs the Gwarinpa and Bwari grades at full load where a diesel box truck drops to second gear.</p>

<h2>The Operating-Cost Case for the FCT Budget</h2>
<p>Nigerian diesel retails around US$1.00-1.15 per litre (roughly N1,000-1,200/L) at the government pump. A 9-12 t box truck on Abuja duty burns 0.30-0.38 L/km &mdash; about US$0.35 per kilometre. The KT5M consumes 0.80-0.95 kWh/km; at Abuja disco tariffs of roughly US$0.14-0.17/kWh, that is US$0.14 per kilometre. On 3,000 km per month, the energy saving is about US$630 per truck per month, and maintenance &mdash; no oil changes, no injector servicing, no DPF &mdash; adds another US$150-200. Total: roughly US$9,000 per truck per year against a purchase premium of US$18,000-25,000, so payback arrives in 20-28 months. For a fleet financed on a multi-year contract, the saving then runs the remaining battery-warranty life as recovered budget.</p>
<ul>
<li><strong>Energy cost per km:</strong> US$0.35 diesel vs US$0.14 electric &mdash; a 60% reduction</li>
<li><strong>Annual saving per truck:</strong> ~US$9,000 (energy + maintenance)</li>
<li><strong>Payback:</strong> 20-28 months inside the battery-warranty period</li>
<li><strong>Tender advantage:</strong> zero-tailpipe option satisfies emerging emissions criteria in federal procurement</li>
</ul>

<h2>Charging at Government Depots</h2>
<p>Abuja&rsquo;s ministry and municipal depots have the medium-voltage capacity for fleet charging; a ten-truck KT5M fleet runs on roughly 300-400 kVA with managed charging, a standard commercial connection for the FCT grid. The layout we deploy: one 120 kW DC charger per 6-8 trucks for daytime rotation, overnight AC posts per bay, and a load-management controller sized for double the initial fleet because agency fleets grow. Solar canopies over government yards are strongly economic &mdash; Abuja receives 5.5-6.0 peak sun hours &mdash; and several FCT buildings already carry rooftop solar, so adding truck charging to existing generation is the cheapest increment. The fleet&rsquo;s own batteries buffer the grid: a 2-hour outage is absorbed by resequencing charge sessions with zero impact on the morning dispatch.</p>

<h2>Procurement, Tenders and Import</h2>
<p>Nigeria&rsquo;s EV import framework is more favourable than the diesel equivalent, and the Lagos and Onne ports handle RoRo truck imports with 30-36 day sailings from China. We deliver the full tender pack: homologation dossier, UN R100 battery certification, charger compliance papers, English manuals, and a spare-parts schedule written to procurement specifications. Agencies running national operations should review our <a href="../markets/nigeria.html">Nigeria market page</a> &mdash; the KT5M serves Abuja, Lagos and Kano with one parts stock and one training standard, and a capital-city pilot feeding a state-level rollout is the structure several ministries are adopting. Support follows our government-fleet protocol: a two-year parts kit per fleet, CATL module availability in 10-14 days, and telematics-based remote diagnostics that give fleet managers live battery and drivetrain health for audit reporting.</p>

<h2>The Public-Sector First-Mover Logic</h2>
<p>The natural first adopters are the FCT municipal services fleets, the ministry logistics units with fixed CBD-to-cluster routes, and the utility agencies whose service bodies suit the KT5M platform. Abuja&rsquo;s fuel subsidy environment is volatile, its air-quality rules are tightening, and its procurement is increasingly scored on emissions. The agencies that electrify their box-truck fleets first convert a budget line into a visible leadership statement &mdash; and the operating-cost saving funds the transition within the first contract term.</p>
'''))

# ---------------------------------------------------------------- 4
ARTICLES.append(dict(
f='hawassa-ethiopia-industrial-park-electric-truck',
t='Hawassa Industrial Park: Electric Trucks for Ethiopia&rsquo;s Textile Export Logistics',
d='Hawassa&rsquo;s textile exporters cut freight cost with the KTH3 electric cargo truck: 262 kWh CATL LFP, cheap hydro power at ~$0.05/kWh and a lower energy cost per km than diesel. EV truck guide.',
k='KTH3 electric cargo truck, EV truck Ethiopia, electric truck Hawassa, textile export electric truck, Dongfeng electric truck, Hawassa Industrial Park logistics, Djibouti corridor EV truck',
img='models/p07_06.jpg',
alt='Dongfeng KTH3 electric cargo truck at Hawassa Industrial Park, Ethiopia, EV truck for textile export logistics',
net='zhc',
body='''
<p>Hawassa Industrial Park is the flagship of Ethiopia&rsquo;s textile and garment export strategy, housing global apparel suppliers whose finished goods ship to the Port of Djibouti and then to Europe and North America. That freight moves first by truck &mdash; from the park&rsquo;s factory floors to the Modjo dry port and the Addis Ababa logistics cluster, then onward to Djibouti &mdash; and those shuttle runs burn diesel at a pump price that, while subsidised, still costs more per kilometre than Ethiopia&rsquo;s famously cheap hydropower. This article examines the <a href="../products/models/kth3-electric-cargo-truck.html">Dongfeng KTH3 electric cargo truck</a> in Hawassa&rsquo;s export-logistics role, with real numbers on energy, range to the dry port, and charging on one of the world&rsquo;s lowest-cost grids. For the park&rsquo;s operators and exporters watching the <a href="../markets/ethiopia.html">Ethiopia market</a>, an EV truck fleet is a scope-3 advantage with a payback measured in months.</p>
<p>The export-logistics case for Hawassa is strengthened by where the value sits in apparel supply chains. Buyers in the EU and North America increasingly price scope-3 transport emissions into supplier scorecards, and a zero-tailpipe leg from the park to the dry port is a credential Ethiopian exporters can charge for. The park&rsquo;s own infrastructure &mdash; reliable industrial power, fenced and guarded yards, and a workforce already maintaining textile machinery &mdash; removes the two biggest barriers to fleet electrification, which are charging access and technician training. Several park tenants already run solar arrays for factory load, so adding truck charging to existing generation is the cheapest possible increment. The Hawassa-to-Djibouti corridor is also the template for the rest of the country&rsquo;s export freight: once the KTH3 proves itself on the park-to-Modjo loop, the same platform extends to the Addis logistics cluster and onward, with one parts stock and one training standard serving the entire chain. That scalability is why the park&rsquo;s operators treat the first EV truck order as infrastructure, not just a vehicle purchase.</p>

<h2>Why Hawassa&rsquo;s Corridor Fits Electric Freight</h2>
<p>Textile and garment logistics have three properties that make them ideal EV truck duty. Routes are fixed: park to Modjo dry port (about 250 km), park to Addis distribution (about 275 km), and constant internal shuttles between factory gates and the on-site warehouse. Schedules are shift-based and predictable, so charging windows are predictable. And the trucks return nightly to the same powered, guarded yard inside the park. The Hawassa-to-Modjo leg sits at the edge of a single-charge envelope, which is exactly why we specify the 262 kWh pack and a destination charger at the dry port &mdash; the trucks arrive with reserve, top up during the customs dwell, and return to Hawassa on regenerated energy from the highland descent.</p>
<p>The second factor is uniquely Ethiopian. The national grid is over 90% hydropower, and industrial tariffs in the Hawassa zone run roughly US$0.04-0.06 per kWh &mdash; among the lowest electricity prices on earth. At that price an electric truck&rsquo;s energy cost per kilometre is a fraction of diesel even before maintenance, and the descent from the Ethiopian highlands to the Awash corridor recovers 15-22% of the round-trip energy through regenerative braking.</p>

<h2>KTH3 Specifications for Export Logistics</h2>
<table style="width:100%;border-collapse:collapse;margin:20px 0;" border="1" cellpadding="8">
<tr style="background:#006341;color:#fff;"><th style="padding:8px;text-align:left;">Parameter</th><th style="padding:8px;text-align:left;">KTH3 4x2 Electric Cargo Truck</th></tr>
<tr><td style="padding:8px;">GVW / payload</td><td style="padding:8px;">16-18 t class / 9-11 t payload</td></tr>
<tr><td style="padding:8px;">Battery</td><td style="padding:8px;">262 kWh CATL LFP, liquid-cooled</td></tr>
<tr><td style="padding:8px;">Motor</td><td style="padding:8px;">LvKong 220-260 kW peak / 1,800-2,000 Nm</td></tr>
<tr><td style="padding:8px;">Real-world range (loaded, mixed)</td><td style="padding:8px;">250-320 km</td></tr>
<tr><td style="padding:8px;">DC charge 20-80%</td><td style="padding:8px;">~50 min at 180 kW</td></tr>
<tr><td style="padding:8px;">Body volume</td><td style="padding:8px;">48-60 m&sup3; curtainside or box body</td></tr>
<tr><td style="padding:8px;">Gradeability</td><td style="padding:8px;">&ge;30% at full load</td></tr>
<tr><td style="padding:8px;">Battery warranty</td><td style="padding:8px;">8 years / 4,500 cycles to 70% SOH</td></tr>
<tr><td style="padding:8px;">FOB price band</td><td style="padding:8px;">US$60,000-76,000</td></tr>
</table>
<p>The 48-60 m&sup3; curtainside body suits garment cartons, which cube out before they weigh out, so the 9-11 t payload covers a full trailer of finished apparel. Gradeability matters on the climb out of the Rift Valley toward Addis; the KTH3 holds torque to rated speed and climbs the Mojo grade at full load where a diesel cargo truck drops to low gears. The LFP pack tolerates Hawassa&rsquo;s warm climate without NMC degradation, and the liquid-cooled system holds cell temperature through back-to-back corridor runs.</p>

<h2>The TCO on Ethiopian Hydro Power</h2>
<p>Ethiopian diesel retails around US$0.95-1.05 per litre at the commercial pump. A 16-18 t cargo truck on the Hawassa-Modjo duty burns 0.40-0.48 L/km &mdash; about US$0.42 per kilometre. The KTH3 consumes 1.0-1.2 kWh/km on the loaded climb; at the industrial tariff of roughly US$0.05/kWh, that is US$0.05-0.06 per kilometre. On 4,000 km per month &mdash; a two-shift export shuttle &mdash; the monthly energy saving is about US$1,450 per truck. Maintenance adds another US$200-300 monthly: no engine oil, no injectors, no clutch, and brake pads lasting 3x longer under regenerative braking on the descent. Total: roughly US$20,000 per truck per year against a purchase premium of US$25,000-35,000, so payback lands at 15-20 months &mdash; among the fastest in our portfolio, driven almost entirely by hydro power pricing.</p>
<ul>
<li><strong>Energy cost per km:</strong> US$0.42 diesel vs US$0.06 electric &mdash; an 86% reduction</li>
<li><strong>Annual saving per truck:</strong> ~US$20,000 (energy + maintenance)</li>
<li><strong>Payback:</strong> 15-20 months at Ethiopian hydro tariffs</li>
<li><strong>Scope-3 advantage:</strong> zero-tailpipe export leg strengthens EU/US buyer sustainability scoring</li>
</ul>

<h2>Charging Inside the Park and at Modjo</h2>
<p>Hawassa Industrial Park already runs high-reliability industrial power for its factories, which makes depot charging straightforward: one 180 kW DC charger per 5-6 trucks for rotation top-ups plus overnight AC at each bay. The connected load for a ten-truck fleet is about 350-450 kVA, well within the park&rsquo;s supply. The Modjo dry port gets a single destination charger on the same platform, restoring 20-80% during the customs dwell so trucks return to Hawassa without a range deficit. Solar is optional here &mdash; Ethiopia&rsquo;s grid is already hydro-clean &mdash; but a modest park canopy still hedges against any future tariff step and provides covered staging for export cartons.</p>
<p>Resilience is structural: the trucks themselves are the buffer. A ten-truck KTH3 fleet carries over 2,500 kWh of storage, and the park&rsquo;s own backup generation (already sized for factory lines) easily covers charging during any grid event. The EV truck&rsquo;s sealed HV system has no air intake to clog with dust and no fuel system to contaminate &mdash; an advantage in a park where uptime protects export letters of credit.</p>

<h2>Import and Corridor Strategy</h2>
<p>Ethiopia grants favourable treatment to electric commercial vehicles under its industrialization incentives, and Djibouti&rsquo;s port handles the ocean leg with efficient transhipment to Europe and North America. We supply the full export pack: homologation dossier, UN R100 battery certification, charger compliance papers, and English manuals. Exporters running the Hawassa-Addis-Djibouti chain should review our <a href="../markets/ethiopia.html">Ethiopia market page</a> &mdash; the KTH3 serves the entire corridor with one parts stock and one training standard, and a park-based pilot feeding a national rollout is the structure the large apparel groups are adopting. Support ships with the fleet: a two-year parts kit, CATL module availability in 12-18 days, and telematics-based remote diagnostics for live battery and drivetrain health.</p>

<h2>The Hawassa First-Mover Case</h2>
<p>The natural first adopters are the park&rsquo;s largest apparel suppliers with captive shuttle routes to Modjo, the 3PLs serving the export corridor, and the bonded-warehouse operators whose fixed loops suit the KTH3 platform. Ethiopia&rsquo;s hydro power is not getting more expensive, its export buyers are demanding lower-carbon logistics, and its industrial policy is explicitly pro-electrification. The suppliers that electrify their export leg first convert a cost line into a sustainability credential &mdash; and bank a payback measured in months, not years.</p>
'''))

# ---------------------------------------------------------------- 5
ARTICLES.append(dict(
f='kisumu-kenya-lake-basin-electric-cargo-truck',
t='Kisumu and the Lake Basin: KT5L Electric Cargo Trucks for Western Kenya Distribution',
d='Kisumu Lake Basin distribution suits the KT5L electric cargo truck: 130-160 kWh CATL LFP, 190-230 km range and geothermal-powered charging. EV truck specs, TCO and cross-border trade guide.',
k='KT5L electric cargo truck, EV truck Kenya, electric truck Kisumu, Lake Basin electric truck, Dongfeng electric truck, Kisumu Busia Uganda cross border, Western Kenya distribution EV truck',
img='models/p07_09.jpg',
alt='Dongfeng KT5L electric cargo truck in Kisumu, Kenya, EV truck for Lake Victoria basin distribution',
net='zhc',
body='''
<p>Kisumu is the commercial capital of Western Kenya and the logistics hinge of the Lake Victoria basin. From here, freight fans out to the Ugandan border at Busia, south to Migori and the Tanzanian corridor, and north toward Eldoret &mdash; much of it 3-7 t distribution trucks serving the cross-border trade that defines the region&rsquo;s economy. Those trucks burn diesel at Kenya&rsquo;s import-parity pump price while running short, repetitive loops that are ideal electric territory. This article looks at the <a href="../products/models/kt5l-electric-cargo-truck.html">Dongfeng KT5L electric cargo truck</a> in Kisumu basin service, with real numbers on range, cost per kilometre, and charging on Kenya&rsquo;s geothermal-heavy grid. For Kisumu distributors and cross-border traders watching the <a href="../markets/kenya.html">Kenya market</a>, an EV truck fleet is a margin decision made sharp by geography.</p>
<p>The cross-border dimension makes Kisumu different from a pure domestic distribution city. Busia is the busiest Uganda-Kenya crossing, and the freight that clears there &mdash; consumer goods northbound, produce and fish southbound &mdash; runs on loops so repetitive that they are ideal for a return-to-base EV truck fleet charged on the Kenya side. Ugandan importers increasingly ask about the carbon profile of their inbound freight, and a Kisumu-based electric fleet gives Kenyan 3PLs a selling point at the border. The lakeshore produce trade &mdash; the Nile perch and tilapia from the beaches around Homa Bay and Mbita, the horticulture from the Kisii highlands &mdash; is time-sensitive and benefits from the KT5L&rsquo;s silent, cool running and predictable range. Kisumu&rsquo;s own municipal market distribution, the NGO and humanitarian logistics that stage through the city for the wider basin, and the growing e-commerce fulfilment serving western Kenya all add density to the same short loops. None of these loads are heavy enough to stress the 2.5-3.5 t payload, and all of them cube out before they weigh out, which is exactly the freight an electric cargo truck carries most profitably. The result is a basin where the duty cycle, the grid and the trade all point toward electrification at once.</p>

<h2>The Lake Basin Duty Cycle</h2>
<p>Western Kenya distribution is compact. Kisumu to Busia is about 110 km, Kisumu to Migori about 85 km, Kisumu to Eldoret about 130 km &mdash; all inside the KT5L&rsquo;s single-charge range with reserve. A typical basin truck runs 90-160 km per day across two waves: a morning run to the border or the southern corridor, an afternoon backhaul, and constant city distribution inside Kisumu itself. The trucks sleep in the same depot every night, so no public charging is required and the entire operation runs on one yard charger. Cross-border trade adds utilisation: the Busia-Uganda leg is a twice-daily loop for many operators, which doubles annual kilometres and halves the payback on the electric premium.</p>
<p>Kisumu&rsquo;s terrain is gentler than the Rift Valley escarpments, but the routes to the border and the lakeshore include grades where regenerative braking pays back; our East African fleet data shows 10-15% energy recovery on basin routes with sustained climbs. A diesel truck spends those decelerations on brake linings and fuel; the KT5L recovers them into the pack.</p>

<h2>KT5L Specifications for the Basin</h2>
<table style="width:100%;border-collapse:collapse;margin:20px 0;" border="1" cellpadding="8">
<tr style="background:#006341;color:#fff;"><th style="padding:8px;text-align:left;">Parameter</th><th style="padding:8px;text-align:left;">KT5L Electric Cargo Truck</th></tr>
<tr><td style="padding:8px;">GVW / payload</td><td style="padding:8px;">6-7.5 t class / 2.5-3.5 t payload</td></tr>
<tr><td style="padding:8px;">Battery</td><td style="padding:8px;">130-160 kWh CATL LFP, liquid-cooled</td></tr>
<tr><td style="padding:8px;">Motor</td><td style="padding:8px;">LvKong 110-140 kW peak / 900-1,100 Nm</td></tr>
<tr><td style="padding:8px;">Real-world range (urban, loaded)</td><td style="padding:8px;">190-230 km</td></tr>
<tr><td style="padding:8px;">DC charge 20-80%</td><td style="padding:8px;">~35 min at 90-120 kW</td></tr>
<tr><td style="padding:8px;">Body volume</td><td style="padding:8px;">18-24 m&sup3; box, curtainside, tail-lift options</td></tr>
<tr><td style="padding:8px;">Gradeability</td><td style="padding:8px;">&ge;25% at full load</td></tr>
<tr><td style="padding:8px;">Battery warranty</td><td style="padding:8px;">8 years / 4,500 cycles to 70% SOH</td></tr>
<tr><td style="padding:8px;">FOB price band</td><td style="padding:8px;">US$44,000-55,000</td></tr>
</table>
<p>The 18-24 m&sup3; body covers the basin&rsquo;s freight mix &mdash; consumer goods, agricultural inputs, and the backhaul of fish and produce from the lakeshore. Gradeability covers the climbs toward the Nandi and Kisii highlands where a loaded diesel box truck drops to second gear; the KT5L holds torque to rated speed and climbs at 45-55 km/h, then regenerates part of the climb back on the descent. The 11.2 m turning circle suits Kisumu&rsquo;s older market-district access.</p>

<h2>The TCO on Kenya&rsquo;s Geothermal Grid</h2>
<p>Kenyan diesel runs around US$1.05-1.15 per litre at the commercial pump. A 6-7.5 t box truck on basin duty burns 0.26-0.32 L/km &mdash; about US$0.31 per kilometre. The KT5L consumes 0.60-0.75 kWh/km; at Kenya Power industrial tariffs of roughly US$0.11-0.14/kWh (geothermal-dominated and among the cleanest in Africa), that is US$0.09-0.10 per kilometre. On 3,500 km per month, the energy saving is about US$760 per truck per month, and maintenance &mdash; no oil, clutch, injectors or DPF &mdash; adds another US$150-200. Total: roughly US$11,000 per truck per year against a purchase premium of US$14,000-20,000, so payback lands at 15-20 months, inside the battery-warranty window. The Busia cross-border operators see stronger numbers still, because their higher daily kilometres are all charged at the EV truck&rsquo;s 70% energy discount.</p>
<ul>
<li><strong>Energy cost per km:</strong> US$0.31 diesel vs US$0.10 electric &mdash; a 68% reduction</li>
<li><strong>Annual saving per truck:</strong> ~US$11,000 (energy + maintenance)</li>
<li><strong>Payback:</strong> 15-20 months; faster on cross-border duty</li>
<li><strong>Clean grid:</strong> geothermal-dominated power makes the export leg genuinely low-carbon</li>
</ul>

<h2>Charging at the Kisumu Depot</h2>
<p>Kisumu&rsquo;s industrial areas have the medium-voltage capacity for fleet charging; a five-to-ten truck KT5L fleet needs 250-350 kVA with managed charging, a standard commercial connection for Kenya Power. The configuration: one 90-120 kW DC charger for midday rotation, overnight AC posts per bay, and load management that caps site draw at the contracted capacity while guaranteeing every truck&rsquo;s departure state of charge. We file the utility application on purchase-order day &mdash; the 8-12 week connection lead time exceeds the 30-35 day vessel transit from China to Mombasa, after which trucks rail or truck to Kisumu. Solar canopies are economic at Kisumu&rsquo;s 5.0-5.5 peak sun hours, covering 35-45% of annual charging energy and providing covered staging.</p>
<p>Grid reliability, the honest regional concern, is manageable by design: the fleet&rsquo;s own batteries are the buffer. Ten KT5Ls carry over 1,300 kWh of storage; a two-hour outage is absorbed by resequencing charge sessions with zero operational impact. Fleets wanting hard resilience add a solar-plus-battery canopy that keeps chargers alive through any local fault.</p>

<h2>Cross-Border Trade and Corridor Strategy</h2>
<p>Kenya applies favourable duty treatment to electric commercial vehicles, and Mombasa&rsquo;s port handles RoRo truck imports efficiently with onward rail or road to Kisumu. We supply the full export pack: homologation dossier, UN R100 battery certification, charger papers, and English manuals. Operators running the Busia-Uganda corridor should review our <a href="../markets/kenya.html">Kenya market page</a> &mdash; the KT5L serves both sides of the border with one parts stock and one training standard, and as Uganda&rsquo;s own EV incentives develop, a Kisumu-based electric fleet is positioned to run the entire western corridor from one base. Support ships with the trucks: a two-year parts kit, CATL module availability in 10-14 days, and telematics-based remote diagnostics.</p>

<h2>The Kisumu First-Mover Case</h2>
<p>The strongest candidates are the FMCG distributors with captive Kisumu-basin routes, the cross-border traders on the Busia loop whose utilisation is highest, and the 3PLs serving the lakeshore produce trade. Kenya&rsquo;s diesel prices are not falling, its grid is among the cleanest in Africa, and its cross-border trade is growing. The fleets that electrify the basin first bank a cost advantage their diesel competitors cannot match &mdash; and a low-carbon export leg that Uganda-bound buyers increasingly ask about.</p>
'''))

# ---------------------------------------------------------------- 6
ARTICLES.append(dict(
f='algiers-algeria-electric-dump-truck-construction',
t='Algiers Construction Logistics: TZ5E Electric Dump Trucks for Algeria&rsquo;s Capital',
d='Algiers metro and housing construction suits the TZ5E electric dump truck: 400 kWh CATL LFP, low night-noise operation and a lower energy cost per km than diesel. EV truck specs, TCO and import guide.',
k='TZ5E electric dump truck, EV truck Algeria, electric truck Algiers, electric tipper construction, Dongfeng electric truck, Algiers construction EV truck, 6x4 electric dump truck',
img='models/p03_05.jpg',
alt='Dongfeng TZ5E electric dump truck on an Algiers construction site, EV truck for Algeria capital construction',
net='zxc',
body='''
<p>Algiers is undergoing a sustained construction cycle &mdash; the metro extensions, the Ain Naadja and Bab Ezzouar housing programmes, and the constant site-mobilisation work that keeps the capital&rsquo;s tippers moving from dawn. Those tippers haul aggregates from the Mitidja plain quarries and the coastal sand operations into the city, and they do it under two pressures a diesel fleet feels acutely: urban night-work noise limits and an air-quality regime that is tightening around the bay. This article examines the <a href="../products/models/tz5e-electric-dump-truck.html">Dongfeng TZ5E electric dump truck</a> in Algiers construction service, with real numbers on payload, energy, charging on the Sonelgaz grid, and the import path. For Algerian contractors watching the <a href="../markets/algeria.html">Algeria market</a>, an EV truck tipper is both a compliance tool and a cost play.</p>
<p>Algiers&rsquo; construction pipeline is long enough that the compliance case for electric tippers strengthens every year. The metro extensions and the Ain Naadja, Bab Ezzouar and Kouba housing programmes run through or beside dense residential districts where night-work noise limits are enforced and complaints trigger stop-work orders that cost far more than any fuel saving. A near-silent electric tipper turns those restricted evening and overnight windows into productive shifts, and the zero-tailpipe operation removes the diesel soot that the bay&rsquo;s air-quality regime is progressively tightening. The Mitidja quarries and coastal sand operations that feed the city sit 15-45 km out &mdash; short, repetitive loops inside the TZ5E&rsquo;s range &mdash; and the ready-mix plants along the coastal corridor already run the kind of industrial power connection a charging depot needs. Public-works groups on nationally funded programmes also face emissions and local-content scoring that favours electric plant, and the TZ5E&rsquo;s sealed, low-maintenance drivetrain suits the dusty haul roads where diesel engines ingest abrasive silica and fail early. For Algiers contractors, the EV truck is therefore less a fuel bet than a permit and availability bet &mdash; and the maintenance saving funds part of the transition regardless of the diesel subsidy. The combination of noise compliance, air-quality rules and lower maintenance is why the capital&rsquo;s largest public-works groups are structuring electric tipper pilots now.</p>

<h2>Why Algiers Construction Electrifies Early</h2>
<p>Construction haulage has the profile electric trucks reward: short, repetitive, return-to-base loops. A typical Algiers tipper shift is 6-10 loaded trips of 25-60 km round trip between the Mitidja quarries and the city sites, totalling 150-220 km per day &mdash; inside the TZ5E&rsquo;s 260-320 km real-world range with a midday opportunity charge for the long days. The second driver is regulatory. Algiers enforces night-work noise limits in dense districts, and a near-silent electric tipper unlocks evening and overnight shifts that a diesel cannot run without complaints and fines. The third factor is cost: Sonelgaz industrial tariffs are low by North African standards, and the energy premium of diesel at the Algerian pump makes the comparison sharper than it first appears.</p>

<h2>TZ5E Specifications for Algerian Sites</h2>
<table style="width:100%;border-collapse:collapse;margin:20px 0;" border="1" cellpadding="8">
<tr style="background:#006341;color:#fff;"><th style="padding:8px;text-align:left;">Parameter</th><th style="padding:8px;text-align:left;">TZ5E 6x4 Electric Dump Truck</th></tr>
<tr><td style="padding:8px;">GVW / payload</td><td style="padding:8px;">28-31 t / ~18-20 t (12-16 m&sup3; body)</td></tr>
<tr><td style="padding:8px;">Battery</td><td style="padding:8px;">400 kWh CATL LFP, liquid-cooled</td></tr>
<tr><td style="padding:8px;">Motor</td><td style="padding:8px;">LvKong 360-410 kW peak / 2,400-2,800 Nm</td></tr>
<tr><td style="padding:8px;">Real-world range (loaded, urban)</td><td style="padding:8px;">260-320 km</td></tr>
<tr><td style="padding:8px;">DC charge 20-80%</td><td style="padding:8px;">~55 min at 240 kW dual-gun</td></tr>
<tr><td style="padding:8px;">Battery swap</td><td style="padding:8px;">5-6 min (heavy swap variant)</td></tr>
<tr><td style="padding:8px;">Gradeability</td><td style="padding:8px;">&ge;30% at full load</td></tr>
<tr><td style="padding:8px;">Battery warranty</td><td style="padding:8px;">8 years / 4,500 cycles to 70% SOH</td></tr>
<tr><td style="padding:8px;">FOB price band</td><td style="padding:8px;">US$95,000-120,000</td></tr>
</table>
<p>The 2,800 Nm of torque changes quarry behaviour: loaded tippers pull away from the Mitidja access ramps with full power from zero rpm, where a diesel drops to low-range crawling. Gradeability covers the climbs into the Bab Ezzouar and Kouba site approaches at full load. The LFP pack tolerates Algiers&rsquo; hot, dusty summer without NMC degradation, and the liquid-cooled system holds cell temperature through back-to-back site cycles. Contractors running the swap variant keep a spare pack per three trucks and never lose a tipper to charging downtime.</p>

<h2>The TCO at Sonelgaz Tariffs</h2>
<p>Algerian diesel retails around US$0.28-0.35 per litre at the commercial pump (heavily influenced by the subsidy framework). A 28 t tipper on Algiers aggregates duty burns 0.45-0.55 L/km &mdash; about US$0.15 per kilometre. The TZ5E consumes 1.3-1.6 kWh/km loaded; at Sonelgaz industrial tariffs of roughly US$0.07-0.09/kWh, that is US$0.10-0.14 per kilometre. On 200 km per day, 26 days a month, the monthly energy saving is about US$260 per truck &mdash; modest on energy alone because of the subsidised diesel &mdash; but maintenance tells the real story. No engine oil, no fuel filters, no DPF, and brake pads lasting 3-4x longer under regenerative braking on the site descents add US$4,000-6,000 per year. Combined, the annual saving reaches US$7,000-9,000, and against a US$30,000-45,000 purchase premium payback arrives in 40-60 months. For contractors, the stronger drivers are the night-shift permit and the zero-tailpipe compliance &mdash; benefits no diesel tipper can buy.</p>
<ul>
<li><strong>Energy cost per km:</strong> US$0.15 diesel vs US$0.12 electric &mdash; comparable, but maintenance swings it</li>
<li><strong>Night-work:</strong> near-silent operation meets Algiers noise limits for evening shifts</li>
<li><strong>Annual maintenance saving:</strong> US$4,000-6,000 per truck</li>
<li><strong>Compliance:</strong> zero NOx and particulates inside dense city sites</li>
</ul>

<h2>Charging on the Sonelgaz Grid</h2>
<p>Algiers construction yards have the medium-voltage capacity for fleet charging; a six-truck TZ5E fleet runs on one 240 kW dual-gun DC charger plus managed overnight AC &mdash; about 400-500 kVA, a standard industrial connection for Sonelgaz. We file the utility application on purchase-order day, because the connection lead time exceeds the 30-36 day vessel transit from China to Algiers port. The swap variant suits contractors above ten tippers or any two-shift operation: one swap station serves 15-20 trucks and eliminates charging downtime entirely. Solar canopies over the yard are economic at Algiers&rsquo; 5.0-5.5 peak sun hours, covering 35-50% of annual charging energy and providing covered staging for equipment.</p>
<p>Resilience is structural: the trucks&rsquo; own batteries are the buffer. A six-truck TZ5E fleet carries over 2,400 kWh of storage; a two-hour outage is absorbed by resequencing charge sessions. The sealed HV system has no air intake to clog with site dust and no fuel system to contaminate &mdash; a real advantage on dusty Mitidja haul roads where diesel engines ingest abrasive silica.</p>

<h2>Import and Algerian Fleet Strategy</h2>
<p>Algeria applies a developing framework for electric commercial vehicles, and Algiers port handles RoRo truck imports with 30-36 day sailings from China. We supply the full export pack: homologation dossier (French and Arabic documentation available), UN R100 battery certification, charger compliance papers, and the two-year parts kit. Contractors running national programmes should review our <a href="../markets/algeria.html">Algeria market page</a> &mdash; the TZ5E serves the capital&rsquo;s metro and housing sites with one parts stock and one training standard, and a pilot feeding a national rollout is the structure the large public-works groups are adopting. Support ships with the fleet: CATL module availability in 12-18 days, telematics-based remote diagnostics, and a maintenance calendar reduced to brake inspection and coolant check.</p>

<h2>The Algiers First-Mover Case</h2>
<p>The natural first adopters are the quarry-owning contractors with captive loading and city unloading points, the public-works groups on the metro and housing programmes, and the ready-mix producers running their own tipper fleets for aggregate inbound. Algiers&rsquo; noise limits are not relaxing, its air-quality rules are tightening, and its construction pipeline is long. The contractors that electrify their tipper fleets first buy a compliance advantage their diesel competitors cannot &mdash; and the maintenance saving funds part of the transition regardless of fuel subsidy.</p>
'''))

# ---------------------------------------------------------------- 7
ARTICLES.append(dict(
f='rabat-morocco-electric-municipal-fleet-kt1d',
t='Rabat Municipal Fleet: KT1D Electric Sweepers for Morocco&rsquo;s Administrative Capital',
d='Rabat street-sweeping and municipal fleets cut cost with the KT1D electric sweeper: 140-180 kWh CATL LFP, near-silent night shifts and lower energy cost per km than diesel. EV truck specs, TCO and tender guide.',
k='KT1D electric sweeper truck, EV truck Morocco, electric truck Rabat, municipal electric sweeper, Dongfeng electric truck, Rabat city fleet, electric street sweeper tender',
img='models/p01_00.jpg',
alt='Dongfeng KT1D electric sweeper truck in Rabat, Morocco, EV truck for municipal street cleaning',
net='gen',
body='''
<p>Rabat is Morocco&rsquo;s administrative capital and one of its cleanest, a status the commune protects with disciplined street-sweeping and municipal service fleets that work the wide boulevards of Agdal, the Hassan district and the waterfront at hours when the city is quiet. Those sweeper and service trucks run short, fixed, night-time loops &mdash; and they run them under municipal noise and emissions rules that a diesel fleet is increasingly struggling to meet. This article examines the <a href="../products/models/kt1d-electric-sweeper-truck.html">Dongfeng KT1D electric sweeper truck</a> as a Rabat municipal vehicle, with real numbers on energy, range, charging on the ONEE/Moroccan grid, and the tender path. For the commune and its contractors serving the <a href="../markets/morocco.html">Morocco market</a>, an EV truck sweeper is a compliance requirement as much as a cost decision, and the quieter streets the KT1D delivers are a direct quality-of-life gain residents associate with the commune&rsquo;s management.</p>
<p>Rabat&rsquo;s status as the administrative capital shapes the municipal case in ways that favour electric sweepers. The commune maintains a visible standard &mdash; clean boulevards, quiet nights, a green image for a city that hosts diplomacy and government &mdash; and a zero-tailpipe, near-silent sweeper is a visible asset rather than a back-office cost. Moroccan municipal tenders increasingly weight emissions, noise and lifecycle cost, so the KT1D scores on criteria a diesel sweeper cannot meet, and the lower energy and maintenance cost funds the higher upfront price across the contract. The city&rsquo;s wide, planned boulevards &mdash; the Agdal grid, the Hassan and Yaacoub El Mansour districts, the waterfront corniche &mdash; give sweepers short, fixed, predictable loops that charge overnight at the depot, and the commune&rsquo;s own workshops can be trained through a single centralized programme. The broom hydraulics running off the traction battery also remove the separate screaming engine that residents hear blocks away, which is the single biggest night-shift change. Several Moroccan communes already run solar canopies over depots, so adding sweeper charging to self-generated power is the cheapest increment, and the telematics portal gives fleet managers the audit-ready reports that modern municipal procurement demands. For Rabat, electrifying the sweeper fleet is therefore both a budget decision and a statement of the city&rsquo;s environmental standard that visiting diplomats and residents notice directly. The capital&rsquo;s cleanliness ranking is a point of civic pride, and the quiet electric sweeper protects it at 3 a.m. when diesel neighbours wake the streets.</p>

<h2>Why Municipal Sweepers Electrify First</h2>
<p>Municipal sweeping is the textbook EV truck duty cycle. Routes are fixed and short &mdash; a Rabat sweeper covers 40-90 km per night across the Agdal, Yaacoub El Mansour and Hassan loops. Schedules are night-time and predictable, which means charging windows are predictable and the trucks return to the same depot before dawn. And the work is audible: a diesel sweeper&rsquo;s broom hydraulics and engine note carry for blocks, while a near-silent electric sweeper meets the night-work noise limits that Moroccan cities enforce around residential districts. The second driver is procurement &mdash; Moroccan municipal tenders increasingly score on emissions and noise, so a zero-tailpipe sweeper is a compliance advantage, not a novelty.</p>

<h2>KT1D Specifications for Rabat Streets</h2>
<table style="width:100%;border-collapse:collapse;margin:20px 0;" border="1" cellpadding="8">
<tr style="background:#006341;color:#fff;"><th style="padding:8px;text-align:left;">Parameter</th><th style="padding:8px;text-align:left;">KT1D Electric Sweeper Truck</th></tr>
<tr><td style="padding:8px;">GVW / payload</td><td style="padding:8px;">10-12 t class / 4-5 t (water + hopper)</td></tr>
<tr><td style="padding:8px;">Battery</td><td style="padding:8px;">140-180 kWh CATL LFP, liquid-cooled</td></tr>
<tr><td style="padding:8px;">Motor</td><td style="padding:8px;">LvKong 150-190 kW peak / 1,100-1,400 Nm</td></tr>
<tr><td style="padding:8px;">Real-world range (sweeping duty)</td><td style="padding:8px;">200-260 km</td></tr>
<tr><td style="padding:8px;">DC charge 20-80%</td><td style="padding:8px;">~40 min at 120 kW</td></tr>
<tr><td style="padding:8px;">Sweep width / hopper</td><td style="padding:8px;">3.0-3.5 m / 5-6 m&sup3; with water tank</td></tr>
<tr><td style="padding:8px;">Noise (cabin/exterior)</td><td style="padding:8px;">~10 dB lower than diesel sweeper at curb</td></tr>
<tr><td style="padding:8px;">Battery warranty</td><td style="padding:8px;">8 years / 4,500 cycles to 70% SOH</td></tr>
<tr><td style="padding:8px;">FOB price band</td><td style="padding:8px;">US$72,000-88,000</td></tr>
</table>
<p>The 200-260 km range translates into a full night&rsquo;s work on a single charge for most Rabat loops, with the 140 kWh variant charging every second night and the 180 kWh variant covering two nights. The sweeper hydraulics run off the traction battery through an efficient electric pump, so there is no separate engine screaming at the broom &mdash; which is the single biggest night-shift change operators notice. The LFP pack tolerates Rabat&rsquo;s warm summers without NMC degradation, and the liquid-cooled system holds cell temperature through the stop-start sweeping cycle.</p>

<h2>The TCO for the Commune Budget</h2>
<p>Moroccan diesel retails around US$1.10-1.20 per litre at the municipal pump. A 10-12 t sweeper on Rabat duty burns 0.30-0.38 L/km &mdash; about US$0.38 per kilometre (and diesel sweepers idle heavily at the broom, inflating this). The KT1D consumes 0.7-0.9 kWh/km; at ONEE industrial tariffs of roughly US$0.12-0.15/kWh, that is US$0.10-0.13 per kilometre. On 2,500 km per month (nightly urban sweeping), the energy saving is about US$650 per truck per month, and maintenance &mdash; no sweeper-engine oil, no broom-drive clutch, no DPF &mdash; adds another US$150-200. Total: roughly US$9,500 per truck per year against a purchase premium of US$20,000-28,000, so payback lands at 25-35 months. The stronger drivers are the night-shift permit and the tender score &mdash; benefits no diesel sweeper can buy &mdash; plus the absence of exhaust heat and fumes around crews working residential streets at 3 a.m.</p>
<ul>
<li><strong>Energy cost per km:</strong> US$0.38 diesel vs US$0.12 electric &mdash; a 68% reduction</li>
<li><strong>Annual saving per truck:</strong> ~US$9,500 (energy + maintenance)</li>
<li><strong>Night-shift:</strong> ~10 dB quieter at the curb, meets Rabat noise limits</li>
<li><strong>Tender advantage:</strong> zero-tailpipe option scores on municipal emissions criteria</li>
</ul>

<h2>Charging at the Municipal Depot</h2>
<p>Rabat&rsquo;s municipal depots have the medium-voltage capacity for fleet charging; a six-to-ten truck KT1D fleet runs on one 120 kW DC charger for rotation top-ups plus overnight AC at each bay &mdash; about 250-350 kVA, a standard commercial connection. We file the utility application on purchase-order day, because the connection lead time exceeds the 30-36 day vessel transit from China to Casablanca port (the trucks then road-freight to Rabat). Solar canopies over the depot are economic at Rabat&rsquo;s 5.0-5.5 peak sun hours, covering 35-50% of annual charging energy and providing covered parking for the fleet. The trucks themselves buffer the grid: a ten-truck KT1D fleet carries over 1,500 kWh of storage, absorbing a two-hour outage with zero impact on the dawn dispatch.</p>

<h2>Tenders, Import and Moroccan Fleet Strategy</h2>
<p>Morocco applies favourable treatment to electric municipal vehicles under its industrial and environmental incentives, and Casablanca and Tangier ports handle RoRo truck imports with 30-36 day sailings from China. We supply the full tender pack: homologation dossier (French and Arabic documentation available), UN R100 battery certification, charger compliance papers, and the two-year parts kit. Communes running multi-city programmes should review our <a href="../markets/morocco.html">Morocco market page</a> &mdash; the KT1D serves Rabat, Casablanca and the coastal cities with one parts stock and one training standard, and a capital-city pilot feeding a national municipal rollout is the structure several communes are adopting. Support ships with the fleet: CATL module availability in 12-18 days, telematics-based remote diagnostics, and a maintenance calendar reduced to brake inspection and coolant check.</p>

<h2>The Rabat First-Mover Case</h2>
<p>The natural first adopters are the commune&rsquo;s own street-services fleet, the contracted sweeping operators on the Agdal and Hassan loops, and the municipal utilities whose service bodies suit the KT1D platform. Rabat&rsquo;s noise limits are not relaxing, its tender scoring rewards low emissions, and its budget pressures reward lower operating cost. The communes that electrify their sweeper fleets first buy a compliance and cost advantage their diesel competitors cannot match &mdash; and set the standard other Moroccan cities will follow.</p>
'''))

# ---------------------------------------------------------------- 8
ARTICLES.append(dict(
f='which-electric-truck-is-best-for-mining-operations',
t='Which Electric Truck Is Best for Mining Operations?',
d='Which electric truck is best for mining? Compare a 30 t 8x4 dump with 600 kWh CATL LFP and 5-6 min battery swap against 80 t rigid haulers and underground EVs, with mining TCO and selection criteria.',
k='best electric truck for mining, EV truck mining, electric mining dump truck, TZ3V electric dump truck, Dongfeng electric truck, battery swap mining truck, mining EV truck TCO',
img='models/p03_01.jpg',
alt='Dongfeng TZ3V 600 kWh electric dump truck at a mining site, EV truck for open-pit mining operations',
net='zxc',
body='''
<p>Quick answer: For most open-pit and quarry operations a 30-tonne-class 8x4 electric dump truck such as the Dongfeng TZ3V &mdash; with a 600 kWh CATL LFP battery, a 350-510 kW LvKong motor, 180-260 km real-world range and 5-6 minute battery swap &mdash; delivers the lowest cost per tonne and the fastest payback. Ultra-class 80-220 t rigid mining haulers need purpose-built trolley or catenary systems, and underground operations need smaller low-profile, intrinsically-safe EVs. Choose by payload, gradient and whether you swap or charge, and the sites that get this right first lock in the lowest cost per tonne in the basin for a decade.</p>
<p>The shift to electric haulage is no longer a pilot question at most mines &mdash; it is a sizing and infrastructure question. Sites that ran a single diesel hauler for years are now modelling fleets of 10-30 electric trucks on the same bench, because the per-tonne cost advantage compounds across the fleet and the battery-swap station that serves one truck serves twenty at modest additional cost. The decision framework we use with miners starts with three numbers: annual tonnage moved, average one-way haul distance, and bench gradient. Below roughly 1 km one-way and under 30 t payload, a surface electric dump truck like the TZ3V with depot charging is usually the whole answer. Between 1-5 km and 30-60 t, battery swap becomes economic because charging downtime starts to cost more than the swap station. Above 5 km or above 80 t payload, you are in rigid-hauler and trolley-assist territory where the business case depends on grid or captive generation at mine scale. Crucially, the energy source decides the payback: a mine charging EVs from its own solar and battery storage &mdash; now standard at remote sites &mdash; pays near-zero marginal energy cost, while a mine buying grid power at industrial rates still beats diesel but with a longer payback. Get those three numbers right and the truck class, the swap-versus-charge choice and the battery size all follow. The mines that move first also capture the availability gain &mdash; fewer breakdown hours than diesel haulers &mdash; which on a haul road is measured directly in tonnes moved, not just in maintenance savings. That is why we treat the EV truck decision as a fleet-design problem, not a vehicle purchase.</p>

<h2>Which Electric Truck Class Fits My Mine?</h2>
<p>Mining EV trucks divide into three clear classes, and picking the wrong one is the most expensive mistake a site can make. The 30 t class &mdash; the Dongfeng TZ3V 8x4 &mdash; covers quarries, small open pits, overburden and aggregate haulage on 1-5 km cycles. It carries a 600 kWh CATL LFP pack, runs 180-260 km per charge, and swaps packs in 5-6 minutes for continuous two-shift duty. The 80-220 t rigid class (CAT 797F / Komatsu 980E equivalents) is a different universe: these need 1.5-3.5 MWh packs, are usually paired with overhead trolley lines on the upgrade, and are only economic at million-tonne-per-year volumes. Underground mines need low-profile, narrow, flame-proof EVs &mdash; typically 15-40 t, with tight turning circles and methane-safe electrical systems &mdash; not surface trucks adapted downward. Match the class to your annual tonnage and bench height before anything else.</p>

<h2>How Do Battery Swap and Fast Charging Compare in Mining?</h2>
<p>The choice between swap and charge decides your infrastructure capital and your truck uptime. Fast charging a 600 kWh pack from 20-80% takes 35-60 minutes at 240-360 kW dual-gun &mdash; fine for single-shift quarries where the lunch break or blast window absorbs the dwell. Battery swap, at 5-6 minutes per pack, beats a diesel refuel and keeps the truck earning on two-shift and continuous operations; one swap station serves 15-20 trucks and holds 6-8 packs on managed charge. The trade-off is capital: a swap station costs more up front than a charger, but it eliminates charging downtime entirely and extends pack life by managing charge rate centrally. Our rule of thumb: charge below ten trucks or single shift, swap above ten trucks or two shifts. Both use the same CATL LFP chemistry with an 8-year / 4,500-cycle warranty to 70% SOH.</p>

<h2>What Payload and Gradient Can Mining EVs Handle?</h2>
<p>The TZ3V 8x4 carries 18-22 t payload in a 12-16 m&sup3; body and holds &ge;30% gradeability at full load &mdash; enough for the haul roads of most quarries and mid-size pits. The LvKong permanent-magnet motor delivers 2,400-2,800 Nm from zero rpm, so the truck pulls away on a loaded ramp without clutch slip, and regenerative braking recovers 18-28% of the descent energy back into the pack on every down-cycle. On a typical pit with a 60-120 m bench, that regeneration is the single largest factor in the EV truck&rsquo;s energy economy: the uphill draw is partly refunded by the downhill return, so round-trip energy cost per tonne-km is far lower than a naive range figure suggests. For ultra-class rigid haulers the gradient story is similar but the packs and trolley infrastructure scale with it.</p>

<h2>Are Electric Mining Trucks Reliable in Dust and Heat?</h2>
<p>Mine sites are the harshest environment a truck meets, and this is where the EV truck&rsquo;s simplicity pays. The TZ3V&rsquo;s HV system is sealed to IP67, the battery pack sits above the wading line, and there is no air intake, turbo or exhaust to ingest abrasive silica or overheat in 40&deg;C plus ambient. The LFP chemistry tolerates heat without the degradation penalties of NMC, and the liquid-cooled pack holds cell temperature through back-to-back haul cycles. Maintenance removes the diesel&rsquo;s weakest categories &mdash; no engine oil, no fuel-water separators, no turbo, no DPF &mdash; and brake linings last 3-4x longer under regenerative braking on the down-ramp. In practice, electric mining trucks show materially higher availability than the diesel haulers they replace, which on a haul road is revenue, not a specification footnote.</p>

<h2>What Is the Real TCO of a Mining EV Truck?</h2>
<p>Mining diesel haulers are fuel monsters: a 30 t class diesel dump burns 0.45-0.55 L/km, and at African or Australian mine-diesel prices of US$0.90-1.20/L that is US$0.45-0.65 per kilometre. The TZ3V consumes 1.3-1.6 kWh/km; at an isolated mine&rsquo;s own solar-plus-storage tariff of roughly US$0.08-0.12/kWh, that is US$0.11-0.19 per kilometre &mdash; a 70-75% energy reduction. On 200 km per day, 300 days a year, the annual energy saving is roughly US$20,000-28,000 per truck, and maintenance adds US$6,000-9,000 more from the eliminated engine and brake load. Against a US$40,000-60,000 purchase premium over a diesel hauler, payback arrives in 16-28 months. Mines with captive solar and battery storage &mdash; now standard at remote sites &mdash; push the payback below 18 months, because the EV truck charges from power the mine already generates for free.</p>
<ul>
<li><strong>Energy cost per km:</strong> US$0.55 diesel vs US$0.15 electric &mdash; a 72% reduction</li>
<li><strong>Annual saving per truck:</strong> US$26,000-37,000 (energy + maintenance)</li>
<li><strong>Payback:</strong> 16-28 months; under 18 with captive solar</li>
<li><strong>Availability:</strong> sealed drivetrain and regen braking lift uptime versus diesel haulers</li>
</ul>
<p>South African and regional miners building electric haul fleets should review our <a href="../markets/south-africa.html">South Africa market page</a> for corridor and import context, and the <a href="../products/models/tz3v-electric-dump-truck.html">Dongfeng TZ3V electric dump truck</a> product page for the full specification sheet. The verdict is consistent across every pit we have electrified: for the 30 t class, the battery-swap EV truck is both the cheaper truck to own and the one that keeps earning through the night shift.</p>
''',
faq=[
('Which electric truck is best for open-pit mining?',
 'A 30-tonne-class 8x4 electric dump truck such as the Dongfeng TZ3V is best for most open pits: its 600 kWh CATL LFP battery, 350-510 kW motor and 180-260 km range with 5-6 minute battery swap deliver the lowest cost per tonne and 16-28 month payback.'),
('How long does it take to charge a mining electric truck?',
 'A 600 kWh mining electric truck charges from 20-80% in 35-60 minutes on a 240-360 kW dual-gun DC charger, but battery-swap variants exchange packs in just 5-6 minutes, beating a diesel refuel for continuous two-shift haulage.'),
('Can electric mining trucks handle steep haul roads?',
 'Yes. The TZ3V holds &ge;30% gradeability at full 18-22 t payload and delivers 2,400-2,800 Nm from zero rpm, while regenerative braking recovers 18-28% of descent energy back into the 600 kWh pack on every down-cycle.'),
('Are electric mining trucks reliable in dust and heat?',
 'They are more reliable than diesel haulers: the HV system is sealed to IP67, the LFP pack tolerates 40&deg;C plus ambient via liquid cooling, and removing the engine, turbo and DPF lifts availability while brake life triples under regen braking.'),
('What is the real cost saving of an electric mining truck?',
 'An electric mining truck cuts energy cost per km from about US$0.55 (diesel) to US$0.15, saving US$26,000-37,000 per truck per year with maintenance, for a 16-28 month payback that drops below 18 months with captive solar.'),
]))

# __MORE__

for a in ARTICLES:
    html = build(a)
    path = os.path.join(ROOT, 'blog', a['f'] + '.html')
    with open(path, 'w', encoding='utf-8') as fh:
        fh.write(html)
    words = len(re.sub(r'<[^>]+>', ' ', a['body']).split())
    print('%-58s %5d words' % (a['f'], words))
print('done batch1:', len(ARTICLES))
