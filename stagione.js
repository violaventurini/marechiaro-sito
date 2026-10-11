/* ============================================================
   MARECHIARO — avviso di stagione + richieste feste ed eventi
   Tutto si regola da qui, senza toccare le pagine.

   STAGIONE_CHIUSA: true d'inverno, false quando si riapre.
   EVENTI: le date da annunciare. Ogni voce:
     { data: "2027-06-21", it: "Festa d'inizio estate", en: "Summer opening party", nota_it: "Dalle 19, musica dal vivo", nota_en: "From 7pm, live music" }
   Se la lista è vuota, la sezione delle date non compare.
   ============================================================ */
var STAGIONE_CHIUSA = true;
var EVENTI = [];

(function(){
  var WA = 'https://wa.me/393484059720?text=';
  var en = (document.documentElement.lang || 'it').indexOf('en') === 0;
  var T = en ? {
    eti: STAGIONE_CHIUSA ? 'Season closed · see you in 2027' : 'Summer 2027',
    titolo: 'Plan your party',
    pTitolo: 'Parties <em>&amp;</em> events',
    pIntro: STAGIONE_CHIUSA
      ? 'The 2026 season is over and we reopen in spring 2027. Summer dates are being booked now: tell us what you have in mind.'
      : 'Birthdays, group aperitivo, private dinners by the sea. Tell us what you have in mind.',
    date: 'Upcoming dates',
    tipo: 'Occasion', tipi: ['Birthday','Private party','Group aperitivo','Dinner','Company event','Other'],
    quando: 'Preferred date', persone: 'Guests', nome: 'Name',
    invia: 'Send on WhatsApp', chiudi: 'Close',
    msg: function(d){ return 'Hello, I\'d like to organise an event at Marechiaro.\n' +
      'Occasion: ' + d.tipo + '\nDate: ' + (d.data || 'to be decided') + '\nGuests: ' + (d.persone || '-') + (d.nome ? '\nName: ' + d.nome : ''); },
    fmt: 'en-GB'
  } : {
    eti: STAGIONE_CHIUSA ? 'Stagione chiusa · ci vediamo nel 2027' : 'Estate 2027',
    titolo: 'Organizza la tua festa',
    pTitolo: 'Feste <em>ed</em> eventi',
    pIntro: STAGIONE_CHIUSA
      ? 'La stagione 2026 è chiusa, riapriamo in primavera 2027. Le date dell’estate si prenotano adesso: raccontaci cosa hai in mente.'
      : 'Compleanni, aperitivi di gruppo, cene private sul mare. Raccontaci cosa hai in mente.',
    date: 'Prossime date',
    tipo: 'Occasione', tipi: ['Compleanno','Festa privata','Aperitivo di gruppo','Cena','Evento aziendale','Altro'],
    quando: 'Data che preferisci', persone: 'Persone', nome: 'Nome',
    invia: 'Invia su WhatsApp', chiudi: 'Chiudi',
    msg: function(d){ return 'Ciao, vorrei organizzare un evento al Marechiaro.\n' +
      'Occasione: ' + d.tipo + '\nData: ' + (d.data || 'da decidere') + '\nPersone: ' + (d.persone || '-') + (d.nome ? '\nNome: ' + d.nome : ''); },
    fmt: 'it-IT'
  };

  function esc(s){ return String(s).replace(/[&<>"]/g, function(c){ return {'&':'&amp;','<':'&lt;','>':'&gt;','"':'&quot;'}[c]; }); }

  var oggi = new Date().toISOString().slice(0,10);
  var prossimi = EVENTI.filter(function(e){ return e.data >= oggi; })
    .sort(function(a,b){ return a.data < b.data ? -1 : 1; });
  var lista = prossimi.length ? '<div class="stg__date"><span class="stg__eti">' + T.date + '</span><ul>' +
    prossimi.map(function(e){
      var d = new Date(e.data + 'T12:00:00');
      return '<li><b>' + d.getDate() + '</b><span>' + d.toLocaleDateString(T.fmt,{month:'short'}) + '</span>' +
        '<div><strong>' + esc(en ? (e.en || e.it) : e.it) + '</strong>' +
        ((en ? (e.nota_en || e.nota_it) : e.nota_it) ? '<small>' + esc(en ? (e.nota_en || e.nota_it) : e.nota_it) + '</small>' : '') + '</div></li>';
    }).join('') + '</ul></div>' : '';

  var btn = document.createElement('button');
  btn.type = 'button';
  btn.className = 'ctaev stg__apri';
  btn.setAttribute('aria-haspopup','dialog');
  btn.innerHTML = '<span class="ctaev__e">' + T.eti + '</span><span class="ctaev__t">' + T.titolo + ' <em>&rarr;</em></span>';

  var pan = document.createElement('div');
  pan.className = 'stg';
  pan.setAttribute('role','dialog');
  pan.setAttribute('aria-modal','true');
  pan.setAttribute('aria-labelledby','stg-titolo');
  pan.hidden = true;
  pan.innerHTML =
    '<div class="stg__velo" data-chiudi></div>' +
    '<form class="stg__box">' +
      '<button type="button" class="stg__x" data-chiudi aria-label="' + T.chiudi + '">&times;</button>' +
      '<span class="stg__eti">' + T.eti + '</span>' +
      '<h2 id="stg-titolo">' + T.pTitolo + '</h2>' +
      '<p class="stg__intro">' + T.pIntro + '</p>' + lista +
      '<fieldset class="stg__tipi"><legend>' + T.tipo + '</legend>' +
        T.tipi.map(function(t,i){ return '<label><input type="radio" name="tipo" value="' + t + '"' + (i===0?' checked':'') + '><span>' + t + '</span></label>'; }).join('') +
      '</fieldset>' +
      '<div class="stg__riga">' +
        '<label class="stg__campo"><span>' + T.quando + '</span><input type="date" name="data" min="' + oggi + '"></label>' +
        '<label class="stg__campo stg__campo--n"><span>' + T.persone + '</span><input type="number" name="persone" min="1" max="300" inputmode="numeric" placeholder="20"></label>' +
      '</div>' +
      '<label class="stg__campo"><span>' + T.nome + '</span><input type="text" name="nome" autocomplete="name"></label>' +
      '<button type="submit" class="btn stg__invia"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 2a10 10 0 0 0-8.6 15.1L2 22l5-1.3A10 10 0 1 0 12 2zm0 18.2c-1.5 0-3-.4-4.3-1.2l-.3-.2-3 .8.8-2.9-.2-.3A8.2 8.2 0 1 1 12 20.2zm4.5-6.1c-.2-.1-1.5-.7-1.7-.8s-.4-.1-.6.1-.7.8-.8 1-.3.2-.5.1a6.7 6.7 0 0 1-3.3-2.9c-.3-.4.3-.4.7-1.4.1-.2 0-.3 0-.4l-.8-1.8c-.2-.5-.4-.4-.6-.4h-.5a1 1 0 0 0-.7.3 3 3 0 0 0-.9 2.2 5.2 5.2 0 0 0 1.1 2.7 11.8 11.8 0 0 0 4.5 4c1.7.7 2.4.8 3.2.6.5-.1 1.5-.6 1.7-1.2s.2-1.1.2-1.2-.2-.1-.4-.2z"/></svg>' + T.invia + '</button>' +
    '</form>';

  document.body.appendChild(btn);
  document.body.appendChild(pan);

  var form = pan.querySelector('form');
  function apri(){ pan.hidden = false; requestAnimationFrame(function(){ pan.classList.add('su'); }); document.body.style.overflow = 'hidden'; }
  function chiudi(){ pan.classList.remove('su'); document.body.style.overflow = ''; setTimeout(function(){ pan.hidden = true; }, 350); btn.focus(); }
  btn.addEventListener('click', apri);
  pan.addEventListener('click', function(e){ if (e.target.hasAttribute('data-chiudi')) chiudi(); });
  window.addEventListener('keydown', function(e){ if (e.key === 'Escape' && !pan.hidden) chiudi(); });

  form.addEventListener('submit', function(e){
    e.preventDefault();
    var f = new FormData(form);
    var d = f.get('data') ? new Date(f.get('data') + 'T12:00:00').toLocaleDateString(T.fmt,{day:'numeric',month:'long',year:'numeric'}) : '';
    var testo = T.msg({ tipo: f.get('tipo'), data: d, persone: f.get('persone'), nome: (f.get('nome') || '').trim() });
    window.open(WA + encodeURIComponent(testo), '_blank', 'noopener');
  });

  setTimeout(function(){ btn.classList.add('vedi'); }, 1400);
})();
