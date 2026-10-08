# -*- coding: utf-8 -*-
"""Run 15 patch: rewrite over-long meta descriptions to 140-160 chars."""
import re

D = {
'tema-ghana-port-te46-electric-terminal-tractor':'Tema Port shuttle suits the TE46 electric terminal tractor: 262-350 kWh CATL LFP, 5-6 min battery swap and 65% lower energy cost per km. EV truck TCO.',
'cape-town-south-africa-electric-delivery-truck':'Cape Town last-mile freight suits the KT5J electric delivery truck: 106-130 kWh LFP, 180-220 km range and solar charging through load-shedding. EV truck TCO.',
'abuja-nigeria-electric-truck-government-fleet':'Abuja ministry and municipal fleets cut operating cost 55% with the KT5M electric box truck: 180-220 kWh LFP, tender-ready specs. EV truck procurement guide.',
'hawassa-ethiopia-industrial-park-electric-truck':'Hawassa textile exporters cut freight cost with the KTH3 electric cargo truck: 262 kWh LFP and hydro power at $0.05/kWh. EV truck TCO and import guide.',
'kisumu-kenya-lake-basin-electric-cargo-truck':'Kisumu Lake Basin distribution suits the KT5L electric cargo truck: 130-160 kWh LFP, 190-230 km range and geothermal-powered charging. EV truck TCO guide.',
'algiers-algeria-electric-dump-truck-construction':'Algiers metro and housing construction suits the TZ5E electric dump truck: 400 kWh LFP, low night noise. EV truck specs, TCO and import guide.',
'rabat-morocco-electric-municipal-fleet-kt1d':'Rabat municipal fleets cut cost with the KT1D electric sweeper: 140-180 kWh LFP, near-silent night shifts. EV truck specs, TCO and tender guide.',
'which-electric-truck-is-best-for-mining-operations':'Which electric truck is best for mining? Compare a 30 t 8x4 dump with 600 kWh CATL LFP against 80 t rigid haulers, with TCO and selection criteria.',
'neom-saudi-arabia-electric-construction-fleet':'NEOM zero-emission site mandates make the TZ3V 8x4 electric dump truck the logical choice for THE LINE earthworks. EV truck specs, TCO and FOB.',
'sharjah-uae-electric-waste-collection-kt3e':'Sharjah waste operators cut collection cost and night noise with the KT3E electric garbage truck. EV truck specs, TCO and charging for UAE fleets.',
'jubail-saudi-industrial-city-electric-cargo-truck':'Jubail petrochemical plants and SABIC suppliers cut in-plant logistics cost with the KTH3 electric cargo truck. EV truck specs, TCO and charging.',
'shymkent-kazakhstan-electric-truck-distribution':'Shymkent FMCG distribution suits the KT5M electric box truck: 200-240 km range, thermal management for -20&deg;C winters. EV truck TCO, import guide.',
'fergana-uzbekistan-agri-electric-cargo-truck':'Fergana Valley produce flows to Tashkent suit the KT5L electric cargo truck. EV truck range, seasonal peaks, TCO and import guide for Uzbekistan.',
'sulaymaniyah-iraq-electric-dump-truck-reconstruction':'Sulaymaniyah reconstruction and mountain quarry duty suit the TZ3Z electric dump truck. EV truck specs, TCO and FOB for Iraq rebuild fleets.',
'aqaba-jordan-port-electric-tractor':'Aqaba container terminal shuttle suits the TE46 electric tractor: 8-10 hour shift range, swap option. EV truck economics and SEZ incentives.',
'fujairah-uae-port-electric-tractor-bunkering':'Fujairah, the world&rsquo;s 2nd-largest bunkering hub, suits the TE46 electric tractor for terminal duty. EV truck safety, TCO and charging.',
'callao-peru-port-electric-tractor-fleet':'Callao Port container handling costs drop with the TE46 electric terminal tractor. Specs, shift range and Peru import steps for this EV truck.',
'iquique-chile-mining-electric-dump-truck':'Northern Chile mining cuts haulage cost with the TZ3V electric dump truck at 2,000-4,000 m altitude. Specs, TCO and Chile import steps for this EV truck.',
'cartagena-colombia-port-electric-cargo-truck':'Cartagena port-city distribution suits the KT5M electric box truck: 180-220 km range at half the energy cost of diesel. EV truck TCO, import guide.',
'puebla-mexico-automotive-electric-truck-logistics':'Puebla OEM logistics cut shuttle cost with the TE8L electric tractor: 400-500 kWh on Puebla-Veracruz runs. EV truck specs, TCO and Mexico import.',
'santiago-dominican-agri-electric-cargo-truck':'Cibao Valley agribusiness cuts haulage cost with the KT5L electric cargo truck. Produce specs, TCO and Dominican import steps for this EV truck.',
'medan-indonesia-palm-oil-electric-truck':'North Sumatra palm oil haulage cuts cost with the KTH3 electric truck: 262 kWh, plantation solar charging. EV truck specs, Indonesia import steps.',
'clark-philippines-logistics-hub-electric-truck':'Clark Freeport e-commerce and airport-city freight suit the KT5J electric delivery truck: 106-130 kWh, FOB US$45-56k. EV truck TCO, import guide.',
'ev-truck-tco-latin-america-country-comparison':'Electric truck TCO across Latin America: Mexico, Chile, Colombia, Peru and Dominican Republic energy prices, duty and payback compared for EV truck fleets.',
'ev-truck-charging-peak-shaving-battery-buffer':'Peak shaving for EV truck depots: battery-buffered charging cuts demand charges 40%. Architecture, sizing math and an Eskom tariff worked example.',
'ev-truck-monsoon-season-operations-guide':'Monsoon operations for EV truck fleets: IP67 high-voltage protection, wading depth, charging-in-rain safety and wet-season route planning in South Asia.',
'peru-electric-truck-import-incentives-policy':'Peru electric truck buyers cut landed cost with EV import incentives, Lima municipal perks and SUNAT clearance. A worked KT5M EV truck landed-cost case.',
'ready-mix-plant-electric-mixer-fleet-design':'Design an electric mixer fleet around the batching plant: plant-anchored charging, drum cycle scheduling and kWh-per-m3 math with the TZ8J EV truck.',
'ev-truck-battery-swap-network-central-asia':'Central Asia corridors suit EV truck battery swap: 5-6 min swaps, standardised packs and lower capex vs depot charging. TE8L corridor strategy inside.',
'tanzania-electric-truck-import-guide':'Tanzania electric truck imports: TRA EV duty treatment, TBS standards, Dar es Salaam RoRo clearance and EAC rules, with landed cost and timeline.',
'quarry-loading-cycle-electric-dump-truck-optimization':'Quarry productivity jumps with the KTA1 electric dump truck: loader matching, cycle-time math, regen on downhill runs, tonnes per kWh. Ghana EV truck guide.',
'electric-truck-uptime-guarantee-service-contract-design':'Electric truck fleets need uptime guarantees: 95-97% SLA targets, spare-truck ratios, parts kits and telemetry PM with the TE8P EV truck in Chile.',
'how-much-can-fleets-save-switching-to-electric-trucks':'Fleets save 50-65% on energy with 18-30 month payback switching to electric trucks. A worked 10-truck Kenya EV truck example with TCO sensitivity.',
'valparaiso-chile-port-electric-tractor':'Valpara&iacute;so port deploys TE46 electric tractors for TPS/EPV terminals and hillside logistics. Chile policy and 262-350 kWh EV truck specs inside.',
}

for f, new in D.items():
    assert 140 <= len(new) <= 160, (f, len(new))
    assert 'EV truck' in new or 'electric truck' in new, f
    p = 'blog/%s.html' % f
    h = open(p, encoding='utf-8').read()
    old = re.search(r'<meta name="description" content="(.*?)">', h).group(1)
    h = h.replace(old, new)
    open(p, 'w', encoding='utf-8').write(h)
print('rewrote', len(D), 'descriptions, all 140-160 chars with EV truck term')
