# -*- coding: utf-8 -*-
"""Run 14 batch 5: 8 articles (model angles + comparison + policy + 2 GEO buyer-decision)."""
import re, os
from _gen_run14_b1 import build

ROOT = os.path.dirname(os.path.abspath(__file__))
ARTICLES = []

# ---------------------------------------------------------------- 33
ARTICLES.append(dict(
f='kt7a-qatar-lusail-electric-washing-truck',
t='Lusail City, Qatar: KT7A Electric Washing Trucks for a City Built From Scratch',
d='Lusail is Qatar&rsquo;s purpose-built smart city and its street-washing fleets fit electrification perfectly. KT7A electric washing truck specs, water economy and TCO inside.',
k='KT7A electric washing truck, EV truck Qatar, electric washing truck Lusail, electric street washing truck, Dongfeng electric truck, municipal EV truck Gulf',
img='models/p09_00.jpg',
alt='Dongfeng KT7A electric washing truck cleaning Lusail boulevards, EV truck for Qatar municipal fleets',
net='gen',
body='''
<p>Lusail is the city Qatar built for the world to see: 38 km&sup2; of master-planned districts north of Doha, with boulevards, marinas and public realm maintained to a standard that requires daily mechanical washing across hundreds of lane-kilometres. The fleets doing that work &mdash; water tankers with spray bars and high-pressure lances &mdash; run fixed night and early-morning circuits from municipal depots, returning to base after every shift. It is municipal duty at its most electrifiable, in a country with cheap power, declared sustainability goals, and procurement that increasingly scores emissions. This article examines the <a href="../products/models/kt7a-electric-washing-truck.html">Dongfeng KT7A electric washing truck</a> in Lusail-scale service.</p>

<h2>The Washing Duty Cycle, Quantified</h2>
<p>A street-washing truck&rsquo;s day splits into two energy consumers: the traction drive covering the circuit (80-140 km per shift on Lusail&rsquo;s district loops), and the water system &mdash; pumps driving the spray bar and lance at 15-25 kW during active washing. On a diesel truck, both draw from one engine that idles through the working cycle&rsquo;s frequent stops; on the KT7A, an electric PTO drives the pumps directly from the 282 kWh CATL LFP pack, and the traction system draws nothing at standstill. The measured result on Gulf municipal duty: 5-7 hours of active washing per charge with the standard tank, or a full double-shift with a 45-minute midday DC charge. Range has never been the constraint on this duty; water capacity is &mdash; and that is true for the diesel variant too.</p>

<h2>KT7A Specification for Gulf Municipal Service</h2>
<table style="width:100%;border-collapse:collapse;margin:20px 0;" border="1" cellpadding="8">
<tr style="background:#006341;color:#fff;"><th style="padding:8px;text-align:left;">Parameter</th><th style="padding:8px;text-align:left;">KT7A Electric Washing Truck</th></tr>
<tr><td style="padding:8px;">Water tank</td><td style="padding:8px;">10-14 m&sup3; stainless, anti-surge baffled</td></tr>
<tr><td style="padding:8px;">Battery</td><td style="padding:8px;">282 kWh CATL LFP, liquid-cooled</td></tr>
<tr><td style="padding:8px;">Traction motor</td><td style="padding:8px;">LvKong 250 kW peak / 2,200 Nm</td></tr>
<tr><td style="padding:8px;">Pump drive</td><td style="padding:8px;">electric PTO, 15-25 kW, variable pressure</td></tr>
<tr><td style="padding:8px;">Active washing per charge</td><td style="padding:8px;">5-7 hours</td></tr>
<tr><td style="padding:8px;">DC charge 20-80%</td><td style="padding:8px;">~45 min at 240 kW</td></tr>
<tr><td style="padding:8px;">Ambient rating</td><td style="padding:8px;">to +50&deg;C, liquid-cooled pack</td></tr>
<tr><td style="padding:8px;">FOB price band</td><td style="padding:8px;">US$88,000-105,000</td></tr>
</table>
<p>The +50&deg;C rating carries special weight in Qatar, where summer night temperatures stay above 35&deg;C and the trucks work hardest in the pre-dawn hours that are still brutally hot. The liquid-cooled pack holds its thermal band through a Gulf August; the cab air conditioning runs at full capacity at standstill without burning diesel; and the pump system&rsquo;s electric drive holds constant pressure regardless of engine speed &mdash; a wash-quality consistency advantage the hydraulic-drive diesel cannot match at idle.</p>

<h2>Economics at Qatari Energy Prices</h2>
<p>Qatar&rsquo;s electricity tariff for municipal and industrial consumers runs around US$0.04-0.06/kWh &mdash; among the world&rsquo;s lowest &mdash; against diesel at US$0.55-0.65/L equivalent. A diesel washing truck consumes 35-45 L per shift on combined traction-and-pump duty: US$22-28 per shift. The KT7A consumes 90-120 kWh for the same shift: US$4-7. The energy saving exceeds 75%, and on a two-shift municipal calendar it compounds to US$13,000-18,000 per truck annually &mdash; before maintenance, where the deletion of engine, transmission and PTO hydraulics adds US$4,000-6,000 more. Payback against the purchase premium runs 30-42 months on a municipal replacement cycle of 8-10 years &mdash; comfortably positive, and that is before scoring the procurement points that zero-emission operation earns under Qatar&rsquo;s tender frameworks.</p>
<ul>
<li><strong>Energy per shift:</strong> US$22-28 diesel vs US$4-7 electric &mdash; 75%+ lower</li>
<li><strong>Annual saving per truck:</strong> US$17,000-24,000 combined</li>
<li><strong>Noise:</strong> pre-dawn washing in residential districts without the diesel note &mdash; a live issue in Lusail&rsquo;s occupied zones</li>
<li><strong>Emissions:</strong> zero at point of use, aligned with Qatar National Vision 2030 procurement scoring</li>
</ul>

<h2>Depot Charging in a Planned City</h2>
<p>Lusail&rsquo;s advantage is that everything was designed recently: the municipal depots have modern medium-voltage service, and a ten-truck KT7A fleet&rsquo;s 400-500 kVA managed-charging requirement is a routine connection. The fleet&rsquo;s rhythm &mdash; trucks out 21:00-05:00, parked 06:00-20:00 &mdash; inverts the solar problem that complicates other fleets: daytime parking means daytime charging, and a depot solar canopy (Qatar&rsquo;s irradiance is exceptional) directly serves the fleet&rsquo;s actual charging window at peak output. Few municipal fleets anywhere align this well with solar; Lusail&rsquo;s washing fleet charges when the sun shines because its working hours are dark.</p>

<h2>Procurement and Regional Context</h2>
<p>Qatar&rsquo;s municipal procurement runs through Ashghal and the relevant authorities with documentation requirements we supply as standard: Arabic/English technical files, UN R100 battery certification, and the conformity package. Trucks ship to Hamad Port in 26-32 days from China. Regional buyers can find the Gulf operating context on our <a href="../markets/qatar.html">Qatar market page</a>, and municipal procurement teams evaluating sanitation-fleet electrification across the GCC will recognise the same platform&rsquo;s deployments from Dubai&rsquo;s street-cleaning programme to Kuwaiti municipal fleets &mdash; the KT7A works Gulf municipal duty with common support infrastructure.</p>
<p>Support for municipal fleets is structured for procurement accountability: commissioning and operator training at the depot, preventive-maintenance scheduling aligned to the municipal CMMS, parts kits sized for fleet self-sufficiency, and telemetry monitoring that reports availability and energy cost in the format municipal audits require. The drivetrain&rsquo;s service calendar &mdash; brakes, coolant, pump wear parts &mdash; is a fraction of the diesel washing truck&rsquo;s engine-and-hydraulics load.</p>

<h2>The Bottom Line for Gulf Municipalities</h2>
<p>Lusail&rsquo;s maintenance standard is not optional &mdash; it is the city&rsquo;s identity &mdash; and the washing fleets delivering it will run every night for decades. Electrifying them converts a fixed duty cycle on a planned grid into a 75% energy saving, a quieter city at 3 am, and procurement scores that align with the country&rsquo;s declared direction. For a city built from scratch to showcase the future, washing its streets with last century&rsquo;s drivetrain is the anomaly; the KT7A simply corrects it.</p>
'''))

# ---------------------------------------------------------------- 34
ARTICLES.append(dict(
f='kt3e-vietnam-heritage-cities-electric-sweeper',
t='Hoi An, Hue and Hanoi&rsquo;s Old Quarter: KT3E Electric Sweepers for Vietnam&rsquo;s Heritage Cities',
d='Vietnam&rsquo;s heritage cities need clean streets and clean air without diesel noise and fumes. KT3E electric sweeper specs, TCO and municipal procurement guide inside.',
k='KT3E electric sweeper, EV truck Vietnam, electric road sweeper Hoi An, electric sweeper heritage city, Dongfeng electric truck, municipal EV truck Southeast Asia',
img='models/p10_00.jpg',
alt='Dongfeng KT3E electric road sweeper in a Vietnamese heritage city, EV truck for municipal cleaning fleets',
net='gen',
body='''
<p>Vietnam&rsquo;s heritage cities face a maintenance paradox: the streets that draw millions of tourists &mdash; Hoi An&rsquo;s lantern-lit old town, Hue&rsquo;s citadel districts, Hanoi&rsquo;s Old Quarter, Hoi An&rsquo;s riverside &mdash; must be cleaned daily, but the diesel sweepers doing the work pump noise and exhaust into exactly the atmosphere the tourists come for. Several of these districts already restrict combustion vehicles by hour or zone, and the municipal operators are caught between cleanliness mandates and heritage protection. This article examines the <a href="../products/models/kt3e-electric-garbage-truck.html">Dongfeng KT3E electric sweeper</a> for Vietnam&rsquo;s heritage-city fleets: the specification, the night-work economics, and the procurement path under Vietnam&rsquo;s municipal frameworks.</p>

<h2>Heritage-City Sweeping: The Duty Profile</h2>
<p>Heritage-district sweeping is compact and intensive: 20-40 km of kerb line per shift, worked at 4-10 km/h with constant stop-start, through the early-morning hours before pedestrian zones open. The diesel sweeper does this with its engine screaming at working rpm to drive suction and brushes &mdash; 70-80 dB of noise at 4 am, and exhaust settling into shopfronts that open at seven. The KT3E does the identical work electrically: traction from the LvKong motor, suction fan and brushes from an electric auxiliary drive, both fed by a 140-180 kWh CATL LFP pack delivering a full 6-8 hour sweeping shift per charge. The noise signature drops to the brushes and the airflow &mdash; the sound of cleaning rather than the sound of an engine &mdash; and the exhaust simply does not exist.</p>

<h2>KT3E Specification for Heritage Duty</h2>
<table style="width:100%;border-collapse:collapse;margin:20px 0;" border="1" cellpadding="8">
<tr style="background:#006341;color:#fff;"><th style="padding:8px;text-align:left;">Parameter</th><th style="padding:8px;text-align:left;">KT3E Electric Sweeper</th></tr>
<tr><td style="padding:8px;">Sweeping width / hopper</td><td style="padding:8px;">2.2-2.4 m / 4-5 m&sup3; stainless hopper</td></tr>
<tr><td style="padding:8px;">Battery</td><td style="padding:8px;">140-180 kWh CATL LFP</td></tr>
<tr><td style="padding:8px;">Traction motor</td><td style="padding:8px;">LvKong 120-150 kW peak</td></tr>
<tr><td style="padding:8px;">Auxiliary drive</td><td style="padding:8px;">electric fan + brush drives, water recirculation option</td></tr>
<tr><td style="padding:8px;">Shift endurance</td><td style="padding:8px;">6-8 h active sweeping</td></tr>
<tr><td style="padding:8px;">Noise at working speed</td><td style="padding:8px;">~62-65 dB (vs 75-80 diesel)</td></tr>
<tr><td style="padding:8px;">Turning circle</td><td style="padding:8px;">~10.5 m &mdash; old-quarter lane access</td></tr>
<tr><td style="padding:8px;">FOB price band</td><td style="padding:8px;">US$72,000-88,000</td></tr>
</table>
<p>Three specification points matter for Vietnam specifically. The turning circle and compact overhangs fit the geometry of Hoi An&rsquo;s and Hanoi&rsquo;s old lanes, where full-size sweepers simply cannot work. The water-recirculation option extends effective shift length in dusty season and suits Vietnam&rsquo;s monsoon-dry cycle. And the liquid-cooled pack handles the tropical thermal load &mdash; Hue and Da Nang touch 38-40&deg;C in season, and night humidity stays extreme &mdash; without the derating that air-cooled designs suffer.</p>

<h2>Economics for Municipal Operators</h2>
<p>Vietnamese municipal diesel costs run US$0.85-0.95/L; a sweeper on heritage duty burns 28-38 L per shift &mdash; US$26-34. The KT3E consumes 60-80 kWh for the same shift; at EVN industrial tariffs of US$0.09-0.11/kWh, US$6-8. Annual energy saving per truck on a 340-shift municipal calendar: US$7,000-9,000. Maintenance &mdash; no engine, no hydraulic-drive system, brushes and filters common to both &mdash; adds US$2,500-3,500. Payback against the purchase premium runs 4-6 years on energy-plus-maintenance alone &mdash; but that arithmetic misses the real procurement driver: in heritage zones with combustion restrictions, the electric sweeper is increasingly the only machine allowed to work the prime early-morning hours. The diesel alternative is not a cheaper machine; it is a banned one.</p>
<ul>
<li><strong>Energy per shift:</strong> US$26-34 diesel vs US$6-8 electric</li>
<li><strong>Noise:</strong> 10-15 dB lower &mdash; the difference between &ldquo;tolerated at 4 am&rdquo; and not</li>
<li><strong>Access:</strong> zero-emission status satisfies pedestrian-zone and heritage-hour restrictions</li>
<li><strong>Image:</strong> the sweeper working a UNESCO street is itself a tourism photograph &mdash; cities notice</li>
</ul>

<h2>Depot Charging in Compact Municipal Yards</h2>
<p>Vietnamese municipal depots are space-constrained but electrically adequate: a five-to-ten sweeper fleet needs 250-400 kVA of managed charging, a standard industrial connection for EVN. The night-work fleet&rsquo;s daytime parking window aligns with Vietnam&rsquo;s growing solar generation &mdash; several provincial cities now offer municipal solar programmes that suit depot canopies exactly. Charging is overnight-in-name-only here: the fleet works 02:00-08:00 and charges 09:00-20:00, straight through the solar peak. Heritage-city fleets may be the best-aligned solar-charging use case in the entire municipal segment.</p>

<h2>Procurement Path</h2>
<p>Municipal vehicle procurement in Vietnam runs through the provincial people&rsquo;s committees and the urban environment companies (URENCO and peers), with documentation requirements we supply complete: Vietnamese-language technical files, UN R100 battery certification, and the conformity package for the national registration system. Trucks ship Haiphong or Cat Lai in 18-25 days from southern Chinese ports. Buyers can find the full market context on our <a href="../markets/vietnam.html">Vietnam market page</a>, including the Decision 876 framework that is pushing municipal fleet electrification nationally. Support includes commissioning and operator training at the depot, parts kits sized for municipal self-sufficiency, and telemetry reporting formatted for municipal audit.</p>

<h2>The Heritage Logic</h2>
<p>Vietnam&rsquo;s heritage cities are national assets whose value is the atmosphere itself &mdash; and atmosphere is precisely what diesel sweepers destroy and electric ones preserve. The KT3E&rsquo;s case here is not a marginal TCO argument; it is that the electric machine does the same work while removing the two things &mdash; noise and fumes &mdash; that heritage districts cannot tolerate. As combustion restrictions tighten from Hoi An outward, the municipal operators who electrify first stop negotiating with the restrictions and start setting the standard the restrictions are written around.</p>
'''))

# ---------------------------------------------------------------- 35
ARTICLES.append(dict(
f='te9l-mexico-bajio-electric-corridor',
t='Mexico&rsquo;s Baj&iacute;o Corridor: TE9L Electric Tractors on the Quer&eacute;taro&ndash;Le&oacute;n&ndash;Silao Triangle',
d='Mexico&rsquo;s Bajio automotive belt runs dense short-haul freight between plants and ports. TE9L electric tractor economics on the Bajio triangle: range, charging, TCO.',
k='TE9L electric tractor, EV truck Mexico, electric tractor Bajio, electric truck Queretaro Leon, Dongfeng electric truck, nearshoring EV truck Mexico, automotive logistics electric',
img='models/p13_00.jpg',
alt='Dongfeng TE9L electric tractor on the Bajio corridor in Mexico, EV truck for automotive plant logistics',
net='qyc',
body='''
<p>The Baj&iacute;o &mdash; the Quer&eacute;taro&ndash;Le&oacute;n&ndash;Silao&ndash;Aguascalientes triangle &mdash; is the engine of Mexico&rsquo;s nearshoring boom: GM, Toyota, BMW, and a tiered supplier universe shipping components and finished vehicles between plants, logistics parks and the Manzanillo and L&aacute;zaro C&aacute;rdenas ports. The freight is dense, the distances are short (plant-to-plant 30-120 km, plant-to-port 350-450 km), the schedules are JIT-critical, and the customers &mdash; global OEMs with science-based carbon targets &mdash; now audit scope-3 logistics emissions. This article examines the <a href="../products/models/te9l-electric-tractor.html">Dongfeng TE9L electric tractor</a> on Baj&iacute;o duty: why the triangle&rsquo;s geometry fits the truck&rsquo;s 600 kWh pack, how charging works at plant logistics parks, and what the TCO looks like at Mexican energy prices.</p>

<h2>The Triangle&rsquo;s Geometry Meets the Battery</h2>
<p>The Baj&iacute;o&rsquo;s freight pattern is an electric truck&rsquo;s design brief. Intra-triangle shuttle runs (Quer&eacute;taro-Silao 120 km, Le&oacute;n-Aguascalientes 130 km, plant-to-railhead 20-60 km) are one-charge round trips for the TE9L&rsquo;s 350-420 km loaded range. The port runs to Manzanillo (430 km from Le&oacute;n) need one 45-60 minute charge en route or at destination &mdash; matched to the driver&rsquo;s rest cycle on a 9-10 hour day. And the entire pattern is depot-anchored: tractors sleep at the plant logistics parks where the freight starts, so charging lands where industrial power already exists. The 600 kWh CATL LFP pack &mdash; among the largest fitted to a road tractor &mdash; is the specification that makes the triangle charger-light: fleets run the dense intra-triangle work on overnight charging alone.</p>

<h2>TE9L Specification for Baj&iacute;o Duty</h2>
<table style="width:100%;border-collapse:collapse;margin:20px 0;" border="1" cellpadding="8">
<tr style="background:#006341;color:#fff;"><th style="padding:8px;text-align:left;">Parameter</th><th style="padding:8px;text-align:left;">TE9L 6x4 Electric Tractor</th></tr>
<tr><td style="padding:8px;">GCW rating</td><td style="padding:8px;">49 t</td></tr>
<tr><td style="padding:8px;">Battery</td><td style="padding:8px;">600 kWh CATL LFP, liquid-cooled</td></tr>
<tr><td style="padding:8px;">Motor</td><td style="padding:8px;">LvKong 510 kW peak / 2,800 Nm</td></tr>
<tr><td style="padding:8px;">Range at 40 t (highway)</td><td style="padding:8px;">350-420 km</td></tr>
<tr><td style="padding:8px;">Fast charge</td><td style="padding:8px;">360-500 kW DC, 20-80% ~60 min</td></tr>
<tr><td style="padding:8px;">Altitude performance</td><td style="padding:8px;">no power derate at 1,800-2,000 m (Baj&iacute;o plateau)</td></tr>
<tr><td style="padding:8px;">Battery warranty</td><td style="padding:8px;">8 years / 4,500 cycles to 70% SOH</td></tr>
<tr><td style="padding:8px;">FOB price band</td><td style="padding:8px;">US$145,000-172,000</td></tr>
</table>
<p>The altitude line deserves emphasis: the Baj&iacute;o sits at 1,800-2,000 metres, where a diesel engine loses 15-18% of its power to thin air &mdash; permanently, on every kilometre. The electric drivetrain delivers identical torque at 2,000 m as at sea level, which means the TE9L&rsquo;s advantage over diesel widens on the plateau rather than narrowing. Regenerative braking recovers 18-24% of energy on the rolling terrain between the triangle&rsquo;s cities, and the full-torque-from-zero character suits the loaded pull-aways from plant docks that define the duty.</p>

<h2>TCO at Mexican Energy Prices</h2>
<p>Mexican diesel runs US$1.05-1.20/L; a 40 t combination on Baj&iacute;o highway duty burns 0.42-0.50 L/km &mdash; US$0.47-0.57 per kilometre. The TE9L consumes 1.4-1.6 kWh/km at 40 t; at CFE industrial tariffs of US$0.10-0.14/kWh, US$0.15-0.21 per kilometre &mdash; and the Baj&iacute;o&rsquo;s industrial parks increasingly offer solar-PPA power at US$0.06-0.09, pushing electric energy toward US$0.10/km. On 90,000 km annually (typical shuttle utilisation), the energy saving runs US$24,000-38,000 per tractor. Maintenance adds US$8,000-12,000. Against the purchase premium over a diesel tractor &mdash; and note the comparison is against US-market-priced diesels in Mexico &mdash; payback lands at 30-42 months, shortening sharply on solar-PPA power and on the higher-utilisation JIT shuttles. The scope-3 documentation the fleet generates is increasingly a contract requirement with the OEM customers, not a bonus.</p>
<ul>
<li><strong>Energy per km:</strong> US$0.52 diesel vs US$0.10-0.21 electric</li>
<li><strong>Annual saving per tractor:</strong> US$32,000-50,000 combined</li>
<li><strong>Altitude advantage:</strong> zero power loss at 2,000 m vs diesel&rsquo;s 15-18% derate</li>
<li><strong>Scope-3 compliance:</strong> documented zero-emission logistics for OEM audits</li>
</ul>

<h2>Charging at the Logistics Parks</h2>
<p>The Baj&iacute;o&rsquo;s industrial parks are among Mexico&rsquo;s best-powered: medium-voltage service, and in several parks private solar-PPA arrangements already serving the plants. A 10-15 tractor TE9L fleet needs two 360 kW DC chargers plus managed overnight capacity &mdash; a 1.5-2 MVA service class within the parks&rsquo; infrastructure envelope. The charge schedule follows the JIT calendar: overnight full charges, rotation top-ups during the mid-shift dock windows. Mexico&rsquo;s federal fast-charging corridor programme is extending truck-capable charging along the 45D/57D axes, which progressively unlocks the port runs for single-charge-plus-top-up operation &mdash; the triangle electrifies first, and the corridor follows on the public build-out.</p>

<h2>Import and Market Context</h2>
<p>Trucks enter through Manzanillo or Veracruz with 28-34 day sailings from China; we deliver with Spanish documentation, NOM homologation support, UN R100 certification and the fleet parts package. Mexico&rsquo;s treatment of electric trucks includes duty advantages, and several Baj&iacute;o states add registration and circulation incentives. Buyers can find the full market context on our <a href="../markets/mexico.html">Mexico market page</a>. Support for Baj&iacute;o fleets includes commissioning at the logistics parks, extended parts kits, CATL module stock via North American logistics at 10-14 days, and telemetry monitoring that reports in the formats OEM logistics audits require.</p>

<h2>The Nearshoring Logic</h2>
<p>Nearshoring is a carbon story as much as a cost story: the OEMs moving production to the Baj&iacute;o are simultaneously committed to decarbonising its logistics, and the 3PLs serving them will be scored on it. The fleet that electrifies its Baj&iacute;o shuttles converts the triangle&rsquo;s geometry into a cost advantage, its industrial-park power into an energy advantage, and its OEM relationships into preferred-supplier status. The freight will move regardless; the only question is whether it moves at diesel cost with diesel&rsquo;s emissions profile, or at the plateau-proof, audit-ready economics the electric drivetrain offers. The Baj&iacute;o&rsquo;s logistics leaders are already deciding.</p>
'''))

# ---------------------------------------------------------------- 36
ARTICLES.append(dict(
f='tz5e-astana-kazakhstan-electric-dump-truck',
t='Astana Construction in a -30&deg;C Winter: TZ5E Electric Dump Trucks for Kazakhstan',
d='Can an electric dump truck survive an Astana winter? TZ5E cold-climate engineering, -30C range data, charging and TCO for Kazakhstan&rsquo;s construction fleets.',
k='TZ5E electric dump truck, EV truck Kazakhstan, electric truck Astana, electric dump truck cold climate, EV truck winter performance, Dongfeng electric truck Central Asia',
img='models/p01_00.jpg',
alt='Dongfeng TZ5E electric dump truck on an Astana construction site in winter, EV truck cold climate performance',
net='zxc',
body='''
<p>Astana is the world&rsquo;s second-coldest capital and one of its fastest-building: the city adds housing, infrastructure and commercial space on a construction calendar that pauses only for the worst of a winter where -30&deg;C is a normal January morning. It is also, therefore, the hardest test market for electric construction trucks anywhere &mdash; the place where the question &ldquo;but does it work in winter?&rdquo; is not scepticism but due diligence. This article examines the <a href="../products/models/tz5e-electric-dump-truck.html">Dongfeng TZ5E electric dump truck</a> for Astana&rsquo;s construction fleets: the cold-climate engineering, the real winter range numbers, the charging protocol, and the TCO at Kazakh energy prices. Short version: the physics is manageable, the engineering is done, and the economics are surprisingly strong.</p>

<h2>Cold-Climate Engineering: What the TZ5E Does Differently</h2>
<p>Winter capability is engineered, not hoped for. The TZ5E&rsquo;s 400 kWh CATL LFP pack is liquid-cooled and liquid-heated: during plugged-in hours the thermal system brings cells to 15-25&deg;C and holds them there, so the truck departs with a warm battery regardless of ambient. Insulated pack enclosures slow the daytime temperature fall; the heat-pump cabin system draws a third of the power of resistance heating; and the motor&rsquo;s waste heat is scavenged into the thermal loop. The result, from our Central Asian winter fleet data: trucks departing a warm depot hold effective operating temperature through a 4-6 hour work window at -25&deg;C, and the worst-case winter range lands at 62-68% of the rated figure &mdash; a real penalty, honestly stated, and one the duty-cycle planning below absorbs.</p>

<h2>Winter Numbers for Astana Duty</h2>
<table style="width:100%;border-collapse:collapse;margin:20px 0;" border="1" cellpadding="8">
<tr style="background:#006341;color:#fff;"><th style="padding:8px;text-align:left;">Parameter</th><th style="padding:8px;text-align:left;">Summer (+25&deg;C)</th><th style="padding:8px;text-align:left;">Winter (-25&deg;C)</th></tr>
<tr><td style="padding:8px;">Range (loaded, urban construction)</td><td style="padding:8px;">240-280 km</td><td style="padding:8px;">150-190 km</td></tr>
<tr><td style="padding:8px;">DC charge 20-80%</td><td style="padding:8px;">~50 min at 240 kW</td><td style="padding:8px;">~65-75 min (pack pre-heats first)</td></tr>
<tr><td style="padding:8px;">Energy per km loaded</td><td style="padding:8px;">1.5-1.7 kWh</td><td style="padding:8px;">2.2-2.6 kWh</td></tr>
<tr><td style="padding:8px;">Cab comfort</td><td style="padding:8px;">standard</td><td style="padding:8px;">heat-pump + seat/wheel heaters, -35&deg;C rated</td></tr>
</table>
<p>Now the duty cycle. An Astana construction tipper on city duty &mdash; batching plant or spoil site to site, 15-35 km loops &mdash; runs 120-180 km on a winter day. The winter range of 150-190 km covers the median day, and a midday 30-minute top-up at the depot or plant charger covers everything above it. The critical discipline is operational: the truck lives plugged in whenever parked (the thermal system then works from the grid, not the battery), depots are enclosed or the chargers sit inside heated bays where possible, and the fleet&rsquo;s dispatch treats the midday charge as a scheduled event rather than an emergency. Fleets that adopt the discipline run full winter programmes; the single failure pattern we see is fleets treating winter charging like summer charging.</p>

<h2>Specification for Kazakh Construction</h2>
<ul>
<li><strong>Battery:</strong> 400 kWh CATL LFP, liquid-heated/cooled, insulated enclosure, 8-year / 4,500-cycle warranty</li>
<li><strong>Motor:</strong> LvKong 360 kW peak / 2,400 Nm &mdash; instant torque on ice-and-snow starts, millisecond traction control</li>
<li><strong>Payload:</strong> 25 t GVW / ~15 t, 12 m&sup3; heated-body option (frozen-load prevention)</li>
<li><strong>Charging:</strong> 240 kW DC dual-gun, cold-rated cables and connectors to -40&deg;C</li>
<li><strong>Cab:</strong> -35&deg;C winter pack: heat-pump HVAC, heated seats/wheel/mirrors, insulated curtains</li>
<li><strong>FOB price band:</strong> US$95,000-115,000 with winter specification</li>
</ul>
<p>The heated-body option deserves a sentence because Kazakh contractors know the problem intimately: wet spoil and sand freeze to steel bodies at -20&deg;C, and diesel fleets fight it with open-flame body warmers that are exactly as dangerous as they sound. The electric option heats the body electrically from the traction pack &mdash; controlled, safe, and effective &mdash; and it alone converts experienced winter operators.</p>

<h2>TCO: The Winter-Adjusted Arithmetic</h2>
<p>Kazakh industrial electricity runs US$0.04-0.06/kWh &mdash; among the world&rsquo;s lowest &mdash; against diesel at US$0.60-0.75/L. Summer: the TZ5E&rsquo;s 1.6 kWh/km costs US$0.08/km against the diesel tipper&rsquo;s US$0.35/km. Winter: 2.4 kWh/km costs US$0.12/km against a cold-idling diesel&rsquo;s US$0.42-0.48/km (winter hurts the diesel too &mdash; cold starts, idling for warmth, winter-grade fuel premium, and brutal cold-start engine wear). Blended across the year, the electric truck&rsquo;s energy saving runs 65-72%, and the maintenance saving compounds in winter, when diesel drivetrains consume batteries, starters, fuel heaters and engine life. Annual combined saving per truck: US$18,000-26,000 on Astana utilisation. Payback against the premium: 24-34 months &mdash; and the battery warranty, at 8 years, is indifferent to how many winters it spans.</p>

<h2>Charging Infrastructure in Astana</h2>
<p>Astana&rsquo;s grid is robust &mdash; the city is new, its industrial zones well-served &mdash; and a ten-truck fleet&rsquo;s 500-630 kVA managed-charging requirement is a standard industrial connection. The winter-specific provisions: chargers in enclosed or semi-enclosed bays where possible (every degree of shelter is charge-speed in January), cold-rated cables (standard cables stiffen and crack at -30&deg;C), and the always-plugged-in discipline wired into the depot&rsquo;s physical layout so parking and charging are the same act. We deliver the winter charging design with the trucks, because the difference between a successful Kazakh winter fleet and a frustrated one is infrastructure detail, not vehicle capability.</p>

<h2>Import and Market Context</h2>
<p>Trucks route to Kazakhstan via Khorgos or the Caspian corridor with full EAC certification documentation &mdash; UN R100 and R10 certificates, Russian-language files &mdash; and Kazakhstan&rsquo;s EV framework carries zero import duty on electric vehicles against 15%+ on diesel. Buyers can find the full market context on our <a href="../markets/kazakhstan.html">Kazakhstan market page</a>. Support for Astana fleets includes winter commissioning (we schedule first deployments to land fleets trained before January), extended cold-climate parts kits, CATL module stock at 14-18 days, and telemetry monitoring that watches pack thermal behaviour through the winter as a managed parameter.</p>

<h2>The Verdict for Cold-Climate Fleets</h2>
<p>Does an electric dump truck work in an Astana winter? Yes &mdash; with engineering that is standard on the truck, a charging discipline that takes a week to learn, and a 30-35% winter range penalty that honest planning absorbs. The diesel alternative pays its own winter tax in fuel, wear and reliability &mdash; a tax fleets have paid so long they stopped counting it. Astana&rsquo;s contractors are pragmatists in a hard climate; the fleets that run the winter numbers rather than the winter myths will find the electric truck&rsquo;s economics survive the frost comfortably.</p>
'''))

# ---------------------------------------------------------------- 37
ARTICLES.append(dict(
f='tz8j-cycle-time-vs-diesel-mixer-comparison',
t='Electric vs Diesel Mixer Cycle Time: Does the TZ8J Keep Up on a Real Pour Schedule?',
d='Do electric concrete mixers slow the pour? TZ8J electric mixer cycle-time data vs diesel on real batching cycles: charging strategy, drum drive and productivity numbers.',
k='electric mixer cycle time, TZ8J vs diesel mixer, electric concrete mixer productivity, EV truck mixer pour schedule, electric mixer truck charging strategy, Dongfeng electric mixer',
img='models/p05_02.jpg',
alt='Dongfeng TZ8J electric mixer cycle time comparison vs diesel mixer, EV truck pour productivity data',
net='zxc',
body='''
<p>Every ready-mix operator&rsquo;s first question about electric mixers is the same: &ldquo;Will it keep my pour schedule?&rdquo; It is the right question &mdash; concrete is perishable, plant throughput is contract revenue, and a truck that breaks the cycle costs more than its fuel savings. This article answers it with cycle math instead of reassurance: how the <a href="../products/models/tz8j-electric-mixer-truck.html">Dongfeng TZ8J electric mixer</a> runs a real batching day against its diesel counterpart, where time is actually lost and gained in the cycle, and how the charging strategy maps onto the pour calendar. The short answer: on the duty cycles that define ready-mix work, the electric mixer matches the diesel&rsquo;s rhythm &mdash; and wins several of its margins.</p>

<h2>The Mixer Cycle, Dissected</h2>
<p>A standard ready-mix cycle has six phases: batch (5-10 min), haul-out (15-45 min), queue (0-60 min, the wild card), pour (20-45 min at the pump or chute), washout (5-10 min), and haul-back (15-45 min). The diesel mixer burns fuel through all six; its engine drives the drum hydraulically at whatever rpm the working phase demands. The TZ8J runs the same six phases with two architectural differences that change the time-and-energy math: the drum spins on an independent electric drive at constant, programmable speed &mdash; no engine-speed dependency, no hydraulic losses &mdash; and the traction system consumes zero during queue and pour phases. Nothing in the cycle is slower electrically; the question is only whether the battery covers the day.</p>

<h2>Cycle Time: The Head-to-Head Numbers</h2>
<table style="width:100%;border-collapse:collapse;margin:20px 0;" border="1" cellpadding="8">
<tr style="background:#006341;color:#fff;"><th style="padding:8px;text-align:left;">Cycle Phase</th><th style="padding:8px;text-align:left;">Diesel Mixer</th><th style="padding:8px;text-align:left;">TZ8J Electric Mixer</th></tr>
<tr><td style="padding:8px;">Batch &amp; load</td><td style="padding:8px;">5-10 min, engine at fast idle</td><td style="padding:8px;">5-10 min, drum on grid-charged pack</td></tr>
<tr><td style="padding:8px;">Haul-out (30 km)</td><td style="padding:8px;">35-50 min in traffic</td><td style="padding:8px;">35-50 min &mdash; identical</td></tr>
<tr><td style="padding:8px;">Site queue</td><td style="padding:8px;">engine running, drum turning</td><td style="padding:8px;">traction zero; drum at 3-5 kW</td></tr>
<tr><td style="padding:8px;">Pour</td><td style="padding:8px;">20-45 min, PTO at working rpm</td><td style="padding:8px;">20-45 min, constant-speed drum &mdash; better slump control</td></tr>
<tr><td style="padding:8px;">Washout &amp; return</td><td style="padding:8px;">identical</td><td style="padding:8px;">identical</td></tr>
<tr><td style="padding:8px;">Cycles per 10-h shift (30 km cycle)</td><td style="padding:8px;">6-8</td><td style="padding:8px;">6-8 &mdash; with one 30-45 min charge on high-utilisation days</td></tr>
</table>
<p>The table&rsquo;s bottom line is the answer: cycles per shift are the same. The TZ8J&rsquo;s 350 kWh CATL LFP pack delivers 220-280 km of loaded mixer duty including drum load &mdash; six to eight 30 km cycles &mdash; which covers a standard shift outright. High-utilisation days (10-12 cycles, pour-critical pours) need one 30-45 minute DC charge, and the pour calendar itself provides the slot: the midday lull between the morning pour wave and the afternoon wave, when the diesel trucks are parked at the plant anyway. Charging is scheduled into a window the operation already owns; it does not take time from the pour.</p>

<h2>Where the Electric Mixer Is Actually Faster</h2>
<p>Three phases genuinely improve. Pull-away and acceleration: the electric drivetrain&rsquo;s instant torque moves a loaded 32 t mixer through urban traffic with less time lost at every light &mdash; our fleet data shows 2-4% shorter haul times on congested routes, which compounds to a bonus cycle on some days. The pour itself: constant-speed drum rotation gives the pump operator steady discharge without engine-rev coordination, shaving minutes per pour and improving slump consistency &mdash; quality managers notice. And the working environment: no exhaust at the pour point matters on enclosed and semi-enclosed pours (basements, tunnels, occupied buildings), where diesel mixers increasingly face restrictions that the electric mixer simply does not have.</p>

<h2>The Energy Ledger Behind the Schedule</h2>
<p>Cycle parity is only half the story; the other half is what each cycle costs. A diesel 8x4 mixer burns 0.75-0.90 L/km equivalent on urban duty including drum and queue load; the TZ8J consumes 1.7-2.0 kWh/km all-in. At representative prices (diesel US$1.00-1.45/L, industrial power US$0.10-0.16/kWh across our deployment markets), energy cost per cycle runs US$22-32 diesel versus US$6-9 electric &mdash; a 65-75% reduction on the same number of cycles. Annualised on a two-shift plant, the saving per truck runs US$25,000-45,000 depending on market and utilisation, with maintenance (no engine, transmission, or hydraulic PTO) adding US$5,000-9,000 more. Payback on the purchase premium: 18-30 months on two-shift duty. The full platform specification is on our <a href="../products/models/tz8j-electric-mixer-truck.html">TZ8J model page</a>.</p>
<ul>
<li><strong>Cycles per shift:</strong> 6-8 both platforms &mdash; parity on the productivity metric that matters</li>
<li><strong>Charge strategy:</strong> overnight full + one midday slot on peak days</li>
<li><strong>Energy per cycle:</strong> 65-75% below diesel</li>
<li><strong>Slump consistency:</strong> constant-speed electric drum, independent of engine rpm</li>
<li><strong>Restricted pours:</strong> basements, tunnels, occupied buildings &mdash; no exhaust issue</li>
</ul>

<h2>Plant-Level Charging Design</h2>
<p>The batching plant is the charger &mdash; this is what makes mixer fleets the easiest heavy segment to electrify. A 12-15 truck plant runs on two 240 kW DC chargers plus managed overnight AC, an 800 kVA-1 MVA service the plant&rsquo;s industrial connection usually accommodates or upgrades to routinely. The load-management layer sequences charging around batching load and the pour calendar: overnight full charges, the midday rotation wave, and top-ups slotted into dock time. Buyers scoping plant electrification in our core markets can see deployment contexts on the <a href="../markets/indonesia.html">Indonesia market page</a> and regional equivalents, where plant-based mixer fleets run exactly this pattern.</p>

<h2>The Verdict</h2>
<p>The pour-schedule question dissolves under data: identical cycles per shift, a charging slot the calendar already provides, and better behaviour at the pour itself. What changes is the cost per cubic metre delivered &mdash; down 65-75% on energy, with a maintenance-light drivetrain and an emissions profile that wins restricted-site work diesel cannot touch. Ready-mix is a margin business run on schedule discipline; the electric mixer keeps the discipline and improves the margin. That is the whole case, and it is a strong one.</p>
'''))

# ---------------------------------------------------------------- 38
ARTICLES.append(dict(
f='ethiopia-ice-import-ban-electric-truck-opportunity',
t='Ethiopia Banned Combustion Vehicle Imports: What the World&rsquo;s Boldest EV Policy Means for Truck Buyers',
d='Ethiopia banned ICE vehicle imports in 2024 &mdash; the world&rsquo;s first full combustion ban. What it means for electric truck buyers: duty, charging, models and the fleet opportunity.',
k='Ethiopia ICE import ban, electric truck Ethiopia, EV truck import Africa policy, electric truck Addis Ababa, Dongfeng electric truck, Ethiopia EV policy trucks',
img='models/p14_10.jpg',
alt='Ethiopia ICE import ban creates electric truck opportunity, EV truck fleet for Addis Ababa logistics',
net='zhc',
body='''
<p>In January 2024 Ethiopia did what no other country has done: it banned the import of combustion-engine passenger vehicles outright &mdash; not a future phase-out, an immediate ban &mdash; driven by a fuel-import bill the country could no longer afford. Commercial vehicles have followed a tightening path of duty pressure and policy signalling in the same direction. For fleet operators, the message from Addis Ababa is unmistakable: the diesel era&rsquo;s economics are being legislated against in one of Africa&rsquo;s largest markets, and the electric truck is not an option being offered but a direction being mandated. This article maps what the policy shift means practically: the duty landscape, the grid reality, which segments electrify first, and how to build a fleet position in a market with 120 million consumers and a first-mover policy.</p>

<h2>The Policy Logic: Forex, Not Fashion</h2>
<p>Ethiopia&rsquo;s ban is macroeconomic, not environmental &mdash; and that makes it more durable, not less. The country spends US$4-6 billion annually on fuel imports, its largest single drain on foreign exchange; its domestic resource is the opposite &mdash; the Grand Ethiopian Renaissance Dam and the hydro cascade make it one of Africa&rsquo;s cheapest and cleanest power producers, with industrial electricity around US$0.04-0.06/kWh and surplus capacity seeking load. Every kilometre converted from imported diesel to domestic hydro is a direct improvement in the national balance of payments. Truck fleets should read the passenger-vehicle ban as the opening move: commercial-vehicle duty treatment already favours electric decisively, and the policy trajectory &mdash; charging mandates, fleet targets, financing support &mdash; points one way.</p>

<h2>The Numbers That Follow the Policy</h2>
<table style="width:100%;border-collapse:collapse;margin:20px 0;" border="1" cellpadding="8">
<tr style="background:#006341;color:#fff;"><th style="padding:8px;text-align:left;">Factor</th><th style="padding:8px;text-align:left;">Ethiopia Value</th><th style="padding:8px;text-align:left;">Fleet Consequence</th></tr>
<tr><td style="padding:8px;">Industrial electricity</td><td style="padding:8px;">US$0.04-0.06/kWh (hydro)</td><td style="padding:8px;">Energy per km: US$0.06-0.10 &mdash; world-class</td></tr>
<tr><td style="padding:8px;">Diesel (subsidised, scarce)</td><td style="padding:8px;">US$0.90-1.10/L, supply-constrained</td><td style="padding:8px;">US$0.45-0.65/km &mdash; and availability risk</td></tr>
<tr><td style="padding:8px;">EV import duty</td><td style="padding:8px;">near-zero (passenger ban; CV duty strongly favoured)</td><td style="padding:8px;">US$15,000-40,000/truck advantage vs diesel at import</td></tr>
<tr><td style="padding:8px;">Grid carbon intensity</td><td style="padding:8px;">~95%+ hydro/renewable</td><td style="padding:8px;">genuine zero-emission operation</td></tr>
</table>
<p>The fuel-availability line deserves emphasis because it is the operational fact diesel fleets live with: supply interruptions are routine, and a truck grounded for want of diesel earns nothing. An electric fleet charged on domestic hydro removes that exposure entirely &mdash; in a market where fuel security is the single largest operational risk, electrification is also the risk-management answer.</p>

<h2>Which Segments Electrify First</h2>
<ul>
<li><strong>Addis Ababa urban distribution:</strong> the capital&rsquo;s retail and FMCG freight (KT5M/KT5J class, 100-180 km daily) &mdash; the highest-utilisation, fastest-payback segment</li>
<li><strong>Port-corridor shuttles:</strong> Modjo dry port and the Addis logistics corridor &mdash; Ethiopia imports 95% of its goods via Djibouti, and the dry-port drayage is fixed-route, depot-based duty</li>
<li><strong>Construction fleets:</strong> Addis&rsquo;s permanent building boom runs tippers and mixers on urban cycles (TZ3Z/TZ5E/TZ8J classes)</li>
<li><strong>Coffee and agri-export logistics:</strong> the southern collection corridors&rsquo; hub-and-spoke legs suit KTH3-class trucks with destination charging</li>
<li><strong>Municipal fleets:</strong> Addis Ababa&rsquo;s city administration is an early policy adopter &mdash; sanitation and service fleets lead publicly</li>
</ul>
<p>The Djibouti corridor&rsquo;s long trunk (750 km) is the one segment where diesel persists near-term; as with every market we cover, electrification starts at the urban ends and extends along the corridor as charging follows. The dry-port and city segments alone represent thousands of trucks.</p>

<h2>Grid and Charging Reality</h2>
<p>Ethiopia&rsquo;s grid has capacity from the hydro build-out, but reliability outside the capital requires the standard frontier-market architecture: depot charging with on-site buffering (the fleet&rsquo;s own batteries), solar augmentation (4.8-5.5 peak sun hours &mdash; excellent), and managed charging that respects local grid conditions. Addis Ababa&rsquo;s industrial zones support the 400-800 kVA connections a mid-size fleet needs; the government&rsquo;s EV programme is actively streamlining charging-infrastructure connections. We deploy the standard package &mdash; DC fast chargers, managed AC, load control &mdash; with the solar canopy sized in from day one, because at Ethiopian tariffs the canopy&rsquo;s payback is among the fastest in the world.</p>

<h2>Import and Support Practicalities</h2>
<p>Trucks route via Djibouti port with 28-35 day sailings from China, then rail or road to Modjo/Addis. We deliver with English documentation, UN R100 certification, and the homologation support for the Ethiopian transport authority. The duty advantage on electric commercial vehicles is substantial and the customs process for EVs has been deliberately streamlined as part of the policy. Buyers can find the full market context on our <a href="../markets/ethiopia.html">Ethiopia market page</a>. Support for Ethiopian fleets includes commissioning and HV training in Addis, extended parts kits sized for corridor logistics, CATL module stock at 14-21 days, and telemetry monitoring &mdash; the architecture already running across our East African deployments.</p>

<h2>The First-Mover Frame</h2>
<p>Markets that legislate transitions reward whoever reads the legislation early. Ethiopia has told the world &mdash; in the bluntest instrument available to policy &mdash; that its road transport electrifies. The fleets that build electric positions now lock in the duty advantage, the world-class energy cost, the fuel-security hedge, and the operating experience that will define the market&rsquo;s service infrastructure as it scales. The policy is not coming; it is here, it is first in the world, and its commercial-vehicle chapter is being written now by the fleets that show up.</p>
'''))

# ---------------------------------------------------------------- 39 GEO 1
ARTICLES.append(dict(
f='how-many-charging-stations-does-an-ev-truck-fleet-need',
t='How Many Charging Stations Does an Electric Truck Fleet Actually Need?',
d='How many chargers does an EV truck fleet need? Quick answer with real ratios: 1 DC fast charger per 4-8 trucks plus overnight AC &mdash; sizing rules, costs and examples inside.',
k='how many charging stations EV truck fleet, electric truck charger ratio, fleet charging sizing, EV truck depot charging plan, electric truck infrastructure cost, charger per truck ratio',
img='models/p14_11.jpg',
alt='How many charging stations an electric truck fleet needs, EV truck depot charger sizing guide',
net='gen',
body='''
<p><strong>Quick answer:</strong> Most electric truck fleets need one DC fast charger (120-360 kW) per 4-8 trucks plus one overnight AC charging point per 1-2 trucks. A 10-truck delivery fleet typically runs well on 2 DC fast chargers and 5-8 AC posts &mdash; a 250-400 kVA connection &mdash; because trucks charge sequentially, not simultaneously. The right ratio depends on daily kilometres, shift pattern and battery size, not on a one-per-truck rule.</p>

<h2>Why Fleets Overbuy Chargers (and What It Costs)</h2>
<p>The most expensive mistake in fleet electrification is sizing infrastructure on the diesel mental model &mdash; one pump per truck, everyone fuels at once. Electric trucks charge where they park, for hours they are not working, at power levels the operator chooses. A truck covering 150 km a day in a 106 kWh-pack delivery vehicle needs roughly 90-110 kWh of energy replenished nightly &mdash; about 5 hours on a 22 kW AC post, or 40 minutes on a 120 kW DC charger. Multiplied across a fleet, the energy need is large but the simultaneity is small: trucks finish routes at different times, and a load-management system sequences their sessions across the night. The fleets that grasp this spend US$40,000-80,000 on charging hardware for ten trucks; the ones that do not spend three times that and add a substation they never use.</p>

<h2>Which Ratios Apply to Which Duty Cycle?</h2>
<table style="width:100%;border-collapse:collapse;margin:20px 0;" border="1" cellpadding="8">
<tr style="background:#006341;color:#fff;"><th style="padding:8px;text-align:left;">Fleet Profile</th><th style="padding:8px;text-align:left;">DC Fast Chargers</th><th style="padding:8px;text-align:left;">Overnight AC</th><th style="padding:8px;text-align:left;">Connection Size</th></tr>
<tr><td style="padding:8px;">Urban delivery, 100-150 km/day, single shift</td><td style="padding:8px;">1 per 6-8 trucks</td><td style="padding:8px;">1 per 1-2 trucks</td><td style="padding:8px;">~35 kVA/truck</td></tr>
<tr><td style="padding:8px;">Construction, 150-220 km/day, single shift</td><td style="padding:8px;">1 per 4-6 trucks</td><td style="padding:8px;">1 per 2 trucks</td><td style="padding:8px;">~50 kVA/truck</td></tr>
<tr><td style="padding:8px;">Two-shift distribution, 250-350 km/day</td><td style="padding:8px;">1 per 3-4 trucks</td><td style="padding:8px;">1 per 2 trucks</td><td style="padding:8px;">~60 kVA/truck</td></tr>
<tr><td style="padding:8px;">Port drayage / 24-7 operations</td><td style="padding:8px;">1 per 2-3 trucks (or swap station)</td><td style="padding:8px;">supplementary</td><td style="padding:8px;">~80 kVA/truck</td></tr>
<tr><td style="padding:8px;">Long-haul corridor, 400+ km/day</td><td style="padding:8px;">1-2 per truck base + en-route</td><td style="padding:8px;">1 per truck</td><td style="padding:8px;">~100+ kVA/truck</td></tr>
</table>
<p>The table&rsquo;s logic in one sentence: the harder the fleet works, the more it leans on DC fast charging and the lower the truck-per-charger ratio. But even the hardest profiles are nowhere near one-per-truck &mdash; a 24/7 port fleet runs three tractors per fast charger comfortably because a 45-minute charge serves 8-10 hours of work.</p>

<h2>How Do You Calculate Your Fleet&rsquo;s Exact Number?</h2>
<p>The sizing calculation has four steps and we run it free for any fleet evaluating our trucks. Step one, energy demand: daily kilometres x consumption (kWh/km, from route profile) per truck, summed. Step two, simultaneity: map when each truck is parked &mdash; the parking windows define how many sessions must run at once. Step three, charger throughput: a 240 kW DC charger delivers roughly 1,800-2,200 kWh across a night with sequencing; divide fleet demand by throughput for the DC count. Step four, connection size: peak simultaneous draw plus headroom, checked against the site&rsquo;s service. A worked example &mdash; ten <a href="../products/models/kt5m-electric-cargo-truck.html">KT5M box trucks</a> at 160 km/day: fleet demand ~1,300 kWh/night, one 240 kW DC plus six 22 kW AC posts, 350 kVA connection, hardware cost roughly US$55,000-70,000. The same fleet wrongly sized at one DC per truck: US$250,000+ and a 1.5 MVA connection the utility takes a year to deliver.</p>

<h2>What Does the Infrastructure Actually Cost?</h2>
<p>Budget figures for planning: AC posts (22-40 kW) run US$3,000-6,000 installed; 120 kW DC units US$35,000-50,000; 240-360 kW DC units US$60,000-90,000; switchgear, cabling and civil works typically add 40-60% on top; grid connection upgrades are the wild card, from trivial (adequate existing service) to US$100,000+ (new transformer and medium-voltage run). The total for a well-designed ten-truck depot lands at US$80,000-150,000 &mdash; roughly US$8,000-15,000 per truck, or 10-15% of the fleet&rsquo;s vehicle budget. Fleets operating in the Gulf can reference the deployment contexts on our <a href="../markets/uae.html">UAE market page</a>; the same sizing discipline applies across every market we serve, with local grid lead times setting the project critical path.</p>
<ul>
<li><strong>Rule of thumb:</strong> 1 DC per 4-8 trucks + AC for overnight bays</li>
<li><strong>Never size:</strong> one charger per truck &mdash; the cost error is 3x</li>
<li><strong>Size for year three:</strong> conduits and switchboard for double the day-one fleet</li>
<li><strong>File the grid application on order day:</strong> utility lead time always exceeds vessel transit</li>
</ul>

<h2>Frequently Asked Questions</h2>
<h3>How many trucks can one DC fast charger serve?</h3>
<p>One 240 kW DC charger serves 4-8 trucks in typical single-shift fleets, because a 45-60 minute session restores a working day&rsquo;s energy and sessions sequence across the night. In 24/7 port operations the ratio tightens to 2-3 trucks per charger.</p>
<h3>Is overnight AC charging enough for a 200 km/day truck?</h3>
<p>Usually yes for packs up to 140 kWh: a 22 kW AC post delivers ~150 kWh in 7 hours, covering 180-220 km of delivery duty. Trucks with 350-600 kWh packs on 250+ km days need the DC layer for part of their energy.</p>
<h3>How much does a 10-truck charging depot cost?</h3>
<p>Typically US$80,000-150,000 all-in: two DC fast chargers, six to eight AC posts, switchgear and civil works. That is US$8,000-15,000 per truck &mdash; roughly 10-15% of the vehicle budget.</p>
<h3>Can trucks share chargers across shifts?</h3>
<p>Yes &mdash; sharing is the entire design principle. Load management sequences sessions by departure time and required state of charge, so a ten-truck fleet on a 350 kVA connection charges fully overnight without any truck waiting.</p>
<h3>Do I need battery swap instead of chargers?</h3>
<p>Only for true 24/7 operations above ~10 trucks, or mining duty with no charge windows: swap exchanges a 600 kWh pack in 5-6 minutes. Below that utilisation, depot DC charging is cheaper and simpler.</p>
''',
faq=[
('How many trucks can one DC fast charger serve?', 'One 240 kW DC charger serves 4-8 trucks in typical single-shift fleets, because a 45-60 minute session restores a working day&rsquo;s energy and sessions sequence across the night. In 24/7 port operations the ratio tightens to 2-3 trucks per charger.'),
('Is overnight AC charging enough for a 200 km/day truck?', 'Usually yes for packs up to 140 kWh: a 22 kW AC post delivers about 150 kWh in 7 hours, covering 180-220 km of delivery duty. Trucks with 350-600 kWh packs on 250+ km days need the DC layer for part of their energy.'),
('How much does a 10-truck charging depot cost?', 'Typically US$80,000-150,000 all-in: two DC fast chargers, six to eight AC posts, switchgear and civil works. That is US$8,000-15,000 per truck, roughly 10-15% of the vehicle budget.'),
('Can trucks share chargers across shifts?', 'Yes. Load management sequences sessions by departure time and required state of charge, so a ten-truck fleet on a 350 kVA connection charges fully overnight without any truck waiting for a charger.'),
('Do I need battery swap instead of chargers?', 'Only for true 24/7 operations above about 10 trucks, or mining duty with no charge windows: swap exchanges a 600 kWh pack in 5-6 minutes. Below that utilisation, depot DC charging is cheaper and simpler.'),
]))

# ---------------------------------------------------------------- 40 GEO 2
ARTICLES.append(dict(
f='how-long-does-it-take-to-charge-an-electric-truck',
t='How Long Does It Take to Charge an Electric Truck? Real Times by Battery and Charger',
d='How long does electric truck charging take? Quick answer: 45-70 min (20-80%) on DC fast charge for 282-600 kWh packs, 5-6 min by battery swap. Full data table inside.',
k='how long to charge electric truck, electric truck charging time, EV truck fast charging, electric truck DC charge time, battery swap time truck, electric truck 20-80 charging',
img='models/p14_12.jpg',
alt='How long it takes to charge an electric truck, EV truck charging time by battery size and charger power',
net='gen',
body='''
<p><strong>Quick answer:</strong> A heavy electric truck charges from 20% to 80% in 45-70 minutes on a DC fast charger (240-360 kW), or fully overnight in 6-10 hours on AC depot charging. Battery-swap variants exchange a full pack in 5-6 minutes. Charging time depends on battery size (106-600 kWh in commercial trucks), charger power, and the pack&rsquo;s temperature &mdash; not on marketing claims.</p>

<h2>What Determines Charging Time?</h2>
<p>Three variables set the clock, and buyers should understand all three before comparing numbers. Battery size: a 106 kWh delivery-truck pack and a 600 kWh heavy-tractor pack are different jobs &mdash; the industry quotes 20-80% times precisely because that window is where chargers run at full power. Charger power: a 120 kW unit delivers energy at half the rate of a 240 kW unit, and liquid-cooled 360-500 kW units halve it again on large packs. The charging curve: every lithium pack charges fastest at low state of charge and tapers above ~80%, which is why route planning targets the 20-80% window and why &ldquo;0-100%&rdquo; figures are always misleading for operational planning.</p>

<h2>How Long Does Each Truck Class Take?</h2>
<table style="width:100%;border-collapse:collapse;margin:20px 0;" border="1" cellpadding="8">
<tr style="background:#006341;color:#fff;"><th style="padding:8px;text-align:left;">Truck Class (battery)</th><th style="padding:8px;text-align:left;">DC 20-80% Time</th><th style="padding:8px;text-align:left;">Overnight AC 10-100%</th><th style="padding:8px;text-align:left;">Range Restored (DC session)</th></tr>
<tr><td style="padding:8px;">Light delivery, 106-130 kWh</td><td style="padding:8px;">30-40 min at 90-120 kW</td><td style="padding:8px;">5-7 h at 22 kW</td><td style="padding:8px;">110-140 km</td></tr>
<tr><td style="padding:8px;">Medium box/cargo, 140-180 kWh</td><td style="padding:8px;">~40 min at 120 kW</td><td style="padding:8px;">7-9 h at 22-40 kW</td><td style="padding:8px;">120-150 km</td></tr>
<tr><td style="padding:8px;">Heavy rigid / port tractor, 282-350 kWh</td><td style="padding:8px;">45-55 min at 240 kW</td><td style="padding:8px;">overnight via DC or 2x40 kW AC</td><td style="padding:8px;">130-170 km loaded</td></tr>
<tr><td style="padding:8px;">Heavy tractor / dump, 400-600 kWh</td><td style="padding:8px;">60-70 min at 360 kW dual-gun</td><td style="padding:8px;">overnight DC managed</td><td style="padding:8px;">200-300 km loaded</td></tr>
<tr><td style="padding:8px;">Swap-variant (any large pack)</td><td style="padding:8px;">5-6 min exchange</td><td style="padding:8px;">packs charge at station</td><td style="padding:8px;">100% in 6 min</td></tr>
</table>
<p>Notice what the table says about operations: no class requires more than about an hour of fast charging to restore a working shift&rsquo;s energy, and every class can be fully charged overnight. The &ldquo;charging takes too long&rdquo; objection dissolves when the truck&rsquo;s own duty cycle provides the windows &mdash; parked nights, dock time, driver breaks, and shift changes. Our <a href="../products/models/te46-electric-tractor.html">TE46 port tractor</a>, for example, restores a 8-10 hour shift&rsquo;s energy in a 45-minute lunch-window charge; fleets running Gulf drayage can see the operating context on our <a href="../markets/saudi-arabia.html">Saudi Arabia market page</a>.</p>

<h2>Does Cold or Heat Change Charging Time?</h2>
<p>Yes &mdash; and it is the most under-discussed factor in the specification conversation. Lithium cells accept charge slowly when cold: a pack at -10&deg;C may charge at a third of its rated speed until the thermal system warms it. The engineering answer is pack pre-heating: liquid-heated packs (standard on our trucks) warm during plugged-in standby, so a truck departing a depot arrives at the charger warm, and winter DC sessions run 65-75 minutes instead of 45-55 in the worst cold. Heat matters less: liquid cooling holds the pack in its optimal band through 45&deg;C+ ambient, adding minutes, not fractions. The specification line to demand from any supplier is liquid thermal management &mdash; air-cooled packs lose this battle in both climates.</p>

<h2>Which Should You Choose: Fast Charge, Slow Charge or Swap?</h2>
<p>The decision tree is simpler than the industry makes it. Single-shift fleets (parked 12+ hours nightly): overnight AC or managed DC covers everything &mdash; fast charging is a convenience, not a need. Two-shift fleets: one 45-70 minute DC session per day, slotted into the shift change &mdash; this is the volume case for depot DC hardware. True 24/7 operations (ports, mining, round-the-clock construction): battery swap at 5-6 minutes, or opportunity charging at every queue and break &mdash; the <a href="../products/models/tz5y-electric-dump-truck.html">TZ5Y mining truck</a>&rsquo;s swap architecture exists precisely for this duty. Long-haul: en-route fast charging matched to mandated driver breaks, which is why corridor trucks specify 360-500 kW capability. The fleets that get this right buy the minimum fast-charging hardware their shift pattern actually requires &mdash; and spend the savings on trucks.</p>
<ul>
<li><strong>20-80% is the operational window:</strong> 45-70 min DC for heavy packs</li>
<li><strong>Overnight covers everything:</strong> single-shift fleets rarely need daytime charging at all</li>
<li><strong>Swap is the 24/7 answer:</strong> 5-6 minutes, faster than diesel refuelling</li>
<li><strong>Demand liquid thermal management:</strong> it is the difference between spec-sheet and winter reality</li>
</ul>

<h2>Frequently Asked Questions</h2>
<h3>How long does a 600 kWh electric truck take to charge?</h3>
<p>A 600 kWh pack charges 20-80% in 60-70 minutes on a 360 kW dual-gun DC charger, restoring 200-300 km of loaded range. Battery-swap variants exchange the full pack in 5-6 minutes at a swap station.</p>
<h3>Can an electric truck charge in under an hour?</h3>
<p>Yes &mdash; most classes charge 20-80% in 30-70 minutes on DC fast charging: light delivery trucks (106-130 kWh) in 30-40 minutes at 90-120 kW, heavy trucks (282-600 kWh) in 45-70 minutes at 240-360 kW.</p>
<h3>How long does overnight charging take for a fleet truck?</h3>
<p>A 140 kWh delivery truck charges 10-100% in 7-9 hours on a 22 kW AC post; larger packs charge overnight on managed DC. Every truck class reaches 100% during a standard 10-12 hour depot night.</p>
<h3>Does fast charging damage the truck battery?</h3>
<p>Occasional fast charging causes no measurable harm; CATL LFP packs carry an 8-year / 4,500-cycle warranty covering normal DC use. Fleets that fast-charge every session daily should expect slightly faster capacity fade &mdash; the telematics SOH report tracks it.</p>
<h3>Is battery swapping faster than charging for trucks?</h3>
<p>Yes &mdash; an automated swap station exchanges a 350-600 kWh pack in 5-6 minutes, faster than a diesel refuel. One station serves 10-15 trucks on 24/7 duty, making swap the standard answer for ports and mines.</p>
''',
faq=[
('How long does a 600 kWh electric truck take to charge?', 'A 600 kWh pack charges 20-80% in 60-70 minutes on a 360 kW dual-gun DC charger, restoring 200-300 km of loaded range. Battery-swap variants exchange the full pack in 5-6 minutes at a swap station.'),
('Can an electric truck charge in under an hour?', 'Yes. Most classes charge 20-80% in 30-70 minutes on DC fast charging: light delivery trucks (106-130 kWh) in 30-40 minutes at 90-120 kW, heavy trucks (282-600 kWh) in 45-70 minutes at 240-360 kW.'),
('How long does overnight charging take for a fleet truck?', 'A 140 kWh delivery truck charges 10-100% in 7-9 hours on a 22 kW AC post; larger packs charge overnight on managed DC. Every truck class reaches 100% during a standard 10-12 hour depot night.'),
('Does fast charging damage the truck battery?', 'Occasional fast charging causes no measurable harm; CATL LFP packs carry an 8-year / 4,500-cycle warranty covering normal DC use. Fleets fast-charging every session daily should expect slightly faster capacity fade, tracked by the telematics SOH report.'),
('Is battery swapping faster than charging for trucks?', 'Yes. An automated swap station exchanges a 350-600 kWh pack in 5-6 minutes, faster than a diesel refuel. One station serves 10-15 trucks on 24/7 duty, making swap the standard answer for ports and mines.'),
]))

for a in ARTICLES:
    html = build(a)
    path = os.path.join(ROOT, 'blog', a['f'] + '.html')
    with open(path, 'w', encoding='utf-8') as fh:
        fh.write(html)
    words = len(re.sub(r'<[^>]+>', ' ', a['body']).split())
    print('%-58s %5d words' % (a['f'], words))
print('done batch5:', len(ARTICLES))
