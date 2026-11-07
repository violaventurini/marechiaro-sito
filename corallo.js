/* MARECHIARO 2027 — apertura con il granchietto, menu a tutto schermo, comparsa dei blocchi.
   Tutti i testi stanno nell'HTML: lo script aggiunge solo il movimento. */
(function(){
  var html = document.documentElement;
  var nav = document.querySelector('.nav');
  var tog = document.querySelector('.nav__tog');
  var sipario = document.querySelector('.sipario');
  var hero = document.querySelector('.hero');
  var apertura = document.querySelector('.apertura');

  /* ---- apertura: il granchietto apre la home (una volta per visita, si salta con un tocco) ---- */
  function finisci(){
    if (!apertura || apertura.classList.contains('via')) { html.classList.add('pronto'); return; }
    apertura.classList.add('via');
    html.classList.add('pronto');
    setTimeout(function(){ apertura.classList.add('finita'); }, 1500);
  }
  if (apertura && !html.classList.contains('no-apertura')){
    var t = setTimeout(finisci, 2100);
    apertura.addEventListener('click', function(){ clearTimeout(t); finisci(); });
  } else {
    html.classList.add('pronto');
  }

  /* ---- menu a tutto schermo ---- */
  function apri(si){
    html.classList.toggle('aperto', si);
    tog.setAttribute('aria-expanded', si ? 'true' : 'false');
    tog.setAttribute('aria-label', si ? tog.dataset.chiudi : tog.dataset.apri);
    if (sipario) sipario.setAttribute('aria-hidden', si ? 'false' : 'true');
    document.body.style.overflow = si ? 'hidden' : '';
  }
  if (tog){
    tog.addEventListener('click', function(){ apri(!html.classList.contains('aperto')); });
    [].forEach.call(document.querySelectorAll('.sipario a'), function(a){
      a.addEventListener('click', function(){ apri(false); });
    });
    window.addEventListener('keydown', function(e){
      if (e.key === 'Escape' && html.classList.contains('aperto')) apri(false);
    });
  }

  /* ---- blocchi che compaiono scorrendo ---- */
  var riv = [].slice.call(document.querySelectorAll('.riv'));
  if ('IntersectionObserver' in window){
    var io = new IntersectionObserver(function(voci){
      voci.forEach(function(v){
        if (v.isIntersecting){ v.target.classList.add('on'); io.unobserve(v.target); }
      });
    }, { rootMargin: '0px 0px -8% 0px' });
    riv.forEach(function(el){ io.observe(el); });
  } else {
    riv.forEach(function(el){ el.classList.add('on'); });
  }

  /* ---- la barra diventa chiara dopo la prima schermata ---- */
  var pendente = false;
  function passo(){
    pendente = false;
    if (!nav) return;
    var soglia = hero ? hero.offsetHeight - 90 : 10;
    nav.classList.toggle('posata', window.scrollY > soglia);
    html.classList.toggle('oltre-hero', !hero || window.scrollY > hero.offsetHeight * 0.6);
  }
  window.addEventListener('scroll', function(){
    if (!pendente){ pendente = true; requestAnimationFrame(passo); }
  }, { passive: true });
  window.addEventListener('resize', passo);
  passo();
})();
