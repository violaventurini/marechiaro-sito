# -*- coding: utf-8 -*-
import io, os, re, json, importlib.util
BASE = '/home/claude/sito'
_e = importlib.util.spec_from_file_location('e', '/home/claude/sito/_strumenti/evento.py')
EV = importlib.util.module_from_spec(_e); _e.loader.exec_module(EV)
s = importlib.util.spec_from_file_location('c', '/home/claude/sito/_strumenti/carta.py')
D = importlib.util.module_from_spec(s); s.loader.exec_module(D)

home   = io.open(os.path.join(BASE,'index.html'), encoding='utf-8').read()
homeen = io.open(os.path.join(BASE,'en','index.html'), encoding='utf-8').read()
def pezzo(src, apri, chiudi):
    i=src.index(apri); j=src.index(chiudi, i)
    return src[i:j+len(chiudi)]
NAV_IT = pezzo(home,'<nav class="nav">','</nav>')
NAV_EN = pezzo(homeen,'<nav class="nav">','</nav>')
FOOT_IT= pezzo(home,'<footer>','</footer>')
FOOT_EN= pezzo(homeen,'<footer>','</footer>')
CTA_IT = pezzo(home,'<a class="ctaev"','</a>')
CTA_EN = pezzo(homeen,'<a class="ctaev"','</a>')
BARRA_IT = pezzo(home,'<div class="barra">','</div>')
BARRA_EN = pezzo(homeen,'<div class="barra">','</div>')
ONDA = ('<svg class="onda" viewBox="0 0 1200 200" preserveAspectRatio="none" aria-hidden="true">'
 '<path d="M0 100 Q150 60 300 100 T600 100 T900 100 T1200 100"></path>'
 '<path d="M0 130 Q150 90 300 130 T600 130 T900 130 T1200 130"></path>'
 '<path d="M0 160 Q150 120 300 160 T600 160 T900 160 T1200 160"></path></svg>')

def voci(lista, lang, prezzo_unico=False):
    out=[]
    for it_n,en_n,it_d,en_d,p,al in lista:
        nome  = it_n if lang=='it' else en_n
        descr = it_d if lang=='it' else en_d
        pr = '' if (prezzo_unico or not p) else '%s&nbsp;&euro;' % p
        out.append('        <li>\n'
          '          <p class="v__riga"><span class="v__n">%s</span><span class="v__l" aria-hidden="true"></span>'
          '<span class="v__p">%s</span></p>%s%s\n        </li>' % (
          nome, pr,
          ('\n          <p class="v__d">%s</p>'%descr) if descr else '',
          ('\n          <p class="v__a">%s</p>'%al) if al else ''))
    return '\n'.join(out)

def blocco(n, ident, tit, alt, eti, lista, lang, intro='', unico=False, largo=False):
    return '''    <section class="menu-blocco%s riv" id="%s">
      <header class="menu-testa">
        <span class="menu-n">%02d</span><h2>%s</h2>
        <span class="menu-alt">%s</span><span class="menu-eti">%s</span>
      </header>%s
      <ul class="voci">
%s
      </ul>
    </section>''' % (' menu-blocco--largo' if largo else '', ident, n, tit, alt, eti,
                     ('\n      <p class="menu-intro">%s</p>'%intro) if intro else '',
                     voci(lista, lang, unico))

TESTA = '''<!DOCTYPE html>
<html lang="{lg}">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{t}</title>
<meta name="description" content="{d}">
<link rel="canonical" href="https://marechiaroostia.it{p}">
<link rel="alternate" hreflang="it" href="https://marechiaroostia.it{ait}">
<link rel="alternate" hreflang="en" href="https://marechiaroostia.it{aen}">
<link rel="alternate" hreflang="x-default" href="https://marechiaroostia.it{ait}">
<link rel="icon" href="/favicon.svg" type="image/svg+xml">
<link rel="apple-touch-icon" href="/apple-touch-icon.png">
<meta name="theme-color" content="#FBF7EF">
<meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">
<meta property="og:type" content="website">
<meta property="og:locale" content="{loc}">
<meta property="og:site_name" content="Marechiaro Ostia">
<meta property="og:title" content="{t}">
<meta property="og:description" content="{d}">
<meta property="og:url" content="https://marechiaroostia.it{p}">
<meta property="og:image" content="https://marechiaroostia.it/img/og-marechiaro.jpg">
<meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght,SOFT@9..144,300..600,60..100&family=Jost:wght@300;400;500;600&display=swap" rel="stylesheet">
<link rel="stylesheet" href="/avorio.css">
'''

CARTE = {
 'it': [('/menu-colazione','Colazione'),('/menu-pranzo','Pranzo'),
        ('/menu-aperitivo','Aperitivo'),('/menu-cena','Cena')],
 'en': [('/en/menu-breakfast','Breakfast'),('/en/menu-lunch','Lunch'),
        ('/en/menu-aperitivo','Aperitivo'),('/en/menu-dinner','Dinner')],
}
def selettore(lang, qui):
    v = ''.join('<a href="%s"%s>%s</a>' % (u, ' aria-current="page"' if u==qui else '', n)
                for u,n in CARTE[lang])
    return ('<nav class="carte" aria-label="%s">\n  <div class="wrap carte__in">%s</div>\n</nav>'
            % ('Le carte' if lang=='it' else 'The menus', v))

def lingue(lang, ait, aen):
    return ('<span class="lingue"><a href="%s" hreflang="it" lang="it">IT</a><b>EN</b></span>' % ait
            if lang=='en' else
            '<span class="lingue"><b>IT</b><a href="%s" hreflang="en" lang="en">EN</a></span>' % aen)

def scrivi(file, lang, t, d, path, ait, aen, testata, corpo, schemi=()):
    h = TESTA.format(lg=lang, t=t, d=d, p=path, ait=ait, aen=aen,
                     loc='it_IT' if lang=='it' else 'en_GB')
    for s_ in schemi: h += '<script type="application/ld+json">\n%s\n</script>\n' % s_
    nav = (NAV_IT if lang=='it' else NAV_EN)
    nav = re.sub(r'<span class="lingue">.*?</span>\s*</span>|<span class="lingue">.*?</span>',
                 lingue(lang, ait, aen), nav, count=1, flags=re.S)
    h += '</head>\n<body>\n' + nav + '\n'
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
    if path not in ('/menu','/en/menu'):
        h += selettore(lang, path) + '\n'
    h += corpo + '\n'
    h += (FOOT_IT if lang=='it' else FOOT_EN) + '\n'
    if EV.ATTIVO:
        h += ('<a class="ctaev" href="%s" aria-label="%s">\n'
              '  <span class="ctaev__e">%s</span>\n'
              '  <span class="ctaev__t">%s <em>&rarr;</em></span>\n</a>\n\n') % (
              EV.WA_IT if lang=='it' else EV.WA_EN,
              'Prenota la cena con musica dal vivo di venerd&igrave; 14 agosto' if lang=='it'
              else 'Book the dinner with live music on Friday 14 August',
              EV.DATA_IT if lang=='it' else EV.DATA_EN,
              ('Prenota la cena' if lang=='it' else 'Book the dinner'))
    h += (BARRA_IT if lang=='it' else BARRA_EN) + '\n'
    h += '<script src="/avorio.js"></script>\n</body>\n</html>\n'
    p = os.path.join(BASE, file)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    io.open(p,'w',encoding='utf-8').write(h)
    print('  %-24s %6d byte' % (file, len(h)))
