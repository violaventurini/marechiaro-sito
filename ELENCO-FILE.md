# Marechiaro — tutto quello da rimettere su GitHub

**23 pagine**, 12 italiane e 11 inglesi. Verifica passata: 296 link controllati, zero errori.

---

## Radice del repository

### Pagine italiane (12)
- [ ] `index.html` — home
- [ ] `spiaggia.html`
- [ ] `ristorante.html`
- [ ] `aperitivi.html`
- [ ] `feste-gruppi.html`
- [ ] `contatti.html`
- [ ] `menu.html` — **smistamento del QR**
- [ ] `menu-colazione.html`
- [ ] `menu-pranzo.html`
- [ ] `menu-aperitivo.html`
- [ ] `menu-cena.html`
- [ ] `404.html`

### Stile, script e icone (4)
- [ ] `avorio.css`
- [ ] `avorio.js`
- [ ] `favicon.svg`
- [ ] `apple-touch-icon.png`

### Google e Netlify (3)
- [ ] `robots.txt`
- [ ] `sitemap.xml` — 22 URL
- [ ] `_redirects`

---

## Cartella `en/` (11 pagine)
`index` · `beach` · `restaurant` · `aperitivo` · `groups` · `find-us`
`menu` · `menu-breakfast` · `menu-lunch` · `menu-aperitivo` · `menu-dinner`

## Cartella `img/` (17 file)
Quindici foto pi&ugrave; i due logo SVG. Senza, il sito si apre ma resta vuoto.

## Cartella `_strumenti/`
Non viene pubblicata. Contiene `carta.py` con tutti i piatti e i prezzi: cambi un prezzo l&igrave;,
lanci `costruisci-carte.py`, e le dieci carte si aggiornano in italiano e inglese insieme.

---

## Se hai gi&agrave; caricato la versione precedente

Sono cambiati **tutti** i file HTML pi&ugrave; `avorio.css` e `sitemap.xml`. Le cinque pagine del
menu (`menu-*.html` e le corrispondenti in `en/`) sono **nuove**: prima non esistevano.

Il modo pi&ugrave; sicuro &egrave; sostituire tutto in blocco con l&rsquo;archivio completo.

---

## Come caricare

**Trascina le cartelle, non il loro contenuto.** Prima di confermare, GitHub elenca i file:
le righe devono iniziare con `en/` e `img/`. Se leggi `index.html` o `menu.html` senza
prefisso, annulla &mdash; sono i due nomi che esistono in entrambe le lingue.

---

## Dopo il deploy, prova questi indirizzi

`/` `/spiaggia` `/ristorante` `/aperitivi` `/feste-gruppi` `/contatti`
`/menu` `/menu-colazione` `/menu-pranzo` `/menu-aperitivo` `/menu-cena`
`/en/` `/en/beach` `/en/restaurant` `/en/aperitivo` `/en/groups` `/en/find-us`
`/en/menu` `/en/menu-breakfast` `/en/menu-lunch` `/en/menu-aperitivo` `/en/menu-dinner`

Poi Search Console &rarr; Sitemap &rarr; rileggi `sitemap.xml`: deve passare a **22 URL**.

---

## Cosa resta aperto

- **Prezzo del tagliere** venduto da solo: unica voce del menu senza cifra
- Conferma sui **dolci della sera a 8&nbsp;&euro;** (a pranzo gli stessi sono 6 e 5)
- **Listino spiaggia**: oggi le righe rimandano a WhatsApp
- Dal **16 agosto**: togliere il richiamo Ferragosto e la sezione in home
