# -*- coding: utf-8 -*-
import io, os, re, json
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
home = io.open(os.path.join(BASE,'index.html'), encoding='utf-8').read()
homeen = io.open(os.path.join(BASE,'en','index.html'), encoding='utf-8').read()
NAV_IT  = re.search(r'<nav class="nav">.*?</nav>', home, re.S).group(0)
NAV_EN  = re.search(r'<nav class="nav">.*?</nav>', homeen, re.S).group(0)
FOOT_IT = re.search(r'<footer>.*?</div>\n\n<script', home, re.S).group(0).replace('\n\n<script','')
FOOT_EN = re.search(r'<footer>.*?</div>\n\n<script', homeen, re.S).group(0).replace('\n\n<script','')

ONDA = ('<svg class="onda" viewBox="0 0 1200 200" preserveAspectRatio="none" aria-hidden="true">'
 '<path d="M0 100 Q150 60 300 100 T600 100 T900 100 T1200 100"></path>'
 '<path d="M0 130 Q150 90 300 130 T600 130 T900 130 T1200 130"></path>'
 '<path d="M0 160 Q150 120 300 160 T600 160 T900 160 T1200 160"></path></svg>')

def testa(t, d, path, alt_it, alt_en, lang):
    return '''<!DOCTYPE html>
<html lang="%s">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>%s</title>
<meta name="description" content="%s">
<link rel="canonical" href="https://marechiaroostia.it%s">
<link rel="alternate" hreflang="it" href="https://marechiaroostia.it%s">
<link rel="alternate" hreflang="en" href="https://marechiaroostia.it%s">
<link rel="alternate" hreflang="x-default" href="https://marechiaroostia.it%s">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<meta name="theme-color" content="#FBF7EF">
<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">
<meta property="og:type" content="website">
<meta property="og:locale" content="%s">
<meta property="og:site_name" content="Marechiaro Ostia">
<meta property="og:title" content="%s">
<meta property="og:description" content="%s">
<meta property="og:url" content="https://marechiaroostia.it%s">
<meta property="og:image" content="https://marechiaroostia.it/img/og-marechiaro.jpg">
<meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght,SOFT@9..144,300..600,60..100&family=Jost:wght@300;400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/avorio.css">
''' % (lang[:2], t, d, path, alt_it, alt_en, alt_it,
       'it_IT' if lang=='it' else 'en_GB', t, d, path)

def briciole(nome, url, lingua):
    return json.dumps({"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[
      {"@type":"ListItem","position":1,"name":"Marechiaro Ostia",
       "item":"https://marechiaroostia.it/" if lingua=='it' else "https://marechiaroostia.it/en/"},
      {"@type":"ListItem","position":2,"name":nome,"item":"https://marechiaroostia.it"+url}]},
      ensure_ascii=False, indent=2)

def scrivi(file, t, d, path, alt_it, alt_en, lang, testata, corpo, schemi=()):
    h = testa(t,d,path,alt_it,alt_en,lang)
    for s in schemi:
        h += '<script type="application/ld+json">\n%s\n</script>\n' % s
    h += '</head>\n<body>\n'
    h += (NAV_IT if lang=='it' else NAV_EN) + '\n'
    h += '''
<header class="testata">
  %s
  <div class="wrap testata__testo">
    <span class="eti">%s</span>
    <h1>%s</h1>
    <p class="guida">%s</p>
  </div>
</header>
''' % ((ONDA,)+testata)
    h += corpo + '\n'
    h += (FOOT_IT if lang=='it' else FOOT_EN) + '\n<script src="/avorio.js"></script>\n</body>\n</html>\n'
    p = os.path.join(BASE, file)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    io.open(p,'w',encoding='utf-8').write(h)
    print('  %-22s %6d byte' % (file, len(h)))
