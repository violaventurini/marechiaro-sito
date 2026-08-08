# -*- coding: utf-8 -*-
exec(open('/home/claude/sito/_strumenti/genera-carte.py').read())
import json, html as H

def faq_schema(c, lang):
    def p(x): return re.sub(r'\s+',' ',H.unescape(re.sub(r'<[^>]+>','',x))).strip()
    return json.dumps({"@context":"https://schema.org","@type":"FAQPage","inLanguage":lang,
      "mainEntity":[{"@type":"Question","name":p(d),"acceptedAnswer":{"@type":"Answer","text":p(r)}} for d,r in c]},
      ensure_ascii=False, indent=2)

def chius(e,h2,p_,b1,w,b2,href):
    return ('\n<section class="sez chiusura">\n  %s\n  <div class="wrap contenuto riv">'
            '<span class="eti">%s</span><h2>%s</h2>\n    <p class="guida">%s</p>\n'
            '    <div class="azioni"><a class="btn" href="https://wa.me/393484059720?text=%s">%s</a>\n'
            '      <a class="btn scuro" href="%s">%s</a></div></div></section>') % (ONDA,e,h2,p_,w,b1,href,b2)

NOTA_IT = ('I numeri tra parentesi indicano gli allergeni, secondo il Reg. UE 1169/2011. '
           'L&rsquo;asterisco segnala i prodotti surgelati all&rsquo;origine. '
           'Per allergie e intolleranze chiedi sempre al personale.')
NOTA_EN = ('Numbers in brackets indicate allergens, under EU Reg. 1169/2011. '
           'An asterisk marks products frozen at source. '
           'For allergies and intolerances please always ask our staff.')
COP_IT = 'Coperto 2&nbsp;&euro; a persona'
COP_EN = 'Cover charge &euro;2 per person'

def legenda(lang):
    return ('\n<section class="sez" style="padding-top:0">\n  <div class="wrap riv">'
            '\n    <section class="menu-legenda">'
            '\n      <p class="menu-nota">%s</p>'
            '\n      <p class="menu-nota"><strong>%s</strong></p>'
            '\n    </section>\n  </div>\n</section>') % (
            NOTA_IT if lang=='it' else NOTA_EN, COP_IT if lang=='it' else COP_EN)

def indice(voci_, lang):
    return '<nav class="menu-indice" aria-label="%s">\n%s\n  </nav>' % (
      'Sezioni del menu' if lang=='it' else 'Menu sections',
      '\n'.join('      <a href="#%s">%s</a>'%(i,n) for i,n in voci_))

# ═══════════════════════ HUB ═══════════════════════
def hub(lang):
    it = lang=='it'
    V = [('colazione' if it else 'breakfast','Colazione' if it else 'Breakfast',
          'Cornetto, cappuccino e spremuta al bancone.' if it else 'Cornetto, cappuccino and fresh juice at the counter.',
          '/menu-colazione' if it else '/en/menu-breakfast'),
         ('pranzo' if it else 'lunch','Pranzo' if it else 'Lunch',
          'Piatti di mare secondo il pescato, insalate, panini e fritti.' if it else 'Seafood following the daily catch, salads, sandwiches and fried bites.',
          '/menu-pranzo' if it else '/en/menu-lunch'),
         ('aperitivo','Aperitivo' if it else 'Aperitivo',
          'Cocktail, vini e sfizi da condividere sulla sabbia.' if it else 'Cocktails, wines and small plates to share on the sand.',
          '/menu-aperitivo' if it else '/en/menu-aperitivo'),
         ('cena' if it else 'dinner','Cena' if it else 'Dinner',
          'Antipasti di mare, primi, secondi e quattordici pizze bassa romana.' if it else 'Seafood starters, first and main courses, fourteen thin Roman pizzas.',
          '/menu-cena' if it else '/en/menu-dinner')]
    righe = '\n'.join(
      '      <a class="riga" href="%s"><span class="n">%02d</span><span class="t">%s</span>\n'
      '        <span class="d">%s</span><span class="v">%s <em>&rarr;</em></span></a>'
      % (u,i+1,t,d,'Vedi il menu' if it else 'See the menu') for i,(_,t,d,u) in enumerate(V))
    corpo = '''
<div class="nastri">
  <div class="nastro nastro--dx"><span>%s%s</span></div>
</div>

<section class="sez">
  <div class="wrap">
    <div class="riv"><span class="eti">%s</span><h2>%s</h2>
      <p class="guida">%s</p></div>
    <div class="righe riv" data-rit="1">
%s
    </div>
  </div>
</section>
''' % (('Colazione<i>&mdash;</i>Pranzo<i>&mdash;</i>Aperitivo<i>&mdash;</i>Cena<i>&mdash;</i>Anche da asporto<i>&mdash;</i>' if it
        else 'Breakfast<i>&mdash;</i>Lunch<i>&mdash;</i>Aperitivo<i>&mdash;</i>Dinner<i>&mdash;</i>Takeaway too<i>&mdash;</i>')*2,
       '',
       'Scegli il momento' if it else 'Choose your moment',
       'Cosa vuoi mangiare' if it else 'What are you after',
       ('Quattro carte diverse, una per ogni momento della giornata. Tocca quella che ti serve.' if it
        else 'Four different menus, one for each moment of the day. Tap the one you need.'),
       righe)
    corpo += legenda(lang)
    corpo += chius('Prenota' if it else 'Book',
      'Un tavolo con il mare davanti' if it else 'A table facing the sea',
      'Un messaggio su WhatsApp e ti confermiamo tutto in giornata.' if it else "Send a WhatsApp message and we'll confirm the same day.",
      'Prenota un tavolo' if it else 'Book a table',
      'Ciao%2C%20vorrei%20prenotare%20un%20tavolo' if it else 'Hello%2C%20I%27d%20like%20to%20book%20a%20table',
      'Il ristorante' if it else 'The restaurant', '/ristorante' if it else '/en/restaurant')
    scrivi('menu.html' if it else 'en/menu.html', lang,
      'Menu | Marechiaro Ostia, Ristorante sulla Spiaggia' if it else 'Menu | Marechiaro Ostia, Restaurant on the Beach',
      ('Le carte del Marechiaro a Ostia: colazione, pranzo, aperitivo e cena. Piatti di mare secondo il pescato, pizza bassa romana, cocktail e vini.' if it
       else 'The Marechiaro menus at Ostia beach near Rome: breakfast, lunch, aperitivo and dinner. Seafood, thin Roman pizza, cocktails and wines.'),
      '/menu' if it else '/en/menu', '/menu', '/en/menu',
      ('Bar e cucina' if it else 'Bar and kitchen',
       'Il menu' if it else 'The menu',
       ('Quattro carte, una per ogni momento della giornata.' if it
        else 'Four menus, one for each moment of the day.')),
      corpo)

# ═══════════════════════ COLAZIONE ═══════════════════════
def colazione(lang):
    it = lang=='it'
    idx = [('colazione','Al bancone' if it else 'At the counter'),
           ('caffe','Il caff&egrave;' if it else 'Coffee'),
           ('forno','Dal forno' if it else 'From the oven'),
           ('fresco','Da bere' if it else 'To drink')]
    corpo = '''
<div class="nastri"><div class="nastro nastro--dx"><span>%s%s</span></div></div>

<div class="menu-corpo">
  %s
  <div class="menu-colonna">
    <section class="giorno riv" id="colazione">
      %s
      <div class="giorno__blocco">
        <header class="menu-testa">
          <span class="menu-n">01</span><h2>%s</h2>
          <span class="menu-alt">%s</span><span class="menu-eti">%s</span>
        </header>
        <p class="giorno__nota" style="margin-top:1.4rem;max-width:54ch;font-size:1.05rem">%s</p>
      </div>
    </section>

    <div class="menu-griglia">
      <section class="menu-blocco riv" id="caffe">
        <header class="menu-testa"><span class="menu-n">02</span><h2>%s</h2>
          <span class="menu-alt">%s</span></header>
        <p class="menu-intro">%s</p>
      </section>
      <section class="menu-blocco riv" id="forno">
        <header class="menu-testa"><span class="menu-n">03</span><h2>%s</h2>
          <span class="menu-alt">%s</span></header>
        <p class="menu-intro">%s</p>
      </section>
      <section class="menu-blocco riv menu-blocco--largo" id="fresco">
        <header class="menu-testa"><span class="menu-n">04</span><h2>%s</h2>
          <span class="menu-alt">%s</span></header>
        <p class="menu-intro">%s</p>
      </section>
    </div>
  </div>
</div>
''' % (('Cornetto appena sfornato<i>&mdash;</i>Cappuccino<i>&mdash;</i>Spremuta fatta al momento<i>&mdash;</i>Succhi e bibite<i>&mdash;</i>' if it
        else 'Cornetto straight from the oven<i>&mdash;</i>Cappuccino<i>&mdash;</i>Juice squeezed to order<i>&mdash;</i>Juices and soft drinks<i>&mdash;</i>')*2,
  '', indice(idx,lang), ONDA,
  'Si comincia dal bancone' if it else 'It starts at the counter',
  'Breakfast' if it else 'Colazione',
  'Dalla mattina' if it else 'From the morning',
  ('Il cornetto appena sfornato e il cappuccino, il caff&egrave; come lo fanno a Roma. Si prende in piedi al banco '
   'guardando il mare, oppure seduti con calma prima di scendere sulla sabbia: qui nessuno ha fretta.'
   if it else
   'A cornetto straight from the oven and a cappuccino, coffee the Roman way. Take it standing at the bar looking at '
   'the sea, or sit down before heading to the sand &mdash; nobody is in a hurry here.'),
  'Il caff&egrave;' if it else 'Coffee', 'Coffee' if it else 'Il caff&egrave;',
  ('Espresso, cappuccino, macchiato, caff&egrave; freddo. Fatti come vanno fatti, senza scorciatoie.'
   if it else 'Espresso, cappuccino, macchiato, iced coffee. Made properly, no shortcuts.'),
  'Dal forno' if it else 'From the oven', 'From the oven' if it else 'Dal forno',
  ('Cornetto vuoto, alla crema o alla marmellata, e il resto della vetrina che cambia ogni mattina.'
   if it else 'Cornetto plain, with custard or with jam, and whatever else fills the counter that morning.'),
  'Da bere' if it else 'To drink', 'To drink' if it else 'Da bere',
  ('La spremuta d&rsquo;arancia &egrave; fatta al momento, davanti a te. Poi i succhi di frutta in bottiglia '
   'e le bibite fresche, per chi la mattina la vuole leggera.'
   if it else
   'The orange juice is squeezed to order, in front of you. Then bottled fruit juices and cold soft drinks, '
   'for a lighter start to the morning.'))
    corpo += legenda(lang)
    corpo += chius('Poi' if it else 'Next',
      'La giornata comincia qui' if it else 'The day starts here',
      ('Dopo colazione si scende in spiaggia. Lettini e ombrelloni si scelgono all&rsquo;arrivo, senza prenotare.'
       if it else 'After breakfast, down to the beach. Sunbeds and umbrellas are chosen on arrival, no booking.'),
      'Scrivici su WhatsApp' if it else 'Message us on WhatsApp',
      'Ciao%2C%20vorrei%20informazioni' if it else 'Hello%2C%20I%27d%20like%20some%20information',
      'La spiaggia' if it else 'The beach', '/spiaggia' if it else '/en/beach')
    scrivi('menu-colazione.html' if it else 'en/menu-breakfast.html', lang,
      'Colazione sulla Spiaggia | Marechiaro Ostia' if it else 'Breakfast on the Beach | Marechiaro Ostia',
      ('Colazione al bancone del Marechiaro a Ostia: cornetto appena sfornato, cappuccino, caff&egrave; e spremuta d&rsquo;arancia fatta al momento.' if it
       else 'Breakfast at the Marechiaro counter on Ostia beach: fresh cornetto, cappuccino, coffee and orange juice squeezed to order.'),
      '/menu-colazione' if it else '/en/menu-breakfast', '/menu-colazione', '/en/menu-breakfast',
      ('Colazione' if it else 'Breakfast',
       'Colazione' if it else 'Breakfast',
       ('Cornetto appena sfornato, cappuccino e spremuta fatta al momento, con il mare davanti.' if it
        else 'Cornetto straight from the oven, cappuccino and juice squeezed to order, with the sea in front of you.')), corpo)

# ═══════════════════════ PRANZO ═══════════════════════
def pranzo(lang):
    it = lang=='it'
    idx = [('proposte','Dal mare' if it else 'From the sea'),
           ('sfizi','Sfizi e fritti' if it else 'Bites &amp; fried'),
           ('insalate','Insalate' if it else 'Salads'),
           ('panini','Panini' if it else 'Sandwiches'),
           ('pizze','Pizze' if it else 'Pizza'),
           ('dolci','Dolci' if it else 'Desserts'),
           ('vini','Vini' if it else 'Wines')]
    corpo = '''
<div class="nastri"><div class="nastro nastro--dx"><span>%s%s</span></div></div>

<div class="menu-corpo">
  %s
  <div class="menu-colonna">

    <section class="giorno riv" id="proposte">
      %s
      <div class="giorno__blocco">
        <header class="menu-testa">
          <span class="menu-n">01</span><h2>%s</h2>
          <span class="menu-alt">%s</span><span class="menu-eti">%s</span>
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
  </div>
</div>
''' % (('Dal mare<i>&mdash;</i>Secondo il pescato del giorno<i>&mdash;</i>Anche da asporto<i>&mdash;</i>' if it
        else 'From the sea<i>&mdash;</i>Following the daily catch<i>&mdash;</i>Takeaway too<i>&mdash;</i>')*2,
       '', indice(idx,lang), ONDA,
       'Dal mare' if it else 'From the sea',
       'From the sea' if it else 'Dal mare',
       'La cucina' if it else 'The kitchen',
       voci(D.PROPOSTE, lang),
       ('La carta segue il mare e pu&ograve; cambiare di giorno in giorno, secondo il pescato. '
        'Per le proposte fuori carta chiedete pure al cameriere: sono quelle arrivate stamattina.' if it
        else 'The menu follows the sea and may change from day to day with the catch. '
             'For the dishes not listed here, just ask your waiter &mdash; they came in this morning.'),
       '\n'.join([
         blocco(2,'sfizi','Sfizi e fritti' if it else 'Bites &amp; fried','Bites &amp; fried' if it else 'Sfizi e fritti','Tutto il giorno' if it else 'All day', D.SFIZI, lang),
         blocco(3,'insalate','Insalate' if it else 'Salads','Salads' if it else 'Insalate','Fresche e abbondanti' if it else 'Fresh and generous', D.INSALATE, lang),
         blocco(4,'panini','Panini' if it else 'Sandwiches','Sandwiches' if it else 'Panini','Pronti e gustosi' if it else 'Ready and tasty', D.PANINI, lang),
         blocco(5,'pizze','Pizze' if it else 'Pizza','Pizza' if it else 'Pizze','Bassa romana' if it else 'Thin Roman style', D.PIZZE, lang,
                'Bassa e croccante, come vuole la tradizione romana.' if it else 'Thin and crispy, true to Roman tradition.'),
         blocco(6,'dolci','Dolci' if it else 'Desserts','Desserts' if it else 'Dolci','Il dolce del giorno' if it else 'Dessert of the day', D.DOLCI_PRANZO, lang),
         blocco(7,'vini','Vini' if it else 'Wines','Wines' if it else 'Vini','Alla bottiglia' if it else 'By the bottle', D.VINI, lang,
                'Bianchi e bollicine, serviti freddi.' if it else 'Whites and sparkling, served chilled.', largo=True),
       ]))
    corpo += legenda(lang)
    corpo += chius('A pranzo' if it else 'At lunch',
      'Al tavolo o sotto l&rsquo;ombrellone' if it else 'At the table or under your umbrella',
      ('Si mangia al ristorante con la vista sul mare, oppure si ordina da asporto e si torna in postazione.' if it
       else 'Eat at the restaurant facing the sea, or order takeaway and head back to your spot.'),
      'Ordina da asporto' if it else 'Order takeaway',
      'Ciao%2C%20vorrei%20ordinare%20da%20asporto' if it else 'Hello%2C%20I%27d%20like%20to%20order%20takeaway',
      'Tutte le carte' if it else 'All the menus', '/menu' if it else '/en/menu')
    scrivi('menu-pranzo.html' if it else 'en/menu-lunch.html', lang,
      'Menu Pranzo sulla Spiaggia | Marechiaro Ostia' if it else 'Lunch Menu on the Beach | Marechiaro Ostia',
      ('Il menu del pranzo al Marechiaro di Ostia: piatti di mare secondo il pescato del giorno, insalate, panini, fritti, pizza e vini. Anche da asporto.' if it
       else 'The lunch menu at Marechiaro on Ostia beach: seafood dishes following the daily catch, salads, sandwiches, fried bites, pizza and wines. Takeaway too.'),
      '/menu-pranzo' if it else '/en/menu-lunch', '/menu-pranzo', '/en/menu-lunch',
      ('Pranzo' if it else 'Lunch',
       'Il pranzo' if it else 'Lunch',
       ('Piatti di mare che seguono il pescato del giorno. Tutto si pu&ograve; ordinare anche da asporto.' if it
        else 'Seafood dishes following the daily catch. Everything can be ordered to take away.')), corpo)

# ═══════════════════════ APERITIVO ═══════════════════════
def aperitivo(lang):
    it = lang=='it'
    idx = [('formule','Le formule' if it else 'Set menus'),('cocktail','Cocktail'),
           ('vini','Vini' if it else 'Wines'),('condividere','Da condividere' if it else 'To share')]
    corpo = '''
<div class="nastri"><div class="nastro nastro--dx"><span>%s%s</span></div></div>

<div class="menu-corpo">
  %s
  <div class="menu-colonna">

    <section class="giorno riv" id="formule">
      %s
      <div class="giorno__blocco">
        <header class="menu-testa">
          <span class="menu-n">01</span><h2>%s</h2>
          <span class="menu-alt">%s</span><span class="menu-eti">%s</span>
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
  </div>
</div>
''' % (('Cocktail e fritti 15&thinsp;&euro;<i>&mdash;</i>Cocktail, tagliere e fritti 18&thinsp;&euro;<i>&mdash;</i>Cocktail alla carta 10&thinsp;&euro;<i>&mdash;</i>Vini e bollicine<i>&mdash;</i>' if it
        else 'Cocktail and fried bites &euro;15<i>&mdash;</i>Cocktail, board and fried bites &euro;18<i>&mdash;</i>Cocktails &agrave; la carte &euro;10<i>&mdash;</i>Wines and sparkling<i>&mdash;</i>')*2,
       '', indice(idx,lang), ONDA,
       'Le formule' if it else 'Set menus',
       'Set menus' if it else 'Le formule',
       'A persona' if it else 'Per person',
       voci(D.FORMULE_APERITIVO, lang),
       ('Prezzi a persona, pi&ugrave; 2&nbsp;&euro; di coperto. Il cocktail si sceglie dalla carta qui sotto.' if it
        else 'Prices per person, plus a &euro;2 cover charge. The cocktail is chosen from the list below.'),
       '\n'.join([
         blocco(2,'cocktail','Cocktail','Cocktails' if it else 'Cocktail','Tutti 10&thinsp;&euro;' if it else 'All &euro;10', D.COCKTAIL, lang,
                ('Ogni cocktail costa 10&nbsp;&euro;. Nessuna sorpresa al conto: scegli quello che ti va.' if it
                 else 'Every cocktail is &euro;10. No surprises on the bill &mdash; just pick the one you fancy.'), unico=True),
         blocco(3,'vini','Vini' if it else 'Wines','Wines' if it else 'Vini','Alla bottiglia' if it else 'By the bottle', D.VINI, lang,
                'Bianchi e bollicine, serviti freddi.' if it else 'Whites and sparkling, served chilled.'),
         blocco(4,'condividere','Da condividere' if it else 'To share','Bites &amp; boards' if it else 'Sfizi e taglieri','In mezzo al tavolo' if it else 'For the middle of the table', D.CONDIVIDERE, lang,
                largo=True),
       ]))
    corpo += legenda(lang)
    corpo += chius('Al tramonto' if it else 'At sunset',
      'Ci vediamo sulla sabbia' if it else 'See you on the sand',
      ('Aperitivo aperto a tutti, anche a chi in spiaggia non c&rsquo;&egrave; stato. Non serve prenotare.' if it
       else "Aperitivo is open to everyone, whether or not you spent the day here. No booking needed."),
      'Scrivici su WhatsApp' if it else 'Message us on WhatsApp',
      'Ciao%2C%20vorrei%20un%20tavolo%20per%20l%27aperitivo' if it else 'Hello%2C%20I%27d%20like%20a%20table%20for%20aperitivo',
      'Le serate' if it else 'The evenings', '/aperitivi' if it else '/en/aperitivo')
    scrivi('menu-aperitivo.html' if it else 'en/menu-aperitivo.html', lang,
      'Aperitivo sul Mare: Formule e Cocktail | Marechiaro' if it else 'Aperitivo by the Sea: Set Menus and Cocktails | Marechiaro',
      ('La carta dell&rsquo;aperitivo al Marechiaro di Ostia: formule da 15&euro; con cocktail e fritti, tagliere, cocktail alla carta a 10&euro;, vini e bollicine.' if it
       else 'The aperitivo list at Marechiaro on Ostia beach: set menus from &euro;15 with cocktail and fried bites, sharing boards, cocktails at &euro;10, wines.'),
      '/menu-aperitivo' if it else '/en/menu-aperitivo', '/menu-aperitivo', '/en/menu-aperitivo',
      ('Aperitivo' if it else 'Aperitivo',
       'L&rsquo;aperitivo' if it else 'Aperitivo',
       ('Due formule con cocktail, fritti e tagliere. Oppure alla carta: ogni cocktail 10&nbsp;&euro;.' if it
        else 'Two set menus with cocktail, fried bites and a sharing board. Or &agrave; la carte: every cocktail &euro;10.')), corpo)

# ═══════════════════════ CENA ═══════════════════════
def cena(lang):
    it = lang=='it'
    idx = [('antipasti','Antipasti' if it else 'Starters'),('primi','Primi' if it else 'First courses'),
           ('secondi','Secondi' if it else 'Main courses'),('pizze','Pizzeria'),
           ('fritti','Fritti' if it else 'Fried bites'),('formula','Menu pizza' if it else 'Pizza menu'),
           ('dolci','Dolci' if it else 'Desserts'),('vini','Vini' if it else 'Wines')]
    corpo = '''
<div class="nastri"><div class="nastro nastro--dx"><span>%s%s</span></div></div>

<div class="menu-corpo">
  %s
  <div class="menu-colonna">

    <section class="giorno riv" id="antipasti">
      %s
      <div class="giorno__blocco">
        <header class="menu-testa">
          <span class="menu-n">01</span><h2>%s</h2>
          <span class="menu-alt">%s</span><span class="menu-eti">%s</span>
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
  </div>
</div>
''' % (('Antipasti di mare<i>&mdash;</i>Primi<i>&mdash;</i>Secondi<i>&mdash;</i>Quattordici pizze bassa romana<i>&mdash;</i>Menu pizza 16&thinsp;&euro;<i>&mdash;</i>Vini<i>&mdash;</i>' if it
        else 'Seafood starters<i>&mdash;</i>First courses<i>&mdash;</i>Main courses<i>&mdash;</i>Fourteen thin Roman pizzas<i>&mdash;</i>Pizza menu &euro;16<i>&mdash;</i>Wines<i>&mdash;</i>')*2,
       '', indice(idx,lang), ONDA,
       'Antipasti' if it else 'Starters',
       'Starters' if it else 'Antipasti',
       'Di mare' if it else 'From the sea',
       voci(D.CENA_ANTIPASTI, lang),
       ('Il pescato cambia con la giornata: se qualcosa manca, il personale ti dice cosa c&rsquo;&egrave; al suo posto.' if it
        else 'The catch changes daily: if something is off, our staff will tell you what we have instead.'),
       '\n'.join([
         blocco(2,'primi','Primi' if it else 'First courses','First courses' if it else 'Primi','Fatti al momento' if it else 'Made to order', D.CENA_PRIMI, lang),
         blocco(3,'secondi','Secondi' if it else 'Main courses','Main courses' if it else 'Secondi','Dal mare alla griglia' if it else 'From the sea to the grill', D.CENA_SECONDI, lang),
         blocco(4,'pizze','Pizzeria','Pizza','Bassa romana' if it else 'Thin Roman style', D.PIZZE_SERA, lang,
                ('Bassa e croccante, come vuole la tradizione romana. Il forno resta acceso fino a tardi.' if it
                 else 'Thin and crispy, true to Roman tradition. The oven stays on until late.'), largo=True),
         blocco(5,'fritti','Fritti' if it else 'Fried bites','Fried bites' if it else 'Fritti','Dal banco' if it else 'From the counter', D.FRITTI, lang),
         blocco(6,'formula','Menu pizza' if it else 'Pizza menu','Pizza menu' if it else 'Menu pizza','A persona' if it else 'Per person', D.FORMULA_PIZZA, lang),
         blocco(7,'dolci','Dolci' if it else 'Desserts','Desserts' if it else 'Dolci','Fatti in casa' if it else 'Made in house', D.DOLCI_CENA, lang),
         blocco(8,'vini','Vini' if it else 'Wines','Wines' if it else 'Vini','Alla bottiglia' if it else 'By the bottle', D.VINI, lang,
                'Bianchi e bollicine, serviti freddi.' if it else 'Whites and sparkling, served chilled.', largo=True),
       ]))
    corpo += legenda(lang)
    corpo += chius('A cena' if it else 'At dinner',
      'Un tavolo con il mare davanti' if it else 'A table facing the sea',
      ('Nei fine settimana e ad agosto conviene prenotare: bastano un messaggio e un&rsquo;ora.' if it
       else 'At weekends and in August it&rsquo;s worth booking &mdash; a message and a time is all we need.'),
      'Prenota un tavolo' if it else 'Book a table',
      'Ciao%2C%20vorrei%20prenotare%20un%20tavolo%20per%20cena' if it else 'Hello%2C%20I%27d%20like%20to%20book%20a%20table%20for%20dinner',
      'Il ristorante' if it else 'The restaurant', '/ristorante' if it else '/en/restaurant')
    scrivi('menu-cena.html' if it else 'en/menu-dinner.html', lang,
      'Menu Cena di Pesce Vista Mare | Marechiaro Ostia' if it else 'Seafood Dinner Menu by the Sea | Marechiaro Ostia',
      ('Il menu della cena al Marechiaro di Ostia: antipasti di mare, primi, secondi alla griglia, quattordici pizze bassa romana, fritti, dolci e vini.' if it
       else 'The dinner menu at Marechiaro on Ostia beach: seafood starters, first courses, grilled mains, fourteen thin Roman pizzas, fried bites and wines.'),
      '/menu-cena' if it else '/en/menu-dinner', '/menu-cena', '/en/menu-dinner',
      ('Cena' if it else 'Dinner',
       'La cena' if it else 'Dinner',
       ('Antipasti di mare, primi fatti al momento, secondi alla griglia. E quattordici pizze bassa romana, per chi la sera preferisce il forno.' if it
        else 'Seafood starters, first courses made to order, grilled mains. And fourteen thin Roman pizzas, if the oven is what you came for.')), corpo)

print('CARTE:')
for f in (hub, colazione, pranzo, aperitivo, cena):
    for lg in ('it','en'): f(lg)
