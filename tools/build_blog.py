import os, json, html

OUT = os.environ.get("OUT", "out")
BASE = "https://materializamexico.com"
DATE = "2026-11-24"

CSS = """
:root{--obs:#0C0C0A;--carbon:#1A1915;--gold:#C9A84C;--gold-d:#9A7820;--ivory:#F0EDE6;--paper:#F7F4EE;--border:#E2DCCE;--ink:#15140F;--ink2:#33312A;--ink3:#6B675C}
*{box-sizing:border-box;margin:0;padding:0}
body{font-family:'Barlow',sans-serif;background:var(--paper);color:var(--ink2);line-height:1.75;font-size:17px}
a{color:var(--gold-d)}
header{background:var(--obs);padding:1.1rem 2rem;display:flex;align-items:center;justify-content:space-between}
header .brand{font-family:Georgia,serif;font-weight:bold;letter-spacing:4px;color:var(--ivory);text-decoration:none;font-size:1.15rem}
header nav a{color:rgba(240,237,230,.7);text-decoration:none;font-size:.85rem;margin-left:1.4rem}
header nav a:hover{color:var(--gold)}
.hero{background:var(--obs);color:var(--ivory);padding:3.5rem 2rem 3rem;text-align:center}
.hero .eb{color:var(--gold);font-size:.72rem;letter-spacing:.22em;text-transform:uppercase;font-weight:600}
.hero h1{font-family:'Fraunces',serif;font-weight:400;font-size:clamp(1.9rem,4vw,2.8rem);line-height:1.2;max-width:820px;margin:.8rem auto 0}
.hero p{color:rgba(240,237,230,.65);max-width:640px;margin:1rem auto 0}
main{max-width:760px;margin:0 auto;padding:3rem 1.5rem 4rem}
main h2{font-family:'Fraunces',serif;font-weight:400;color:var(--ink);font-size:1.6rem;margin:2.4rem 0 .8rem}
main h3{color:var(--ink);font-size:1.1rem;margin:1.6rem 0 .5rem}
main p{margin:0 0 1rem}
main ul,main ol{margin:0 0 1.2rem 1.4rem}
main li{margin:.35rem 0}
table{width:100%;border-collapse:collapse;margin:1rem 0 1.6rem;font-size:.95rem}
th,td{border-bottom:1px solid var(--border);padding:.6rem .5rem;text-align:left;vertical-align:top}
th{color:var(--ink);font-weight:600;background:#EFEBE2}
.note{background:#EFEBE2;border-left:3px solid var(--gold);padding:1rem 1.2rem;border-radius:6px;margin:1.6rem 0;font-size:.95rem}
.cta{background:var(--obs);color:var(--ivory);border-radius:14px;padding:2rem;margin-top:3rem;text-align:center}
.cta h2{color:var(--ivory);margin-top:0}
.cta a{display:inline-block;background:var(--gold);color:var(--obs);text-decoration:none;font-weight:600;padding:.8rem 1.6rem;border-radius:8px;margin-top:.6rem}
.meta{font-size:.82rem;color:var(--ink3);margin-bottom:2rem}
.cards{display:grid;gap:1.2rem}
.card{display:block;background:#fff;border:1px solid var(--border);border-radius:12px;padding:1.5rem;text-decoration:none;color:var(--ink2)}
.card:hover{border-color:var(--gold)}
.card .tag{font-size:.7rem;letter-spacing:.16em;text-transform:uppercase;color:var(--gold-d);font-weight:600}
.card h2{font-size:1.35rem;margin:.4rem 0 .5rem}
footer{background:var(--obs);color:rgba(240,237,230,.55);text-align:center;padding:2rem;font-size:.82rem}
footer a{color:rgba(240,237,230,.75);margin:0 .6rem;text-decoration:none}
"""

FONTS = '<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Fraunces:wght@400&family=Barlow:wght@400;500;600&display=swap" rel="stylesheet">'

HEADER = '<header><a class="brand" href="/">MATERIALIZA</a><nav><a href="/doma">DOMA</a><a href="/guizar">Guizar Living</a><a href="/umbau">UMBAU</a><a href="/kl">KL</a><a href="/blog/">Blog</a><a href="/#contacto">Contacto</a></nav></header>'
FOOTER = '<footer><div><a href="/">Materializa</a><a href="/doma">DOMA</a><a href="/guizar">Guizar Living</a><a href="/umbau">UMBAU</a><a href="/kl">KL</a><a href="/blog/">Blog</a></div><p style="margin-top:.8rem">© 2026 Materializa · Grupo inmobiliario · materializamexico.com</p><p style="margin-top:.4rem">Contenido informativo. No constituye asesoría legal, fiscal ni financiera.</p></footer>'


def page(title, desc, path, body, extra_ld=None):
    ld = extra_ld or {}
    return f"""<!DOCTYPE html>
<html lang="es">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{html.escape(title)}</title>
<meta name="description" content="{html.escape(desc)}">
<link rel="canonical" href="{BASE}{path}">
<meta property="og:type" content="{'article' if extra_ld else 'website'}">
<meta property="og:site_name" content="Materializa">
<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(desc)}">
<meta property="og:url" content="{BASE}{path}">
<meta property="og:locale" content="es_MX">
{FONTS}
<style>{CSS}</style>
{('<script type="application/ld+json">' + json.dumps(ld, ensure_ascii=False) + '</script>') if ld else ''}
</head>
<body>
{HEADER}
{body}
{FOOTER}
</body>
</html>
"""


ARTICLES = [
{
"slug": "como-presupuestar-remodelacion-departamento",
"tag": "Construcción y remodelación · Guizar Living",
"title": "Cómo presupuestar la remodelación de un departamento: partidas, tiempos y errores comunes",
"desc": "Guía práctica para armar el presupuesto de una remodelación: qué partidas incluir, cómo comparar cotizaciones, cuánto contingente dejar y qué errores encarecen la obra.",
"lead": "Una remodelación casi nunca se sale de presupuesto por el precio de los materiales. Se sale por lo que nadie puso en la lista.",
"cta": ("¿Vas a remodelar?", "Guizar Living te entrega un presupuesto por partida y un calendario de obra antes de empezar.", "/guizar"),
"body": """
<p>Antes de pedir cotizaciones conviene tener claro qué se va a hacer, en qué orden y con qué nivel de acabados. Con eso, cualquier contratista puede cotizar lo mismo y la comparación es justa.</p>

<h2>1. Define el alcance por espacios</h2>
<p>Haz una lista cuarto por cuarto: cocina, baños, áreas comunes, recámaras, fachada o terraza. Para cada espacio anota si es <strong>renovación ligera</strong> (pintura, luminarias, accesorios), <strong>media</strong> (pisos, carpintería, muebles de baño) o <strong>integral</strong> (demolición, instalaciones nuevas, redistribución).</p>

<h2>2. Las partidas que no pueden faltar</h2>
<table>
<tr><th>Partida</th><th>Qué incluye</th><th>Lo que suele olvidarse</th></tr>
<tr><td>Preliminares y demoliciones</td><td>Protección de áreas, retiro de acabados, acarreo de escombro</td><td>Permisos del condominio y horario de trabajo</td></tr>
<tr><td>Instalaciones</td><td>Eléctrica, hidráulica, sanitaria, gas</td><td>Cambiar tubería vieja mientras el muro está abierto</td></tr>
<tr><td>Albañilería y tablaroca</td><td>Muros, plafones, nivelación de firmes</td><td>Resanes y detalles en esquinas</td></tr>
<tr><td>Pisos y recubrimientos</td><td>Porcelanato, madera, mármol, azulejo</td><td>Merma de material (8–12%) y zoclo</td></tr>
<tr><td>Carpintería y cocina</td><td>Cocina integral, closets, puertas</td><td>Herrajes de calidad y cubierta</td></tr>
<tr><td>Muebles de baño y grifería</td><td>WC, lavabos, regaderas, accesorios</td><td>Cancelería de vidrio templado</td></tr>
<tr><td>Pintura y acabados finales</td><td>Sellador, pintura, impermeabilizante</td><td>Limpieza fina de entrega</td></tr>
</table>

<h2>3. Pide cotizaciones comparables</h2>
<p>Entrega a cada proveedor la misma lista de partidas, con cantidades (m², piezas, metros lineales) y especificación de materiales. Una cotización "por todo" sin desglose no se puede comparar ni supervisar.</p>
<ul>
<li>Pide que separen <strong>mano de obra</strong> y <strong>materiales</strong>.</li>
<li>Revisa qué incluye el precio: fletes, maniobras, retiro de escombro, limpieza.</li>
<li>Confirma la forma de pago ligada a avances de obra, no a fechas.</li>
</ul>

<h2>4. Deja un contingente</h2>
<p>Abrir muros y pisos casi siempre revela algo: tubería dañada, humedad, instalaciones fuera de norma. Una práctica común es reservar entre 10% y 15% del presupuesto para imprevistos. Si no se usa, mejor.</p>

<h2>5. Calcula tiempos reales</h2>
<p>Una renovación ligera puede resolverse en unas semanas; una remodelación integral de departamento suele tomar varios meses. Lo que más retrasa una obra es esperar materiales que no se pidieron a tiempo, sobre todo cubiertas de piedra, cancelería y cocinas a la medida.</p>

<h2>Errores que más encarecen una remodelación</h2>
<ol>
<li>Cambiar el diseño a mitad de la obra.</li>
<li>Comprar acabados antes de tener medidas finales.</li>
<li>No revisar instalaciones ocultas antes de cerrar muros.</li>
<li>Elegir solo por el precio más bajo sin comparar alcance.</li>
<li>No dejar por escrito el alcance, los tiempos y las garantías.</li>
</ol>

<div class="note">Tip: si vas a rentar o vender después de remodelar, invierte primero en cocina, baños e iluminación. Son los espacios que más pesan en la decisión de quien visita el inmueble.</div>
"""
},
{
"slug": "marmol-granito-o-cuarzo-cocina",
"tag": "Materiales y acabados · UMBAU",
"title": "Mármol, granito o cuarzo: cuál conviene para la cubierta de tu cocina",
"desc": "Comparamos mármol, granito, cuarzo y porcelanato para cubiertas de cocina y baño: resistencia, mantenimiento, manchas, calor y para qué estilo funciona cada uno.",
"lead": "La cubierta es lo que más se toca, se mancha y se ve en una cocina. Elegir bien el material evita reparaciones y arrepentimientos.",
"cta": ("¿Estás eligiendo acabados?", "En UMBAU te mostramos piezas reales y te ayudamos a elegir según el uso que le vas a dar.", "/umbau"),
"body": """
<p>No existe un material "mejor" en abstracto. Existe el que mejor se adapta a cómo usas tu cocina, cuánto mantenimiento estás dispuesto a dar y el estilo que buscas.</p>

<h2>Comparativa rápida</h2>
<table>
<tr><th></th><th>Mármol</th><th>Granito</th><th>Cuarzo</th><th>Porcelanato de gran formato</th></tr>
<tr><td><strong>Origen</strong></td><td>Piedra natural</td><td>Piedra natural</td><td>Piedra compuesta (cuarzo + resinas)</td><td>Cerámica sinterizada</td></tr>
<tr><td><strong>Manchas</strong></td><td>Sensible (ácidos, vino, limón)</td><td>Resistente si está sellado</td><td>Muy resistente, no poroso</td><td>Muy resistente</td></tr>
<tr><td><strong>Rayones</strong></td><td>Se raya con más facilidad</td><td>Muy resistente</td><td>Resistente</td><td>Muy resistente</td></tr>
<tr><td><strong>Calor</strong></td><td>Tolera calor moderado</td><td>Tolera bien el calor</td><td>Evitar ollas calientes directas</td><td>Tolera bien el calor</td></tr>
<tr><td><strong>Mantenimiento</strong></td><td>Sellado periódico</td><td>Sellado ocasional</td><td>Mínimo</td><td>Mínimo</td></tr>
<tr><td><strong>Estética</strong></td><td>Vetas únicas, look clásico</td><td>Granulado, tonos variados</td><td>Uniforme, muchos diseños</td><td>Imita piedra, cemento o madera</td></tr>
</table>

<h2>Mármol: para quien prioriza la belleza</h2>
<p>Cada placa es única. Envejece con pátina: aparecen marcas y desgaste que a algunos les encanta y a otros les molesta. Funciona muy bien en baños, islas de poco uso y cocinas donde se cocina poco.</p>

<h2>Granito: el más resistente de las piedras naturales</h2>
<p>Aguanta calor, golpes y uso diario. Bien sellado, resiste manchas. Es buena opción para cocinas de uso intensivo y exteriores.</p>

<h2>Cuarzo: práctico y uniforme</h2>
<p>Al no ser poroso, prácticamente no se mancha ni necesita sellado. Es ideal para familias y cocinas muy usadas. Su punto débil es el calor directo: siempre usa base para ollas.</p>

<h2>Porcelanato de gran formato</h2>
<p>Placas delgadas y ligeras, resistentes a manchas, rayones y calor. Permiten continuidad entre cubierta, muro y piso. Requieren mano de obra especializada para cortes e instalación.</p>

<h2>Antes de comprar, revisa</h2>
<ul>
<li><strong>Ve la placa completa</strong>, no solo una muestra: en piedra natural cada placa cambia.</li>
<li><strong>Medidas finales</strong> de la cocina ya armada, para minimizar uniones.</li>
<li><strong>Tipo de canto</strong> (recto, boleado, inglete) y si incluye perforaciones para tarja y parrilla.</li>
<li><strong>Garantía</strong> del material y de la instalación.</li>
</ul>
"""
},
{
"slug": "como-vender-tu-casa-mas-rapido",
"tag": "Compra y venta · DOMA",
"title": "Cómo vender tu casa o departamento más rápido: 8 pasos antes de publicarlo",
"desc": "Documentos, precio, presentación y estrategia: lo que conviene resolver antes de poner tu casa o departamento a la venta en México para venderlo más rápido y sin sorpresas.",
"lead": "La mayoría de las ventas que se atoran no tienen un problema de mercado, sino de precio, documentos o presentación.",
"cta": ("¿Quieres vender tu propiedad?", "DOMA te ayuda con valuación, documentos, fotos y promoción, y te acompaña hasta la firma.", "/doma"),
"body": """
<h2>1. Ten tus documentos en orden</h2>
<p>Un comprador con crédito hipotecario o un notario los van a pedir. Tenerlos desde el inicio evita que una venta se caiga:</p>
<ul>
<li>Escritura inscrita en el Registro Público de la Propiedad.</li>
<li>Boletas de predial y agua al corriente.</li>
<li>Identificación oficial y, si aplica, acta de matrimonio y régimen.</li>
<li>Constancia de no adeudo de mantenimiento, si es condominio.</li>
<li>Planos o croquis, y en su caso licencias o permisos de construcción.</li>
</ul>

<h2>2. Define un precio con datos</h2>
<p>Compara propiedades similares <em>vendidas</em>, no solo publicadas: mismo tipo, zona, metros y estado. Un avalúo profesional ayuda a negociar. Un precio inflado al inicio hace que el inmueble "se queme" en los portales y luego cueste más venderlo.</p>

<h2>3. Arregla lo que se ve en la visita</h2>
<p>Pintura, luminarias fundidas, fugas, puertas que no cierran. Son reparaciones pequeñas que el comprador convierte en descuentos grandes.</p>

<h2>4. Despersonaliza y ordena</h2>
<p>Menos objetos personales y más espacio libre. El comprador necesita imaginarse viviendo ahí.</p>

<h2>5. Invierte en fotos profesionales</h2>
<p>La primera visita ocurre en el celular. Fotos con luz natural, gran angular y un recorrido en video multiplican las solicitudes de visita.</p>

<h2>6. Publica donde están los compradores</h2>
<p>Portales inmobiliarios, redes sociales y red de asesores. Un anuncio con descripción completa (metros, recámaras, baños, estacionamientos, amenidades, mantenimiento) filtra curiosos y atrae compradores reales.</p>

<h2>7. Facilita las visitas</h2>
<p>Responde rápido y ofrece horarios amplios. Cada día de demora en responder es un comprador que sigue buscando.</p>

<h2>8. Conoce los costos de la venta</h2>
<p>Considera comisión inmobiliaria, posibles reparaciones, cancelación de hipoteca si aún la tienes y el impuesto sobre la renta por enajenación, que puede tener exenciones si es tu casa habitación y cumples ciertos requisitos. Consúltalo con el notario antes de fijar tu precio mínimo.</p>

<div class="note">Importante: los requisitos fiscales y notariales cambian según cada caso. Valida tu situación con un notario o contador antes de firmar.</div>
"""
},
{
"slug": "renta-vacacional-airbnb-que-revisar",
"tag": "Administración de propiedades · KL",
"title": "Renta vacacional en Cancún o Mérida: qué revisar antes de poner tu departamento en Airbnb",
"desc": "Reglamento del condominio, permisos locales, impuestos, equipamiento, limpieza y precios: lo que conviene revisar antes de convertir tu propiedad en renta vacacional.",
"lead": "Una renta vacacional bien operada se parece más a un pequeño hotel que a un arrendamiento. Estos son los puntos a revisar antes de abrir el calendario.",
"cta": ("¿Tienes una propiedad para renta vacacional?", "KL se encarga de anuncios, huéspedes, limpieza, mantenimiento y reportes mensuales.", "/kl"),
"body": """
<h2>1. Reglamento del condominio</h2>
<p>Muchos condominios regulan o prohíben las rentas de corta estancia. Revisa el reglamento y las actas de asamblea antes de invertir en equipamiento.</p>

<h2>2. Regulación local</h2>
<p>Algunos estados y municipios piden registros, licencias o el pago de impuestos locales sobre hospedaje. Infórmate con la autoridad de turismo y la tesorería de tu localidad.</p>

<h2>3. Impuestos</h2>
<p>En México, las plataformas digitales de hospedaje retienen ISR e IVA a los anfitriones personas físicas. Aun así, conviene que un contador revise si te conviene ese esquema o tributar de otra forma, y cómo deducir gastos.</p>

<h2>4. Equipamiento mínimo</h2>
<ul>
<li>Blancos dobles por cama (un juego en uso, otro en lavado).</li>
<li>Cocina básica completa, cafetera y utensilios.</li>
<li>Internet estable, aire acondicionado en clima cálido, cerradura digital.</li>
<li>Botiquín, extintor y datos de emergencia visibles.</li>
</ul>

<h2>5. Limpieza y mantenimiento</h2>
<p>Las calificaciones dependen sobre todo de la limpieza y de que todo funcione. Ten un protocolo por salida, inventario de blancos y una lista de revisión mensual (aires, filtros, plomería, focos).</p>

<h2>6. Precio dinámico</h2>
<p>Ajusta tarifas por temporada, día de la semana, eventos y anticipación. Un precio fijo todo el año deja dinero sobre la mesa en temporada alta y calendario vacío en temporada baja.</p>

<h2>7. Cuentas claras</h2>
<p>Lleva un registro mensual de ingresos, comisiones de la plataforma, limpieza, mantenimiento, servicios y cuota de condominio. Así sabes cuánto produce realmente tu propiedad.</p>

<div class="note">Antes de decidir entre renta vacacional o de largo plazo, compara ambos escenarios con números reales de tu zona: ocupación, tarifa promedio y costos de operación.</div>
"""
},
]


def main():
    os.makedirs(f"{OUT}/blog", exist_ok=True)
    cards = []
    for a in ARTICLES:
        path = f"/blog/{a['slug']}/"
        ld = {"@context": "https://schema.org", "@type": "Article", "headline": a["title"], "description": a["desc"],
              "datePublished": DATE, "dateModified": DATE, "inLanguage": "es-MX",
              "author": {"@type": "Organization", "name": "Materializa", "url": BASE + "/"},
              "publisher": {"@type": "Organization", "name": "Materializa", "url": BASE + "/"},
              "mainEntityOfPage": BASE + path}
        t, d, link = a["cta"]
        body = f"""<section class="hero"><div class="eb">{a['tag']}</div><h1>{a['title']}</h1><p>{a['lead']}</p></section>
<main><div class="meta">Equipo Materializa · 24 de noviembre de 2026</div>
{a['body']}
<div class="cta"><h2>{t}</h2><p>{d}</p><a href="{link}">Conocer más</a> <a href="/#contacto" style="background:transparent;border:1px solid var(--gold);color:var(--gold);margin-left:.4rem">Contáctanos</a></div>
<p style="margin-top:2.4rem"><a href="/blog/">← Ver todos los artículos</a></p>
</main>"""
        os.makedirs(f"{OUT}/blog/{a['slug']}", exist_ok=True)
        with open(f"{OUT}/blog/{a['slug']}/index.html", "w", encoding="utf-8") as f:
            f.write(page(a["title"] + " | Materializa", a["desc"], path, body, ld))
        cards.append(f'<a class="card" href="{path}"><div class="tag">{a["tag"]}</div><h2>{a["title"]}</h2><p>{a["desc"]}</p></a>')
    body = f"""<section class="hero"><div class="eb">Blog Materializa</div><h1>Guías para comprar, vender, remodelar y administrar inmuebles</h1><p>Información práctica del equipo de DOMA, Guizar Living, UMBAU y KL.</p></section>
<main><div class="cards">{''.join(cards)}</div></main>"""
    ld = {"@context": "https://schema.org", "@type": "Blog", "name": "Blog Materializa", "url": BASE + "/blog/",
          "publisher": {"@type": "Organization", "name": "Materializa", "url": BASE + "/"}}
    with open(f"{OUT}/blog/index.html", "w", encoding="utf-8") as f:
        f.write(page("Blog | Materializa — compra, venta, remodelación y administración de inmuebles",
                     "Guías prácticas sobre compra y venta de inmuebles, remodelación, materiales y acabados, y administración de rentas vacacionales en México.",
                     "/blog/", body, None).replace('<meta property="og:type" content="website">', '<meta property="og:type" content="website">\n<script type="application/ld+json">' + json.dumps(ld, ensure_ascii=False) + '</script>'))
    urls = ["/", "/doma", "/guizar", "/umbau", "/kl", "/blog/"] + [f"/blog/{a['slug']}/" for a in ARTICLES]
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "".join(
        f"  <url><loc>{BASE}{u}</loc><lastmod>{DATE}</lastmod></url>\n" for u in urls) + "</urlset>\n"
    open(f"{OUT}/sitemap.xml", "w").write(sm)
    open(f"{OUT}/robots.txt", "w").write(f"User-agent: *\nAllow: /\n\nSitemap: {BASE}/sitemap.xml\n")
    print("ok", len(urls))


if __name__ == "__main__":
    main()
