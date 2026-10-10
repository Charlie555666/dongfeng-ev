# -*- coding: utf-8 -*-
"""Contenido + runner del lote piloto en espanol. Importa infraestructura de _gen_es."""
import os, re, io, json
from _gen_es import (page, w, cta_band_es, faq_html_es, faq_schema_es,
                     json_str, BASE, SITE, TODAY, ORG_SCHEMA, WA_LINK)

WA_BTN = ('<a class="btn btn-primary" href="' + WA_LINK + '" target="_blank" rel="noopener">'
          'Solicitar cotizaci\u00f3n por WhatsApp</a>')

def hero_sm(bc_html, h1, sub):
    return ('<div class="page-hero-sm">\n  <div class="section-inner">\n'
            '    <div class="bc">' + bc_html + '</div>\n'
            '    <h1>' + h1 + '</h1>\n'
            '    <p>' + sub + '</p>\n'
            '  </div>\n</div>\n')

def main_open():
    return '<main class="section"><div class="section-inner">\n'

def main_close():
    return '</div></main>\n'

def card(name, slug, kind, spec, img):
    return ('<div class="prod-card">\n'
            '  <div class="pc-img"><img src="' + img + '" alt="Dongfeng ' + name + ' cami\u00f3n el\u00e9ctrico" loading="lazy"></div>\n'
            '  <div class="pc-body">\n'
            '    <h3><a href="' + slug + '" style="color:inherit;text-decoration:none;">' + name + '</a></h3>\n'
            '    <div class="pc-tags"><em>' + kind + '</em></div>\n'
            '    <p>' + spec + '</p>\n'
            '  </div>\n'
            '</div>\n')

def prod_grid(cards):
    return '<div class="prod-grid-4">\n' + "\n".join(cards) + '\n</div>\n'

# ============================================================ HOME
HOME_FAQ = [
    ("\u00bfQu\u00e9 es un cami\u00f3n el\u00e9ctrico (EV truck)?",
     "Un cami\u00f3n el\u00e9ctrico es un veh\u00edculo comercial impulsado \u00edntegramente por un tren motriz el\u00e9ctrico con bater\u00eda, sin motor di\u00e9sel. Los camiones el\u00e9ctricos Dongfeng que exportamos usan paquetes de bater\u00edas CATL LFP (262\u2013600 kWh) y ejes motrices el\u00e9ctricos LvKong, con 282\u2013510 kW de potencia y cero emisiones para puertos, miner\u00eda, municipios y log\u00edstica urbana."),
    ("\u00bfCu\u00e1nta autonom\u00eda tiene un cami\u00f3n el\u00e9ctrico Dongfeng?",
     "Depende del modelo y la carga. Los tractocamiones de la serie TE alcanzan hasta 350 km por carga con un paquete de 600 kWh, mientras que el KT5M de carga cubre 200\u2013280 km con 262\u2013310 kWh. Las versiones con intercambio de bater\u00eda se recargan en 5\u20136 minutos."),
    ("\u00bfCu\u00e1nto tarda la recarga?",
     "Con carga r\u00e1pida DC de doble pistola a 350 kW, del 20% al 80% en unos 40\u201360 minutos seg\u00fan el tama\u00f1o del paquete. Las flotas que operan 24/7 pueden elegir modelos de intercambio de bater\u00eda, que cambian un paquete completo en menos de 6 minutos."),
    ("\u00bfUn cami\u00f3n el\u00e9ctrico es m\u00e1s econ\u00f3mico que uno di\u00e9sel?",
     "S\u00ed. La electricidad cuesta normalmente entre 60% y 80% menos que el combustible di\u00e9sel por kil\u00f3metro, y el tren motriz el\u00e9ctrico tiene muchas menos piezas de desgaste: sin aceite de motor, filtros, turbo ni postratamiento de escape. La mayor\u00eda de las flotas de alta utilizaci\u00f3n recuperan la prima de compra en 1,5 a 3 a\u00f1os, con garant\u00eda de bater\u00eda de 8 a\u00f1os / 4.500 ciclos."),
    ("\u00bfQu\u00e9 cami\u00f3n el\u00e9ctrico conviene para miner\u00eda, puertos y cargas pesadas?",
     "Para miner\u00eda y construcci\u00f3n, los volquetes el\u00e9ctricos 8x4 de la serie TZ (KTA1, TZ3Z, TZ3V) manejan 55\u201380 t con paquetes de 400\u2013600 kWh. Para puertos y contenedores de corto recorrido, el tractocami\u00f3n 4x2 TE46 (42 t GCW) es la opci\u00f3n m\u00e1s popular. Para log\u00edstica urbana, los camiones de caja KT5M/KTH son los m\u00e1s rentables."),
    ("\u00bfExportan a mi pa\u00eds?",
     "Exportamos a m\u00e1s de 60 pa\u00edses en \u00c1frica, Medio Oriente, Sudeste Asi\u00e1tico, Asia Central, Am\u00e9rica Latina y Europa, con env\u00edo RoRo, granelero o contenedor, y configuraciones RHD (volante a la derecha) y CCS2 con especificaci\u00f3n europea. Ind\u00edcanos tu pa\u00eds y aplicaci\u00f3n y confirmamos la homologaci\u00f3n y el est\u00e1ndar de carga exactos."),
]

def home_body():
    b = []
    b.append('<main>\n')
    b.append('''<section class="hero">
  <div class="hero-inner">
    <h1>Camiones El\u00e9ctricos Dongfeng \u2014 Veh\u00edculos Comerciales Cero Emisiones listos para exportaci\u00f3n</h1>
    <p>Exportador autorizado de tractocamiones, volquetes, camiones de carga y veh\u00edculos especiales el\u00e9ctricos Dongfeng \u2014 bater\u00edas CATL, motores LvKong, carga r\u00e1pida e intercambio de bater\u00eda.</p>
    <div class="hero-btns">
      <a class="btn btn-primary" href="/es/products/electric-tractor.html">Ver productos</a>
      <a class="btn btn-outline" href="/es/contact-us.html">Pedir cotizaci\u00f3n</a>
    </div>
  </div>
</section>
''')
    b.append('''<section class="stats-band">
  <div class="stats-inner">
    <div class="stat-item"><div class="stat-num">1969</div><div class="stat-label">Dongfeng: m\u00e1s de 55 a\u00f1os fabricando camiones</div></div>
    <div class="stat-item"><div class="stat-num">63<small>M+</small></div><div class="stat-label">Veh\u00edculos entregados desde 1969</div></div>
    <div class="stat-item"><div class="stat-num">60+</div><div class="stat-label">Pa\u00edses con venta y servicio</div></div>
    <div class="stat-item"><div class="stat-num">600<small>kWh</small></div><div class="stat-label">Paquete CATL m\u00e1ximo</div></div>
    <div class="stat-item"><div class="stat-num">8<small>a\u00f1os</small></div><div class="stat-label">Garant\u00eda de bater\u00eda / 4.500 ciclos</div></div>
  </div>
</section>
''')
    b.append('<section class="rec-section">\n  <div class="section-inner" style="margin-bottom:36px;text-align:center;">\n'
             '    <h2 class="section-title">Modelos el\u00e9ctricos destacados</h2>\n'
             '    <p class="section-sub" style="margin-left:auto;margin-right:auto;">Configuraciones m\u00e1s vendidas para mercados internacionales.</p>\n  </div>\n')
    b.append(prod_grid([
        card("TE46", "/es/products/models/te46-electric-tractor.html", "4x2 \u00b7 Puerto", "Cabeza tractora KL MAX, 42 t GCW, CATL 400 kWh, LvKong 315/510 kW. Bater\u00eda lateral, centro de gravedad bajo, carga r\u00e1pida de doble pistola 500 A.", "/images/models/p05_01.jpg"),
        card("TE8L / TE8K", "/es/products/electric-tractor.html", "6x4 \u00b7 49 t", "Tractocami\u00f3n de larga distancia, CATL 400/466/600 kWh, LvKong 315/510 kW, 4AMT, EBS+ESC, LDWS+FCWS. TE8K con interfaz CCS2 para Europa.", "/images/models/p06_00.jpg"),
        card("TZ3Z", "/es/products/models/tz3z-electric-dump-truck.html", "8x4 \u00b7 55 t", "Volquete de construcci\u00f3n KC PRO D320KC, CATL 400 kWh, LvKong 315/510 kW, eje HDZ300. 20\u201380% SOC en ~40 min con carga de 600 A.", "/images/cat-dump.jpg"),
        card("TZ3V", "/es/products/electric-dump.html", "8x4 \u00b7 80 t", "Volquete minero de grado pesado, chasis multicapa 8+8+4, CATL 600 kWh, LvKong 400/550 kW.", "/images/models/p13_00.jpg"),
        card("KT5M", "/es/products/models/kt5m-electric-cargo-truck.html", "4x2 \u00b7 65 m\u00b3", "Cami\u00f3n de caja KR D560e, distancia entre ejes 7.150 mm, CATL 262/310 kWh, eje motriz el\u00e9ctrico LvKong 150/270 kW. Volumen >65 m\u00b3, autonom\u00eda hasta 400 km.", "/images/models/p08_01.jpg"),
        card("KT5J", "/es/products/electric-cargo.html", "4x2 \u00b7 Regional", "Variante de batalla corta (5.000 mm) para distribuci\u00f3n urbana. CATL 262/310 kWh, motor 150/270 kW.", "/images/models/p09_00.jpg"),
        card("KT3F / KT7A", "/es/products/electric-special.html", "4x2 / 6x4 \u00b7 Riego", "Cisternas municipales y de supresi\u00f3n de polvo. CATL 166\u2013232 kWh, LvKong 128/260 kW. Configuraciones 4x2 (18 t) y 6x4 (25 t).", "/images/models/p14_07.jpg"),
        card("TZ8J / KT9X", "/es/products/electric-special.html", "8x4 \u00b7 Hormig\u00f3n", "Hormigoneras 44\u201345 t, CATL 333/410 kWh, LvKong 350/520 kW. KT9X cumple WVTA GSR2 para homologaci\u00f3n EU completa.", "/images/models/p16_00.jpg"),
    ]))
    b.append('</section>\n')
    b.append('''<section class="section" style="background:#fff;">
  <div class="section-inner">
    <h2 class="section-title">Tecnolog\u00eda y ventajas</h2>
    <p class="section-sub">Sistemas "tres el\u00e9ctricos" de los principales proveedores del sector.</p>
    <div class="tech-grid">
      <div class="tech-card"><h4>Bater\u00edas CATL LFP</h4><p>Paquetes de litio-ferrofosfato CATL de 166\u2013600 kWh con garant\u00eda de 8 a\u00f1os / 4.500 ciclos. Montaje lateral o trasero seg\u00fan su operaci\u00f3n.</p></div>
      <div class="tech-card"><h4>Propulsi\u00f3n LvKong</h4><p>Motores s\u00edncronos de imanes permanentes LvKong hasta 550 kW y ejes motrices el\u00e9ctricos 4AMT: par comparable al di\u00e9sel desde cero.</p></div>
      <div class="tech-card"><h4>Carga r\u00e1pida e intercambio</h4><p>Carga de doble pistola hasta 600 A: 20\u201380% SOC en unos 40 minutos. Modelos seleccionados admiten intercambio de bater\u00eda CATL para operar 24/7.</p></div>
      <div class="tech-card"><h4>RHD y cumplimiento europeo</h4><p>Modelos RHD TE9Y, TZ4Y y TZ5Y y variantes CCS2 / WVTA GSR2 listas para tr\u00e1fico por la izquierda y mercados de la UE.</p></div>
    </div>
  </div>
</section>
''')
    b.append('''<section class="split" style="background:var(--bg);">
  <div class="split-row">
    <div class="split-media ratio"><img src="/images/models/p07_04.jpg" alt="Cami\u00f3n de carga el\u00e9ctrico Dongfeng en f\u00e1brica" loading="lazy"></div>
    <div class="split-copy">
      <h3>Exportaci\u00f3n autorizada directamente de f\u00e1brica</h3>
      <p>Exportamos veh\u00edculos de nueva energ\u00eda Dongfeng directamente del fabricante, con documentaci\u00f3n completa: de la especificaci\u00f3n al embarque.</p>
      <ul>
        <li>Canal de exportaci\u00f3n oficial Dongfeng con soporte de garant\u00eda de f\u00e1brica</li>
        <li>30% de anticipo por T/T, saldo antes del embarque o contra copia del B/L</li>
        <li>Env\u00edo RoRo, granelero o contenedor a todo el mundo</li>
        <li>Plazo de producci\u00f3n de 20\u201325 d\u00edas para configuraciones est\u00e1ndar</li>
        <li>Repuestos y posventa en m\u00e1s de 60 pa\u00edses</li>
      </ul>
      <div class="slide-actions" style="margin-top:22px;"><a href="/es/about-us.html" class="btn btn-primary">Por qu\u00e9 nosotros</a><a href="/es/contact-us.html" class="btn btn-ghost" style="color:#006341;border-color:#006341;">Hablar con ventas</a></div>
    </div>
  </div>
  <div class="split-row flip">
    <div class="split-media ratio"><img src="/images/models/p11_04.jpg" alt="Camiones el\u00e9ctricos Dongfeng en operaci\u00f3n urbana y portuaria" loading="lazy"></div>
    <div class="split-copy">
      <h3>Cero emisiones y costo total de propiedad m\u00e1s bajo</h3>
      <p>Los camiones el\u00e9ctricos recortan el costo de combustible entre 60% y 80% y simplifican el mantenimiento.</p>
      <ul>
        <li>Recuperaci\u00f3n de energ\u00eda v\u00eda EBS hasta 10\u201320% m\u00e1s eficiente que ABS</li>
        <li>Menor costo por kil\u00f3metro en rutas portuarias, mineras, municipales y urbanas</li>
        <li>Ensayos de fiabilidad de 1.250 km y 323 pruebas de componentes por modelo</li>
        <li>Calefacci\u00f3n de agua PTC, cabinas con suspensi\u00f3n neum\u00e1tica e iluminaci\u00f3n LED de serie</li>
        <li>Gesti\u00f3n t\u00e9rmica de bater\u00eda HD para climas c\u00e1lidos y fr\u00edos</li>
      </ul>
      <div class="slide-actions" style="margin-top:22px;"><a href="/es/products/electric-tractor.html" class="btn btn-primary">Ver modelos</a><a href="/es/markets/index.html" class="btn btn-ghost" style="color:#006341;border-color:#006341;">Mercados</a></div>
    </div>
  </div>
</section>
''')
    b.append('<section class="section" id="faq" style="background:#fff;"><div class="section-inner">\n')
    b.append('  <h2 class="section-title">Preguntas frecuentes sobre camiones el\u00e9ctricos</h2>\n')
    b.append('  <p class="section-sub">Respuestas directas sobre comprar y operar camiones el\u00e9ctricos desde China.</p>\n')
    b.append(faq_html_es(HOME_FAQ, "M\u00e1s preguntas"))
    b.append('\n</div></section>\n')
    b.append(cta_band_es("\u00bfListo para electrificar su flota?",
                         "Env\u00edenos su aplicaci\u00f3n, carga y ruta: recomendamos la configuraci\u00f3n Dongfeng EV adecuada y le damos una cotizaci\u00f3n directa de f\u00e1brica en 24 horas."))
    b.append('</main>\n')
    return "\n".join(b)

# ============================================================ CATEGORY PAGES
CATS = {
 "tractor": dict(
   es="es/products/electric-tractor.html", en="products/electric-tractor.html",
   title="Tractocamiones El\u00e9ctricos Dongfeng \u2014 TE46, TE8L, TE9L, TE8M | Exportaci\u00f3n",
   desc="Tractocamiones el\u00e9ctricos Dongfeng para exportaci\u00f3n: TE46 4x2 (42 t), TE8L/TE8K 6x4 (49 t), TE8M 6x4 (80 t) y TE9Y RHD. Bater\u00edas CATL 400\u2013600 kWh, motores LvKong.",
   kw="tractocami\u00f3n el\u00e9ctrico, tractocami\u00f3n el\u00e9ctrico Dongfeng, cabeza tractora el\u00e9ctrica, TE46, TE8L, TE8M, cami\u00f3n el\u00e9ctrico para puerto, exportaci\u00f3n camiones China",
   h1="Tractocamiones El\u00e9ctricos Dongfeng",
   sub="Tractocamiones 4x2 y 6x4 de 42 a 80 t GCW con bater\u00edas CATL e impulsi\u00f3n el\u00e9ctrica LvKong \u2014 para puertos, larga distancia y cargas pesadas.",
   intro="La serie TE combina cabinas Dongfeng KL/KR con ejes motrices el\u00e9ctricos LvKong y paquetes de bater\u00edas CATL LFP de 400 a 600 kWh. Son tractocamiones pensados para operaciones de alta utilizaci\u00f3n: contenedores portuarios, transporte de larga distancia y trenes de carretera pesados.",
   rows=[("TE46","4x2 · 42 t GCW","Cabeza tractora KL MAX. CATL 400 kWh, LvKong 315/510 kW, bater\u00eda lateral, carga r\u00e1pida 500 A de doble pistola.","/images/models/p05_01.jpg"),
         ("TE8L / TE8K","6x4 · 49 t GCW","Tractocami\u00f3n de larga distancia. CATL 400/466/600 kWh, LvKong 315/510 kW, 4AMT, EBS+ESC, LDWS+FCWS. TE8K con CCS2 para Europa.","/images/models/p06_00.jpg"),
         ("TE8M","6x4 · 80 t GCW","Tractocami\u00f3n de carga pesada para carb\u00f3n y mineral. Bastidor reforzado 300x90x8+6, CATL 466/497/600 kWh, LvKong 400/550 kW, ejes DF701S/DF485.","/images/models/p04_09.jpg"),
         ("TE9Y RHD","6x4 · Volante a la derecha","Tractocami\u00f3n el\u00e9ctrico RHD para Nigeria, Kenia, Sud\u00e1frica, Australia e India. CATL 600 kWh, LvKong 400/550 kW.","/images/models/p04_00.jpg")],
   faqs=[("\u00bfCu\u00e1nta autonom\u00eda tiene un tractocami\u00f3n el\u00e9ctrico Dongfeng?","La serie TE alcanza hasta 350 km por carga con el paquete de 600 kWh, seg\u00fan carga y perfil de ruta. Las versiones con intercambio de bater\u00eda recuperan un paquete completo en menos de 6 minutos."),
         ("\u00bfCu\u00e1l es la diferencia entre el TE46 y el TE8L?","El TE46 es un 4x2 de 42 t GCW pensado para puertos y recorridos cortos con alta frecuencia de giro. El TE8L es un 6x4 de 49 t GCW para larga distancia, con paquetes de hasta 600 kWh y m\u00e1s sistemas de seguridad."),
         ("\u00bfOfrecen volante a la derecha (RHD)?","S\u00ed. El TE9Y RHD est\u00e1 dise\u00f1ado para mercados de tr\u00e1fico por la izquierda, con la misma cadena de tracci\u00f3n LvKong de 400/550 kW y bater\u00eda CATL de 600 kWh.")],
 ),
 "dump": dict(
   es="es/products/electric-dump.html", en="products/electric-dump.html",
   title="Volquetes El\u00e9ctricos Dongfeng \u2014 KTA1, TZ3Z, TZ3V 8x4 | Exportaci\u00f3n",
   desc="Volquetes el\u00e9ctricos Dongfeng para miner\u00eda y construcci\u00f3n: KTA1 8x4 (31 t), TZ3Z 8x4 (55 t) y TZ3V 8x4 (80 t). Bater\u00edas CATL 352\u2013600 kWh y versiones RHD.",
   kw="volquete el\u00e9ctrico, cami\u00f3n volquete el\u00e9ctrico, volquete minero el\u00e9ctrico, TZ3Z, TZ3V, KTA1, dump truck el\u00e9ctrico, exportaci\u00f3n volquetes China",
   h1="Volquetes El\u00e9ctricos Dongfeng",
   sub="Volquetes 8x4 de 31 a 80 t para miner\u00eda, canteras y construcci\u00f3n urbana \u2014 cero emisiones y costo por tonelada m\u00e1s bajo.",
   intro="La serie TZ/KTA de volquetes el\u00e9ctricos Dongfeng est\u00e1 construida sobre chasis KC reforzados con bastidores multicapa. Combinan paquetes CATL de 352 a 600 kWh con motores LvKong de 270 a 550 kW para mantener el ciclo de trabajo en mina y obra.",
   rows=[("KTA1","8x4 · 31 t GVW","Volquete KC PLUS D560KC para residuos de construcci\u00f3n urbana. CATL 352 kWh, LvKong 270/450 kW, 4AMT, bastidor multicapa de alta resistencia.","/images/models/p11_10.jpg"),
         ("TZ3Z","8x4 · 55 t GVW","Volquete de obra KC PRO D320KC. CATL 400 kWh, LvKong 315/510 kW, eje HDZ300. 20\u201380% SOC en ~40 min.","/images/cat-dump.jpg"),
         ("TZ3V","8x4 · 80 t GVW","Volquete de grado minero, bastidor 8+8+4, CATL 600 kWh, LvKong 400/550 kW. M\u00e1xima carga \u00fatil en caminos de mina y cantera.","/images/models/p13_00.jpg"),
         ("TZ4Y / TZ5Y RHD","8x4 · Volante a la derecha","Volquetes RHD (55\u201380 t) para mercados africanos y de la Commonwealth. CATL 600 kWh con arquitectura opcional de intercambio de bater\u00eda.","/images/models/p11_00.jpg")],
   faqs=[("\u00bfQu\u00e9 volquete el\u00e9ctrico Dongfeng conviene para miner\u00eda?","Para miner\u00eda y canteras, el TZ3V 8x4 de 80 t con bastidor 8+8+4 y CATL 600 kWh es el modelo de mayor capacidad; el TZ3Z de 55 t equilibra costo y capacidad para obras y residuos de construcci\u00f3n."),
         ("\u00bfC\u00f3mo afecta el fr\u00edo o el calor extremo a la bater\u00eda?","Todos los paquetes CATL LFP llevan gesti\u00f3n t\u00e9rmica HD y est\u00e1n validados de -20\u00b0C a +50\u00b0C, con pruebas de fiabilidad de 12.500 km por unidad de exportaci\u00f3n."),
         ("\u00bfSe puede operar 24 horas al d\u00eda?","S\u00ed, con carga r\u00e1pida de doble pistola (20\u201380% en ~40 minutos) o con modelos de intercambio de bater\u00eda que cambian el paquete en menos de 6 minutos.")],
 ),
 "cargo": dict(
   es="es/products/electric-cargo.html", en="products/electric-cargo.html",
   title="Camiones de Carga El\u00e9ctricos Dongfeng \u2014 KT5M, KT5J, KTH 4x2/8x4 | Exportaci\u00f3n",
   desc="Camiones de carga el\u00e9ctricos Dongfeng: KT5M 4x2 con m\u00e1s de 65 m\u00b3, KT5J urbano y chasis 8x4 KTH1/KTH3. Bater\u00edas CATL 262\u2013400 kWh y eje motriz el\u00e9ctrico.",
   kw="cami\u00f3n de carga el\u00e9ctrico, cami\u00f3n de caja el\u00e9ctrico, KT5M, KT5J, KTH, cami\u00f3n el\u00e9ctrico urbano, exportaci\u00f3n camiones el\u00e9ctricos China",
   h1="Camiones de Carga El\u00e9ctricos Dongfeng",
   sub="Camiones de caja y chasis 4x2 y 8x4 para distribuci\u00f3n urbana y regional, con eje motriz el\u00e9ctrico y hasta 400 km de autonom\u00eda.",
   intro="La serie KT/KTH cubre la log\u00edstica urbana y regional: camiones de caja 4x2 con vol\u00famenes superiores a 65 m\u00b3, versiones de batalla corta para ciudad y chasis r\u00edgidos 8x4 para granel, forraje o ganado. El eje motriz el\u00e9ctrico LvKong reduce el consumo y elimina el \u00e1rbol de transmisi\u00f3n.",
   rows=[("KT5M","4x2 · 65 m\u00b3","Cami\u00f3n de caja KR D560e, distancia entre ejes 7.150 mm, CATL 262/310 kWh, eje motriz LvKong 150/270 kW. Autonom\u00eda hasta 400 km.","/images/models/p08_01.jpg"),
         ("KT5J","4x2 · Regional","Variante de batalla corta (5.000 mm) para distribuci\u00f3n urbana. CATL 262/310 kWh, 150/270 kW \u2014 equivalente a un di\u00e9sel de 6 cilindros.","/images/models/p09_00.jpg"),
         ("KTH1 / KTH2","8x4 · Carga pesada","Chasis r\u00edgido 8x4 para granel, forraje y ganado. CATL 264\u2013400 kWh, LvKong 270/450 kW, radio de giro 10,5 m, TDP 120 kW.","/images/models/p07_04.jpg"),
         ("KTH3","8x4 · Caja larga","Caja de hasta 9,8 m con CATL 400 kWh y LvKong 450 kW. Chasis ligero (9,65 t) para hasta 38 t de conjunto.","/images/models/p10_00.jpg")],
   faqs=[("\u00bfCu\u00e1l es el costo por kil\u00f3metro de un cami\u00f3n el\u00e9ctrico?","La electricidad suele costar entre 60% y 80% menos que el di\u00e9sel por kil\u00f3metro. En rutas urbanas y portuarias, la mayor\u00eda de las flotas recuperan la prima de compra en 1,5 a 3 a\u00f1os."),
         ("\u00bfQu\u00e9 autonom\u00eda real tiene el KT5M?","El KT5M cubre 200\u2013280 km con paquetes de 262\u2013310 kWh y hasta 400 km en condiciones favorables. En rutas planas y con carga constante, el consumo baja de 8% de bater\u00eda por 100 km."),
         ("\u00bfSe puede adaptar la caja o el chasis?","S\u00ed. Ofrecemos caja seca, plataforma y chasis para carrozar, adem\u00e1s de adaptaciones de pintura, bater\u00eda y est\u00e1ndar de carga seg\u00fan el pa\u00eds de destino.")],
 ),
 "special": dict(
   es="es/products/electric-special.html", en="products/electric-special.html",
   title="Veh\u00edculos Especiales El\u00e9ctricos Dongfeng \u2014 Riego, Barrido, Basura y Hormigonera",
   desc="Veh\u00edculos especiales el\u00e9ctricos Dongfeng: cisternas de riego KT3F/KT7A, barredoras KT1D, camiones de basura KT3E/TZ2E y hormigoneras TZ8J/KT9X (WVTA).",
   kw="cami\u00f3n el\u00e9ctrico de riego, barredora el\u00e9ctrica, cami\u00f3n de basura el\u00e9ctrico, hormigonera el\u00e9ctrica, veh\u00edculos municipales el\u00e9ctricos Dongfeng",
   h1="Veh\u00edculos Especiales El\u00e9ctricos Dongfeng",
   sub="Riego, barrido, recogida de residuos y hormigoneras el\u00e9ctricas \u2014 operaci\u00f3n silenciosa y sin emisiones para ciudades y obras.",
   intro="Los veh\u00edculos especiales el\u00e9ctricos Dongfeng cubren los servicios municipales y la construcci\u00f3n: cisternas de riego y supresi\u00f3n de polvo, barredoras-lavadoras, camiones de recogida y traslado de residuos y hormigoneras. Todos utilizan bater\u00edas CATL LFP y propulsi\u00f3n LvKong, con tomas de fuerza el\u00e9ctricas para el equipo de trabajo.",
   rows=[("KT3F / KT7A","4x2 / 6x4 · Riego","Cisternas municipales y de supresi\u00f3n de polvo. CATL 166\u2013232 kWh, LvKong 128/260 kW. Configuraciones 4x2 (18 t) y 6x4 (25 t).","/images/models/p14_07.jpg"),
         ("KT1D","4x2 · Barrido y lavado","Barredora-lavadora para v\u00edas urbanas. CATL 232/266 kWh, LvKong 128/260 kW de accionamiento directo, EBS. Operaci\u00f3n silenciosa y sin emisiones de madrugada.","/images/models/p14_00.jpg"),
         ("KT3E / TZ2E","4x2 / 8x4 · Residuos","Camiones de recogida y traslado de basura. CATL 232\u2013252 kWh, LvKong 156/310 kW con 4AMT. Recuperaci\u00f3n de energ\u00eda de hasta 20% v\u00eda EBS.","/images/models/p15_00.jpg"),
         ("TZ8J / KT9X","8x4 · Hormig\u00f3n","Hormigoneras de 44\u201345 t. CATL 333/410 kWh, LvKong 350/520 kW. El KT9X cumple WVTA GSR2 para homologaci\u00f3n completa en la UE.","/images/models/p16_00.jpg")],
   faqs=[("\u00bfLos veh\u00edculos municipales el\u00e9ctricos aguantan un turno completo?","S\u00ed. Los modelos de riego, barrido y residuos usan paquetes de 166 a 266 kWh dimensionados para un turno urbano t\u00edpico, con carga de oportunidad en el dep\u00f3sito durante la noche."),
         ("\u00bfQu\u00e9 diferencia hay entre el KT3F y el KT7A?","Ambos son cisternas el\u00e9ctricas: el KT3F es un 4x2 de 18 t para calles y riego urbano, y el KT7A es un 6x4 de 25 t para mayor volumen de agua y supresi\u00f3n de polvo en obra."),
         ("\u00bfEl KT9X se puede matricular en Europa?","S\u00ed. El KT9X cumple los requisitos WVTA GSR2 de seguridad, lo que permite la homologaci\u00f3n completa de tipo en la Uni\u00f3n Europea.")],
 ),
}

MODEL_LINKS = {
    "TE46": "/es/products/models/te46-electric-tractor.html",
    "TZ3Z": "/es/products/models/tz3z-electric-dump-truck.html",
    "KT5M": "/es/products/models/kt5m-electric-cargo-truck.html",
}

def cat_body(c):
    b = [main_open()]
    b.append('<div class="section-title"><h2>' + c["h1"] + '</h2></div>\n')
    b.append('<p style="font-size:16px;line-height:1.8;max-width:900px;">' + c["intro"] + '</p>\n')
    b.append('<div class="section-title" style="margin-top:28px;"><h2>Modelos de la serie</h2></div>\n')
    cat_url = "/" + c["es"]
    cards = []
    for (n, k, d, img) in c["rows"]:
        first = n.split()[0]
        link = MODEL_LINKS.get(first, cat_url)
        cards.append(card(n, link, k, d, img))
    b.append(prod_grid(cards))
    b.append('\n<div style="margin-top:8px;font-size:13px;color:#777;">* Modelos seg\u00fan disponibilidad. Cons\u00faltenos la ficha t\u00e9cnica completa y la configuraci\u00f3n para su pa\u00eds.</div>\n')
    b.append(faq_html_es(c["faqs"], "Preguntas frecuentes"))
    b.append(main_close())
    b.append(cta_band_es("Solicite la ficha t\u00e9cnica y el precio FOB",
                         "Indique su pa\u00eds, aplicaci\u00f3n y cantidad: enviamos especificaciones detalladas y cotizaci\u00f3n FOB/CIF en 24 horas."))
    return "\n".join(b)

# ============================================================ MODEL PAGES
MODELS = {
 "te46": dict(
   es="es/products/models/te46-electric-tractor.html", en="products/models/te46-electric-tractor.html",
   title="Dongfeng TE46 Tractocami\u00f3n El\u00e9ctrico 4x2 \u2014 Especificaciones y Precio FOB",
   desc="Ficha del tractocami\u00f3n el\u00e9ctrico Dongfeng TE46 4x2: 42 t GCW, bater\u00eda CATL 400 kWh, motor LvKong 315/510 kW, carga r\u00e1pida 500 A. Precio FOB y cotizaci\u00f3n en 24 h.",
   kw="Dongfeng TE46, tractocami\u00f3n el\u00e9ctrico 4x2, cabeza tractora el\u00e9ctrica puerto, TE46 precio FOB, cami\u00f3n el\u00e9ctrico 42 toneladas",
   h1="Dongfeng TE46 \u2014 Tractocami\u00f3n El\u00e9ctrico 4x2",
   sub="Cabeza tractora el\u00e9ctrica para puertos y contenedores: 42 t GCW, CATL 400 kWh y 510 kW de potencia m\u00e1xima.",
   specs=[("Configuraci\u00f3n de ejes","4x2"),("Peso bruto combinado (GCW)","42 t"),
          ("Bater\u00eda","CATL LFP 400 kWh, montaje lateral"),("Motor el\u00e9ctrico","LvKong 315/510 kW"),
          ("Carga r\u00e1pida","Doble pistola 500 A"),("Cabina","KL MAX, suspensi\u00f3n neum\u00e1tica"),
          ("Emisiones","Cero emisiones (BEV)"),("Garant\u00eda de bater\u00eda","8 a\u00f1os / 4.500 ciclos")],
   body="El TE46 es el tractocami\u00f3n el\u00e9ctrico 4x2 de Dongfeng para operaciones portuarias y de contenedores de alta frecuencia. Su bater\u00eda CATL de 400 kWh va montada lateralmente, lo que baja el centro de gravedad y deja libre el chasis para el enganche de semirremolque. Con 315 kW continuos y 510 kW de pico, mueve trenes de 42 t sin esfuerzo en rampas de puerto y accesos a terminal.",
   apps=["Contenedores portuarios y patio de terminal","Distribuci\u00f3n regional de corto recorrido","Operaciones en turnos m\u00faltiples con carga de oportunidad"],
   faqs=[("\u00bfCu\u00e1l es el precio FOB del Dongfeng TE46?","El precio depende de la configuraci\u00f3n (bater\u00eda, cabina, enganche y equipamiento). Como referencia, los tractocamiones el\u00e9ctricos de este rango parten de USD 75.000 FOB China. Env\u00ede su destino y uso y le damos una cotizaci\u00f3n FOB/CIF en 24 horas."),
         ("\u00bfCu\u00e1nto tarda la carga del TE46?","Con carga r\u00e1pida DC de doble pistola a 500 A, pasa del 20% al 80% en aproximadamente 40\u201360 minutos seg\u00fan el cargador disponible."),
         ("\u00bfSe puede exportar con volante a la derecha?","El TE46 se ofrece en configuraci\u00f3n LHD est\u00e1ndar. Para mercados de tr\u00e1fico por la izquierda ofrecemos el TE9Y RHD 6x4 con la misma familia de propulsi\u00f3n.")],
 ),
 "tz3z": dict(
   es="es/products/models/tz3z-electric-dump-truck.html", en="products/models/tz3z-electric-dump-truck.html",
   title="Dongfeng TZ3Z Volquete El\u00e9ctrico 8x4 55 t \u2014 Especificaciones y Precio",
   desc="Ficha del volquete el\u00e9ctrico Dongfeng TZ3Z 8x4: 55 t GVW, bater\u00eda CATL 400 kWh, motor LvKong 315/510 kW y eje HDZ300. Precio FOB y cotizaci\u00f3n en 24 h.",
   kw="Dongfeng TZ3Z, volquete el\u00e9ctrico 8x4, cami\u00f3n volquete el\u00e9ctrico 55 toneladas, TZ3Z precio, dump truck el\u00e9ctrico construcci\u00f3n",
   h1="Dongfeng TZ3Z \u2014 Volquete El\u00e9ctrico 8x4 (55 t)",
   sub="Volquete de construcci\u00f3n sobre chasis KC PRO D320KC con CATL 400 kWh, ideal para obra civil y residuos.",
   specs=[("Configuraci\u00f3n de ejes","8x4"),("Peso bruto vehicular (GVW)","55 t"),
          ("Bater\u00eda","CATL LFP 400 kWh"),("Motor el\u00e9ctrico","LvKong 315/510 kW"),
          ("Chasis","KC PRO D320KC, bastidor de alta resistencia"),("Eje trasero","HDZ300"),
          ("Carga r\u00e1pida","Doble pistola 600 A: 20\u201380% en ~40 min"),("Emisiones","Cero emisiones (BEV)")],
   body="El TZ3Z es el volquete el\u00e9ctrico 8x4 de Dongfeng para obra y movimiento de tierras. Monta el chasis KC PRO D320KC con bastidor reforzado y eje trasero HDZ300, y combina una bater\u00eda CATL de 400 kWh con el motor LvKong de 315/510 kW. Es la alternativa el\u00e9ctrica directa al volquete di\u00e9sel de 6x4/8x4 en entornos urbanos y periurbanos con restricciones de emisiones y ruido.",
   apps=["Obra civil urbana y residuos de construcci\u00f3n","Movimiento de tierras y áridos","Minas y canteras con recorridos cortos"],
   faqs=[("\u00bfCu\u00e1l es el precio FOB del Dongfeng TZ3Z?","Como referencia, los volquetes el\u00e9ctricos 8x4 de esta clase parten de USD 95.000 FOB China seg\u00fan bater\u00eda y equipamiento. Env\u00ede su pa\u00eds y aplicaci\u00f3n para una cotizaci\u00f3n FOB/CIF en 24 horas."),
         ("\u00bfCu\u00e1nto peso puede cargar?","El TZ3Z trabaja con 55 t de peso bruto vehicular. La carga \u00fatil depende del tipo de caja y de la densidad del material."),
         ("\u00bfQu\u00e9 diferencia hay con el TZ3V?","El TZ3V es la versi\u00f3n de grado minero de 80 t con bastidor 8+8+4 y bater\u00eda de 600 kWh; el TZ3Z de 55 t es m\u00e1s \u00e1gil y econ\u00f3mico para obra urbana.")],
 ),
 "kt5m": dict(
   es="es/products/models/kt5m-electric-cargo-truck.html", en="products/models/kt5m-electric-cargo-truck.html",
   title="Dongfeng KT5M Cami\u00f3n de Carga El\u00e9ctrico 4x2 65 m\u00b3 \u2014 Especificaciones",
   desc="Ficha del cami\u00f3n de carga el\u00e9ctrico Dongfeng KT5M 4x2: m\u00e1s de 65 m\u00b3, bater\u00eda CATL 262/310 kWh, eje motriz LvKong 150/270 kW y hasta 400 km de autonom\u00eda.",
   kw="Dongfeng KT5M, cami\u00f3n de carga el\u00e9ctrico 4x2, cami\u00f3n de caja el\u00e9ctrico, KT5M precio, cami\u00f3n el\u00e9ctrico distribuci\u00f3n urbana",
   h1="Dongfeng KT5M \u2014 Cami\u00f3n de Carga El\u00e9ctrico 4x2",
   sub="Cami\u00f3n de caja de m\u00e1s de 65 m\u00b3 con eje motriz el\u00e9ctrico y hasta 400 km de autonom\u00eda para distribuci\u00f3n urbana.",
   specs=[("Configuraci\u00f3n de ejes","4x2"),("Distancia entre ejes","7.150 mm"),
          ("Bater\u00eda","CATL LFP 262/310 kWh"),("Motor / eje motriz","LvKong 150/270 kW, eje el\u00e9ctrico"),
          ("Volumen de caja","M\u00e1s de 65 m\u00b3"),("Autonom\u00eda","Hasta 400 km"),
          ("Peso bruto vehicular","18 t"),("Emisiones","Cero emisiones (BEV)")],
   body="El KT5M es el cami\u00f3n de caja el\u00e9ctrico 4x2 de Dongfeng para distribuci\u00f3n urbana y regional. Usa el chasis KR D560e con 7.150 mm de distancia entre ejes y un eje motriz el\u00e9ctrico LvKong de 150/270 kW que elimina el \u00e1rbol de transmisi\u00f3n tradicional. Con m\u00e1s de 65 m\u00b3 de volumen y bater\u00edas CATL de 262 a 310 kWh, cubre rutas de reparto diarias sin recarga intermedia en la mayor\u00eda de las ciudades.",
   apps=["Distribuci\u00f3n urbana de mercanc\u00edas","Reparto regional de corto y medio recorrido","Log\u00edstica de almac\u00e9n y \u00faltima milla"],
   faqs=[("\u00bfCu\u00e1l es el precio FOB del Dongfeng KT5M?","Como referencia, los camiones de caja el\u00e9ctricos 4x2 de esta clase parten de USD 45.000 FOB China con bater\u00eda de 262 kWh. Indique su ruta y tonelaje para una cotizaci\u00f3n exacta FOB/CIF en 24 horas."),
         ("\u00bfCu\u00e1nta autonom\u00eda real ofrece?","El KT5M cubre 200\u2013280 km con paquetes de 262\u2013310 kWh y hasta 400 km en condiciones favorables. En rutas planas, el consumo puede bajar de 8% de bater\u00eda por 100 km."),
         ("\u00bfSe puede cargar en un enchufe trif\u00e1sico normal?","Admite carga AC de dep\u00f3sito durante la noche y carga r\u00e1pida DC para cargas de oportunidad. Confirmamos el est\u00e1ndar (CCS2, GB/T u otro) seg\u00fan su pa\u00eds.")],
 ),
}

def model_body(m):
    b = [main_open()]
    b.append('<div class="section-title"><h2>' + m["h1"] + '</h2></div>\n')
    b.append('<p style="font-size:16px;line-height:1.8;max-width:900px;">' + m["body"] + '</p>\n')
    b.append('<div class="section-title" style="margin-top:28px;"><h2>Especificaciones principales</h2></div>\n<table class="spec-tbl">\n')
    for k, v in m["specs"]:
        b.append('  <tr><td>' + k + '</td><td>' + v + '</td></tr>\n')
    b.append('</table>\n')
    b.append('<div class="section-title" style="margin-top:28px;"><h2>Aplicaciones recomendadas</h2></div>\n<ul class="tick">\n')
    for a in m["apps"]:
        b.append('  <li>' + a + '</li>\n')
    b.append('</ul>\n')
    b.append('<p style="margin-top:20px;font-size:14px;color:#555;">Ficha completa, video de operaci\u00f3n y pedidos de referencia disponibles a solicitud. Escriba a <a href="' + WA_LINK + '" target="_blank" rel="noopener" style="color:var(--primary);font-weight:700;">WhatsApp +86 15319431311</a> o a sales@fenghan-trade.com.</p>\n')
    b.append(faq_html_es(m["faqs"], "Preguntas frecuentes"))
    b.append(main_close())
    b.append(cta_band_es("Pida la cotizaci\u00f3n de este modelo",
                         "Ficha t\u00e9cnica, precio FOB/CIF y opciones de financiamiento en 24 horas."))
    return "\n".join(b)

# ============================================================ MARKETS
MARKETS = [
 dict(slug="dominican-republic", country="Rep\u00fablica Dominicana", region="Caribe", port="R\u00edo Haina / Caucedo",
      why="Las redes de distribuci\u00f3n de Santo Domingo y la log\u00edstica hotelera de Punta Cana encajan con flotas el\u00e9ctricas compactas de autonom\u00eda insular. Fenghan Trading, exportador autorizado de nueva energ\u00eda Dongfeng con sede en Xi'an (China), configura cada cami\u00f3n para Rep\u00fablica Dominicana: tama\u00f1o de bater\u00eda, est\u00e1ndar de carga, paquete clim\u00e1tico y direcci\u00f3n a la izquierda (LHD).",
      models=[("KT5M","Cami\u00f3n de Carga El\u00e9ctrico","4\u00d72 \u00b7 18 t GVW \u00b7 CATL 262/310 kWh LFP"),
              ("KT5J","Cami\u00f3n de Carga El\u00e9ctrico","4\u00d72 \u00b7 18 t GVW \u00b7 CATL 262/310 kWh LFP"),
              ("KT3F","Veh\u00edculo Especial El\u00e9ctrico","4\u00d72 \u00b7 18 t GVW \u00b7 CATL 166/200 kWh LFP")],
      notes=["Direcci\u00f3n: LHD (volante a la izquierda)","Puerto de llegada: R\u00edo Haina / Caucedo",
             "Tr\u00e1nsito mar\u00edtimo desde China: 35\u201342 d\u00edas",
             "Ciclos insulares (menos de 150 km/d\u00eda): la carga AC nocturna en dep\u00f3sito suele ser suficiente",
             "Documentos incluidos: B/L, factura comercial, lista de empaque, certificado de origen y papeles de homologaci\u00f3n",
             "Asesor\u00eda de carga, apoyo en estudio de sitio y capacitaci\u00f3n de conductores para pedidos de flota (5+ unidades)"],
      faqs=[("\u00bfCu\u00e1nto cuesta un cami\u00f3n el\u00e9ctrico Dongfeng en Rep\u00fablica Dominicana?","El precio depende del modelo, la bater\u00eda y las opciones. Como referencia, los precios FOB China para el rango recomendado en Rep\u00fablica Dominicana van de USD 45.000 (carga de 18 t) a m\u00e1s de USD 120.000 (tractocami\u00f3n pesado de miner\u00eda). Cotizamos FOB y CIF R\u00edo Haina / Caucedo en 24 horas."),
            ("\u00bfLos camiones el\u00e9ctricos Dongfeng resisten las carreteras y el clima dominicanos?","S\u00ed. Los camiones para Rep\u00fablica Dominicana se configuran seg\u00fan las condiciones locales: los ciclos insulares (menos de 150 km/d\u00eda) permiten que la carga AC nocturna sea suficiente. Todas las unidades de exportaci\u00f3n superan 12.500 km de pruebas de fiabilidad y est\u00e1n validadas de -20\u00b0C a +50\u00b0C."),
            ("\u00bfC\u00f3mo se env\u00edan los camiones y cu\u00e1nto tardan?","Las unidades se env\u00edan en RoRo o contenedor flat-rack a R\u00edo Haina / Caucedo. El tr\u00e1nsito t\u00edpico desde China es de 35\u201342 d\u00edas. Nosotros gestionamos la exportaci\u00f3n y su agente local el despacho de importaci\u00f3n con los documentos que entregamos (B/L, certificado de origen, papeles de homologaci\u00f3n).")]),
 dict(slug="chile", country="Chile", region="Sudam\u00e9rica", port="San Antonio / Valpara\u00edso",
      why="La miner\u00eda del cobre y la construcci\u00f3n chilenas son el escenario ideal para volquetes y tractocamiones el\u00e9ctricos de gran capacidad. Configuramos las unidades para altura, polvo y ciclos de mina, con paquetes CATL de 400 a 600 kWh y bastidores reforzados.",
      models=[("TZ3V","Volquete El\u00e9ctrico","8\u00d74 \u00b7 80 t GVW \u00b7 CATL 600 kWh"),
              ("TZ3Z","Volquete El\u00e9ctrico","8\u00d74 \u00b7 55 t GVW \u00b7 CATL 400 kWh"),
              ("TE8M","Tractocami\u00f3n El\u00e9ctrico","6\u00d74 \u00b7 80 t GCW \u00b7 CATL 466\u2013600 kWh")],
      notes=["Direcci\u00f3n: LHD (volante a la izquierda)","Puerto de llegada: San Antonio / Valpara\u00edso",
             "Tr\u00e1nsito mar\u00edtimo desde China: 35\u201345 d\u00edas",
             "Configuraci\u00f3n para miner\u00eda: protecci\u00f3n contra polvo y paquete de altura para faenas sobre 2.500 m",
             "Documentos incluidos: B/L, factura comercial, lista de empaque, certificado de origen y papeles de homologaci\u00f3n",
             "Capacitaci\u00f3n de conductores y asesor\u00eda de carga para pedidos de flota"],
      faqs=[("\u00bfQu\u00e9 cami\u00f3n el\u00e9ctrico conviene para la miner\u00eda en Chile?","Para faenas de cobre y canteras, el TZ3V 8x4 de 80 t con bater\u00eda CATL de 600 kWh y bastidor 8+8+4 es la opci\u00f3n de mayor capacidad; el TZ3Z de 55 t cubre obra y movimiento de tierras con menor inversi\u00f3n."),
            ("\u00bfC\u00f3mo se comportan las bater\u00edas en altura y con polvo?","Los paquetes CATL LFP llevan gesti\u00f3n t\u00e9rmica HD y est\u00e1n validados de -20\u00b0C a +50\u00b0C. Para altura ofrecemos paquete de compensaci\u00f3n y protecci\u00f3n reforzada contra polvo en mina."),
            ("\u00bfCu\u00e1nto tarda la entrega a Chile?","Tras confirmar la configuraci\u00f3n, el plazo de producci\u00f3n es de 20\u201325 d\u00edas y el tr\u00e1nsito mar\u00edtimo a San Antonio / Valpara\u00edso de 35\u201345 d\u00edas.")]),
 dict(slug="peru", country="Per\u00fa", region="Sudam\u00e9rica", port="Callao",
      why="Per\u00fa combina miner\u00eda, construcci\u00f3n y una creciente log\u00edstica urbana en Lima. Ofrecemos volquetes el\u00e9ctricos para faena y camiones de carga para distribuci\u00f3n, con configuraci\u00f3n para altura y climas costeros h\u00famedos.",
      models=[("TZ3Z","Volquete El\u00e9ctrico","8\u00d74 \u00b7 55 t GVW \u00b7 CATL 400 kWh"),
              ("KTA1","Volquete El\u00e9ctrico","8\u00d74 \u00b7 31 t GVW \u00b7 CATL 352 kWh"),
              ("KT5M","Cami\u00f3n de Carga El\u00e9ctrico","4\u00d72 \u00b7 65 m\u00b3 \u00b7 CATL 262/310 kWh")],
      notes=["Direcci\u00f3n: LHD (volante a la izquierda)","Puerto de llegada: Callao",
             "Tr\u00e1nsito mar\u00edtimo desde China: 35\u201345 d\u00edas",
             "Configuraci\u00f3n para miner\u00eda en altura y protecci\u00f3n anticorrosi\u00f3n para clima costero",
             "Documentos incluidos: B/L, factura comercial, lista de empaque, certificado de origen y papeles de homologaci\u00f3n",
             "Repuestos y soporte posventa a trav\u00e9s de nuestra red regional"],
      faqs=[("\u00bfQu\u00e9 modelos se recomiendan para Per\u00fa?","Para miner\u00eda y canteras recomendamos el TZ3Z 8x4 de 55 t; para residuos de construcci\u00f3n urbana el KTA1 de 31 t; y para distribuci\u00f3n el KT5M de caja con m\u00e1s de 65 m\u00b3."),
            ("\u00bfHay soporte posventa en Per\u00fa?","S\u00ed. Entregamos repuestos, documentaci\u00f3n t\u00e9cnica y capacitaci\u00f3n, y coordinamos servicio con nuestra red regional y con el distribuidor local."),
            ("\u00bfQu\u00e9 documentaci\u00f3n necesito para importar?","Le entregamos B/L, factura comercial, lista de empaque, certificado de origen y papeles de homologaci\u00f3n; su agente aduanero local gestiona el despacho.")]),
 dict(slug="colombia", country="Colombia", region="Sudam\u00e9rica", port="Buenaventura",
      why="Colombia avanza en la electrificaci\u00f3n del transporte urbano y de carga. Nuestros camiones de caja y volquetes el\u00e9ctricos reducen costo por kil\u00f3metro en reparto urbano y obra, con configuraci\u00f3n para altura en el interior andino.",
      models=[("TZ3Z","Volquete El\u00e9ctrico","8\u00d74 \u00b7 55 t GVW \u00b7 CATL 400 kWh"),
              ("KT5M","Cami\u00f3n de Carga El\u00e9ctrico","4\u00d72 \u00b7 65 m\u00b3 \u00b7 CATL 262/310 kWh"),
              ("KT3E","Veh\u00edculo Especial El\u00e9ctrico","4\u00d72 \u00b7 Residuos \u00b7 CATL 232\u2013252 kWh")],
      notes=["Direcci\u00f3n: LHD (volante a la izquierda)","Puerto de llegada: Buenaventura",
             "Tr\u00e1nsito mar\u00edtimo desde China: 40\u201350 d\u00edas (Pac\u00edfico)",
             "Configuraci\u00f3n para altura en el interior andino y para operaci\u00f3n urbana en ciudades principales",
             "Documentos incluidos: B/L, factura comercial, lista de empaque, certificado de origen y papeles de homologaci\u00f3n",
             "Asesor\u00eda de carga y capacitaci\u00f3n para pedidos de flota (5+ unidades)"],
      faqs=[("\u00bfQu\u00e9 cami\u00f3n el\u00e9ctrico conviene para el reparto urbano en Colombia?","Para reparto urbano, el KT5M de caja con m\u00e1s de 65 m\u00b3 y bater\u00eda CATL de 262 a 310 kWh ofrece el mejor costo por kil\u00f3metro; para obra y \u00e1ridos, el TZ3Z 8x4 de 55 t."),
            ("\u00bfFuncionan las bater\u00edas en altura?","S\u00ed. Los paquetes CATL LFP con gesti\u00f3n t\u00e9rmica HD est\u00e1n validados de -20\u00b0C a +50\u00b0C y ofrecemos paquete de altitud para el interior andino."),
            ("\u00bfCu\u00e1nto tarda el env\u00edo a Buenaventura?","El tr\u00e1nsito t\u00edpico desde China es de 40\u201350 d\u00edas, m\u00e1s 20\u201325 d\u00edas de producci\u00f3n seg\u00fan configuraci\u00f3n.")]),
 dict(slug="mexico", country="M\u00e9xico", region="Latinoam\u00e9rica", port="Manzanillo / Veracruz",
      why="M\u00e9xico es una potencia manufacturera y log\u00edstica: los tractocamiones y camiones de caja el\u00e9ctricos reducen costos en corredores industriales, mientras las hormigoneras y cisternas el\u00e9ctricas sirven a la construcci\u00f3n urbana.",
      models=[("TE8L","Tractocami\u00f3n El\u00e9ctrico","6\u00d74 \u00b7 49 t GCW \u00b7 CATL 400\u2013600 kWh"),
              ("KT5M","Cami\u00f3n de Carga El\u00e9ctrico","4\u00d72 \u00b7 65 m\u00b3 \u00b7 CATL 262/310 kWh"),
              ("TZ8J","Veh\u00edculo Especial El\u00e9ctrico","8\u00d74 \u00b7 44\u201345 t \u00b7 Hormigonera \u00b7 CATL 333 kWh")],
      notes=["Direcci\u00f3n: LHD (volante a la izquierda)","Puerto de llegada: Manzanillo / Veracruz",
             "Tr\u00e1nsito mar\u00edtimo desde China: 30\u201340 d\u00edas",
             "Configuraci\u00f3n para corredores industriales y clima c\u00e1lido en costa y baj\u00edo",
             "Documentos incluidos: B/L, factura comercial, lista de empaque, certificado de origen y papeles de homologaci\u00f3n",
             "Soporte de repuestos y capacitaci\u00f3n de conductores para pedidos de flota"],
      faqs=[("\u00bfQu\u00e9 tractor el\u00e9ctrico conviene para corredores industriales en M\u00e9xico?","El TE8L 6x4 de 49 t GCW con bater\u00eda CATL de 400 a 600 kWh es el tractocami\u00f3n m\u00e1s adecuado para corredores industriales y transporte de larga distancia."),
            ("\u00bfSe puede usar una hormigonera el\u00e9ctrica en obra urbana?","S\u00ed. El TZ8J 8x4 de 44\u201345 t con CATL 333 kWh y propulsi\u00f3n LvKong de 350/520 kW es silencioso y sin emisiones, ideal para obra en ciudad."),
            ("\u00bfCu\u00e1nto tarda la entrega a M\u00e9xico?","El tr\u00e1nsito t\u00edpico desde China a Manzanillo o Veracruz es de 30\u201340 d\u00edas, m\u00e1s 20\u201325 d\u00edas de producci\u00f3n.")]),
]

def market_body(m):
    b = [main_open()]
    b.append('<p style="font-size:16px;line-height:1.8;max-width:900px;">' + m["why"] + '</p>\n')
    b.append('<div class="section-title" style="margin-top:28px;"><h2>Recomendado para ' + m["country"] + '</h2></div>\n')
    for name, kind, spec in m["models"]:
        b.append('<div class="prod-card">\n  <h3 style="margin:0 0 6px;">Dongfeng ' + name +
                 ' <span style="font-size:13px;color:#666;font-weight:400;">\u00b7 ' + kind + '</span></h3>\n'
                 '  <p style="margin:0;font-size:14px;color:#444;">' + spec + '</p>\n</div>\n')
    b.append('<div class="section-title" style="margin-top:28px;"><h2>Notas de importaci\u00f3n y carga \u2014 ' + m["country"] + '</h2></div>\n<ul class="tick">\n')
    for n in m["notes"]:
        b.append('  <li>' + n + '</li>\n')
    b.append('</ul>\n')
    b.append(faq_html_es(m["faqs"], "Preguntas frecuentes \u2014 " + m["country"]))
    b.append(main_close())
    b.append(cta_band_es("Inicie su cotizaci\u00f3n de flota el\u00e9ctrica para " + m["country"],
                         "Cotizaci\u00f3n FOB / CIF en 24 horas. Ficha t\u00e9cnica, video y pedidos de referencia a solicitud."))
    return "\n".join(b)

# ============================================================ ABOUT / CONTACT
ABOUT_FAQ = [
 ("\u00bfQui\u00e9n es Shaanxi Fenghan Trading?","Shaanxi Fenghan Trading Co., Ltd es una empresa exportadora de veh\u00edculos comerciales con sede en Xi'an, Shaanxi (China), exportador autorizado de camiones de nueva energ\u00eda Dongfeng y camiones pesados SAGMOTO (SHACMAN), que sirve a m\u00e1s de 50 pa\u00edses."),
 ("\u00bfEs Fenghan Trading exportador autorizado de Dongfeng EV?","S\u00ed. La empresa es socio exportador autorizado de veh\u00edculos comerciales de nueva energ\u00eda Dongfeng y suministra toda la gama de tractocamiones TE, volquetes TZ, camiones KT y veh\u00edculos especiales con t\u00e9rminos de garant\u00eda de f\u00e1brica."),
 ("\u00bfQu\u00e9 mercados atiende la empresa?","Los mercados de exportaci\u00f3n incluyen \u00c1frica Occidental y Oriental, el Golfo (Medio Oriente), el Sudeste Asi\u00e1tico, Asia Central, Am\u00e9rica Latina y Europa, con soporte de documentaci\u00f3n y certificaci\u00f3n para cada destino."),
 ("\u00bfCu\u00e1les son las condiciones de pago y env\u00edo?","30% de anticipo por T/T y 70% antes del embarque o contra copia del B/L. El 90% de los env\u00edos son mar\u00edtimos, en contenedor, RoRo o granelero."),
]

def about_body():
    b = [main_open()]
    b.append('<div class="breadcrumb"><a href="/es/">Inicio</a> &rsaquo; Nosotros</div>\n')
    b.append('<div class="section-title"><h2>Sobre Dongfeng Vehicle Export</h2></div>\n')
    b.append('<p class="section-sub">Shaanxi Fenghan Trading Co., Ltd \u2014 su socio autorizado para veh\u00edculos comerciales de nueva energ\u00eda Dongfeng.</p>\n')
    b.append('''<div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(280px,1fr)); gap:32px; margin-top:32px;">
  <div>
    <h3 style="font-size:22px; margin-bottom:12px;">Resumen de la empresa</h3>
    <p style="color:var(--muted); margin-bottom:16px;">Fundada en Xi'an, provincia de Shaanxi, somos una empresa comercial exportadora autorizada especializada en veh\u00edculos comerciales de nueva energ\u00eda Dongfeng. Integramos desarrollo de producto para mercados exteriores, venta de veh\u00edculos completos y repuestos, garant\u00eda posventa y soluciones financieras.</p>
    <p style="color:var(--muted); margin-bottom:16px;">Nuestro negocio comenz\u00f3 con el servicio posventa en el exterior. Gracias a la integridad y a un soporte excelente, hemos ganado una gran reputaci\u00f3n entre empresas chinas en el extranjero y operadores de flotas locales. Hoy promovemos Dongfeng Commercial Vehicles, Dongfeng Xinjiang, Dongfeng Liuzhou y Dongfeng New Energy Vehicles en \u00c1frica, Sudam\u00e9rica, Medio Oriente y Europa.</p>
    <p style="color:var(--muted);">Con un volumen de ventas anual superior a 1.000 unidades y un equipo de m\u00e1s de 50 personas (incluidas m\u00e1s de 30 en nuestra filial de Nigeria), ofrecemos soporte localizado desde la consulta hasta la entrega.</p>
  </div>
  <div>
    <h3 style="font-size:22px; margin-bottom:12px;">Nuestras ventajas</h3>
    <ul style="color:var(--muted); line-height:2; padding-left:20px;">
      <li><strong>Productos de alta calidad</strong> adaptados a las normas locales de emisiones y carretera</li>
      <li><strong>Financiamiento flexible</strong> \u2014 T/T 30% de anticipo + 70% antes del embarque o contra B/L</li>
      <li><strong>Log\u00edstica profesional</strong> \u2014 90% por v\u00eda mar\u00edtima: contenedor, RoRo o granelero</li>
      <li><strong>Garant\u00eda posventa</strong> \u2014 soporte de I+D, centros de repuestos y diagn\u00f3stico remoto</li>
      <li><strong>Personalizaci\u00f3n</strong> \u2014 RHD, pintura, tipo de carrocer\u00eda, capacidad de bater\u00eda y est\u00e1ndar de carga</li>
    </ul>
  </div>
</div>
<div style="margin-top:48px; display:grid; grid-template-columns: repeat(auto-fit, minmax(200px,1fr)); gap:24px; text-align:center;">
  <div style="padding:24px; background:var(--bg); border-radius:var(--radius);"><div style="font-size:36px; font-weight:800; color:var(--accent);">20+</div><div style="color:var(--muted); font-size:14px;">A\u00f1os de experiencia exportadora</div></div>
  <div style="padding:24px; background:var(--bg); border-radius:var(--radius);"><div style="font-size:36px; font-weight:800; color:var(--accent);">60+</div><div style="color:var(--muted); font-size:14px;">Pa\u00edses con red de servicio</div></div>
  <div style="padding:24px; background:var(--bg); border-radius:var(--radius);"><div style="font-size:36px; font-weight:800; color:var(--accent);">1.000+</div><div style="color:var(--muted); font-size:14px;">Unidades vendidas al a\u00f1o</div></div>
  <div style="padding:24px; background:var(--bg); border-radius:var(--radius);"><div style="font-size:36px; font-weight:800; color:var(--accent);">10</div><div style="color:var(--muted); font-size:14px;">Centros de repuestos en el exterior</div></div>
</div>
<div class="section-title" style="margin-top:40px;"><h2>Autorizaciones y datos fiscales</h2></div>
<table class="spec-tbl">
  <tr><td>Raz\u00f3n social</td><td>Shaanxi Fenghan Trading Co., Ltd (\u9655\u897f\u98ce\u6d69\u8d38\u6613\u6709\u9650\u516c\u53f8)</td></tr>
  <tr><td>Autorizaci\u00f3n SAGMOTO</td><td>SAG-2025-201 (\u9655\u6c7d\u5546\u7528\u8f66 / SAGMOTO), vigente 2025.01\u20132026.12</td></tr>
  <tr><td>Autorizaci\u00f3n SHACMAN</td><td>SQIDACN 28 (\u9655\u897f\u91cd\u6c7d\u8fdb\u51fa\u53e3 / Shaanxi Heavy Duty Automobile Import & Export), vigente 2026.06\u20132027.06</td></tr>
  <tr><td>C\u00f3digo USCC</td><td>91610104MACWWH682Q</td></tr>
  <tr><td>Constituci\u00f3n</td><td>29 de agosto de 2023</td></tr>
  <tr><td>Domicilio</td><td>Room 603A, Floor 6, Building B, Chanba Free Trade Center, Xi'an, Shaanxi 710000, China</td></tr>
</table>
''')
    b.append(faq_html_es(ABOUT_FAQ, "Preguntas frecuentes"))
    b.append(main_close())
    b.append(cta_band_es("Hable con un exportador autorizado",
                         "Somos su socio directo de f\u00e1brica en China para camiones el\u00e9ctricos Dongfeng. Respuesta en 24 horas."))
    return "\n".join(b)

def contact_body():
    b = [main_open()]
    b.append('<div class="breadcrumb"><a href="/es/">Inicio</a> &rsaquo; Contacto</div>\n')
    b.append('<div class="section-title"><h2>Cont\u00e1ctenos</h2></div>\n')
    b.append('<p class="section-sub">Envie su pa\u00eds, aplicaci\u00f3n, carga y cantidad \u2014 le respondemos con una cotizaci\u00f3n FOB/CIF en 24 horas.</p>\n')
    b.append('''<div style="display:grid; grid-template-columns: repeat(auto-fit, minmax(260px,1fr)); gap:28px; margin-top:24px;">
  <div style="padding:24px; background:var(--bg); border-radius:var(--radius);">
    <h3 style="font-size:19px; margin-bottom:10px;">WhatsApp / Tel\u00e9fono</h3>
    <p style="color:var(--muted);">+86 153 1943 1311</p>
    <p style="margin-top:10px;"><a class="btn btn-primary" href="''' + WA_LINK + '''" target="_blank" rel="noopener">Escribir por WhatsApp</a></p>
  </div>
  <div style="padding:24px; background:var(--bg); border-radius:var(--radius);">
    <h3 style="font-size:19px; margin-bottom:10px;">Email</h3>
    <p style="color:var(--muted);">sales@fenghan-trade.com</p>
  </div>
  <div style="padding:24px; background:var(--bg); border-radius:var(--radius);">
    <h3 style="font-size:19px; margin-bottom:10px;">Direcci\u00f3n</h3>
    <p style="color:var(--muted);">Room 603A, Floor 6, Building B,<br>Chanba Free Trade Center,<br>Xi'an, Shaanxi 710000, China</p>
  </div>
</div>
<div class="section-title" style="margin-top:36px;"><h2>Qu\u00e9 incluir en su consulta</h2></div>
<ul class="tick">
  <li>Pa\u00eds de destino y puerto de llegada</li>
  <li>Tipo de cami\u00f3n (tractocami\u00f3n, volquete, carga o especial) y aplicaci\u00f3n</li>
  <li>Carga \u00fatil o peso bruto requerido y longitud de ruta diaria</li>
  <li>Cantidad de unidades y si hay requisito de volante a la derecha (RHD)</li>
  <li>Est\u00e1ndar de carga preferido (CCS2, GB/T u otro), si lo conoce</li>
</ul>
''')
    b.append(main_close())
    b.append(cta_band_es("Cotizaci\u00f3n en 24 horas",
                         "FOB / CIF, ficha t\u00e9cnica, video de operaci\u00f3n y pedidos de referencia disponibles a solicitud."))
    return "\n".join(b)

def markets_index_body():
    b = [main_open()]
    b.append('<p style="font-size:16px;line-height:1.8;max-width:900px;">Gu\u00edas por pa\u00eds en espa\u00f1ol: modelos recomendados, puertos de llegada, lado de conducci\u00f3n, tiempos de tr\u00e1nsito y notas de importaci\u00f3n. Exportamos a m\u00e1s de 60 pa\u00edses; estas son nuestras gu\u00edas para Am\u00e9rica Latina y el Caribe.</p>\n')
    b.append('<ul style="list-style:none;padding:0;columns:2;column-gap:48px;">\n')
    for m in MARKETS:
        b.append('<li style="margin:6px 0;"><a href="' + m["slug"] + '.html" style="color:var(--primary);font-weight:600;">Camiones el\u00e9ctricos para ' + m["country"] + '</a> <span style="color:#777;font-size:13px;">\u00b7 ' + m["region"] + ' \u00b7 ' + m["port"] + '</span></li>\n')
    b.append('</ul>\n')
    b.append('<p style="margin-top:24px;color:var(--muted);">\u00bfSu pa\u00eds no aparece? Enviamos a m\u00e1s de 60 pa\u00edses: escr\u00edbanos y confirmamos homologaci\u00f3n, puerto y est\u00e1ndar de carga.</p>\n')
    b.append(main_close())
    b.append(cta_band_es("\u00bfSu mercado no est\u00e1 en la lista? Enviamos a m\u00e1s de 60 pa\u00edses",
                         "Cotizaci\u00f3n FOB / CIF en 24 horas. Ficha t\u00e9cnica, video y pedidos de referencia a solicitud."))
    return "\n".join(b)

# ============================================================ RUN
PAGES = []          # (es_rel, en_rel, html)

def build():
    # HOME
    PAGES.append(("es/index.html", "index.html",
        page("es/index.html", "index.html",
             "Camiones El\u00e9ctricos Dongfeng para Exportaci\u00f3n | Fenghan Trading",
             "Exportador autorizado de camiones el\u00e9ctricos Dongfeng: tractocamiones, volquetes, camiones de carga y veh\u00edculos especiales con bater\u00edas CATL. Env\u00edos a m\u00e1s de 60 pa\u00edses.",
             "camiones el\u00e9ctricos, cami\u00f3n el\u00e9ctrico Dongfeng, tractocami\u00f3n el\u00e9ctrico, volquete el\u00e9ctrico, cami\u00f3n de carga el\u00e9ctrico, exportaci\u00f3n camiones el\u00e9ctricos China, bater\u00eda CATL",
             home_body(),
             extra_schema=faq_schema_es(HOME_FAQ), active="/es/")))
    # CATEGORIES
    for key, c in CATS.items():
        PAGES.append((c["es"], c["en"],
            page(c["es"], c["en"], c["title"], c["desc"], c["kw"],
                 hero_sm('<a href="/es/">Inicio</a> &rsaquo; Productos', c["h1"], c["sub"])
                 + cat_body(c),
                 extra_schema=faq_schema_es(c["faqs"]), active="/" + c["es"])))
    # MODELS
    MODEL_CAT = {"te46": "electric-tractor", "tz3z": "electric-dump", "kt5m": "electric-cargo"}
    for key, m in MODELS.items():
        cat = MODEL_CAT[key]
        PAGES.append((m["es"], m["en"],
            page(m["es"], m["en"], m["title"], m["desc"], m["kw"],
                 hero_sm('<a href="/es/">Inicio</a> &rsaquo; <a href="/es/products/' + cat + '.html">Productos</a>', m["h1"], m["sub"])
                 + model_body(m),
                 extra_schema=faq_schema_es(m["faqs"]), active="/es/products/" + cat + ".html")))
    # MARKETS
    PAGES.append(("es/markets/index.html", "markets/index.html",
        page("es/markets/index.html", "markets/index.html",
             "Mercados \u2014 Camiones El\u00e9ctricos Dongfeng para Am\u00e9rica Latina y el Caribe",
             "Gu\u00edas por pa\u00eds de camiones el\u00e9ctricos Dongfeng: modelos recomendados, puertos, lado de conducci\u00f3n y tiempos de tr\u00e1nsito para Am\u00e9rica Latina y el Caribe.",
             "camiones el\u00e9ctricos por pa\u00eds, cami\u00f3n el\u00e9ctrico Am\u00e9rica Latina, cami\u00f3n el\u00e9ctrico Caribe, exportaci\u00f3n cami\u00f3n el\u00e9ctrico",
             hero_sm('<a href="/es/">Inicio</a> &rsaquo; Mercados', "Mercados que atendemos",
                     "Gu\u00edas pa\u00eds por pa\u00eds: modelos recomendados, puertos, lado de conducci\u00f3n, tr\u00e1nsitos y notas de importaci\u00f3n.")
             + markets_index_body(), active="/es/markets/index.html")))
    for m in MARKETS:
        es_rel = "es/markets/" + m["slug"] + ".html"
        en_rel = "markets/" + m["slug"] + ".html"
        PAGES.append((es_rel, en_rel,
            page(es_rel, en_rel,
                 "Camiones El\u00e9ctricos Dongfeng para " + m["country"] + " \u2014 Exportaci\u00f3n | Fenghan",
                 "Camiones el\u00e9ctricos Dongfeng para " + m["country"] + ": tractocamiones, volquetes, camiones de carga y veh\u00edculos municipales. Env\u00edo a " + m["port"] + ". Cotizaci\u00f3n FOB/CIF en 24 h.",
                 "cami\u00f3n el\u00e9ctrico " + m["country"] + ", camiones el\u00e9ctricos " + m["country"] + ", volquete el\u00e9ctrico " + m["country"] + ", importar cami\u00f3n el\u00e9ctrico " + m["country"],
                 hero_sm('<a href="/es/">Inicio</a> &rsaquo; <a href="/es/markets/index.html">Mercados</a> &rsaquo; ' + m["country"],
                         "Camiones El\u00e9ctricos para " + m["country"],
                         m["region"] + " \u00b7 Puerto " + m["port"] + " \u00b7 LHD")
                 + market_body(m),
                 extra_schema=faq_schema_es(m["faqs"]), active="/es/markets/index.html")))
    # ABOUT / CONTACT
    PAGES.append(("es/about-us.html", "about-us.html",
        page("es/about-us.html", "about-us.html",
             "Nosotros \u2014 Exportador Autorizado de Camiones Dongfeng EV | Fenghan Trading",
             "Shaanxi Fenghan Trading Co., Ltd: exportador autorizado de camiones de nueva energ\u00eda Dongfeng y camiones pesados SAGMOTO (SHACMAN) con sede en Xi'an, China. 60+ pa\u00edses y m\u00e1s de 1.000 unidades al a\u00f1o.",
             "exportador autorizado camiones Dongfeng, Shaanxi Fenghan Trading, exportaci\u00f3n camiones China, SAGMOTO SHACMAN exportador",
             about_body(), extra_schema=faq_schema_es(ABOUT_FAQ), active="/es/about-us.html")))
    PAGES.append(("es/contact-us.html", "contact-us.html",
        page("es/contact-us.html", "contact-us.html",
             "Contacto \u2014 Cotizaci\u00f3n de Camiones El\u00e9ctricos Dongfeng | Fenghan Trading",
             "Contacte a Shaanxi Fenghan Trading para su cotizaci\u00f3n de camiones el\u00e9ctricos Dongfeng. Respuesta en 24 horas por WhatsApp +86 153 1943 1311 o sales@fenghan-trade.com.",
             "contacto camiones el\u00e9ctricos Dongfeng, cotizaci\u00f3n cami\u00f3n el\u00e9ctrico, precio cami\u00f3n el\u00e9ctrico China",
             contact_body(), active="/es/contact-us.html")))

def patch_en():
    """Anade hreflang es + selector de idioma a las paginas EN correspondientes."""
    pairs = {}
    for es_rel, en_rel, _ in PAGES:
        pairs[en_rel] = es_rel
    for en_rel, es_rel in pairs.items():
        p = os.path.join(BASE, en_rel)
        if not os.path.exists(p):
            print("  ! EN no encontrada:", en_rel); continue
        with io.open(p, "r", encoding="utf-8") as f:
            h = f.read()
        orig = h
        en_url = SITE + "/" + en_rel
        es_url = SITE + "/" + es_rel
        if en_rel == "index.html":
            en_url = SITE + "/"
        if es_rel == "es/index.html":
            es_url = SITE + "/es/"
        # 0) fix pre-existing bug: about/contact canonical apuntaba al home
        if en_rel in ("about-us.html", "contact-us.html"):
            h = h.replace('<link rel="canonical" href="' + SITE + '/">',
                          '<link rel="canonical" href="' + en_url + '">', 1)
        # 1) limpiar hreflang previos
        h = re.sub(r'\n<link rel="alternate" hreflang="[^"]*" href="[^"]*">', '', h)
        # 2) insertar bloque hreflang tras canonical
        block = ('\n<link rel="alternate" hreflang="en" href="%s">'
                 '\n<link rel="alternate" hreflang="es" href="%s">'
                 '\n<link rel="alternate" hreflang="x-default" href="%s">' % (en_url, es_url, en_url))
        h2, n = re.subn(r'(<link rel="canonical" href="[^"]*">)', r'\1' + block, h, count=1)
        if n:
            h = h2
        else:
            print("    ? canonical no hallado en", en_rel)
        # 3) selector de idioma en el nav (una vez)
        if 'class="lang-switch"' not in h:
            h = h.replace('</nav>', '<li class="lang-switch"><a href="/%s" hreflang="es" lang="es">ES</a></li>\n</nav>' % es_rel, 1)
        if h != orig:
            with io.open(p, "w", encoding="utf-8", newline="\n") as f:
                f.write(h)
            print("  patched EN:", en_rel)
    # 4) CSS + robots + sitemap
    css = os.path.join(BASE, "css", "dongfeng-ev.css")
    with io.open(css, "r", encoding="utf-8") as f:
        c = f.read()
    if ".lang-switch" not in c:
        c += ("\n/* Language switcher (ES pilot) */\n"
              ".lang-switch a { font-weight: 800; color: var(--primary); }\n"
              ".main-nav li.on > a { color: var(--primary); }\n")
        with io.open(css, "w", encoding="utf-8", newline="\n") as f:
            f.write(c)
        print("  patched css/dongfeng-ev.css")
    # 5) sitemap: anadir namespace xhtml + URLs es
    sm = os.path.join(BASE, "sitemap.xml")
    with io.open(sm, "r", encoding="utf-8") as f:
        s = f.read()
    s_orig = s
    if 'xmlns:xhtml' not in s:
        s = s.replace('<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
                      '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9" '
                      'xmlns:xhtml="http://www.w3.org/1999/xhtml">', 1)
    # normalizar home es a forma de directorio
    s = s.replace('<loc>' + SITE + '/es/index.html</loc>', '<loc>' + SITE + '/es/</loc>')
    s = s.replace(SITE + '/es/index.html"', SITE + '/es/"')
    add = []
    for es_rel, en_rel, _ in PAGES:
        es_url = SITE + "/" + es_rel
        en_url = SITE + "/" + en_rel
        if es_rel == "es/index.html":
            es_url = SITE + "/es/"
        if en_rel == "index.html":
            en_url = SITE + "/"
        if "<loc>" + es_url + "</loc>" in s:
            continue
        add.append('  <url><loc>%s</loc><lastmod>%s</lastmod><changefreq>weekly</changefreq><priority>0.8</priority>'
                   '<xhtml:link rel="alternate" hreflang="es" href="%s"/>'
                   '<xhtml:link rel="alternate" hreflang="en" href="%s"/>'
                   '<xhtml:link rel="alternate" hreflang="x-default" href="%s"/></url>'
                   % (es_url, TODAY, es_url, en_url, en_url))
    if add:
        s = s.replace('</urlset>', "\n".join(add) + "\n</urlset>", 1)
    if s != s_orig:
        with io.open(sm, "w", encoding="utf-8", newline="\n") as f:
            f.write(s)
        print("  patched sitemap.xml (+%d nuevas URLs es)" % len(add))

if __name__ == "__main__":
    build()
    for es_rel, en_rel, html in PAGES:
        w(es_rel, html)
    print("--- patching EN pages ---")
    patch_en()
    print("DONE:", len(PAGES), "es pages")
