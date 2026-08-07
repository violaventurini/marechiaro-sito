# Marechiaro — tutti i file da mettere su GitHub

**23 pagine, 12 italiane e 11 inglesi.** Verifica passata: zero errori, zero link rotti.

---

## Radice del repository

### Pagine italiane (12)
- [ ] `index.html` — home
- [ ] `spiaggia.html` → `/spiaggia`
- [ ] `ristorante.html` → `/ristorante`
- [ ] `aperitivi.html` → `/aperitivi`
- [ ] `feste-gruppi.html` → `/feste-gruppi`
- [ ] `contatti.html` → `/contatti`
- [ ] `menu.html` → `/menu` — **smistamento del QR, quattro pulsanti**
- [ ] `menu-colazione.html` → `/menu-colazione`
- [ ] `menu-pranzo.html` → `/menu-pranzo`
- [ ] `menu-aperitivo.html` → `/menu-aperitivo`
- [ ] `menu-cena.html` → `/menu-cena`
- [ ] `404.html` — pagina di errore

### Stile, script e icone (4)
- [ ] `avorio.css`
- [ ] `avorio.js`
- [ ] `favicon.svg`
- [ ] `apple-touch-icon.png`

### File per Google e Netlify (3)
- [ ] `robots.txt`
- [ ] `sitemap.xml` — 22 URL
- [ ] `_redirects` — tiene fuori dal sito pubblico il LEGGIMI e gli strumenti

---

## Cartella `en/` (11 pagine)
- [ ] `en/index.html` → `/en/`
- [ ] `en/beach.html` → `/en/beach`
- [ ] `en/restaurant.html` → `/en/restaurant`
- [ ] `en/aperitivo.html` → `/en/aperitivo`
- [ ] `en/groups.html` → `/en/groups`
- [ ] `en/find-us.html` → `/en/find-us`
- [ ] `en/menu.html` → `/en/menu`
- [ ] `en/menu-breakfast.html` → `/en/menu-breakfast`
- [ ] `en/menu-lunch.html` → `/en/menu-lunch`
- [ ] `en/menu-aperitivo.html` → `/en/menu-aperitivo`
- [ ] `en/menu-dinner.html` → `/en/menu-dinner`

## Cartella `img/` (17 file)
Le 15 foto pi&ugrave; i due logo SVG, bianco e rosso. Senza questa cartella il sito si apre ma resta vuoto.

## Cartella `_strumenti/`
Non viene pubblicata (ci pensa `_redirects`). Contiene `carta.py` con tutti i piatti e i prezzi:
cambi un prezzo l&igrave;, lanci `costruisci-carte.py` e le dieci carte si aggiornano in italiano e inglese insieme.

---

## Come caricare

Tre archivi separati, cos&igrave; puoi andare per gradi:

1. **`marechiaro-sito-completo.zip`** — tutto insieme, da scompattare e copiare in radice
2. **`cartella-en.zip`** — solo la cartella `en`
3. **`cartella-img.zip`** — solo la cartella `img`

Regola d&rsquo;oro: **trascina le cartelle, non il loro contenuto.** Prima di confermare, GitHub
elenca i file: le righe devono iniziare con `en/` e `img/`. Se leggi `index.html` o `menu.html`
senza prefisso, annulla &mdash; stai per sovrascrivere le pagine italiane.

---

## Dopo il deploy

Prova questi indirizzi, devono aprirsi tutti:

`/` &middot; `/spiaggia` &middot; `/ristorante` &middot; `/aperitivi` &middot; `/feste-gruppi` &middot; `/contatti`
`/menu` &middot; `/menu-colazione` &middot; `/menu-pranzo` &middot; `/menu-aperitivo` &middot; `/menu-cena`
`/en/` &middot; `/en/beach` &middot; `/en/restaurant` &middot; `/en/aperitivo` &middot; `/en/groups` &middot; `/en/find-us`
`/en/menu` &middot; `/en/menu-breakfast` &middot; `/en/menu-lunch` &middot; `/en/menu-aperitivo` &middot; `/en/menu-dinner`

Poi Search Console &rarr; Sitemap &rarr; rileggi `sitemap.xml`: da 14 URL deve passare a 22.

**Il QR punta a `/menu`**: da l&igrave; si smista sulle quattro carte. Non serve rigenerarlo.

---

## Cosa manca ancora

- Il **prezzo del tagliere** venduto da solo: unica voce senza cifra
- Conferma sui **dolci della sera a 8&nbsp;&euro;** (a pranzo gli stessi sono 6 e 5)
- Il **listino della spiaggia**: le righe rimandano a WhatsApp, ma i prezzi in chiaro varrebbero molto di pi&ugrave;
- Dal **16 agosto** vanno tolti il richiamo Ferragosto in basso a destra e la sezione in home
