/* ============================================================
   MARECHIARO — "Che tipo da Marechiaro sei?"
   Quiz con il granchietto: niente risposte giuste o sbagliate,
   alla fine il profilo e un consiglio su come vivere il Marechiaro.
   All'inizio si raccolgono nome ed email (newsletter): ogni iscrizione va
   nella lista Brevo (netlify/functions/iscrizione.mjs) e, come copia,
   in Netlify → Forms → "newsletter-gioco".
   Domande, profili e frasi si cambiano qui sotto.
   ============================================================ */
(function(){
  var box = document.getElementById('gioco');
  if (!box) return;
  var en = (document.documentElement.lang || 'it').indexOf('en') === 0;
  var WA = 'https://wa.me/393484059720?text=';

  /* ogni risposta assegna un punto a un profilo:
     L = lettino, T = tramonto, P = palato, V = viaggio, F = festa */
  var DOMANDE = en ? [
    { q: 'You arrive at the beach. What’s the first thing you do?', a: [['I lie down and don’t move again', 'L'], ['I check what’s for lunch', 'P'], ['I look for the spot with the best view', 'T'], ['I drop my suitcase and run into the sea', 'V']] },
    { q: 'Your ideal company for a day by the sea?', a: [['A good book', 'L'], ['My closest friends: the more the merrier', 'F'], ['Someone who loves good food as much as I do', 'P'], ['Whoever I meet along the way', 'V']] },
    { q: 'It’s midday. For you, lunch is…', a: [['Something fresh to take away, eaten in the shade', 'L'], ['A table facing the sea and the catch of the day', 'P'], ['An early aperitivo, why not', 'T'], ['Quick, I have a plane to catch', 'V']] },
    { q: 'Sunset finds you…', a: [['With a cocktail in hand', 'T'], ['Still on the sunbed, eyes closed', 'L'], ['Raising a glass with the whole group', 'F'], ['Choosing the wine for dinner', 'P']] },
    { q: 'Your souvenir of the summer?', a: [['A photo at sunset', 'T'], ['The perfect tan', 'L'], ['The memory of a dish', 'P'], ['A birthday nobody will forget', 'F']] },
    { q: 'What’s always in your suitcase?', a: [['My passport', 'V'], ['Something elegant for the evening', 'T'], ['A book I never finish', 'L'], ['Everything we need for the party', 'F']] }
  ] : [
    { q: 'Arrivi al mare. Qual è la prima cosa che fai?', a: [['Mi stendo e non mi muovo più', 'L'], ['Guardo cosa c’è per pranzo', 'P'], ['Cerco il punto con la vista più bella', 'T'], ['Lascio la valigia e corro in acqua', 'V']] },
    { q: 'La compagnia ideale per una giornata al mare?', a: [['Un buon libro', 'L'], ['Gli amici di sempre: più siamo, meglio è', 'F'], ['Chi ama la buona tavola quanto me', 'P'], ['Chi incontro strada facendo', 'V']] },
    { q: 'È mezzogiorno. Il pranzo, per te, è…', a: [['Qualcosa di fresco da asporto, da gustare all’ombra', 'L'], ['Un tavolo vista mare e il pesce del giorno', 'P'], ['Un aperitivo in anticipo, perché no', 'T'], ['Veloce, ho un aereo da prendere', 'V']] },
    { q: 'Il tramonto ti trova…', a: [['Con un cocktail in mano', 'T'], ['Ancora sul lettino, a occhi chiusi', 'L'], ['A brindare con tutto il gruppo', 'F'], ['A scegliere il vino per la cena', 'P']] },
    { q: 'Il tuo ricordo dell’estate?', a: [['Una foto al tramonto', 'T'], ['L’abbronzatura perfetta', 'L'], ['Il sapore di un piatto', 'P'], ['Un compleanno che nessuno dimenticherà', 'F']] },
    { q: 'In valigia non manca mai…', a: [['Il passaporto', 'V'], ['Qualcosa di elegante per la sera', 'T'], ['Un libro che non finisco mai', 'L'], ['Tutto il necessario per la festa', 'F']] }
  ];

  /* i profili: la giornata usa solo quello che il Marechiaro offre davvero */
  var PROFILI = en ? {
    L: { t: 'Sunbed and silence', d: 'For you, the sea is a pause: the sound of the waves, a good book, no hurry at all.',
         g: [['Morning', 'A double sunbed under a well-spaced umbrella.'], ['Lunch', 'Something fresh to take away, enjoyed in the shade.'], ['Evening', 'A shower in the beach hut and a glass of Falanghina facing the sea.']],
         c: ['Ask us on WhatsApp', WA + 'Hello%2C%20I%27m%20contacting%20you%20from%20your%20website%20and%20I%27d%20like%20some%20information%20about%20the%20beach.'] },
    T: { t: 'Spirit of the sunset', d: 'Your moment is when the sun goes down and the light turns gold.',
         g: [['Afternoon', 'One last swim, then a shower in the beach hut.'], ['Sunset', 'Cocktail and fried bites on the sand, from 6pm.'], ['Night', 'After dinner on the sand, with the music low.']],
         c: ['Book an aperitivo', WA + 'Hello%2C%20I%27m%20contacting%20you%20from%20your%20website%20and%20I%27d%20like%20to%20book%20a%20table%20for%20aperitivo.'] },
    P: { t: 'A taste for the sea', d: 'You go to the beach for what’s on the plate, too.',
         g: [['Lunch', 'The seafood dishes of the day, depending on the catch.'], ['Aperitivo', 'A glass of Prosecco as the sun goes down.'], ['Dinner', 'Spaghetti with clams and tuna tartare, with the sea in front of you.']],
         c: ['Book a table', WA + 'Hello%2C%20I%27m%20contacting%20you%20from%20your%20website%20and%20I%27d%20like%20to%20book%20a%20table%20at%20the%20restaurant.'] },
    V: { t: 'One last swim before the flight', d: 'You’re passing through Rome, but you’re not going to miss the sea.',
         g: [['Arrival', 'You leave your luggage in our storage room.'], ['The day', 'Sunbed, swim and lunch with a sea view.'], ['Departure', 'A shower in the beach hut, and Fiumicino is 20 minutes away.']],
         c: ['Luggage storage', '/en/#luggage-storage'] },
    F: { t: 'Life of the party', d: 'For you, the sea is better with company.',
         g: [['Afternoon', 'Everyone together on the beach.'], ['Sunset', 'Platters and fried bites to share, and a toast.'], ['Evening', 'A private party by the sea, tailored to you.']],
         c: ['Parties and events', '/en/groups'] }
  } : {
    L: { t: 'Lettino e silenzio', d: 'Per te il mare è una pausa: il rumore delle onde, un buon libro, nessuna fretta.',
         g: [['Mattina', 'Un lettone sotto l’ombrellone, ben distanziato dai vicini.'], ['Pranzo', 'Qualcosa di fresco da asporto, da gustare all’ombra.'], ['Sera', 'Una doccia in cabina e un calice di Falanghina guardando il mare.']],
         c: ['Scrivici su WhatsApp', WA + 'Ciao%2C%20vi%20contatto%20dal%20sito%20web%20e%20vorrei%20avere%20informazioni%20sulla%20spiaggia.'] },
    T: { t: 'Spirito del tramonto', d: 'Il tuo momento è quando il sole scende e la luce diventa oro.',
         g: [['Pomeriggio', 'L’ultimo bagno, poi la doccia in cabina.'], ['Tramonto', 'Cocktail e fritti sulla sabbia, dalle 18.'], ['Notte', 'Il dopocena sulla sabbia, con la musica bassa.']],
         c: ['Prenota l’aperitivo', WA + 'Ciao%2C%20vi%20contatto%20dal%20sito%20web%20e%20vorrei%20prenotare%20un%20tavolo%20per%20l%27aperitivo.'] },
    P: { t: 'Palato di mare', d: 'Al mare ci vai anche per quello che c’è nel piatto.',
         g: [['Pranzo', 'I piatti di mare del giorno, secondo il pescato.'], ['Aperitivo', 'Un calice di Prosecco mentre il sole scende.'], ['Cena', 'Spaghetti alle vongole e tartare di tonno, con il mare davanti.']],
         c: ['Prenota un tavolo', WA + 'Ciao%2C%20vi%20contatto%20dal%20sito%20web%20e%20vorrei%20prenotare%20un%20tavolo%20al%20ristorante.'] },
    V: { t: 'Un tuffo prima del volo', d: 'Sei a Roma di passaggio, ma il mare non te lo vuoi perdere.',
         g: [['Arrivo', 'Lasci i bagagli nel nostro deposito.'], ['La giornata', 'Lettino, bagno e pranzo vista mare.'], ['Partenza', 'Una doccia in cabina, e Fiumicino è a 20 minuti.']],
         c: ['Il deposito bagagli', '/#deposito-bagagli'] },
    F: { t: 'Anima della festa', d: 'Per te il mare è più bello in compagnia.',
         g: [['Pomeriggio', 'Tutti insieme in spiaggia.'], ['Tramonto', 'Taglieri e fritti da condividere, e un brindisi.'], ['Sera', 'Una festa privata sul mare, su misura per voi.']],
         c: ['Feste ed eventi', '/feste-gruppi'] }
  };

  var T = en ? {
    domanda: function(i, n){ return 'Question ' + i + ' of ' + n; },
    sei: 'You are', giornata: 'Our tip for you', aspetta: 'We\u2019ll be waiting for you', aspetta_p: 'See you next summer at Lungomare Paolo Toscanelli 27, Lido di Ostia.', scrivi: 'Message us on WhatsApp', spiaggia: 'Discover the beach', rifai: 'Play again', condividi: 'Share', copiato: 'Link copied',
    ciao: 'Hi! I’m the little crab. Shall we find out what kind of beachgoer you are?',
    via: function(n){ return n ? 'Let’s go, ' + n + '!' : 'Let’s go!'; },
    commenti: ['Interesting…', 'I like it!', 'Noted.', 'Good choice.', 'I see, I see…', 'I would too!'],
    quasi: 'Last one!', fine: 'Here you are!',
    errEmail: 'Please enter a valid email.', errConsenso: 'Please tick the box to subscribe.',
    share: function(t){ return 'At Marechiaro I’m “' + t + '”. What kind of beachgoer are you?'; }
  } : {
    domanda: function(i, n){ return 'Domanda ' + i + ' di ' + n; },
    sei: 'Sei', giornata: 'Il nostro consiglio per te', aspetta: 'Ti aspettiamo al Marechiaro', aspetta_p: 'Ci vediamo la prossima estate al Lungomare Paolo Toscanelli 27, Lido di Ostia.', scrivi: 'Scrivici su WhatsApp', spiaggia: 'Scopri la spiaggia', rifai: 'Gioca di nuovo', condividi: 'Condividi', copiato: 'Link copiato',
    ciao: 'Ciao! Io sono il granchietto. Scopriamo che tipo da Marechiaro sei?',
    via: function(n){ return n ? 'Cominciamo, ' + n + '!' : 'Cominciamo!'; },
    commenti: ['Interessante…', 'Mi piace!', 'Segnato.', 'Ottima scelta.', 'Capisco, capisco…', 'Anche io!'],
    quasi: 'Ultima domanda!', fine: 'Eccoti qua!',
    errEmail: 'Scrivi un indirizzo email valido.', errConsenso: 'Spunta la casella per iscriverti.',
    share: function(t){ return 'Al Marechiaro io sono «' + t + '». Tu che tipo da Marechiaro sei?'; }
  };

  var palco = box.querySelector('.gq-palco');
  var cammina = box.querySelector('.gq-cammina');
  var granchio = box.querySelector('.gq-granchio');
  var fumetto = box.querySelector('.gq-fumetto');
  var schermo = box.querySelector('.gq-schermo');
  var nome = '', i, conti, bloccato;

  function a_caso(l){ return l[Math.floor(Math.random() * l.length)]; }
  function mescola(a){ a = a.slice(); for (var k = a.length - 1; k > 0; k--) { var j = Math.floor(Math.random() * (k + 1)); var t = a[k]; a[k] = a[j]; a[j] = t; } return a; }
  function esc(s){ return String(s).replace(/[&<>"]/g, function(c){ return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]; }); }

  function dice(testo){
    fumetto.textContent = testo;
    fumetto.classList.remove('su'); void fumetto.offsetWidth; fumetto.classList.add('su');
  }
  function umore(classe){
    granchio.classList.remove('festa','giu','pensa','guarda','gira');
    void granchio.getBoundingClientRect();
    if (classe) granchio.classList.add(classe);
    cammina.classList.toggle('va', classe === 'pensa');
  }
  function conchiglie(n){
    for (var k = 0; k < n; k++) {
      var s = document.createElement('i');
      s.className = 'gq-coccio';
      s.style.left = (40 + Math.random() * 20) + '%';
      s.style.setProperty('--dx', (Math.random() * 260 - 130) + 'px');
      s.style.setProperty('--dy', (-60 - Math.random() * 120) + 'px');
      s.style.setProperty('--r', (Math.random() * 540 - 270) + 'deg');
      s.style.animationDelay = (Math.random() * .12) + 's';
      palco.appendChild(s);
      setTimeout(function(el){ return function(){ el.remove(); }; }(s), 1400);
    }
  }

  /* ---------- iscrizione (Netlify Forms) ---------- */
  function iscrivi(dati){
    try {
      fetch('/', { method: 'POST', headers: { 'Content-Type': 'application/x-www-form-urlencoded' }, body: new URLSearchParams(dati).toString() }).catch(function(){});
    } catch (e) {}
  }
  var form = box.querySelector('.gq-form');
  if (form) {
    form.addEventListener('submit', function(e){
      e.preventDefault();
      var f = new FormData(form), err = form.querySelector('.gq-errore');
      nome = String(f.get('nome') || '').trim().split(' ')[0].slice(0, 20);
      var email = String(f.get('email') || '').trim();
      var salta = e.submitter && e.submitter.classList.contains('gq-salta');
      if (!salta) {
        if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email)) { err.textContent = T.errEmail; form.querySelector('[name=email]').focus(); return; }
        if (!f.get('consenso')) { err.textContent = T.errConsenso; return; }
        if (f.get('bot-field')) return;
        var dati = { nome: String(f.get('nome') || '').trim(), email: email, consenso: 'si', lingua: en ? 'en' : 'it' };
        iscrivi({ 'form-name': 'newsletter-gioco', nome: dati.nome, email: email, consenso: 'si', lingua: dati.lingua, data: new Date().toISOString() });
        try { fetch('/.netlify/functions/iscrizione', { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify(dati) }).catch(function(){}); } catch (x) {}
      }
      err.textContent = '';
      inizia();
    });
  }

  /* ---------- quiz ---------- */
  function inizia(){
    i = 0; conti = { L: 0, T: 0, P: 0, V: 0, F: 0 };
    box.classList.add('in-gioco');
    dice(T.via(nome));
    mostra();
  }

  function mostra(){
    bloccato = false;
    umore('pensa');
    var d = DOMANDE[i];
    schermo.innerHTML =
      '<div class="gq-testa"><span class="gq-num">' + T.domanda(i + 1, DOMANDE.length) + '</span></div>' +
      '<div class="gq-tempo gq-avanzamento" aria-hidden="true"><i style="transform:scaleX(' + (i / DOMANDE.length) + ')"></i></div>' +
      '<h2 class="gq-domanda entra" tabindex="-1">' + esc(d.q) + '</h2>' +
      '<div class="gq-risposte">' + mescola(d.a).map(function(r, k){
        return '<button type="button" class="gq-r entra" style="animation-delay:' + (.08 + k * .07) + 's" data-p="' + r[1] + '">' +
          '<span class="gq-lettera">' + 'ABCD'[k] + '</span>' + esc(r[0]) + '</button>';
      }).join('') + '</div>';
    schermo.querySelector('.gq-domanda').focus({ preventScroll: true });
    requestAnimationFrame(function(){ var b = schermo.querySelector('.gq-avanzamento i'); b.style.transform = 'scaleX(' + ((i + .35) / DOMANDE.length) + ')'; });
  }

  function scegli(btn){
    if (bloccato) return;
    bloccato = true;
    conti[btn.getAttribute('data-p')]++;
    btn.classList.add('scelta');
    var tutti = schermo.querySelectorAll('.gq-r');
    for (var k = 0; k < tutti.length; k++) { tutti[k].disabled = true; }
    schermo.querySelector('.gq-avanzamento i').style.transform = 'scaleX(' + ((i + 1) / DOMANDE.length) + ')';
    umore(Math.random() < .5 ? 'festa' : 'guarda'); conchiglie(5);
    dice(i === DOMANDE.length - 2 ? T.quasi : a_caso(T.commenti));
    setTimeout(function(){ i++; if (i < DOMANDE.length) mostra(); else fine(); }, 900);
  }

  function fine(){
    var max = -1, vincitore = 'L', ordine = mescola(['L', 'T', 'P', 'V', 'F']);
    for (var k = 0; k < ordine.length; k++) if (conti[ordine[k]] > max) { max = conti[ordine[k]]; vincitore = ordine[k]; }
    var p = PROFILI[vincitore];
    umore('gira'); conchiglie(22); dice(T.fine);
    schermo.innerHTML =
      '<p class="gq-num">' + (nome ? esc(nome) + ', ' + T.sei.toLowerCase() : T.sei) + '</p>' +
      '<h2 class="gq-titolo gq-profilo-t" tabindex="-1">' + esc(p.t) + '</h2>' +
      '<p class="gq-intro gq-profilo-d">' + esc(p.d) + '</p>' +
      '<div class="gq-giornata"><span class="eti">' + T.giornata + '</span><ol>' + p.g.map(function(r, k){
        return '<li class="entra" style="animation-delay:' + (.35 + k * .15) + 's"><b>' + esc(r[0]) + '</b><span>' + esc(r[1]) + '</span></li>';
      }).join('') + '</ol></div>' +
      '<div class="gq-cta entra" style="animation-delay:.9s"><p class="gq-cta__t">' + T.aspetta + '</p><p class="gq-cta__p">' + T.aspetta_p + '</p>' +
      '<div class="azioni gq-azioni"><a class="btn" href="' + p.c[1] + '"' + (p.c[1].indexOf('http') === 0 ? ' rel="noopener"' : '') + '>' + esc(p.c[0]) + '</a>' +
      (p.c[1].indexOf('wa.me') > -1
        ? '<a class="btn scuro" href="' + (en ? '/en/beach' : '/spiaggia') + '">' + T.spiaggia + '</a>'
        : '<a class="btn scuro" href="' + WA + (en ? 'Hello%2C%20I%27m%20contacting%20you%20from%20your%20website%20and%20I%27d%20like%20some%20information.' : 'Ciao%2C%20vi%20contatto%20dal%20sito%20web%20e%20vorrei%20avere%20informazioni.') + '" rel="noopener">' + T.scrivi + '</a>') +
      '</div></div>' +
      '<p class="gq-dopo"><button type="button" class="gq-salta gq-condividi">' + T.condividi + '</button><span aria-hidden="true">&middot;</span><button type="button" class="gq-salta gq-rifai">' + T.rifai + '</button></p>';
    schermo.querySelector('.gq-titolo').focus({ preventScroll: true });
    box.dataset.titolo = p.t;
  }

  function condividi(){
    var testo = T.share(box.dataset.titolo);
    var url = location.href.split('#')[0];
    if (navigator.share) { navigator.share({ title: document.title, text: testo, url: url }).catch(function(){}); return; }
    try {
      navigator.clipboard.writeText(testo + ' ' + url).then(function(){
        var b = schermo.querySelector('.gq-condividi'); if (b) b.textContent = T.copiato;
      });
    } catch (e) {}
  }

  box.addEventListener('click', function(e){
    var t = e.target.closest('button');
    if (!t || t.type === 'submit') return;
    if (t.classList.contains('gq-rifai')) inizia();
    else if (t.classList.contains('gq-r')) scegli(t);
    else if (t.classList.contains('gq-condividi')) condividi();
  });

  umore('pensa');
  setTimeout(function(){ dice(T.ciao); }, 600);
})();
