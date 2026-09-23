# -*- coding: utf-8 -*-
import io, os, re

BASE = r"C:/Users/69498/WorkBuddy/20260605101515/dongfeng-ev-repo/blog"
ANCHOR = '<p style="margin-top:40px;padding:16px;background:#f0f7f4;border-left:4px solid #006341;">'

S = {}

S["tz5e-vs-tz3z-electric-dump-truck-urban-comparison"] = """
<h2>Specifying Both in One Fleet</h2>
<p>Contractors running mixed programmes usually end up with both models, and the specification work then shifts from vehicle selection to fleet composition. A practical method is to split the order by material stream rather than by site: allocate TZ3Z units to the spoil, rock and demolition stream and TZ5E units to the road-facing and asphalt stream, then size each group from its own cycle model.</p>
<table border="1" cellpadding="8" cellspacing="0" style="border-collapse:collapse;width:100%;">
<tr style="background:#006341;color:#fff;"><th>Material stream</th><th>Model</th><th>Body</th><th>Cycles/shift</th></tr>
<tr><td>Spoil and topsoil</td><td>TZ3Z</td><td>Standard tipper, sealed tailgate</td><td>20–35</td></tr>
<tr><td>Rock and demolition</td><td>TZ3Z</td><td>Wear plate, reinforced floor</td><td>18–28</td></tr>
<tr><td>Asphalt</td><td>TZ5E</td><td>Insulated body</td><td>10–18</td></tr>
<tr><td>Recycled aggregate</td><td>Either</td><td>Moderate wear, sealed</td><td>15–25</td></tr>
</table>
<p>Two shared items keep a mixed fleet economical. First, standardise on one tyre specification and one telematics configuration across both models so that stock and reporting stay simple. Second, run a single charger bank sized to the combined fleet's nightly energy rather than separate chargers per model — the platforms share an energy profile, so separate provisioning would duplicate capex for no operational gain. Where a programme has a defined end date, also consider residual value: both models carry the same CATL 400 kWh pack warranty, so a documented state-of-health certificate supports resale on either when the project closes.</p>
"""

S["kth3-vs-kt5l-electric-cargo-truck-comparison"] = """
<h2>What Buyers Get Wrong About This Choice</h2>
<p>Three recurring errors account for most mis-specification between these two platforms, and all three are avoidable at quotation stage.</p>
<ul>
<li><strong>Assuming the bigger truck is always safer.</strong> Specifying the KTH3 for cube-limited work buys capability the duty never uses while adding tare, energy consumption and capital cost. A KT5L carrying packaging or textiles at 150 kg/m³ will move more usable volume per shift than a KTH3 on the same route.</li>
<li><strong>Ignoring axle limits on the delivery route.</strong> A heavier rigid may be legal on the highway but restricted on the final access road. Check the tightest constraint on the route, not the easiest.</li>
<li><strong>Specifying body length before confirming turning circle.</strong> The KT5L's longer bodies are its advantage, but a 9,000 mm body needs a yard and a delivery point that can accommodate it. Measure the worst access point on the route before ordering.</li>
</ul>
<p>A simple pre-order exercise prevents all three: log two weeks of actual loads — mass, volume, route, and access constraints — then classify each load as mass-limited or volume-limited. The split tells you the fleet mix directly, and it is the same data you will need for the energy model. Our <a href="ev-truck-battery-capacity-sizing-duty-cycle.html">battery sizing methodology</a> uses exactly this dataset, and <a href="ev-truck-fleet-rfp-tender-writing-guide.html">the RFP guide</a> shows how to turn it into a specification that suppliers can price accurately.</p>
"""

S["tz3v-electric-dump-truck-mining-emission-regulations"] = """
<h2>Building the Internal Compliance Case</h2>
<p>Regulation provides the trigger, but the approval usually has to survive an internal capital committee. Four elements make that submission defensible.</p>
<ol>
<li><strong>State the regulatory driver precisely.</strong> Name the limit, the monitoring method and the current measured exposure. A submission that says "emissions are a concern" loses to one that says "section 4 averages 0.14 mg/m³ against a 0.10 mg/m³ limit".</li>
<li><strong>Quantify the ventilation saving with the ventilation engineer.</strong> This is typically the largest single benefit in underground applications and the one most often omitted, because it sits in a different department's budget.</li>
<li><strong>Present the pilot as a measurement exercise, not a commitment.</strong> Two to four units, ninety days, defined success criteria. This lowers the approval barrier and produces the data that justifies the next tranche.</li>
<li><strong>Include the battery risk treatment explicitly.</strong> The 8-year / 4,500-cycle warranty to 80% state of health is a contractual mitigation; stating it directly answers the first question most committees ask.</li>
</ol>
<p>Where the mine reports against a corporate emissions framework, the same data supports Scope 1 reporting — see <a href="ev-truck-esg-reporting-fleet-carbon-data.html">ESG reporting and fleet carbon data</a>. And where a lender or insurer is involved, <a href="ev-truck-battery-insurance-underwriting-guide.html">battery insurance underwriting</a> explains what documentation they will request before accepting an electric fleet into the asset base.</p>
"""

S["kt5m-electric-box-truck-port-container-yard-transfers"] = """
<h2>Security and Customs Considerations</h2>
<p>Port transfer work sits inside a customs-controlled perimeter, which imposes requirements that do not apply to ordinary distribution.</p>
<ul>
<li><strong>Bonded movements.</strong> Where goods move under customs seal between a bonded warehouse and the terminal, the body must support sealing and the sealing method must be documented in the operating procedure.</li>
<li><strong>Driver and vehicle accreditation.</strong> Port access credentials are issued per driver and per vehicle; adding electric units to an accredited fleet requires the registration data to match, which is why the specification sheet matters.</li>
<li><strong>Gate camera and plate recognition.</strong> Confirm the electric units are correctly registered in the terminal operating system so that automated gate processing is not delayed by an unrecognised vehicle record.</li>
<li><strong>Charger siting inside the secure perimeter.</strong> Charging infrastructure located in a customs area may need additional approval; raise it during the port authority engagement rather than after installation.</li>
</ul>
<p>Where transfer work extends onto public roads — typically the off-dock depot leg — the vehicle also falls under general road vehicle rules, including mass and dimension limits and, in many cities, low-emission zone access. Electrification helps with the latter but not with the former: check the GVW against the road classification before committing to a route. Our <a href="kt5m-electric-box-truck-zero-emission-zone-compliance.html">zero-emission zone compliance guide</a> covers the access and registration mechanics in detail.</p>
"""

S["kt3e-electric-garbage-truck-tco-per-tonne"] = """
<h2>Fleet Mix: Sizing the Refuse Fleet Correctly</h2>
<p>Cost per tonne is also a function of fleet composition, not just vehicle choice. Three sizing errors are common and all of them raise the per-tonne figure:</p>
<ul>
<li><strong>Over-specifying body volume for dense rounds.</strong> A large body on a low-density suburban round runs partly empty; the vehicle carries tare it does not need.</li>
<li><strong>Under-specifying for peak season.</strong> In resort and seasonal districts, peak volumes can exceed average by 50% or more, forcing double runs. Specify for the peak week, not the mean.</li>
<li><strong>Ignoring the transfer station leg.</strong> Where rounds include a run to a transfer station, that leg adds distance without adding tonnes collected — a direct hit on cost per tonne. Locating transfer capacity closer to the collection area is often worth more than any vehicle change.</li>
</ul>
<p>Our recommended method is to build the round design from bin density and lift counts first, then size the body, then size the fleet. The vehicle specification follows the round, not the reverse. Related detail: <a href="kt3e-electric-garbage-truck-hotel-resort-waste-collection.html">hotel and resort collection rounds</a> and <a href="kt1d-kt3e-municipal-tender-bid-strategy.html">municipal tender bid strategy</a>.</p>
"""

S["egypt-electric-truck-spotlight-kt5j-cairo-giza"] = """
<h2>Fleet Mix for Egyptian Operators</h2>
<p>A Cairo-based distribution fleet rarely runs a single vehicle class. The practical split most operators converge on looks like this:</p>
<table border="1" cellpadding="8" cellspacing="0" style="border-collapse:collapse;width:100%;">
<tr style="background:#006341;color:#fff;"><th>Role</th><th>Model</th><th>Pack</th><th>Typical day</th></tr>
<tr><td>Dense urban last mile</td><td>KT5J</td><td>262 kWh</td><td>100–140 km, 25–40 drops</td></tr>
<tr><td>Bulky urban freight</td><td>KT5L</td><td>348 kWh</td><td>120–180 km, 12–20 drops</td></tr>
<tr><td>Regional inter-city</td><td>KTH3</td><td>400 kWh</td><td>200–320 km</td></tr>
<tr><td>Port and canal corridor</td><td>TE46</td><td>400 kWh</td><td>120–220 km shuttle</td></tr>
</table>
<p>Starting with the KT5J is the lowest-risk entry: it covers the highest-volume duty, it charges inside an existing depot supply in most cases, and it generates the operational data that makes the business case for the larger classes. Once the depot charging and telematics platform is established, adding KT5L or KTH3 units for longer legs is incremental rather than a new project. Training, spares and diagnostics carry across the range, which is why we recommend standardising on one platform rather than mixing suppliers during the electrification phase.</p>
"""

S["kt5m-electric-box-truck-urban-depot-charging-strategy"] = """
<h2>Scaling From Pilot to Full Fleet</h2>
<p>Most urban fleets electrify in three tranches, and the charging design should anticipate the third even when only the first is funded.</p>
<ol>
<li><strong>Tranche one (2–4 vehicles):</strong> install AC sockets at the bays used by the pilot vehicles, plus spare capacity in the distribution board. Do not optimise — the purpose is data, and the cheapest installation that works is correct.</li>
<li><strong>Tranche two (8–15 vehicles):</strong> extend AC to all bays and add a load-management controller. By this point the measured kWh/km data tells you the true nightly energy, and the controller is what keeps demand charges under control as the fleet grows.</li>
<li><strong>Tranche three (20+ vehicles):</strong> review the supply. Above roughly 20 box trucks the depot connection usually needs upgrading, and the lead time for that work should start a full quarter before the vehicles arrive.</li>
</ol>
<p>The recurring failure is designing each tranche independently, which produces an electrical layout that has to be reworked at every stage. Designing the final layout once and building it in phases costs marginally more in tranche one and substantially less overall. Our <a href="ev-truck-fleet-electrification-roadmap-12-month.html">12-month fleet electrification roadmap</a> sets out the sequence, and <a href="ev-truck-charging-infrastructure-capex-financing.html">charging capex and financing</a> covers how to fund the infrastructure alongside the vehicles.</p>
"""

S["dominican-republic-electric-truck-spotlight-kt5l"] = """
<h2>Working With Resort Operators</h2>
<p>Resort supply chains impose requirements that do not appear in ordinary retail distribution, and they are worth understanding before quoting a contract.</p>
<ul>
<li><strong>Delivery windows are narrow and enforced.</strong> Most resorts specify receiving hours, frequently early morning or late evening, and a vehicle that arrives outside them is turned away. Quiet electric operation is often what allows a supplier to win an earlier window.</li>
<li><strong>Service yards are tight.</strong> Resort back-of-house areas were often designed for smaller vehicles. Confirm overall length, turning circle and body height against every service yard on the route.</li>
<li><strong>Volume is seasonal.</strong> Occupancy swings of 40–70% mean the body should be specified for peak weeks, with the understanding that average-week utilisation will be lower.</li>
<li><strong>Presentation matters.</strong> Resort clients notice vehicle condition and noise. A clean, quiet vehicle is a commercial asset in this segment, which is difficult to quantify but real in contract renewals.</li>
</ul>
<p>For operators serving both resorts and city retail, the same KT5L covers both duties, which is the argument for standardising on the model rather than running a separate light vehicle for each. The 348 kWh pack covers a full day in either application with reserve, and one platform means one charger type, one training programme and one spares inventory across the whole operation.</p>
"""

S["kt3e-electric-garbage-truck-hotel-resort-waste-collection"] = """
<h2>Contract Structure and Service Levels</h2>
<p>Hospitality waste contracts are usually let on service level rather than on tonnage, which changes how an operator should price and plan an electric fleet.</p>
<ul>
<li><strong>Collection frequency is contractual.</strong> Missed collections carry penalties, so fleet availability matters more than cost per tonne. An electric fleet's higher availability — fewer unscheduled repairs, no aftertreatment faults — is directly relevant to penalty exposure.</li>
<li><strong>Noise clauses are common.</strong> Many resort contracts specify maximum noise levels or restrict collection hours. Quiet operation can be written into the bid as a differentiator rather than a compliance cost.</li>
<li><strong>Separated streams are increasingly required.</strong> Glass, organics and general waste are often collected separately, which raises lift counts and, on an electric vehicle, energy per shift. Specify the pack against separated-stream duty, not single-stream.</li>
<li><strong>Seasonality must be priced.</strong> Peak-season volume can exceed the annual average by half. Fleets sized to the average run out of capacity when occupancy peaks.</li>
</ul>
<p>Where a contractor bids both municipal and hospitality work, the same vehicle class can serve both, provided the pack is sized for the higher lift-count duty. That flexibility is one of the stronger arguments for standardising on a single refuse platform across a mixed contract book, and it simplifies the depot charging design as well.</p>
"""

S["kth3-electric-cargo-truck-fleet-operations-route-planning"] = """
<h2>Network Design: The Lever Bigger Than the Vehicle</h2>
<p>Operators often expect electrification to change their network. In most cases it should not — but measuring the network properly almost always reveals savings that exceed the vehicle change itself.</p>
<ul>
<li><strong>Consolidate low-density routes.</strong> A route running at 45% load factor costs nearly as much energy as one at 80%. Consolidating two thin routes into one full one is the single largest available saving in most regional networks.</li>
<li><strong>Re-examine the depot-to-first-drop leg.</strong> Deadhead mileage at the start and end of a shift carries no payload and consumes energy. Where a satellite parking location exists, it may be worth more than additional battery capacity.</li>
<li><strong>Sequence drops by mass, not just geography.</strong> Delivering the heaviest drops first reduces the energy consumed while the vehicle is at its heaviest, and improves regenerative recovery on the lighter remainder of the round.</li>
<li><strong>Review the return leg.</strong> Empty returns are often unavoidable, but where a backhaul exists it converts a pure cost into revenue at marginal additional energy.</li>
</ul>
<p>Each of these is measurable, and telematics makes the measurement routine rather than a one-off study. Fleets that run this exercise before their second order typically find 8–15% of network cost that has nothing to do with the vehicle specification — which is why we recommend doing it early rather than treating electrification as a purely technical project.</p>
"""

S["te46-vs-te8l-electric-tractor-terminal-comparison"] = """
<h2>Residual Value and Second-Life Considerations</h2>
<p>Both tractors carry the same CATL pack warranty, so residual value is driven by condition, documented state of health, and the depth of the used market for the configuration.</p>
<ul>
<li><strong>Terminal tractors</strong> accumulate low annual mileage relative to line-haul units, so a ten-year-old TE46 may have a relatively low cycle count — which is favourable for resale, since cycle count is what buyers of used electric trucks scrutinise.</li>
<li><strong>Line-haul tractors</strong> accumulate high mileage but predictable duty; a well-documented service history and a clean SOH certificate support value in the used market.</li>
<li><strong>Both</strong> benefit from a formal battery health certificate at disposal, which converts an unverifiable claim into a measured figure. See <a href="ev-truck-battery-soh-diagnostics-resale.html">SOH diagnostics and resale certification</a> and <a href="used-electric-truck-export-market-residual-values.html">used electric truck residual values</a>.</li>
<li><strong>Packs retired from traction</strong> at around 80% SOH retain stationary storage value, which is increasingly factored into end-of-life economics — covered in <a href="second-life-battery-ev-truck-residual-value-recycling.html">second-life battery value</a>.</li>
</ul>
<p>For fleets that replace on a fixed cycle, the practical advice is simple: instrument the pack from day one and keep the records. The difference between a documented and an undocumented battery history is worth more at disposal than most of the specification choices made at purchase.</p>
"""

S["kt1d-electric-sweeper-truck-municipal-depot-charging"] = """
<h2>Backup Power and Service Continuity</h2>
<p>Street sweeping is a visible public service, and a depot power failure that strands the fleet produces a consequence out of proportion to its cause. Three measures keep the service running:</p>
<ol>
<li><strong>N+1 charge points.</strong> One spare socket per bank means a single failure does not take a vehicle out of service.</li>
<li><strong>A priority charging hierarchy.</strong> Where supply is constrained, the controller should charge the vehicles needed for the earliest shift first. A flat priority order set once is far better than manual decisions at 02:00.</li>
<li><strong>An emergency DC unit or generator-backed charger</strong> at depots serving critical routes. One high-power unit can recover a stranded vehicle far faster than an AC socket, and it converts a service failure into a delay.</li>
</ol>
<p>Alongside the electrical resilience, build an operational fallback: a defined minimum SOC for dispatch, a procedure for swapping vehicles mid-shift, and a named contact for charger faults with a contracted response time. See <a href="ev-truck-charging-station-operations-maintenance.html">charging station operations and maintenance</a> and <a href="ev-truck-charging-contract-negotiation-guide.html">charging contract negotiation</a> for the commercial terms worth insisting on. Fleets that plan continuity in advance rarely need it, and fleets that do not plan it need it in the first winter.</p>
"""

S["tz3z-electric-dump-truck-import-guide-latin-america"] = """
<h2>After-Sales: What to Negotiate Before Signing</h2>
<p>The import is the easy part; keeping the fleet working is what determines whether a second order follows. Four items belong in the contract rather than in a later conversation.</p>
<ul>
<li><strong>Spares package for the first 12 months.</strong> Specify the contents by part number and agree who holds it — on site or at a regional warehouse. A defined kit shipped with the order avoids a three-month wait for a component that should have been stocked.</li>
<li><strong>Training scope.</strong> State the number of operators and technicians, the duration, and whether training is delivered on site or remotely. Two days of technician training is worth more than any extended warranty clause.</li>
<li><strong>Diagnostics access.</strong> Confirm that the fleet can read fault codes, state of health and energy data without proprietary tooling, and that remote support is available by video.</li>
<li><strong>Warranty claim procedure.</strong> Define what evidence is required, who decides, and the response time. The CATL pack warranty — 8 years or 4,500 cycles to 80% SOH — is only as good as the process behind it.</li>
</ul>
<p>Our export support model is described in <a href="dongfeng-ev-truck-aftermarket-parts-supply-export-fleet-support.html">aftermarket parts supply and fleet support</a>, and the wider ownership picture in <a href="ev-truck-preventive-maintenance-schedule.html">the preventive maintenance schedule</a>. Buyers who negotiate these four points before signing consistently report smoother first-year operation than those who address them after delivery.</p>
"""

S["kt7a-electric-washing-truck-tco-per-kilometre"] = """
<h2>Presenting Sensitivity, Not a Single Number</h2>
<p>A TCO model that produces one number invites one question: what if you are wrong? Municipal finance committees are right to ask, and the submission should answer before it is asked. Run at least four sensitivities and present the range.</p>
<table border="1" cellpadding="8" cellspacing="0" style="border-collapse:collapse;width:100%;">
<tr style="background:#006341;color:#fff;"><th>Variable</th><th>Low case</th><th>High case</th><th>Effect on result</th></tr>
<tr><td>Diesel price</td><td>USD 0.85/L</td><td>USD 1.35/L</td><td>Electric advantage widens as diesel rises</td></tr>
<tr><td>Electricity tariff</td><td>USD 0.07/kWh</td><td>USD 0.18/kWh</td><td>Narrows but does not reverse</td></tr>
<tr><td>Annual distance</td><td>20,000 km</td><td>36,000 km</td><td>Higher utilisation favours electric</td></tr>
<tr><td>Residual value</td><td>Equal for both</td><td>Electric +8 pts</td><td>Upside, not a base-case assumption</td></tr>
</table>
<p>The conclusion should hold across the full range. If it only holds at the favourable end, the honest answer is to wait or to pilot — and a committee will respect that more than a model that quietly assumes the best case. Where a committee wants explicit treatment of battery risk, <a href="ev-truck-battery-warranty-residual-value-insurance.html">warranty and residual risk can be insured</a>, which converts an open question into a priced line.</p>
"""

S["kta1-electric-dump-truck-asphalt-road-construction"] = """
<h2>Working With the Paving Crew</h2>
<p>The haulage fleet and the paving train are one production system, and most asphalt problems attributed to haulage are actually interface problems. Four practices prevent them:</p>
<ul>
<li><strong>Radio discipline between plant, haulage and paver.</strong> The paver operator controls the pace; the haulage fleet exists to keep it moving. A single point of contact who can adjust dispatch in real time prevents most stoppages.</li>
<li><strong>Do not dump directly into the paver hopper from a stationary queue.</strong> Trucks should back to the paver under control and in sequence; contact damage to the paver is a costly and avoidable failure.</li>
<li><strong>Manage the hold time.</strong> Holding behind the paver is where the temperature budget is spent. Dispatch should aim for a short, steady queue rather than a long one — two trucks waiting is efficient, five is waste.</li>
<li><strong>Return empty promptly.</strong> The return leg is where the cycle is recovered, and a truck idling at the paver after discharge is a truck not loading.</li>
</ul>
<p>An electric fleet changes one thing here: waiting costs almost nothing in energy, so the temptation is to run a larger buffer. Resist it — the concrete-equivalent constraint is temperature, not fuel, and a larger buffer simply means more mix cooling in more trucks.</p>
"""

S["algeria-electric-truck-spotlight-te46-port-construction"] = """
<h2>Financing and Procurement Routes</h2>
<p>Algerian fleet renewal is often financed through structures that differ from straightforward cash purchase, and the funding route affects the specification as much as the vehicle does.</p>
<ul>
<li><strong>Direct corporate purchase</strong> suits established industrial groups with existing maintenance capability and depot infrastructure.</li>
<li><strong>Leasing and operating lease structures</strong> are increasingly available and shift residual value risk off the operator's balance sheet — see <a href="ev-truck-leasing-vs-buying-decision.html">leasing versus buying</a>.</li>
<li><strong>Battery-as-a-service</strong> separates the pack from the chassis, reducing capital exposure and aligning battery risk with the party best able to manage it. Our <a href="ev-truck-baas-battery-as-a-service-economics.html">BaaS economics analysis</a> covers when it works.</li>
<li><strong>Development-finance and green facilities</strong> sometimes apply to low-emission fleet investment; worth investigating where a project has an environmental mandate.</li>
</ul>
<p>In all four cases the lender will ask two questions about an electric fleet: what is the asset worth at the end of the term, and what happens if the battery underperforms. Both are answered with documentation — the 8-year / 4,500-cycle CATL warranty, and a measurable state-of-health record from the vehicle. Our <a href="ev-truck-battery-insurance-underwriting-guide.html">battery insurance underwriting guide</a> sets out what underwriters typically require, and getting that documentation in order before approaching a lender shortens the process considerably.</p>
"""

S["tz8j-electric-mixer-truck-dispatch-fleet-operations"] = """
<h2>Handling Delays and Rejected Loads</h2>
<p>Every ready-mix operation eventually faces a load that cannot be placed: the pour stops, the site is not ready, or the concrete exceeds its working life. How the fleet handles that event determines whether it costs a load or a day.</p>
<ol>
<li><strong>Define the return threshold.</strong> Set a clear time-at-site limit after which the truck returns to the plant rather than waiting. A returned load can often be re-tempered or redirected; a load that sets in the drum cannot.</li>
<li><strong>Keep a redirection option open.</strong> A load rejected at one site may be usable at another nearby pour within its working life. Dispatch should know what else is running.</li>
<li><strong>Never let the drum stop.</strong> The single absolute rule: while concrete is in the drum, the drum turns. Battery state of charge is irrelevant to this decision, which is why the 333 kWh pack and the plant-charging strategy exist.</li>
<li><strong>Log every event.</strong> Rejected loads are a dispatch-quality metric. A pattern of rejections at one site is a contract conversation, not a fleet problem.</li>
</ol>
<p>Related operational detail: <a href="tz8j-batching-plant-relocation-electric-mixer.html">batching plant relocation work</a> and <a href="tz8j-electric-mixer-tco-per-cubic-meter.html">cost per cubic metre analysis</a>. Fleets that formalise these four steps recover a meaningful share of what would otherwise be written off, and the discipline tends to improve dispatch quality generally.</p>
"""

S["kt1d-electric-sweeper-truck-market-outlook-gulf-north-africa"] = """
<h2>What Buyers Should Ask Before Awarding</h2>
<p>Municipal procurement in both regions increasingly includes evaluation criteria beyond price. Five questions separate a credible supplier from one that will underperform after award:</p>
<ul>
<li><strong>What is the ambient temperature rating, and is the thermal package included?</strong> A unit rated for temperate duty will derate in a Gulf summer. Get the figure in writing.</li>
<li><strong>What filtration and sealing specification is supplied?</strong> Dust ingress is the leading cause of premature failure in these markets, and it is determined by the specification, not the brand.</li>
<li><strong>What does the spares package contain and where is it held?</strong> A 12-month kit on site is worth more than an extended warranty serviced from another continent.</li>
<li><strong>Is there a reference deployment in a comparable city?</strong> Comparable means comparable climate and duty, not just comparable fleet size.</li>
<li><strong>What does the training include, and in what languages?</strong> French and Arabic for North Africa; English and Arabic for the Gulf. Operator comprehension determines whether the fleet is used correctly.</li>
</ul>
<p>Tender structure guidance is in <a href="kt1d-kt3e-municipal-tender-bid-strategy.html">municipal tender bid strategy</a> and <a href="ev-truck-fleet-rfp-tender-writing-guide.html">RFP writing for fleet buyers</a>. Our <a href="dongfeng-ev-truck-aftermarket-parts-supply-export-fleet-support.html">aftermarket support page</a> sets out what we commit to on each of the five points.</p>
"""

S["kt5m-electric-box-truck-zero-emission-zone-compliance"] = """
<h2>Enforcement Reality: Cameras, Fines and Appeals</h2>
<p>Most modern zone schemes are enforced automatically by number-plate recognition rather than by roadside stops, which changes the practical risk profile for a fleet.</p>
<ul>
<li><strong>The record, not the vehicle, is what is checked.</strong> If the registration database classifies the vehicle incorrectly, the camera will fine it regardless of what is physically true. Verifying the registration record is a compliance task, not an administrative afterthought.</li>
<li><strong>Appeals are possible but slow.</strong> A misclassified vehicle generates fines until the record is corrected, and each fine requires an individual appeal. Fixing the record before deployment avoids the entire problem.</li>
<li><strong>Fleet operators should audit quarterly.</strong> Pull the plate list, confirm each vehicle's classification in the scheme database, and keep the confirmation. A quarterly audit takes an hour and prevents a five-figure fine run.</li>
<li><strong>Contractor vehicles need the same treatment.</strong> Where subcontractors enter the zone on your behalf, their vehicles must be registered correctly too — a common gap that surfaces only when a fine arrives.</li>
</ul>
<p>Where schemes phase in tighter standards, diary the change date and re-audit beforehand. Our <a href="ev-truck-fleet-change-management-workforce.html">fleet change management guide</a> covers the organisational side of running a mixed fleet through a regulatory transition, and <a href="chile-zero-emission-zones-electric-truck.html">the Santiago analysis</a> shows how a phased scheme behaves in practice.</p>
"""

S["te9l-vs-mercedes-eactros-electric-tractor-comparison"] = """
<h2>Questions to Put to Both Suppliers</h2>
<p>Whichever way a fleet leans, the same six questions should be put to both suppliers in writing, because the answers are more revealing than the brochures.</p>
<ol>
<li><strong>What is the continuous motor rating, and at what ambient temperature is it guaranteed?</strong> Peak figures are marketing; continuous rating at your operating temperature is engineering.</li>
<li><strong>What is the stated range, and under what payload, speed, gradient and ambient?</strong> A range without conditions is not a specification.</li>
<li><strong>What is the battery warranty in cycles and years, and what state-of-health threshold triggers remedy?</strong> Compare like for like: 8 years / 4,500 cycles to 80% SOH is a specific commitment.</li>
<li><strong>Where are spares held, and what is the lead time to my depot?</strong> This is usually decisive outside Europe.</li>
<li><strong>What training is included, for how many technicians, and in what language?</strong></li>
<li><strong>Can I read state of health and fault data without proprietary tooling?</strong> If not, every diagnostic event becomes a dealer visit.</li>
</ol>
<p>Suppliers that answer all six specifically are the ones that will still be supporting the fleet in year seven. Our own answers are documented in <a href="dongfeng-ev-truck-aftermarket-parts-supply-export-fleet-support.html">aftermarket and parts supply</a> and <a href="ev-truck-battery-soh-diagnostics-resale.html">SOH diagnostics</a>, and the evaluation framework is expanded in <a href="ev-truck-fleet-rfp-tender-writing-guide.html">our RFP guide</a>.</p>
"""

S["te8m-electric-tractor-steel-scrap-haulage"] = """
<h2>Weighbridge, Documentation and Site Discipline</h2>
<p>Steel and scrap operations run on documented mass, and the weighbridge is the point where vehicle specification meets commercial reality. Three items matter:</p>
<ul>
<li><strong>Tare accuracy.</strong> Every payload figure derives from gross minus tare. Re-weigh tare after any body modification, and re-record it after any significant repair. An inaccurate tare silently corrupts every transaction.</li>
<li><strong>Axle weight distribution.</strong> Scrap loads are frequently unevenly distributed, and an axle overload is an enforcement issue even when gross mass is legal. Load distribution guidance for crews pays for itself in avoided fines.</li>
<li><strong>Document the load.</strong> Photographic or telematics-linked load records resolve disputes quickly and are increasingly expected by buyers and insurers.</li>
</ul>
<p>Payload verification is covered in <a href="weigh-in-motion-telematics-ev-truck-fleet.html">weigh-in-motion and payload telematics</a>. On the vehicle side, two specification items support the same goal: a reversing camera with a wide field of view, because a tractor manoeuvring in a scrap yard has severe blind spots, and a robust underbody protection package, because debris in the yard is the leading cause of damage to components mounted beneath the chassis.</p>
"""

S["te8l-electric-tractor-charging-planning-long-corridors"] = """
<h2>What to Do When the Grid Connection Slips</h2>
<p>Grid connection delays are the most common cause of a corridor electrification programme missing its date. Four mitigations keep the plan intact:</p>
<ul>
<li><strong>Phase the corridor.</strong> Open the sections where depot charging at either end is already sufficient, and defer the mid-route node until its connection lands. Partial operation is better than none.</li>
<li><strong>Use battery-buffered or generator-backed chargers</strong> as an interim measure at the mid-route node. Higher cost per kWh, but it keeps the schedule.</li>
<li><strong>Reduce the energy requirement temporarily</strong> by adjusting payload or scheduling — for example, running the corridor with a lighter trailer specification during the interim period.</li>
<li><strong>Apply for the connection at the same time as ordering vehicles, not after.</strong> This is the actual fix; the other three are damage control.</li>
</ul>
<p>Contractually, the charging provider's obligation should be tied to a date with a remedy, because the vehicle supplier can deliver on time and still be blamed for a programme failure caused by the electrical connection. See <a href="ev-truck-charging-contract-negotiation-guide.html">charging contract negotiation</a> and <a href="ev-truck-depot-charging-fire-code-permitting.html">fire code and permitting</a>, which covers the approvals that frequently sit on the same critical path.</p>
"""

S["tz5e-electric-dump-truck-urban-emission-rules-night-permits"] = """
<h2>Community Relations on Constrained Sites</h2>
<p>Permits are granted by authorities, but they are often influenced by residents — and a site that manages its neighbours well gets fewer complaints and faster approvals on the next application.</p>
<ul>
<li><strong>Publish the working schedule</strong> and a contact number at the site gate. Most complaints escalate because nobody could reach anyone.</li>
<li><strong>Log and respond to complaints within a defined period.</strong> A documented response procedure is frequently a permit condition and always a credibility asset.</li>
<li><strong>Keep haul roads watered and wheel washes working.</strong> Dust and mud on adjacent streets generate more complaints than noise in most residential contexts.</li>
<li><strong>Use the electric fleet visibly.</strong> Where a site has invested in zero-emission plant, saying so in community communications converts a cost into goodwill — and it is factually defensible, which matters if challenged.</li>
</ul>
<p>Where monitoring is required, place boundary monitors before work starts so there is a baseline. A baseline makes subsequent readings interpretable and protects the contractor against complaints that predate the site. Related: <a href="tz3z-night-operations-electric-dump-truck.html">night operations practice</a> and <a href="ev-truck-fleet-change-management-workforce.html">managing workforce change</a> when introducing electric plant to crews.</p>
"""

S["te8p-electric-tractor-battery-motor-engineering"] = """
<h2>What to Measure Before the Second Order</h2>
<p>Heavy haul electrification is usually proven on one route before it scales, and the pilot should be instrumented to answer four specific questions.</p>
<ol>
<li><strong>Energy per move against the model.</strong> Log kWh for the full route, split by segment, and compare with the pre-move estimate. The gap tells you whether the gradient and surface assumptions were right.</li>
<li><strong>Arrival state of charge against the reserve policy.</strong> If moves consistently arrive below the intended reserve, the pack or the route plan needs revision before the next route is added.</li>
<li><strong>Regenerative recovery on descents.</strong> Compare the descent recovery actually achieved with the modelled figure. Where recovery is lower than expected, the cause is usually a full pack at departure or a BMS thermal limit — both fixable operationally.</li>
<li><strong>Derating events.</strong> Record every instance where output was reduced for thermal reasons, with ambient temperature and gradient. This is the data that decides whether a larger thermal package is needed on the next order.</li>
</ol>
<p>Telemetry makes all four automatic, and the dataset is what turns the second order from a gamble into a specification. See <a href="dongfeng-ev-truck-telemetry-fleet-management.html">fleet telemetry</a> and <a href="ev-truck-real-world-range-testing-methodology.html">real-world range testing methodology</a>.</p>
"""

S["tz8j-electric-mixer-truck-charging-strategy-batching-plants"] = """
<h2>Water, Admixtures and Load Temperature</h2>
<p>Charging is not the only plant-side variable that affects the energy budget. Concrete temperature management interacts directly with how much energy the vehicle has available.</p>
<ul>
<li><strong>Hot-weather concreting</strong> often requires chilled water or ice at the plant, which is a plant energy cost rather than a vehicle one — but it reduces the vehicle's refrigeration and drum load on site, which helps the pack.</li>
<li><strong>Admixture strategy</strong> can extend working life without additional on-board energy, which reduces the cost of delays far more effectively than any vehicle change.</li>
<li><strong>Shading the drum</strong> during long holds is a low-cost measure with a measurable effect on discharge temperature in high-ambient markets.</li>
<li><strong>Load scheduling</strong> that places the largest pours in the coolest part of the day reduces both concrete temperature risk and vehicle cooling load simultaneously.</li>
</ul>
<p>These are dispatch and plant decisions rather than vehicle decisions, but they change the energy the truck must supply, and they belong in the same model as the charger sizing. Operators who optimise only the charger and ignore the concrete temperature strategy typically over-specify the pack. Related: <a href="kt9x-electric-mixer-saudi-giga-projects.html">giga-project mixer deployment</a> and <a href="electric-mixer-drum-body-specification.html">drum body specification</a>.</p>
"""

S["tz5e-electric-dump-truck-urban-site-fleet-operations"] = """
<h2>Measuring Site Productivity Properly</h2>
<p>Tonnes per day is the number a site is judged on, but it is a poor diagnostic: it tells you the result without telling you which constraint produced it. Decompose it instead.</p>
<table border="1" cellpadding="8" cellspacing="0" style="border-collapse:collapse;width:100%;">
<tr style="background:#006341;color:#fff;"><th>Component</th><th>How to measure</th><th>Typical improvement available</th></tr>
<tr><td>Loader cycle efficiency</td><td>Loads per loader-hour</td><td>10–20% from better truck-to-loader ratio</td></tr>
<tr><td>Queue time</td><td>Telematics dwell at load point</td><td>15–30% from staggered starts</td></tr>
<tr><td>Haul and return time</td><td>Cycle time excluding queue</td><td>5–15% from road maintenance</td></tr>
<tr><td>Tip and turn time</td><td>Time at discharge point</td><td>10–20% from better tip-face management</td></tr>
<tr><td>Availability</td><td>Operating hours ÷ planned hours</td><td>3–8% from preventive discipline</td></tr>
</table>
<p>Measure all five for two weeks before changing anything, then address the largest constraint first. Sites that skip straight to buying more trucks usually discover the loader was the bottleneck all along. Our <a href="ev-truck-pilot-program-design-10-trucks.html">pilot programme design guide</a> sets out the measurement structure, and <a href="weigh-in-motion-telematics-ev-truck-fleet.html">payload telematics</a> covers the load data needed to convert cycle counts into tonnes.</p>
"""

S["te9l-electric-tractor-driver-route-engineering"] = """
<h2>Handling Deviations From Plan</h2>
<p>A route energy plan is built on assumptions, and the road does not always cooperate. Drivers need a defined procedure for the four deviations that actually occur:</p>
<ul>
<li><strong>Roadworks or diversion.</strong> Any unplanned additional distance consumes reserve. The rule: report to dispatch immediately, and let dispatch decide whether to reroute, recharge or swap the load.</li>
<li><strong>Severe weather.</strong> Headwind, heavy rain and extreme heat all raise consumption — by 8–15% in bad cases. Dispatch should add margin to the plan when weather warnings are issued rather than discovering the shortfall at the destination.</li>
<li><strong>Charger unavailable at the planned stop.</strong> Every corridor plan needs a designated alternate stop with the charger type and location recorded in the cab, not only in the office.</li>
<li><strong>Extended dwell at a customer site.</strong> Waiting with HVAC running consumes energy; drivers should know the cabin preconditioning settings that minimise draw while stationary.</li>
</ul>
<p>None of these is exotic, and all of them are cheaper to plan for than to experience. Fleets that brief drivers on deviations, rather than only on the nominal route, consistently run closer to plan. See <a href="ev-truck-driver-incentive-scheme-design.html">driver incentive scheme design</a> for how to align driver behaviour with the energy plan, and <a href="ev-truck-smart-charging-load-management.html">depot load management</a> for the depot-side equivalent.</p>
"""

S["kta1-electric-dump-truck-cement-plant-raw-material-haulage"] = """
<h2>Weighing, Blending and Quality Control</h2>
<p>Cement production is a chemistry process, and the haulage fleet is part of the quality chain rather than just a materials mover. Three interfaces matter:</p>
<ul>
<li><strong>Blend consistency.</strong> Limestone from different quarry faces has different chemistry. Where blending is controlled at the face or the stockpile, the haulage plan must follow the blend instruction exactly — a truck loaded from the wrong face is a quality incident, not a logistics one.</li>
<li><strong>Weighbridge accuracy.</strong> Crusher feed rates and blend ratios depend on accurate mass. Re-verify tare after body repairs, and calibrate on a schedule.</li>
<li><strong>Contamination control.</strong> Bodies carrying clinker, gypsum or additives should not cross-contaminate. Where a fleet runs multiple material streams, dedicated units or documented cleanout procedures prevent off-spec product.</li>
</ul>
<p>An electric fleet supports all three: predictable cycle times make blend scheduling more reliable, and telematics-linked load records give the quality team an auditable chain. Our <a href="weigh-in-motion-telematics-ev-truck-fleet.html">payload telematics guide</a> covers the measurement, and <a href="kta1-electric-dump-truck-aggregates-recycling.html">aggregates and recycling duty</a> covers the related case where material streams must be kept separate.</p>
"""

S["kt5j-electric-delivery-truck-retail-replenishment"] = """
<h2>Returns, Reverse Logistics and Empty Handling</h2>
<p>Retail routes are rarely one-directional. Returns, roll-cage recovery and packaging take-back add distance and dwell without adding drops, and they are frequently omitted from the energy model.</p>
<ul>
<li><strong>Returns volume varies by season and by chain.</strong> Post-promotional periods and post-holiday weeks generate substantially more returns; model the peak, not the average.</li>
<li><strong>Roll-cage recovery changes the body requirement.</strong> Empty cages consume cube that would otherwise carry outbound goods, which effectively reduces usable payload on the return-leg portion of the round.</li>
<li><strong>Dwell at the returns point is often longer than at delivery.</strong> Counting and signing for returns takes time; include it in the route schedule or the round will overrun.</li>
<li><strong>An electric vehicle handles this better than diesel.</strong> Long stationary periods with the vehicle parked cost almost nothing, so reverse logistics duty is one of the more favourable applications for electrification on a cost-per-stop basis.</li>
</ul>
<p>Include returns in the pilot measurement. Fleets that size the pack on outbound distance alone discover the shortfall in the first peak week. Related: <a href="kt5j-electric-delivery-truck-deep-dive.html">KT5J platform deep dive</a> and <a href="kt5j-electric-delivery-truck-tco-last-mile.html">last-mile TCO analysis</a>.</p>
"""

S["kt7a-electric-washing-truck-product-deep-dive"] = """
<h2>Water Recycling and Environmental Compliance</h2>
<p>High-pressure washing consumes significant water, and in water-stressed markets the environmental case for a washing truck increasingly depends on how that water is managed.</p>
<ul>
<li><strong>Recycling units</strong> can recover a share of wash water for reuse, reducing both consumption and the number of refill trips — which improves productive time per shift as well as environmental performance.</li>
<li><strong>Runoff control matters.</strong> Wash water carrying oil, detergents and suspended solids must not enter storm drains. Specify collection or settlement at the wash area, and train crews on it.</li>
<li><strong>Detergent selection affects compliance.</strong> Biodegradable agents simplify discharge permitting in most jurisdictions and are increasingly specified in municipal contracts.</li>
<li><strong>Meter the water.</strong> Consumption per shift is a management metric; unmetered fleets cannot demonstrate improvement, and improvement is what regulators and clients ask about.</li>
</ul>
<p>Where a municipality has published water-use or discharge conditions, an electric washing truck with a documented recycling and runoff plan is materially easier to approve than a diesel equivalent that satisfies neither the noise nor the discharge requirements. Related: <a href="kt3f-kt7a-water-tank-body-specification.html">tank body specification</a> and <a href="kt7a-electric-sprinkler-municipal-fleet-electrification.html">municipal fleet electrification</a>.</p>
"""

S["kt3f-electric-sprinkler-truck-product-deep-dive"] = """
<h2>Seasonal Duty and Water Scarcity</h2>
<p>Sprinkler duty is seasonal in most markets, and specification should reflect the peak rather than the annual average — while acknowledging that water availability, not vehicle capacity, is increasingly the binding constraint.</p>
<ul>
<li><strong>Peak season demand</strong> in dry months can run two to three times the wet-season requirement. Fleets sized to the average run short exactly when dust control matters most.</li>
<li><strong>Water source planning</strong> determines productivity. A truck that must travel ten kilometres to refill spends more time fetching than distributing. Map refill points against routes before specifying tank size.</li>
<li><strong>Recycled and treated water</strong> is increasingly used for road watering, which reduces cost but may require filtration to protect pumps and nozzles — specify accordingly.</li>
<li><strong>Application rate control</strong> matters more than tank size in water-scarce markets. Calibrated nozzles and flow control deliver the required coverage with less water, which is both an environmental and an operational improvement.</li>
</ul>
<p>Where municipal budgets are constrained, the productivity argument usually wins the case: a correctly specified electric sprinkler covers more road-kilometres per shift than a diesel equivalent, because it does not stop for fuel, does not idle expensively in queues, and can work extended windows without noise complaints. Related: <a href="kt3f-electric-sprinkler-mining-haul-roads.html">haul road dust control</a> and <a href="kt3f-port-stockyard-dust-control.html">port stockyard application</a>.</p>
"""

S["kt5l-electric-cargo-truck-product-deep-dive"] = """
<h2>Resale, Reassignment and Fleet Flexibility</h2>
<p>Medium rigids are the most flexible asset in most fleets, and that flexibility is worth specifying for. Three considerations:</p>
<ul>
<li><strong>Body interchangeability.</strong> Where a fleet might reassign a vehicle between dry freight and temperature-controlled work, specifying the chassis and electrical provisions for a reefer body at purchase is far cheaper than retrofitting later.</li>
<li><strong>Standardised body mounting.</strong> Keeping one mounting interface across the fleet allows bodies to move between chassis as demand changes, which extends the useful life of both.</li>
<li><strong>Documented battery health.</strong> A 348 kWh pack warranted 8 years / 4,500 cycles to 80% SOH, with a readable state-of-health record, is what supports resale value when the vehicle is reassigned or sold. See <a href="ev-truck-battery-soh-diagnostics-resale.html">SOH diagnostics and resale</a>.</li>
</ul>
<p>Fleets that expect to reassign vehicles between duties should say so at quotation stage, because it changes the electrical and mounting specification. Fleets with stable, single-purpose routes can optimise more narrowly and save capital. Both approaches are correct; what costs money is discovering the requirement after delivery.</p>
"""

S["tz3v-electric-dump-truck-buying-guide-mining-specs"] = """
<h2>Operator Training on Large Electric Tippers</h2>
<p>An 8x4 electric tipper at 60 tonnes is not a vehicle that operators adapt to by instinct. Four training elements consistently separate fleets that hit their productivity targets from those that do not:</p>
<ol>
<li><strong>Regenerative braking on haul roads.</strong> Most of the energy recovery available on a mine haul road comes from anticipating the descent and letting regeneration hold speed. Taught properly, this is worth 8–15% of shift energy.</li>
<li><strong>Payload discipline.</strong> Overloading an electric tipper does not cause more fuel burn — it causes range shortfalls and tyre and suspension damage. Crews need to understand the new failure mode.</li>
<li><strong>Charging and swap procedure.</strong> Who connects, when, and what the minimum departure state of charge is. Written, enforced, and reported through telematics.</li>
<li><strong>Fault reporting.</strong> What to photograph, what data to capture, who to call. This is what converts a warranty claim from a dispute into a service ticket.</li>
</ol>
<p>We deliver this as part of commissioning, and it is the single highest-return item in the deployment budget. See <a href="electric-truck-driver-training-program-fleet.html">the driver training programme</a> and <a href="ev-truck-driver-incentive-scheme-design.html">incentive scheme design</a> for sustaining the behaviour after the trainers leave.</p>
"""

S["te46-electric-tractor-fleet-operations-shift-planning"] = """
<h2>Handling Peak and Disruption</h2>
<p>Terminal operations face two predictable stresses: vessel peaks, when throughput doubles for 48 hours, and disruption, when a berth or gate closes. Both test the charging plan.</p>
<ul>
<li><strong>Peak planning.</strong> Model the peak day, not the average day. If the fleet's nightly energy in peak exceeds the depot's charging capacity, the answer is usually a mid-shift opportunity charge rather than more charger capacity used only occasionally.</li>
<li><strong>Reserve policy during peaks.</strong> Relax the arrival reserve floor slightly during declared peaks, but never below what the route requires with margin — and reinstate it immediately afterwards.</li>
<li><strong>Disruption response.</strong> When the gate closes, trucks idle. An electric fleet idles almost for free, which is a genuine advantage: a diesel fleet burns fuel through a two-hour closure, an electric one does not.</li>
<li><strong>Recovery charging.</strong> After a disruption, the fleet may return at unusually low state of charge simultaneously. Load management matters most at exactly this moment, which is why the controller's priority hierarchy should be set in advance.</li>
</ul>
<p>Our <a href="ev-truck-charging-uptime-redundancy-design.html">charging uptime redundancy guide</a> covers the engineering, and <a href="ev-truck-pilot-program-design-10-trucks.html">pilot programme design</a> covers how to test peak behaviour before committing the full fleet.</p>
"""

S["te8p-electric-tractor-heavy-equipment-haulage-permits"] = """
<h2>Insurance and Liability for Abnormal Loads</h2>
<p>Heavy haul insurance is priced around the load, the route and the operator's safety record — and introducing electric vehicles into that equation raises questions underwriters will ask.</p>
<ul>
<li><strong>Declared value of the load.</strong> Transformers and mill components can be worth more than the tractor. Confirm that the policy covers the load, not just the vehicle.</li>
<li><strong>Route risk assessment.</strong> Underwriters increasingly expect a documented route survey, including gradient, bridge capacity and turning analysis. This is the same document the permit application needs, so produce it once.</li>
<li><strong>Battery and high-voltage documentation.</strong> UN 38.3, thermal management description and emergency response data are standard requests. See <a href="ev-truck-battery-insurance-underwriting-guide.html">battery insurance underwriting</a>.</li>
<li><strong>Recovery planning.</strong> A disabled combination carrying a 90-tonne transformer is a serious incident. Confirm the recovery provider can handle both the mass and the high-voltage system — covered in <a href="ev-truck-high-voltage-rescue-towing-safety.html">high-voltage rescue and towing</a>.</li>
</ul>
<p>Operators who prepare these four items before approaching insurers typically find electric heavy haul straightforward to place, because the underlying risk profile is unchanged by the powertrain. Those who present it as a novelty invite a slower, more cautious underwriting process than the risk warrants.</p>
"""

S["te8m-electric-tractor-battery-charging-architecture"] = """
<h2>Reading the Data Before Specifying the Next Batch</h2>
<p>The second order should be specified from measured data rather than from the assumptions used for the first. Four data series matter most, and all are available from the vehicle's telematics export:</p>
<ul>
<li><strong>Energy per route pair</strong> — loaded plus empty, by route and by shift. This is what determines whether the next pack should be larger, smaller or the same.</li>
<li><strong>Distribution of arrival state of charge.</strong> If the fleet consistently arrives with large margin, the next order can take the smaller pack and save capital. If arrivals cluster near the reserve floor, the larger pack is justified.</li>
<li><strong>Thermal events and derating incidents.</strong> Recorded with ambient temperature and duty, this decides whether the thermal package specification needs to change for the next batch.</li>
<li><strong>Charger utilisation and session success rate.</strong> Low utilisation means the charger bank is oversized; a low success rate means a maintenance or scheduling problem that will get worse as the fleet grows.</li>
</ul>
<p>Our <a href="dongfeng-ev-truck-telemetry-fleet-management.html">fleet telemetry guide</a> covers the data structure, and <a href="ev-truck-thermal-management-field-data-analysis.html">thermal management field data</a> shows how to interpret the thermal series. Fleets that run this review before the second order consistently land closer to optimal specification than those that simply reorder the same configuration.</p>
"""

S["tz3z-electric-dump-truck-dam-reservoir-construction"] = """
<h2>Seasonal and Weather Constraints on Earthworks</h2>
<p>Dam and reservoir projects are governed by the hydrological calendar, and the haulage plan has to fit inside it. Three constraints shape the fleet requirement:</p>
<ul>
<li><strong>The working season.</strong> Most earthworks are concentrated in the dry months, which compresses an enormous volume of material movement into a limited window. Fleet size is set by peak-season tonnage, not annual average.</li>
<li><strong>Rain and road condition.</strong> Wet haul roads raise rolling resistance sharply and can halt operations entirely. Budget for road maintenance capacity as seriously as for trucks, because a soft road stops an electric fleet as effectively as a diesel one.</li>
<li><strong>River diversion deadlines.</strong> Foundation excavation must typically complete before the next flood season — a hard date that makes fleet availability more valuable than fleet cost.</li>
</ul>
<p>An electric fleet serves this pattern well: peak-season intensity means long daily operating hours, which is exactly where fuel and maintenance savings accumulate fastest, and where the absence of engine-related downtime protects a critical-path date. Where the working window extends into night shifts for schedule recovery, the noise advantage also removes a constraint that would apply to diesel plant near any settlement. See <a href="ev-truck-tropical-climate-corrosion-protection.html">corrosion protection for wet climates</a> and <a href="kta1-electric-dump-truck-asphalt-road-construction.html">fleet sizing against a production train</a>.</p>
"""

ok = fail = 0
for name, snippet in S.items():
    p = os.path.join(BASE, name + ".html")
    if not os.path.exists(p):
        print("MISSING", name); fail += 1; continue
    with io.open(p, "r", encoding="utf-8") as f:
        html = f.read()
    if ANCHOR not in html:
        print("NO ANCHOR", name); fail += 1; continue
    html = html.replace(ANCHOR, snippet.strip() + "\n\n" + ANCHOR, 1)
    with io.open(p, "w", encoding="utf-8") as f:
        f.write(html)
    ok += 1

print("inserted:", ok, "failed:", fail)
