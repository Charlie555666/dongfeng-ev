# -*- coding: utf-8 -*-
"""Run 15 batch 3: 8 articles (Latin America + Southeast Asia spotlights)."""
import re, os
import _gen_run14_b1 as G
G.DATE = "2026-10-08"
build = G.build

ROOT = os.path.dirname(os.path.abspath(__file__))
ARTICLES = []

# ---------------------------------------------------------------- 1
ARTICLES.append(dict(
f='callao-peru-port-electric-tractor-fleet',
t='Callao Port: TE46 Electric Terminal Tractors for Peru&rsquo;s Container Gateway',
d='Callao Port container handling costs drop sharply with the TE46 electric terminal tractor. Specs, shift range, Lima air-quality rules and Peru import steps for this EV truck.',
k='TE46 electric terminal tractor, EV truck Peru, electric truck Callao, electric port tractor Lima, Dongfeng EV truck, container drayage electric truck, Callao terminal tractor',
img='models/p11_00.jpg',
alt='Dongfeng TE46 electric terminal tractor shuttling containers at Callao Port, EV truck for Peru container logistics',
net='qyc',
body='''
<p>Callao is Peru&rsquo;s single maritime gateway &mdash; roughly 80% of the country&rsquo;s containerized imports and exports move through its terminals, and the port sits inside the Lima metro area where 10 million people breathe the air the trucks and tractors produce. For terminal operators and the 3PLs working the DP World and APM Terminals concessions, the electrification question is no longer about whether, but about how fast the Lima regional government&rsquo;s air-quality rules will force the transition. This article examines the <a href="../products/models/te46-electric-tractor.html">Dongfeng TE46 electric terminal tractor</a> as the workhorse for Callao&rsquo;s container shuttle: what it costs to run per shift, how the battery holds up across a two-shift day, and what the import path into Peru looks like. For a port whose economics run on cents per container move, an EV truck tractor is a margin instrument, not a green badge.</p>

<h2>Why Callao Is Built for Electric Drayage</h2>
<p>Terminal tractor duty is the most predictable freight profile in road transport, and Callao&rsquo;s geometry makes it ideal. A shuttle tractor never leaves the terminal footprint: it moves a loaded chassis from the quay crane to the stacking yard, drops it, returns empty for the next, and repeats for 8-12 hours. Total daily distance is 120-200 km, almost all of it at 15-30 km/h, with 25-40% of engine-hours spent idling in crane queues and gate lines. Idle time is where diesel economics collapse &mdash; a 12 L diesel terminal tractor burns 3-4 litres per hour producing nothing while waiting. The TE46&rsquo;s electric drivetrain draws essentially zero at standstill; only the cab HVAC draws, at about 1.5 kW. Across a shift, queue idling alone is 25-35% of a diesel tractor&rsquo;s daily fuel bill and under 2% of the electric tractor&rsquo;s energy bill.</p>
<p>The second driver is regulatory. Lima Metropolitana has tightened low-emission-zone rules around the port, and Peru&rsquo;s national electrification incentives (Law 30490 and the evolving CONAMER framework) zero-rate the import tariff on electric vehicles while diesel trucks pay 6-9% plus the 18% IGV base. For terminal operators whose corporate customers &mdash; the global shipping lines &mdash; now report scope-3 landside emissions per call, a zero-exhaust terminal tractor is becoming a commercial requirement written into concession renewals.</p>

<h2>TE46 Specifications for Callao Duty</h2>
<table style="width:100%;border-collapse:collapse;margin:20px 0;" border="1" cellpadding="8">
<tr style="background:#006341;color:#fff;"><th style="padding:8px;text-align:left;">Parameter</th><th style="padding:8px;text-align:left;">TE46 4x2 Electric Terminal Tractor</th></tr>
<tr><td style="padding:8px;">GCW rating</td><td style="padding:8px;">42-46 t (container shuttle spec)</td></tr>
<tr><td style="padding:8px;">Battery</td><td style="padding:8px;">262-350 kWh CATL LFP, liquid-cooled, swap-capable option</td></tr>
<tr><td style="padding:8px;">Motor</td><td style="padding:8px;">LvKong 250 kW peak / 2,800 Nm</td></tr>
<tr><td style="padding:8px;">Shift endurance (262 kWh pack)</td><td style="padding:8px;">7-8 h mixed drayage duty</td></tr>
<tr><td style="padding:8px;">Shift endurance (350 kWh pack)</td><td style="padding:8px;">10-12 h, full two-shift coverage</td></tr>
<tr><td style="padding:8px;">DC charge 20-80%</td><td style="padding:8px;">~45 min at 240 kW dual-gun</td></tr>
<tr><td style="padding:8px;">Battery swap time</td><td style="padding:8px;">5-6 min (swap variant)</td></tr>
<tr><td style="padding:8px;">Fifth wheel</td><td style="padding:8px;">50 mm oscillating, terminal-rated</td></tr>
<tr><td style="padding:8px;">Gradeability</td><td style="padding:8px;">&ge;30% at full GCW</td></tr>
<tr><td style="padding:8px;">Battery warranty</td><td style="padding:8px;">8 years / 4,500 cycles to 70% SOH</td></tr>
<tr><td style="padding:8px;">FOB price band</td><td style="padding:8px;">US$72,000-88,000</td></tr>
</table>
<p>Operators sizing a Callao fleet should think about two packs rather than one. The 262 kWh version covers a single shift comfortably and is the right choice for day-shift-only concessions. The 350 kWh version runs the full two-shift pattern on one charge with a lunch-break top-up, and it is the configuration we recommend for terminals running 18-20 hour windows to clear mega-vessel calls. Both use the same CATL LFP chemistry rated for 4,500+ cycles at 45&deg;C cell temperature &mdash; critical at Callao, where the summer coastal heat pushes ambient to 28-32&deg;C and the liquid-cooled pack keeps cells in the safe band without the degradation penalty NMC chemistry would pay.</p>

<h2>The Peruvian TCO: Cents per Container Move</h2>
<p>Peru&rsquo;s industrial electricity tariff at port-adjacent zones runs roughly US$0.11-0.14 per kWh. A diesel terminal tractor on this stop-start duty burns 0.55-0.70 L/km equivalent including idle; at Peruvian diesel of US$1.10-1.20/L, that is about US$0.65-0.75 per kilometre. The TE46 consumes 1.5-1.8 kWh/km at 40 t GCW; at US$0.13/kWh, that is US$0.20-0.23 per kilometre. On 160 km per day, 300 days a year, the annual energy saving is roughly US$21,000-26,000 per tractor. Maintenance &mdash; no engine, transmission, clutch or aftertreatment, plus brake pads lasting 3-4x longer under regenerative braking &mdash; adds US$5,000-7,000 more. Against a purchase premium of US$28,000-38,000 over a diesel terminal tractor, payback lands at 14-20 months. In terminal economics, that is less than one vessel season.</p>
<ul>
<li><strong>Energy per km:</strong> US$0.70 diesel vs US$0.22 electric &mdash; a 68% reduction</li>
<li><strong>Annual saving per tractor:</strong> US$26,000-33,000 combined</li>
<li><strong>Queue idling:</strong> ~30% of the diesel fuel bill eliminated entirely</li>
<li><strong>Terminal air quality:</strong> zero NOx and particulates inside the gate &mdash; directly answers Lima&rsquo;s low-emission rules</li>
<li><strong>Noise:</strong> ~12 dB lower at the cab, improving spotter-yard communication and safety</li>
</ul>

<h2>Charging and Swap at the Terminal Gate</h2>
<p>Callao&rsquo;s terminals sit on medium-voltage grid with ample spare capacity for fleet charging; a six-tractor TE46 fleet runs on one 240 kW DC dual-gun charger plus managed overnight AC, a 400-500 kVA service class that the distributor processes routinely. For two-shift operations the battery-swap configuration changes the math: one swap station serves 15-20 tractors, holds 6-8 packs charging on managed load, and eliminates charging downtime entirely &mdash; a 5-6 minute pack exchange is faster than a diesel refuel. We specify swap for fleets above ten tractors or any terminal running two shifts; below that, depot DC charging is cheaper and simpler. Both ship as a coordinated package with the tractors: chargers, swap station, switchgear and the load-management software preconfigured to the terminal&rsquo;s shift pattern.</p>
<p>One Callao-specific note: the port&rsquo;s yard surfaces are sealed and flat, so the charging and swap footprints drop straight into existing staging lanes without civil works. Terminals that already run reefer stacks have the transformer headroom to add tractor charging by tapping the same substation &mdash; we model the combined load before quoting so operators avoid a costly substation upgrade.</p>

<h2>Import Path into Peru</h2>
<p>Electric vehicles enter Peru under the Law 30490 incentive framework with the import tariff zero-rated, versus 6-9% on diesel tractors, and the 18% IGV applies to the landed value in both cases. Callao itself is the RoRo discharge point &mdash; the tractors sail from Shanghai or Tianjin in 32-38 days and are driven off the vessel at the same terminal they will serve. Customs clearance with a Licencia Unica de Importador and a maritime broker runs 5-10 working days. We supply the Spanish-language homologation dossier, the OSINERGMIN and MTC compliance references where required, and UN R100 battery certification as standard. Terminal operators running multi-port Andean strategies should also review our <a href="../markets/peru.html">Peru electric truck market page</a>, which covers the parallel Chancay mega-port corridor where the same TE46 platform will serve the new deep-water terminal 60 km north.</p>
<p>After-sales follows our port-fleet protocol: every tractor ships with a terminal-duty parts kit (fifth-wheel components, HV contactors, suspension wear parts), the telematics portal streams battery and drivetrain health to our engineering desk, and swap-variant fleets receive on-site station commissioning. The drivetrain&rsquo;s service calendar &mdash; brake inspections and coolant checks every 40,000 km &mdash; is a rounding error beside the diesel terminal tractor&rsquo;s engine, transmission and DPF maintenance load, which is the real story for a terminal measured on tractor availability per vessel call.</p>

<h2>The Strategic Call for Callao</h2>
<p>Callao competes on turnaround time, and container-move cost is set by energy price multiplied by a duty cycle that punishes diesel hardest of any application in road freight. The TE46 turns that duty cycle into an advantage: zero idle burn, regenerative braking on every yard traverse, and a battery sized to the actual shift rather than over-specified for range anxiety. Terminal operators who electrify their shuttle fleets first lock in lower per-move cost, a cleaner concession-renewal story, and a reference site the rest of the Pacific South American coast will visit. The economics above are not projections &mdash; they are the same terminal-tractor architecture already running in Mediterranean and African ports we have deployed, and Callao&rsquo;s geometry is even more favorable.</p>
'''))

# ---------------------------------------------------------------- 2
ARTICLES.append(dict(
f='iquique-chile-mining-electric-dump-truck',
t='Iquique and Tarapac&aacute;: TZ3V Electric Dump Trucks for Northern Chile Mining',
d='Northern Chile mining services cut haulage cost with the TZ3V electric dump truck at 2,000-4,000 m altitude. Specs, no power-loss data, TCO and Chile import steps for this EV truck.',
k='TZ3V electric dump truck, EV truck Chile, electric truck Iquique, electric dump truck mining Tarapaca, Dongfeng electric truck, copper mine electric truck, 8x4 electric tipper',
img='models/p03_05.jpg',
alt='Dongfeng TZ3V 8x4 electric dump truck at a northern Chile copper mine, EV truck for Tarapaca mining',
net='zxc',
body='''
<p>Northern Chile&rsquo;s mining economy runs on haulage, and haulage runs on diesel &mdash; at altitude, where diesel engines lose 25-40% of their power to thin air, that combination has been the unspoken tax on every tonne of copper and nitrate moved. The cities of Iquique and the Tarapac&aacute; region sit at the gateway to this world: the ports move concentrate to the world, while the service contractors running the pits and leach pads operate fleets of 8x4 tippers in the 2,000-4,000 m band where a diesel&rsquo;s turbo is always working overtime. This article examines the <a href="../products/models/tz3v-electric-dump-truck.html">Dongfeng TZ3V electric dump truck</a> for exactly this duty: why electric drivetrains are immune to altitude power loss, what the 600 kWh pack delivers on a mine shift, and how the Chile import path works. For mining-service contractors, an EV truck tipper is the rare capital decision that pays back on power alone.</p>

<h2>Altitude Is Where Electric Wins First</h2>
<p>The defining fact of northern Chile haulage is that diesel engines are altitude-limited and electric motors are not. A turbocharged diesel at 4,000 m produces roughly 60-70% of its sea-level power; the same haul up a pit ramp needs more throttle, more fuel, and more turbo boost that the thin air cannot supply, so cycle times stretch and fuel burn climbs. A permanent-magnet electric motor delivers its rated torque and power at any altitude &mdash; there is no air to compress, no combustion to oxygen-starve. On the TZ3V&rsquo;s LvKong 360 kW motor, the 2,400 Nm of peak torque is identical at Iquique sea level and at 4,000 m on the porphyry rim. Mining contractors consistently report that the single biggest operational change after electrifying is that the truck climbs the ramp at the same speed all shift, instead of fading as the day&rsquo;s altitude work wears the diesel down.</p>
<p>The second altitude factor is cooling. Diesel engines run hotter and derate harder in the Atacama&rsquo;s 30-38&deg;C dry heat combined with thin air&rsquo;s poor convective cooling. The TZ3V&rsquo;s liquid-cooled CATL LFP pack and motor loop hold their thermal band without the fan-and-radiator挣扎 diesel trucks face, and the LFP chemistry&rsquo;s 4,500+ cycle rating at 45&deg;C cell temperature is purpose-built for this environment. There is no cat until 90% &mdash; the chemistry simply does not combust &mdash; which matters in a region where fire containment on a mine site is a board-level concern.</p>

<h2>TZ3V Specifications for Mine Haulage</h2>
<table style="width:100%;border-collapse:collapse;margin:20px 0;" border="1" cellpadding="8">
<tr style="background:#006341;color:#fff;"><th style="padding:8px;text-align:left;">Parameter</th><th style="padding:8px;text-align:left;">TZ3V 8x4 Electric Dump Truck</th></tr>
<tr><td style="padding:8px;">GVW / payload</td><td style="padding:8px;">42-45 t / 28-32 t (18-20 m&sup3; body)</td></tr>
<tr><td style="padding:8px;">Battery</td><td style="padding:8px;">600 kWh CATL LFP, liquid-cooled</td></tr>
<tr><td style="padding:8px;">Motor</td><td style="padding:8px;">LvKong 360 kW peak / 2,400 Nm</td></tr>
<tr><td style="padding:8px;">Real-world range (loaded, mine profile)</td><td style="padding:8px;">180-240 km per charge</td></tr>
<tr><td style="padding:8px;">DC charge 20-80%</td><td style="padding:8px;">~60 min at 350 kW dual-gun</td></tr>
<tr><td style="padding:8px;">Altitude performance</td><td style="padding:8px;">No power derate to 4,000 m (vs 30-40% diesel loss)</td></tr>
<tr><td style="padding:8px;">Gradeability</td><td style="padding:8px;">&ge;30% at full load</td></tr>
<tr><td style="padding:8px;">Regeneration on pit descent</td><td style="padding:8px;">18-25% of round-trip energy recovered</td></tr>
<tr><td style="padding:8px;">Battery warranty</td><td style="padding:8px;">8 years / 4,500 cycles to 70% SOH</td></tr>
<tr><td style="padding:8px;">FOB price band</td><td style="padding:8px;">US$95,000-120,000 depending on body</td></tr>
</table>
<p>The 600 kWh pack is sized for the mine shift, not the marketing range number. A typical Tarapac&aacute; service-contractor cycle is 15-25 loaded round trips of 8-16 km from pit to crusher or leach pad, totaling 150-220 km per shift with heavy grade both ways. The pack covers that with margin and takes a mid-shift opportunity charge during the lunch and maintenance window. The descent regeneration point is the quiet winner: every loaded haul back down the pit ramp returns 18-25% of the climb energy to the pack, which on a diesel truck is simply lost to brake heat and liner wear &mdash; northern Chile fleets replace brake components at intervals their foremen know by heart, and the TZ3V stretches those intervals 3-4x.</p>

<h2>The Chilean Mining TCO</h2>
<p>Northern Chile industrial electricity &mdash; much of it from the Atacama&rsquo;s own solar &mdash; runs roughly US$0.09-0.12 per kWh. A diesel 8x4 tipper at altitude burns 0.50-0.65 L/km equivalent thanks to the turbo working harder; at Chilean mining diesel of US$1.05-1.15/L, that is about US$0.60-0.70 per kilometre. The TZ3V consumes 2.0-2.4 kWh/km at full payload on pit grades; at US$0.10/kWh, US$0.20-0.24 per kilometre. On 200 km per shift, 250 shifts a year, the annual energy saving is roughly US$18,000-23,000 per truck. Add maintenance &mdash; no engine, turbo, DPF or clutch, plus 3-4x brake life &mdash; for another US$8,000-12,000 annually. Against a purchase premium of US$40,000-55,000 over a diesel tipper, payback arrives in 20-28 months of mine service, inside the first half of the battery warranty.</p>
<ul>
<li><strong>Energy per km:</strong> US$0.65 diesel vs US$0.22 electric &mdash; a 66% reduction</li>
<li><strong>Altitude power:</strong> zero derate vs 30-40% diesel loss at 4,000 m</li>
<li><strong>Annual saving per truck:</strong> US$26,000-35,000 combined</li>
<li><strong>Brake life:</strong> 3-4x longer &mdash; pit descents no longer consume linings</li>
<li><strong>Safety:</strong> sealed HV system, no diesel fuel on site, quieter cab for spotters</li>
</ul>

<h2>Charging at the Mine Site</h2>
<p>Mine sites are the easiest place in the world to charge a truck fleet, because they generate or import serious power and operate a single controlled yard. The natural installation is one 350 kW dual-gun DC charger at the crusher or workshop, plus a depot post for overnight balance, on a 500-700 kVA service. For sites with captive solar (common in the Atacama), a 250-500 kWp canopy over the truck park offsets 40-60% of annual charging energy and is frequently already in the mine&rsquo;s power plan for other loads. We deliver the single-line diagram, load-management config and the utility or generator interface pack with the truck order, because charger lead time usually exceeds the 30-36 day vessel transit from China to Iquique or Antofagasta.</p>
<p>One operational note for contractors: battery-electric tippers change the shift pattern. Because the pack charges during the natural meal and maintenance window, the truck&rsquo;s available hours align to the human shift rather than the refuel stop &mdash; no driver waiting at a diesel bowser, no fuel bowser competing for pit road. Fleets that sequence charging into the existing break structure report higher effective utilisation than the diesel fleet it replaces, which the TCO models above do not even count.</p>

<h2>Import Path and the Chile Mining Context</h2>
<p>Chile applies differential treatment to electric vehicles under its electromobility framework, and Iquique&rsquo;s port handles RoRo truck imports with 30-36 day sailings from China&rsquo;s east coast and efficient customs for properly documented industrial vehicles. We supply the Spanish-language homologation dossier, the SERNAGEOMIN-relevant safety documentation for mine deployment, and UN R100 battery certification. Contractors serving multiple northern regions should also review our <a href="../markets/chile.html">Chile electric truck market page</a>, which covers the parallel Antofagasta and Atacama mining corridors where the same TZ3V platform serves copper, lithium and nitrate operations with shared parts and training.</p>
<p>Service support follows our mining protocol: a two-year fast-moving parts kit ships with the fleet, CATL modules are reachable from regional stock in 10-14 days, and telematics-based remote diagnostics give our engineers live battery and drivetrain visibility. The TZ3V&rsquo;s drivetrain &mdash; one motor, one reduction gear, no clutch, no aftertreatment &mdash; removes the maintenance categories that ground diesel tippers waiting on imported turbo and injection parts. On a mine site where a stopped truck is a stopped production line, drivetrain simplicity is revenue.</p>

<h2>Who Moves First in the Norte Grande</h2>
<p>The natural first adopters are the service contractors with captive pit-to-crusher routes &mdash; they control both ends of the duty cycle and can site chargers at the workshop. Copper and nitrate producers running their own haulage fleets are second. The altitude argument alone settles it: a diesel tipper at 4,000 m is a derated, fuel-hungry machine, while the TZ3V is the same truck it was at the port. Northern Chile&rsquo;s mining sector is already the cleanest-powered in the world on grid electricity; electrifying the haulage that moves the ore is the obvious next step, and the fleets that take it first bank the power advantage their diesel competitors cannot recover.</p>
'''))

# ---------------------------------------------------------------- 3
ARTICLES.append(dict(
f='cartagena-colombia-port-electric-cargo-truck',
t='Cartagena Port Logistics: KT5M Electric Box Trucks for Colombia&rsquo;s Caribbean Coast',
d='Cartagena port-city distribution suits the KT5M electric box truck: 180-220 km range, half the energy cost of diesel. EV truck specs, TCO and Colombia import guide.',
k='KT5M electric box truck, EV truck Colombia, electric truck Cartagena, electric cargo truck Caribbean coast, Dongfeng electric truck, electric box truck port logistics',
img='models/p07_04.jpg',
alt='Dongfeng KT5M electric box truck on a Cartagena port distribution route, EV truck for Colombia Caribbean logistics',
net='zhc',
body='''
<p>Cartagena is Colombia&rsquo;s Caribbean gateway &mdash; the container terminal, the free zone, and the tourism economy of the walled city and the Bocagrande hotels all share the same narrow peninsula, and the freight that feeds them moves through a port-city corridor that is short, congested and increasingly emissions-sensitive. Hotels and cruise passengers do not want diesel soot on the seafront; the free zone wants low-carbon logistics as a tenant selling point; and the distribution fleets want fuel costs that stop climbing. This article looks at the <a href="../products/models/kt5m-electric-cargo-truck.html">Dongfeng KT5M electric box truck</a> in exactly that role: Cartagena port-to-warehouse and hotel-supply distribution, with real numbers on range, TCO and the Colombian import path. For a city where the last freight leg is both short and watched, an EV truck box truck is the right tool.</p>

<h2>The Cartagena Freight Signature</h2>
<p>Port logistics on a peninsula is compact freight. The container terminal to the Mamonal industrial zone is 8-15 km; terminal to the free zone and the city DCs, under 12 km; hotel and restaurant supply runs across Bocagrande and Castillogrande, 5-20 km. A distribution box truck on this pattern runs 70-130 km daily across two waves &mdash; morning port clearance, afternoon city and tourism-zone delivery &mdash; and returns to the same yard every night. The KT5M&rsquo;s 200-240 km real-world range covers the longest day with 40% reserve, and the two-wave pattern leaves a natural midday window for a 30-40 minute top-up. No public charging is needed; the operation runs entirely from one depot, which is why port-city distribution is the lowest-risk EV truck entry in any market.</p>
<p>Tourism-zone sensitivity is the second driver and it is specific to Cartagena. The walled city and the hotel strips enforce informal and formal low-emission expectations, and several hotel groups now specify electric or Euro-VI delivery for seafront supply runs. A silent, zero-exhaust KT5M on the early-morning bakery-and-produce run is a commercial asset for the 3PL that owns it &mdash; it keeps the delivery window open when diesel idling would draw complaints, and it reads as a sustainability credential the hotels increasingly ask about in their vendor questionnaires.</p>

<h2>KT5M Specifications for Caribbean Coast Duty</h2>
<table style="width:100%;border-collapse:collapse;margin:20px 0;" border="1" cellpadding="8">
<tr style="background:#006341;color:#fff;"><th style="padding:8px;text-align:left;">Parameter</th><th style="padding:8px;text-align:left;">KT5M Electric Box Truck</th></tr>
<tr><td style="padding:8px;">GVW / payload</td><td style="padding:8px;">9-12 t class / 4.5-6 t payload</td></tr>
<tr><td style="padding:8px;">Battery</td><td style="padding:8px;">180-220 kWh CATL LFP options</td></tr>
<tr><td style="padding:8px;">Motor</td><td style="padding:8px;">LvKong 150-190 kW peak / 1,100-1,500 Nm</td></tr>
<tr><td style="padding:8px;">Real-world range (port-city, loaded)</td><td style="padding:8px;">200-240 km</td></tr>
<tr><td style="padding:8px;">DC charge 20-80%</td><td style="padding:8px;">~45 min at 120-150 kW</td></tr>
<tr><td style="padding:8px;">Body options</td><td style="padding:8px;">28-35 m&sup3; dry box, curtainside, reefer</td></tr>
<tr><td style="padding:8px;">Gradeability</td><td style="padding:8px;">&ge;25% at full load</td></tr>
<tr><td style="padding:8px;">Battery warranty</td><td style="padding:8px;">8 years / 4,500 cycles to 70% SOH</td></tr>
<tr><td style="padding:8px;">FOB price band</td><td style="padding:8px;">US$50,000-64,000</td></tr>
</table>
<p>The 180-220 kWh battery band lets operators right-size to the route. Fleets running only the Mamonal-corridor short loops can take the 180 kWh pack and save upfront weight and cost; fleets serving the tourism zone with longer backhauls take the 220 kWh version with margin. Both share the same chassis, motor and telematics, so a mixed fleet is trivial to maintain. The reefer variant deserves a mention for Cartagena&rsquo;s seafood and hospitality cold chain: the electric reefer draws from the traction battery at a fraction of a diesel reefer unit&rsquo;s fuel cost, which sharpens the TCO for the hotel-food and frozen-fish distribution that moves through the port.</p>

<h2>Colombian TCO at Caribbean Energy Prices</h2>
<p>Colombian diesel on the coast runs US$0.95-1.05 per litre. A 9-12 t box truck on Cartagena port duty burns 0.30-0.38 L/km including gate idle &mdash; about US$0.32 per kilometre. The KT5M consumes 0.75-0.90 kWh/km; at Afinia/EPM coastal industrial tariffs of roughly US$0.12-0.14/kWh, US$0.11 per kilometre. On 4,000 km per month (two-wave port duty), the monthly energy saving is about US$840 per truck. Maintenance adds US$200-300 monthly &mdash; no oil, clutch, injectors or DPF, and brake pads lasting 2-3x longer under regenerative braking. Against a purchase premium of US$18,000-25,000, payback lands at 17-22 months. The reefer variant strengthens this further because the electric refrigeration load displaces the most expensive diesel in the operation.</p>
<ul>
<li><strong>Energy per km:</strong> US$0.32 diesel vs US$0.11 electric &mdash; a 66% reduction</li>
<li><strong>Monthly saving per truck:</strong> ~US$1,000-1,100 on two-wave duty</li>
<li><strong>Payback:</strong> 17-22 months; faster for reefer variants</li>
<li><strong>Gate queues:</strong> 20-30% of diesel idle fuel eliminated</li>
<li><strong>Tourism zone:</strong> silent, zero-exhaust delivery keeps seafront windows open</li>
</ul>
<p>A second cost layer strengthens the case beyond fuel. Colombian insurers are beginning to price electric commercial fleets below diesel equivalents on lower fire and mechanical-risk profiles, and several leasing arms now offer preferential rates on certified EV truck assets, which lowers the effective monthly carry on the purchase premium and pulls the payback window inward. Resale also behaves differently: a diesel box truck depreciates toward its engine&rsquo;s rebuild cost, while the KT5M&rsquo;s dominant value sits in the CATL pack, which the 8-year warranty protects &mdash; so a three-year-old unit still carries a bankable battery asset that diesel resale cannot match.</p>

<h2>Charging in the Port Free Zone</h2>
<p>Cartagena&rsquo;s Mamonal industrial zone and free zone have medium-voltage capacity for depot charging; a ten-truck KT5M fleet runs on roughly 300-350 kVA with managed charging &mdash; a standard industrial connection class. The practical layout: one 120-150 kW DC charger per 6-8 trucks for rotation, overnight AC at each bay, and a load-management controller matched to the shift schedule. Colombia&rsquo;s Caribbean solar resource (4.8-5.2 peak sun hours) makes a yard canopy strongly economic: 150-250 kWp offsets 40-55% of charging energy and provides covered, shaded staging &mdash; shade has operational value on a peninsula where surface temperatures hit 34&deg;C.</p>
<p>A sizing note for transhipment-dependent operators: Cartagena&rsquo;s volumes track the global cycle, and electrification kit should be specified for the month-24 fleet, not month one. We size switchboards and conduits for double the initial charger count; the marginal cost at construction is trivial and eliminates the most expensive retrofit in fleet electrification, which is re-digging the yard.</p>

<h2>Import Path and the Colombian Context</h2>
<p>Colombia offers tax and tariff incentives under its electromobility policy (including VAT and duty reductions on certified electric vehicles), and Cartagena&rsquo;s RoRo facilities are the country&rsquo;s most experienced for truck imports, with 30-36 day sailings from China and efficient Aduanas cycles for documented vehicles. We deliver the Spanish-language homologation dossier, the Ministerio de Transporte and RTM reference documentation, and UN R100 battery certification. Distribution groups with national coverage should also review our <a href="../markets/colombia.html">Colombia electric truck market page</a>, which covers the parallel Buenaventura Pacific-corridor and Bogot&aacute; urban-freight opportunities where the same KT5M platform serves both coasts with shared parts and training.</p>
<p>After-sales ships with the trucks: a two-year fast-moving parts kit per fleet, CATL module stock reachable in 10-14 days, and telematics remote diagnostics with Spanish-language support. The drivetrain&rsquo;s maintenance calendar &mdash; brake inspections, coolant checks, software updates &mdash; removes the workshop dependency that grounds diesel trucks waiting on imported engine components, which is the entire point for a port city whose freight never stops.</p>

<h2>First Movers on the Caribbean Coast</h2>
<p>The strongest first candidates are the free-zone 3PLs and the food, beverage and hotel-supply distributors with captive port-to-city routes. Their utilisation is the highest, their yards are already secured and powered, and their customers &mdash; hotel groups and multinational FMCG with scope-3 targets &mdash; will pay attention to zero-emission final legs. Cartagena built its tourism economy on a clean, walkable seafront; extending that cleanliness to the freight that serves it is the logical next step, and the arithmetic above says the fleets that do it first bank a cost advantage their diesel competitors cannot match.</p>
'''))

# ---------------------------------------------------------------- 4
ARTICLES.append(dict(
f='puebla-mexico-automotive-electric-truck-logistics',
t='Puebla Automotive Corridor: TE8L Electric Tractors for Mexico&rsquo;s OEM Logistics',
d='Puebla OEM logistics cut shuttle cost with the TE8L electric tractor: 400-500 kWh, Puebla-Mexico City-Veracruz runs. EV truck specs, TCO and Mexico import steps.',
k='TE8L electric tractor, EV truck Mexico, electric truck Puebla, electric tractor OEM logistics, Dongfeng electric truck, automotive supplier shuttle truck, 6x4 electric prime mover',
img='models/p11_04.jpg',
alt='Dongfeng TE8L 6x4 electric tractor on a Puebla automotive supplier route, EV truck for Mexico OEM logistics',
net='qyc',
body='''
<p>Puebla is the engine room of Mexico&rsquo;s auto industry &mdash; Volkswagen&rsquo;s largest plant outside Germany, Audi&rsquo;s San Jos&eacute; Chiapa facility, and a dense tier-1 and tier-2 supplier belt that feeds both with just-in-sequence (JIS) parts delivered on punishingly tight windows. The freight that keeps those lines running moves on a triangle: parts from supplier plants around Puebla to the OEM assembly lines, components up the Autopista del Sol to Mexico City distribution, and finished vehicles and inbound kits down to the port of Veracruz for export. This article examines the <a href="../products/models/te8l-electric-tractor.html">Dongfeng TE8L electric tractor</a> on exactly these shuttle runs &mdash; what the 400-500 kWh pack delivers on the corridor, how JIS timing survives electrification, and how the Mexican import path works. For an industry where a stopped line costs six figures an hour, an EV truck tractor has to be more reliable than the diesel it replaces, not less.</p>

<h2>The Automotive Shuttle Duty Cycle</h2>
<p>Supplier logistics is the most disciplined freight in the world, and Puebla&rsquo;s version is a clean electric fit. A JIS shuttle tractor runs fixed routes on fixed clocks: Puebla supplier to VW/Audi line (10-40 km), supplier to Mexico City DC (110-130 km), or inbound kit run to Veracruz port (240-280 km one way, with a return the same day). Daily distance is 180-360 km, almost all highway or perif&eacute;rico at steady 60-90 km/h cruise &mdash; the efficiency sweet spot for an electric drivetrain. The TE8L&rsquo;s 400-500 kWh pack covers the Puebla-Mexico City loop on one charge and the Veracruz round trip with a port-top-up, which is why the corridor is the textbook first deployment for a 6x4 electric prime mover.</p>
<p>JIS timing is the reason reliability matters more than range headroom. A parts tractor that misses its 12-minute delivery window stops an assembly line. The TE8L&rsquo;s telematics portal schedules charging around the dispatch clock and guarantees departure state of charge, so the question operators actually care about &mdash; will the truck be charged and ready at 05:00 &mdash; is answered by software, not by a driver&rsquo;s fuel-gauge anxiety. Depot charging overnight plus a port or DC top-up handles the long runs; the trucks never wait at a public charger.</p>

<h2>TE8L Specifications for OEM Logistics</h2>
<table style="width:100%;border-collapse:collapse;margin:20px 0;" border="1" cellpadding="8">
<tr style="background:#006341;color:#fff;"><th style="padding:8px;text-align:left;">Parameter</th><th style="padding:8px;text-align:left;">TE8L 6x4 Electric Tractor</th></tr>
<tr><td style="padding:8px;">GCW rating</td><td style="padding:8px;">40-49 t (JIS trailer spec)</td></tr>
<tr><td style="padding:8px;">Battery</td><td style="padding:8px;">400-500 kWh CATL LFP, liquid-cooled</td></tr>
<tr><td style="padding:8px;">Motor</td><td style="padding:8px;">LvKong 420-510 kW peak / 3,200-3,600 Nm</td></tr>
<tr><td style="padding:8px;">Real-world range (loaded, mixed)</td><td style="padding:8px;">280-350 km</td></tr>
<tr><td style="padding:8px;">Puebla&ndash;Veracruz round trip</td><td style="padding:8px;">500-560 km with port top-up</td></tr>
<tr><td style="padding:8px;">DC charge 20-80%</td><td style="padding:8px;">~55-60 min at 350 kW dual-gun</td></tr>
<tr><td style="padding:8px;">Gradeability</td><td style="padding:8px;">&ge;30% at full GCW</td></tr>
<tr><td style="padding:8px;">Battery warranty</td><td style="padding:8px;">8 years / 4,500 cycles to 70% SOH</td></tr>
<tr><td style="padding:8px;">FOB price band</td><td style="padding:8px;">US$95,000-130,000</td></tr>
</table>
<p>The torque figure is what sells the Puebla belt. A loaded JIS trailer combination at 40-49 t GCW pulls away from a supplier yard or up the grade toward the Autopista del Sol with full torque from zero rpm &mdash; no clutch slip, no turbo lag, no rev-matching. The gradeability holds the truck at highway speed on the climbs where a diesel tractor drops a gear and loses time. Drivers transitioning from diesel report the single biggest change is predictable, repeatable acceleration across the whole shift, which is exactly what a JIS clock rewards. The 4,500-cycle LFP warranty covers the high-annual-kilometre life an automotive shuttle tractor actually lives.</p>

<h2>Mexican TCO on the Corridor</h2>
<p>Mexican diesel runs US$1.00-1.10 per litre depending on the border and IESPS band. A 6x4 tractor on the Puebla corridor burns 0.42-0.52 L/km equivalent; at US$1.05/L, about US$0.47 per kilometre. The TE8L consumes 1.3-1.6 kWh/km at 45 t GCW; at CFE industrial tariffs of roughly US$0.10-0.13/kWh, US$0.17-0.21 per kilometre. On 300 km per day, 300 days a year, the annual energy saving is roughly US$23,000-29,000 per tractor. Maintenance &mdash; no engine, transmission, clutch or aftertreatment, plus 3x brake life under regen &mdash; adds US$6,000-9,000 more. Against a purchase premium of US$45,000-65,000 over a diesel 6x4, payback lands at 18-26 months. For a supplier running 15-30 tractors on the corridor, that is US$400,000-550,000 per year of recovered margin from year two onward.</p>
<ul>
<li><strong>Energy per km:</strong> US$0.47 diesel vs US$0.19 electric &mdash; a 60% reduction</li>
<li><strong>Annual saving per tractor:</strong> US$29,000-38,000 combined</li>
<li><strong>Payback:</strong> 18-26 months at Mexican fuel and power prices</li>
<li><strong>Uptime:</strong> sealed drivetrain, no DPF regen, no clutch wear in stop-go DC queues</li>
<li><strong>Brand fit:</strong> aligns supplier ESG reporting with OEM scope-3 targets</li>
</ul>
<p>Financing and resale reinforce the math. Development-bank and supplier leasing lines in Mexico increasingly discount certified electric tractors, lowering the effective carry on the premium, and the TE8L&rsquo;s value concentrates in the CATL pack that the 8-year warranty protects &mdash; so a mid-life unit retains a bankable battery asset the diesel&rsquo;s engine rebuild cost cannot match.</p>

<h2>Charging at the Supplier Yard and Port</h2>
<p>The Puebla supplier belt and the Veracruz port logistics zone both have medium-voltage capacity for fleet charging; a ten-tractor TE8L fleet runs on roughly 700-900 kVA with managed charging &mdash; a standard industrial connection class CFE processes routinely. The configuration we deploy: one 350 kW dual-gun DC charger per 5-6 tractors for rotation, overnight AC at each bay, and load management matched to the dispatch clock so the site never exceeds contracted capacity. The utility application goes in on purchase-order day &mdash; the 8-14 week CFE connection lead time is the critical path and almost always exceeds the 28-34 day vessel transit from China to Veracruz or Manzanillo.</p>
<p>One Mexico-specific opportunity: the Autopista del Sol and the Perif&eacute;rico corridor fleets can share charging infrastructure with Mexico City DCs, and several supplier groups we work with run their tractors out of a single powered yard that serves both the OEM line and the capital distribution. The TE8L&rsquo;s telematics manage the mixed long- and short-haul schedule through one portal, which is what makes a 15-tractor mixed fleet practical rather than chaotic.</p>

<h2>Import Path and the Mexican Market</h2>
<p>Mexico&rsquo;s electromobility incentives vary by state, and Puebla and several states offer reduced vehicle registration and temporary duty relief on certified electric trucks, against the standard 15-20% on diesel tractors. Veracruz and Manzanillo handle RoRo truck imports with 28-34 day sailings from China and efficient customs for documented industrial vehicles. We supply the Spanish-language homologetion dossier, NOM-ONN-regulatory references where required, and UN R100 battery certification. Supplier groups with US cross-border operations should also review our <a href="../markets/mexico.html">Mexico electric truck market page</a>, which covers the US-Mexico border corridor and the parallel Monterrey automotive belt where the same TE8L platform serves both with shared parts and training.</p>
<p>After-sales follows our automotive protocol: a two-year fast-moving parts kit per fleet, CATL module stock reachable in 10-14 days, and telematics remote diagnostics with Spanish-language engineering support. The drivetrain&rsquo;s service calendar &mdash; brake inspections, coolant checks, software updates &mdash; is a fraction of the diesel tractor&rsquo;s engine, transmission and DPF load, which is the real story for a supplier measured on line-stoppage minutes.</p>

<h2>First Movers in the Puebla Belt</h2>
<p>The natural first adopters are the tier-1 suppliers with captive shuttle routes to the VW and Audi lines, followed by the 3PLs running JIS and finished-vehicle logistics. Their utilisation is the highest in Mexican freight, their yards are secured and powered, and their OEM customers are already demanding electrified inbound logistics as a scope-3 lever. Puebla&rsquo;s auto cluster built its reputation on precision logistics; electrifying the shuttle that feeds the line is the next precision step, and the fleets that take it first bank a cost and ESG advantage their diesel competitors cannot answer.</p>
'''))

# ---------------------------------------------------------------- 5
ARTICLES.append(dict(
f='santiago-dominican-agri-electric-cargo-truck',
t='Santiago de los Caballeros: KT5L Electric Cargo Trucks for Dominican Agribusiness',
d='Cibao Valley agribusiness cuts haulage cost with the KT5L electric cargo truck. Tobacco, cocoa and produce logistics specs, TCO and Dominican Republic import steps for this EV truck.',
k='KT5L electric cargo truck, EV truck Dominican Republic, electric truck Santiago de los Caballeros, electric cargo truck agribusiness, Dongfeng electric truck, Cibao valley farm truck',
img='models/p07_09.jpg',
alt='Dongfeng KT5L electric cargo truck on a Cibao Valley agribusiness route, EV truck for Dominican produce logistics',
net='zhc',
body='''
<p>Santiago de los Caballeros sits in the heart of the Cibao Valley, the agricultural engine of the Dominican Republic, where tobacco, cocoa, plantains and fresh produce move from farm and processing cooperative to the packing houses, then north to Puerto Plata or south to Santo Domingo&rsquo;s markets and the Las Am&eacute;ricas export gate. That freight is short, repetitive and return-to-base &mdash; and it runs today in diesel trucks paying some of the Caribbean&rsquo;s higher effective fuel costs while hauling perishable goods that hate heat and delay. This article examines the <a href="../products/models/kt5l-electric-cargo-truck.html">Dongfeng KT5L electric cargo truck</a> for Cibao agribusiness: what the 130-160 kWh pack delivers on farm-to-packhouse runs, the cold-chain angle, and the Dominican import path. For a cooperative or exporter moving volume daily, an EV truck is a margin decision with a sustainability bonus the buyers now pay for.</p>

<h2>The Cibao Freight Pattern</h2>
<p>Agribusiness logistics in the Cibao is compact by nature. Tobacco and cocoa farms around Jarabacoa and the Constanza highlands sit 40-90 km from Santiago&rsquo;s processing houses; produce growing belts around La Vega and San Francisco de Macor&iacute;s are 30-70 km; the export lane to Puerto Plata is 150-180 km and to Santo Domingo 130-160 km. A cargo truck on this pattern runs 90-180 km daily, almost all secondary road at 40-70 km/h with rolling grades through the valley &mdash; ideal electric territory because the descents return energy and the distances sit inside the KT5L&rsquo;s 190-230 km real-world range. The two-wave harvest pattern (morning farm pickup, afternoon packhouse delivery) leaves a natural midday charge window, so the fleet runs from one cooperative yard.</p>
<p>The cold-chain angle is the quiet winner. Dominican fresh produce and cocoa exports are temperature-sensitive, and the KT5L&rsquo;s electric reefer draws from the traction battery instead of a diesel reefer unit burning 2-3 L/hour in the field. A refrigerated KT5L holds setpoint from farm to packhouse on traction energy alone, cutting both fuel cost and the heat spikes that bruise premium cocoa and leafy produce. Exporters targeting EU and US premium shelves &mdash; where carbon and cold-chain documentation now travel with the invoice &mdash; get a double benefit: lower cost and a cleaner shipment record.</p>

<h2>KT5L Specifications for Agribusiness</h2>
<table style="width:100%;border-collapse:collapse;margin:20px 0;" border="1" cellpadding="8">
<tr style="background:#006341;color:#fff;"><th style="padding:8px;text-align:left;">Parameter</th><th style="padding:8px;text-align:left;">KT5L Electric Cargo Truck</th></tr>
<tr><td style="padding:8px;">GVW / payload</td><td style="padding:8px;">6-7.5 t class / 2.5-3.5 t payload</td></tr>
<tr><td style="padding:8px;">Battery</td><td style="padding:8px;">130-160 kWh CATL LFP</td></tr>
<tr><td style="padding:8px;">Motor</td><td style="padding:8px;">LvKong 110-140 kW peak / 900-1,100 Nm</td></tr>
<tr><td style="padding:8px;">Real-world range (loaded, mixed)</td><td style="padding:8px;">190-230 km</td></tr>
<tr><td style="padding:8px;">DC charge 20-80%</td><td style="padding:8px;">~35-40 min at 90-120 kW</td></tr>
<tr><td style="padding:8px;">Body options</td><td style="padding:8px;">18-24 m&sup3; box, curtainside, reefer</td></tr>
<tr><td style="padding:8px;">Gradeability</td><td style="padding:8px;">&ge;25% &mdash; handles Constanza-hill climbs</td></tr>
<tr><td style="padding:8px;">Battery warranty</td><td style="padding:8px;">8 years / 4,500 cycles to 70% SOH</td></tr>
<tr><td style="padding:8px;">FOB price band</td><td style="padding:8px;">US$42,000-54,000</td></tr>
</table>
<p>The gradeability figure matters specifically for the Cibao, because the Constanza and Jarabacoa highlands include sustained 10-14% grades where a loaded diesel box truck crawls in second gear. The KT5L&rsquo;s motor holds torque to rated speed and climbs the same grades at 40-50 km/h, then regenerates 18-25% of the climb energy back on the descent &mdash; a diesel truck turns that same descent into brake heat and liner wear. For cooperatives running the highland tobacco and vegetable belts, that regeneration is a measurable share of round-trip energy, not a footnote.</p>

<h2>Dominican Republic TCO</h2>
<p>Dominican diesel runs US$1.10-1.20 per litre. A 6-7.5 t box truck on Cibao duty burns 0.22-0.28 L/km; at US$1.15/L, about US$0.29 per kilometre. The KT5L consumes 0.55-0.70 kWh/km; at EDENORTE commercial tariffs of roughly US$0.18-0.22/kWh, US$0.13-0.15 per kilometre. On 3,000 km per month the grid-charged saving is about US$420 per truck monthly; at a cooperative solar-canopy effective cost of US$0.08-0.10/kWh it rises to US$570+. Maintenance adds US$150-200 monthly &mdash; no oil, clutch, injectors or DPF, brakes lasting 2-3x longer. Against a purchase premium of US$14,000-18,000, payback arrives in 18-26 months grid-charged, 14-20 months with solar. The CATL battery warranty &mdash; 8 years or 4,500 cycles &mdash; outlasts payback by a factor of four.</p>
<ul>
<li><strong>Energy per km:</strong> US$0.29 diesel vs US$0.13-0.15 electric (solar under US$0.10)</li>
<li><strong>Monthly saving per truck:</strong> US$570-770 including maintenance</li>
<li><strong>Payback:</strong> 14-26 months depending on charging source</li>
<li><strong>Cold chain:</strong> electric reefer on traction battery cuts field fuel and heat spikes</li>
<li><strong>Resilience:</strong> a 5-truck fleet carries 600+ kWh of mobile storage for farm-site backup</li>
</ul>
<p>Two softer factors move the same direction. EDENORTE and development-finance lines are starting to prefer electrified agro-logistics in their lending, which lowers the carry on the premium and pulls payback inward, and cooperative-owned fleets amortize chargers and solar across the harvest season rather than a single truck&rsquo;s books &mdash; so the cooperative&rsquo;s per-tonne transport cost falls faster than a private operator&rsquo;s would. Resale also favors the electric unit: the KT5L&rsquo;s value sits in the CATL pack the 8-year warranty protects, while a diesel&rsquo;s worth decays toward its next turbo and injector overhaul.</p>

<h2>Charging at the Cooperative Yard</h2>
<p>Santiago&rsquo;s industrial and agro-industrial zones have the medium-voltage capacity for depot charging; a ten-truck KT5L fleet runs on roughly 250-300 kVA with managed charging &mdash; a standard EDENORTE commercial connection. The practical layout: one 90-120 kW DC charger per 6-8 trucks for rotation, overnight AC at each bay, and load management matched to the harvest clock. The Cibao&rsquo;s solar resource (5.0-5.5 peak sun hours) makes a yard canopy the obvious first investment: 100-200 kWp offsets 40-55% of charging energy and doubles as covered staging for produce waiting on the packhouse line &mdash; covered, shaded produce is a quality win the exporters price directly.</p>
<p>Grid reliability, the honest concern, is manageable by design: the fleet&rsquo;s own batteries are the buffer. Ten KT5Ls carry over 1,300 kWh of storage; a two-hour outage is absorbed by resequencing charge sessions with zero operational impact. Cooperatives wanting harder resilience add a hybrid-inverter solar canopy that keeps chargers alive through outages &mdash; several Cibao packhouses already run solar for processing, and adding trucks to it is incremental.</p>

<h2>Import Path and Caribbean Context</h2>
<p>The Dominican Republic applies preferential duty treatment to electric vehicles under its electromobility decree, against 15-20% on diesel trucks, and Puerto Plata and Santo Domingo handle RoRo imports with 32-38 day sailings via transhipment. We supply the Spanish-language homologation dossier, UN R100 battery certification, and the two-year parts kit. Exporters with regional reach should also review our <a href="../markets/dominican-republic.html">Dominican Republic market page</a>, which covers the parallel Santo Domingo and Santiago freight ecosystems and the Haiti-border trade where the same KT5L platform serves both with shared parts and training.</p>
<p>After-sales ships with the trucks: a two-year fast-moving parts kit per fleet, CATL module stock reachable in 7-10 days via Panama, and telematics remote diagnostics with Spanish-language support. The drivetrain&rsquo;s maintenance calendar &mdash; brake inspections, coolant checks, software updates &mdash; removes the workshop dependency that grounds diesel trucks during peak harvest, which is the worst possible week to lose a truck.</p>

<h2>First Movers in the Cibao</h2>
<p>The strongest first adopters are the export-oriented cooperatives and packhouses with captive farm-to-port routes, the cocoa and tobacco processors whose premium shelves reward clean cold chain, and the produce distributors running fixed Santiago-Santo Domingo lanes. The Dominican fuel prices are not falling and the solar resource is not going away; the duty incentive is already law. The fleets that electrify their Cibao routes first bank a cost and sustainability advantage their diesel competitors cannot match &mdash; and in an export market where the buyer reads the carbon line, that advantage is increasingly the bid.</p>
'''))

# ---------------------------------------------------------------- 6
ARTICLES.append(dict(
f='medan-indonesia-palm-oil-electric-truck',
t='Medan Palm Oil Logistics: KTH3 Electric Trucks for North Sumatra Plantations',
d='North Sumatra palm oil haulage cuts cost with the KTH3 electric truck: 262 kWh, plantation solar charging. EV truck specs, ISPO sustainability and Indonesia import steps.',
k='KTH3 electric truck, EV truck Indonesia, electric truck Medan, electric cargo truck palm oil, Dongfeng electric truck, plantation haulage truck, North Sumatra electric truck',
img='models/p07_05.jpg',
alt='Dongfeng KTH3 electric cargo truck at a North Sumatra palm plantation, EV truck for Medan palm oil logistics',
net='zhc',
body='''
<p>Medan is the commercial capital of North Sumatra and the logistics hub for one of the world&rsquo;s largest palm oil producing regions &mdash; the mill-to-port and estate-to-mill haulage that moves fresh fruit bunches (FFB) from plantation to mill within hours of harvest, then crude palm oil and kernels from mill to the Belawan export terminal. That freight is short, repetitive, estate-based and brutally sensitive to two forces: the round-the-clock harvest clock (FFB must reach the mill within 24 hours or free fatty acid ruins the oil) and the ISPO sustainability certification that now gates access to European and premium buyers. This article examines the <a href="../products/models/kth3-electric-cargo-truck.html">Dongfeng KTH3 electric truck</a> for North Sumatra palm logistics: what the 262 kWh pack delivers on estate-to-mill runs, how plantation solar charging closes the loop, and how the Indonesian import path works. For a sector where sustainability is a sales license, an EV truck is both a cost play and a certification asset.</p>

<h2>The Plantation Haulage Duty Cycle</h2>
<p>Estate-to-mill haulage is the most predictable freight in Indonesian agri-logistics. FFB collection points sit 5-40 km from the mill, the trucks run fixed loops all day and return to the estate workshop every night &mdash; classic return-to-base duty. A KTH3 on this pattern covers 120-220 km daily across multiple short loops, at 20-40 km/h on estate roads with rolling laterite grades. The 262 kWh CATL LFP pack covers a full day of FFB shuttle with margin, and the estate workshop is the natural charger site. The mill-to-Belawan leg (Medan port, 20-30 km) and the mill-to-depots runs add a second wave that the same depot charging handles with a midday top-up. No public charging is required; the entire operation runs from the estate yard, which is exactly why plantation electrification is the lowest-risk EV truck entry in Southeast Asia.</p>
<p>The ISPO dimension is the strategic driver and it is specific to this sector. The Indonesian Sustainable Palm Oil (ISPO) standard &mdash; mandatory since 2020 and tightening toward Paris-aligned metrics &mdash; scores estates on emissions across the value chain, and Scope 1 (own diesel truck) emissions are the most visible line a mill controls directly. An electric FFB fleet converts that line from a liability to a certification strength, and premium buyers in the EU and Japan now ask for the transport emissions number specifically. A KTH3 fleet charged from estate solar is, on paper, a near-zero Scope 1 transport operation &mdash; a credential no diesel fleet can show.</p>

<h2>KTH3 Specifications for Estate Duty</h2>
<table style="width:100%;border-collapse:collapse;margin:20px 0;" border="1" cellpadding="8">
<tr style="background:#006341;color:#fff;"><th style="padding:8px;text-align:left;">Parameter</th><th style="padding:8px;text-align:left;">KTH3 6x4 Electric Cargo Truck</th></tr>
<tr><td style="padding:8px;">GVW / payload</td><td style="padding:8px;">28 t / 18-20 t (FFB or bulk body)</td></tr>
<tr><td style="padding:8px;">Battery</td><td style="padding:8px;">262 kWh CATL LFP, liquid-cooled</td></tr>
<tr><td style="padding:8px;">Motor</td><td style="padding:8px;">LvKong 360 kW peak / 2,400 Nm</td></tr>
<tr><td style="padding:8px;">Real-world range (loaded, estate profile)</td><td style="padding:8px;">200-240 km</td></tr>
<tr><td style="padding:8px;">DC charge 20-80%</td><td style="padding:8px;">~50 min at 240 kW</td></tr>
<tr><td style="padding:8px;">Gradeability</td><td style="padding:8px;">&ge;30% &mdash; laterite estate roads at load</td></tr>
<tr><td style="padding:8px;">Regeneration on estate descents</td><td style="padding:8px;">18-25% of round-trip energy recovered</td></tr>
<tr><td style="padding:8px;">Battery warranty</td><td style="padding:8px;">8 years / 4,500 cycles to 70% SOH</td></tr>
<tr><td style="padding:8px;">FOB price band</td><td style="padding:8px;">US$82,000-100,000</td></tr>
</table>
<p>The sealed HV system is the feature North Sumatra&rsquo;s climate demands. Estate roads flood in the November-March wet season and the laterite turns to slurry; the KTH3&rsquo;s HV system is sealed to IP67, the pack sits above the wading line, and there is no air intake, turbo or exhaust to ingest water and dust. The traction control modulates motor torque in milliseconds on slippery laterite, where a diesel&rsquo;s clutch and throttle response is an order of magnitude slower. Estates that run electric report fewer wet-season breakdowns and no flooded-engine write-offs &mdash; a real number in a region where a submerged diesel is a total loss.</p>

<h2>Indonesian TCO on the Estate</h2>
<p>Indonesian industrial diesel runs roughly US$0.75-0.85 per litre (B35 subsidized, but estate fleets buy commercial). A 28 t cargo truck on FFB duty burns 0.50-0.60 L/km; at US$0.80/L, about US$0.42 per kilometre. The KTH3 consumes 1.3-1.5 kWh/km on estate grades; at PLN industrial tariffs of roughly US$0.10-0.12/kWh, US$0.14-0.18 per kilometre, and at estate-solar effective cost of US$0.05-0.07/kWh, under US$0.10. On 200 km per day, 300 days a year, the grid-charged saving is roughly US$17,000-20,000 per truck annually; with solar it doubles to US$24,000-28,000. Maintenance &mdash; no engine, clutch or DPF, plus 3x brake life &mdash; adds US$5,000-7,000. Against a purchase premium of US$35,000-45,000, payback is 18-24 months grid-charged, 12-16 months with solar. The ISPO certification value sits on top of that and is not in the fuel math.</p>
<ul>
<li><strong>Energy per km:</strong> US$0.42 diesel vs US$0.14-0.18 grid (US$0.07 solar)</li>
<li><strong>Annual saving per truck:</strong> US$22,000-35,000 combined</li>
<li><strong>Payback:</strong> 12-24 months depending on charging source</li>
<li><strong>ISPO:</strong> near-zero Scope 1 transport line, premium-buyer credential</li>
<li><strong>Wet season:</strong> sealed HV, no flooded-engine losses, better traction control</li>
</ul>

<h2>Plantation Solar Hybrid Charging</h2>
<p>North Sumatra receives 4.0-4.5 peak sun hours daily, and every palm estate already has open land and a milling load &mdash; the natural hybrid is a 200-500 kWp solar canopy over the estate workshop and truck park, feeding the chargers and the mill&rsquo;s own load, with PLN grid as backup. A 300 kWp array offsets 45-60% of a 10-truck fleet&rsquo;s annual charging energy and pays for itself in under five years on charging load alone. We deliver the single-line diagram, the solar-hybrid controller config and the PLN interface pack with the truck order, because the charger and solar lead times usually exceed the 22-30 day vessel transit from China to Belawan. For estates already running biomass or solar at the mill, adding truck charging is the obvious next load to soak.</p>
<p>One operating note: the FFB clock means charging must fit the slack in the loop. Because the KTH3 charges during the natural meal and maintenance window and the trucks run fixed loops, the available hours align to the harvest shift rather than the refuel stop &mdash; no driver waiting at a diesel bowser while FFB ages in the trailer. Estates that sequence charging into the existing break structure report higher effective utilisation than the diesel fleet it replaces, which the TCO models above do not even count.</p>

<h2>Import Path and the Indonesian Context</h2>
<p>Indonesia exempts or reduces luxury tax and import duty on certified battery electric vehicles under its KBLBB program, and Belawan and Tanjung Priok handle RoRo truck imports with 22-30 day sailings from China and efficient customs for documented industrial vehicles. We supply the Indonesian-language homologation dossier where required, the SNI and Kemenperin references, and UN R100 battery certification. Groups with multi-island operations should also review our <a href="../markets/indonesia.html">Indonesia electric truck market page</a>, which covers the parallel Riau, Kalimantan and Sulawesi plantation and mining corridors where the same KTH3 platform serves both with shared parts and training.</p>
<p>After-sales ships with the trucks: a two-year fast-moving parts kit per fleet, CATL module stock reachable in 10-14 days, and telematics remote diagnostics with Bahasa and English support. The drivetrain&rsquo;s maintenance calendar &mdash; brake inspections, coolant checks, software updates &mdash; removes the workshop dependency that grounds diesel trucks during peak harvest, which is the worst possible week to lose a truck on an estate.</p>

<h2>First Movers in North Sumatra</h2>
<p>The natural first adopters are the integrated mills with captive estate-to-mill loops and their own power infrastructure &mdash; they control both ends of the duty cycle, can site solar and chargers at the workshop, and live the ISPO score every audit. Independent FFB transporters are second. The combination of short fixed loops, captive estate power, and a certification line that increasingly decides market access makes North Sumatra palm logistics the cleanest EV truck case in Southeast Asia. The estates that electrify first bank a cost and ISPO advantage their diesel competitors cannot answer &mdash; and the buyer is already asking for the number.</p>
'''))

# ---------------------------------------------------------------- 7
ARTICLES.append(dict(
f='penang-malaysia-electronics-electric-cargo-truck',
t='Penang Electronics Logistics: KT5M Electric Box Trucks for Malaysia&rsquo;s Silicon Island',
d='Penang semiconductor and E&E free-zone logistics suit the KT5M electric box truck: 180-220 kWh, MNC ESG-aligned. EV truck specs, TCO and Malaysia import guide.',
k='KT5M electric box truck, EV truck Malaysia, electric truck Penang, electric cargo truck semiconductor logistics, Dongfeng electric truck, free zone electric truck, E&E logistics',
img='models/p07_06.jpg',
alt='Dongfeng KT5M electric box truck at a Penang free-zone electronics plant, EV truck for Malaysia E&E logistics',
net='zhc',
body='''
<p>Penang is Malaysia&rsquo;s Silicon Island &mdash; the Batu Kawan and Bayan Lepas free zones host the封装 and test operations of the world&rsquo;s largest semiconductor and electronics firms, and the freight that feeds them is a precision ballet of just-in-time component delivery, subcontractor shuttles and finished-goods moves between plants, the Penang airport cargo terminal and the port of Butterworth. That freight is short, repetitive and governed by a force unique to this sector: the ESG and scope-3 transport requirements that multinational customers now write into supplier contracts. This article examines the <a href="../products/models/kt5m-electric-cargo-truck.html">Dongfeng KT5M electric box truck</a> for Penang&rsquo;s E&E logistics: what the 180-220 kWh pack delivers on free-zone shuttle runs, how the ESG case stacks with the cost case, and the Malaysian import path. For a sector where the buyer audits the truck, an EV truck is a contract requirement wearing a cost-saving suit.</p>

<h2>The Free-Zone Logistics Signature</h2>
<p>Semiconductor and E&E logistics is the most clock-disciplined freight in Malaysia. A box truck on this pattern runs fixed loops: component supplier to OSAT plant (5-25 km), plant to plant across the Bayan Lepas and Batu Kawan zones (10-40 km), plant to Penang airport cargo (20-30 km), or plant to Butterworth port (15-25 km). Daily distance is 80-160 km at steady 40-70 km/h, with gate queues at every secure facility. The KT5M&rsquo;s 200-240 km real-world range covers the longest day with 40% reserve, and the two-wave pattern (morning inbound, afternoon outbound) leaves a midday charge window. The trucks return to the same fenced, powered plant yard every night &mdash; return-to-base duty, the safest electric fit there is, and the reason Penang free zones electrify their fleets before the open road does.</p>
<p>The ESG driver is the differentiator and it is specific to Penang. The multinational principals &mdash; Intel, Bosch, AMD, Renesas and their tier-1 packagers &mdash; report transport emissions per shipment as scope-3, and they increasingly require logistics providers to show electric or certified-low-emission last-leg delivery. A silent, zero-exhaust KT5M on the early-morning component run is not just cheaper; it is a qualification criterion for the next contract. The free zones themselves market green logistics as a tenant benefit, and the parks that electrify first write it into their pitch decks. Penang&rsquo;s logistics economics therefore run on two parallel ledgers &mdash; cost and compliance &mdash; and the KT5M pays on both.</p>

<h2>KT5M Specifications for E&E Duty</h2>
<table style="width:100%;border-collapse:collapse;margin:20px 0;" border="1" cellpadding="8">
<tr style="background:#006341;color:#fff;"><th style="padding:8px;text-align:left;">Parameter</th><th style="padding:8px;text-align:left;">KT5M Electric Box Truck</th></tr>
<tr><td style="padding:8px;">GVW / payload</td><td style="padding:8px;">9-12 t class / 4.5-6 t payload</td></tr>
<tr><td style="padding:8px;">Battery</td><td style="padding:8px;">180-220 kWh CATL LFP</td></tr>
<tr><td style="padding:8px;">Motor</td><td style="padding:8px;">LvKong 150-190 kW peak / 1,100-1,500 Nm</td></tr>
<tr><td style="padding:8px;">Real-world range (free-zone, loaded)</td><td style="padding:8px;">200-240 km</td></tr>
<tr><td style="padding:8px;">DC charge 20-80%</td><td style="padding:8px;">~45 min at 120-150 kW</td></tr>
<tr><td style="padding:8px;">Body options</td><td style="padding:8px;">28-35 m&sup3; dry box, curtainside, temperature-controlled</td></tr>
<tr><td style="padding:8px;">Gradeability</td><td style="padding:8px;">&ge;25% at full load</td></tr>
<tr><td style="padding:8px;">Battery warranty</td><td style="padding:8px;">8 years / 4,500 cycles to 70% SOH</td></tr>
<tr><td style="padding:8px;">FOB price band</td><td style="padding:8px;">US$50,000-64,000</td></tr>
</table>
<p>The temperature-controlled variant deserves a paragraph because Malaysian E&E and some pharma-adjacent freight moves under controlled humidity and temperature, and the KT5M&rsquo;s electric HVAC draws from the traction battery instead of a diesel unit burning in the yard. A temperature-controlled KT5M holds setpoint from supplier to cleanroom dock on traction energy alone, cutting both fuel cost and the heat spikes that matter for sensitive components. For 3PLs serving the principal&rsquo;s quality specs, that is a measurable compliance win the diesel box truck cannot show.</p>

<h2>Malaysian TCO on the Island</h2>
<p>Malaysian industrial diesel runs roughly US$0.70-0.80 per litre. A 9-12 t box truck on Penang free-zone duty burns 0.30-0.38 L/km including gate idle &mdash; about US$0.25 per kilometre. The KT5M consumes 0.75-0.90 kWh/km; at TNB industrial tariffs of roughly US$0.10-0.12/kWh, US$0.09-0.11 per kilometre. On 4,000 km per month (two-wave free-zone duty), the monthly energy saving is about US$640 per truck. Maintenance adds US$200-300 monthly &mdash; no oil, clutch, injectors or DPF, brakes lasting 2-3x longer. Against a purchase premium of US$18,000-25,000, payback lands at 18-24 months. For the temperature-controlled variant the case strengthens because the electric HVAC displaces the most expensive diesel in the operation, and for the ESG-bound 3PL the contract-retention value sits on top of the fuel math.</p>
<ul>
<li><strong>Energy per km:</strong> US$0.25 diesel vs US$0.10 electric &mdash; a 60% reduction</li>
<li><strong>Monthly saving per truck:</strong> ~US$840-940 on two-wave duty</li>
<li><strong>Payback:</strong> 18-24 months; faster for temperature-controlled variants</li>
<li><strong>Gate queues:</strong> 20-30% of diesel idle fuel eliminated</li>
<li><strong>ESG:</strong> zero-exhaust last leg meets MNC scope-3 transport requirements</li>
</ul>
<p>Financing and resale tilt the same way. Malaysian green-vehicle incentives and development-finance leasing lines discount certified electric trucks, lowering the effective monthly carry on the premium and pulling payback inward, and the KT5M&rsquo;s value concentrates in the CATL pack the 8-year warranty protects &mdash; so a mid-life unit retains a battery asset the diesel&rsquo;s engine rebuild cannot match, which matters for the 3PLs that rotate fleets every three to four years.</p>

<h2>Charging Inside the Free Zones</h2>
<p>Penang&rsquo;s free zones have excellent medium-voltage capacity &mdash; the parks were built for fab-grade power &mdash; so depot charging is a tenant-load coordination question more than a capacity one. A ten-truck KT5M fleet runs on roughly 300-350 kVA with managed charging. The practical layout: one 120-150 kW DC charger per 6-8 trucks for rotation, overnight AC at each bay, and load management matched to the plant shift schedule. Malaysia&rsquo;s solar resource (4.5-5.0 peak sun hours on the island) makes a plant-canopy array strongly economic: 150-250 kWp offsets 40-55% of charging energy and provides covered, shaded staging that protects sensitive cargo during loading. We deliver the single-line diagram, load-management config and TNB interface pack with the truck order.</p>
<p>A sizing note for growth-bound 3PLs: Penang&rsquo;s semiconductor volumes track the global up-cycle, and electrification kit should be specified for the month-24 fleet, not month one. We size switchboards and conduits for double the initial charger count; the marginal cost at construction is trivial and eliminates the most expensive retrofit in fleet electrification, which is re-digging the yard.</p>

<h2>Import Path and the Malaysian Context</h2>
<p>Malaysia grants import duty and excise exemptions on approved battery electric commercial vehicles under its green-vehicle framework, and Penang and Port Klang handle RoRo truck imports with 12-18 day sailings from China and efficient customs for documented vehicles. We supply the English and Bahasa Malaysia homologation dossier, the SIRIM and JPJ references where required, and UN R100 battery certification. Logistics groups with multi-corridor operations should also review our <a href="../markets/malaysia.html">Malaysia electric truck market page</a>, which covers the parallel Kulim, Johor and Klang Valley electronics and port corridors where the same KT5M platform serves both with shared parts and training.</p>
<p>After-sales ships with the trucks: a two-year fast-moving parts kit per fleet, CATL module stock reachable in 7-10 days, and telematics remote diagnostics with English and Bahasa support. The drivetrain&rsquo;s maintenance calendar &mdash; brake inspections, coolant checks, software updates &mdash; removes the workshop dependency that grounds diesel trucks during peak production weeks, which is the worst time to lose a component shuttle.</p>

<h2>First Movers on Silicon Island</h2>
<p>The strongest first candidates are the free-zone 3PLs and the in-house logistics arms of the OSAT andEMS firms with captive plant-to-port routes. Their utilisation is the highest, their yards are secured and powered by fab-grade infrastructure, and their principals are already demanding electrified inbound logistics as a scope-3 lever. Penang built its semiconductor reputation on precision and compliance; electrifying the shuttle that feeds the line is the next precision step, and the fleets that take it first bank a cost and ESG advantage their diesel competitors cannot answer &mdash; and in this sector, the ESG line is increasingly the bid.</p>
'''))

# ---------------------------------------------------------------- 8
ARTICLES.append(dict(
f='clark-philippines-logistics-hub-electric-truck',
t='Clark Freeport Zone: KT5J Electric Delivery Trucks for the Philippines&rsquo; Rising Logistics Hub',
d='Clark Freeport Zone e-commerce and airport-city freight suit the KT5J electric delivery truck: 106-130 kWh, FOB US$45-56k. EV truck specs, TCO and Philippines import guide.',
k='KT5J electric delivery truck, EV truck Philippines, electric truck Clark, electric delivery truck Clark Freeport, Dongfeng electric truck, e-commerce logistics truck, Manila decongestion freight',
img='models/p07_08.jpg',
alt='Dongfeng KT5J electric delivery truck at the Clark Freeport Zone, EV truck for Philippines logistics hub',
net='zhc',
body='''
<p>Clark is the Philippines&rsquo; fastest-rising logistics hub &mdash; the old airbase is now a freeport zone and international airport city, the northern anchor of the Manila decongestion strategy, and the fulfillment backbone for the country&rsquo;s exploding e-commerce volumes. Freight moves from the Clark airport cargo terminal and the freeport warehouses to Metro Manila (90-110 km south), to Subic (40 km west), and across the Central Luzon growth corridor, while a rising share of e-commerce fulfillment is now sited inside Clark itself to escape Manila&rsquo;s gridlock. This article examines the <a href="../products/models/kt5j-electric-cargo-truck.html">Dongfeng KT5J electric delivery truck</a> for exactly that role: what the 106-130 kWh pack delivers on Clark-Metro and in-zone runs, how it supports the Manila decongestion play, and the Philippine import path. For a hub whose entire thesis is moving freight off Manila&rsquo;s streets, an EV truck is the aligned tool &mdash; and at a FOB band of US$45-56k it is an accessible one.</p>

<h2>Why Clark Electrifies Naturally</h2>
<p>Clark&rsquo;s freight splits into two clean electric profiles. The first is in-zone e-commerce and airport-city distribution: short 5-30 km loops from freeport warehouses to the airport cargo terminal, the hotels and the growing residential grids, returning to the same yard nightly. The second is the Clark-to-Metro Manila corridor: 90-110 km one way, run as a round trip of 180-220 km that sits right at the top of the KT5J&rsquo;s 180-220 km real-world range, with a 20-30 minute top-up at a Metro depot or the Clark yard on return. Both are return-to-base or fixed-corridor duty &mdash; the safest electric fit &mdash; and both avoid the public-charging dependency that sinks open-road EV truck plans. The KT5J&rsquo;s 106-130 kWh CATL LFP pack is sized for exactly this: high daily utilisation on short-to-medium loops, not fantasy long-haul range.</p>
<p>The Manila decongestion thesis is the strategic driver. Every container and parcel shifted to a Clark-based fulfillment and transport node is one fewer truck fighting EDSA gridlock, and the national logistics strategy explicitly favors Clark as the northern relief valve. An electric delivery fleet based in Clark is the purest expression of that strategy: it operates from the freeport&rsquo;s clean infrastructure, serves Metro Manila without adding to its air-quality problem, and reads as the modern logistics brand the BPO and e-commerce tenants want adjacent to. For 3PLs winning Philippine e-commerce contracts, the Clark-electric story is a pitch point, not a footnote.</p>

<h2>KT5J Specifications for Clark Duty</h2>
<table style="width:100%;border-collapse:collapse;margin:20px 0;" border="1" cellpadding="8">
<tr style="background:#006341;color:#fff;"><th style="padding:8px;text-align:left;">Parameter</th><th style="padding:8px;text-align:left;">KT5J Electric Delivery Truck</th></tr>
<tr><td style="padding:8px;">GVW / payload</td><td style="padding:8px;">7.5-9 t class / 3.5-4.5 t payload</td></tr>
<tr><td style="padding:8px;">Battery</td><td style="padding:8px;">106-130 kWh CATL LFP</td></tr>
<tr><td style="padding:8px;">Motor</td><td style="padding:8px;">LvKong 120-150 kW peak / 950-1,200 Nm</td></tr>
<tr><td style="padding:8px;">Real-world range (loaded, mixed)</td><td style="padding:8px;">180-220 km</td></tr>
<tr><td style="padding:8px;">DC charge 20-80%</td><td style="padding:8px;">~35 min at 90-120 kW</td></tr>
<tr><td style="padding:8px;">Body options</td><td style="padding:8px;">22-28 m&sup3; box, side-door, tail-lift</td></tr>
<tr><td style="padding:8px;">Turning circle</td><td style="padding:8px;">~11.8 m &mdash; Metro side-street friendly</td></tr>
<tr><td style="padding:8px;">Battery warranty</td><td style="padding:8px;">8 years / 4,500 cycles to 70% SOH</td></tr>
<tr><td style="padding:8px;">FOB price band</td><td style="padding:8px;">US$45,000-56,000</td></tr>
</table>
<p>The body configuration matters for Clark&rsquo;s e-commerce freight: the side-door option converts condo and warehouse street-side unloading from a rear-door bottleneck into a parallel operation, and the tail-lift variant eliminates the manual handling that slows last-mile drops. We specify bodies per route &mdash; in-zone e-commerce fleets take the side-door box, Metro fulfillment fleets take the tail-lift &mdash; because the 15-25 minutes saved per stop compounds across a 20-30 stop day into an extra delivery wave. At a FOB band of US$45-56k the KT5J is also the most affordable electric truck in our export range, which matters for the price-sensitive Philippine 3PL market where diesel trucks still dominate the parc.</p>

<h2>Philippine TCO on the Corridor</h2>
<p>Philippine diesel runs roughly US$1.00-1.10 per litre. A 7.5-9 t box truck on Clark duty burns 0.26-0.32 L/km &mdash; about US$0.30 per kilometre. The KT5J consumes 0.60-0.75 kWh/km; at Meralco and distribution utility commercial tariffs of roughly US$0.17-0.20/kWh, US$0.12-0.15 per kilometre. On 4,000 km per month (two-wave Clark-Metro and in-zone duty), the monthly energy saving is about US$600-720 per truck. Maintenance adds US$150-250 monthly &mdash; no oil, clutch, injectors or DPF, brakes lasting 2-3x longer. Against a purchase premium of US$15,000-20,000 over a diesel equivalent, payback lands at 18-24 months. The Clark-Metro corridor trucks, running higher daily kilometres, see the stronger end of that range, and the CATL battery warranty &mdash; 8 years or 4,500 cycles &mdash; outlasts payback by a factor of four.</p>
<ul>
<li><strong>Energy per km:</strong> US$0.30 diesel vs US$0.13 electric &mdash; a 57% reduction</li>
<li><strong>Monthly saving per truck:</strong> ~US$750-970 including maintenance</li>
<li><strong>Payback:</strong> 18-24 months on mixed Clark duty</li>
<li><strong>Manila decongestion:</strong> Clark-based fulfillment removes trucks from EDSA gridlock</li>
<li><strong>Entry price:</strong> US$45-56k FOB &mdash; the most accessible electric truck in the range</li>
</ul>

<h2>Charging at the Freeport</h2>
<p>Clark Freeport Zone has fab- and airport-grade medium-voltage capacity, so depot charging is straightforward: a ten-truck KT5J fleet runs on roughly 250-350 kVA with managed charging. The practical layout: one 90-120 kW DC charger per 6-8 trucks for rotation, overnight AC at each bay, and load management matched to the dispatch clock. The Philippines&rsquo; solar resource (4.5-5.0 peak sun hours) makes a freeport canopy array strongly economic: 100-150 kWp offsets 35-45% of charging energy and provides covered staging. We deliver the single-line diagram, load-management config and the utility interface pack with the truck order, because the 8-12 week connection lead time is the critical path and usually exceeds the 12-18 day vessel transit from China to Subic or Manila.</p>
<p>Grid reliability, the honest Philippine concern, is manageable by design: the fleet&rsquo;s own batteries are the buffer. Ten KT5Js carry over 1,100 kWh of storage; a two-hour outage is absorbed by resequencing charge sessions with zero operational impact. Fleets wanting harder resilience add a hybrid-inverter solar canopy that keeps chargers alive through outages &mdash; several Clark warehouses already run solar for operations, and adding trucks to it is incremental.</p>

<h2>Import Path and the Philippine Context</h2>
<p>The Philippines applies reduced tariffs and the electric vehicle promotion program incentives on certified battery electric commercial vehicles, and Subic and Manila handle RoRo truck imports with 12-18 day sailings from China and efficient customs for documented vehicles. We supply the English and Filipino homologation dossier, the LTO and BOI references where required, and UN R100 battery certification. Logistics groups with Visayas and Mindanao operations should also review our <a href="../markets/philippines.html">Philippines electric truck market page</a>, which covers the parallel Cebu and Davao port corridors where the same KT5J platform serves both with shared parts and training.</p>
<p>After-sales ships with the trucks: a two-year fast-moving parts kit per fleet, CATL module stock reachable in 10-14 days, and telematics remote diagnostics with English and Filipino support. The drivetrain&rsquo;s maintenance calendar &mdash; brake inspections, coolant checks, software updates &mdash; removes the workshop dependency that grounds diesel trucks during peak sale seasons, which is the worst week to lose a delivery truck.</p>

<h2>First Movers in the Freeport</h2>
<p>The strongest first candidates are the e-commerce 3PLs and the in-house logistics arms of the BPO and retail groups with captive Clark-to-Metro and in-zone routes. Their utilisation is the highest, their yards are secured and powered by freeport-grade infrastructure, and their customers &mdash; the e-commerce platforms with scope-3 and urban-air-quality commitments &mdash; will pay attention to zero-emission last legs. Clark built its logistics thesis on decongesting Manila; electrifying the delivery fleet that serves the hub is the logical next step, and at a US$45-56k FOB entry the fleets that move first bank a cost and brand advantage their diesel competitors cannot match.</p>
'''))

# __MORE__

for a in ARTICLES:
    html = build(a)
    path = os.path.join(ROOT, 'blog', a['f'] + '.html')
    with open(path, 'w', encoding='utf-8') as fh:
        fh.write(html)
    words = len(re.sub(r'<[^>]+>', ' ', a['body']).split())
    print('%-58s %5d words' % (a['f'], words))
print('done batch3:', len(ARTICLES))
