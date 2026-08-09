# Perch&eacute; il sito online non funziona &mdash; e come sistemarlo

I file di questo archivio sono verificati: 23 pagine, 42 risorse richiamate, **zero errori**.
Se online non funziona, il caricamento &egrave; incompleto. Sono **134 file**: se ne mancano alcuni,
il sito si apre ma resta rotto.

---

## La causa quasi certa: le immagini

La cartella `img/` contiene ora **95 file**, non pi&ugrave; 17. Ogni foto esiste in WebP e JPEG a tre
larghezze diverse, perch&eacute; il browser scelga la pi&ugrave; leggera. Se hai caricato solo l&rsquo;HTML,
il sito cerca 42 immagini che non ci sono e resta vuoto.

**Verifica in dieci secondi.** Apri:

```
marechiaroostia.it/img/stabilimento-marechiaro-ostia-1600.jpg
```

Se dà 404, la cartella `img/` non &egrave; aggiornata. &Egrave; questa la causa.

---

## Il secondo sospetto: il foglio di stile

Le sezioni nuove della home &mdash; ristorante, spiaggia, la sera, evento &mdash; usano regole che
esistono solo nel nuovo `avorio.css`. Se hai caricato `index.html` senza `avorio.css`, la pagina
esce scomposta.

Stessa cosa per `avorio.js`: senza, l&rsquo;orologio non gira e il menu del telefono non si apre.

---

## Il terzo: pagine miste

Se alcune pagine sono nuove e altre vecchie, la navigazione punta a indirizzi diversi e il
selettore di lingua manda nel posto sbagliato. **Vanno sostituite tutte insieme**, non una alla volta.

---

## Come caricare, questa volta

Il modo sicuro &egrave; **sostituire l&rsquo;intero contenuto della radice**:

1. Scompatta l&rsquo;archivio
2. Su GitHub carica **tutto insieme**: i file di radice, la cartella `en`, la cartella `img`
3. Conferma il commit
4. Su Netlify controlla che il deploy sia **Published** e che il numero del commit corrisponda

---

## Le sei prove da fare dopo il deploy

- [ ] `marechiaroostia.it/img/stabilimento-marechiaro-ostia-1600.jpg` &rarr; si vede la foto
- [ ] `marechiaroostia.it/` &rarr; la foto in apertura c&rsquo;&egrave;, e scorrendo il quadrante gira
- [ ] `marechiaroostia.it/menu-cena` &rarr; sette sezioni, tutte con i prezzi
- [ ] `marechiaroostia.it/en/menu-dinner` &rarr; stesse voci e stessi prezzi dell&rsquo;italiano
- [ ] `marechiaroostia.it/menu-colazione` &rarr; dice **dalle 9**
- [ ] Dal telefono: il pulsante del menu si apre e si chiude

Se dopo il caricamento completo qualcosa ancora non va, mandami l&rsquo;indirizzo esatto della
pagina e cosa vedi: cos&igrave; guardo quel file invece di tirare a indovinare.
