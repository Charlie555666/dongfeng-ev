# -*- coding: utf-8 -*-
import os, re

BLOG = r"C:\Users\69498\WorkBuddy\20260605101515\dongfeng-ev-repo\blog"
CTA_MARK = '<p style="margin-top:40px;padding:16px;background:#f0f7f4;'

# per-file unique closing sections (inserted before CTA)
S = {}

S["johannesburg-gauteng-electric-truck-freight.html"] = """
<h2>The Gauteng Checklist Before You Order</h2>
<p>Before converting a single Gauteng truck, our engineering desk asks operators to complete six pieces of homework — the same questionnaire we run in every market, tuned for Reef conditions:</p>
<ul>
<li><strong>Route logs for 90 days:</strong> kilometres, gate-queue minutes and load factors per truck — the fuel and idle data that decides which routes convert first.</li>
<li><strong>Site access audit:</strong> weighbridge limits, site-gate widths and tip restrictions on your active projects, which decide the 6x4-versus-8x4 question per corridor.</li>
<li><strong>Depot power enquiry:</strong> written confirmation from the municipality or Eskom distribution on available capacity at your yard — before truck contracts, not after.</li>
<li><strong>Tariff structure review:</strong> whether your account qualifies for time-of-use pricing that rewards the overnight charging window.</li>
<li><strong>Maintenance crew baseline:</strong> which of your technicians will take the HV certification at handover, and their retention plan — the same discipline the driver-retention piece in this blog covers.</li>
<li><strong>Tender calendar mapping:</strong> which of your upcoming Gauteng bids carry sustainability scoring that an electric fleet can win outright.</li>
</ul>
<p>Operators who arrive at the ordering table with these six answers typically cut their procurement timeline in half — because the truck specification, the charger count and the financing structure all fall out of the data rather than out of debate. The Reef's diesel prices, load-shedding-buffered tariffs and construction pipeline are not waiting for consensus; the first movers are already quoting electric options into tenders their competitors cannot match.</p>
"""

S["lahore-pakistan-electric-delivery-truck-fleet.html"] = """
<h2>The Lahore Pilot Kit: What Operators Prepare</h2>
<p>Our Lahore conversions run on a standard preparation checklist that removes most first-fleet risk before a single KT5J boards a vessel at Shanghai:</p>
<ul>
<li><strong>A 90-day diesel ledger:</strong> per-truck fuel, idle hours and maintenance spend on the two routes being converted — the baseline the electric fleet will be measured against.</li>
<li><strong>A night-band power contract:</strong> the LESCO/IESCO time-of-use arrangement that turns the charging window into the cheapest energy in the operation.</li>
<li><strong>A load-shedding map of the feeder:</strong> documented outage windows for the depot feeder over the last quarter, which sizes the BESS buffer honestly.</li>
<li><strong>A customs broker briefing:</strong> our documentation package reviewed with the importer's broker in advance, so the EV tariff lines are entered correctly the first time — misclassification is the most expensive paperwork error in Pakistani imports.</li>
<li><strong>A driver roster of the top performers:</strong> Lahore's best diesel drivers are the first electric drivers; the training week converts them, and the retention piece in this blog explains why that choice pays for itself.</li>
<li><strong>An anchor customer conversation:</strong> the FMCG or e-commerce shipper whose sustainability scorecard will reward the switch — many Lahore shippers now ask.</li>
</ul>
<p>With that kit in hand, a five-truck pilot is a six-week exercise from order to data, and the expansion decision usually makes itself before the pilot quarter ends. Pakistan's import window is open, Punjab's grid is cheaper than its diesel by three to one, and Lahore's distribution geometry was drawn for exactly this fleet.</p>
"""

S["guadalajara-mexico-electric-delivery-truck.html"] = """
<h2>Next Steps for Jalisco Operators</h2>
<p>Guadalajara buyers evaluating the conversion can run a compressed evaluation that produces a decision-grade dataset in one quarter, using our standard instruments:</p>
<ul>
<li><strong>Route instrumentation:</strong> 60-90 days of GPS, idle-time and load data on the candidate loops — the Inner Ring first, where the idle share is highest.</li>
<li><strong>CFE tariff review:</strong> confirm the depot's commercial rate class and whether a TOU migration makes sense before the chargers are specified.</li>
<li><strong>NOM and broker pre-clearance:</strong> our conformity documentation package reviewed by the Manzanillo-side broker so the entry class and duty treatment are fixed before shipping.</li>
<li><strong>A five-truck pilot order:</strong> KT5J units on the two densest loops, one dual-gun 120 kW charger, and a written comparison protocol against the incumbent diesel units.</li>
<li><strong>A shipper conversation:</strong> Jalisco's electronics and food brands increasingly reward logistics partners with documented emission reductions — turn the pilot's telematics into tender material.</li>
</ul>
<p>Jalisco's mix — mild climate, industrial depth, short radii and one of Latin America's widest fuel-power price spreads — makes it a top-three metro in the region for first-fleet economics. The evaluation work is a fortnight of desk effort; the first-mover advantage it protects is measured in years.</p>
"""

S["cali-colombia-sugar-corridor-electric-truck.html"] = """
<h2>What Valle Fleet Managers Should Do Next</h2>
<p>For mill operators and construction fleets ready to evaluate the switch, the sequence that works in the Valle is specific:</p>
<ul>
<li><strong>Run the zafra baseline:</strong> instrument the incumbent diesel fleet's fuel, idle and downtime for one full harvest — the seasonal data the electric comparison must beat.</li>
<li><strong>Model the bagasse-mill tariff:</strong> mills that co-generate should price fleet charging at internal transfer cost, which changes the payback table in the article above by half.</li>
<li><strong>Check axle enforcement on your corridors:</strong> the Cauca valley's bridge and weight controls decide the 6x4-versus-8x4 mix per route — our engineering desk runs this against your route logs.</li>
<li><strong>Time the pilot to the calendar:</strong> trucks arriving just before the harvest start, charged and commissioned, convert the season's data into the expansion order by the season's end.</li>
<li><strong>Confirm the tariff line at customs:</strong> our Colombian documentation package pre-clears the EV classification so the preferential treatment survives the broker's first draft.</li>
</ul>
<p>The Valle del Cauca is one of the few places in the world where the freight corridor, the fuel price and the electricity source all point the same direction at once — flat terrain, among South America's highest diesel prices, and mills that literally make their own power. The sugar corridor's electrification is not a question of economics; it is a question of which mill signs first.</p>
"""

S["bangkok-thailand-electric-truck-urban-logistics.html"] = """
<h2>The Bangkok Conversion Checklist</h2>
<p>Thai operators preparing a first Bangkok fleet can compress the evaluation into a structured six-week exercise:</p>
<ul>
<li><strong>Instrument the candidate routes:</strong> 60 days of stop counts, idle minutes and load factors on the two densest loops — Inner-Ring modern-trade replenishment converts fastest.</li>
<li><strong>Confirm the depot metering position:</strong> whether the warehouse's MEA account sits on a TOU-eligible tariff, and what the off-peak window does to the charging schedule.</li>
<li><strong>Survey flood exposure:</strong> the depot's flood history and the 2011 line — charger plinths and switchgear sit above it in our standard layout.</li>
<li><strong>Review the reefer option:</strong> distribution fleets running chilled or temperature-sensitive cargo should price the factory electric reefer body against the diesel donk it replaces — the compound saving usually decides.</li>
<li><strong>Engage the corporate shippers early:</strong> the modern-trade and FMCG accounts that dominate Thai logistics contracts now carry Scope 3 questions of their own; the pilot's data becomes next year's tender annex.</li>
<li><strong>BoI and duty pre-clearance:</strong> our documentation set reviewed with the importer's agent so the EV import treatment is entered correctly at the port.</li>
</ul>
<p>Bangkok's duty cycles are among the most electric-favourable on earth — the traffic that punishes diesel rewards the drivetrain that idles for free. The fleets that convert their first ten trucks this year will hold the cost and compliance position when the city's delivery sector renewals accelerate through the decade.</p>
"""

S["almaty-kazakhstan-electric-truck-distribution.html"] = """
<h2>The Almaty Winter Pilot: How to Run It Right</h2>
<p>Kazakh fleets convert sceptics with data, so the pilot design is everything. The structure that has worked in comparable cold-climate deployments:</p>
<ul>
<li><strong>Pilot through one full winter:</strong> trucks arriving in late summer give the fleet one complete cold season of consumption, charging and cabin-comfort data — the dataset that answers every board question at once.</li>
<li><strong>Charge inside:</strong> Almaty depots that park trucks in a heated or semi-heated yard cut the pack pre-heating load and protect connector hardware — our depot layouts for Central Asia assume it.</li>
<li><strong>Log the pre-heat ritual:</strong> drivers plug in at shift end and the BMS conditions the pack on shore power before morning — the discipline that keeps January range at its planned figure.</li>
<li><strong>Track driver adoption:</strong> the heated cabin and instant cold-start torque are retention weapons in a market where diesel cold-starts at minus 25 are a daily misery; the league-table mechanics described elsewhere in this blog transfer directly.</li>
<li><strong>Keep the diesel comparison honest:</strong> the winter baseline should include the diesel fleet's pre-heat idling and cold-start maintenance — costs the ledger forgets and the electric fleet deletes.</li>
</ul>
<p>Almaty's grid, its EV import treatment and its dense metro distribution make the economics work before any subsidy is counted — the cold is an engineering variable with engineering answers, not a veto. The operators who run the winter pilot first will own the spring expansion.</p>
"""

S["jeddah-saudi-electric-truck-port-logistics.html"] = """
<h2>The Jeddah Drayage Entry Plan</h2>
<p>Contractors moving containers at Jeddah Islamic Port can structure a first electric fleet in five moves:</p>
<ul>
<li><strong>Map the queue data:</strong> two weeks of gate and weighbridge timestamps tell you where the idle minutes — and therefore the savings — concentrate, and whether opportunity charging at the yard gate earns its capex.</li>
<li><strong>Confirm the depot supply:</strong> the industrial feed at the yard and the headroom for three 240 kW dispensers, with the solar-carport option priced against the grid tariff.</li>
<li><strong>Choose the mission split:</strong> TE46-class tractors on the metro drayage legs, TE8M-class on the heavier intermodal runs — the configuration table in our spec-sheet guide applies directly.</li>
<li><strong>Pre-clear SASO and Saber:</strong> our conformity documentation and heat-spec file enter the platform before the trucks sail, so the port that receives them is the port they serve.</li>
<li><strong>Quote the ESG annex:</strong> port operators and their shipping-line customers increasingly score drayage emissions — the pilot's telematics ledger becomes next year's bid document.</li>
</ul>
<p>Red Sea drayage is a fixed-radius, depot-anchored, idle-heavy mission under one of the world's best solar resources — the combination that makes electric conversion a cost decision rather than a policy gesture. The first contractor to sign the depot charging agreement holds the price position while the others study the question.</p>
"""

S["abu-dhabi-electric-sanitation-fleet.html"] = """
<h2>Bidding the Electric Fleet: A Contractor's Preparation List</h2>
<p>For Emirate sanitation contractors preparing to bid with an electric fleet, the preparation that scores is specific:</p>
<ul>
<li><strong>Route-level duty data:</strong> tonnage, kilometres and compactor hours per round from the incumbent operation — the baseline the electric TCO table must beat line by line.</li>
<li><strong>A depot power agreement:</strong> written capacity at the concession yard for the charger bank, sized for the fleet plus the growth the concession contract implies.</li>
<li><strong>The night-shift schedule overlay:</strong> charge windows mapped against the round schedule, showing the concession authority that no operational hour is lost to charging.</li>
<li><strong>Washdown and corrosion SOPs:</strong> the leachate-and-washdown maintenance regime from our waste-fleet package, attached to the bid as evidence the fleet will hold its availability through the contract term.</li>
<li><strong>The emissions reporting annex:</strong> the telematics kWh ledger that converts directly into the tender's environmental scoring section — points a diesel bid cannot reach.</li>
<li><strong>Driver retention data:</strong> Emirate tender evaluators increasingly ask about workforce metrics; the cooled, quiet electric cab is a retention instrument with numbers behind it.</li>
</ul>
<p>Abu Dhabi's sanitation economics favour the electric fleet more strongly than almost any Gulf segment — the idle-heavy duty, the cheap night power and the municipal ESG mandate all compound. The concessionaires who bid electric first will set the cost benchmark the next round is awarded against.</p>
"""

S["davao-philippines-agri-electric-truck.html"] = """
<h2>What Mindanao Operators Should Prepare</h2>
<p>Davao-region fleets evaluating the conversion can prepare in six moves, the same instruments we run across our Philippine deployments:</p>
<ul>
<li><strong>Harvest-calendar mapping:</strong> the daily tonnage profile of the candidate loops across the year, so the fleet is sized on the season's reality, not its peak fantasy.</li>
<li><strong>A packing-house power agreement:</strong> the mill or plant's substation headroom for two to three dual-gun chargers — the depot that makes the whole model work.</li>
<li><strong>EVIDA and BOI paperwork early:</strong> the incentive registration our Philippines package pre-structures, entered before the vessels sail so the duty treatment lands with the trucks.</li>
<li><strong>A solar feasibility read:</strong> Davao's irradiance makes a 100-200 kW roof array a hedge worth pricing against grid outages in the same proposal.</li>
<li><strong>An export-customer conversation:</strong> for banana and fruit shippers, the electric farm-to-port chain is a Scope 3 line item the Japanese and Korean trading houses now ask about in supplier audits.</li>
<li><strong>A driver training week:</strong> our commissioning package includes it; Mindanao's rural ramps make the instant-torque advantage a daily felt experience, and adoption follows.</li>
</ul>
<p>Mindanao's advantage is structural — cheap hydro-backed power, disciplined agri-haul schedules and export customers who audit emissions — and the region's competitors are only now noticing. The first co-op or plant that converts its hauling fleet converts its cost line and its audit narrative at once.</p>
"""

S["da-nang-vietnam-electric-truck-port-city.html"] = """
<h2>The Central Coast Entry Sequence</h2>
<p>Da Nang operators can stage a first fleet against the city's clearest opportunities in five steps:</p>
<ul>
<li><strong>Pick the hospitality corridor first:</strong> the tourism supply chains around My Khe and the Son Tra peninsula already prefer quiet, zero-exhaust delivery — the easiest contracts to convert and the easiest story to sell.</li>
<li><strong>Instrument the metro loops:</strong> 60 days of drops, idle and load data on the candidate routes, which sizes the KT5M order and the depot's charger count honestly.</li>
<li><strong>Anchor the depot at the warehouse district:</strong> the Hoa Khanh or An Khe yard, with EVN's commercial tariff and the night window doing the heavy lifting on cost.</li>
<li><strong>Add the drayage pair second:</strong> two TE8M tractors on the Tien Sa gate runs, with the weighbridge dwell study deciding whether an opportunity-charge bay earns its place at the port end.</li>
<li><strong>Pre-clear conformity:</strong> our Vietnamese documentation package rides with the shipment, so the ACFTA preferential entry and the BEV registration treatment both apply at first entry.</li>
</ul>
<p>Central Vietnam's growth corridor is scheduled through the decade — port capacity, industrial zones and tourism capacity all expanding at once — and every new tonne it generates is cheapest moved on electricity. The fleets that hold the electrified depot sites around Lien Chieu will run the corridor's cheapest freight from day one.</p>
"""

S["oran-algeria-electric-truck-port-fleet.html"] = """
<h2>What West Algerian Operators Should Do With This</h2>
<p>Given the subsidy reality, the honest sequencing for an Oran-region fleet is deliberate:</p>
<ul>
<li><strong>Target the enclosed and night-ops duty first:</strong> tunnel and utility projects, port-adjacent haulage and night road works — the missions where zero-exhaust is worth money today, regardless of the fuel subsidy.</li>
<li><strong>Price the hedge honestly:</strong> run the fleet model at both current diesel prices and market-adjacent prices — the second column is the risk the electric fleet removes, and boards should see both.</li>
<li><strong>Anchor at an industrial tenant:</strong> the Arzew complex, a cement plant or the port operator — the partner whose HSE regime and substation make the first depot trivial.</li>
<li><strong>Structure the import path early:</strong> licensed-importer and project-regime routes take months to arrange in Algeria; our documentation and French-language technical files are designed to start that clock immediately, not after the trucks are chosen.</li>
<li><strong>Start with the maintenance dividend:</strong> even at subsidised diesel, the drivetrain savings in Oran's dust and heat are USD 4,000-5,500 per truck-year — the argument that survives any fuel policy.</li>
</ul>
<p>West Algeria is a patience market with a genuine prize: when diesel reprices — by reform, rationing or simple arithmetic — the fleets that already run electric will hold the only cost base in the region that does not move. The pilot ordered now is the hedge that pays then.</p>
"""

S["takoradi-ghana-manganese-electric-truck.html"] = """
<h2>The Ghana Entry Playbook</h2>
<p>Fleets and mining contractors on the western corridor can move from interest to first fleet in a defined sequence:</p>
<ul>
<li><strong>Run the duty study:</strong> weighbridge, cycle counts and fuel ledgers on the Nsuta and Awaso runs for 60 days — the data that sizes the TE46/KTA1 mix and the depot charger count.</li>
<li><strong>Confirm the duty exemption in writing:</strong> Ghana's EV import treatment is a live budget item; our Ghana quotations verify the current position with the importer's broker at entry time.</li>
<li><strong>Split the depot:</strong> chargers at both the mine end and the port stockyard, so the corridor's two natural dwell points become the two charging windows.</li>
<li><strong>Attach the ESG annex to the next mining-services bid:</strong> the manganese and bauxite operators' contractor frameworks score emissions — the fleet's kWh ledger is tender material, as our tender-strategy piece details.</li>
<li><strong>Schedule around the harmattan:</strong> the dust season's shortened filter intervals belong in the maintenance plan from day one, not discovered in year two.</li>
</ul>
<p>Ghana's duty exemption, its hydro-heavy grid and its institutionalised mining ESG make the western corridor one of the strongest heavy-electric cases in West Africa — the arithmetic closes before any subsidy is counted. The first contractor to electrify the manganese runs will price the next concession bid with a cost line its competitors cannot reach.</p>
"""

S["eldoret-kenya-tea-highlands-electric-truck.html"] = """
<h2>The Rift Valley Conversion Sequence</h2>
<p>Kenyan Rift operators can run a first-fleet conversion in five defined steps:</p>
<ul>
<li><strong>Instrument the two densest loops:</strong> the mill-to-distributor and the dairy or leaf collection runs — 90 days of diesel baselines including brake wear, which the Rift's grades make the honest comparison's largest line.</li>
<li><strong>Anchor charging at the mill or factory:</strong> the compound's existing substation hosts the charger bank; our Kenyan depot layouts assume the plant-gate depot from day one.</li>
<li><strong>Verify the duty exemption at entry:</strong> our Kenyan documentation package carries the EV tariff-line evidence the clearing agent needs — misclassification forfeits the policy dividend that makes Kenya exceptional.</li>
<li><strong>Price the reefer option where temperature matters:</strong> dairy and horticulture loops should compare the factory electric reefer body against the diesel compressor unit it replaces — the audit-friendly temperature log is worth as much as the fuel saving.</li>
<li><strong>Book driver training at commissioning:</strong> the highland descents reward regenerative technique handsomely, and the first two weeks of coaching set the consumption baseline for the fleet's life.</li>
</ul>
<p>The Rift's advantages stack unusually high — altitude where electric outperforms diesel, gradients that feed the pack, factory-gate depots, and a national policy framework that discounts the trucks at the border. Eldoret's renewals this decade are the opportunity; the arithmetic above says electrify them.</p>
"""

S["port-harcourt-nigeria-electric-truck-logistics.html"] = """
<h2>Structuring a Delta Pilot That Survives Scrutiny</h2>
<p>Oil-services and distribution fleets in Rivers State can de-risk a first electric fleet with six preparation moves:</p>
<ul>
<li><strong>Choose the concession first:</strong> the single operator or anchor tenant whose base compound hosts the depot — the security, substation and ESG mandate all come with the anchor.</li>
<li><strong>Build the buffered depot:</strong> charger + battery storage + generator tie-in, the configuration this article prices; in Delta conditions the buffer is not optional infrastructure.</li>
<li><strong>Instrument the convoy duty:</strong> schedule windows, gate queues and fuel stops of the incumbent diesel runs — the baseline that will also show the security surface electric charging removes.</li>
<li><strong>Enter on the EV tariff line:</strong> Nigeria's new fiscal framework rewards correct classification; our documentation set pre-clears it with the clearing agent before sailing.</li>
<li><strong>Plan the fuel-independence annex:</strong> the number of public fuel stops per truck-week that the electric fleet eliminates is both a cost line and a security metric — present it to the HSE department, not just the finance office.</li>
<li><strong>Train the crew for the humidity file:</strong> our tropical commissioning covers the sealed-HV washdown and connector inspections Delta duty demands.</li>
</ul>
<p>The Niger Delta is the toughest market in our coverage and one of the most rewarding — the diesel cost, the fuel-quality risk and the anchor tenants' ESG pressure all point the same direction. The first base-compound fleet will convert its contractor's tender position permanently.</p>
"""

S["mandalay-myanmar-dry-zone-electric-truck.html"] = """
<h2>Running a Mandalay Pilot Under Real Constraints</h2>
<p>Upper-Myanmar operators should size a first fleet around the market's real constraints rather than pretending them away:</p>
<ul>
<li><strong>Anchor at one mill or trading house:</strong> the depot, the substation and the security story all live inside a single compound — the structure that works in constrained markets everywhere.</li>
<li><strong>Pilot four trucks on the agri loops:</strong> the fixed farm-to-mill runs where the return-to-base rhythm makes charging trivial and the savings show fastest.</li>
<li><strong>Ride the hydro seasons:</strong> plan the fleet's charging economics on the annual tariff and outage pattern, with the dry-season months providing the stress-test data.</li>
<li><strong>Use the Muse channel deliberately:</strong> border-trade entry suits right-hand-configured Chinese units and shortens logistics — our export package ships with the documentation set either channel requires.</li>
<li><strong>Price the fuel-risk dividend explicitly:</strong> Mandalay's diesel price jumps 15-20% inside weeks at times; the electric fleet's fixed energy line is worth a premium the spreadsheet does not capture until the next jump arrives.</li>
<li><strong>Keep the expansion decision at one dry season's data:</strong> the discipline that turns a constrained market into a rational one.</li>
</ul>
<p>Mandalay's commodity traders count costs with more precision than most fleet owners on earth — which is exactly why the dry zone converts: the arithmetic is not close. The first mill that electrifies its haul loop sets the price floor the next harvest is traded against.</p>
"""

S["tanzania-cashew-corridor-electric-truck.html"] = """
<h2>What Southern Corridor Operators Should Prepare</h2>
<p>Fleets and plant operators on the Mtwara-Lindi cashew chain can prepare a first fleet with five moves:</p>
<ul>
<li><strong>Model the blended season:</strong> harvest tonnage for the rush, kernel distribution and general cargo for the off-season — the fleet sized on the year, not the October peak.</li>
<li><strong>Anchor at the processing plant:</strong> the substation, the security and the management culture make the plant the natural first depot; the auction-point charger extends the corridor's reach in phase two.</li>
<li><strong>Verify duty and VAT treatment at entry:</strong> our Tanzanian quotations carry the classification and concession-structure options the importer's broker should review before the vessels are booked.</li>
<li><strong>Specify the moisture discipline:</strong> in-shell cashew and Delta humidity argue for the sealed box body and its humidity-stable cargo environment — a quality line the kernel buyers' audits already price.</li>
<li><strong>Schedule the dust service:</strong> harvest-season collection roads demand the shortened filter intervals from day one; the commissioning training covers the why.</li>
</ul>
<p>The southern corridor's economics — TANESCO off-peak power against peak-season diesel queues — are as clean as agri-logistics gets, and the processing-plant anchor removes every infrastructure objection. The sector's industrialisation push is building the plants; the smart money attaches the electric fleet to the same investment.</p>
"""

S["chile-lithium-triangle-electric-heavy-haul.html"] = """
<h2>The Antofagasta Deployment Sequence</h2>
<p>Contractors serving the Atacama brine operations can structure a first electric corridor fleet in five steps:</p>
<ul>
<li><strong>Map the reagent and consumable flows:</strong> the plant-to-salar distances, gate queues and return legs — the duty data that sizes the TE8P order and the midday top-up windows.</li>
<li><strong>Sign the solar PPA before the truck contract:</strong> the sub-$0.05/kWh energy line is the economic engine of the whole case; the array and charger bank belong in the same negotiation.</li>
<li><strong>Specify the dust and altitude package:</strong> pressurised pack filtration, UV-stable components and the shortened coolant schedule — the engineering that keeps 4,000 m duty boring.</li>
<li><strong>Attach the emissions annex to the next tender:</strong> the brine operators' Scope 3 audits increasingly score logistics emissions; the fleet's telematics ledger is bid material, as this blog's tender-strategy pieces detail.</li>
<li><strong>Pilot on the highest-frequency supply loop:</strong> three or four tractors on the resupply runs that pass the same gates daily, where the savings and the data accumulate fastest.</li>
</ul>
<p>The Atacama holds the world's best sun, its driest corridors and its most ESG-scrutinised minerals — a rare alignment of physics, policy and procurement that makes the electric heavy-haul case nearly unarguable. The first supply-base fleet that plugs into its own solar will hold the corridor's cost and compliance position for the decade.</p>
"""

S["vietnam-seafood-cold-chain-electric-truck.html"] = """
<h2>Running a Delta Cold-Chain Pilot</h2>
<p>Seafood processors evaluating the KT5L reefer can produce board-ready data with a structured pilot:</p>
<ul>
<li><strong>Instrument the diesel reefer baseline:</strong> two engines' fuel burn, compressor failures and temperature-excursion events on the candidate plant-to-port legs — the baseline the electric reefer must beat on all three lines.</li>
<li><strong>Charge at the plant:</strong> the processing plant's grid connection and night tariff host the charger bank; the seafood sector's EVN rates are the cheapest energy in the chain.</li>
<li><strong>Log box temperature as the headline metric:</strong> the electric compressor's hold-during-queue performance is the audit-ready number the export customers care about — present it alongside the fuel saving.</li>
<li><strong>Time the pilot to the harvest calendar:</strong> peak-season double shifts provide the stress data; the off-season provides the calm confirmation.</li>
<li><strong>Review bridge and route limits:</strong> delta secondary routes and monsoon flooding argue for the KT5L's lighter class and the wading-rated tropical package — the specification notes in this article.</li>
</ul>
<p>Vietnam's seafood export markets audit the full chain now — temperature, traceability and increasingly transport emissions — and the processing plants are the natural anchor for all three answers at once. The electric reefer fleet is the sector's next competitive upgrade; the plants that run the pilot first will sell the documentation advantage with every container.</p>
"""

S["johor-data-center-construction-electric-truck.html"] = """
<h2>The Johor Contractor's Preparation Kit</h2>
<p>Concrete and earthworks contractors bidding the DC corridor can prepare an electric-fleet option with five moves:</p>
<ul>
<li><strong>Map the pour schedules:</strong> the 24-hour continuous-pour windows where zero-idle mixers save the most and night noise rules bind — the data that prices the electric option's premium.</li>
<li><strong>Anchor charging at the batching plant:</strong> the plant substation hosts the charger bank; the mixer's four-hour return rhythm makes the plant the perfect depot without new land.</li>
<li><strong>Attach the telematics annex to the next bid:</strong> hyperscalers answer to Scope 3 accounting with unusual rigour — a documented electric concrete option is a scoring line diesel-only competitors cannot reach.</li>
<li><strong>Verify MIDA and NETR positioning:</strong> our Malaysian documentation package pre-clears the import treatment, and the incentive channel for charging infrastructure is worth the application.</li>
<li><strong>Pilot on one campus's foundations:</strong> four TZ8Js and two KTA1s on a single project — the smallest unit that produces fleet-scale data inside one pour cycle.</li>
</ul>
<p>Johor's data center decade will pour more concrete than most countries' national programmes, and every campus is being built for clients who measure emissions to two decimal places. The contractor who arrives at the next tender with a proven electric fleet holds the differentiator the whole corridor is about to be scored on.</p>
"""

S["solar-farm-construction-electric-truck-fleet.html"] = """
<h2>The EPC's Electric Construction Checklist</h2>
<p>EPCs bidding utility-scale PV can convert the arguments above into tender-ready structure with six moves:</p>
<ul>
<li><strong>Price the construction-substation charger early:</strong> the temporary depot is a relocatable project asset — it appears in the bid as reusable capex, not stranded cost.</li>
<li><strong>Model the site loops:</strong> earthworks volumes, haul distances and materials logistics from comparable past sites — the numbers that size the KTA1/TE8M mix per project phase.</li>
<li><strong>Write the zero-exhaust option into the bid:</strong> developers' ESG frameworks increasingly reward it explicitly; the option line costs little to carry and scores when the framework asks.</li>
<li><strong>Specify for the build environment:</strong> the desert or steppe package this article describes, with the dust schedule trained at handover — the spec that keeps the fleet boring.</li>
<li><strong>Carry the fleet between sites deliberately:</strong> the trucks' project-to-project rotation is the fleet's second life — the relocatable charger and the duty data travel with it.</li>
<li><strong>Report the construction-phase emissions honestly:</strong> the kWh ledger from the first energised blocks is the marketing asset that wins the next mega-site.</li>
</ul>
<p>The renewable build-out is the decade's largest construction programme, and its financiers are the world's most emissions-literate clients. The EPCs that build the plants with the plant's own electricity will own the sector's premium narrative — and its cheapest fuel line.</p>
"""

S["steel-mill-scrap-inbound-electric-truck.html"] = """
<h2>The Mill Inbound Pilot, Structured</h2>
<p>Steel-mill operators can convert the economics in this article into a first fleet with five moves:</p>
<ul>
<li><strong>Pick the highest-frequency scrap loop:</strong> the yard-to-stockyard run with the most daily cycles — where the idle and fuel data will show the electric advantage inside one melt campaign.</li>
<li><strong>Charge from the melt-shop tariff:</strong> the mill's own night window and heavy-load-factor rate host the charger bank — the cheapest fleet energy in heavy industry.</li>
<li><strong>Run the comparison in tonnes:</strong> cost per tonne delivered, not per truck — the metric the melt-shop manager answers to, and the one the electric fleet wins fastest.</li>
<li><strong>Write the green-steel annex:</strong> the inbound-fleet emissions line belongs in the mill's Scope 3 documentation for CBAM-facing and low-carbon export sales — our ESG reporting piece covers the data mechanics.</li>
<li><strong>Train the yard crew first:</strong> scrap yards are hostile environments; the tropical-and-debris commissioning package and the two-person HV rules apply from day one.</li>
</ul>
<p>An EAF mill melting scrap with cheap night electricity and trucking it in with diesel is leaving the last visible emissions line on the table — and the customers paying green-steel premiums are the ones who will notice first. The mills that electrify the inbound loop will sell the cleanest steel in their markets, gate to gate.</p>
"""

S["pantograph-opportunity-charging-electric-truck-port.html"] = """
<h2>Running the Queue Study That Decides Everything</h2>
<p>The pantograph decision begins with a two-week data exercise on your port's own timestamps, and the markets where we have run it — from the Gulf to North Africa's <a href="../markets/egypt.html">Egyptian port corridors</a> — follow the same template:</p>
<ul>
<li><strong>Extract gate, weighbridge and crane dwell times:</strong> the port's TOS or gatehouse timestamps already hold the dataset; no new hardware is needed to find the chargeable queues.</li>
<li><strong>Rank the dwell points:</strong> average minutes × truck-encounters per day per location — the product that identifies which two or three queues justify gantries.</li>
<li><strong>Model pack size against the winners:</strong> with the top-up sessions quantified, the fleet's pack requirement usually drops a battery class — the capex trade this article's table prices.</li>
<li><strong>Price the co-funding conversation:</strong> terminals benefit from the emissions accounting as much as hauliers — our MENA deployments have drawn 30-50% infrastructure co-funding on exactly that logic.</li>
<li><strong>Standardise the depot first, gantry second:</strong> prove the energy math on plug-based fast bays, then add the gantry where the timestamps justify it — the sequencing that has never wasted a dollar in comparable deployments.</li>
</ul>
<p>Ports concentrate trucks, queues and power in one fence — the three ingredients opportunity charging needs. The fleets that read their own timestamp data before their competitors do will convert the dead minutes the others keep burning as diesel idle.</p>
"""

S["electric-truck-battery-swap-station-siting.html"] = """
<h2>The Five-Gate Review, Compressed</h2>
<p>Buyers who want the swap question answered for their specific duty cycle can compress the five siting gates into a structured desk review — the same process we run for quarry clients from Indonesia's nickel districts to the Central Asian mines described on our <a href="../markets/kazakhstan.html">Kazakhstan market page</a>:</p>
<ul>
<li><strong>Swap count first:</strong> trucks × swaps per day, from the duty logs — below roughly 30 daily swaps, the station economics rarely clear and the honest answer is depot charging.</li>
<li><strong>Utility letter second:</strong> written capacity confirmation on the candidate parcels — the queue or the headroom kills more swap projects than any other single gate.</li>
<li><strong>Land on the route:</strong> the natural mid-shift waypoint the trucks already pass — detour kilometres are the silent tax that erodes swap's utilisation gain.</li>
<li><strong>Custody structure early:</strong> pack ownership, insurance and SOH certification between swaps — the commercial file that makes the racks bankable, covered in this blog's BaaS and second-life pieces.</li>
<li><strong>Both models side by side:</strong> our engineering questionnaire returns the swap and depot-charging models against the same duty data — the decision made by arithmetic, not by ideology.</li>
</ul>
<p>Swap is the right answer often enough to matter — roughly a third of the high-utilisation fleets we model — and the wrong answer often enough that the modelling discipline is the whole game. The station that gets built on the five gates is the station that stays busy for a decade.</p>
"""

S["ev-truck-battery-theft-depot-security.html"] = """
<h2>The Security File Buyers Should Assemble</h2>
<p>The security question resolves into a documentation exercise, and buyers in markets from Lagos to the Sahel — where our <a href="../markets/nigeria.html">Nigeria market coverage</a> deals with it most directly — should assemble five pieces:</p>
<ul>
<li><strong>The telematics evidence:</strong> geofencing, movement alerts and remote lockout — standard on every fleet we ship, and the layer insurers price first.</li>
<li><strong>The depot layout drawing:</strong> camera lines, gate control and parking geometry against the guardhouse sightlines — the same discipline any valuable yard already runs.</li>
<li><strong>The procedural roster:</strong> HV-authorised technicians, two-person pack rules and custody logging — the insider-threat layer the spec article above prices at management cost.</li>
<li><strong>The serialisation record:</strong> pack and module serials registered to the fleet cloud — the paper trail that makes a stolen pack worthless and a warranty claim painless.</li>
<li><strong>The insurance presentation:</strong> those four files, bound, at underwriting time — the difference between a quoted premium and a polite refusal in emerging-market EV cover.</li>
</ul>
<p>The honest summary for fleet boards: battery theft is a real risk class with a mature toolkit, cheaper to manage than the diesel fraud it replaces. Security belongs on the specification sheet, not on the veto list.</p>
"""

S["how-to-read-electric-truck-spec-sheet.html"] = """
<h2>Bringing the Twelve Numbers to Your Next Purchase</h2>
<p>The buyer who arrives at a comparison with the twelve numbers structured — whether against our own line-up like the <a href="../products/models/kt5j-electric-cargo-truck.html">KT5J electric cargo truck</a> or any competitor's sheet — controls the meeting. The compression we recommend:</p>
<ul>
<li><strong>Demand the mission-profiled numbers:</strong> consumption at your load and gradient, charge curve to 80%, continuous power at your worst ramp — the three requests that separate engineered sheets from marketing ones.</li>
<li><strong>Run the honest-range division:</strong> usable capacity ÷ loaded consumption, per route — the single calculation that exposes most range claims.</li>
<li><strong>Read the warranty against the finance term:</strong> years, cycles, SOH floor and the claim procedure — the three lines that determine whether the pack's value survives the loan.</li>
<li><strong>Name the cell supplier:</strong> a CATL-branded LFP pack with serialised data is a bankable asset; an anonymous "lithium-ion" line is an unpriced risk — the second-life economics in our battery piece depend on exactly this documentation.</li>
<li><strong>Check market-specific duty context:</strong> the same truck runs different numbers in Jakarta's humidity than in Almaty's winter — our country pages, such as the <a href="../markets/indonesia.html">Indonesia electric truck market</a>, carry the local adjustments that make the twelve numbers locally honest.</li>
</ul>
<p>Spec literacy is a two-hour investment that pays on every truck a fleet ever buys — and the vendors who resist the twelve questions are answering one of them involuntarily.</p>
"""

S["green-finance-development-banks-electric-truck-africa.html"] = """
<h2>The Buyer's Green-Finance Opening Moves</h2>
<p>Fleet operators who want the rate advantage can start this week with four moves:</p>
<ul>
<li><strong>Ask your bank the one question:</strong> "Do you hold a climate or green credit line, and does it cover commercial electric vehicles?" — the query that starts most of the facilities we have seen drawn, from Lagos to Nairobi to the corridors covered on our <a href="../markets/ghana.html">Ghana market page</a>.</li>
<li><strong>Build the impact page:</strong> litres displaced, tonnes avoided, kWh metered — the one-page math the bank's climate mandate requires, generated from the duty model in our fleet pieces.</li>
<li><strong>Pair the application with a standard import:</strong> our conformity and contract documentation makes the truck purchase the ordinary part of an extraordinary-rate loan.</li>
<li><strong>Volunteer the monitoring plan:</strong> the telematics reporting template offered before it is asked for — the difference between an application and a relationship.</li>
</ul>
<p>The green lines are allocated, the covenants are answerable, and the fleets that apply first get the rate for the decade's entire fleet build. The capital is sitting in the bank you already use; the only unusual step is the question.</p>
"""

S["kenya-electric-mobility-policy-ev-trucks.html"] = """
<h2>The Kenyan Importer's Action List</h2>
<p>Converting the policy environment into a live fleet plan takes a defined sequence:</p>
<ul>
<li><strong>Confirm the current fiscal position at entry time:</strong> our Kenyan quotations verify the live duty and levy treatment with the clearing agent — budget cycles adjust the schedules, and the importer's file should carry the current position, not last year's.</li>
<li><strong>Register PVoC early:</strong> the KEBS inspection is a pre-shipment gate; our package books it with the pro-forma, so certification never delays a vessel.</li>
<li><strong>Batch the consignments:</strong> five to ten units per shipment amortises the conformity layer and lands the depot's charging complement with the trucks.</li>
<li><strong>Engage a customs agent on the EV lines:</strong> classification familiarity is worth days at the entry point — the difference this article quantifies.</li>
<li><strong>Anchor the depot on the commercial tariff:</strong> the standard Kenyan depot design — off-peak scheduled dual-gun chargers — connects within the distribution company's normal commercial process, as our Eldoret and Nairobi pieces detail.</li>
<li><strong>Bank the ESG dividend formally:</strong> the kWh ledger feeds the corporate sustainability reporting that increasingly decides Kenyan B2B tenders — the compliance artefact that costs nothing to keep and wins contracts to spend.</li>
</ul>
<p>Kenya wrote its EV policy before its EV wave — the unusual sequencing that makes the current import window structurally favourable. The importers who draw it down this cycle will hold both the exemption and the operating-cost position when the market's second act arrives.</p>
"""

S["nigeria-electric-vehicle-policy-ev-truck-importers.html"] = """
<h2>The Nigerian Importer's Execution List</h2>
<p>Turning the policy into a landed fleet takes a deliberate sequence:</p>
<ul>
<li><strong>Enter on the EV tariff line, verified live:</strong> our documentation package pre-clears the classification with the clearing agent — the fiscal core of the whole case, confirmed against the current customs schedule at entry time.</li>
<li><strong>Run SONCAP in China before sailing:</strong> the pre-shipment inspection our package arranges, with the BEV conformity evidence and UN 38.3 battery file in the certificate set.</li>
<li><strong>Specify behind-the-fence charging:</strong> the buffered depot design (charger + storage + generator tie-in) priced in this article — the configuration every serious Nigerian deployment uses, from the Lagos distribution fleets to the Delta oil-services pilots.</li>
<li><strong>Choose first missions by fuel exposure:</strong> distribution and industrial loops where fuel is 40% of operating cost — the duty cycles our <a href="../products/models/kt5m-electric-cargo-truck.html">KT5M electric box truck</a> Nigeria pieces model at 20-30 month payback.</li>
<li><strong>Pair trucks with technician training:</strong> the HV crew trained at commissioning is the policy's quiet requirement — and the operator's quiet advantage, as the maintenance economics in our scaling playbook show.</li>
<li><strong>Track the policy's next phase:</strong> the local-assembly incentives will mature; importers building fleet experience now will be the assemblers' anchor customers then.</li>
</ul>
<p>Nigeria's freight economy runs on some of the world's most expensive diesel and some of its cheapest charging opportunities — the policy simply gave importers the paperwork tool to close the gap. The window is open, the classification is written, and the fleets that enter on the EV lines first will run the cheapest cost base in the market.</p>
"""

S["ev-truck-driver-recruitment-retention.html"] = """
<h2>The HR Starter Kit for a Converting Fleet</h2>
<p>Operations managers building the human layer alongside the hardware — whether for a KT5M-class box fleet in Bangkok or a tipper fleet on the corridors covered on our <a href="../markets/thailand.html">Thailand market page</a> — can start with five artefacts:</p>
<ul>
<li><strong>The honest job ad:</strong> air-conditioned, automatic, new truck — the three words that measurably change applicant volume and quality.</li>
<li><strong>The five-day onboarding:</strong> regen technique, charge discipline, HV checks, telematics — the curriculum table in this article, delivered at commissioning.</li>
<li><strong>The route-normalised league table:</strong> consumption scored against engineered baselines, not against other drivers' luck — the fair version that avoids the mission-gaming failure mode.</li>
<li><strong>The buddy pairing:</strong> new electric drivers paired with converted sceptics, first two weeks on the home routes — the adoption mechanics that cost nothing and work everywhere.</li>
<li><strong>The technician introduction:</strong> drivers meeting the HV crew in week one — the trust connection that turns range questions into ten-minute answers.</li>
</ul>
<p>The hardware does the heavy lifting on cost; the people decide how much of the savings the P&amp;L banks. Fleets that budget a week for the human layer — the cheapest line in any electrification proposal — are the fleets whose spreadsheets come true.</p>
"""

S["scaling-electric-truck-fleet-10-to-100.html"] = """
<h2>The Scale-Up Self-Assessment</h2>
<p>Operators between stages can audit their readiness with six questions — the same review we run with fleets scaling <a href="../products/models/kta1-electric-dump-truck.html">KTA1-class quarry operations</a> and distribution fleets from the Gulf to the corridors covered on our <a href="../markets/indonesia.html">Indonesia market page</a>:</p>
<ul>
<li><strong>Are the baselines written down?</strong> Route-level kWh, charge durations, failure modes — if it lives in one manager's head, it is not yet a system.</li>
<li><strong>Is the charger plan energy-based or truck-count-based?</strong> Daily fleet kWh × 1.15 over the off-peak window, not a socket ratio — the error that breaks fleets at truck forty.</li>
<li><strong>Does HV knowledge live in more than two people?</strong> The two-tier technician structure and train-the-trainer layer are the fix before the heroes become bottlenecks.</li>
<li><strong>Is the spares pool min-max managed?</strong> Consumption-driven reorders, bonded fast movers — the difference between maintenance and scavenging.</li>
<li><strong>Does dispatch see SoC before committing trucks?</strong> Range-aware assignment is the software habit that prevents the stranded-truck day.</li>
<li><strong>Who owns the energy bill?</strong> At a hundred trucks, the tariff negotiation and the second-life battery stream are a named person's job, not a finance footnote.</li>
</ul>
<p>Scale is where electric fleets earn their keep: the depot is paid, the crews are trained, and every new truck improves the machine. The self-assessment above is how operators make sure the machine is actually built before they feed it.</p>
"""

S["tz3z-vs-tz5e-city-dump-truck-choice.html"] = """
<h2>Making the Call on Your Own Routes</h2>
<p>The configuration decision compresses into five questions any construction buyer can answer from their own site data:</p>
<ul>
<li><strong>What does the bridge formula allow on your corridors?</strong> The axle-loading answer is the master constraint — it decides whether the TZ3Z's second steer axle buys payload or buys nothing.</li>
<li><strong>How many tonnes per contract-day?</strong> Fixed-tonnage programmes reward the TZ3Z's throughput; variable small-load work rewards the TZ5E's lower unit cost.</li>
<li><strong>How wide are the site gates?</strong> The wheelbase difference is a daily reality on redevelopment sites — the single most common regret we hear from mismatched purchases.</li>
<li><strong>What does the tyre budget say?</strong> Eight wheels against six, compounded across the fleet's life — the line item that quietly favours the 6x4 in pure arithmetic.</li>
<li><strong>Where does the duty data point?</strong> Our engineering questionnaire resolves a genuinely open call with one week of your route data — the same instrument the spec-sheet piece in this blog describes.</li>
</ul>
<p>Most operators end up with the mix: TZ5Es carrying the majority of the daily trips, TZ3Zs holding the heavy-corridor contracts, both fleets sharing the same depot, spares pool and driver training cohort. That mixed answer, backed by the arithmetic above, is usually the right one — and it is a lot cheaper to reach before the first order than after it.</p>
"""

S["saudi-aggregates-giga-project-electric-dump-truck.html"] = """
<h2>The Contractor's Giga-Project Entry Kit</h2>
<p>Aggregates operators bidding giga-project supply can prepare the electric option with five moves:</p>
<ul>
<li><strong>Assemble the corridor dataset:</strong> crusher-to-plant distances, cycle counts and fuel ledgers on the incumbent diesel runs — the baseline the TZ3V/KTA1 comparison must beat, quarry by quarry.</li>
<li><strong>Price the solar pairing in the depot proposal:</strong> the PPA-charged fleet is the 15-month payback version of this article's table — the number that wins the finance committee.</li>
<li><strong>Write the emissions annex into the bid:</strong> the developers' scorecards reward documented reductions with award weight; the fleet's kWh ledger is the evidence line.</li>
<li><strong>Confirm SASO and Saber early:</strong> our conformity documentation and heat-spec file enter the platform before shipment — the import mechanics that keep a fleet order on schedule in the Kingdom.</li>
<li><strong>Pilot on the highest-tonnage run:</strong> four TZ3Vs, quarry-charged, one summer quarter of instrumented data — the smallest commitment that produces fleet-scale proof.</li>
</ul>
<p>The Kingdom's construction supercycle has a decade to run, and its clients are the most emissions-scored developers on earth. The aggregates contractor who electrifies the corridor first holds both the cost line and the compliance line — and the window in which rivals can respond is measured in quarters, not years.</p>
"""

S["kt5m-beverage-plant-distribution-electric.html"] = """
<h2>The Bottler's Electrification Starter Kit</h2>
<p>Beverage operators preparing a first electric fleet can structure the plant-gate case with five moves:</p>
<ul>
<li><strong>Instrument the trade routes:</strong> drops, idle minutes and fuel per truck on the two densest loops — the baseline the KT5M pilot will be measured against, quarter by quarter.</li>
<li><strong>Confirm the plant's tariff position:</strong> the existing industrial rate and its off-peak window host the charger bank — the cheapest fleet energy in the operation, already contracted.</li>
<li><strong>Pilot five trucks on one plant:</strong> the trade routes first, where idle share is highest; the wholesale runs follow once the energy data lands.</li>
<li><strong>Review the licensor audit calendar:</strong> the international parents' environment audits increasingly include distribution — arriving at the next audit with an electric fleet and its kWh ledger is the franchise-strengthening move.</li>
<li><strong>Price the reefer variant where relevant:</strong> juice and dairy-inclusive distributors should compare the factory electric reefer body against the diesel donk — the compound saving this article prices.</li>
</ul>
<p>The beverage sector's economics — dense loads, short radii, plant-gate depots and the industry's thinnest margins — make it the textbook first mover in every market we track. The only open question in each country is which bottler signs the first plant charging agreement; the first signature usually ends the debate for the rest.</p>
"""

S["kt1d-waste-transfer-station-electric.html"] = """
<h2>The Station Operator's Conversion Sequence</h2>
<p>Concessionaires and municipal operators can convert a transfer station fleet in five moves:</p>
<ul>
<li><strong>Start with the haul-out leg:</strong> the simplest mission in the station's portfolio — three KT1Ds on the landfill runs, station-charged, one quarter of per-tonne data.</li>
<li><strong>Convert the tipping-floor compaction second:</strong> the station-side KT1Ds whose electric PTO replaces eight hours of diesel high-idle — the mission where the energy saving is starkest.</li>
<li><strong>Build the per-tonne TCO table:</strong> the bid-winning metric from this article, built on the station's own tonnage ledger and the concession's contract price.</li>
<li><strong>Document the quiet-operation hours:</strong> the night-shift headroom the electric fleet buys — a permitting and community-relations asset worth real operating windows in constrained urban sites.</li>
<li><strong>Attach the emissions annex to the next tender:</strong> municipal waste tenders now score environmental performance, as our KT1D/KT3E tender-strategy piece details — the station fleet is the easiest scoring line to hold.</li>
</ul>
<p>The transfer station is the waste chain's fixed point — grid-connected, fenced, running around the clock — and the natural place for a municipality's electrification to begin. Once the station fleet is electric, every collection round that feeds it has a place to charge; the second phase builds itself.</p>
"""

S["dominican-republic-tourism-construction-electric-truck.html"] = """
<h2>The DR Contractor's Bid Preparation</h2>
<p>Contractors preparing to bid resort work with an electric fleet can assemble the option with five moves:</p>
<ul>
<li><strong>Build the corridor dataset:</strong> quarry-to-plant and plant-to-site distances with the incumbent diesel fuel ledgers — the baseline the TZ5E/KT5M case must beat on the Punta Cana loops.</li>
<li><strong>Write the sustainability annex into every bid:</strong> the hospitality groups' ESG scoring is the DR's unusual bid factor — the telematics kWh ledger attached to the proposal is the line diesel competitors cannot reach.</li>
<li><strong>Confirm the import classification early:</strong> our DR documentation package — Spanish-language files, conformity certificates, Caucedo logistics — keeps the entry on the right tariff lines and on schedule.</li>
<li><strong>Pilot on one project, not the portfolio:</strong> three tippers and one charger at the batching plant, one resort build's worth of data, then hold the fleet as the company's standard bid package.</li>
<li><strong>Specify for the coast:</strong> the salt-humid, hurricane-season package this article describes — the specification that turns Caribbean weather from a risk line into a diesel-fleet comparison.</li>
</ul>
<p>The Dominican tourism build-out is booked for the decade, its projects are gated, its clients score emissions, and its fuel is imported at Caribbean prices. The contractor who arrives at the next Cap Cana tender with a proven electric fleet will hold a bid position the market cannot quickly copy — on the cost line as well as the scorecard.</p>
"""

# GEO FAQ blocks
S["how-long-does-electric-truck-battery-really-last.html"] = """
<h2>Frequently Asked Questions</h2>
<h3>How many years does an electric truck battery last?</h3>
<p>A CATL LFP pack typically lasts 8-12 years of heavy-duty service. The standard warranty covers 8 years or 4,500 full cycles to 70-80% state of health, and well-managed fleets report only 3-5% capacity loss per year on daily duty cycles — meaning the pack usually outlives the first owner.</p>
<h3>How many kilometres can an EV truck battery cover before replacement?</h3>
<p>Roughly 900,000 to 1.5 million km. At one full cycle per 200-350 km of range, 4,500 warranted cycles compound into seven figures of service life — which is why most fleets replace or repurpose packs after 8-10 years for capacity planning reasons, not because the battery failed.</p>
<h3>Does fast charging shorten an electric truck battery's life?</h3>
<p>Only modestly. Charging at 240-360 kW has a small effect on LFP chemistry when liquid cooling is healthy: CATL packs taper charge rates above 80% state of charge and hold cell temperatures in the optimal window, so fleets mixing fast and overnight slow charging see degradation within about 1% per year of depot-only fleets.</p>
<h3>What is the state of health threshold for a warranty claim?</h3>
<p>70-80% of original capacity, depending on pack series, within 8 years or 4,500 cycles. A diagnostic certificate showing the pack below that line — with a complete service log — triggers module repair or replacement at no cost under the warranty terms described in this article.</p>
<h3>Can an EV truck battery be replaced or upgraded instead of scrapped?</h3>
<p>Yes, at three levels: individual CATL modules swap at a fraction of pack cost, a whole 262-600 kWh pack can be exchanged, and a retired pack at 75-80% SOH enters second-life stationary storage worth USD 25,000-45,000 — the residual-value dividend this blog's second-life article prices in detail.</p>
"""

S["how-much-does-electric-dump-truck-cost-china-fob.html"] = """
<h2>Frequently Asked Questions</h2>
<h3>How much does an electric dump truck cost from China?</h3>
<p>Between $95,000 and $180,000 FOB in 2026: the 6x4 TZ5E with a 400 kWh CATL pack runs $95,000-$120,000, the KTA1 quarry spec $120,000-$150,000, and the 8x4 TZ3V with the 600 kWh battery $150,000-$180,000, before project discounts on volume orders.</p>
<h3>Why is an electric dump truck more expensive than a diesel one?</h3>
<p>The battery: a 400-600 kWh pack adds $35,000-$60,000 to the build. The premium repays in 2-4 years through $18,000-$35,000 of annual fuel and maintenance savings on typical quarry and construction duty — after which the electric truck is cheaper every year it runs.</p>
<h3>What extra costs come on top of the FOB price?</h3>
<p>Ocean freight of $6,000-$12,000 (RoRo or flat-rack), import duty of 5-25% depending on destination — or zero in EV-exempt markets like Kenya and Ghana — VAT and clearing of $3,000-$6,000, and a first 240 kW depot charger with installation at $25,000-$45,000, shared across the fleet rather than per truck.</p>
<h3>Is battery swap cheaper than buying the battery with the truck?</h3>
<p>For high-utilisation duty, often yes: buying the truck without its pack cuts capex 30-40% against a per-swap fee of roughly $0.35-$0.50 per kWh. Quarries running 5-6 minute swaps two to three times daily usually win on swap finance; single-shift construction fleets almost always do better owning the battery.</p>
<h3>How many years does an electric dump truck take to pay back?</h3>
<p>Three to four years on the FOB premium at 250 km/day against a diesel 8x4 — $25,000-$30,000 of annual fuel and maintenance savings on a $75,000-$100,000 premium — compressing to 2-3 years where electricity is cheap relative to diesel, such as Ethiopia, Kenya, Chile's solar-fed sites and anywhere a solar PPA is available.</p>
"""

# shorter add-ons for files already passing other checks but low word count
S["ev-truck-battery-second-life-mini-grid-storage.html"] = """
<h2>Buying the Optionality: Contract Lines That Preserve Second-Life Value</h2>
<p>Whether a fleet's packs retire as assets or as scrap is decided in the purchase contract, years before the first pack comes out of a truck. The lines that matter:</p>
<ul>
<li><strong>Serialisation and data custody:</strong> pack and module serials registered to the buyer, with SOH and cycle history exportable on demand — the documentation that makes a retired pack bankable in the second-life market.</li>
<li><strong>Repurposing rights:</strong> the explicit right to convert, sell or redeploy the pack into stationary duty after its vehicle life — a clause BaaS and lease structures must state unambiguously.</li>
<li><strong>Grading protocol access:</strong> the module-level diagnostic interface our engineering package hands over, so the client's own crew can re-baseline a retired pack without the manufacturer's gatekeeping.</li>
<li><strong>Certification inheritance:</strong> the UN 38.3 heritage, chemistry declaration and first-life history travelling with the pack — exactly the file stationary-storage insurers and mini-grid developers ask to see.</li>
<li><strong>Custody in service contracts:</strong> any third-party maintenance agreement must preserve the buyer's title and data rights over packs removed for any reason — the insider-risk and insurance pieces in this blog cover the security side of the same custody question.</li>
</ul>
<p>Fleets that sign these lines bank USD 25,000-45,000 per retired pack; fleets that do not discover at year eight that their battery value needed paperwork they never wrote. The optionality is cheap at signing and priceless at retirement.</p>
"""

S["6x4-vs-8x4-electric-dump-truck-configuration.html"] = """
<h2>Three Regional Cases That Show the Fork</h2>
<p>The configuration answer changes with geography, and three of our active markets illustrate the fork better than any theory:</p>
<ul>
<li><strong>Chile's mine-feeding corridors:</strong> enforced axle loading, full loads, straight hauls — the 8x4 TZ3V class dominates, its payload-per-trip converting directly into fewer dispatches per campaign.</li>
<li><strong>West African urban construction:</strong> moderate loads, road-quality GVW reality and tight sites — the 6x4 TZ5E class carries most trips, which is why our Lagos and Accra fleet models skew 6x4 by roughly two to one.</li>
<li><strong>Southeast Asian secondary roads:</strong> bridge-rated routes that punish over-axle loading — the 6x4's legal-weight productivity beats an 8x4 that cannot load to its design weight, the pattern our Vietnam and Indonesia market pages document.</li>
</ul>
<p>The buyer's move is to price both configurations against their own route data before the first order: one duty-cycle questionnaire, both models, the decision made by the numbers your corridors actually allow. The showroom intuition that works for diesel does not survive the electric payload arithmetic — the pack is fixed tare, and every tonne of battery the mission does not need is payload the fleet never earns.</p>
"""

S["tz3v-andes-altitude-copper-mine-electric-dump.html"] = """
<h2>The Andean Fleet Pilot, Structured for Altitude</h2>
<p>Mining contractors evaluating the TZ3V for altiplano duty can de-risk the decision with a pilot designed around the mountain's real conditions:</p>
<ul>
<li><strong>Run the pilot through the cold season:</strong> dawn shifts at minus five degrees and afternoon dust are the stress case — a fleet that passes the Andean winter passes everything below 4,000 m.</li>
<li><strong>Instrument the descents:</strong> the regen recovery figure on your actual haul profile decides the consumption model's honesty; our commissioning captures it wheel by wheel.</li>
<li><strong>Charge at the camp, not the pit:</strong> the camp substation and its night window host the charger bank, with the midday top-up at the ROM pad where trucks queue anyway.</li>
<li><strong>Pair the pilot with the tender calendar:</strong> Chilean and Peruvian mine-service tenders increasingly score zero-emission options — a running electric fleet with campaign data converts directly into bid points, as our tender-strategy pieces detail.</li>
<li><strong>Train the crew on the dust schedule:</strong> the altiplano's fine dust is the maintenance story; the shortened coolant and filter intervals from handover are what keep availability boring.</li>
</ul>
<p>The altitude argument ends when the first loaded TZ3V pulls past a derated diesel on the same ramp — after that, the conversation is logistics, not physics. The mines that run the pilot first will hold the corridor's cost and compliance position while their competitors argue with a torque curve.</p>
"""

S["pantograph-opportunity-charging-electric-truck-port.html"] += ""
S["ev-truck-battery-second-life-mini-grid-storage.html"] = S["ev-truck-battery-second-life-mini-grid-storage.html"]  # keep
S["chile-lithium-triangle-electric-heavy-haul.html"] = S["chile-lithium-triangle-electric-heavy-haul.html"]

inserted = []
skipped = []
for fn, snippet in S.items():
    p = os.path.join(BLOG, fn)
    if not os.path.exists(p):
        skipped.append((fn, "missing")); continue
    t = open(p, encoding="utf-8").read()
    if CTA_MARK not in t:
        skipped.append((fn, "CTA mark not found")); continue
    if "Frequently Asked Questions" in snippet and "Frequently Asked Questions" in t:
        skipped.append((fn, "already has FAQ")); continue
    if snippet.strip()[:20] in t:
        skipped.append((fn, "already inserted")); continue
    t = t.replace(CTA_MARK, snippet + "\n" + CTA_MARK, 1)
    open(p, "w", encoding="utf-8", newline="\n").write(t)
    inserted.append(fn)

print(f"inserted: {len(inserted)}")
for f in inserted: print("  +", f)
print(f"skipped: {skipped}")
