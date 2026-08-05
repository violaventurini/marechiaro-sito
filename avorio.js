(function(){
  var ridotto = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* Il titolo dell'hero e' testo vero nell'HTML: l'animazione e' solo CSS,
     cosi' Google lo legge anche senza eseguire JavaScript. */

  var nav   = document.querySelector('.nav');
  var hero  = document.querySelector('.hero');
  var rivela = [].slice.call(document.querySelectorAll('.riv'));

  /* ---- la giornata: quadrante guidato dallo scorrimento ---- */
  var giornata = document.querySelector('.giornata');
  var cielo    = document.querySelector('.cielo');
  var lancetta = document.querySelector('.quadrante .lancetta');
  var fasi     = [].slice.call(document.querySelectorAll('.fase'));
  var ore      = [].slice.call(document.querySelectorAll('.ora-eti'));

  /* cinque cieli: mattina, mezzogiorno, tramonto, sera, notte */
  var cieli = [
    [[0xDC,0xE9,0xF0],[0xF6,0xEE,0xDC],[0xEB,0xE0,0xCE]],
    [[0xCF,0xE5,0xEE],[0xF9,0xF3,0xE4],[0xEF,0xE6,0xD6]],
    [[0xF2,0xD3,0xAE],[0xF3,0xDD,0xC4],[0xE7,0xD2,0xB4]],
    [[0xE0,0xA8,0x84],[0xE6,0xC0,0x9E],[0xD6,0xB0,0x92]],
    [[0x8C,0x8D,0xA6],[0xB6,0xA9,0xA8],[0xC9,0xBB,0xAC]]
  ];
  function mescola(a,b,t){
    return 'rgb('+a.map(function(v,i){return Math.round(v+(b[i]-v)*t)}).join(',')+')';
  }
  function dipingi(p){
    var n = cieli.length - 1;
    var i = Math.min(n-1, Math.floor(p*n));
    var t = p*n - i;
    for (var k=0;k<3;k++) cielo.style.setProperty('--c'+(k+1), mescola(cieli[i][k], cieli[i+1][k], t));

    /* la lancetta copre 300 gradi, da -150 a +150 */
    if (lancetta) lancetta.style.transform = 'rotate(' + (-150 + p*300).toFixed(1) + 'deg)';

    var att = Math.min(fasi.length-1, Math.round(p*(fasi.length-1)));
    fasi.forEach(function(f,i){ f.classList.toggle('attiva', i===att); });
    ore.forEach(function(o,i){ o.classList.toggle('qui', i===att); });
  }

  /* le ore sono cliccabili: portano al punto giusto dello scorrimento */
  ore.forEach(function(o){
    o.addEventListener('click', function(){
      if (!giornata) return;
      var corsa = giornata.offsetHeight - window.innerHeight;
      var p = parseInt(o.dataset.va,10) / (ore.length - 1);
      window.scrollTo({ top: giornata.offsetTop + corsa*p, behavior: ridotto ? 'auto' : 'smooth' });
    });
  });

  /* ---- indice del menu che segue la sezione visibile ---- */
  var voci = [].slice.call(document.querySelectorAll('.menu-indice a'));
  var sezioni = voci.map(function(a){ return document.querySelector(a.getAttribute('href')); });

  var pendente = false;
  function passo(){
    pendente = false;
    var y = window.scrollY;
    nav.classList.toggle('posata', y > (hero ? hero.offsetHeight - 100 : 20));

    if (giornata && cielo && !ridotto){
      var r = giornata.getBoundingClientRect();
      var corsa = giornata.offsetHeight - window.innerHeight;
      var p = corsa > 0 ? Math.min(1, Math.max(0, -r.top / corsa)) : 0;
      dipingi(p);
    }

    if (voci.length){
      var qui = 0;
      sezioni.forEach(function(s,i){
        if (s && s.getBoundingClientRect().top < window.innerHeight * 0.34) qui = i;
      });
      voci.forEach(function(a,i){ a.classList.toggle('qui', i===qui); });
    }

    rivela.forEach(function(el){
      if (el.classList.contains('on')) return;
      if (el.getBoundingClientRect().top < window.innerHeight * 0.88) el.classList.add('on');
    });
  }
  function tick(){ if(!pendente){ pendente = true; requestAnimationFrame(passo); } }
  window.addEventListener('scroll', tick, {passive:true});
  window.addEventListener('resize', tick);
  passo();
})();
