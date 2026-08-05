# -*- coding: utf-8 -*-
import io, importlib.util
from costruisci import pagina

spec = importlib.util.spec_from_file_location('md','menu-dati.py')
D = importlib.util.module_from_spec(spec); spec.loader.exec_module(D)

ONDA = ('<svg class="onda" viewBox="0 0 1200 200" preserveAspectRatio="none" aria-hidden="true">'
        '<path d="M0 100 Q150 60 300 100 T600 100 T900 100 T1200 100"></path>'
        '<path d="M0 130 Q150 90 300 130 T600 130 T900 130 T1200 130"></path>'
        '<path d="M0 160 Q150 120 300 160 T600 160 T900 160 T1200 160"></path></svg>')

def voci(lista, lingua, giorno=False):
    r = []
    for it_n, en_n, it_d, en_d, prezzo, alle in lista:
        nome  = it_n if lingua=='it' else en_n
        descr = it_d if lingua=='it' else en_d
        p = ('%s&euro;' % prezzo) if prezzo else '<span class="da-definire">&mdash;</span>'
        r.append(
'''        <li>
          <p class="v__riga"><span class="v__n">%s</span><span class="v__l" aria-hidden="true"></span><span class="v__p">%s</span></p>%s%s
        </li>''' % (nome, p,
            ('\n          <p class="v__d">%s</p>' % descr) if descr else '',
            ('\n          <p class="v__a">%s</p>' % alle) if alle else ''))
    return '\n'.join(r)

def sera(n, lingua, T):
    t = ('Antipasti','Primi','Secondi') if lingua=='it' else ('Starters','First courses','Main courses')
    sotto = ''.join(
      '\n      <h3 class="sera__t">%s</h3>\n      <ul class="voci">\n%s\n      </ul>' % (t[i], voci(l, lingua))
      for i,l in enumerate([D.SERA_ANTIPASTI, D.SERA_PRIMI, D.SERA_SECONDI]))
    return '''    <section class="menu-blocco menu-blocco--largo riv" id="sera">
      <header class="menu-testa">
        <span class="menu-n">%02d</span>
        <h2>%s</h2>
        <span class="menu-alt">%s</span>
        <span class="menu-eti">%s</span>
      </header>
      <p class="menu-intro">%s</p>%s
    </section>''' % (n, T[0], T[1], T[2], T[3], sotto)

def blocco(n, ident, titolo, sotto, occhiello, lista, lingua, nota=''):
    return '''    <section class="menu-blocco riv" id="%s">
      <header class="menu-testa">
        <span class="menu-n">%02d</span>
        <h2>%s</h2>
        <span class="menu-alt">%s</span>
        <span class="menu-eti">%s</span>
      </header>%s
      <ul class="voci">
%s
      </ul>
    </section>''' % (ident, n, titolo, sotto, occhiello,
                     ('\n      <p class="menu-intro">%s</p>' % nota) if nota else '',
                     voci(lista, lingua))

T = {
 'it': dict(
   titolo='Menu Ristorante e Pizzeria | Marechiaro Ostia',
   descr="Il menu del Marechiaro a Ostia: proposte del giorno secondo il pescato, fritti, panini, insalate, pizza bassa romana e dolci. Pranzo anche da asporto.",
   occhiello='Bar e cucina', h1='Il menu',
   guida='Le proposte del giorno cambiano con il pescato. Il resto &egrave; sempre disponibile, dal panino sotto l&rsquo;ombrellone alla pizza bassa romana della sera.',
   nastro='Proposte del giorno<i>&mdash;</i>Pranzo dalle 13<i>&mdash;</i>Anche da asporto<i>&mdash;</i>Pizza dalle 17<i>&mdash;</i>Aperitivo dalle 18<i>&mdash;</i>',
   indice=[('proposte','Proposte del giorno'),('sfizi','Sfizi e fritti'),('panini','Panini'),
           ('insalate','Insalate'),('sera','La sera'),('pizze','Pizze'),('dolci','Dolci')],
   orari=[('08:30','Colazione al bancone'),('13:00','Pranzo, anche da asporto'),
          ('17:00','Pizza, il forno si accende'),('18:00','Aperitivo sulla sabbia'),
          ('20:30','Ristorante e pizzeria')],
   orari_eti='Gli orari del servizio',
   giorno=('Le proposte del giorno','Chef&rsquo;s daily specials','Secondo il pescato',
           'E ogni giorno nuove proposte a discrezione dello chef, secondo il pescato. Chiedi al personale.'),
   sera=('La sera','The evening','Ristorante e pizzeria',
         'Dalle 17 la cucina passa al menu della sera: crudi e antipasti di mare, primi e secondi. Chi preferisce la pizza la trova comunque, bassa e croccante, fino a tardi.'),
   blocchi=[('sfizi','Sfizi e fritti','Bites &amp; fried','Tutto il giorno',D.SFIZI,''),
            ('panini','Panini','Sandwiches','Pronti e gustosi',D.PANINI,''),
            ('insalate','Insalate','Salads','Fresche e abbondanti',D.INSALATE,''),
            ('pizze','Pizze','Pizza','La sera, dalle 17',D.PIZZE,'Bassa e croccante, come vuole la tradizione romana. Dalle 17 il forno resta acceso fino a tardi. La sera siamo ristorante e pizzeria: si cena alla carta o si prende una pizza, sempre con il mare davanti, oppure si ordina da asporto.'),
            ('dolci','Dolci','Desserts','Il dolce del giorno',D.DOLCI,'')],
   nota_all='I numeri tra parentesi indicano gli allergeni, secondo il Reg. UE 1169/2011. Per allergie e intolleranze chiedi sempre al personale.',
   coperto='Coperto 2&euro; a persona &middot; Aperitivo dalle 18:00',
   cta_eti='Prenota', cta_h2='Un tavolo con il mare davanti',
   cta_p='Un messaggio su WhatsApp e ti confermiamo tutto in giornata.',
   cta1='Prenota un tavolo', cta2='Il ristorante e la pizzeria', href2='/ristorante',
   wa='Ciao%2C%20vorrei%20prenotare%20un%20tavolo'),
 'en': dict(
   titolo='Menu | Seafront Restaurant and Pizzeria in Ostia, Rome',
   descr="The Marechiaro menu at Ostia beach near Rome: daily specials based on the catch, fried bites, sandwiches, salads, Roman thin pizza and desserts. Takeaway too.",
   occhiello='Bar and kitchen', h1='The menu',
   guida='The daily specials change with the catch. Everything else is always on, from a sandwich under your umbrella to thin Roman pizza in the evening.',
   nastro='Daily specials<i>&mdash;</i>Lunch from 1pm<i>&mdash;</i>Takeaway too<i>&mdash;</i>Pizza from 5pm<i>&mdash;</i>Aperitivo from 6pm<i>&mdash;</i>',
   indice=[('proposte','Daily specials'),('sfizi','Bites &amp; fried'),('panini','Sandwiches'),
           ('insalate','Salads'),('sera','The evening'),('pizze','Pizza'),('dolci','Desserts')],
   orari=[('8:30','Breakfast at the bar'),('1:00 pm','Lunch, takeaway too'),
          ('5:00 pm','Pizza, the oven fires up'),('6:00 pm','Aperitivo on the sand'),
          ('8:30 pm','Restaurant and pizzeria')],
   orari_eti='Service hours',
   giorno=('Daily specials','Le proposte del giorno','Based on the catch',
           'Plus new dishes every day at the chef&rsquo;s discretion, based on the catch. Just ask our staff.'),
   sera=('The evening','La sera','Restaurant and pizzeria',
         'From 5pm the kitchen moves to the evening menu: raw and cooked seafood starters, first and main courses. If you would rather have pizza, it is there too, thin and crispy, until late.'),
   blocchi=[('sfizi','Bites &amp; fried','Sfizi e fritti','All day',D.SFIZI,''),
            ('panini','Sandwiches','Panini','Ready and tasty',D.PANINI,''),
            ('insalate','Salads','Insalate','Fresh and generous',D.INSALATE,''),
            ('pizze','Pizza','Pizze','Evenings, from 5pm',D.PIZZE,'Thin and crispy, true to Roman tradition. From 5pm the oven stays on until late. In the evening we are both restaurant and pizzeria: dinner &agrave; la carte or a pizza, always facing the sea, or takeaway.'),
            ('dolci','Desserts','Dolci','Dessert of the day',D.DOLCI,'')],
   nota_all='Numbers in brackets indicate allergens, under EU Reg. 1169/2011. For allergies and intolerances please always ask our staff.',
   coperto='Cover charge &euro;2 per person &middot; Aperitivo from 6pm',
   cta_eti='Book', cta_h2='A table facing the sea',
   cta_p='Send a WhatsApp message and we&rsquo;ll confirm the same day. We answer in English.',
   cta1='Book a table', cta2='The restaurant and pizzeria', href2='/en/restaurant',
   wa='Hello%2C%20I%20would%20like%20to%20book%20a%20table'),
}

for lingua, t in T.items():
    g = t['giorno']
    indice = '\n'.join('      <a href="#%s">%s</a>' % (i,n) for i,n in t['indice'])
    orari = '\n'.join('      <li><span class="o__h">%s</span><span class="o__c">%s</span></li>' % (h_,c_) for h_,c_ in t['orari'])
    corpo = '''
<header class="testata">
  %s
  <div class="wrap testata__testo">
    <span class="eti">%s</span>
    <h1>%s</h1>
    <p class="guida">%s</p>
  </div>
</header>

<div class="nastri">
  <div class="nastro nastro--dx"><span>%s%s</span></div>
</div>

<section class="orari">
  <div class="wrap">
    <span class="eti">%s</span>
    <ul class="orari__lista riv">
%s
    </ul>
  </div>
</section>

<div class="menu-corpo">
  <nav class="menu-indice" aria-label="%s">
%s
  </nav>

  <div class="menu-colonna">

    <section class="giorno riv" id="proposte">
      %s
      <div class="giorno__blocco">
        <header class="menu-testa">
          <span class="menu-n">01</span>
          <h2>%s</h2>
          <span class="menu-alt">%s</span>
          <span class="menu-eti">%s</span>
        </header>
        <ul class="voci voci--giorno">
%s
        </ul>
        <p class="giorno__nota">%s</p>
      </div>
    </section>

    <div class="menu-griglia">
%s
    </div>

    <section class="menu-legenda riv">
      <p class="menu-nota">%s</p>
      <p class="menu-nota"><strong>%s</strong></p>
    </section>

  </div>
</div>

<section class="sez chiusura">
  %s
  <div class="wrap contenuto riv">
    <span class="eti">%s</span>
    <h2>%s</h2>
    <p class="guida">%s</p>
    <div class="azioni">
      <a class="btn" href="https://wa.me/393484059720?text=%s">%s</a>
      <a class="btn scuro" href="%s">%s</a>
    </div>
  </div>
</section>
''' % (ONDA, t['occhiello'], t['h1'], t['guida'], t['nastro'], t['nastro'],
       t['orari_eti'], orari, t['h1'], indice, ONDA,
       g[0], g[1], g[2], voci(D.PROPOSTE, lingua, True), g[3],
       '\n'.join(([blocco(i+2,b[0],b[1],b[2],b[3],b[4],lingua,b[5]) for i,b in enumerate(t['blocchi'][:3])]
                  + [sera(5, lingua, t['sera'])]
                  + [blocco(i+6,b[0],b[1],b[2],b[3],b[4],lingua,b[5]) for i,b in enumerate(t['blocchi'][3:])])),
       t['nota_all'], t['coperto'], ONDA,
       t['cta_eti'], t['cta_h2'], t['cta_p'], t['wa'], t['cta1'], t['href2'], t['cta2'])

    sezioni = ','.join('{ "@type": "MenuSection", "name": "%s" }' % n.replace('&amp;','&') for _,n in t['indice'])
    schema = '''<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Menu",
  "name": "Menu Marechiaro Ostia",
  "url": "https://marechiaroostia.it%s",
  "inLanguage": "%s",
  "provider": { "@type": "Restaurant", "@id": "https://marechiaroostia.it/ristorante#ristorante" },
  "hasMenuSection": [ %s ]
}
</script>''' % ('/menu' if lingua=='it' else '/en/menu', 'it-IT' if lingua=='it' else 'en-GB', sezioni)

    file = 'menu.html' if lingua=='it' else 'en/menu.html'
    pagina(file, t['titolo'], t['descr'],
           '/menu' if lingua=='it' else '/en/menu',
           '/en/menu' if lingua=='it' else '/menu',
           corpo, schema)
