# -*- coding: utf-8 -*-
"""Run 15 batch 2: 8 articles (Middle East + Central Asia spotlights)."""
import re, os
import _gen_run14_b1 as G
G.DATE = "2026-10-08"
build = G.build

ROOT = os.path.dirname(os.path.abspath(__file__))
ARTICLES = []

# ---------------------------------------------------------------- 1
ARTICLES.append(dict(
f='neom-saudi-arabia-electric-construction-fleet',
t='NEOM Construction Logistics: Electric Dump Trucks for Saudi Arabia&rsquo;s Giga-Project',
d='NEOM&rsquo;s zero-emission site mandate makes the TZ3V 8x4 electric dump truck the logical choice for THE LINE and Oxagon earthworks. EV truck specs, TCO and FOB for Saudi giga-project fleets.',
k='TZ3V electric dump truck, EV truck Saudi Arabia, electric dump truck NEOM, THE LINE electric truck, Dongfeng electric construction truck, zero-emission construction fleet, electric tipper giga-project',
img='models/p03_00.jpg',
alt='Dongfeng TZ3V 8x4 electric dump truck on a NEOM giga-project earthworks site, EV truck for Saudi Arabia construction',
net='zxc',
body='''
<p>Saudi Arabia&rsquo;s northwest is the largest construction site on earth. NEOM &mdash; the US$500 billion-plus giga-project anchored by THE LINE linear city, the Oxagon floating industrial port and the Trojena mountain resort &mdash; is moving hundreds of millions of tonnes of earth, aggregate and fill across a desert corridor where summer ambient temperatures exceed 50&deg;C. In that environment, the project&rsquo;s own sustainability mandate is the decisive purchase driver: NEOM has committed to a zero-emission construction site, which rules out diesel tippers for the bulk of earthworks. This article examines how the <a href="../products/models/tz3v-electric-dump-truck.html">Dongfeng TZ3V 8x4 electric dump truck</a> fits that mandate with real operating numbers, and what the procurement and TCO picture looks like for fleets working the Saudi giga-projects. For contractors bidding PIF-backed civil works, an EV truck fleet is now a compliance requirement as much as a cost decision.</p>

<h2>Why the Giga-Projects Electrify First</h2>
<p>NEOM, the Red Sea Project, Qiddiya and Roshn are not ordinary developers. They are PIF (Public Investment Fund) vehicles with published decarbonization targets, and their main works contracts now carry embodied-carbon and on-site emissions clauses that directly affect contractor scoring. A diesel tipper on an earthworks shift emits roughly 0.55-0.65 kg of CO2 per litre burned; a civil-works fleet of 30-60 tippers therefore carries a measurable, contract-penalised emissions footprint. The TZ3V&rsquo;s electric drivetrain produces zero tailpipe emissions, and when charged from the giga-project&rsquo;s own solar-plus-storage microgrids &mdash; NEOM is building gigawatts of renewables &mdash; the well-to-wheel figure collapses toward zero. That is not a marketing point; it is a clause in the tender.</p>
<p>The second driver is operating economics, which we detail below. Saudi industrial electricity runs roughly US$0.05-0.08 per kWh for large off-taker and project-grid consumers, among the lowest in the world, while diesel retails at SAR 2.18 per litre (about US$0.58). The gap between grid energy and diesel energy per kilometre is wider in Saudi Arabia than almost any market we serve, which is why the electric tipper&rsquo;s payback is measured in months on a severe earthworks duty cycle.</p>

<h2>TZ3V Specifications for Giga-Project Earthworks</h2>
<table style="width:100%;border-collapse:collapse;margin:20px 0;" border="1" cellpadding="8">
<tr style="background:#006341;color:#fff;"><th style="padding:8px;text-align:left;">Parameter</th><th style="padding:8px;text-align:left;">TZ3V 8x4 Electric Dump Truck</th></tr>
<tr><td style="padding:8px;">Configuration / GVW</td><td style="padding:8px;">8x4 / 31-35 t class, ~20 t payload</td></tr>
<tr><td style="padding:8px;">Battery</td><td style="padding:8px;">600 kWh CATL LFP, liquid-cooled</td></tr>
<tr><td style="padding:8px;">Motor</td><td style="padding:8px;">LvKong dual permanent-magnet, 510 kW peak / 6,200 Nm combined</td></tr>
<tr><td style="padding:8px;">Real-world range (loaded earthworks)</td><td style="padding:8px;">220-300 km per charge</td></tr>
<tr><td style="padding:8px;">DC fast charge 20-80%</td><td style="padding:8px;">~55 min at 360 kW dual-gun</td></tr>
<tr><td style="padding:8px;">Hot-climate pack rating</td><td style="padding:8px;">Operational to +50&deg;C ambient with active thermal management</td></tr>
<tr><td style="padding:8px;">Gradeability</td><td style="padding:8px;">&ge;30% at full payload on site ramps</td></tr>
<tr><td style="padding:8px;">Battery warranty</td><td style="padding:8px;">8 years / 4,500 cycles to 70% SOH</td></tr>
<tr><td style="padding:8px;">FOB price band</td><td style="padding:8px;">US$105,000-135,000 by body and axle spec</td></tr>
</table>
<p>Two specification points matter specifically for NEOM. First, the 600 kWh pack is sized for the project&rsquo;s haul profile: borrow-pit to fill, or cut to THE LINE foundation works, typically runs 15-45 km one way, so a single charge covers a full shift of 6-12 loaded trips with a mid-shift opportunity charge absorbing the long days. Second, the hot-climate rating is non-negotiable. Gulf summer ambient hits 50&deg;C, and pack cell temperature would exceed that under load; the liquid-cooled LFP system holds cells in their safe window, and CATL&rsquo;s LFP chemistry tolerates high-temperature cycling far better than NMC, which is why the 4,500-cycle warranty stays intact even under Saudi summer duty.</p>

<h2>TCO on a Saudi Earthworks Duty Cycle</h2>
<p>Model a 250 km shift: a diesel 31 t tipper burns 0.50-0.60 L/km, so 125-150 L daily at US$0.58/L equals US$73-87 per day, roughly US$22,600-27,000 per year at 310 shifts. The TZ3V consumes 2.0-2.4 kWh/km loaded on site ramps; at US$0.07/kWh project-grid power, that is US$35-42 per day, about US$11,000-13,000 per year. The annual energy saving alone is US$11,000-14,000 per truck. Add maintenance &mdash; no engine oil, fuel filters, DPF, turbo or clutch, and brake pads lasting 3-4x longer under regenerative braking on site descents &mdash; for another US$5,000-7,000 per year. Against a purchase premium of US$40,000-55,000 over an equivalent diesel 8x4 tipper, payback arrives in 24-38 months. On a 40-truck fleet that is US$640,000-840,000 of recovered margin per year from year three onward, on top of the contract-compliance value of a zero-emission fleet.</p>
<ul>
<li><strong>Energy cost per km:</strong> diesel ~US$0.33 vs EV truck ~US$0.16 on a 50&deg;C site &mdash; a 52% reduction</li>
<li><strong>Payback:</strong> 24-38 months at Saudi diesel and project-grid prices</li>
<li><strong>Site noise:</strong> ~12 dB lower at the curb, enabling extended night-shift earthworks near residential and resort zones</li>
<li><strong>Downtime:</strong> sealed electric drivetrain eliminates dust-ingestion engine failures during the windy shamal season</li>
</ul>

<h2>Charging Infrastructure at the Site</h2>
<p>Giga-project sites are uniquely suited to depot and on-site charging because the developer controls the grid. NEOM and the Red Sea Project are building their own renewable generation and 380V/11kV distribution, so the practical model is a site charging yard with 2-4 dual-gun 360 kW DC chargers fed from the project microgrid, plus opportunity top-ups at the cut-and-fill staging areas. A 360 kW charger restores 20-80% of the 600 kWh pack in about 55 minutes &mdash; aligned to the mandatory rest and shift-handover windows. Because the project owns the power, the charging cost is the internal transfer rate, often below US$0.07/kWh, which is the single biggest reason Saudi earthworks electrification pencils out so fast.</p>
<p>For contractors bringing their own mobile charging, we specify containerised DC chargers that plug into the site&rsquo;s temporary power, so charging capacity moves with the works front. This is the standard pattern on large civil-works packages: the charger is a piece of plant, not fixed infrastructure, which keeps the capital mobile across THE LINE modules and Oxagon reclamation works.</p>

<h2>Procurement and PIF Contract Alignment</h2>
<p>Saudi giga-project procurement runs through prime contractors and their equipment-leasing arms, with local-content (Nitaqat and Vision 2030 localization) scoring increasingly weighted. We support contractors with the full export dossier &mdash; UN R100 battery safety certification, Gulf heat-rating test reports, Arabic-language operator manuals and the spare-parts schedule &mdash; and we structure shipments to Dammam or Jeddah for overland haul to the northwest. For fleet operators building a regional Saudi book of work, our <a href="../markets/saudi-arabia.html">Saudi Arabia market page</a> covers the wider pipeline beyond NEOM, including Riyadh mass-transit works, Qiddiya and the Jafurah upstream camps, where the same TZ3V platform and charging playbook apply.</p>
<p>Service support for mission-critical site fleets is structured in three tiers: a comprehensive first-line parts kit shipped with every truck (HV contactors, suspension and body components, brake parts), remote diagnostics through the fleet telematics portal with our regional engineering desk on WhatsApp, and CATL module stock positioned in the Gulf for 7-12 day delivery. The LvKong dual-motor drivetrain has roughly 40% of the moving parts of the diesel it replaces, which is the real site-availability story when a stopped tipper means a stopped earthworks chain.</p>

<h2>The Strategic Case for Contractors</h2>
<p>For Saudi giga-project contractors, the TZ3V is not a green virtue signal; it is a tender-competitive and financially superior asset. It meets the zero-emission site mandate that diesel cannot, it runs on the cheapest electricity in our global portfolio, it survives Gulf heat that degrades lesser packs, and it delivers a two-to-three-year payback on a severe duty cycle. The contractors who standardize their earthworks fleets on this EV truck platform now will write lower bids, win more PIF scoring points, and bank a cost advantage their diesel-equipped competitors cannot match on the same contract.</p>
'''))

# ---------------------------------------------------------------- 2
ARTICLES.append(dict(
f='sharjah-uae-electric-waste-collection-kt3e',
t='Sharjah Waste Management: KT3E Electric Garbage Trucks for the UAE&rsquo;s Cultural Capital',
d='Sharjah&rsquo;s Bee&rsquo;ah-led waste operators can cut collection cost and night noise with the KT3E electric garbage truck. EV truck specs, TCO and charging for UAE municipal fleets.',
k='KT3E electric garbage truck, EV truck UAE, electric truck Sharjah, electric refuse collection truck, Dongfeng electric waste truck, Beeah electric fleet, municipal EV truck UAE',
img='models/p02_00.jpg',
alt='Dongfeng KT3E electric garbage truck on a Sharjah municipal collection route, EV truck for UAE waste management',
net='gen',
body='''
<p>Sharjah is the cultural capital of the UAE and, through Bee&rsquo;ah (the Emirates&rsquo; award-winning environmental-services company), one of the most ambitious waste operators in the Gulf. The emirate collects municipal solid waste across dense residential blocks, industrial zones and the university city, and it does much of that collection on night and pre-dawn shifts to beat the 45-50&deg;C summer daytime heat. Those two facts &mdash; nocturnal collection and a sustainability-driven operator &mdash; make Sharjah a textbook market for the electric refuse truck. This article looks at how the <a href="../products/models/kt3e-electric-garbage-truck.html">Dongfeng KT3E electric garbage truck</a> fits Sharjah&rsquo;s collection rounds, with real numbers on energy, noise, charging and TCO for UAE municipal fleets.</p>

<h2>Why Refuse Collection Is the Easiest EV Truck Win</h2>
<p>Municipal waste collection has the most favourable duty cycle of any truck segment. Routes are fixed and short &mdash; a Sharjah collection round runs 60-120 km per shift across the Al Nahda, Al Qasimia, Al Majaz and Industrial Area 1-6 districts. Stops are frequent (every 20-60 metres in dense blocks), which means the truck is constantly decelerating &mdash; and regenerative braking recovers 20-30% of the round&rsquo;s energy on a stop-start route. Every truck returns to the same depot or transfer station nightly. And the work happens when residents sleep, which makes the diesel&rsquo;s noise and exhaust a genuine complaint surface that Bee&rsquo;ah and the municipality actively manage. An EV truck removes both.</p>
<p>The sustainability angle is structural, not optional. Sharjah&rsquo;s waste strategy targets high landfill diversion and low fleet emissions, and Bee&rsquo;ah has publicly run electric and hybrid collection pilots. A permanently electrified collection fleet turns a compliance narrative into an operational one: zero tailpipe emissions on every street, and a near-silent truck that the municipality can run deeper into residential night hours without noise escalation.</p>

<h2>KT3E Specifications for Sharjah Collection</h2>
<table style="width:100%;border-collapse:collapse;margin:20px 0;" border="1" cellpadding="8">
<tr style="background:#006341;color:#fff;"><th style="padding:8px;text-align:left;">Parameter</th><th style="padding:8px;text-align:left;">KT3E Electric Garbage Truck</th></tr>
<tr><td style="padding:8px;">GVW / payload</td><td style="padding:8px;">15-18 t class / 8-10 t compacted waste</td></tr>
<tr><td style="padding:8px;">Battery</td><td style="padding:8px;">140-180 kWh CATL LFP, liquid-cooled</td></tr>
<tr><td style="padding:8px;">Motor</td><td style="padding:8px;">LvKong 180-220 kW peak / 2,000 Nm</td></tr>
<tr><td style="padding:8px;">Real-world range (loaded collection)</td><td style="padding:8px;">160-220 km per shift</td></tr>
<tr><td style="padding:8px;">DC charge 20-80%</td><td style="padding:8px;">~40 min at 120-150 kW</td></tr>
<tr><td style="padding:8px;">Hot-climate rating</td><td style="padding:8px;">Operational to +50&deg;C ambient with active cooling</td></tr>
<tr><td style="padding:8px;">Body</td><td style="padding:8px;">Rear or side-loader compactor, 12-16 m&sup3;</td></tr>
<tr><td style="padding:8px;">FOB price band</td><td style="padding:8px;">US$85,000-110,000 with body</td></tr>
</table>
<p>The stop-start torque profile is what makes the KT3E feel like an upgrade rather than a compromise. A fully loaded compactor pulling away from a kerbside stop does so on full motor torque from zero rpm &mdash; no clutch, no rev flare, no rollback on the slight grades of Sharjah&rsquo;s flyovers. Drivers transitioning from diesel consistently cite the smooth, instant response at every one of the 200-400 daily stops as the biggest quality-of-work change, followed by the absence of cab heat and exhaust odour during summer collection.</p>

<h2>TCO for UAE Municipal Fleets</h2>
<p>UAE diesel retails at about AED 2.40 per litre (US$0.65). A 15-18 t diesel refuse truck on a stop-start Sharjah round burns 0.45-0.55 L/km &mdash; roughly US$0.30 per kilometre. The KT3E consumes 1.0-1.3 kWh/km including regeneration; at DEWA/SEWA industrial tariffs of roughly US$0.10-0.12/kWh (Sharjah is served by SEWA), that is US$0.11-0.15 per kilometre. On 100 km per shift, 26 shifts a month, the monthly energy saving is about US$450-500 per truck, roughly US$5,500-6,000 per year. Maintenance adds another US$3,000-4,000 annually: no engine oil, no DPF regen, no clutch, and brake pads lasting 3-4x longer under regeneration. Against a purchase premium of US$35,000-50,000 over a diesel compactor, payback lands at 38-55 months &mdash; longer than freight duty because collection kilometres are low, but the noise-complaint reduction, the emissions mandate compliance, and the 8-year battery warranty that outlasts the payback by years make the case on total cost of ownership rather than energy alone.</p>
<ul>
<li><strong>Energy cost per km:</strong> diesel ~US$0.30 vs EV truck ~US$0.13 &mdash; a 56% reduction</li>
<li><strong>Noise at the kerb:</strong> ~12-15 dB lower, unlocking deeper residential night collection</li>
<li><strong>Regeneration:</strong> 20-30% of round energy recovered on stop-start routes</li>
<li><strong>Operator comfort:</strong> no exhaust heat or diesel odour in the cab during 48&deg;C summer shifts</li>
</ul>

<h2>Charging the Collection Fleet</h2>
<p>Refuse depots are the simplest charging sites in any city because the fleet is captive overnight. A Sharjah collection fleet of 10-20 KT3Es needs 2-3 dual-gun 120 kW DC chargers at the depot, fed from a managed 600-900 kVA service that SEWA provisions for commercial depots in standard lead times. Because collection trucks sit idle for 8-12 hours between the late shift and the next, overnight AC top-up plus one rotation DC charger covers the fleet with margin; the trucks rarely need daytime charging. We file the utility application on order day, since charger lead time (10-14 weeks) typically exceeds the vessel transit from China to Jebel Ali (18-22 days).</p>
<p>Sharjah&rsquo;s solar resource (5.0+ peak sun hours) makes a depot canopy strongly economic for a fleet that charges at night but can self-generate by day &mdash; a 200-300 kWp array offsets 35-50% of annual charging energy and, with battery storage, can shift cheap midday solar into evening charge. Bee&rsquo;ah&rsquo;s own sustainability profile makes this a natural pairing, and several Gulf waste operators already run solar canopies over their depots.</p>

<h2>Procurement and Gulf Context</h2>
<p>UAE municipal procurement favours sustainability credentials and local-service capability. We supply the full export and compliance dossier &mdash; UN R100 battery certification, Gulf heat-rating reports, Arabic operator manuals and the spare-parts schedule &mdash; and we ship to Jebel Ali for overland delivery to Sharjah. For operators running fleets across the federation, our <a href="../markets/uae.html">UAE market page</a> covers the parallel Abu Dhabi and Dubai collection programmes where the same KT3E platform and charging playbook apply, and where platform standardisation across emirates halves parts inventory and technician training.</p>
<p>Service support ships with the fleet: a two-year fast-moving parts kit (compactor hydraulics, contactors, brake and body components), telematics-based remote diagnostics with our Gulf engineering desk on WhatsApp, and CATL module stock positioned regionally for 7-12 day delivery. The LvKong drivetrain removes the engine, clutch, turbo and aftertreatment service calendar that grounds diesel compactors during peak summer, which is exactly when Sharjah&rsquo;s collection demand peaks.</p>

<h2>The Case for Sharjah</h2>
<p>Sharjah&rsquo;s combination of a sustainability-led operator, nocturnal collection, dense fixed routes and Gulf heat that punishes diesel cab comfort makes the KT3E electric garbage truck a logical fleet standard rather than a pilot. The energy saving is real, the noise benefit is immediate and resident-visible, and the emissions compliance aligns with the emirate&rsquo;s published waste strategy. For Bee&rsquo;ah and the municipality, electrifying collection is the rare intervention that lowers cost, lowers complaints and strengthens the sustainability record at the same time.</p>

<h2>Staging the Sharjah Fleet Rollout</h2>
<p>A practical deployment for a Sharjah collection operator starts with a single depot and five to eight KT3Es on the densest residential rounds in Al Nahda, Al Qasimia and the university city, where night noise is the sharpest complaint and regeneration recovers the most energy. The depot charger and utility application go in on order day; the first trucks arrive to a live charger and a trained crew. As the maintenance saving and resident feedback accumulate, the fleet extends to the industrial-area and wholesale-market rounds, then to the deep-night shifts that the electric truck can now run without noise escalation. We model the body configuration per route &mdash; rear-loader for dense blocks, side-loader where kerbside access is tight &mdash; because the right body compounds the savings across every stop. The diesel fleet is retained for the heaviest bulk and long-haul transfer runs until charging extends to the transfer station, a staged plan that keeps capital aligned to demonstrated savings rather than a leap of faith.</p>
'''))

# ---------------------------------------------------------------- 3
ARTICLES.append(dict(
f='jubail-saudi-industrial-city-electric-cargo-truck',
t='Jubail Industrial City: KTH3 Electric Cargo Trucks for Saudi Petrochemical Logistics',
d='Jubail&rsquo;s petrochemical plants and SABIC supplier fleets can cut in-plant logistics cost with the KTH3 electric cargo truck. EV truck specs, TCO and charging for Saudi industry.',
k='KTH3 electric cargo truck, EV truck Saudi Arabia, electric truck Jubail, petrochemical logistics electric truck, Dongfeng electric cargo truck, SABIC supplier fleet, industrial EV truck',
img='models/p07_04.jpg',
alt='Dongfeng KTH3 electric cargo truck in Jubail Industrial City petrochemical logistics, EV truck for Saudi industry',
net='zhc',
body='''
<p>Jubail Industrial City on the Saudi Arabian Gulf coast is the largest petrochemical complex on earth &mdash; home to SABIC and a dense ecosystem of downstream plants, tank farms, pipe racks and port logístics that move feedstock, intermediates and packed product around the clock. That internal logistics flow runs today on diesel flatbeds, box trucks and stake vehicles shuttling between plants, warehouses and the Jubail Commercial Port. For the supplier fleets that serve the complex, the case for electrification is unusually strong: captive routes, captive yards, 24-hour duty, and some of the cheapest grid power in the world. This article examines the <a href="../products/models/kth3-electric-cargo-truck.html">Dongfeng KTH3 electric cargo truck</a> in Jubail&rsquo;s petrochemical logistics role, with real numbers on energy, TCO and charging.</p>

<h2>Why Plant Logistics Electrifies First</h2>
<p>Industrial in-plant and inter-plant freight shares a signature that makes it the lowest-risk EV truck entry point: fixed short routes (plant to warehouse 3-15 km, plant to port 10-25 km), shift-based predictable schedules, return nightly to the same secured, powered yard, and high daily utilisation across three shifts. Jubail&rsquo;s geography compresses this further &mdash; the entire industrial complex sits within a 30 km radius, and the port is minutes from the major plants. A KTH3 on this duty cycle covers 120-220 km daily inside its real-world range with margin. The commercial angle is decisive: petrochemical majors and their tier-one suppliers now report scope-3 logistics emissions per shipment, and a zero-emission supplier fleet is a commercial asset in that procurement scoring, not just a cost line.</p>
<p>Safety is a second, Gulf-specific driver. Petrochemical sites restrict ignition sources, and diesel exhaust and hot surfaces are managed hazards. An electric drivetrain has no combustion, no exhaust and no hot manifold &mdash; which simplifies the site permit for electric trucks in hazardous-area-adjacent logistics compared with diesel, a point every Jubail EHS manager understands.</p>

<h2>KTH3 Specifications for Petrochemical Duty</h2>
<table style="width:100%;border-collapse:collapse;margin:20px 0;" border="1" cellpadding="8">
<tr style="background:#006341;color:#fff;"><th style="padding:8px;text-align:left;">Parameter</th><th style="padding:8px;text-align:left;">KTH3 Electric Cargo Truck</th></tr>
<tr><td style="padding:8px;">GVW / payload</td><td style="padding:8px;">16-18 t class / 9-11 t payload</td></tr>
<tr><td style="padding:8px;">Battery</td><td style="padding:8px;">262 kWh CATL LFP, liquid-cooled</td></tr>
<tr><td style="padding:8px;">Motor</td><td style="padding:8px;">LvKong 260-300 kW peak / 2,000 Nm</td></tr>
<tr><td style="padding:8px;">Real-world range (loaded, plant duty)</td><td style="padding:8px;">200-260 km</td></tr>
<tr><td style="padding:8px;">DC charge 20-80%</td><td style="padding:8px;">~45 min at 240 kW</td></tr>
<tr><td style="padding:8px;">Hot-climate rating</td><td style="padding:8px;">Operational to +50&deg;C ambient with active thermal management</td></tr>
<tr><td style="padding:8px;">Gradeability</td><td style="padding:8px;">&ge;30% at full load</td></tr>
<tr><td style="padding:8px;">FOB price band</td><td style="padding:8px;">US$75,000-95,000</td></tr>
</table>
<p>Payload is the first question every fleet manager raises, and the straight answer is that the 9-11 t payload covers the packed-product, drum and intermediate freight that dominates Jubail&rsquo;s internal flows; dense liquid-bulk moves by pipeline rather than truck. The 262 kWh pack is deliberately sized to the duty cycle &mdash; over-batterying a 16-18 t truck only costs payload and capital it does not need. We model each supplier&rsquo;s route profile before quoting, because right-sizing the battery is the single most common error in first EV truck purchases.</p>

<h2>TCO at Saudi Industrial Power Prices</h2>
<p>Saudi industrial electricity for large off-takers runs roughly US$0.05-0.08 per kWh, while diesel retails at about US$0.58 per litre. A 16-18 t diesel cargo truck on Jubail plant duty burns 0.32-0.40 L/km &mdash; roughly US$0.20 per kilometre. The KTH3 consumes 0.9-1.1 kWh/km loaded; at US$0.07/kWh, about US$0.07 per kilometre. On 4,000 km per month (two-to-three-shift plant duty), the monthly energy saving is about US$520 per truck, roughly US$6,200 per year. Maintenance adds another US$3,500-4,500 annually &mdash; no engine oil, no fuel filters, no DPF, no clutch, and brake pads lasting 3-4x longer under regenerative braking in stop-go plant traffic. Against a purchase premium of US$30,000-40,000 over a diesel equivalent, payback arrives in 30-48 months. The CATL battery warranty &mdash; 8 years or 4,500 cycles &mdash; outlasts payback by years, and the scope-3 reporting value to SABIC-facing suppliers adds commercial upside the TCO model does not capture.</p>
<ul>
<li><strong>Energy cost per km:</strong> diesel ~US$0.20 vs EV truck ~US$0.07 &mdash; a 65% reduction</li>
<li><strong>Annual saving per truck:</strong> ~US$10,000 combined (energy + maintenance)</li>
<li><strong>Payback:</strong> 30-48 months at Saudi industrial tariffs</li>
<li><strong>Safety:</strong> no diesel exhaust or hot surfaces &mdash; easier hazardous-area site permits</li>
</ul>

<h2>Charging Inside the Complex</h2>
<p>Jubail&rsquo;s plants already run heavy electrical infrastructure, so depot and warehouse charging is a standard industrial connection. A supplier fleet of 10-20 KTH3s needs 2-3 dual-gun 240 kW DC chargers at the fleet yard, fed from a managed 800-1,200 kVA service that the complex&rsquo;s utility provisions routinely. Because much of the duty is shift-based with natural changeover windows, one rotation charger per 6-8 trucks plus managed overnight AC covers the fleet. We file the utility application on order day &mdash; charger lead time (10-14 weeks) exceeds the 18-22 day vessel transit to Jebel Ali and overland haul to the Eastern Province.</p>
<p>Load management is where first-time fleets overspend. Twenty trucks do not need twenty fast chargers; they need sessions sequenced so the site never exceeds contracted capacity. The KTH3 fleet portal schedules by departure time and required state of charge, and in practice a 20-truck fleet runs on a connection a third the size of the unmanaged peak &mdash; often US$100,000-200,000 of avoided substation work for the complex operator.</p>

<h2>Procurement and Saudi Industrial Context</h2>
<p>Saudi industrial procurement weights Vision 2030 localization and sustainability increasingly heavily. We supply the full export dossier &mdash; UN R100 battery certification, Gulf heat-rating test reports, Arabic operator manuals and the spare-parts schedule &mdash; and ship to Dammam or Jebel Ali for overland delivery to Jubail. For supplier fleets serving the wider Eastern Province, our <a href="../markets/saudi-arabia.html">Saudi Arabia market page</a> covers parallel opportunities at Yanbu, Ras Tanura and Riyadh&rsquo;s industrial valleys where the same KTH3 platform and charging playbook apply.</p>
<p>Service support ships with the fleet: a two-year fast-moving parts kit (contactors, sensors, brake and suspension components), telematics-based remote diagnostics with our Gulf engineering desk on WhatsApp, and CATL module stock positioned regionally for 7-12 day delivery. The LvKong drivetrain has roughly 40% of the moving parts of the diesel it replaces, which is the real availability story when a stopped supplier truck stalls a plant&rsquo;s outbound flow.</p>

<h2>The Case for Jubail Suppliers</h2>
<p>Jubail&rsquo;s supplier fleets operate inside the most favourable EV truck conditions in our global portfolio: captive routes, captive powered yards, 24-hour duty, the world&rsquo;s cheapest industrial power, and a customer base that prices logistics emissions. The KTH3 is not a compromise vehicle on this duty cycle; it is simply the cheaper, safer, lower-emission truck to own. The fleets that standardize first will write lower bids into SABIC and major-tenant supply contracts and bank a structural cost advantage their diesel-equipped competitors cannot match.</p>

<h2>Staging the Jubail Supplier Transition</h2>
<p>A sensible rollout for a tier-one supplier begins with the shortest, highest-utilisation loops &mdash; the plant-to-warehouse and warehouse-to-port shuttles that run two or three shifts and never leave the complex. Five to eight KTH3s on those routes build the depot-charging habit and the telematics confidence while delivering the full energy and maintenance saving from day one. The 240 kW charger and utility application are filed on order day, and the first trucks arrive to a commissioned charger. As savings accumulate, the fleet extends to the inter-plant runs and the bulk-feedstock movements, then to the hazardous-area-adjacent logistics where the no-ignition-source advantage earns the easiest site permits. The diesel fleet is retained for the heaviest and longest external hauls until charging reaches the outer supplier parks &mdash; a staged plan that keeps every electric truck on a duty cycle where the numbers are overwhelmingly positive, rather than forcing a single wholesale switch.</p>
'''))

# ---------------------------------------------------------------- 4
ARTICLES.append(dict(
f='shymkent-kazakhstan-electric-truck-distribution',
t='Shymkent Distribution Hub: KT5M Electric Box Trucks for Southern Kazakhstan',
d='Shymkent&rsquo;s FMCG distribution hub suits the KT5M electric box truck: 200-240 km range, battery thermal management for -20&deg;C winters. EV truck specs, TCO and import guide for Kazakhstan.',
k='KT5M electric box truck, EV truck Kazakhstan, electric truck Shymkent, electric cargo truck Central Asia, Dongfeng electric truck, FMCG distribution EV truck, cold-climate electric truck',
img='models/p05_00.jpg',
alt='Dongfeng KT5M electric box truck on a Shymkent FMCG distribution route, EV truck for southern Kazakhstan',
net='zhc',
body='''
<p>Shymkent, in southern Kazakhstan near the Uzbek border, is one of the country&rsquo;s three largest cities and a major distribution gateway for the densely populated south &mdash; feeding Turkestan, Kyzylorda and the agricultural belt, and bridging trade with Uzbekistan and the wider Central Asian corridor. Its freight is dominated by FMCG, food, textiles and construction materials moving on fixed urban and regional routes. That duty cycle, combined with Kazakhstan&rsquo;s industrial electricity prices well below Western European levels and a hard continental winter, makes the <a href="../products/models/kt5m-electric-cargo-truck.html">Dongfeng KT5M electric box truck</a> a serious candidate &mdash; provided cold-weather battery behaviour is handled correctly. This article works through the KT5M for Shymkent distribution, with real numbers and the thermal-management detail that cold climates demand.</p>

<h2>The Shymkent Duty Cycle</h2>
<p>A Shymkent distribution round is 80-160 km per day: supermarket and bazaar deliveries inside the city, regional runs to Turkestan (160 km) and Kyzylorda (310 km, a twice-weekly run), and cross-border FMCG flows toward Tashkent 140 km south. The urban and near-regional patterns sit inside the KT5M&rsquo;s 200-240 km real-world range with comfortable reserve; the occasional long Kyzylorda run needs a midpoint top-up or is left to diesel for now. Routes are fixed and predictable, the fleet returns to a single depot nightly, and utilisation is high &mdash; the textbook profile for a first EV truck deployment. The one variable the spreadsheet must respect is temperature, which swings from +40&deg;C summer to -20&deg;C winter.</p>

<h2>KT5M Specifications for Kazakh Service</h2>
<table style="width:100%;border-collapse:collapse;margin:20px 0;" border="1" cellpadding="8">
<tr style="background:#006341;color:#fff;"><th style="padding:8px;text-align:left;">Parameter</th><th style="padding:8px;text-align:left;">KT5M Electric Box Truck</th></tr>
<tr><td style="padding:8px;">GVW / payload</td><td style="padding:8px;">9-12 t class / 4.5-6 t payload</td></tr>
<tr><td style="padding:8px;">Battery</td><td style="padding:8px;">180-220 kWh CATL LFP, liquid-cooled with thermal management</td></tr>
<tr><td style="padding:8px;">Motor</td><td style="padding:8px;">LvKong 150-190 kW peak / 1,100-1,500 Nm</td></tr>
<tr><td style="padding:8px;">Real-world range (loaded, +20&deg;C)</td><td style="padding:8px;">200-240 km</td></tr>
<tr><td style="padding:8px;">Real-world range (-20&deg;C, heated)</td><td style="padding:8px;">150-190 km (pack pre-conditioning)</td></tr>
<tr><td style="padding:8px;">DC charge 20-80%</td><td style="padding:8px;">~40 min at 120 kW</td></tr>
<tr><td style="padding:8px;">Cold-weather system</td><td style="padding:8px;">Pack pre-heat + cabin heat-pump, grid-draw at depot</td></tr>
<tr><td style="padding:8px;">FOB price band</td><td style="padding:8px;">US$50,000-65,000</td></tr>
</table>
<p>Cold-weather range is the question every Kazakh operator asks, and the honest engineering answer is that LFP packs lose usable capacity in deep cold &mdash; but the loss is manageable with correct system design. The KT5M pre-conditions the pack while still plugged in at the depot, drawing grid power (not battery) to bring cells into their efficient window before departure, and a cabin heat-pump provides driver warmth without the resistive heater drain that ruins winter range. Net effect: a -20&deg;C Shymkent winter still delivers 150-190 km of usable range, enough for the urban and near-regional rounds, with the longest Kyzylorda runs scheduled in warmer months or left to diesel until charging extends north.</p>

<h2>TCO at Kazakh Energy Prices</h2>
<p>Kazakhstan industrial electricity runs roughly US$0.06-0.09 per kWh, among the lowest outside the Gulf, while diesel retails at about US$0.65-0.75 per litre. A 9-12 t diesel box truck on Shymkent duty burns 0.28-0.35 L/km &mdash; roughly US$0.23 per kilometre. The KT5M consumes 0.75-0.95 kWh/km; at US$0.08/kWh, about US$0.07 per kilometre. On 3,500 km per month, the monthly energy saving is about US$560 per truck, roughly US$6,700 per year. Maintenance adds US$2,500-3,500 annually &mdash; no oil, clutch, injectors or DPF, and brake pads lasting 2-3x longer under regenerative braking. Against a purchase premium of US$18,000-25,000, payback lands at 24-36 months. The CATL battery warranty &mdash; 8 years or 4,500 cycles &mdash; outlasts payback by years, and Kazakhstan&rsquo;s exceptionally cheap power makes the per-kilometre energy gap wider than in most markets.</p>
<ul>
<li><strong>Energy cost per km:</strong> diesel ~US$0.23 vs EV truck ~US$0.07 &mdash; a 70% reduction</li>
<li><strong>Annual saving per truck:</strong> ~US$9,200-10,000 combined</li>
<li><strong>Payback:</strong> 24-36 months at Kazakh energy prices</li>
<li><strong>Winter range:</strong> 150-190 km usable at -20&deg;C with depot pre-conditioning</li>
</ul>

<h2>Charging in Shymkent</h2>
<p>Shymkent&rsquo;s industrial and depot districts have the medium-voltage capacity for fleet charging; a 10-15 truck KT5M fleet needs 2-3 dual-gun 120 kW DC chargers plus managed overnight AC, a 400-600 kVA service class that the regional grid operator provisions for commercial loads. Because Kazakh winters are harsh, we specify the pre-conditioning connection as part of the depot design &mdash; the pack heater draws from the grid at the bay, so the battery leaves warm and full, eliminating the cold-soak range penalty at the start of each shift. Charger lead time (10-14 weeks) typically exceeds the vessel-plus-rail transit from China, so the utility application goes in on order day.</p>
<p>One regional note: the Shymkent-Tashkent corridor is the busiest in Central Asia, and distribution groups increasingly run fleets on both sides of the border. Electrifying the Shymkent base first, with charging, creates a template that extends south as Uzbek charging matures &mdash; and the same KT5M platform serves both markets with one parts stock.</p>

<h2>Import and Central Asia Context</h2>
<p>Kazakhstan applies reduced or zero excise to electric vehicles under its decarbonization measures, against standard duty on diesel trucks, and Shymkent is well served by the overland and rail routes from northwest China (Khorgos and Dostyk gateways) with transit of roughly 10-18 days &mdash; far shorter than sea freight. We supply the full export dossier including UN R100 battery certification, Russian/Kazakh-language manuals and the spare-parts schedule. For distributors building a Central Asian book, our <a href="../markets/kazakhstan.html">Kazakhstan market page</a> covers the Almaty and Astana corridors where the same platform and charging playbook apply, and where cross-border fleet standardization with Uzbekistan multiplies the savings.</p>
<p>Service support ships with the fleet: a two-year fast-moving parts kit, telematics-based remote diagnostics with our engineering desk on WhatsApp (with Russian-speaking support), and CATL module stock reachable across the corridor in 10-18 days. The LvKong drivetrain&rsquo;s sealed, low-part-count design is especially valuable in a market where winter downtime on a diesel&rsquo;s frozen aftertreatment is a recurring headache &mdash; the electric truck simply has no DPF or EGR to ice up.</p>

<h2>The First-Mover Logic for Shymkent</h2>
<p>Shymkent&rsquo;s FMCG and food distributors with captive urban and near-regional routes are the natural first adopters: their utilisation is high, their depots are powered, and their winter operations are exactly what the KT5M&rsquo;s thermal management is built to handle. Kazakhstan&rsquo;s cheap power makes the per-kilometre case among the strongest we model anywhere, and the corridor position means an early Shymkent fleet becomes the hub of a wider Central Asian electrification network. The operators who move in the next 12-18 months bank a structural cost advantage before electrification becomes the expected standard for regional distribution.</p>

<h2>Staging the Shymkent Fleet Rollout</h2>
<p>A practical deployment for a Shymkent distributor starts with five to eight KT5Ms on the fixed urban and Turkestan-corridor rounds, where the range sits well inside a single charge and the depot pre-conditioning handles the winter morning cold. The 120 kW charger and the bay-side pre-heat connection go in on order day; the first trucks arrive to a commissioned depot and a trained crew. As the energy and maintenance saving build through a full summer-to-winter cycle, the fleet extends to the Kyzylorda runs and the cross-border flows toward Tashkent, matched to the charging that the corridor itself is building. We size the battery per route &mdash; the 180 kWh pack for the urban rounds, the 220 kWh pack for the longer regional legs &mdash; because right-sizing is the difference between a truck that pays back in two years and one that costs payload it never needed. The diesel fleet covers the occasional long Kyzylorda run until a midpoint charger closes that gap, a staged plan that keeps capital tied to demonstrated savings.</p>
'''))

# ---------------------------------------------------------------- 5
ARTICLES.append(dict(
f='fergana-uzbekistan-agri-electric-cargo-truck',
t='Fergana Valley Agriculture: KT5L Electric Cargo Trucks for Uzbekistan&rsquo;s Produce Corridor',
d='The Fergana Valley&rsquo;s fruit and vegetable produce flows to Tashkent suit the KT5L electric cargo truck. EV truck range, seasonal peaks, TCO and import guide for Uzbekistan.',
k='KT5L electric cargo truck, EV truck Uzbekistan, electric truck Fergana, agricultural produce electric truck, Dongfeng electric cargo truck, Fergana Valley logistics, Central Asia EV truck',
img='models/p05_01.jpg',
alt='Dongfeng KT5L electric cargo truck carrying produce in the Fergana Valley, EV truck for Uzbekistan agriculture',
net='zhc',
body='''
<p>The Fergana Valley is Uzbekistan&rsquo;s agricultural heartland &mdash; the country&rsquo;s largest fruit, vegetable and cotton-producing region, ringed by the terminals of Kokand, Margilan and Fergana city, and feeding the national consumption centre of Tashkent 300 km northwest. Every harvest season, millions of tonnes of perishable produce move from orchard, field and greenhouse to the capital&rsquo;s wholesale markets and onward to export corridors toward Kazakhstan and Russia. That flow runs today on diesel box and curtainside trucks, often on punishing seasonal peaks. This article examines the <a href="../products/models/kt5l-electric-cargo-truck.html">Dongfeng KT5L electric cargo truck</a> in the Fergana produce corridor, with real numbers on range, seasonal duty, TCO and import logistics for Uzbek agri-logistics.</p>

<h2>Why Produce Logistics Fits the EV Truck</h2>
<p>Agricultural produce freight has properties that make it an excellent first EV truck application. Routes are fixed and seasonal: Fergana city to Tashkent is 300 km (a long single charge, but the valley&rsquo;s inner flows &mdash; Kokand to Margilan, Andijan to Fergana, farm to packhouse &mdash; run 20-120 km daily and sit comfortably inside the KT5L&rsquo;s range). The work is shift-based and predictable outside the peak, and produce consolidates at packhouses and wholesale terminals that are natural charging sites. Critically, produce is time- and temperature-sensitive, and the electric truck&rsquo;s smooth, vibration-free drivetrain and optional electric-refrigeration draw (no diesel reefer unit) protect fragile fruit better than a rattling diesel box. The diesel reefer unit alone burns 1.5-3 L/hour idling at market &mdash; an expense the electric alternative removes.</p>

<h2>KT5L Specifications for the Valley</h2>
<table style="width:100%;border-collapse:collapse;margin:20px 0;" border="1" cellpadding="8">
<tr style="background:#006341;color:#fff;"><th style="padding:8px;text-align:left;">Parameter</th><th style="padding:8px;text-align:left;">KT5L Electric Cargo Truck</th></tr>
<tr><td style="padding:8px;">GVW / payload</td><td style="padding:8px;">6-7.5 t class / 2.5-3.5 t payload</td></tr>
<tr><td style="padding:8px;">Battery</td><td style="padding:8px;">130-160 kWh CATL LFP, liquid-cooled</td></tr>
<tr><td style="padding:8px;">Motor</td><td style="padding:8px;">LvKong 110-140 kW peak / 900-1,100 Nm</td></tr>
<tr><td style="padding:8px;">Real-world range (loaded, valley duty)</td><td style="padding:8px;">190-230 km</td></tr>
<tr><td style="padding:8px;">DC charge 20-80%</td><td style="padding:8px;">~35 min at 90-120 kW</td></tr>
<tr><td style="padding:8px;">Body options</td><td style="padding:8px;">18-24 m&sup3; curtainside, box or electric reefer</td></tr>
<tr><td style="padding:8px;">Gradeability</td><td style="padding:8px;">&ge;25% &mdash; handles valley approach roads loaded</td></tr>
<tr><td style="padding:8px;">FOB price band</td><td style="padding:8px;">US$44,000-56,000</td></tr>
</table>
<p>The inner-valley range is the practical story: Kokand-to-Fergana (60 km), Andijan-to-Margilan (25 km), farm-to-packhouse (10-40 km) all sit inside a single charge with large reserve, so the KT5L charges nightly at the packhouse or terminal where the produce already consolidates. For the 300 km Tashkent run, the truck handles the valley-side collection and the inbound empty/partial leg; the long-haul leg is best paired with a midpoint charger under development, or run by the operator&rsquo;s diesel fleet until charging extends &mdash; a staged migration we model per operator rather than an all-or-nothing switch.</p>

<h2>TCO at Uzbek Energy Prices</h2>
<p>Uzbekistan industrial electricity runs roughly US$0.07-0.10 per kWh, while diesel retails at about US$0.70-0.80 per litre. A 6-7.5 t diesel box truck on valley produce duty burns 0.24-0.30 L/km &mdash; roughly US$0.21 per kilometre. The KT5L consumes 0.60-0.75 kWh/km; at US$0.09/kWh, about US$0.06-0.07 per kilometre. On 3,000 km per month (high in harvest season, lower off-season), the monthly energy saving is about US$420 per truck, roughly US$5,000 per year. Maintenance adds US$2,000-2,500 annually &mdash; no oil, clutch, injectors or DPF, and brake pads lasting 2-3x longer. Against a purchase premium of US$15,000-20,000, payback lands at 28-40 months. The CATL battery warranty &mdash; 8 years or 4,500 cycles &mdash; outlasts payback by years; for the electric-reefer variant, the diesel reefer fuel saving (1.5-3 L/h at market) adds another US$1,500-3,000 per season, strengthening the case for temperature-controlled produce.</p>
<ul>
<li><strong>Energy cost per km:</strong> diesel ~US$0.21 vs EV truck ~US$0.06 &mdash; a 71% reduction</li>
<li><strong>Annual saving per truck:</strong> ~US$7,000-8,000 combined (more with electric reefer)</li>
<li><strong>Payback:</strong> 28-40 months at Uzbek energy prices</li>
<li><strong>Produce care:</strong> smooth drivetrain + electric reefer protects fragile fruit, cuts spoilage</li>
</ul>

<h2>Charging at Packhouses and Terminals</h2>
<p>The Fergana Valley&rsquo;s packhouses, cold stores and wholesale terminals are the natural charging anchor: produce already consolidates there, they have three-phase power, and trucks sit during loading and overnight. A regional operator with 10-15 KT5Ls needs 2-3 dual-gun 90-120 kW DC chargers spread across the main packhouse sites, plus overnight AC at each bay, a 300-500 kVA aggregate service class the local grid provisions for agri-processing loads. We file the utility application on order day; charger lead time (10-14 weeks) exceeds the overland transit from China via the Kyrgyz or Kazakh gateways (12-20 days). Seasonal peak planning matters: harvest surges double daily kilometres, so we size chargers for peak-month throughput, not the off-season average.</p>
<p>Solar is a strong fit for valley packhouses: Fergana receives 4.5-5.0 peak sun hours, and a 100-200 kWp canopy over the packhouse yard offsets 35-50% of charging energy while shading produce during loading. Several Uzbek agri-processors already run solar for cold storage; adding truck charging to that generation is incremental and hedges the tariff entirely.</p>

<h2>Import and Regional Export Context</h2>
<p>Uzbekistan grants customs and tax preferences to electric vehicles under its green-economy measures, against standard duty on diesel trucks, and the Fergana Valley is served by overland routes from China via the Kyrgyz border (Osh-Kashgar corridor) and the Kazakh gateway, with transit of roughly 12-20 days. We supply the full export dossier including UN R100 battery certification, Russian/Uzbek-language manuals and the spare-parts schedule. For operators serving the national corridor, our <a href="../markets/uzbekistan.html">Uzbekistan market page</a> covers the Tashkent, Samarkand and Bukhara logistics networks where the same KT5L platform and charging playbook apply, and where the produce export chain toward Kazakhstan and Russia creates a natural cross-border electrification roadmap.</p>
<p>Service support ships with the fleet: a two-year fast-moving parts kit, telematics-based remote diagnostics with our engineering desk (Russian-speaking support available), and CATL module stock reachable across Central Asia in 10-18 days. The LvKong drivetrain&rsquo;s sealed, low-part-count design is valuable in an agricultural environment where dust and harvest-season duty cycles are hard on diesel aftertreatment &mdash; the electric truck has no DPF to clog with field dust.</p>

<h2>Who Moves First in the Valley</h2>
<p>The strongest first adopters are the large packhouses and wholesale-terminal operators with captive collection routes and on-site power, the export-oriented fruit groups running temperature-controlled produce toward Tashkent and beyond, and the cooperative fleets that consolidate smallholder harvest. Uzbekistan&rsquo;s low power price and the valley&rsquo;s fixed, consolidating freight make the KT5L a lower-cost truck to own on its duty cycle; the electric-reefer option turns a major diesel expense into a grid charge. The operators who electrify their valley flows first will protect more of each harvest&rsquo;s margin and build the charging backbone that the longer Tashkent export run will plug into as it matures.</p>

<h2>Staging the Fergana Fleet Transition</h2>
<p>A practical rollout for a valley packhouse operator starts with five to eight KT5Ls on the inner-valley collection loops, where range is never a constraint and charging sits at the packhouse. As the depot-charging habit and telematics confidence build, the fleet extends to the Andijan and Kokand distribution runs, then pilots the electric-reefer variant on high-value fruit bound for Tashkent&rsquo;s wholesale markets. The diesel fleet is retained for the 300 km capital run until a midpoint charger at a waypoint terminal closes the gap &mdash; typically a 90-120 kW unit at a roadside consolidation point that also serves the export corridor toward Kazakhstan. We model this staged plan per operator rather than proposing an abrupt switch, because produce margins are thin and seasonal cashflow matters; the electric truck must pay for itself inside the harvest cycles that fund the business, not on a five-year horizon. The numbers above show it does, on the inner-valley duty that dominates daily kilometres, and the electric-reefer option converts a major diesel expense into a grid charge.</p>
'''))

# ---------------------------------------------------------------- 6
ARTICLES.append(dict(
f='sulaymaniyah-iraq-electric-dump-truck-reconstruction',
t='Sulaymaniyah Reconstruction: TZ3Z Electric Dump Trucks for Northern Iraq',
d='Sulaymaniyah&rsquo;s Kurdistan-region reconstruction and mountain quarry duty suit the TZ3Z electric dump truck. EV truck specs, TCO and FOB for Iraq rebuild fleets.',
k='TZ3Z electric dump truck, EV truck Iraq, electric truck Sulaymaniyah, electric dump truck reconstruction, Dongfeng electric tipper, Kurdistan construction truck, electric truck Iraq',
img='models/p03_05.jpg',
alt='Dongfeng TZ3Z electric dump truck on a Sulaymaniyah reconstruction site, EV truck for northern Iraq',
net='zxc',
body='''
<p>Sulaymaniyah, in the Kurdistan Region of Iraq, is rebuilding. Decades of conflict, displacement and under-investment have left a backlog of housing, road and public-works projects, and the city&rsquo;s surrounding hills hold the limestone and aggregate quarries that supply them. Reconstruction freight is the classic tipper duty cycle &mdash; short, repetitive haul from quarry to site &mdash; and it runs today on ageing diesel 6x4 dump trucks burning expensive, imported diesel. This article examines the <a href="../products/models/tz3z-electric-dump-truck.html">Dongfeng TZ3Z electric dump truck</a> in Sulaymaniyah&rsquo;s reconstruction and mountain-quarry role, with real numbers on energy, TCO, FOB and the terrain considerations that matter in Iraqi Kurdistan.</p>

<h2>Why Reconstruction Haulage Electrifies</h2>
<p>Reconstruction and housing-site logistics share the duty cycle that makes electric tippers compelling: fixed short routes. Sulaymaniyah&rsquo;s quarries &mdash; the limestone operations in the Bazian and Tasluja hills west of the city, and aggregate sources toward Halabja &mdash; sit 10-40 km from the urban construction fronts. A typical tipper shift is 8-12 loaded trips of 20-80 km round trip, totaling 180-260 km per day, inside the TZ3Z&rsquo;s real-world range. The second factor is fuel cost: Iraq imports the bulk of its refined products, and Kurdistan diesel retails at roughly US$0.50-0.65 per litre, while grid power &mdash; where available &mdash; runs US$0.05-0.10 per kWh at industrial rates. The per-kilometre gap is wide enough that the electric tipper pays back quickly on a severe haul cycle.</p>
<p>The terrain is the variable that shapes the spec. Sulaymaniyah sits in a mountain basin; the quarry access ramps are steep, and the haul includes sustained grades that force diesel tippers into low-range crawling. The TZ3Z&rsquo;s instant motor torque and 30% gradeability handle those ramps at speed, and regenerative braking recovers energy on the loaded descent back to the city &mdash; a descent a diesel truck converts into brake wear.</p>

<h2>TZ3Z Specifications for Iraqi Kurdistan</h2>
<table style="width:100%;border-collapse:collapse;margin:20px 0;" border="1" cellpadding="8">
<tr style="background:#006341;color:#fff;"><th style="padding:8px;text-align:left;">Parameter</th><th style="padding:8px;text-align:left;">TZ3Z 6x4 Electric Dump Truck</th></tr>
<tr><td style="padding:8px;">Configuration / GVW</td><td style="padding:8px;">6x4 / 25 t class, ~15 t payload (12 m&sup3; body)</td></tr>
<tr><td style="padding:8px;">Battery</td><td style="padding:8px;">350 kWh CATL LFP, liquid-cooled</td></tr>
<tr><td style="padding:8px;">Motor</td><td style="padding:8px;">LvKong permanent-magnet, 360 kW peak / 2,400 Nm</td></tr>
<tr><td style="padding:8px;">Real-world range (loaded, quarry duty)</td><td style="padding:8px;">220-260 km per charge</td></tr>
<tr><td style="padding:8px;">DC fast charge 20-80%</td><td style="padding:8px;">~50 min at 240 kW dual-gun</td></tr>
<tr><td style="padding:8px;">Gradeability</td><td style="padding:8px;">&ge;30% at full payload on hill ramps</td></tr>
<tr><td style="padding:8px;">Battery warranty</td><td style="padding:8px;">8 years / 4,500 cycles to 70% SOH</td></tr>
<tr><td style="padding:8px;">FOB price band</td><td style="padding:8px;">US$78,000-92,000 by body spec</td></tr>
</table>
<p>Two specification points matter specifically for Sulaymaniyah. First, the hill grades: the Bazian and Tasluja quarry ramps include sustained 12-18% sections where a loaded diesel tipper drops to 15-20 km/h in low gear; the TZ3Z holds 30-40 km/h on the same ramp on motor torque alone, then regenerates 15-22% of the climb energy on the descent. Second, dust and heat: the LFP pack is liquid-cooled and sealed to IP67, with no air intake to ingest the fine limestone dust of the quarries &mdash; a recurring failure mode for diesel engines in this environment. The sealed drivetrain is the real reliability story in a region where a stopped tipper is a stopped housing project.</p>

<h2>TCO on a Reconstruction Haul Cycle</h2>
<p>Model a 220 km shift: a diesel 25 t tipper burns 0.45-0.55 L/km, so 100-120 L daily at US$0.58/L equals US$58-70 per day, roughly US$17,900-21,600 per year at 310 shifts. The TZ3Z consumes 1.3-1.5 kWh/km loaded on quarry ramps; at US$0.08/kWh industrial power, that is US$26-33 per day, about US$8,000-10,000 per year. The annual energy saving is US$9,900-11,600 per truck. Add maintenance &mdash; no engine oil, fuel filters, DPF, turbo or clutch, and brake pads lasting 3-4x longer on regen descents &mdash; for another US$4,000-5,500 per year. Against a purchase premium of US$25,000-35,000 over an equivalent diesel 6x4 tipper, payback arrives in 24-38 months. On a 20-truck reconstruction fleet that is US$280,000-340,000 of recovered margin per year from year three onward, on top of the noise and emissions benefits that matter in residential rebuild zones.</p>
<ul>
<li><strong>Energy cost per km:</strong> diesel ~US$0.29 vs EV truck ~US$0.11 &mdash; a 62% reduction</li>
<li><strong>Payback:</strong> 24-38 months at Kurdistan fuel and power prices</li>
<li><strong>Brake life:</strong> 3-4x longer &mdash; loaded mountain descents no longer consume linings</li>
<li><strong>Downtime:</strong> sealed drivetrain eliminates dust-ingestion engine failures</li>
</ul>

<h2>Charging at Quarry and Site</h2>
<p>Sulaymaniyah&rsquo;s reconstruction fleets operate from yards and quarry weighbridges that can host depot charging. The practical model is a 240 kW dual-gun DC charger at the quarry or main yard, fed from an industrial service, plus an opportunity top-up during the midday break. A 240 kW unit restores 20-80% of the 350 kWh pack in about 50 minutes &mdash; aligned to the crew rest window. Because grid reliability in the region is variable, we specify the charger with wide input tolerance and, for sites with unstable supply, pair it with a modest battery-backed solar canopy: Sulaymaniyah receives 4.5-5.0 peak sun hours, and a 150-250 kWp array offsets 40-55% of annual charging energy while providing covered staging. The trucks themselves are a buffer &mdash; ten TZ3Zs carry 3,500 kWh of storage, absorbing short outages with zero operational impact.</p>

<h2>Import and Regional Context</h2>
<p>Iraqi Kurdistan applies preferential treatment to electric vehicles under its reconstruction-incentive framework, against standard duty on diesel trucks, and Sulaymaniyah is served by overland routes from Turkey (the Habur/Ibrahim Khalil crossing) and from the Gulf via Umm Qasr and overland, with transit of roughly 7-14 days by road from the Turkish border. We supply the full export dossier including UN R100 battery certification, Arabic and Kurdish-language manuals and the spare-parts schedule. For operators serving the wider country, our <a href="../markets/iraq.html">Iraq market page</a> covers the Baghdad and Basra corridors where the same TZ3Z platform and charging playbook apply as national reconstruction scales.</p>
<p>Service support ships with the fleet: a two-year fast-moving parts kit (contactors, brake and suspension components, body parts), telematics-based remote diagnostics with our engineering desk on WhatsApp, and CATL module stock reachable across the region in 10-18 days. The LvKong drivetrain&rsquo;s roughly 40% lower moving-part count than the diesel it replaces is the availability story that reconstruction contractors value most &mdash; every day a tipper is in a workshop is a day a housing block is not built.</p>

<h2>The Case for Sulaymaniyah Contractors</h2>
<p>For Sulaymaniyah&rsquo;s reconstruction and quarry contractors, the TZ3Z is financially and operationally the stronger truck on its duty cycle: it pays back inside three years on severe haul work, it climbs the mountain quarry ramps faster than the diesel it replaces, it survives limestone dust that destroys diesel engines, and it runs near-silently in residential rebuild zones. The contractors who standardize their tipper fleets on this EV truck platform now will bank a cost advantage their diesel-equipped competitors cannot match on the same reconstruction contracts &mdash; and position themselves for the larger national rebuild pipeline as it scales.</p>

<h2>Staging the Sulaymaniyah Rollout</h2>
<p>A practical rollout for a Kurdistan contractor begins with five to eight TZ3Zs on the shortest quarry-to-site loops in the Bazian and Tasluja hills, where range covers a full shift and the quarry weighbridge hosts the first 240 kW charger. The utility application and charger order go in on order day, and the first trucks arrive to a commissioned depot. As the energy and brake-life savings accumulate through a construction season, the fleet extends to the longer Halabja and regional housing-site hauls, matched to chargers added at those sites. We size the battery and body per duty &mdash; the 350 kWh pack for the steep, long ramps, a 12 m&sup3; body for the dense limestone &mdash; because over- or under-specifying the truck is the most common way first fleets leave savings on the table. The diesel tippers are retained for the most remote mountain sites until charging reaches them, a staged plan that keeps every electric truck on a duty cycle where the arithmetic is overwhelmingly positive.</p>
'''))

# ---------------------------------------------------------------- 7
ARTICLES.append(dict(
f='aqaba-jordan-port-electric-tractor',
t='Aqaba Port: TE46 Electric Tractors for Jordan&rsquo;s Only Seaport',
d='Aqaba&rsquo;s container terminal shuttle suits the TE46 electric tractor: 8-10 hour shift range, swap option. EV truck economics and SEZ incentives for Jordan&rsquo;s port.',
k='TE46 electric tractor, EV truck Jordan, electric truck Aqaba, electric terminal tractor, Dongfeng electric port tractor, Aqaba port EV truck, container drayage electric truck',
img='models/p11_00.jpg',
alt='Dongfeng TE46 electric tractor shuttling containers at Aqaba port, EV truck for Jordan seaport',
net='qyc',
body='''
<p>Aqaba is Jordan&rsquo;s only seaport and the sole maritime gateway for a country that is otherwise landlocked by geography and trade policy. Its container terminal, bulk handling and Aqaba Special Economic Zone (SEZ) logistics parks move the entirety of Jordan&rsquo;s import and export freight, and that movement runs on terminal tractors shuttling containers between quay, yard and gate. It is a severe, repetitive, return-to-base duty cycle that is, worldwide, the single best-understood electric truck application. This article examines the <a href="../products/models/te46-electric-tractor.html">Dongfeng TE46 electric tractor</a> in Aqaba port service &mdash; shift endurance, economics at Jordanian energy prices, SEZ incentives and the swap option that eliminates charging downtime.</p>

<h2>The Drayage Duty Cycle, Measured</h2>
<p>Port terminal tractors are transparent because telematics makes every metre measurable. An Aqaba tractor works 10-14 hours daily, covers 120-200 km, spends 30-40% of engine-hours idling in terminal queues and gate holds, and never travels more than 15 km from its depot. The idling figure is where diesel economics collapse: a 12 L diesel tractor engine burns 3-4 litres per hour producing nothing in a queue. The TE46&rsquo;s electric drivetrain consumes essentially zero at standstill &mdash; only the cab A/C draws, at about 1.5 kW. Across a shift, queue time alone accounts for 25-35% of the diesel truck&rsquo;s fuel bill and roughly 2% of the EV truck&rsquo;s energy bill. Aqaba&rsquo;s terminal gates and vessel peaks create exactly this queue pattern, which is why the TE46 is purpose-built for it.</p>
<p>The TE46&rsquo;s 282-350 kWh CATL LFP battery delivers 8-10 hours of mixed drayage duty per charge. Two strategies fit Aqaba: depot DC fast charging (a 240 kW unit restores 20-80% in about 45 minutes, matched to the lunch shift-change), or battery swap for two-shift operations &mdash; the swap variant exchanges packs in 5-6 minutes, faster than a diesel refuel, from a compact station that fits in a container footprint beside the terminal gate.</p>

<h2>TE46 Terminal Tractor Specifications</h2>
<table style="width:100%;border-collapse:collapse;margin:20px 0;" border="1" cellpadding="8">
<tr style="background:#006341;color:#fff;"><th style="padding:8px;text-align:left;">Parameter</th><th style="padding:8px;text-align:left;">TE46 4x2 Electric Port Tractor</th></tr>
<tr><td style="padding:8px;">GCW rating</td><td style="padding:8px;">42-46 t (container drayage spec)</td></tr>
<tr><td style="padding:8px;">Battery</td><td style="padding:8px;">282-350 kWh CATL LFP, swap-capable option</td></tr>
<tr><td style="padding:8px;">Motor</td><td style="padding:8px;">LvKong 250-320 kW peak / 2,800 Nm</td></tr>
<tr><td style="padding:8px;">Shift endurance</td><td style="padding:8px;">8-10 h mixed drayage duty</td></tr>
<tr><td style="padding:8px;">DC charge 20-80%</td><td style="padding:8px;">~45 min at 240 kW dual-gun</td></tr>
<tr><td style="padding:8px;">Battery swap time</td><td style="padding:8px;">5-6 min (swap variant)</td></tr>
<tr><td style="padding:8px;">Fifth wheel</td><td style="padding:8px;">50 mm, oscillating, terminal-rated</td></tr>
<tr><td style="padding:8px;">FOB price band</td><td style="padding:8px;">US$85,000-115,000 by battery and swap spec</td></tr>
</table>
<p>The torque figure changes terminal operations in a way numbers alone do not capture. A loaded 40 ft container combination at 40 t GCW pulls away from a terminal stack with full torque from zero rpm &mdash; no clutch slip, no rev-matching, no turbo lag. Yard jockeys transitioning from diesel consistently report the same two things: the truck is faster across the first 50 metres (the distance that matters in a terminal), and the absence of diesel noise lets them hear the yard. Ports we serve measured near-miss incident reductions after electrifying, a safety benefit no TCO model prices in.</p>

<h2>Economics at Jordanian Energy Prices</h2>
<p>Jordan&rsquo;s industrial electricity runs roughly US$0.12-0.16 per kWh (the SEZ rate is lower still for qualifying operators), while diesel retails at about US$0.85-0.95 per litre. A diesel drayage tractor burns 0.55-0.70 L/km equivalent on this stop-start duty (idling included); at US$0.90/L, that is US$0.50-0.63 per kilometre. The TE46 consumes 1.6-1.9 kWh/km at 40 t GCW; at US$0.14/kWh, about US$0.22-0.27 per kilometre. On 180 km per day, 300 days a year, the annual energy saving is roughly US$15,000-20,000 per tractor. Maintenance &mdash; no engine, transmission or aftertreatment &mdash; adds US$5,000-7,000 more. Payback on the purchase premium arrives in 24-36 months, and the SEZ incentive framework shortens that further, since qualifying Aqaba operators receive duty and tax relief on electric equipment that narrows the premium.</p>
<ul>
<li><strong>Energy per km:</strong> US$0.55 diesel vs US$0.25 electric &mdash; 55% lower</li>
<li><strong>Annual saving per tractor:</strong> US$20,000-27,000 combined</li>
<li><strong>Queue idling:</strong> ~30% of diesel fuel bill eliminated entirely</li>
<li><strong>Terminal air quality:</strong> zero NOx and particulates inside the gate &mdash; an Aqaba SEZ environmental requirement</li>
</ul>

<h2>Charging and Swap at the Terminal</h2>
<p>Aqaba&rsquo;s port estate and SEZ have the medium-voltage capacity for fleet charging; a six-tractor TE46 fleet runs on one 240 kW DC charger plus managed overnight AC, a 400-500 kVA service class that the port utility provisions routinely. For two-shift operations, the battery-swap configuration changes the infrastructure math: one swap station serves 15-20 tractors, holds 6-8 packs charging on managed load, and eliminates charging downtime entirely. We specify swap for fleets above ten tractors or any two-shift operation, and depot DC charging below that. Both configurations ship with the trucks as a coordinated package &mdash; chargers, swap station, switchgear and load-management software preconfigured for the shift pattern.</p>
<p>One Aqaba-specific opportunity: the SEZ already markets green-logistics credentials to shipping lines and 3PLs with scope-3 targets, and an electrified terminal tractor fleet is a visible, auditable proof point. Several Aqaba operators use exactly this asset in their customer pitches &mdash; a commercial benefit the energy saving alone does not capture.</p>

<h2>Import and Regional Positioning</h2>
<p>Jordan grants duty and tax incentives to electric vehicles and port equipment under its SEZ and green-transport measures, against standard duty on diesel equivalents, and Aqaba&rsquo;s RoRo facilities handle truck imports routinely with 24-30 day sailings from China. We supply the complete homologation package including UN R100 battery certification and English/Arabic manuals. Jordanian logistics groups with regional operations should note our <a href="../markets/jordan.html">Jordan market page</a> &mdash; the TE46 also serves the inland Amman distribution and the Aqaba-to-Amman corridor drayage where the same platform and parts stock apply.</p>
<p>Support follows our port-fleet protocol: every tractor ships with a terminal-duty parts kit (fifth-wheel components, contactors, suspension wear parts), the telematics portal streams battery and drivetrain health to our engineering desk, and swap-variant fleets receive station commissioning support on-site. The drivetrain&rsquo;s service calendar &mdash; brake inspections and coolant checks &mdash; is a rounding error beside the diesel terminal tractor&rsquo;s engine, transmission and DPF maintenance load.</p>

<h2>The Strategic Case for Aqaba</h2>
<p>Aqaba competes on port efficiency and increasingly on green-logistics credentials, and drayage cost is set by energy price multiplied by a duty cycle that punishes diesel. Jordan&rsquo;s SEZ framework rewards the electric move with incentives the diesel alternative cannot claim, and the TE46 is purpose-built for exactly this terminal pattern. The port authority, the terminal operators and the SEZ 3PLs all hold pieces of this opportunity. Whoever assembles them first owns the lowest-cost, lowest-emission container logistics in the country &mdash; and a reference site the wider region will visit.</p>

<h2>Staging the Aqaba Terminal Transition</h2>
<p>A practical rollout for an Aqaba terminal operator starts with a single shift and six to eight TE46 tractors on the quay-to-yard and yard-to-gate shuttles, where the duty cycle is most severe and the depot charger sits at the terminal. The 240 kW charger and the SEZ incentive application go in on order day; the first tractors arrive to a commissioned charger and a trained yard team. As the queue-idling fuel saving and the maintenance reduction accumulate, the fleet extends to the second shift, at which point the battery-swap variant earns its keep by eliminating the charging window entirely. We model the swap-versus-charge decision per operation &mdash; swap above ten tractors or for any two-shift pattern, depot DC below that &mdash; because the right infrastructure choice is the difference between a smooth terminal and a bottleneck at the gate. The diesel tractors are retained for the occasional external drayage leg until charging reaches the inland corridor, a staged plan that keeps every electric tractor on a duty cycle where the numbers are decisively positive.</p>
'''))

# ---------------------------------------------------------------- 8
ARTICLES.append(dict(
f='fujairah-uae-port-electric-tractor-bunkering',
t='Fujairah Port: TE46 Electric Tractors for the UAE&rsquo;s East Coast Bunkering Hub',
d='Fujairah, the world&rsquo;s 2nd-largest bunkering hub, suits the TE46 electric tractor for tank and container terminal duty. EV truck safety, TCO and charging for the UAE port.',
k='TE46 electric tractor, EV truck UAE, electric truck Fujairah, electric port tractor bunkering hub, Dongfeng electric terminal tractor, Fujairah port EV truck, oil terminal electric truck',
img='models/p11_04.jpg',
alt='Dongfeng TE46 electric tractor at Fujairah port bunkering terminal, EV truck for UAE east coast',
net='qyc',
body='''
<p>Fujairah, on the UAE&rsquo;s east coast, is one of the world&rsquo;s most strategically important energy ports: the country&rsquo;s only oil terminal outside the Gulf, the world&rsquo;s second-largest bunkering hub, and a major container and bulk gateway that sits outside the Strait of Hormuz chokepoint. Its terminals &mdash; the oil and product jetties, the bunkering anchorages and the container and bulk yards &mdash; move freight on terminal tractors that shuttle tanks, containers and breakbulk around the clock. That duty cycle is severe, repetitive and return-to-base, and it carries a safety dimension unique to oil terminals: every ignition source is a managed hazard. This article examines the <a href="../products/models/te46-electric-tractor.html">Dongfeng TE46 electric tractor</a> in Fujairah port service, with real numbers on energy, TCO, charging and the safety case that makes electric the logical choice in a bunkering hub.</p>

<h2>Why a Bunkering Hub Electrifies Its Tractors</h2>
<p>Oil-terminal and bunkering-port logistics carry a hard safety constraint: diesel engines are potential ignition sources. Ex-rated zones, hot manifolds and exhaust sparks are managed hazards that drive expensive permitting, hot-work controls and restricted-access rules around tank farms and bunkering jetties. An electric terminal tractor has no combustion, no exhaust and no hot surface &mdash; which simplifies the site permit for electric trucks in hazardous-adjacent logistics and, in many terminal configurations, lets them operate in zones where diesel tractors require special authorization. That safety dimension is the first reason Fujairah&rsquo;s terminal operators look at electric, before the economics.</p>
<p>The second reason is the duty cycle itself. A Fujairah terminal tractor works 10-14 hours daily, covers 120-200 km, spends 30-40% of engine-hours idling in terminal queues and gate holds, and never leaves the port estate. The idling figure is where diesel economics collapse: a 12 L diesel tractor burns 3-4 litres per hour at the jetty queue producing nothing. The TE46&rsquo;s electric drivetrain consumes essentially zero at standstill. Across a shift, queue time alone is 25-35% of the diesel truck&rsquo;s fuel bill and roughly 2% of the EV truck&rsquo;s energy bill.</p>

<h2>TE46 Terminal Tractor Specifications</h2>
<table style="width:100%;border-collapse:collapse;margin:20px 0;" border="1" cellpadding="8">
<tr style="background:#006341;color:#fff;"><th style="padding:8px;text-align:left;">Parameter</th><th style="padding:8px;text-align:left;">TE46 4x2 Electric Port Tractor</th></tr>
<tr><td style="padding:8px;">GCW rating</td><td style="padding:8px;">42-46 t (tank and container drayage spec)</td></tr>
<tr><td style="padding:8px;">Battery</td><td style="padding:8px;">282-350 kWh CATL LFP, swap-capable option</td></tr>
<tr><td style="padding:8px;">Motor</td><td style="padding:8px;">LvKong 250-320 kW peak / 2,800 Nm</td></tr>
<tr><td style="padding:8px;">Shift endurance</td><td style="padding:8px;">8-10 h mixed drayage duty</td></tr>
<tr><td style="padding:8px;">DC charge 20-80%</td><td style="padding:8px;">~45 min at 240 kW dual-gun</td></tr>
<tr><td style="padding:8px;">Battery swap time</td><td style="padding:8px;">5-6 min (swap variant)</td></tr>
<tr><td style="padding:8px;">Hot-climate rating</td><td style="padding:8px;">Operational to +50&deg;C ambient with active thermal management</td></tr>
<tr><td style="padding:8px;">FOB price band</td><td style="padding:8px;">US$85,000-115,000 by battery and swap spec</td></tr>
</table>
<p>The torque profile changes terminal operations measurably: a loaded tank-chassis combination or 40 ft box at 40 t GCW pulls away from a stack with full torque from zero rpm, no clutch slip, no turbo lag. Yard jockeys transitioning from diesel report the truck is faster across the first 50 metres &mdash; the distance that matters in a terminal &mdash; and the absence of diesel noise lets them hear the yard, with several terminals measuring near-miss incident reductions after electrifying. In a bunkering hub where safety is the operating priority, that audible-awareness gain compounds the no-ignition-source advantage.</p>

<h2>Economics at UAE Energy Prices</h2>
<p>UAE industrial electricity runs roughly US$0.08-0.12 per kWh (FEWA/SEWA and port-tariff rates), while diesel retails at about US$0.65 per litre. A diesel drayage tractor burns 0.55-0.70 L/km equivalent on this stop-start duty; at US$0.65/L, that is US$0.36-0.46 per kilometre. The TE46 consumes 1.6-1.9 kWh/km at 40 t GCW; at US$0.10/kWh, about US$0.16-0.19 per kilometre. On 180 km per day, 300 days a year, the annual energy saving is roughly US$13,000-18,000 per tractor. Maintenance &mdash; no engine, transmission or aftertreatment &mdash; adds US$5,000-7,000 more. Payback on the purchase premium arrives in 24-36 months, and the safety-permit savings (reduced hot-work controls, broader terminal access) add value the TCO model does not capture.</p>
<ul>
<li><strong>Energy per km:</strong> US$0.40 diesel vs US$0.17 electric &mdash; 57% lower</li>
<li><strong>Annual saving per tractor:</strong> US$18,000-25,000 combined</li>
<li><strong>Ignition-source removal:</strong> no diesel exhaust or hot manifold &mdash; simpler hazardous-zone permits</li>
<li><strong>Queue idling:</strong> ~30% of diesel fuel bill eliminated entirely at jetty queues</li>
</ul>

<h2>Charging and Swap Inside the Port</h2>
<p>Fujairah&rsquo;s port estate has the medium-voltage capacity for fleet charging; a six-tractor TE46 fleet runs on one 240 kW DC charger plus managed overnight AC, a 400-500 kVA service class the port utility provisions routinely. For two-shift operations, the battery-swap configuration changes the infrastructure math: one swap station serves 15-20 tractors, holds 6-8 packs charging on managed load, and eliminates charging downtime entirely &mdash; critical at a bunkering hub where vessel turnaround drives revenue. We specify swap for fleets above ten tractors or any two-shift operation, and depot DC charging below that. Both configurations ship with the trucks as a coordinated package, preconfigured for the shift pattern and the port&rsquo;s hot-climate duty.</p>
<p>The +50&deg;C Gulf summer is a real design requirement here, not a footnote. The TE46&rsquo;s liquid-cooled LFP pack holds cells in their safe window under 50&deg;C ambient load, and CATL&rsquo;s LFP chemistry tolerates high-temperature cycling far better than NMC &mdash; which is why the 4,500-cycle warranty stays intact even under Fujairah summer bunkering duty. The sealed HV system is rated to IP67, with no air intake to ingest the salt-air corrosion that shortens diesel engine life on a coastal energy port.</p>

<h2>Import and Gulf Context</h2>
<p>UAE port and green-logistics procurement favours sustainability credentials and safety performance. We supply the full export and compliance dossier &mdash; UN R100 battery certification, Gulf heat-rating reports, Arabic operator manuals and the spare-parts schedule &mdash; and ship to Jebel Ali for overland delivery to Fujairah (about 120 km by road). For operators running fleets across the federation, our <a href="../markets/uae.html">UAE market page</a> covers the parallel Jebel Ali, Khalifa and Sharjah port programmes where the same TE46 platform and charging playbook apply, and where platform standardisation across ports halves parts inventory and technician training.</p>
<p>Service support ships with the fleet: a terminal-duty parts kit (fifth-wheel components, contactors, suspension wear parts), telematics-based remote diagnostics with our Gulf engineering desk on WhatsApp, and CATL module stock positioned regionally for 7-12 day delivery. The LvKong drivetrain&rsquo;s low-part-count, sealed design is especially valuable at a coastal energy port where salt air and diesel aftertreatment are a recurring maintenance burden &mdash; the electric tractor simply has no DPF, EGR or turbo to fail.</p>

<h2>The Strategic Case for Fujairah</h2>
<p>Fujairah&rsquo;s position as the world&rsquo;s second-largest bunkering hub makes its terminal tractor fleet both a safety-critical and a cost-critical asset. The TE46 removes the diesel ignition source from hazardous-adjacent logistics, pays back inside three years on severe drayage duty, survives Gulf heat that degrades lesser packs, and strengthens the port&rsquo;s green-logistics credentials with shipping lines that report scope-3 emissions. The terminal operators and bunkering 3PLs who electrify their Fujairah fleets first will own the lowest-cost, safest, lowest-emission port logistics on the east coast &mdash; and a reference site the wider Gulf energy-port network will study.</p>

<h2>Staging the Fujairah Terminal Transition</h2>
<p>A practical rollout for a Fujairah terminal operator starts with a single shift and six to eight TE46 tractors on the tank-chassis and container shuttles nearest the jetties, where the no-ignition-source advantage earns the easiest hazardous-zone permits and the depot charger sits inside the terminal. The 240 kW charger and the port-safety documentation go in on order day; the first tractors arrive to a commissioned charger and a trained yard team. As the queue-idling fuel saving and the maintenance reduction accumulate through a bunkering season, the fleet extends to the second shift, where the battery-swap variant eliminates the charging window entirely and keeps vessels turning. We model the swap-versus-charge decision per terminal &mdash; swap above ten tractors or for any two-shift pattern, depot DC below that &mdash; because at a bunkering hub vessel turnaround is revenue and charging downtime is the one cost the swap station removes. The diesel tractors are retained for the external drayage leg until charging reaches the inland corridor, a staged plan that keeps every electric tractor on a duty cycle where the safety and cost cases both point the same way.</p>
'''))

# __MORE__

for a in ARTICLES:
    html = build(a)
    path = os.path.join(ROOT, 'blog', a['f'] + '.html')
    with open(path, 'w', encoding='utf-8') as fh:
        fh.write(html)
    words = len(re.sub(r'<[^>]+>', ' ', a['body']).split())
    print('%-58s %5d words' % (a['f'], words))
print('done batch2:', len(ARTICLES))
