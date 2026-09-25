# -*- coding: utf-8 -*-
"""Run 14 batch 4: 8 articles (ops/policy + model market angles)."""
import re, os
from _gen_run14_b1 import build

ROOT = os.path.dirname(os.path.abspath(__file__))
ARTICLES = []

# ---------------------------------------------------------------- 25
ARTICLES.append(dict(
f='ev-truck-fleet-kpi-dashboard-metrics',
t='The Electric Truck Fleet KPI Dashboard: 12 Metrics That Actually Run an EV Fleet',
d='Which KPIs should an electric truck fleet track weekly? kWh/km, charge compliance, regen rate, battery SOH and 8 more &mdash; with targets and how to act on each.',
k='EV truck fleet KPI, electric truck fleet metrics, EV fleet dashboard, electric truck telematics KPI, fleet electrification metrics, kWh per km truck',
img='models/p14_06.jpg',
alt='Electric truck fleet KPI dashboard with telematics metrics, EV truck fleet performance tracking',
net='gen',
body='''
<p>Diesel fleets run on three numbers &mdash; fuel per 100 km, uptime, cost per km. Electric fleets inherit those and add a second layer that diesels never had: energy efficiency per route, charging behaviour, battery health, and regenerative performance. The fleets that extract the full value of electrification are the ones that pick a small set of KPIs, review them weekly, and act on the variances. This article lays out the twelve metrics we deploy with every fleet &mdash; what each measures, what good looks like, and what to do when the number drifts. Everything here reads directly off the telematics portal that ships with our electric trucks; none of it requires new hardware.</p>

<h2>Energy Efficiency Metrics</h2>
<table style="width:100%;border-collapse:collapse;margin:20px 0;" border="1" cellpadding="8">
<tr style="background:#006341;color:#fff;"><th style="padding:8px;text-align:left;">KPI</th><th style="padding:8px;text-align:left;">Good Looks Like</th><th style="padding:8px;text-align:left;">When It Drifts</th></tr>
<tr><td style="padding:8px;">kWh per km (per route class)</td><td style="padding:8px;">&plusmn;10% of route baseline</td><td style="padding:8px;">Driver behaviour, payload creep, tyre pressure, HVAC load</td></tr>
<tr><td style="padding:8px;">Regenerative recovery rate</td><td style="padding:8px;">15-25% urban, 20-30% hilly</td><td style="padding:8px;">Driver regen technique, wrong drive mode</td></tr>
<tr><td style="padding:8px;">Energy cost per km (blended)</td><td style="padding:8px;">&le;35% of diesel baseline</td><td style="padding:8px;">Tariff drift, unmanaged peak charging</td></tr>
<tr><td style="padding:8px;">Idle energy share</td><td style="padding:8px;">&lt;5% of daily consumption</td><td style="padding:8px;">HVAC left running at stops &mdash; driver habit</td></tr>
</table>
<p>The kWh-per-km baseline deserves the most care. Set it per route class &mdash; urban delivery, corridor, quarry &mdash; during the first 90 days, per driver and per truck. The variance between best and worst drivers on identical routes runs 10-15%; closing that gap with league tables and coaching is free capacity. A truck whose efficiency decays while its drivers stay constant is telling you something mechanical &mdash; tyre pressure, brake drag, wheel alignment &mdash; and the KPI catches it weeks before a breakdown does.</p>

<h2>Charging Discipline Metrics</h2>
<p>Charging KPIs protect both the energy bill and the battery. Charge-window compliance &mdash; the share of energy drawn in off-peak hours &mdash; should run 70%+ for depot fleets, and every point below target costs real money under time-of-use tariffs. Session completion rate tracks interrupted sessions; interruptions usually mean a bay blocked by a diesel vehicle or a connector fault, both fixable once visible. Departure state-of-charge compliance &mdash; did every truck leave at its planned SOC? &mdash; is the dispatch-trust metric; below 95%, investigate load-management settings before blaming hardware. Peak demand versus contracted capacity keeps the demand-charge line honest: a well-managed site holds its peak at 60-70% of contract, and a fleet consistently brushing its ceiling should either raise the contract deliberately or fix the schedule.</p>

<h2>Battery Health Metrics</h2>
<ul>
<li><strong>State of health (SOH) per pack:</strong> review monthly; expect ~1-1.5% fade per year on liquid-cooled LFP &mdash; a truck fading faster is a warranty conversation with data attached</li>
<li><strong>Charge-rate distribution:</strong> share of DC sessions above 1C &mdash; occasional fast charging is fine; a fleet living at maximum rate ages packs faster</li>
<li><strong>Thermal band compliance:</strong> share of operating time in the optimal cell-temperature band &mdash; chronic high-temperature operation shows up here before it shows up in SOH</li>
<li><strong>Cell imbalance (max-min cell voltage spread):</strong> a slowly widening spread flags a module worth watching &mdash; the earliest possible warning of a warranty event</li>
</ul>
<p>Battery metrics feel technical, but their purpose is financial: the pack is 30-40% of the truck&rsquo;s value and its health documentation drives warranty claims, insurance pricing and resale value. A fleet reviewing SOH monthly catches abnormal degradation at 2-3% deviation, when the conversation with the OEM is easy &mdash; instead of at 15%, when it is an argument.</p>

<h2>Operations Metrics</h2>
<p>The classics stay, reinterpreted. Uptime for an electric fleet should exceed the diesel baseline &mdash; 97%+ is realistic because the drivetrain has fewer failure modes &mdash; and below-target uptime on electric usually traces to charging process failures rather than vehicle faults. Cost per km (all-in) is the board metric: energy, maintenance, tyres, insurance, depreciation &mdash; and it should land 25-40% under the diesel comparator within the first year or the review asks why. Utilisation (revenue km per truck-day) matters more on electric than diesel because the capital premium amortises per kilometre; an underutilised electric truck is the only configuration in which the TCO case fails, and this KPI is its early warning.</p>

<h2>Making the Dashboard Run the Week</h2>
<p>Metrics without rhythm are decoration. The operating pattern we deploy: a 30-minute Monday review &mdash; EV fleet manager, dispatcher, HV tech &mdash; walking the twelve KPIs against targets, assigning one action per red number. Monthly, the energy-cost and battery-health lines go to the CFO in the same format every month, building the dataset that later wins the insurance renewal and the warranty claim. Quarterly, driver league tables reset with recognition for the top performers &mdash; the cheapest efficiency programme in the industry. Buyers structuring their first electric operation can see the deployment context for this playbook on our <a href="../markets/kenya.html">Kenya market page</a>, where fleets run exactly this KPI discipline across Nairobi and corridor duty.</p>

<h2>The Bottom Line</h2>
<p>An electric truck fleet generates better operational data than any diesel fleet ever could &mdash; the question is whether anyone reads it. Twelve metrics, one weekly meeting, monthly battery review, quarterly driver tables: that is the entire discipline. Fleets that run it find their efficiency converging on the best driver&rsquo;s numbers, their energy cost holding at target, and their battery documentation compounding into warranty, insurance and resale value. The data is already flowing; the dashboard just decides whether it works for you.</p>
'''))

# ---------------------------------------------------------------- 26
ARTICLES.append(dict(
f='uzbekistan-ev-assembly-policy-electric-truck-imports',
t='Uzbekistan&rsquo;s EV Assembly Push: What the 2026 Policy Shift Means for Electric Truck Importers',
d='Uzbekistan is building local EV assembly and adjusting import rules. What the policy shift means for electric truck buyers: duties, localisation timelines and the import window.',
k='Uzbekistan EV policy, electric truck Uzbekistan, EV truck import Central Asia, Uzbekistan EV assembly, electric truck duty Uzbekistan, Dongfeng electric truck CIS',
img='models/p14_07.jpg',
alt='Uzbekistan EV assembly policy and electric truck imports, EV truck Central Asia market analysis',
net='zhc',
body='''
<p>Uzbekistan has become Central Asia&rsquo;s most aggressive EV policy market. The country that hosted BYD&rsquo;s first Central Asian passenger-car plant, slashed EV import duties to near zero, and built a charging network across Tashkent in three years is now extending the same logic toward commercial vehicles &mdash; and the policy signals of 2025-2026 matter enormously for anyone planning to import electric trucks into the region&rsquo;s largest consumer market. This article maps the current framework: where duties stand, what the localisation push means for the import window, how certification works, and how fleet buyers should sequence their moves. For context on the platform side, our <a href="../markets/uzbekistan.html">Uzbekistan market page</a> tracks the operating environment continuously.</p>

<h2>The Policy Architecture as of 2026</h2>
<p>Uzbekistan&rsquo;s EV framework rests on three pillars. Duty treatment: electric vehicles have enjoyed zero or near-zero import duty since 2022, against 15-30% plus excise for diesel trucks &mdash; an advantage worth US$15,000-40,000 per heavy truck at import. Localisation incentives: the government&rsquo;s automotive programme offers land, tax holidays and preferential energy tariffs to assembly operations meeting local-content thresholds, with commercial vehicles explicitly named in the 2024-2026 industrial programme. Infrastructure mandates: new fuel stations, shopping centres and residential developments above size thresholds must include charging, and the state grid operator offers preferential tariffs for depot charging. The direction is unambiguous: import-friendly today, localisation-rewarding tomorrow.</p>

<h2>The Importer&rsquo;s Window: Reading the Timeline</h2>
<table style="width:100%;border-collapse:collapse;margin:20px 0;" border="1" cellpadding="8">
<tr style="background:#006341;color:#fff;"><th style="padding:8px;text-align:left;">Phase</th><th style="padding:8px;text-align:left;">Policy Posture</th><th style="padding:8px;text-align:left;">Importer Play</th></tr>
<tr><td style="padding:8px;">2022-2026 (now)</td><td style="padding:8px;">Zero/low EV duty, open imports, certification streamlined</td><td style="padding:8px;">Import fully-built trucks; build fleet references and service capability</td></tr>
<tr><td style="padding:8px;">2026-2028 (forming)</td><td style="padding:8px;">Local-content preferences in state tenders; assembly incentives widen to CV</td><td style="padding:8px;">Evaluate SKD partnerships; lock distribution agreements</td></tr>
<tr><td style="padding:8px;">2028+ (signalled)</td><td style="padding:8px;">Graduated localisation requirements, tender scoring favours local assembly</td><td style="padding:8px;">SKD/CKD operation or local partner for tender-heavy segments</td></tr>
</table>
<p>The pattern follows the passenger-car playbook exactly: open the market to imports to build volume and charging density, then tilt procurement toward local assembly once the ecosystem exists. Passenger EVs ran this cycle in three years. For heavy trucks the practical read: the fully-built import window is open now and will remain commercially viable for years, but state-tender segments (municipal sanitation, utility fleets, state logistics) will score local assembly progressively higher. Importers should win reference fleets now &mdash; the localisation conversation is far easier with operating trucks and trained technicians already in country.</p>

<h2>Certification and Homologation Reality</h2>
<p>Uzbekistan certifies vehicles under the UzStandard framework with ECE-recognition pathways &mdash; UN R100 (battery safety) and UN R10 (EMC) documentation accelerates approval materially, and we supply both as standard with export vehicles. Russian-language documentation remains operationally essential: the homologation file, service manuals and parts catalogues in Russian cut weeks from approval and years from technician development. Customs clearance in Tashkent for properly documented EVs runs efficiently by regional standards, and the zero-duty status simplifies the valuation conversation that complicates diesel truck imports. First-time importers should budget 4-8 weeks for the initial homologation and near-routine clearance thereafter.</p>

<h2>Where the Demand Is: Segment by Segment</h2>
<ul>
<li><strong>Municipal sanitation:</strong> Tashkent&rsquo;s fleet-modernisation programme names electric sweepers and compactors &mdash; the KT1D and KT3E classes &mdash; in its procurement pipeline; tender scoring already weights local service capability</li>
<li><strong>Urban distribution:</strong> the e-commerce and grocery boom in Tashkent (2.5 m metro) fits KT5M/KT5J-class box trucks on 100-180 km daily duty</li>
<li><strong>Construction:</strong> the Tashkent City and New Tashkent megaprojects run tipper fleets on short, depot-based cycles &mdash; TZ3Z/TZ5E territory</li>
<li><strong>Corridor freight:</strong> Tashkent-Samarkand (300 km) and the Fergana valley routes suit KTH3/TE8L with destination charging</li>
<li><strong>Mining and heavy haul:</strong> Navoi and Almalyk mining logistics are early but watching; swap-configured rigs answer their 24/7 requirement</li>
</ul>
<p>Energy economics underpin all of it: Uzbek industrial electricity runs US$0.05-0.08/kWh &mdash; among the world&rsquo;s lowest &mdash; against diesel at US$0.85-1.00/L. The per-kilometre energy saving of 70-75% is among the strongest we model anywhere, and the state&rsquo;s gas-to-power transition is freeing further generation capacity explicitly earmarked for transport electrification.</p>

<h2>The Localisation Question for Buyers</h2>
<p>Should an importer chase SKD assembly? The honest framework: for distributor-scale volumes (hundreds of trucks annually across the region), assembly economics and tender scoring increasingly justify a partnership conversation &mdash; and we structure such partnerships with kit supply, training and quality systems. For fleet buyers purchasing tens of trucks, fully-built imports remain correct; the duty advantage holds, and the service ecosystem &mdash; parts stock in Tashkent, HV-trained technicians, remote diagnostics &mdash; is what actually determines fleet success. The buyers making the best moves today are locking distribution and service agreements while competition for them is thin, and building the operating references that will decide tender scoring later.</p>

<h2>The Strategic Read</h2>
<p>Uzbekistan is running the most coherent EV industrial policy between China and Europe, and its commercial-vehicle phase is just beginning. The import window is open, the duty advantage is real, the energy economics are exceptional, and the localisation tilt rewards exactly the early movers who build references and capability now. Fleet buyers and distributors who treat 2026 as the entry year &mdash; not the wait-and-see year &mdash; will hold the positions the 2028 procurement rules are being written to reward.</p>
'''))

# ---------------------------------------------------------------- 27
ARTICLES.append(dict(
f='ev-truck-charging-connector-standards-gbt-ccs2-mcs',
t='GB/T, CCS2 or MCS? Electric Truck Charging Connector Standards Explained for Importers',
d='Which charging connector should your imported electric trucks carry? GB/T vs CCS2 vs MCS compared: power ceilings, regional fit and how to future-proof an EV truck fleet.',
k='electric truck charging connector, GBT CCS2 MCS, EV truck charging standard, MCS megawatt charging, electric truck CCS2, EV truck import charging plug',
img='models/p14_09.jpg',
alt='Electric truck charging connector standards GBT CCS2 MCS compared, EV truck importer guide',
net='gen',
body='''
<p>Ask a room of fleet buyers what worries them about importing electric trucks and &ldquo;the plug&rdquo; comes up within five minutes. The concern is legitimate &mdash; the wrong connector choice can strand a fleet from its region&rsquo;s charging infrastructure &mdash; but the standards landscape is simpler than the anxiety suggests. Three systems matter for heavy trucks: GB/T (China&rsquo;s standard, dominant in Chinese-market vehicles), CCS2 (the European-descended standard used across most export markets), and MCS (the Megawatt Charging System, the heavy-truck future). This guide explains what each really is, which markets run on which, and how to specify imports so the fleet is right today and adaptable tomorrow.</p>

<h2>The Three Standards in One Paragraph Each</h2>
<p>GB/T is China&rsquo;s national DC charging standard: a robust connector rated to 250 A (with liquid-cooled high-power variants reaching 400-600 kW on the newest specification), used on every Chinese domestic charger and vehicle. Its strengths are maturity and the sheer scale of its installed base; its weakness is that almost nobody outside China deploys it. CCS2 (Combined Charging System, Type 2) is the export-world standard: the combined AC/DC connector used across Europe, the Gulf, Africa, Latin America, Central and Southeast Asia, rated to 500 A on liquid-cooled cables &mdash; roughly 350-500 kW, enough for any current truck battery. MCS (Megawatt Charging System) is the purpose-built heavy-truck standard finalised by CharIN: a single large connector rated to 1,250 A / 3.75 MW, designed so a 600 kWh truck battery charges 20-80% in the time of a driver&rsquo;s mandatory break.</p>

<h2>Which Market Runs Which</h2>
<table style="width:100%;border-collapse:collapse;margin:20px 0;" border="1" cellpadding="8">
<tr style="background:#006341;color:#fff;"><th style="padding:8px;text-align:left;">Region</th><th style="padding:8px;text-align:left;">Truck Charging Standard</th><th style="padding:8px;text-align:left;">Importer Specification</th></tr>
<tr><td style="padding:8px;">Gulf (UAE, KSA, Qatar)</td><td style="padding:8px;">CCS2; MCS pilots announced</td><td style="padding:8px;">CCS2 today, MCS-ready wiring</td></tr>
<tr><td style="padding:8px;">Africa (all regions)</td><td style="padding:8px;">CCS2 on virtually all public/fleet installs</td><td style="padding:8px;">CCS2</td></tr>
<tr><td style="padding:8px;">Central &amp; Southeast Asia</td><td style="padding:8px;">CCS2 dominant; GB/T pockets (Mongolia, Laos)</td><td style="padding:8px;">CCS2; GB/T variant for border fleets</td></tr>
<tr><td style="padding:8px;">Latin America</td><td style="padding:8px;">CCS2 (CCS1 in parts of the north)</td><td style="padding:8px;">CCS2; CCS1 for Mexico northbound</td></tr>
<tr><td style="padding:8px;">Europe</td><td style="padding:8px;">CCS2 now, MCS rolling out on AFIR corridors</td><td style="padding:8px;">CCS2 + MCS readiness</td></tr>
<tr><td style="padding:8px;">China domestic</td><td style="padding:8px;">GB/T</td><td style="padding:8px;">GB/T</td></tr>
</table>
<p>The practical rule for our export markets: CCS2 is the safe default everywhere, full stop. Every public high-power charger and every fleet depot installation across Africa, the Gulf, Central Asia and Latin America is CCS2. That is why our export-specification electric trucks ship with CCS2 inlets as standard, with GB/T retained for domestic-Chinese duty and CCS1 available for North-American-adjacent Caribbean duty.</p>

<h2>The Power Ceiling Question</h2>
<p>Connector choice caps charging speed, so match it to the battery. Fleets often over-index on this: a 106-140 kWh delivery truck cannot physically use more than 120-160 kW, which standard CCS2 serves comfortably. The 282-350 kWh packs in tractors and construction trucks charge 20-80% in 45-60 minutes at 240-360 kW &mdash; also within liquid-cooled CCS2&rsquo;s envelope. Only the largest packs (500-600 kWh in heavy tractors and mining trucks) begin to justify MCS, and even there, dual-gun CCS2 &mdash; two cables into two inlets, standard on our large-pack variants &mdash; delivers 400-500 kW today from hardware that already exists. MCS matters for the 2027+ generation of megawatt corridor charging; for a fleet buying in 2026, CCS2 with MCS-ready wiring harnesses is the future-proof specification, and it is how we build the trucks.</p>
<ul>
<li><strong>Default export spec:</strong> CCS2, liquid-cooled cable support, ISO 15118 authentication</li>
<li><strong>Large-pack trucks:</strong> dual-gun CCS2 for 400-500 kW today; MCS-ready harness for tomorrow</li>
<li><strong>Never retrofit connectors casually:</strong> inlet, wiring and BMS charge maps are engineered together &mdash; order the right spec instead</li>
<li><strong>Adapter reality:</strong> GB/T-to-CCS2 adapters exist but throttle power and add failure points &mdash; acceptable as emergency backup, never as a plan</li>
</ul>

<h2>Depot Hardware: The Other Half of the Decision</h2>
<p>The truck inlet is only half the connector story; the depot charger is the other half, and the same logic applies. Specify OCPP-native CCS2 dispensers with liquid-cooled cables for anything above 150 kW &mdash; air-cooled cables at 500 A are a handling nightmare in a truck yard. For fleets running mixed sizes, dual-dispenser chargers (one power unit, two cables) balance utilisation across shifts. And for any fleet planning beyond five years: lay the MCS-capable conduit and reserve the bay space now, because the civil works are the expensive half of a later upgrade. Our charger packages ship pre-configured for the truck fleet&rsquo;s exact inlet and charge-map specification &mdash; the handshake between truck and charger is validated before the vessel sails, not discovered at the depot.</p>

<h2>Regional Notes From the Field</h2>
<p>Gulf fleets should know that both the UAE and Saudi Arabia standardised public high-power charging on CCS2, and their announced corridor programmes are MCS-forward &mdash; the CCS2-plus-readiness specification fits perfectly. East African fleets will find CCS2 at every commercial installation from Nairobi to Lusaka; our <a href="../markets/tanzania.html">Tanzania market page</a> covers the corridor charging picture. Central Asian fleets running cross-border into western China (Khorgos, Irkeshtam) are the one case where a GB/T secondary inlet genuinely earns its cost &mdash; a real option we configure for exactly those operators. Latin American fleets should confirm CCS1 versus CCS2 for any Mexico-northbound duty; south of Mexico the answer is uniformly CCS2.</p>

<h2>The Bottom Line</h2>
<p>The connector question has a boring, correct answer for 95% of import fleets: CCS2, liquid-cooled, ISO 15118, dual-gun on large packs, MCS-ready wiring. Specify that, match the depot hardware to it, and the fleet charges everywhere its region offers power &mdash; today, and through the MCS transition when it arrives. The buyers who get this wrong are the ones who accept whatever inlet the truck happens to carry; the buyers who get it right spend one line in the purchase order and never think about it again.</p>
'''))

# ---------------------------------------------------------------- 28
ARTICLES.append(dict(
f='kta1-senegal-phosphate-electric-dump-truck',
t='Senegal&rsquo;s Phosphate Belt: KTA1 Electric Dump Trucks for the Ta&iuml;ba Corridor',
d='Senegal&rsquo;s phosphate industry hauls millions of tonnes on the Thies-Taiba corridor. KTA1 electric dump truck economics for phosphate haulage: specs, swap and TCO inside.',
k='KTA1 electric dump truck, EV truck Senegal, phosphate haulage electric truck, electric dump truck Taiba, Dongfeng electric truck, mining EV truck West Africa, ICS Senegal truck',
img='models/p04_00.jpg',
alt='Dongfeng KTA1 electric dump truck hauling phosphate in Senegal, EV truck for the Taiba corridor',
net='zxc',
body='''
<p>Senegal is one of the world&rsquo;s significant phosphate producers, and the industry&rsquo;s geography is a gift to electrification. The mines around Ta&iuml;ba and the Lam Lam deposit feed the ICS (Industries Chimiques du S&eacute;n&eacute;gal) complex and the port of Dakar along short, fixed corridors of 15-100 km &mdash; millions of tonnes a year moving on routes that never change, between facilities that never move, hauled by diesel trucks burning imported fuel. This article examines the <a href="../products/models/kta1-electric-dump-truck.html">Dongfeng KTA1 electric dump truck</a> on Senegalese phosphate duty: the haul profile, the battery-swap architecture that fits round-the-clock operations, and the TCO against the diesel status quo. Few industrial corridors in West Africa match this one for EV truck readiness.</p>

<h2>The Corridor Profile</h2>
<p>Phosphate haulage in the Thi&egrave;s region has three electric-friendly properties. First, distance: Ta&iuml;ba to the ICS Mbao complex runs roughly 90-100 km on the N1; the satellite pits to Ta&iuml;ba processing, 10-30 km. Both sit inside a single charge for the KTA1&rsquo;s 282-350 kWh battery options on rigid-haul duty, and the longer legs are one top-up from round-trip coverage. Second, the material: phosphate ore and concentrates run at densities that fill the body by volume &mdash; the truck works at its designed payload, not its weight limit. Third, the infrastructure: mines, plants and port are fixed industrial facilities with power, security and maintenance bases &mdash; every property a charging-and-swap installation needs. Add Senegal&rsquo;s flat coastal-plain terrain &mdash; minimal climbing, moderate speeds &mdash; and the duty cycle lands squarely in the electric drivetrain&rsquo;s efficiency sweet spot.</p>

<h2>KTA1 Specification for Phosphate Duty</h2>
<table style="width:100%;border-collapse:collapse;margin:20px 0;" border="1" cellpadding="8">
<tr style="background:#006341;color:#fff;"><th style="padding:8px;text-align:left;">Parameter</th><th style="padding:8px;text-align:left;">KTA1 8x4 Electric Dump Truck</th></tr>
<tr><td style="padding:8px;">GVW / payload</td><td style="padding:8px;">31 t / 20-21 t (18-20 m&sup3; body)</td></tr>
<tr><td style="padding:8px;">Battery</td><td style="padding:8px;">282-350 kWh CATL LFP, swap-capable</td></tr>
<tr><td style="padding:8px;">Motor</td><td style="padding:8px;">LvKong 360-420 kW peak / 2,400-2,800 Nm</td></tr>
<tr><td style="padding:8px;">Range (loaded, flat corridor)</td><td style="padding:8px;">200-260 km</td></tr>
<tr><td style="padding:8px;">Energy turnaround</td><td style="padding:8px;">swap 5-6 min / 240 kW DC ~50 min</td></tr>
<tr><td style="padding:8px;">Dust sealing</td><td style="padding:8px;">IP67 HV system, pressurised filtered cab</td></tr>
<tr><td style="padding:8px;">Battery warranty</td><td style="padding:8px;">8 years / 4,500 cycles to 70% SOH</td></tr>
<tr><td style="padding:8px;">FOB price band</td><td style="padding:8px;">US$95,000-118,000</td></tr>
</table>
<p>The dust question dominates any Sahelian-edge industrial conversation, and phosphate dust is particularly aggressive &mdash; fine, abrasive and chemically active. The KTA1&rsquo;s answer is architectural: no engine air filter to clog, no turbocharger to erode, no intercooler to blind. The HV system is sealed to IP67, the cab runs pressurised filtration, and the drivetrain&rsquo;s only air-moving components are the liquid-cooling fans &mdash; serviceable items on a scheduled interval. Diesel trucks in this environment measure air-filter life in days and engine life in shortened thousands of hours; the electric drivetrain simply removes that entire maintenance category.</p>

<h2>Swap Architecture for Continuous Operations</h2>
<p>ICS-scale phosphate logistics run continuously, and battery swap is what makes electric haulage continuous. The corridor design we propose: one containerised swap station at the mine end, one at the plant/port end, each holding 7-9 packs and serving 12-18 trucks on rotation. Trucks swap at whichever end their cycle dictates &mdash; a 5-6 minute exchange, faster than a diesel refuel with queue &mdash; and packs charge on managed load during the troughs. The stations draw 1.5-2.5 MW each, well within the industrial power envelope at both sites, and their containerised format relocates as pit phases advance. For contractors running 10-30 truck fleets on this corridor, swap converts electrification from a shift-planning exercise into a like-for-like diesel replacement with better economics.</p>

<h2>TCO on the Ta&iuml;ba Corridor</h2>
<p>The arithmetic at Senegalese prices. A diesel 31 t tipper on this duty burns 0.50-0.58 L/km; at US$1.15-1.25/L, US$0.60-0.70 per kilometre. The KTA1 consumes 1.6-1.9 kWh/km loaded on the flat corridor; at Senelec industrial tariffs around US$0.16-0.18/kWh, US$0.28-0.32 per kilometre &mdash; and under a solar canopy (Senegal&rsquo;s 5.0-5.5 peak sun hours are among West Africa&rsquo;s best), an effective US$0.15-0.20. On 350 km daily across two shifts, 300 days, the annual energy saving per truck runs US$35,000-50,000 depending on charging source. Maintenance adds US$8,000-12,000 in a dust environment that is merciless to diesel engines. Against the purchase premium and apportioned swap infrastructure, payback lands at 18-26 months &mdash; and the corridor&rsquo;s 24/7 utilisation is what makes the numbers this strong.</p>
<ul>
<li><strong>Energy per km:</strong> US$0.65 diesel vs US$0.15-0.32 electric (solar vs grid)</li>
<li><strong>Annual saving per truck:</strong> US$43,000-60,000 on two-shift corridor duty</li>
<li><strong>Payback:</strong> 18-26 months including swap infrastructure</li>
<li><strong>Dust dividend:</strong> no air filters, turbo or engine wear from phosphate dust</li>
<li><strong>Noise:</strong> night haulage past corridor villages without the diesel roar &mdash; a social-licence asset</li>
</ul>

<h2>Import and Industrial Context</h2>
<p>Trucks enter Senegal through Dakar&rsquo;s RoRo facilities with 30-36 day sailings from China; we deliver with full French documentation, UN R100 certification, and the industrial-fleet parts package. Senegal&rsquo;s treatment of electric industrial vehicles includes duty advantages, and the customs process for documented industrial imports is efficient. Regional operators should note our <a href="../markets/ghana.html">Ghana market page</a> for the parallel West African mining-logistics deployments &mdash; the KTA1 platform serves comparable duty across the region&rsquo;s mineral corridors with shared support infrastructure.</p>
<p>Support for an ICS-scale deployment is structured as an industrial contract: commissioning engineers through the swap-station build and ramp-up, a resident or fly-in technical programme sized to fleet count, parts warehousing at site, and 24/7 telemetry monitoring of every pack. The maintenance model inverts the diesel reality &mdash; a small team on brakes, suspension and coolant replaces the large workshop organisation that dust-ingested diesel engines demand, and availability rises accordingly.</p>

<h2>The Strategic Case</h2>
<p>Senegal&rsquo;s phosphate industry competes in a global commodity market where delivered cost decides contracts, and haulage energy is a first-order cost line it currently buys at imported-diesel prices. A corridor that electrifies cuts that line by half or more, removes a fuel supply chain vulnerable to every disruption the region knows too well, and gains an ESG credential that European and Asian buyers increasingly price. The corridor&rsquo;s owners have already built the mines, the plants and the port; the electric fleet is the obvious next layer of the same industrial logic &mdash; and the first operator to run it owns the cost curve everyone else will be measured against.</p>
'''))

# ---------------------------------------------------------------- 29
ARTICLES.append(dict(
f='kt9x-egypt-new-capital-electric-mixer',
t='Egypt&rsquo;s New Administrative Capital: KT9X Electric Mixers for the Region&rsquo;s Biggest Build',
d='Egypt&rsquo;s New Administrative Capital pours concrete at continental scale. KT9X electric mixer truck economics for NAC batching fleets: drum specs, charging and TCO inside.',
k='KT9X electric mixer truck, EV truck Egypt, electric concrete mixer New Administrative Capital, electric mixer truck Cairo, Dongfeng electric truck, construction EV truck Middle East',
img='models/p05_00.jpg',
alt='Dongfeng KT9X electric concrete mixer at Egypt New Administrative Capital, EV truck for NAC construction',
net='zxc',
body='''
<p>East of Cairo, the New Administrative Capital continues one of the largest construction programmes on earth &mdash; ministries, residential districts, the Iconic Tower district, and the infrastructure to serve a city designed for six million people. Concrete moves to those sites from batching plants ringed around the development, in mixer trucks running short, intense cycles that idle away half their engine hours in queues and drum-rotation standby. It is a duty cycle that punishes diesel machinery and rewards electrification with unusual clarity. This article examines the <a href="../products/models/kt9x-electric-mixer-truck.html">Dongfeng KT9X electric mixer truck</a> for NAC-scale operations: the drum-drive architecture, the charging plan, and the economics at Egyptian energy prices.</p>

<h2>Why Mixer Duty Is Made for Electric</h2>
<p>A concrete mixer&rsquo;s diesel engine does two jobs: drive the truck and turn the drum &mdash; and on a typical NAC cycle (batch plant to site, 20-45 km), the engine spends 60-90 minutes per trip running largely to serve the drum, the queue and the pour. The KT9X separates these functions electrically: the traction motor drives, a dedicated electric drum drive rotates the barrel, and both draw from a 350-420 kWh CATL LFP pack sized for 8-10 deliveries per charge on typical NAC cycles. The electric drum drive holds precise rotation at any speed &mdash; better slump control than an engine-speed-dependent hydraulic drive &mdash; and draws its 3-5 kW continuously without the diesel&rsquo;s baseline burn. Queue time, the diesel mixer&rsquo;s great fuel sink, costs the electric truck almost nothing.</p>

<h2>KT9X Specification for Mega-Project Duty</h2>
<table style="width:100%;border-collapse:collapse;margin:20px 0;" border="1" cellpadding="8">
<tr style="background:#006341;color:#fff;"><th style="padding:8px;text-align:left;">Parameter</th><th style="padding:8px;text-align:left;">KT9X 8x4 Electric Mixer</th></tr>
<tr><td style="padding:8px;">Drum capacity</td><td style="padding:8px;">10-12 m&sup3; (rated mixing volume)</td></tr>
<tr><td style="padding:8px;">Battery</td><td style="padding:8px;">350-420 kWh CATL LFP, liquid-cooled</td></tr>
<tr><td style="padding:8px;">Traction motor</td><td style="padding:8px;">LvKong 360-420 kW peak / 2,400-2,800 Nm</td></tr>
<tr><td style="padding:8px;">Drum drive</td><td style="padding:8px;">independent electric drive, precise RPM control</td></tr>
<tr><td style="padding:8px;">Deliveries per charge (30 km cycle)</td><td style="padding:8px;">8-10 loads</td></tr>
<tr><td style="padding:8px;">DC charge 20-80%</td><td style="padding:8px;">~55 min at 240-360 kW</td></tr>
<tr><td style="padding:8px;">Ambient rating</td><td style="padding:8px;">to +50&deg;C &mdash; Egyptian summer duty</td></tr>
<tr><td style="padding:8px;">FOB price band</td><td style="padding:8px;">US$118,000-140,000</td></tr>
</table>
<p>The +50&deg;C rating is decisive in Egypt, where June-through-September site temperatures exceed 40&deg;C daily and concrete temperature control is already a quality battle. The liquid-cooled pack holds its thermal band through the summer, and the cab&rsquo;s electric air conditioning runs at full capacity during queues without the diesel&rsquo;s heat and noise &mdash; a driver-welfare point that matters in a market competing for skilled mixer operators. The dust environment of a greenfield mega-project meets the same sealed-drivetrain answer: no air filters, no turbo, no engine ingestion, in a place where dust is a permanent weather condition.</p>

<h2>TCO at Egyptian Prices</h2>
<p>Egyptian diesel, even after subsidy reforms, runs around US$0.55-0.70 per litre equivalent for industrial buyers &mdash; cheaper than Europe, but a 12 m&sup3; mixer burns 0.8-1.0 L/km equivalent on loaded NAC cycles including drum and queue load, so energy still costs US$0.50-0.65 per kilometre. The KT9X consumes 1.7-2.0 kWh/km all-in on the same cycle; at industrial tariffs of US$0.08-0.12/kWh, US$0.15-0.22 per kilometre. On 220 km daily across two shifts, 300 days, the annual energy saving runs US$23,000-28,000 per truck. Maintenance &mdash; no engine, transmission, or hydraulic pump drive &mdash; adds US$6,000-9,000. Against the purchase premium, payback lands at 24-34 months, improving sharply at higher utilisation &mdash; and NAC fleets run some of the highest mixer utilisation in the region.</p>
<ul>
<li><strong>Energy per km:</strong> US$0.55-0.65 diesel vs US$0.15-0.22 electric</li>
<li><strong>Queue/standby cost:</strong> ~60-90 min per trip of diesel baseline burn eliminated</li>
<li><strong>Annual saving per truck:</strong> US$29,000-37,000 combined on two-shift duty</li>
<li><strong>Slump control:</strong> constant-speed electric drum drive, independent of engine rpm</li>
<li><strong>Site noise:</strong> near-silent pour operation &mdash; an advantage on the NAC&rsquo;s occupied-phase sites</li>
</ul>

<h2>Charging at the Batching Plant</h2>
<p>Mixer fleets charge where they batch &mdash; the plant is the depot. A 15-20 truck NAC plant fleet needs two to three 240-360 kW DC chargers plus managed overnight capacity, a 1-1.5 MVA service class that Egypt&rsquo;s distribution companies supply to industrial customers in the new-city zones, where grid infrastructure is genuinely new and generously specified. Charge scheduling follows the pour calendar: overnight full charges, a midday rotation during the batching lull, and the load-management controller holding the site under its contract. The plants&rsquo; own standby generation provides resilience; the fleets&rsquo; batteries, collectively 6-8 MWh across twenty trucks, provide the buffer that makes outages a scheduling matter rather than a stoppage.</p>

<h2>Import and Market Context</h2>
<p>Trucks enter Egypt through Alexandria or Sokhna with 28-34 day sailings from China; we deliver with Arabic/English documentation, UN R100 certification and the fleet parts package. Egypt&rsquo;s treatment of electric commercial vehicles includes duty advantages under its localisation-and-EV programme, and the NAC project&rsquo;s own procurement increasingly weights emissions performance &mdash; the government has stated air-quality goals for the new city that favour zero-emission construction logistics. Regional operators can find the wider context on our <a href="../markets/egypt.html">Egypt market page</a>, and Gulf buyers facing identical mega-project duty should note the parallel deployments across Saudi giga-projects where this platform already works.</p>
<p>Support follows our mega-project protocol: commissioning through the charger build and the first pour season, extended parts kits sized for site self-sufficiency, CATL module stock at 10-14 days via regional logistics, and telemetry monitoring of every truck&rsquo;s drum drive, traction system and pack. The service calendar &mdash; brakes, suspension, coolant, drum rollers &mdash; is a fraction of the diesel mixer&rsquo;s engine-hydraulic-transmission load, and availability on a pour-critical fleet is revenue.</p>

<h2>The Bottom Line for NAC Fleets</h2>
<p>The New Administrative Capital is exactly the environment where electric mixers win first: fixed plants, short cycles, brutal utilisation, punitive queue time, and a client &mdash; the Egyptian state &mdash; that has declared its air-quality intentions for the city. The batching companies that electrify their NAC fleets convert those conditions into a 60-70% energy cost reduction, a maintenance-light fleet, and a procurement advantage on the project&rsquo;s next phases. The concrete will be poured either way; the only question is whose mixers deliver it at the lower cost per cubic metre.</p>
'''))

# ---------------------------------------------------------------- 30
ARTICLES.append(dict(
f='tz8j-kenya-affordable-housing-electric-mixer',
t='Kenya&rsquo;s Affordable Housing Programme: TZ8J Electric Mixers for the Construction Pipeline',
d='Kenya&rsquo;s Affordable Housing Programme needs millions of cubic metres of concrete. TZ8J electric mixer truck economics for Nairobi batching fleets: specs, charging, TCO.',
k='TZ8J electric mixer truck, EV truck Kenya, electric concrete mixer Nairobi, Affordable Housing Programme trucks, Dongfeng electric truck, construction EV truck East Africa',
img='models/p05_01.jpg',
alt='Dongfeng TZ8J electric concrete mixer on a Nairobi housing site, EV truck for Kenya construction',
net='zxc',
body='''
<p>Kenya&rsquo;s Affordable Housing Programme is one of Africa&rsquo;s largest state-backed construction pipelines &mdash; hundreds of thousands of units under contract across Nairobi and the secondary towns, with site after site pouring concrete six days a week. Every one of those sites is served by batching plants running mixer fleets on short urban cycles, and every one of those mixers burns diesel in Nairobi traffic at US$1.40-1.55 per litre. This article examines the <a href="../products/models/tz8j-electric-mixer-truck.html">Dongfeng TZ8J electric mixer truck</a> for Kenya&rsquo;s housing programme: why the project&rsquo;s specific logistics fit electrification precisely, how the charging works at Kenyan batching plants, and what the TCO looks like against the diesel fleet.</p>

<h2>The Programme&rsquo;s Logistics, Mapped</h2>
<p>Affordable-housing concrete logistics in Nairobi have a distinctive shape. The batching plants cluster along the industrial corridors &mdash; Mombasa Road, Thika Road, Athi River, Ruiru &mdash; and the housing sites sit 15-45 km away across the metro. A mixer&rsquo;s day is 6-10 cycles of 30-90 km round trip, totalling 200-350 km at the upper end, with 40-60% of engine hours spent in traffic queues and on-site standby. The TZ8J&rsquo;s 350 kWh CATL LFP pack covers 220-280 km of loaded mixer duty &mdash; a full day for most plants, with a midday top-up absorbing peak programmes. Critically, the duty is depot-based: every truck returns to the batching plant nightly, so the entire fleet charges at infrastructure the operator already controls.</p>
<p>Nairobi&rsquo;s congestion, usually a curse, improves the electric case. A diesel mixer in two-hour traffic burns 3-4 litres hourly to turn the drum and idle; the TZ8J&rsquo;s independent electric drum drive turns at constant speed drawing 3-5 kW, and the traction system consumes nothing at standstill. In severe traffic, the electric mixer&rsquo;s relative advantage grows &mdash; and Nairobi traffic is severe.</p>

<h2>TZ8J Specification for Housing-Programme Duty</h2>
<table style="width:100%;border-collapse:collapse;margin:20px 0;" border="1" cellpadding="8">
<tr style="background:#006341;color:#fff;"><th style="padding:8px;text-align:left;">Parameter</th><th style="padding:8px;text-align:left;">TZ8J 8x4 Electric Mixer</th></tr>
<tr><td style="padding:8px;">Drum capacity</td><td style="padding:8px;">8-10 m&sup3; rated mixing volume</td></tr>
<tr><td style="padding:8px;">Battery</td><td style="padding:8px;">350 kWh CATL LFP, liquid-cooled</td></tr>
<tr><td style="padding:8px;">Traction motor</td><td style="padding:8px;">LvKong 360 kW peak / 2,400 Nm</td></tr>
<tr><td style="padding:8px;">Drum drive</td><td style="padding:8px;">independent electric, constant-speed control</td></tr>
<tr><td style="padding:8px;">Range (loaded, urban cycles)</td><td style="padding:8px;">220-280 km</td></tr>
<tr><td style="padding:8px;">DC charge 20-80%</td><td style="padding:8px;">~50 min at 240 kW</td></tr>
<tr><td style="padding:8px;">Gradeability</td><td style="padding:8px;">&ge;30% &mdash; site access ramps loaded</td></tr>
<tr><td style="padding:8px;">FOB price band</td><td style="padding:8px;">US$108,000-128,000</td></tr>
</table>
<p>Site access deserves a note because affordable-housing sites are not gentle: temporary ramps, unmade ground, and tight pours in occupied neighbourhoods. The TZ8J&rsquo;s electric drivetrain delivers full torque from standstill on loose ramps &mdash; no clutch slip, no wheelspin drama &mdash; and the near-silent operation changes the site&rsquo;s relationship with its neighbours. Housing projects sit inside communities, and the mixer that arrives without a diesel roar at 6 am is the one the ward administrator hears fewer complaints about. Several Nairobi plants already market quieter logistics as part of their tender story; electrification makes it structural.</p>

<h2>TCO at Kenyan Prices</h2>
<p>A diesel 8x4 mixer on Nairobi housing duty burns 0.75-0.90 L/km equivalent including drum and queue load; at US$1.45/L, US$1.10-1.30 per kilometre. The TZ8J consumes 1.7-2.0 kWh/km all-in; at KPLC industrial tariffs around US$0.14-0.16/kWh &mdash; or the off-peak rate near US$0.10 &mdash; US$0.20-0.30 per kilometre. On 250 km daily, 290 operating days, the annual energy saving per truck runs US$65,000-72,000 at grid tariffs. Read that again: Kenyan diesel prices make mixer electrification one of the strongest TCO cases in our entire portfolio. Maintenance adds US$7,000-10,000 annually. Payback against the purchase premium: 14-20 months. The 8-year battery warranty outlasts the payback by a factor of five.</p>
<ul>
<li><strong>Energy per km:</strong> US$1.20 diesel vs US$0.25 electric &mdash; ~79% lower</li>
<li><strong>Annual saving per truck:</strong> US$70,000+ combined at Kenyan fuel prices</li>
<li><strong>Payback:</strong> 14-20 months on housing-programme utilisation</li>
<li><strong>Queue cost:</strong> 40-60% of diesel engine-hours are queue/standby &mdash; eliminated</li>
<li><strong>Community noise:</strong> near-silent pours in residential districts</li>
</ul>

<h2>Charging at the Plant</h2>
<p>Kenyan batching plants are well-positioned for fleet charging: they are industrial power customers already, typically on 415 V three-phase with medium-voltage service available. A 12-15 truck TZ8J fleet needs two 240 kW DC chargers plus managed overnight AC &mdash; an 800 kVA-1 MVA service upgrade that KPLC processes routinely for industrial customers. The pour calendar sets the charge schedule: full charges overnight at off-peak rates, rotation charging during the midday batching trough, and the load-management controller holding site demand under contract. Kenya&rsquo;s grid is 85%+ renewable (geothermal, hydro, wind), which means the concrete&rsquo;s embodied emissions drop materially &mdash; a metric the programme&rsquo;s international financiers increasingly ask about, and a tender differentiator for the plants that can document it.</p>

<h2>Import and Support</h2>
<p>Trucks enter through Mombasa with 30-36 day sailings from China; we deliver with English documentation, UN R100 certification and the fleet parts package, and Kenya&rsquo;s duty treatment of electric vehicles &mdash; materially advantaged under the current finance framework &mdash; keeps landed cost sharp. Nairobi-based support includes commissioning through the first pour season, an extended parts kit, CATL module stock at 10-14 days, and telemetry monitoring of every truck. Buyers can find the full market context on our <a href="../markets/kenya.html">Kenya market page</a>, and regional operators will recognise the same platform&rsquo;s East African commercial-concrete deployments from Kampala to Dar es Salaam.</p>

<h2>The Tender Logic</h2>
<p>The Affordable Housing Programme&rsquo;s batching contractors compete on delivered cost per cubic metre, and the mixer fleet is the largest variable in that cost after cement itself. A plant running electric mixers at a 75-80% energy saving per kilometre holds a structural cost advantage on every pour &mdash; plus the documented-emissions story the programme&rsquo;s financiers want, and the community-relations benefit of quiet trucks. Kenya&rsquo;s diesel price is not coming down and its grid is not getting dirtier. The plants that electrify their Nairobi fleets first will set the cost benchmark for the programme&rsquo;s next decade of contracts.</p>
'''))

# ---------------------------------------------------------------- 31
ARTICLES.append(dict(
f='te8p-tanzania-sgr-heavy-haul-electric',
t='Tanzania&rsquo;s SGR Build-Out: TE8P Electric Heavy-Haul Tractors for Railway Construction Logistics',
d='Tanzania&rsquo;s Standard Gauge Railway construction moves transformers, girders and plant on heavy-haul routes. TE8P 120t electric tractor economics for SGR logistics inside.',
k='TE8P electric tractor, EV truck Tanzania, electric heavy haul truck SGR, electric tractor 120 ton, Dongfeng electric truck, heavy haulage EV truck Africa, transformer transport electric',
img='models/p12_00.jpg',
alt='Dongfeng TE8P electric heavy haul tractor moving railway equipment in Tanzania, EV truck for SGR construction',
net='qyc',
body='''
<p>Tanzania&rsquo;s Standard Gauge Railway is the country&rsquo;s largest infrastructure programme in a generation &mdash; over 1,200 km of new line from Dar es Salaam to Mwanza and beyond &mdash; and building a railway consumes heavy haulage at industrial scale: transformers and switchgear to substation sites, precast girders and track panels to laying fronts, crushers and batching plants leapfrogging along the corridor. That freight moves on escorted multi-axle combinations at 60-120 tonnes GCW, on routes that repeat weekly along the same corridor. This article examines the <a href="../products/models/te8p-electric-tractor.html">Dongfeng TE8P electric heavy-haul tractor</a> for SGR-scale logistics &mdash; a niche where this EV truck platform&rsquo;s specific strengths (huge torque, depot-based cycles, regeneration on escarpment descents) align almost perfectly with the duty.</p>

<h2>Heavy Haulage&rsquo;s Electric Logic</h2>
<p>Heavy haulage surprises people as an electrification candidate, but the duty cycle argues for it. First, routes repeat: the corridor from Dar port to the current laying front runs the same roads weekly for months, so charging nodes at fixed points serve the whole programme. Second, speeds are low &mdash; 40-60 km/h escorted &mdash; where electric drivetrains are most efficient. Third, the loads are the heaviest torque demands in road transport, and the electric motor&rsquo;s full-torque-from-zero character is precisely what pulling 100+ tonnes up a 6% grade requires; the TE8P&rsquo;s 510 kW LvKong drive delivers it without a gearbox&rsquo;s heat and slip. Fourth, the return legs are empty or light &mdash; and the descents that punish diesel retarders return 20-28% of cycle energy through regeneration.</p>

<h2>TE8P Heavy-Haul Specification</h2>
<table style="width:100%;border-collapse:collapse;margin:20px 0;" border="1" cellpadding="8">
<tr style="background:#006341;color:#fff;"><th style="padding:8px;text-align:left;">Parameter</th><th style="padding:8px;text-align:left;">TE8P 6x4 Electric Heavy-Haul Tractor</th></tr>
<tr><td style="padding:8px;">GCW rating</td><td style="padding:8px;">up to 120 t (multi-axle combinations)</td></tr>
<tr><td style="padding:8px;">Battery</td><td style="padding:8px;">600 kWh CATL LFP, liquid-cooled</td></tr>
<tr><td style="padding:8px;">Drive</td><td style="padding:8px;">LvKong 510 kW peak / 4,200 Nm at wheels via reduction</td></tr>
<tr><td style="padding:8px;">Range at 80-100 t GCW</td><td style="padding:8px;">180-240 km per charge</td></tr>
<tr><td style="padding:8px;">Fast charge</td><td style="padding:8px;">360-500 kW DC, 20-80% ~70 min</td></tr>
<tr><td style="padding:8px;">Gradeability at 100 t</td><td style="padding:8px;">&ge;10% sustained</td></tr>
<tr><td style="padding:8px;">Battery warranty</td><td style="padding:8px;">8 years / 4,500 cycles to 70% SOH</td></tr>
<tr><td style="padding:8px;">FOB price band</td><td style="padding:8px;">US$160,000-185,000</td></tr>
</table>
<p>The range figure shapes the operating model: heavy-haul days are short in distance (150-250 km is a full escorted day), so the tractor covers a day&rsquo;s work per charge, then charges overnight at the staging camp. For the escarpment sections &mdash; the corridor crosses the Rift Valley shoulders &mdash; the regeneration profile means a loaded westbound climb is partially refunded on every eastbound return. Camp power is already on site: construction camps run megawatt-scale generation for crushers and batching plants, and truck charging is a schedulable night load on infrastructure that exists for the programme anyway.</p>

<h2>TCO Against Diesel Heavy Haulage</h2>
<p>Diesel heavy-haul tractors at 80-120 t GCW burn 1.2-1.6 L/km; at Tanzanian prices around US$1.20-1.30/L, US$1.50-2.00 per kilometre. The TE8P consumes 2.6-3.2 kWh/km at these weights; at camp power costs of US$0.15-0.22/kWh (genset-augmented) or grid tariffs near US$0.10 where TANESCO medium voltage reaches, US$0.30-0.70 per kilometre. On 200 km daily, 280 operating days, the annual energy saving runs US$45,000-75,000 per tractor depending on power source. Maintenance is the second dividend: heavy-haul diesel drivetrains &mdash; engine, multi-speed transmission, retarder &mdash; are the most maintenance-intensive kit in road transport, and the electric drivetrain deletes nearly all of it; add US$15,000-25,000 annually. Payback against the premium: 24-36 months, inside a programme scheduled to run years longer.</p>
<ul>
<li><strong>Energy per km:</strong> US$1.50-2.00 diesel vs US$0.30-0.70 electric</li>
<li><strong>Annual saving per tractor:</strong> US$60,000-100,000 combined</li>
<li><strong>Torque delivery:</strong> full torque from standstill at 120 t GCW &mdash; no clutch, no gear-hunting</li>
<li><strong>Descent safety:</strong> regenerative retarding replaces faded service brakes on escarpment descents</li>
<li><strong>Camp synergy:</strong> charging rides on existing construction power infrastructure</li>
</ul>

<h2>The Programme Logistics Fit</h2>
<p>SGR construction logistics run on staging: materials consolidate at Dar port and Morogoro, move forward to camps, and distribute to the laying front. The electrification plan mirrors it: charging at the Dar consolidation depot, at the Morogoro mid-corridor camp, and at the advancing front camps (relocatable skid-mounted DC chargers that leapfrog with the programme). The TE8P&rsquo;s dual-gun 500 kW capability means a 70-minute turnaround even on the 600 kWh pack &mdash; matched to the escorted convoy&rsquo;s rest stops. For contractors running both heavy-haul and standard construction fleets on the programme, the same charging infrastructure serves the tippers and mixers &mdash; one energy system for the whole motorised fleet.</p>

<h2>Import and Regional Context</h2>
<p>Heavy tractors enter through Dar es Salaam with 32-38 day sailings from China; we deliver with English documentation, UN R100 certification, and the heavy-haul support package including escort-duty parts kits. Tanzania&rsquo;s treatment of electric vehicles carries duty advantages, and programme-linked procurement increasingly values emissions performance. Buyers can find the full operating context on our <a href="../markets/tanzania.html">Tanzania market page</a>, and contractors with multi-country infrastructure portfolios will recognise the same platform&rsquo;s deployments on mining heavy-haul across the region &mdash; the TE8P&rsquo;s 120 t GCW rating serves copper-belt and wind-farm logistics with identical architecture.</p>
<p>Support for programme duty is structured around the corridor: commissioning at the first camps, fly-in technical coverage tied to the convoy schedule, parts kits at the staging depots, and telemetry monitoring that tracks every tractor&rsquo;s pack health, consumption and location across the corridor. The drivetrain&rsquo;s service calendar &mdash; brakes, suspension, coolant &mdash; is a fraction of what a 120 t-rated diesel drivetrain demands, and on a programme where a stranded transformer load closes a road, availability is the whole business.</p>

<h2>The Strategic Read</h2>
<p>Africa&rsquo;s infrastructure decade is a heavy-haulage decade, and the contractors who win its margins will be those who cut the two costs that define the niche: fuel and drivetrain maintenance. The SGR corridor &mdash; fixed routes, camp power, repeating cycles &mdash; is as close to a designed-for-electric heavy-haul environment as the continent offers. The contractors who electrify their programme fleets convert that fit into a cost position their diesel competitors cannot tender against &mdash; and into a reference that wins the next corridor, and the one after that.</p>
'''))

# ---------------------------------------------------------------- 32
ARTICLES.append(dict(
f='kth1-pakistan-textile-cargo-electric-truck',
t='Faisalabad to Karachi: KTH1 Electric Cargo Trucks for Pakistan&rsquo;s Textile Corridor',
d='Pakistan&rsquo;s textile exports move from Faisalabad to Karachi on 1,100 km corridors. Where KTH1 electric cargo trucks fit the chain: port shuttles, city mills, TCO and charging.',
k='KTH1 electric cargo truck, EV truck Pakistan, electric truck Faisalabad, textile logistics electric truck, Dongfeng electric truck, electric cargo truck Karachi port',
img='models/p07_02.jpg',
alt='Dongfeng KTH1 electric cargo truck serving Pakistan textile corridor, EV truck for Faisalabad Karachi freight',
net='zhc',
body='''
<p>Pakistan&rsquo;s textile industry earns the country roughly US$15 billion a year in exports, and its logistics chain is a study in concentrated geography: spinning and weaving clustered in Faisalabad and the Punjab triangle, stitching and finishing in Karachi&rsquo;s industrial estates, and everything flowing to the world through Karachi&rsquo;s two ports. The long Punjab-to-port trunk haul is (for now) diesel territory &mdash; but the chain&rsquo;s two ends, the mill-district shuttles and the port-side distribution, are textbook electric duty. This article examines the <a href="../products/models/kth1-electric-cargo-truck.html">Dongfeng KTH1 electric cargo truck</a> in Pakistan&rsquo;s textile logistics: where this EV truck fits today, what it saves, and how the corridor electrifies in stages.</p>

<h2>Map the Chain, Find the Electric Segments</h2>
<p>Textile logistics break into four leg types, and their electrification readiness differs sharply. Mill-to-consolidation shuttles (Faisalabad&rsquo;s mills to the dry ports and CFS yards): 10-40 km, multi-drop, depot-based &mdash; electric-ready today. Karachi intra-city (Landhi, Korangi, SITE and Port Qasim industrial estates to the terminals): 15-50 km in severe congestion &mdash; electric-ready, with congestion actively improving the EV advantage. The 1,100 km Faisalabad-Karachi trunk: needs corridor charging that does not yet exist at truck power levels &mdash; a 2028+ conversation. And port-side drayage: ideal, as our terminal-tractor coverage shows. The KTH1&rsquo;s 240-280 km loaded range on its 350 kWh CATL pack covers every leg except the trunk with margin &mdash; which is exactly how corridor electrification begins everywhere: own the ends, extend as infrastructure follows.</p>

<h2>KTH1 Specification for Textile Duty</h2>
<table style="width:100%;border-collapse:collapse;margin:20px 0;" border="1" cellpadding="8">
<tr style="background:#006341;color:#fff;"><th style="padding:8px;text-align:left;">Parameter</th><th style="padding:8px;text-align:left;">KTH1 8x4 / 6x4 Electric Cargo Truck</th></tr>
<tr><td style="padding:8px;">GVW / payload</td><td style="padding:8px;">26-31 t / 16-20 t (high-cube box ideal for textiles)</td></tr>
<tr><td style="padding:8px;">Battery</td><td style="padding:8px;">350 kWh CATL LFP, liquid-cooled</td></tr>
<tr><td style="padding:8px;">Motor</td><td style="padding:8px;">LvKong 360 kW peak / 2,400 Nm</td></tr>
<tr><td style="padding:8px;">Range (loaded, urban/semi-urban)</td><td style="padding:8px;">240-280 km</td></tr>
<tr><td style="padding:8px;">DC charge 20-80%</td><td style="padding:8px;">~50 min at 240 kW</td></tr>
<tr><td style="padding:8px;">Body</td><td style="padding:8px;">high-cube dry box, garment-on-hanger option</td></tr>
<tr><td style="padding:8px;">Battery warranty</td><td style="padding:8px;">8 years / 4,500 cycles to 70% SOH</td></tr>
<tr><td style="padding:8px;">FOB price band</td><td style="padding:8px;">US$92,000-110,000</td></tr>
</table>
<p>Textile freight&rsquo;s defining property &mdash; it cubes out long before it weighs out &mdash; makes it ideal for electric trucks. Bales, cartons and garment racks fill a high-cube box at 8-12 tonnes, half the chassis payload rating, which means the battery weight penalty that exercises dense-freight operators simply does not apply. The KTH1 on textile duty runs at its efficiency optimum: moderate weight, urban speeds, regenerative braking harvesting the constant deceleration of Karachi and Faisalabad traffic. The garment-on-hanger body option &mdash; increasingly demanded by export buyers to cut creasing and handling &mdash; integrates electrically with the chassis (lighting, climate for sensitive loads) as a factory option.</p>

<h2>TCO at Pakistani Prices</h2>
<p>Pakistani diesel runs US$0.95-1.05 per litre; a 26-31 t cargo truck on urban textile duty burns 0.45-0.55 L/km &mdash; US$0.45-0.55 per kilometre. The KTH1 consumes 1.3-1.5 kWh/km on the same duty; at industrial tariffs around US$0.09-0.12/kWh, US$0.13-0.17 per kilometre &mdash; a 65-70% energy saving. On 4,000 km monthly, the energy saving alone is US$1,300-1,500 per truck; maintenance adds US$400-600 (no engine service calendar in an industry where diesel trucks idle half their hours in Karachi gridlock). Annual combined saving: US$20,000-25,000 per truck, against a purchase premium of US$30,000-40,000 &mdash; payback in 18-24 months. The export dimension strengthens the case: the industry&rsquo;s European and American buyers now audit scope-3 emissions, and a mill shipping in electric trucks documents a supply-chain advantage its competitors cannot.</p>
<ul>
<li><strong>Energy per km:</strong> US$0.50 diesel vs US$0.15 electric &mdash; ~70% lower</li>
<li><strong>Annual saving per truck:</strong> US$20,000-25,000 combined</li>
<li><strong>Payback:</strong> 18-24 months on urban mill-and-port duty</li>
<li><strong>Scope-3 dividend:</strong> documented zero-emission logistics for export buyer audits</li>
<li><strong>Payload reality:</strong> textiles cube out at 8-12 t &mdash; no battery-weight penalty</li>
</ul>

<h2>Charging in the Mill Districts</h2>
<p>Pakistan&rsquo;s textile belt is industrially powered &mdash; the mills themselves are among the country&rsquo;s largest electricity consumers, many with captive generation from years of grid unreliability. That captive capacity is the charging answer: a mill running its own gas or solar-hybrid generation charges its truck fleet at its own marginal cost, behind the grid entirely. A 10-15 truck KTH1 fleet needs one to two 240 kW DC chargers plus overnight AC &mdash; an 800 kVA service class trivially within mill-scale electrical rooms. Faisalabad&rsquo;s M-3 industrial estate and Karachi&rsquo;s export processing zones both have the medium-voltage infrastructure for depot charging; the EPZ context adds duty simplifications for the charging hardware itself.</p>
<p>Solar deserves its line: Punjab&rsquo;s 5.0-5.5 peak sun hours and the mills&rsquo; vast roofscapes make solar-plus-charging the natural architecture. Several Faisalabad groups already run megawatt-scale rooftop solar for process power; adding truck charging to that estate is an incremental investment against the largest fuel bill the group pays.</p>

<h2>Import and Support</h2>
<p>Trucks enter through Karachi with 25-32 day sailings from China; we deliver with English/Urdu-accessible documentation, UN R100 certification and the fleet parts package. Pakistan&rsquo;s EV policy framework extends duty advantages to electric commercial vehicles, and the customs process for documented industrial imports through Karachi is established. Buyers can find the full market context on our <a href="../markets/pakistan.html">Pakistan market page</a>. Support for textile-belt fleets includes commissioning at the mill depots, extended parts kits, CATL module stock at 12-16 days, and telemetry monitoring &mdash; the same architecture running in the region&rsquo;s other industrial corridors.</p>

<h2>The Staged Corridor Vision</h2>
<p>The textile chain&rsquo;s electrification will proceed exactly as it has elsewhere: urban ends first (mill shuttles, Karachi distribution, port drayage), then the trunk as corridor charging materialises along the M-3/M-9. The mill groups that electrify their urban fleets now bank the cost savings and the scope-3 documentation immediately, build the operating competence the trunk phase will need, and position for the day &mdash; visible on the policy horizon &mdash; when export buyers stop asking whether logistics emissions are documented and start requiring that they be low. Pakistan&rsquo;s textile competitiveness has always rested on cost discipline; the electric fleet is the next chapter of the same discipline, written in the industry&rsquo;s own backyard.</p>
'''))

for a in ARTICLES:
    html = build(a)
    path = os.path.join(ROOT, 'blog', a['f'] + '.html')
    with open(path, 'w', encoding='utf-8') as fh:
        fh.write(html)
    words = len(re.sub(r'<[^>]+>', ' ', a['body']).split())
    print('%-58s %5d words' % (a['f'], words))
print('done batch4:', len(ARTICLES))
