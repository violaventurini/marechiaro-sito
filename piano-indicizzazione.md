# Marechiaro — piano di indicizzazione completo

Contesto: stabilimento riaperto da poco, autorità di dominio prossima allo zero,
concorrenza fatta di aggregatori con dieci anni di anzianità. Obiettivo: utenza
numerosa **e** di qualità, su quattro intenti diversi — spiaggia, pranzo, aperitivo, cena.

Il principio che regge tutto il piano: **non esiste una pagina che possa
posizionarsi su quattro intenti insieme.** Chi cerca "lettini Ostia prezzi" e chi cerca
"ristorante vista mare Ostia" sono due persone diverse, in due momenti diversi, con due
bisogni diversi. Servono quattro pagine forti, non una home che le contiene tutte.

---

## 1. Cosa è cambiato in Google, e che impatto ha su di te

**I FAQ rich results non esistono più.** Il 7 maggio 2026 Google ha messo un avviso di
deprecazione in cima alla documentazione: i risultati avanzati FAQ non compaiono più nella
Ricerca. Il report in Search Console e il supporto nel Rich Results Test spariscono a
giugno 2026, l'API ad agosto.

Cosa significa in pratica per noi:

- Il markup `FAQPage` resta valido e **non danneggia** il sito. Lo teniamo.
- Ma **non aspettarti più le tendine a fisarmonica sotto il tuo risultato**. Quel vantaggio
  visivo è finito per tutti, anche per i siti governativi e sanitari che erano rimasti gli
  ultimi ad averlo.
- Quindi le FAQ vanno scritte **per le persone**, non per lo snippet. Domande formulate come
  le fa un cliente, risposta nella prima frase, niente riempitivi. È esattamente come le ho
  scritte in pagina.

Sui meta tag la situazione è stabile e vale la pena essere chiari su cosa conta davvero:

| Tag | Conta? | Perché |
|---|---|---|
| `<title>` | **Sì, molto** | È il segnale on-page dichiarativo più forte, ed è il testo blu cliccabile |
| `meta description` | Indirettamente | Non è fattore di ranking, ma decide il click. Google la riscrive spesso, non sempre |
| `canonical` | **Sì** | Evita che due URL si facciano concorrenza |
| `robots` | **Sì** | Controlla indicizzazione e anteprime |
| `hreflang` | **Sì, per te** | Con IT ed EN è obbligatorio, altrimenti sono contenuti duplicati |
| `viewport`, `charset` | Tecnici | Senza, il sito non funziona su mobile |
| `meta keywords` | **No** | Ignorato da vent'anni. Non metterlo |
| `revisit-after`, `author`, `rating` | No | Reperti archeologici |

---

## 2. Architettura: sette pagine, quattro intenti

```
/                          marchio + smistamento verso i quattro intenti
├── /spiaggia              INTENTO 1 · lettini, lettoni, sdraio, ombrelloni, PREZZI
├── /ristorante            INTENTO 2 + 4 · pranzo, asporto, cena, pizzeria vista mare
│   └── #asporto           ancora dedicata al take away
├── /menu                  supporto a /ristorante
├── /aperitivi             INTENTO 3 · aperitivo al tramonto, serate
├── /feste-gruppi          compleanni, gruppi, eventi privati
└── /contatti              come arrivare, orari

/en/                       versione inglese
├── /en/beach
└── /en/restaurant
```

Tre pagine da creare: `/ristorante`, `/en/`, `/en/beach`, `/en/restaurant`.
`/ristorante` è la più urgente in assoluto: oggi manca del tutto, e con lei manca metà
del fatturato potenziale dal digitale.

---

## 3. SEO interna: come i link si passano forza

È la parte che quasi nessuno cura e che per un sito nuovo conta più dei backlink, perché
è l'unica leva che controlli al 100%.

### Le tre regole

1. **Ancore descrittive, mai "clicca qui".** Google usa il testo del link per capire di cosa
   parla la pagina di destinazione. Un link che dice *"lettini e ombrelloni"* vale cento
   volte uno che dice *"scopri di più"*.
2. **Ogni pagina deve essere raggiungibile in massimo due click dalla home.** Lo è già.
3. **Nessuna parola chiave su due pagine.** Se "pranzo sul mare Ostia" compare come titolo
   sia in home che su `/ristorante`, le due pagine si cannibalizzano e Google non sa quale
   mostrare. Vince nessuna delle due.

### Mappa dei link interni da mettere in pagina

| Da | A | Testo del link |
|---|---|---|
| Home → | /spiaggia | lettini e ombrelloni · vedi i prezzi |
| Home → | /ristorante | ristorante e pizzeria · il ristorante |
| Home → | /ristorante#asporto | pranzo e asporto |
| Home → | /aperitivi | aperitivo al tramonto |
| Home → | /feste-gruppi | feste e gruppi |
| FAQ home → | /spiaggia | listino prezzi spiaggia |
| FAQ home → | /spiaggia#abbonamenti | abbonamenti stagionali |
| /spiaggia → | /ristorante#asporto | pranzo da asporto sotto l'ombrellone |
| /spiaggia → | /contatti | come arrivare da Roma |
| /ristorante → | /menu | il menu completo |
| /ristorante → | /aperitivi | aperitivo prima di cena |
| /aperitivi → | /ristorante | cena e pizzeria vista mare |
| /menu → | /ristorante | prenota un tavolo vista mare |
| /feste-gruppi → | /menu | menu per gruppi |
| Ogni pagina → | / | logo (già fatto) |

Regola d'oro: **da ogni pagina almeno due link in uscita verso altre pagine tue**, con
ancore diverse. Un sito dove tutto punta solo alla home è un sito piatto.

---

## 4. Meta tag, pagina per pagina — pronti da incollare

Title entro 60 caratteri, description entro 158. La parola chiave all'inizio del title,
il marchio alla fine dopo il `|`.

### `/` — home
```html
<title>Marechiaro Ostia | Spiaggia e Ristorante sul Mare</title>
<meta name="description" content="Stabilimento balneare a Ostia: lettini, lettoni, sdraio e ombrelloni, pranzo anche da asporto, aperitivi e pizzeria vista mare. A 30 minuti da Roma.">
```
**H1:** Il mare di Roma

### `/spiaggia`
```html
<title>Lettini, Lettoni e Ombrelloni a Ostia | Marechiaro</title>
<meta name="description" content="Noleggio lettini, lettoni matrimoniali, sdraio, ombrelloni e cabine sulla spiaggia di Ostia. Prezzi giornalieri feriali e weekend, abbonamenti stagionali.">
```
**H1:** Lettini, ombrelloni e cabine sulla spiaggia di Ostia

### `/ristorante`
```html
<title>Ristorante e Pizzeria Vista Mare a Ostia | Marechiaro</title>
<meta name="description" content="Ristorante e pizzeria con vista mare sul lungomare di Ostia. Pranzo in spiaggia anche da asporto dalle 13, pizza dalle 17, cena fino a tardi.">
```
**H1:** Ristorante e pizzeria vista mare a Lido di Ostia

### `/menu`
```html
<title>Menu Ristorante e Pizzeria | Marechiaro Ostia</title>
<meta name="description" content="Il menu del Marechiaro a Ostia: primi e secondi di mare, pizza dalle 17, panini e insalate a pranzo, taglieri per l'aperitivo. Anche da asporto.">
```
**H1:** Il menu del Marechiaro

### `/aperitivi`
```html
<title>Aperitivo al Tramonto sul Mare a Ostia | Marechiaro</title>
<meta name="description" content="Aperitivo sulla spiaggia di Ostia dalle 18: cocktail al tramonto, dj set e serate sulla sabbia. Aperto anche a chi non è stato in spiaggia.">
```
**H1:** Aperitivo al tramonto sulla spiaggia di Ostia

### `/feste-gruppi`
```html
<title>Feste, Gruppi ed Eventi sul Mare | Marechiaro Ostia</title>
<meta name="description" content="Compleanni, cene di gruppo ed eventi privati sulla spiaggia di Ostia. Tavolo sotto il gazebo vista mare e menu concordato. Su prenotazione.">
```
**H1:** Feste, gruppi ed eventi sulla spiaggia di Ostia

### `/contatti`
```html
<title>Dove Siamo e Orari | Marechiaro, Lido di Ostia</title>
<meta name="description" content="Marechiaro, Lungomare Paolo Toscanelli 27, Lido di Ostia. Come arrivare da Roma in auto o col treno Roma-Lido, orari e contatti. Aperti dalle 8:30.">
```
**H1:** Dove siamo e come arrivare

### `/en/`
```html
<title>Beach Club near Rome | Marechiaro Ostia</title>
<meta name="description" content="Beach club 30 minutes from Rome. Sunbeds, double sunbeds and umbrellas on Ostia beach, seafront restaurant, pizzeria and sunset aperitivo. Free beach access.">
```
**H1:** Rome's own sea

### `/en/beach`
```html
<title>Sunbeds and Umbrellas on Ostia Beach | Marechiaro</title>
<meta name="description" content="Hire sunbeds, double sunbeds, deckchairs and umbrellas on Ostia beach near Rome. Daily prices, seasonal passes, free beach access, 35 minutes by train.">
```
**H1:** Sunbeds and umbrellas on Ostia beach

### `/en/restaurant`
```html
<title>Seafront Restaurant and Pizzeria in Ostia | Marechiaro</title>
<meta name="description" content="Seafront restaurant and pizzeria at Lido di Ostia, near Rome. Lunch on the beach and takeaway from 1pm, pizza from 5pm, dinner facing the sea.">
```
**H1:** Seafront restaurant and pizzeria in Ostia

**Su ogni pagina servono anche i tag hreflang**, altrimenti Google considera IT ed EN
contenuti duplicati e ne sceglie uno solo:
```html
<link rel="alternate" hreflang="it" href="https://marechiaroostia.it/spiaggia">
<link rel="alternate" hreflang="en" href="https://marechiaroostia.it/en/beach">
<link rel="alternate" hreflang="x-default" href="https://marechiaroostia.it/spiaggia">
```

---

## 5. Coprire più aree geografiche

Non servono pagine finte per ogni quartiere — quella tattica Google la penalizza dal 2012.
Serve **contenuto vero sulle distanze**, ed è quello che ho messo in home nella sezione
"Quanto ci metti ad arrivare": Roma centro, EUR, Infernetto, Casal Palocco, Axa, Acilia,
Dragona, Ostia Antica, Fiumicino.

Perché funziona: chi cerca *"spiaggia vicino Infernetto"* o *"mare vicino EUR"* trova una
pagina che nomina il suo quartiere **e** gli dice il tempo di percorrenza. È un contenuto
che nessun aggregatore ha, perché gli aggregatori non conoscono la geografia locale.

Nella versione inglese le aree sono diverse, perché il turista straniero ragiona per
attrazioni e non per quartieri: centro storico, Colosseo e Termini, aeroporto di Fiumicino,
scavi di Ostia Antica. L'abbinamento **rovine la mattina, spiaggia il pomeriggio** è una
ricerca reale e nessuno la presidia.

Nei dati strutturati questo si dichiara con `areaServed`.

---

## 6. Grappoli di parole chiave, una per pagina

**`/spiaggia`** — stabilimento balneare Ostia · lettini e ombrelloni Ostia · noleggio lettini
Ostia · lettone matrimoniale spiaggia Ostia · sdraio e ombrellone Ostia prezzi · prezzi
spiaggia Ostia 2026 · spiaggia attrezzata Ostia · cabine Ostia · abbonamento stagionale
spiaggia Roma · spiaggia vicino Roma

**`/ristorante`** — ristorante vista mare Ostia · pizzeria vista mare Ostia · ristorante sulla
spiaggia Ostia · pranzo sul mare Ostia · mangiare in spiaggia Ostia · pizza d'asporto Ostia ·
pranzo da asporto Ostia · cena sulla spiaggia Ostia · pizzeria lungomare Toscanelli

**`/aperitivi`** — aperitivo sul mare Ostia · aperitivo al tramonto Ostia · aperitivo in spiaggia
Roma · beach club Ostia · dj set spiaggia Ostia

**`/en/`** — beach near Rome · rome beach day trip · beach club rome · ostia beach ·
best beach near rome · rome seaside

**`/en/restaurant`** — beach restaurant rome · seafront restaurant ostia · pizzeria with sea
view rome · lunch on the beach rome

---

## 7. Perché questo sito è leggibile da Google

Domanda giusta, perché un sito molto animato spesso **non** lo è. Qui abbiamo evitato tre
trappole:

1. **Il titolo dell'hero è testo vero nell'HTML.** All'inizio lo costruiva il JavaScript
   lettera per lettera: significa che un crawler che non esegue script vedeva un `<h1>` vuoto.
   Ora le parole stanno nel sorgente e l'animazione è solo CSS.
2. **Il modulo "La giornata" è testo statico.** Le cinque fasi — 8:30, 13, 17, 18, 20:30 —
   esistono nell'HTML anche a JavaScript spento. Il sole e il cielo sono decorazione.
3. **Le FAQ usano `<details>` nativi**, non un accordion in JavaScript. Il testo delle
   risposte è nel sorgente e viene indicizzato anche da chiuso.

Verifica tu stessa: apri la pagina, tasto destro, *Visualizza sorgente*. Se leggi i testi
lì dentro, li legge anche Google. Poi conferma con lo strumento **Controllo URL** di Search
Console, scheda *HTML sottoposto a rendering*.

---

## 8. Checklist tecnica

- [ ] `sitemap.xml` in radice, con i blocchi hreflang (file pronto)
- [ ] `robots.txt` in radice che punta alla sitemap (file pronto)
- [ ] Search Console: proprietà verificata, sitemap inviata, indicizzazione richiesta per le pagine nuove
- [ ] Un solo `<h1>` per pagina
- [ ] Nessun title o description duplicato tra pagine — è l'errore più comune
- [ ] Immagini in WebP, sotto i 250 KB, con `alt` descrittivo e nome file parlante
- [ ] `loading="lazy"` ovunque tranne l'immagine dell'hero, che ha `fetchpriority="high"`
- [ ] HTTPS e redirect da `www` alla versione senza (o viceversa, ma una sola)
- [ ] Pagina 404 personalizzata con link alle pagine principali
- [ ] Test su Core Web Vitals da mobile: i tuoi visitatori arrivano quasi tutti da telefono

---

## 9. Google Maps — dove si gioca davvero la partita

Per "ristorante vista mare Ostia" il turista guarda la mappa, non i risultati blu. Il sito
serve, ma da solo non basta.

1. **Le due schede doppie vanno unite.** Ce ne sono due allo stesso indirizzo: quella storica
   con 244 recensioni e quella della nuova gestione. Finché convivono, l'autorità si divide e
   le recensioni vecchie non lavorano per te. Da "Segnala un duplicato" sulla scheda vecchia.
   **Questa è la singola azione con il miglior rapporto tra impatto e costo di tutto il piano.**
2. **Categorie.** Primaria *Stabilimento balneare*; secondarie *Ristorante*, *Pizzeria*, *Bar*.
   Senza la categoria Ristorante non compari mai a chi cerca da mangiare.
3. **Attributi:** vista mare, posti all'aperto, asporto, accessibile in sedia a rotelle,
   adatto alle famiglie.
4. **Orari separati per reparto**, così Maps mostra "aperto adesso" correttamente anche la sera.
5. **Foto ogni settimana** in stagione: è il segnale che Google usa per capire se un'attività è viva.
6. **Recensioni:** chiedile al momento del conto, con il QR degli adesivi. Venti recensioni
   fresche valgono più di qualsiasi ottimizzazione in questo documento.

---

## 10. Ordine di esecuzione

| # | Azione | Impatto | Costo |
|---|---|---|---|
| 1 | Unione schede Google + categorie Ristorante/Pizzeria | Altissimo | Zero |
| 2 | Prezzi reali in chiaro su `/spiaggia` e nelle FAQ | Altissimo | Un'ora |
| 3 | Creare `/ristorante` | Alto | Mezza giornata |
| 4 | Title e description su tutte le pagine | Alto | Un'ora |
| 5 | Dati strutturati aggiornati | Medio | Mezz'ora |
| 6 | Sitemap + Search Console | Medio | Venti minuti |
| 7 | Versione inglese completa | Medio-alto in estate | Un giorno |
| 8 | Foto professionali con nomi file parlanti | Medio, cresce nel tempo | Uno shooting |

I **prezzi in chiaro** restano la cosa più sottovalutata: "prezzi spiaggia Ostia" è tra le
ricerche più fatte del litorale e quasi nessuno pubblica le cifre. Chi lo fa vince il click,
e vince anche il cliente, perché arriva già informato e non discute alla cassa.
