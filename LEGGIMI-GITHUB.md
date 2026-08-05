# Marechiaro — sito completo, pronto da pubblicare

Ultima verifica: 4 agosto 2026. **15 pagine, zero errori, zero link rotti.**

---

## PASSO 1 — Svuota il repository

Nel repository ci sono ancora le pagine vecchie. Se restano, convivono due siti diversi
e Netlify ne pubblica un misto.

**Cancella tutto** quello che c'è adesso nella radice, in particolare:
`index.html`, `spiaggia.html`, `menu.html`, `aperitivi.html`, `feste-gruppi.html`,
`contatti.html`, `style.css`, `script.js`, e la vecchia cartella `img/`.

## PASSO 2 — Copia questa cartella nella radice

Non dentro una sottocartella: i file devono stare al primo livello del repository.

```
repository/
├── index.html            home italiana
├── spiaggia.html         → /spiaggia
├── ristorante.html       → /ristorante
├── menu.html             → /menu
├── aperitivi.html        → /aperitivi
├── feste-gruppi.html     → /feste-gruppi
├── contatti.html         → /contatti
├── 404.html              pagina di errore
├── avorio.css            foglio di stile unico
├── avorio.js             animazioni e quadrante
├── favicon.svg
├── apple-touch-icon.png
├── robots.txt
├── sitemap.xml
├── en/
│   ├── index.html        → /en/
│   ├── beach.html        → /en/beach
│   ├── restaurant.html   → /en/restaurant
│   ├── menu.html         → /en/menu
│   ├── aperitivo.html    → /en/aperitivo
│   ├── groups.html       → /en/groups
│   └── find-us.html      → /en/find-us
├── img/                  17 file: foto, logo bianco, logo rosso, immagine social
└── _strumenti/           NON viene pubblicato: serve a te per rigenerare i menu
```

Netlify serve `spiaggia.html` all'indirizzo `/spiaggia` da solo. Non devi configurare nulla.

## PASSO 3 — Push

Il deploy parte automaticamente. **Carica tutto insieme, non serve dividere niente.**

Nella cartella c'è un file `_redirects`: fa in modo che questo LEGGIMI e la cartella
`_strumenti` restino nel repository ma **non siano raggiungibili online**. Senza di lui
chiunque potrebbe aprire `marechiaroostia.it/_strumenti/piano-indicizzazione.md` e leggersi
il tuo piano SEO. Con lui, riceve la 404. Il `robots.txt` dice la stessa cosa a Google.

Se il repository su GitHub è privato, il codice non si vede comunque: ma il sito
pubblicato sì, ed è quello il punto.

---

## Cosa NON caricare

I file `anteprima-*.html` che ti ho mostrato in chat. Hanno le immagini incorporate,
pesano quattro volte tanto e non servono online.

---

## Dopo il primo deploy

1. Verifica che il sito risponda **senza** `www` (o solo con: scegline una e reindirizza l'altra)
2. Search Console → invia `https://marechiaroostia.it/sitemap.xml`
3. Controllo URL → scheda *HTML sottoposto a rendering*: devi leggere il titolo dell'hero
   e il testo delle FAQ. Se li leggi, li legge anche Google
4. Passa la home dal Rich Results Test

---

## Cos'è già dentro, che non devi aggiungere

- **Dati strutturati** nel `<head>` di ogni pagina: attività, ristorante con orari separati
  pranzo e cena, catalogo spiaggia con la tariffa giovani a 8 €, formule eventi a 15/20/28 €,
  FAQ generate dal testo visibile in pagina, briciole di navigazione
- **hreflang** reciproci su tutte le coppie italiano/inglese
- **Canonical** su ogni pagina
- **Favicon e icona iOS** ricavate dal logo vettoriale
- **404** con lo stesso impianto grafico e quattro scorciatoie

---

## Gli unici buchi rimasti — servono i tuoi numeri

1. **Listino spiaggia**: ombrellone con due lettini feriale e weekend, lettone matrimoniale,
   sdraio, cabina giornaliera, abbonamento mensile e stagionale.
   Al momento le righe dicono «Chiedi il prezzo» e portano su WhatsApp: funziona, ma i prezzi
   in chiaro valgono molto di più. «Prezzi spiaggia Ostia» è tra le ricerche più fatte del
   litorale e quasi nessuno li pubblica.
2. **Menu della sera**: i dodici piatti ci sono, i prezzi no.
3. **Le quattro pizze** in carta: Margherita, Diavola, Marinara, Napoli.
4. **Allergeni** di insalata di mare, spaghetti al pomodoro e frutta.

Il menu vive in un file solo, `_strumenti/menu-dati.py`. Cambi i prezzi lì, lanci
`python3 _strumenti/genera-menu.py` e italiano e inglese si aggiornano insieme: non
potranno mai divergere.

---

## La cosa che conta più del sito

Le **due schede Google** allo stesso indirizzo vanno unite. Finché sono due, le 244
recensioni storiche non lavorano per te e l'autorità si divide. Dieci minuti, gratis,
da «Segnala un duplicato» sulla scheda vecchia.

Poi sulla scheda servono le categorie secondarie **Ristorante** e **Pizzeria**: senza,
non compari mai a chi cerca dove mangiare — ed è lì che guarda il turista, non nei
risultati blu.
