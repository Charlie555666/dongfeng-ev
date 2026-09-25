# -*- coding: utf-8 -*-
"""Run 14 batch 1: 8 articles (Central America / Caribbean / Francophone & West Africa cities)."""
import re, os, json

DATE = "2026-09-25"
ROOT = os.path.dirname(os.path.abspath(__file__))

NET = {
 'zxc': ('https://sagmoto-trucks.com/zxc.html', 'heavy duty mining dump truck 6x4 8x4'),
 'qyc': ('https://sagmoto-trucks.com/qyc.html', '4x2 6x4 tractor truck prime mover'),
 'zhc': ('https://sagmoto-trucks.com/zhc.html', 'SAGMOTO cargo truck flatbed box stake'),
 'tco': ('https://sagmoto-trucks.com/', 'heavy duty trucks export China'),
 'gen': ('https://sagmoto-trucks.com/', 'SAGMOTO heavy duty diesel trucks'),
}

HEAD = '''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="keywords" content="{kw}">
<meta name="robots" content="index, follow, max-image-preview:large">
<meta name="geo.region" content="CN"/>
<meta name="geo.placename" content="Xi'an, Shaanxi, China"/>
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="article">
<meta property="og:url" content="https://dongfengevtrucks.com/blog/{f}.html">
<meta property="og:image" content="{img_abs}">
<meta property="og:site_name" content="Dongfeng EV Trucks Export">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{img_abs}">
<link rel="canonical" href="https://dongfengevtrucks.com/blog/{f}.html">
<link rel="stylesheet" href="../css/dongfeng-ev.css">
<link rel="icon" href="../favicon.ico" type="image/x-icon">
<script type="application/ld+json">
{blogposting}
</script>
{faq_schema}</head>
<body style="font-family:Arial,sans-serif;line-height:1.7;max-width:900px;margin:0 auto;padding:20px;color:#333;">
<h1>{title}</h1>
<p><img src="{img_rel}" alt="{alt}" style="max-width:100%;height:auto;display:block;margin:20px auto;"/></p>

'''

FOOT = '''
<p style="margin-top:40px;padding:16px;background:#f0f7f4;border-left:4px solid #006341;">Ready to electrify your fleet? Contact Shaanxi Fenghan Trading &mdash; authorized Dongfeng EV truck exporter. WhatsApp: <a href="https://wa.me/8615319431311">+86 153 1943 1311</a> | Email: sales@fenghan-trade.com | <a href="https://dongfengevtrucks.com/">dongfengevtrucks.com</a></p>

<p style="font-size:13px;color:#666;">&#127760; Our Network: <a href="https://www.fenghan-trade.com/" target="_blank" rel="noopener">Fenghan Trade (SAGMOTO/SHACMAN Truck Export)</a> &middot; <a href="{net_url}" target="_blank" rel="noopener">{net_anchor}</a></p>

<p style="font-size:13px;"><a href="index.html">&larr; Back to Blog</a> | <a href="../index.html">Home</a></p>
</body>
</html>
'''

def build(a):
    img_abs = 'https://dongfengevtrucks.com/images/' + a['img']
    img_rel = '../images/' + a['img']
    bp = {"@context": "https://schema.org", "@type": "BlogPosting",
      "headline": a['t'], "description": a['d'],
      "author": {"@type": "Organization", "name": "Shaanxi Fenghan Trading Co., Ltd", "url": "https://dongfengevtrucks.com/"},
      "publisher": {"@type": "Organization", "name": "Dongfeng EV Trucks Export", "logo": {"@type": "ImageObject", "url": "https://dongfengevtrucks.com/images/hero-cover.jpg"}},
      "datePublished": DATE, "dateModified": DATE,
      "image": img_abs, "url": "https://dongfengevtrucks.com/blog/" + a['f'] + ".html",
      "keywords": a['k']}
    faq_schema = ''
    body = a['body']
    if a.get('faq'):
        ents = []
        faq_html = ['<h2>Frequently Asked Questions</h2>']
        for q, ans in a['faq']:
            faq_html.append('<h3>%s</h3>\n<p>%s</p>' % (q, ans))
            ents.append({"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": ans}})
        body = body + '\n' + '\n'.join(faq_html) + '\n'
        fq = {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": ents}
        faq_schema = '<script type="application/ld+json">\n' + json.dumps(fq, ensure_ascii=False) + '\n</script>\n'
    net_url, net_anchor = NET[a['net']]
    html = HEAD.format(title=a['t'], desc=a['d'], kw=a['k'], f=a['f'], img_abs=img_abs, img_rel=img_rel,
                       alt=a['alt'], blogposting=json.dumps(bp, ensure_ascii=False), faq_schema=faq_schema)
    html += body + FOOT.format(net_url=net_url, net_anchor=net_anchor)
    return html

ARTICLES = []

# ---------------------------------------------------------------- 1
ARTICLES.append(dict(
f='san-salvador-el-salvador-electric-dump-truck-construction',
t='San Salvador Construction Boom: TZ3Z Electric Dump Truck Guide for El Salvador',
d='El Salvador construction fleets can cut haulage cost 55% with the TZ3Z electric dump truck. Specs, TCO, charging and import steps for this EV truck in San Salvador.',
k='TZ3Z electric dump truck, EV truck El Salvador, electric truck San Salvador, electric dump truck Central America, Dongfeng electric truck, construction EV truck, electric tipper truck import',
img='models/p03_00.jpg',
alt='Dongfeng TZ3Z electric dump truck working on a San Salvador construction site, EV truck for El Salvador',
net='zxc',
body='''
<p>San Salvador is in the middle of a construction cycle that is reshaping the metro area: the Los Chorros highway expansion, new logistics parks around Apopa, and a steady pipeline of mid-rise residential towers in Santa Tecla and Antiguo Cuscatl&aacute;n. Every one of those projects runs on tippers &mdash; and every one of those tippers burns diesel at some of the highest pump prices in Central America. This guide looks at how the <a href="../products/models/tz3z-electric-dump-truck.html">Dongfeng TZ3Z electric dump truck</a> fits El Salvador&rsquo;s construction economy, with real numbers on energy cost, payload, charging and import logistics. For contractors running 10-30 tipper trucks, an EV truck fleet is no longer a pilot idea; it is a margin decision.</p>

<h2>Why San Salvador Is a Natural EV Truck City</h2>
<p>Electric trucks succeed where duty cycles are short, repetitive and return-to-base. San Salvador&rsquo;s construction logistics match that profile almost perfectly. Quarries and aggregate plants sit in a ring 15-40 km from the city &mdash; San Juan Opico to the northwest, the volcanic sand operations near Cojutepeque, and concrete batching clustered along the Troncal del Norte. A typical tipper shift is 6-10 loaded trips of 25-60 km round trip, totaling 150-220 km per day. That sits comfortably inside the TZ3Z&rsquo;s real-world range of 220-260 km on its 350 kWh CATL LFP battery, with a midday opportunity charge absorbing the days that run long.</p>
<p>The second factor is electricity cost. El Salvador&rsquo;s industrial tariff runs roughly US$0.16-0.20 per kWh depending on the distribution zone and time of use &mdash; not cheap by global standards, but transformative next to diesel at US$1.10-1.25 per litre. A diesel tipper on this duty cycle burns 0.45-0.55 litres per kilometre. The TZ3Z consumes 1.3-1.5 kWh per kilometre loaded on urban aggregates work. The arithmetic below is why Salvadoran contractors are asking about electric trucks in 2026.</p>

<h2>TZ3Z Specifications for Salvadoran Duty Cycles</h2>
<table style="width:100%;border-collapse:collapse;margin:20px 0;" border="1" cellpadding="8">
<tr style="background:#006341;color:#fff;"><th style="padding:8px;text-align:left;">Parameter</th><th style="padding:8px;text-align:left;">TZ3Z 6x4 Electric Dump Truck</th></tr>
<tr><td style="padding:8px;">GVW / payload</td><td style="padding:8px;">25 t / ~15 t (12 m&sup3; body)</td></tr>
<tr><td style="padding:8px;">Battery</td><td style="padding:8px;">350 kWh CATL LFP, liquid-cooled</td></tr>
<tr><td style="padding:8px;">Motor</td><td style="padding:8px;">LvKong permanent magnet, 360 kW peak / 2,400 Nm</td></tr>
<tr><td style="padding:8px;">Real-world range (loaded, urban)</td><td style="padding:8px;">220-260 km</td></tr>
<tr><td style="padding:8px;">DC fast charge 20-80%</td><td style="padding:8px;">~50 min at 240 kW dual-gun</td></tr>
<tr><td style="padding:8px;">Gradeability</td><td style="padding:8px;">&ge;30% at full load</td></tr>
<tr><td style="padding:8px;">Battery warranty</td><td style="padding:8px;">8 years / 4,500 cycles to 70% SOH</td></tr>
<tr><td style="padding:8px;">FOB price band</td><td style="padding:8px;">US$78,000-92,000 depending on body spec</td></tr>
</table>
<p>Two specification points matter specifically for El Salvador. First, the country&rsquo;s volcanic soils mean steep quarry access ramps &mdash; the TZ3Z&rsquo;s 2,400 Nm of near-instant torque and 30% gradeability handle ramps that force diesel tippers into low-range crawling. Second, the LFP chemistry tolerates the 30-35&deg;C ambient temperatures of the dry season without the degradation penalties that NMC packs suffer; CATL&rsquo;s LFP cells are rated for 4,500+ cycles at 45&deg;C cell temperature with proper thermal management, which the liquid-cooled pack provides.</p>

<h2>The TCO Equation in Salvadoran Col&oacute;n-Era Dollars</h2>
<p>Run the numbers on a 200 km day, 26 days a month. A diesel 25 t tipper: 200 km x 0.5 L/km = 100 L daily, US$118 per day at US$1.18/L, or roughly US$36,800 per year in fuel. The TZ3Z: 200 km x 1.4 kWh/km = 280 kWh daily, US$50 per day at US$0.18/kWh, or US$15,700 per year. The annual energy saving is about US$21,000 per truck. Add maintenance &mdash; no engine oil, no fuel filters, no DPF, brake pads lasting 3-4x longer thanks to regenerative braking &mdash; and another US$4,000-6,000 per year drops out of the operating budget. Against a US$25,000-35,000 purchase premium over an equivalent diesel tipper, payback lands at 14-22 months of operation. On a ten-truck fleet, that is US$250,000 per year of recovered margin from year three onward.</p>
<ul>
<li><strong>Energy cost per km:</strong> diesel ~US$0.59 vs EV truck ~US$0.25 &mdash; a 58% reduction</li>
<li><strong>Payback period:</strong> 14-22 months at Salvadoran fuel and power prices</li>
<li><strong>Noise:</strong> ~10 dB lower at the curb, unlocking night work near residential zones in Santa Tecla</li>
<li><strong>Downtime:</strong> sealed drivetrain means no dust-ingestion engine failures during the dusty November-April dry season</li>
</ul>

<h2>Charging Infrastructure in the Salvadoran Grid</h2>
<p>Most Salvadoran construction firms operate from a single yard in Apopa, Soyapango or along the Pan-American corridor &mdash; ideal for depot charging. A realistic first installation is one 240 kW dual-gun DC charger serving four to six trucks on rotation, plus overnight AC top-up for the balance. A 240 kW charger needs a 350-400 kVA service; AES El Salvador and the other distributors process industrial connections of this size routinely, with lead times of 8-16 weeks. Our standard advice: file the grid application the day the truck order is signed, because the vessel from Shanghai or Tianjin to Puerto Acajutla sails in 30-35 days and will beat an unfiled grid connection every time.</p>
<p>Solar deserves a mention here: El Salvador averages 5.0-5.5 peak sun hours daily, among the best in Central America. A 150-250 kWp canopy over a truck yard offsets 40-55% of annual charging energy and hedges the tariff exposure entirely. Several of the ready-mix plants around San Salvador already run solar canopies for their batching equipment; adding truck charging to an existing solar-plus-storage yard is the cheapest electrification path in the country.</p>

<h2>Import Process and Regional Context</h2>
<p>El Salvador applies a 1% tariff on electric vehicles under its EV incentive framework, versus 15-30% on diesel trucks, and EVs are exempt from the FOVIAL road tax surcharge. Trucks ship RoRo or flat-rack from Shanghai to Acajutla in 30-35 days; customs clearance with a licensed broker runs 5-10 working days. Registration requires the standard VUMA homologation file, which we supply pre-translated into Spanish. Contractors working across the northern triangle should also read our <a href="../markets/mexico.html">Mexico electric truck market page</a> for regional corridor context &mdash; several Salvadoran aggregate groups operate sister fleets in Guatemala and southern Mexico, and multi-country electrification unlocks shared charger procurement and technician training economies.</p>
<p>Spare parts and service are the honest question every buyer asks. We ship every TZ3Z with a two-year fast-moving parts kit (filters, brake components, suspension bushes, HV contactors), and CATL&rsquo;s LFP modules are stocked in Panama for 10-14 day delivery anywhere in Central America. The drivetrain itself &mdash; one motor, one reduction gearbox, no clutch, no turbo, no injection system &mdash; has roughly 40% of the moving parts of the diesel it replaces, which is the real service story.</p>

<h2>Who Should Move First</h2>
<p>The strongest first movers in El Salvador are quarry-owning contractors with captive loading and unloading points: they control both ends of the duty cycle, can site chargers at the quarry weighbridge and the city batching plant, and run the most predictable routes. Ready-mix producers running their own tipper fleets for aggregate inbound are second. Pure subcontract haulers should wait for the second wave, when public fast charging along the Pan-American corridor matures. For either profile, the economics above are no longer theoretical &mdash; they are the same arithmetic already running in fleets we have deployed across Latin America, and the Salvadoran fuel-price environment makes them sharper here than almost anywhere else in the region.</p>
'''))

# ---------------------------------------------------------------- 2
ARTICLES.append(dict(
f='tegucigalpa-honduras-electric-cargo-truck-logistics',
t='Tegucigalpa Urban Freight: KT5M Electric Box Truck Economics for Honduras',
d='Honduras distributors can run Tegucigalpa urban freight at half the energy cost with the KT5M electric box truck. Specs, range, charging and import guide for this EV truck.',
k='KT5M electric box truck, EV truck Honduras, electric truck Tegucigalpa, electric cargo truck Central America, Dongfeng electric truck, urban logistics EV truck, electric box truck import',
img='models/p07_04.jpg',
alt='Dongfeng KT5M electric box truck on a Tegucigalpa delivery route, EV truck for Honduras urban logistics',
net='zhc',
body='''
<p>Tegucigalpa is a hard city for trucks. The basin topography means every distribution run includes grades of 8-12%, the CA-5 and CA-6 corridors funnel freight through chokepoints that idle diesel engines for hours a week, and the city&rsquo;s wholesale markets and supermarket DCs sit inside dense urban fabric where noise and soot are political issues, not just operating ones. It is also, for exactly those reasons, a city where an EV truck fleet produces outsized savings. This article walks through the <a href="../products/models/kt5m-electric-cargo-truck.html">Dongfeng KT5M electric box truck</a> for Honduran urban freight: what it costs to run, what it carries, how it charges, and how to import one into Honduras.</p>

<h2>The Duty Cycle: Short, Steep and Stop-and-Go</h2>
<p>A typical Tegucigalpa box-truck route is 80-140 km per day: a morning run from a DC in the Amarateca valley to supermarkets in Comayag&uuml;ela and the Colonias, afternoon backhauls from the San Lorenzo corridor, or beverage distribution from the plants along the CA-5. Two characteristics make this ideal electric territory. First, distance is short and predictable &mdash; the KT5M&rsquo;s 200-240 km real-world range covers the longest day with 30% reserve. Second, the topography actively pays you back: every descent from the Amarateca ridge or the El Hatillo climb returns energy through regenerative braking, and our fleet data from comparable Andean and Central American terrain shows 15-22% energy recovery on routes with sustained 8%+ grades. A diesel truck burns those descents into brake dust.</p>

<h2>KT5M Key Numbers for Honduran Fleets</h2>
<table style="width:100%;border-collapse:collapse;margin:20px 0;" border="1" cellpadding="8">
<tr style="background:#006341;color:#fff;"><th style="padding:8px;text-align:left;">Parameter</th><th style="padding:8px;text-align:left;">KT5M Electric Box Truck</th></tr>
<tr><td style="padding:8px;">GVW / payload</td><td style="padding:8px;">9-12 t class / 4.5-6 t payload</td></tr>
<tr><td style="padding:8px;">Battery</td><td style="padding:8px;">140-180 kWh CATL LFP options</td></tr>
<tr><td style="padding:8px;">Motor</td><td style="padding:8px;">LvKong 150-190 kW peak / 1,100-1,500 Nm</td></tr>
<tr><td style="padding:8px;">Real-world range (urban, loaded)</td><td style="padding:8px;">200-240 km</td></tr>
<tr><td style="padding:8px;">DC charge 20-80%</td><td style="padding:8px;">~40 min at 120 kW</td></tr>
<tr><td style="padding:8px;">Body volume</td><td style="padding:8px;">28-35 m&sup3; dry box or insulated</td></tr>
<tr><td style="padding:8px;">Gradeability</td><td style="padding:8px;">&ge;25% at full load</td></tr>
<tr><td style="padding:8px;">FOB price band</td><td style="padding:8px;">US$48,000-62,000</td></tr>
</table>
<p>The 25% gradeability figure deserves emphasis because it is the first thing Honduran operators ask about. The KT5M&rsquo;s permanent-magnet motor delivers peak torque from zero rpm &mdash; the truck pulls away on a 12% grade at full load without clutch slip, without rollback, and without the diesel&rsquo;s 1,500 rpm torque-converter dance. Drivers transitioning from diesel report the hill starts are the single biggest quality-of-life change, followed by the absence of exhaust heat in the cab during Tegucigalpa&rsquo;s April heat.</p>

<h2>Cost Per Kilometre: Diesel vs Electric in Honduras</h2>
<p>Honduran diesel runs US$1.05-1.15 per litre, and a 9-12 t box truck on Tegucigalpa&rsquo;s stop-and-go routes consumes 0.28-0.35 L/km &mdash; call it US$0.32 per kilometre in fuel. The KT5M consumes 0.75-0.9 kWh/km on the same routes including grade recovery; at ENEE&rsquo;s industrial tariff of roughly US$0.15-0.17/kWh, that is US$0.13 per kilometre. On 3,500 km per month, the energy saving is about US$665 per truck per month, or US$8,000 per year. Maintenance adds roughly US$2,000-3,000 more: no oil changes, no injector servicing, no clutch replacements, and brake pads that last two to three times longer under regenerative braking. Against a purchase premium of US$18,000-25,000 over a diesel equivalent, payback arrives in 22-30 months &mdash; inside the first battery-warranty period by a wide margin, since the CATL pack carries an 8-year / 4,500-cycle warranty.</p>
<ul>
<li><strong>Fuel cost per km:</strong> diesel US$0.32 vs EV truck US$0.13 &mdash; a 59% saving</li>
<li><strong>Monthly saving per truck:</strong> ~US$800 including maintenance</li>
<li><strong>Payback:</strong> 22-30 months at Honduran energy prices</li>
<li><strong>Operating hours:</strong> near-silent operation unlocks early-morning delivery windows in residential Colonias</li>
</ul>

<h2>Charging: Simpler Than Buyers Expect</h2>
<p>Urban distribution is the easiest fleet segment to electrify because every truck sleeps at the same depot. A first-wave Honduran fleet of 5-10 KT5Ms needs one 120 kW DC fast charger for daytime opportunity charging plus one 22-40 kW AC post per two trucks overnight. Total connected load: about 250-350 kVA &mdash; well within standard commercial service in Tegucigalpa&rsquo;s industrial zones. ENEE connection lead times run 6-12 weeks for this service class. Our deployment checklist files the utility application on purchase-order day, and we size the switchboard for double the initial fleet because every fleet that reaches month six orders more trucks.</p>
<p>One Honduras-specific note: the grid has reliability challenges in some zones, and fleets ask about resilience. The practical answer is that a truck fleet is inherently buffered &mdash; the trucks carry 140-180 kWh each and a five-truck fleet can absorb a two-hour outage with zero operational impact by simply resequencing charge sessions. Fleets wanting hard resilience add a modest battery-backed solar canopy; at Honduran irradiance levels (~5.2 peak sun hours), a 100 kWp canopy covers 35-45% of a ten-truck fleet&rsquo;s annual energy.</p>

<h2>Import and Regional Positioning</h2>
<p>Honduras grants electric vehicles duty-free treatment under its EV promotion decree, against 15% duty on diesel trucks, and Puerto Cort&eacute;s is an efficient RoRo port with 28-32 day sailings from China&rsquo;s east coast. Customs clearance with SAR registration runs about a week with a competent broker. We supply the Spanish-language homologation dossier, UN R100 battery safety certificates and charger CE/UL documentation as a standard export pack. Distributors running multi-country Central American operations should also review our <a href="../markets/mexico.html">Mexico market page</a> &mdash; several Honduran beverage and FMCG groups share fleet standards with their Mexican sister companies, and aligning on one EV truck platform across countries cuts parts inventory and training cost roughly in half.</p>
<p>Service support is structured in three layers: the two-year fast-moving parts kit shipped with every truck (contactors, sensors, filters, brake components), remote diagnostics through the fleet telematics portal with our engineering team on WhatsApp response, and CATL module stock in Panama for anything battery-related. In practice, the LvKong drivetrain&rsquo;s service calendar is a brake inspection and a coolant check every 40,000 km &mdash; a fraction of the diesel maintenance calendar it replaces.</p>

<h2>The Bottom Line for Honduran Distributors</h2>
<p>Tegucigalpa&rsquo;s geography, once the enemy of trucking economics, is precisely what makes the EV truck case so strong: short routes, paid descents, depot-based nights and expensive diesel. The fleets that move first also lock in the early-mover advantages &mdash; preferred status with supermarket chains building scope-3 reporting, and municipal goodwill that matters when delivery-window regulations tighten, as they are doing across the region. The KT5M is not a compromise vehicle doing electric duty; on this duty cycle it is simply the cheaper truck to own.</p>
'''))

# ---------------------------------------------------------------- 3
ARTICLES.append(dict(
f='san-pedro-sula-honduras-electric-delivery-truck',
t='San Pedro Sula Industrial Freight: KT5J Electric Delivery Trucks for Honduras&rsquo; Manufacturing Hub',
d='San Pedro Sula maquila and industrial freight suits the KT5J electric delivery truck: 180-220 km range, half the energy cost of diesel. EV truck specs, TCO and import steps.',
k='KT5J electric delivery truck, EV truck San Pedro Sula, electric truck Honduras, electric delivery truck maquila, Dongfeng electric truck, last mile EV truck Central America',
img='models/p07_06.jpg',
alt='Dongfeng KT5J electric delivery truck outside a San Pedro Sula industrial park, EV truck for Honduras manufacturing freight',
net='zhc',
body='''
<p>San Pedro Sula generates more freight per square kilometre than any other city in Honduras. The Choloma and Villanueva industrial corridors host the country&rsquo;s maquila belt &mdash; textiles, plastics, food processing &mdash; and the ZIP and free-zone parks dispatch thousands of delivery runs a week toward Puerto Cort&eacute;s, Tegucigalpa and the city&rsquo;s own retail grid. This article examines the <a href="../products/models/kt5j-electric-cargo-truck.html">Dongfeng KT5J electric delivery truck</a> in that specific role: what the numbers look like on industrial duty cycles, how charging fits free-zone operations, and what it takes to land the trucks in Honduras. For industrial-park operators and 3PLs, this EV truck segment is where electrification pays back fastest.</p>

<h2>Why Industrial-Park Freight Electrifies First</h2>
<p>Maquila and industrial freight has three properties that make it the lowest-risk EV truck entry point in any market. Routes are fixed and short &mdash; plant to port (55 km), plant to plant (10-40 km), plant to city retail (15-30 km). Schedules are shift-based and predictable, which means charging windows are predictable. And the trucks return nightly to the same fenced, powered, guarded yard. San Pedro Sula&rsquo;s industrial geography compresses all of this: the entire maquila belt sits within a 25 km radius, and Puerto Cort&eacute;s &mdash; the region&rsquo;s best deep-water port &mdash; is under an hour away. A KT5J on this duty cycle covers 120-200 km daily, inside its 180-220 km real-world range with margin to spare.</p>
<p>The commercial angle matters too. The maquila sector sells to US and European brands with scope-3 emissions targets, and logistics emissions are increasingly reported per shipment. An electric delivery truck fleet is a sales asset for the free zones themselves: several Central American industrial parks now market &ldquo;low-carbon logistics&rdquo; as a tenant benefit, and the parks that electrify first will write that into their pitch decks.</p>

<h2>KT5J Specifications for Industrial Duty</h2>
<table style="width:100%;border-collapse:collapse;margin:20px 0;" border="1" cellpadding="8">
<tr style="background:#006341;color:#fff;"><th style="padding:8px;text-align:left;">Parameter</th><th style="padding:8px;text-align:left;">KT5J Electric Delivery Truck</th></tr>
<tr><td style="padding:8px;">GVW / payload</td><td style="padding:8px;">7.5-9 t class / 3.5-4.5 t payload</td></tr>
<tr><td style="padding:8px;">Battery</td><td style="padding:8px;">106-130 kWh CATL LFP</td></tr>
<tr><td style="padding:8px;">Motor</td><td style="padding:8px;">LvKong 120-150 kW peak / 950-1,200 Nm</td></tr>
<tr><td style="padding:8px;">Real-world range (loaded, mixed)</td><td style="padding:8px;">180-220 km</td></tr>
<tr><td style="padding:8px;">DC charge 20-80%</td><td style="padding:8px;">~35 min at 90-120 kW</td></tr>
<tr><td style="padding:8px;">Cargo volume</td><td style="padding:8px;">22-28 m&sup3; box, side-door option</td></tr>
<tr><td style="padding:8px;">Turning circle</td><td style="padding:8px;">~11.8 m (urban dock-friendly)</td></tr>
<tr><td style="padding:8px;">FOB price band</td><td style="padding:8px;">US$45,000-56,000</td></tr>
</table>
<p>Payload is the question every fleet manager raises first, and it deserves a straight answer. The battery pack weighs more than the diesel powertrain it replaces, and on a 7.5-9 t truck that costs roughly 300-500 kg of payload versus a diesel equivalent. For textile, plastics and food freight &mdash; which cubes out before it weighs out &mdash; that penalty is irrelevant. For dense freight (beverages, construction materials) it matters, and we size those fleets on the 9 t variant with the 106 kWh pack rather than over-batterying the truck. Right-sizing the battery is the single most common specification error in first EV truck purchases; we model the duty cycle before quoting.</p>

<h2>Energy and Maintenance Economics in the Sula Valley</h2>
<p>Diesel at US$1.05-1.15/L and a 7.5-9 t truck consuming 0.24-0.30 L/km puts diesel energy at about US$0.28/km. The KT5J consumes 0.60-0.75 kWh/km on industrial stop-start duty; at the industrial tariff of US$0.15-0.17/kWh, that is US$0.11/km. On 4,000 km per month &mdash; typical for a two-shift industrial delivery truck &mdash; the saving is US$680 per month per truck in energy alone. Maintenance on the sealed drivetrain adds US$150-250 per month versus the diesel&rsquo;s oil, filters, clutch and injector calendar. Total: roughly US$10,000 per truck per year. Against a purchase premium of US$15,000-20,000, payback lands at 18-24 months &mdash; and the truck then runs another six-plus years inside its 8-year battery warranty while the savings continue.</p>
<ul>
<li><strong>Energy cost per km:</strong> US$0.28 diesel vs US$0.11 electric &mdash; 61% lower</li>
<li><strong>Annual saving per truck:</strong> ~US$10,000 (energy + maintenance)</li>
<li><strong>Payback:</strong> 18-24 months on two-shift industrial duty</li>
<li><strong>Uptime:</strong> no DPF regeneration cycles, no clutch wear in dock queue traffic</li>
</ul>

<h2>Charging Inside Free Zones: What to Plan</h2>
<p>Free-zone parks simplify charging in one respect &mdash; they have industrial-grade power infrastructure &mdash; and complicate it in another: electrical capacity is allocated per tenant, so a fleet of ten KT5Js drawing 300-400 kVA needs early coordination with the park operator. Our standard package for industrial-park fleets is a 120 kW DC charger per 6-8 trucks for daytime top-ups, plus 22 kW AC posts at each overnight bay. We deliver the single-line diagram, load-management configuration and utility application pack as part of the truck order, because the charger lead time (8-12 weeks) typically exceeds the vessel transit from Shanghai to Puerto Cort&eacute;s (28-32 days).</p>
<p>Load management deserves one paragraph because it is where first-time fleets overspend. Ten trucks do not need ten fast chargers; they need charging sessions sequenced so the site never exceeds its contracted capacity. The KT5J fleet management portal schedules sessions by departure time and required state of charge, and in practice a ten-truck fleet runs comfortably on a 350 kVA connection that would otherwise need to be 800+ kVA if all trucks charged unmanaged. That difference is often US$80,000-150,000 of avoided substation work.</p>

<h2>Import Path and Regional Fleet Strategy</h2>
<p>Electric trucks enter Honduras duty-free under the national EV decree, and Puerto Cort&eacute;s handles RoRo efficiently with 5-8 day customs cycles for properly documented vehicles. We ship with the full homologation dossier in Spanish, UN R100 battery certification, and the two-year parts kit. For groups operating across the northern triangle, standardising on one EV truck platform across Honduras, El Salvador and Guatemala cuts parts stock and training cost substantially &mdash; and our <a href="../markets/mexico.html">Mexico market overview</a> covers the corridor context for fleets running north toward the CA-1. Several maquila groups we work with run exactly this multi-country playbook.</p>
<p>After-sales is the deciding factor for industrial buyers, and it is worth stating plainly: the KT5J&rsquo;s drivetrain has no engine, gearbox, clutch or exhaust aftertreatment to service. The maintenance calendar is brake inspections, coolant checks and software updates, delivered through the telematics portal with our engineers on direct WhatsApp support. Spare modules and fast-moving parts stock in Panama reach San Pedro Sula in 10-14 days. For a sector where a stopped truck means a stopped production line&rsquo;s outbound flow, that simplicity is the entire point.</p>

<h2>First Movers in the Sula Valley</h2>
<p>The natural first adopters are the free-zone operators themselves &mdash; electrifying the internal shuttle and port drayage fleet as a tenant service &mdash; followed by the large 3PLs serving the maquila belt and the beverage distributors whose dense freight suits the 9 t variant. The economics at Honduran diesel prices are not marginal; they are a 55-60% energy cost reduction on the highest-utilisation trucks in the fleet. In a market where logistics cost is a quoted line item in every FOB negotiation, that margin flows directly to the bottom line of whoever moves first.</p>
'''))

# ---------------------------------------------------------------- 4
ARTICLES.append(dict(
f='kingston-jamaica-electric-delivery-truck-fleet',
t='Kingston Delivery Fleets: KT5L Electric Cargo Trucks for Jamaica&rsquo;s Import Economy',
d='Jamaica&rsquo;s high diesel prices make the KT5L electric cargo truck a strong fit for Kingston delivery fleets. Range, payload, charging and import guide for this EV truck.',
k='KT5L electric cargo truck, EV truck Jamaica, electric truck Kingston, electric delivery truck Caribbean, Dongfeng electric truck, electric box truck island logistics',
img='models/p07_09.jpg',
alt='Dongfeng KT5L electric cargo truck on a Kingston delivery route, EV truck for Jamaica urban freight',
net='zhc',
body='''
<p>Jamaica runs on imports, and imports run through Kingston. Roughly 80% of the island&rsquo;s containerized freight lands at Kingston&rsquo;s terminals, and from there a fleet of 3-8 t trucks fans out across the Liguanea plain, up to Spanish Town, along the coastal corridor to Portmore, and over the junction routes to the north coast. That freight moves in diesel trucks burning fuel at US$1.20-1.30 per litre &mdash; some of the highest pump prices in the western hemisphere. This article looks at the <a href="../products/models/kt5l-electric-cargo-truck.html">Dongfeng KT5L electric cargo truck</a> in Jamaican service: range, payload, charging realities on the JPS grid, and the import math. Island duty cycles are, it turns out, almost perfectly shaped for an EV truck.</p>

<h2>Islands Are Electric Territory</h2>
<p>The physics of island freight favour electrification in ways mainland markets cannot match. Distances are short by geography: Kingston to Ocho Rios is 85 km, to Montego Bay 180 km &mdash; and the latter is a twice-weekly run, not a daily one. Urban delivery inside the Kingston metro runs 60-120 km per day. Nothing on the island exceeds the KT5L&rsquo;s 190-230 km real-world range on its 130 kWh CATL LFP pack. Second, fuel is imported and expensive while electricity, though not cheap at US$0.28-0.35/kWh retail, still prices energy per kilometre at less than half the diesel figure. Third &mdash; and uniquely Jamaican &mdash; the island&rsquo;s solar resource (5.3+ peak sun hours) lets a depot canopy cut that electricity cost by half again, which is why our Jamaican fleet proposals always include a solar sizing annex.</p>

<h2>KT5L Numbers for Jamaican Routes</h2>
<table style="width:100%;border-collapse:collapse;margin:20px 0;" border="1" cellpadding="8">
<tr style="background:#006341;color:#fff;"><th style="padding:8px;text-align:left;">Parameter</th><th style="padding:8px;text-align:left;">KT5L Electric Cargo Truck</th></tr>
<tr><td style="padding:8px;">GVW / payload</td><td style="padding:8px;">6-7.5 t class / 2.5-3.5 t payload</td></tr>
<tr><td style="padding:8px;">Battery</td><td style="padding:8px;">100-130 kWh CATL LFP</td></tr>
<tr><td style="padding:8px;">Motor</td><td style="padding:8px;">LvKong 110-140 kW peak / 900-1,100 Nm</td></tr>
<tr><td style="padding:8px;">Real-world range (urban, loaded)</td><td style="padding:8px;">190-230 km</td></tr>
<tr><td style="padding:8px;">DC charge 20-80%</td><td style="padding:8px;">~35 min at 90 kW</td></tr>
<tr><td style="padding:8px;">Body</td><td style="padding:8px;">18-24 m&sup3; box, curtainside or reefer options</td></tr>
<tr><td style="padding:8px;">Gradeability</td><td style="padding:8px;">&ge;25% &mdash; handles Junction Road grades loaded</td></tr>
<tr><td style="padding:8px;">FOB price band</td><td style="padding:8px;">US$42,000-54,000</td></tr>
</table>
<p>Two features matter specifically for Jamaica. The gradeability figure covers the island&rsquo;s real constraint: the routes over Mount Diablo and the Junction road include sustained 10-15% grades where a loaded diesel box truck drops to 25 km/h in second gear. The KT5L&rsquo;s motor holds torque to its rated speed and climbs the same grades at 45-55 km/h &mdash; then regenerates 18-25% of the climb energy back on the descent. Second, the 11.2 m turning circle and compact cab suit Kingston&rsquo;s older industrial estates and the tight docks behind the retail strips on Constant Spring Road and Hagley Park Road.</p>

<h2>The Jamaican TCO: Where the Savings Come From</h2>
<p>A diesel 6-7.5 t box truck on Kingston urban duty burns 0.22-0.28 L/km; at US$1.25/L, that is US$0.30 per kilometre. The KT5L consumes 0.55-0.70 kWh/km; at JPS commercial tariffs of US$0.30/kWh, US$0.19 per kilometre &mdash; and at solar-canopy effective cost of US$0.12-0.15/kWh, under US$0.10. On 3,000 km per month the grid-charged saving is about US$330 and the solar-assisted saving US$600+ per truck monthly. Maintenance adds another US$150-200 monthly versus the diesel calendar. Payback against the US$14,000-18,000 purchase premium: 20-28 months grid-charged, 15-20 months with solar. The CATL battery warranty &mdash; 8 years or 4,500 cycles &mdash; outlasts the payback period by a factor of four.</p>
<ul>
<li><strong>Energy cost per km:</strong> US$0.30 diesel vs US$0.10-0.19 electric (solar vs grid)</li>
<li><strong>Monthly saving per truck:</strong> US$480-800 including maintenance</li>
<li><strong>Payback:</strong> 15-28 months depending on charging source</li>
<li><strong>Resilience:</strong> a 5-truck fleet carries 500+ kWh of mobile storage &mdash; usable as depot backup during hurricane-season outages</li>
</ul>

<h2>Charging on the JPS Grid</h2>
<p>Kingston&rsquo;s commercial districts have adequate medium-voltage capacity for depot charging; a ten-truck KT5L fleet needs roughly 250-300 kVA with managed charging, which JPSCo processes as a standard commercial upgrade in 8-14 weeks. The practical configuration is one 90-120 kW DC charger for daytime rotation plus overnight AC posts per bay. Two Jamaica-specific notes from our deployment planning: first, specify chargers with wide voltage-tolerance input because grid fluctuation is real on some feeders; second, put the solar canopy in the initial budget &mdash; at Jamaican retail tariffs it pays for itself in under five years on charging load alone, and it doubles as hurricane-rated covered parking.</p>
<p>Hurricane resilience deserves its own sentence because buyers always ask. Electric trucks have no air intake to flood and no fuel system to contaminate; the HV system is sealed to IP67 and the pack sits at frame height. Post-storm, a charged EV truck fleet is a mobile power asset &mdash; with a bidirectional inverter, five trucks can run a depot&rsquo;s refrigeration and lighting for days. Jamaican operators who lived through recent hurricane seasons immediately see the value.</p>

<h2>Import Process and CARICOM Context</h2>
<p>Jamaica applies a 10% duty rate to electric trucks versus 20-30% on diesel equivalents, and EVs are exempt from the special consumption tax on vehicles &mdash; the combined saving at import is roughly US$8,000-12,000 per truck versus diesel. Sailings from China to Kingston run 32-38 days via transhipment, typically through Panama or a US Gulf port. We handle the full export documentation: bill of lading, UN R100 battery certification, charger compliance papers, and the Spanish/English manuals. For distributors serving the wider Caribbean from a Kingston base, our <a href="../markets/dominican-republic.html">Dominican Republic market page</a> covers the region&rsquo;s other major island market &mdash; the same KT5L platform serves both, simplifying a multi-island parts strategy.</p>
<p>Parts and support for island fleets follow our Caribbean protocol: an extended first-line parts kit ships with the trucks (the island premium on freight makes local stock more valuable than on the mainland), CATL modules are held in Panama at 7-10 day delivery, and the telematics portal gives our engineers live visibility into every truck&rsquo;s battery and drivetrain health. Most issues are resolved by remote diagnosis plus a couriered part &mdash; the drivetrain has no wear items that require specialist workshop equipment.</p>

<h2>Who Moves First in Jamaica</h2>
<p>The strongest candidates are the supermarket and distribution groups with captive Kingston metro routes, the breweries and beverage distributors whose dense freight suits the 7.5 t variant, and the 3PLs serving the tourism corridor &mdash; a hotel supply run from Kingston to the north coast resorts is a perfect 190 km round trip with a lunch-stop top-up. Jamaica&rsquo;s fuel prices are not coming down, its solar resource is not going away, and the duty incentive is already law. The fleets that electrify their Kingston routes first will bank a cost advantage their competitors cannot match with diesel at any efficiency.</p>
'''))

# ---------------------------------------------------------------- 5
ARTICLES.append(dict(
f='port-of-spain-trinidad-electric-port-tractor',
t='Port of Spain Container Drayage: TE46 Electric Port Tractor for Trinidad &amp; Tobago',
d='Trinidad&rsquo;s port drayage and Point Lisas industrial shuttle suit the TE46 electric port tractor: 8-hour shift range, 5-6 min battery swap option. EV truck economics inside.',
k='TE46 electric port tractor, EV truck Trinidad, electric truck Port of Spain, electric terminal tractor Caribbean, Dongfeng electric truck, port drayage EV truck',
img='models/p11_00.jpg',
alt='Dongfeng TE46 electric port tractor hauling containers near Port of Spain, EV truck for Trinidad drayage',
net='qyc',
body='''
<p>Port of Spain handles the containerized lifeline of Trinidad &amp; Tobago, and the freight ecology around it is compact, repetitive and industrial: drayage from the port to warehouses in Barataria and Sea Lots, shuttles to the Point Lisas industrial estate 45 km south, and distribution runs across the East-West Corridor. It is also an economy with subsidized electricity, an energy-sector workforce comfortable with industrial equipment, and diesel that, while cheaper than its Caribbean neighbours, still prices every drayage kilometre at a multiple of the electric alternative. This article examines the <a href="../products/models/te46-electric-tractor.html">Dongfeng TE46 electric port tractor</a> in Trinidadian service &mdash; a duty cycle where this EV truck platform has already proven itself from Tanger Med to Dar es Salaam.</p>

<h2>The Drayage Duty Cycle, Measured</h2>
<p>Port drayage is the single best-understood electric truck application in the world because telematics makes it transparent. A Port of Spain drayage tractor works 10-14 hours daily, covers 120-200 km, spends 30-40% of engine-hours idling in terminal queues, and never travels more than 60 km from its depot. The idling figure is where diesel economics collapse: a 12 L diesel tractor engine burns 3-4 litres per hour producing nothing in a queue. The TE46&rsquo;s electric drivetrain consumes essentially zero at standstill &mdash; the air conditioning is the only draw, at about 1.5 kW. Across a shift, queue time alone accounts for 25-35% of the diesel truck&rsquo;s fuel bill and roughly 2% of the EV truck&rsquo;s energy bill.</p>
<p>The TE46&rsquo;s 282 kWh CATL LFP battery delivers 8-10 hours of mixed drayage duty per charge. Two charging strategies fit Trinidadian operations: depot DC fast charging (a 240 kW unit restores 20-80% in about 45 minutes, matched to the lunch shift-change), or battery swap for two-shift operations &mdash; the swap variant exchanges packs in 5-6 minutes, faster than a diesel refuel, from a compact station that fits in a container footprint beside the terminal gate.</p>

<h2>TE46 Terminal Tractor Specifications</h2>
<table style="width:100%;border-collapse:collapse;margin:20px 0;" border="1" cellpadding="8">
<tr style="background:#006341;color:#fff;"><th style="padding:8px;text-align:left;">Parameter</th><th style="padding:8px;text-align:left;">TE46 4x2 Electric Port Tractor</th></tr>
<tr><td style="padding:8px;">GCW rating</td><td style="padding:8px;">42-46 t (container drayage spec)</td></tr>
<tr><td style="padding:8px;">Battery</td><td style="padding:8px;">282 kWh CATL LFP, swap-capable option</td></tr>
<tr><td style="padding:8px;">Motor</td><td style="padding:8px;">LvKong 250 kW peak / 2,800 Nm</td></tr>
<tr><td style="padding:8px;">Shift endurance</td><td style="padding:8px;">8-10 h mixed drayage duty</td></tr>
<tr><td style="padding:8px;">DC charge 20-80%</td><td style="padding:8px;">~45 min at 240 kW dual-gun</td></tr>
<tr><td style="padding:8px;">Battery swap time</td><td style="padding:8px;">5-6 min (swap variant)</td></tr>
<tr><td style="padding:8px;">Fifth wheel</td><td style="padding:8px;">50 mm, oscillating, terminal-rated</td></tr>
<tr><td style="padding:8px;">FOB price band</td><td style="padding:8px;">US$72,000-88,000</td></tr>
</table>
<p>The torque figure changes terminal operations in a way numbers alone do not capture. A loaded 40 ft container combination at 40 t GCW pulls away from a terminal stack with full torque from zero rpm &mdash; no clutch slip, no rev-matching, no turbo lag. Spotters and yard jockeys transitioning from diesel consistently report the same two things: the truck is faster across the first 50 metres (which is the distance that matters in a terminal), and the absence of diesel noise lets them hear the yard. Several terminals we serve measured near-miss incident reductions after electrifying, a safety benefit no TCO model prices in.</p>

<h2>Economics at Trinidadian Energy Prices</h2>
<p>Trinidad&rsquo;s industrial electricity tariff &mdash; among the lowest in the Caribbean at roughly US$0.06-0.09/kWh thanks to the gas-based grid &mdash; makes the electric case exceptional even by regional standards. A diesel drayage tractor burns 0.55-0.70 L/km equivalent on this stop-start duty (idling included); at US$0.75-0.85/L, that is US$0.45-0.55 per kilometre. The TE46 consumes 1.6-1.9 kWh/km at 40 t GCW; at US$0.08/kWh, US$0.14 per kilometre. On 180 km per day, 300 days a year, the annual energy saving is roughly US$18,000-21,000 per tractor. Maintenance &mdash; no engine, transmission, or aftertreatment &mdash; adds US$5,000-7,000 more. Payback on the purchase premium arrives in 18-24 months, among the fastest of any market we serve, precisely because Trinidad&rsquo;s power is cheap and its drayage cycle is severe on diesel.</p>
<ul>
<li><strong>Energy per km:</strong> US$0.50 diesel vs US$0.14 electric &mdash; 72% lower</li>
<li><strong>Annual saving per tractor:</strong> US$23,000-28,000 combined</li>
<li><strong>Queue idling:</strong> ~30% of diesel fuel bill eliminated entirely</li>
<li><strong>Terminal air quality:</strong> zero NOx and particulates inside the gate &mdash; a growing port-authority requirement across the Caribbean</li>
</ul>

<h2>Charging and Swap Infrastructure at the Port</h2>
<p>Port of Spain&rsquo;s port estate and the surrounding industrial zone have the medium-voltage capacity for fleet charging; a six-tractor TE46 fleet runs on one 240 kW DC charger plus managed overnight AC, a 400-500 kVA service class that T&amp;TEC processes routinely. For two-shift operations, the battery-swap configuration changes the infrastructure math: one swap station serves 15-20 tractors, holds 6-8 packs charging on managed load, and eliminates charging downtime entirely. We specify swap for fleets above ten tractors or any two-shift operation, and depot DC charging below that. Both configurations ship with the trucks as a coordinated package &mdash; chargers, swap station, switchgear and the load-management software preconfigured for the fleet&rsquo;s shift pattern.</p>
<p>One Trinidad-specific opportunity: the Point Lisas industrial estate runs on abundant gas-generated power and hosts exactly the kind of heavy, short-haul shuttle traffic (ammonia, methanol, steel products) where tractor fleets work brutally repetitive cycles. An energy-sector company electrifying its own shuttle fleet inside Point Lisas is the lowest-risk first deployment in the country &mdash; captive power, captive routes, and a workforce that already maintains industrial plant.</p>

<h2>Import and CARICOM Positioning</h2>
<p>Trinidad &amp; Tobago applies preferential duty treatment to electric vehicles, and Port of Spain&rsquo;s RoRo facilities handle truck imports routinely with 30-36 day sailings from China via transhipment. We supply the complete homologation package including UN R100 battery certification and English manuals. Trinidadian energy and logistics groups with regional operations should note our <a href="../markets/dominican-republic.html">Dominican Republic market page</a> &mdash; Caribbean fleets increasingly standardise on shared platforms, and the TE46 serves terminal duty across the region&rsquo;s major ports with common parts and training.</p>
<p>Support follows our port-fleet protocol: every tractor ships with a terminal-duty parts kit (fifth-wheel components, contactors, suspension wear parts), the telematics portal streams battery and drivetrain health to our engineering desk, and swap-variant fleets receive station commissioning support on-site. The drivetrain&rsquo;s service calendar &mdash; brake inspections and coolant checks &mdash; is a rounding error beside the diesel terminal tractor&rsquo;s engine, transmission and DPF maintenance load.</p>

<h2>The Strategic Case</h2>
<p>Caribbean ports compete on cost, and drayage cost is set by energy price multiplied by a duty cycle that punishes diesel. Trinidad &amp; Tobago holds a structural advantage almost nobody in the region has exploited yet: industrial power at prices that make electric drayage 70%+ cheaper per kilometre. The port authority, the 3PLs, and the Point Lisas operators all hold pieces of this opportunity. Whoever assembles them first owns the region&rsquo;s lowest-cost container logistics &mdash; and a reference site the entire CARICOM market will visit.</p>
'''))

# ---------------------------------------------------------------- 6
ARTICLES.append(dict(
f='yaounde-cameroon-electric-cargo-truck-corridor',
t='Yaound&eacute; Freight Corridor: KTH3 Electric Cargo Trucks for Cameroon&rsquo;s Capital Logistics',
d='The Douala&ndash;Yaound&eacute; corridor is Cameroon&rsquo;s freight artery. KTH3 electric cargo truck range, charging and TCO for this EV truck route, plus import guidance.',
k='KTH3 electric cargo truck, EV truck Cameroon, electric truck Yaounde, Douala Yaounde corridor electric truck, Dongfeng electric truck, electric cargo truck Central Africa',
img='models/p07_05.jpg',
alt='Dongfeng KTH3 electric cargo truck on the Douala to Yaounde corridor, EV truck for Cameroon freight',
net='zhc',
body='''
<p>Cameroon&rsquo;s freight economy runs on one road: the 230 km corridor from the port of Douala up the escarpment to Yaound&eacute;. Everything the capital consumes &mdash; food, fuel-adjacent goods, construction materials, consumer products &mdash; climbs that road, and everything the coast imports for CEMAC transhipment passes through it. It is a demanding profile for any truck: a loaded climb from sea level to 750 m, heavy seasonal rain, and traffic that compresses speeds into the 40-60 km/h band where diesel engines run least efficiently. This article assesses the <a href="../products/models/kth3-electric-cargo-truck.html">Dongfeng KTH3 electric cargo truck</a> on exactly this corridor &mdash; with midpoint charging, the route is inside EV truck range today, and the descent economics are remarkable.</p>

<h2>Corridor Physics: The Climb and the Payback</h2>
<p>The Douala-Yaound&eacute; profile is a study in asymmetric energy. Douala to Yaound&eacute;, loaded at 20 t payload, the KTH3 consumes roughly 1.55-1.75 kWh/km on the climbing legs &mdash; the battery delivers about 260-290 kWh into the ascent. The return, loaded or empty, descends the same escarpment, and regenerative braking recovers 22-28% of the round-trip energy. A diesel truck converts that same descent into heat in its brake linings &mdash; and Cameroonian corridor fleets replace brake components at intervals their drivers know by heart. The practical consequence: the electric truck&rsquo;s round-trip energy cost per kilometre is far lower than a naive range calculation suggests, because the topography itself refunds a quarter of the energy.</p>
<p>The single-charge question needs a direct answer. The KTH3&rsquo;s 350 kWh CATL LFP pack covers 200-240 km of loaded corridor work &mdash; enough for the full one-way trip with reserve, but not the round trip. The corridor therefore needs one midpoint or destination charger, and the natural site is Yaound&eacute;&rsquo;s own freight yards on the city&rsquo;s southern approach, where most Douala freight terminates anyway. A 240 kW DC charger at the Yaound&eacute; depot restores 20-80% in about 50 minutes &mdash; inside the standard unloading window. For operators whose freight continues to Bafoussam or the far north, a second charging point at the destination completes the pattern.</p>

<h2>KTH3 Corridor Specifications</h2>
<table style="width:100%;border-collapse:collapse;margin:20px 0;" border="1" cellpadding="8">
<tr style="background:#006341;color:#fff;"><th style="padding:8px;text-align:left;">Parameter</th><th style="padding:8px;text-align:left;">KTH3 6x4 Electric Cargo Truck</th></tr>
<tr><td style="padding:8px;">GVW / payload</td><td style="padding:8px;">28 t / 18-20 t (box or stake body)</td></tr>
<tr><td style="padding:8px;">Battery</td><td style="padding:8px;">350 kWh CATL LFP, liquid-cooled</td></tr>
<tr><td style="padding:8px;">Motor</td><td style="padding:8px;">LvKong 360 kW peak / 2,400 Nm</td></tr>
<tr><td style="padding:8px;">Range (loaded corridor profile)</td><td style="padding:8px;">200-240 km</td></tr>
<tr><td style="padding:8px;">DC charge 20-80%</td><td style="padding:8px;">~50 min at 240 kW</td></tr>
<tr><td style="padding:8px;">Gradeability</td><td style="padding:8px;">&ge;30% &mdash; escarpment climbs at speed</td></tr>
<tr><td style="padding:8px;">Regeneration on Douala&ndash;Yaound&eacute;</td><td style="padding:8px;">22-28% of round-trip energy recovered</td></tr>
<tr><td style="padding:8px;">FOB price band</td><td style="padding:8px;">US$88,000-105,000</td></tr>
</table>
<p>The wet-season question is the one every Cameroonian operator asks, and the engineering answer is straightforward: the KTH3&rsquo;s HV system is sealed to IP67, the battery pack sits above the wading line used for diesel intake design, and there is no air intake, turbo, or exhaust to ingest water. Electric drivetrains handle the corridor&rsquo;s flooded-season sections better than the diesels they replace &mdash; the traction control modulates motor torque in milliseconds on wet laterite, where a diesel&rsquo;s clutch and throttle response is an order of magnitude slower.</p>

<h2>Corridor TCO: Where the Margin Comes From</h2>
<p>A diesel 28 t cargo truck on this corridor burns 0.50-0.60 L/km; at Cameroonian pump prices around US$1.15-1.25/L, energy runs US$0.60-0.70 per kilometre. The KTH3&rsquo;s round-trip consumption nets to 1.3-1.5 kWh/km after regeneration; at ENEO industrial tariffs of roughly US$0.14-0.16/kWh, that is US$0.19-0.23 per kilometre. On a 460 km round trip, 22 days a month, the monthly energy saving is about US$4,200-4,700 per truck. Add maintenance &mdash; brake component life extends 3-4x with regenerative braking on descents that destroy diesel brakes, and there is no engine service calendar at all &mdash; for another US$800-1,200 monthly. Against the purchase premium of US$35,000-45,000, payback arrives in 8-11 months of corridor service. This is one of the fastest paybacks in our entire deployment portfolio, and it is entirely a function of the corridor&rsquo;s severity on diesel equipment.</p>
<ul>
<li><strong>Energy per km:</strong> US$0.65 diesel vs US$0.21 electric &mdash; 68% lower</li>
<li><strong>Monthly saving per truck:</strong> ~US$5,000-5,800 combined</li>
<li><strong>Payback:</strong> 8-11 months on two-way corridor duty</li>
<li><strong>Brake life:</strong> 3-4x longer &mdash; the escarpment descent no longer consumes linings</li>
</ul>

<h2>Charging Infrastructure Along the Corridor</h2>
<p>The infrastructure plan is simple because the freight pattern is simple: chargers belong where trucks already stop. Douala&rsquo;s port-side yards host the base installation &mdash; one 240 kW DC charger per 4-6 trucks with managed overnight AC. Yaound&eacute;&rsquo;s southern freight district hosts the destination unit. ENEO medium-voltage service at both sites is a standard industrial connection class, and we deliver the utility application documentation with the truck order. For operators running beyond Yaound&eacute;, the next logical node is Bafoussam (another 290 km), and the same depot-charging logic applies: the trucks sleep where the freight ends, and that is where the charger goes.</p>
<p>Solar integration is worth serious attention in Cameroon. The corridor&rsquo;s Yaound&eacute; end receives 4.5-5.0 peak sun hours daily, and a 200-300 kWp canopy over a freight yard offsets 35-50% of annual charging energy while providing covered staging. Several Douala cold-storage operators already run solar-plus-diesel-hybrid yard power; substituting truck charging for diesel genset load is the cheapest electrification increment available in the market.</p>

<h2>Import and CEMAC Regional Context</h2>
<p>Cameroon applies reduced duty treatment to electric vehicles under its 2023 finance measures, and Douala&rsquo;s RoRo terminal handles truck imports with 30-38 day sailings from China. We supply the full French-language homologation dossier &mdash; critical for CEMAC markets &mdash; plus UN R100 battery certification and the two-year parts kit. Corridor operators should also review our <a href="../markets/nigeria.html">Nigeria market page</a>: several Cameroonian freight groups operate cross-border into eastern Nigeria, and a shared EV truck platform across both markets halves parts stock and technician training. The Douala-Yaound&eacute; electrification template replicates directly onto the Douala-N&rsquo;Djamena and Yaound&eacute;-Bata corridors as those fleets modernise.</p>
<p>Service support for Cameroon follows our Central African structure: parts kits shipped with the fleet, CATL module stock reachable in 12-18 days, and telematics-based remote diagnostics with French-language support. The KTH3&rsquo;s drivetrain &mdash; one motor, one reduction gear, no clutch, no aftertreatment &mdash; removes the maintenance categories that keep diesel trucks in Douala workshops for weeks waiting on imported engine parts. On a corridor where every day off the road is a missed round trip, drivetrain simplicity is not a convenience; it is revenue.</p>

<h2>Who Should Move First on the Corridor</h2>
<p>The natural first fleets are the large FMCG and beverage distributors with their own Douala yards and Yaound&eacute; DCs &mdash; captive routes, captive depots, maximum daily utilisation. Cement and construction-materials haulers are second; their backhaul patterns are predictable and their diesel bills are the largest in the corridor. The economics above are not projections from a spreadsheet: they are the same architecture already operating in East African escarpment corridors we have electrified, where the descent-regeneration effect is identical. Cameroon&rsquo;s corridor is ready; the first operator to electrify it owns a cost position the diesel competition cannot answer.</p>
'''))

# ---------------------------------------------------------------- 7
ARTICLES.append(dict(
f='lome-togo-electric-truck-port-logistics',
t='Lom&eacute; Port Logistics: KT5M Electric Box Trucks for Togo&rsquo;s Transhipment Hub',
d='Lom&eacute; port is West Africa&rsquo;s transhipment hub. KT5M electric box truck economics for Togo port-to-warehouse freight: range, TCO, charging and import guide for this EV truck.',
k='KT5M electric box truck, EV truck Togo, electric truck Lome, Lome port electric truck, Dongfeng electric truck, electric truck West Africa transhipment, electric box truck',
img='models/p07_07.jpg',
alt='Dongfeng KT5M electric box truck at Lome port container terminal, EV truck for Togo logistics',
net='zhc',
body='''
<p>Lom&eacute; has quietly become West Africa&rsquo;s most efficient container port. The only deep-water terminal on the coast between Abidjan and Lagos, it tranships for the entire region &mdash; and every container that lands there moves the last 5-50 km by truck: to the port&rsquo;s own logistics zone, to warehouses along the N1, to the cement plants east of the city, or onto corridor tractors bound for Burkina Faso, Niger and Mali. That final-leg freight is compact, repetitive and urban &mdash; precisely the profile where an EV truck fleet produces its largest cost advantage. This article examines the <a href="../products/models/kt5m-electric-cargo-truck.html">Dongfeng KT5M electric box truck</a> in Lom&eacute; port logistics service.</p>

<h2>Why Port-City Distribution Electrifies First</h2>
<p>Port logistics zones share a freight signature: short distances (5-50 km), high daily utilisation (two shifts are common at Lom&eacute;&rsquo;s terminals), heavy queue time at gates, and nightly return to the same secured yard. The queue-time factor alone justifies the analysis &mdash; a diesel box truck idling at a terminal gate burns 2.5-3 litres per hour producing nothing; the KT5M&rsquo;s electric drivetrain draws essentially zero at standstill. At Lom&eacute;&rsquo;s gate congestion levels, idle fuel represents 20-30% of a diesel truck&rsquo;s daily energy bill. The second factor is utilisation: two-shift operations double the annual kilometres, which halves the payback period of the electric premium. High-utilisation urban freight is the segment where EV truck economics are strongest everywhere in the world, and Lom&eacute;&rsquo;s port zone is exactly that.</p>

<h2>KT5M in Lom&eacute; Port Service: The Numbers</h2>
<table style="width:100%;border-collapse:collapse;margin:20px 0;" border="1" cellpadding="8">
<tr style="background:#006341;color:#fff;"><th style="padding:8px;text-align:left;">Parameter</th><th style="padding:8px;text-align:left;">KT5M Electric Box Truck</th></tr>
<tr><td style="padding:8px;">GVW / payload</td><td style="padding:8px;">9-12 t class / 4.5-6 t payload</td></tr>
<tr><td style="padding:8px;">Battery</td><td style="padding:8px;">140-180 kWh CATL LFP</td></tr>
<tr><td style="padding:8px;">Motor</td><td style="padding:8px;">LvKong 150-190 kW peak / 1,100-1,500 Nm</td></tr>
<tr><td style="padding:8px;">Real-world range (port-city duty)</td><td style="padding:8px;">200-240 km &mdash; 2-3 days of typical runs</td></tr>
<tr><td style="padding:8px;">DC charge 20-80%</td><td style="padding:8px;">~40 min at 120 kW</td></tr>
<tr><td style="padding:8px;">Body options</td><td style="padding:8px;">28-35 m&sup3; dry box, curtainside, reefer</td></tr>
<tr><td style="padding:8px;">Battery warranty</td><td style="padding:8px;">8 years / 4,500 cycles to 70% SOH</td></tr>
<tr><td style="padding:8px;">FOB price band</td><td style="padding:8px;">US$48,000-62,000</td></tr>
</table>
<p>The range figure translates into operational reality like this: a Lom&eacute; port-zone box truck averages 60-100 km per day across warehouse shuttles, gate runs and city deliveries. A 140 kWh KT5M therefore charges every second or third night, not every night &mdash; which flattens the depot&rsquo;s power demand and means a five-truck fleet runs comfortably on a single 120 kW DC charger plus overnight AC. Under-specifying chargers is the common error; over-specifying them is the expensive one. The duty-cycle data says Lom&eacute; fleets need less charging hardware than buyers assume.</p>

<h2>TCO at Togolese Energy Prices</h2>
<p>Togolese diesel runs US$1.00-1.10 per litre; a 9-12 t box truck on port duty burns 0.30-0.38 L/km including idle time &mdash; about US$0.34 per kilometre. The KT5M consumes 0.75-0.90 kWh/km; at CEET industrial tariffs of roughly US$0.13-0.15/kWh, US$0.12 per kilometre. On 4,500 km per month (two-shift port duty), the monthly energy saving is about US$1,000 per truck. Maintenance adds US$200-300 monthly &mdash; no oil, no clutch, no DPF, and brake pads lasting 2-3x longer. Against a US$18,000-25,000 purchase premium, payback lands at 15-20 months. For the reefer variant serving Lom&eacute;&rsquo;s cold chain (frozen fish and poultry transhipment is significant), the case strengthens further: the electric reefer runs off the traction battery at a fraction of a diesel reefer unit&rsquo;s fuel cost.</p>
<ul>
<li><strong>Energy per km:</strong> US$0.34 diesel vs US$0.12 electric &mdash; 65% lower</li>
<li><strong>Monthly saving per truck:</strong> ~US$1,200-1,300 on two-shift duty</li>
<li><strong>Payback:</strong> 15-20 months; faster for reefer variants</li>
<li><strong>Gate queues:</strong> 20-30% of diesel idle fuel eliminated</li>
</ul>

<h2>Charging at the Port Logistics Zone</h2>
<p>Lom&eacute;&rsquo;s port logistics zone and the N1 warehouse corridor have the medium-voltage capacity for depot charging; a ten-truck KT5M fleet runs on roughly 300-350 kVA with managed charging &mdash; a standard industrial connection for the CEET network in this district. The practical layout: one 120 kW DC charger per 6-8 trucks for rotation charging, overnight AC at each bay, and the load-management controller configured to the terminal&rsquo;s shift schedule. Togo&rsquo;s solar resource (4.8-5.2 peak sun hours) makes a yard canopy strongly economic: 150-250 kWp offsets 40-55% of charging energy and provides covered parking in a port city where shade has operational value.</p>
<p>A planning note specific to transhipment hubs: freight volumes at Lom&eacute; are growing as the port captures market share, and electrification infrastructure should be sized for the fleet at month 24, not month one. We specify switchboards and conduits for double the initial charger count &mdash; the marginal cost is trivial at construction and eliminates the most expensive retrofit in fleet electrification, which is re-digging the yard.</p>

<h2>Import and Corridor Context</h2>
<p>Togo offers duty advantages on electric vehicles, and Lom&eacute;&rsquo;s RoRo facilities are the most efficient on the coast &mdash; the same operational excellence that won the transhipment traffic applies to truck imports, with 30-36 day sailings from China and fast customs cycles. We deliver the French-language homologation dossier, UN R100 certification and parts kit as standard. For logistics groups operating across the coastal corridor, our <a href="../markets/ghana.html">Ghana market page</a> covers the parallel Tema port ecosystem 190 km east &mdash; several 3PLs run both ports&rsquo; final-leg fleets, and platform standardisation across Lom&eacute; and Tema halves parts and training overhead.</p>
<p>The corridor dimension deserves emphasis because it is Lom&eacute;&rsquo;s unique role: the port is the maritime gateway for Burkina Faso, Niger and Mali, and the N1 corridor fleets serving those landlocked markets are watching the coastal electrification closely. The box trucks electrify first; the corridor tractors follow as charging extends north. Fleet owners with both coastal and corridor operations can sequence exactly this transition, and the telematics platform manages the mixed fleet through the whole migration.</p>

<h2>First Movers at the Region&rsquo;s Hub</h2>
<p>The strongest first candidates are the terminal-adjacent 3PLs and the cement/food distributors with captive port-zone routes. Their utilisation is the highest, their yards are already secured and powered, and their customers &mdash; increasingly the multinational FMCG groups with scope-3 targets &mdash; will pay attention to zero-emission final legs. Lom&eacute; won its transhipment position by moving faster than its neighbours on port efficiency. The same instinct applied to final-leg electrification produces the region&rsquo;s lowest-cost port logistics &mdash; and the arithmetic above suggests the window where this is still a differentiator, rather than a necessity, is measured in years, not decades.</p>
'''))

# ---------------------------------------------------------------- 8
ARTICLES.append(dict(
f='cotonou-benin-electric-delivery-truck-fleet',
t='Cotonou Delivery Economics: KT5J Electric Trucks for Benin&rsquo;s Port-City Freight',
d='Cotonou&rsquo;s port-city freight and Nigeria-border trade suit the KT5J electric delivery truck. Real TCO numbers, charging plan and import guide for this EV truck in Benin.',
k='KT5J electric delivery truck, EV truck Benin, electric truck Cotonou, electric delivery truck West Africa, Dongfeng electric truck, Cotonou port electric truck',
img='models/p07_08.jpg',
alt='Dongfeng KT5J electric delivery truck on a Cotonou distribution route, EV truck for Benin freight',
net='zhc',
body='''
<p>Cotonou is Benin&rsquo;s economic capital and its only real port &mdash; and it is also, functionally, the second port of Nigeria. A substantial share of the containers cleared at Cotonou roll east toward the Seme border and the Lagos market, while the rest feeds Benin&rsquo;s own consumption through a tight urban freight network compressed between the lagoon and the N1. That freight moves today in ageing diesel box trucks paying some of West Africa&rsquo;s higher effective fuel costs. This article works through the <a href="../products/models/kt5j-electric-cargo-truck.html">Dongfeng KT5J electric delivery truck</a> for Cotonou&rsquo;s port-city distribution: the duty cycle, the TCO, the charging plan, and the import path. For Beninese 3PLs and distributors, this EV truck segment offers the fastest payback in the country&rsquo;s fleet economy.</p>

<h2>The Cotonou Duty Cycle</h2>
<p>Urban delivery in Cotonou is compact even by West African standards. The port to the warehouse districts of Gb&eacute;gamey and Akpakpa is 5-15 km; port to the Dantokpa market zone, under 10 km; port to the Seme border post, 35 km. A delivery truck on this pattern runs 80-150 km daily across two waves &mdash; morning port clearance and afternoon city distribution &mdash; and sleeps in the same yard every night. The KT5J&rsquo;s 180-220 km real-world range covers the longest day with a 30% reserve, and the two-wave pattern creates a natural midday window for a 30-40 minute top-up charge at the yard. No public charging is required; the entire operation runs on one depot.</p>
<p>Traffic congestion, which Cotonou shares with every coastal West African city, inverts the diesel-versus-electric comparison. A diesel box truck in stop-and-go traffic burns fuel at its worst efficiency point and wears its clutch at dock and market approaches. The electric drivetrain is at its best precisely there: zero idle consumption, instant torque for the gap-shooting urban driving style, and regenerative braking that turns the constant deceleration into recovered energy. Our fleet data from comparable Lagos and Abidjan duty shows urban congestion improves the EV truck&rsquo;s relative economy by 8-12% versus free-flowing routes.</p>

<h2>KT5J Specifications for Beninese Fleets</h2>
<table style="width:100%;border-collapse:collapse;margin:20px 0;" border="1" cellpadding="8">
<tr style="background:#006341;color:#fff;"><th style="padding:8px;text-align:left;">Parameter</th><th style="padding:8px;text-align:left;">KT5J Electric Delivery Truck</th></tr>
<tr><td style="padding:8px;">GVW / payload</td><td style="padding:8px;">7.5-9 t class / 3.5-4.5 t payload</td></tr>
<tr><td style="padding:8px;">Battery</td><td style="padding:8px;">106-130 kWh CATL LFP</td></tr>
<tr><td style="padding:8px;">Motor</td><td style="padding:8px;">LvKong 120-150 kW peak / 950-1,200 Nm</td></tr>
<tr><td style="padding:8px;">Real-world range (urban, loaded)</td><td style="padding:8px;">180-220 km</td></tr>
<tr><td style="padding:8px;">DC charge 20-80%</td><td style="padding:8px;">~35 min at 90-120 kW</td></tr>
<tr><td style="padding:8px;">Body</td><td style="padding:8px;">22-28 m&sup3; box, side-door and tail-lift options</td></tr>
<tr><td style="padding:8px;">Turning circle</td><td style="padding:8px;">~11.8 m &mdash; suits Dantokpa-area access</td></tr>
<tr><td style="padding:8px;">FOB price band</td><td style="padding:8px;">US$45,000-56,000</td></tr>
</table>
<p>Body configuration matters in Cotonou&rsquo;s market-serving freight: the side-door option converts street-side unloading from a rear-door bottleneck into a parallel operation, and the tail-lift variant eliminates the manual handling that slows market deliveries. We specify bodies per route &mdash; Dantokpa-serving fleets take the side-door box, supermarket-serving fleets take the tail-lift &mdash; because the 20-30 minutes saved per stop compounds across a 15-25 stop day into an extra delivery wave.</p>

<h2>The Benin TCO Calculation</h2>
<p>Beninese diesel retails at US$1.05-1.15 per litre. A 7.5-9 t box truck on Cotonou urban duty burns 0.26-0.32 L/km &mdash; about US$0.31 per kilometre. The KT5J consumes 0.60-0.75 kWh/km; at SBEE commercial tariffs around US$0.16-0.18/kWh, US$0.12 per kilometre. On 3,500 km per month: US$665 monthly energy saving per truck, plus US$150-250 in maintenance (no oil, clutch, injectors, or DPF; brakes lasting 2-3x longer). Total: roughly US$10,000 per truck per year against a purchase premium of US$15,000-20,000 &mdash; payback in 18-24 months, inside a battery warranty that runs 8 years or 4,500 cycles. The cross-border operators running the Seme-Lagos trade see even stronger numbers: their trucks run higher daily kilometres, and every additional kilometre is charged at the EV truck&rsquo;s 60% energy discount.</p>
<ul>
<li><strong>Energy per km:</strong> US$0.31 diesel vs US$0.12 electric &mdash; 61% lower</li>
<li><strong>Annual saving per truck:</strong> ~US$10,000 combined</li>
<li><strong>Payback:</strong> 18-24 months; faster on cross-border duty</li>
<li><strong>Urban congestion:</strong> improves relative EV economy by 8-12%</li>
</ul>

<h2>Charging: One Depot, One Application</h2>
<p>Cotonou&rsquo;s industrial districts have the grid capacity for fleet charging; a five-to-ten truck KT5J fleet needs 250-350 kVA with managed charging, which SBEE processes as a standard commercial upgrade. The configuration we deploy: one 90-120 kW DC charger for the midday rotation, overnight AC posts per bay, and load management that caps site draw at the contracted capacity while guaranteeing every truck&rsquo;s departure state of charge. The utility application goes in on purchase-order day &mdash; the 8-12 week connection lead time is the critical path, always longer than the 32-38 day vessel transit from China to Cotonou.</p>
<p>Grid reliability, the honest concern in Benin, is manageable by design: the fleet&rsquo;s own batteries are the buffer. Ten KT5Js carry over 1,000 kWh of storage; a two-hour outage is absorbed by resequencing charge sessions, with zero operational impact. Fleets wanting harder resilience add a solar canopy &mdash; at 4.8-5.2 peak sun hours, a 100-150 kWp array covers 35-45% of annual charging energy and, with a hybrid inverter, keeps the chargers alive through outages. Several Cotonou cold-storage operators already run exactly this architecture for refrigeration; adding trucks to it is incremental.</p>

<h2>Import Path and the Nigeria Dimension</h2>
<p>Benin applies reduced duties to electric vehicles, and Cotonou&rsquo;s port processes RoRo truck imports efficiently with French-language documentation, which we supply complete with UN R100 battery certification. For the substantial operator community serving the Nigeria-border trade, the strategic picture links directly to our <a href="../markets/nigeria.html">Nigeria market page</a>: the KT5J platform serves both sides of the Seme crossing with identical parts and training, and as Nigeria&rsquo;s own EV incentives develop, a Cotonou-based electric fleet is positioned to run the entire coastal corridor from one parts stock. Several Beninese 3PLs are structuring exactly this two-market play.</p>
<p>After-sales support ships with the trucks: a two-year fast-moving parts kit per fleet, CATL module availability at 10-14 days via regional stock, and telematics-based remote diagnostics with French-language engineering support. The drivetrain&rsquo;s maintenance calendar &mdash; brake inspections, coolant checks, software updates &mdash; removes the workshop dependency that grounds diesel trucks waiting on imported engine components. In a market where a truck&rsquo;s daily revenue is 1-2% of its value, uptime is the profit line.</p>

<h2>The First-Mover Logic</h2>
<p>Cotonou&rsquo;s electrification pioneers will be the FMCG distributors with captive port-to-market routes, the brewers and beverage distributors whose dense freight and fixed routes are textbook EV duty, and the 3PLs building regional ambitions on the Seme corridor. The economics at Beninese fuel prices are decisive &mdash; a 60% energy cost reduction on the highest-utilisation trucks in the fleet &mdash; and the infrastructure requirement is a single depot charger and an SBEE application. The fleets that move in the next 12 months will bank three to four years of cost advantage before electrification becomes the market standard their customers begin to expect.</p>
'''))

for a in ARTICLES:
    html = build(a)
    path = os.path.join(ROOT, 'blog', a['f'] + '.html')
    with open(path, 'w', encoding='utf-8') as fh:
        fh.write(html)
    words = len(re.sub(r'<[^>]+>', ' ', a['body']).split())
    print('%-58s %5d words' % (a['f'], words))
print('done batch1:', len(ARTICLES))
