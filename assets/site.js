(function(){
  var mb=document.getElementById('mb'),nl=document.getElementById('nl');
  if(mb&&nl){mb.addEventListener('click',function(){var o=nl.classList.toggle('o');mb.setAttribute('aria-expanded',o);document.body.style.overflow=o?'hidden':''});}
  document.querySelectorAll('.dd>button').forEach(function(b){
    b.addEventListener('click',function(){var o=b.parentNode.classList.toggle('o');b.setAttribute('aria-expanded',o)});
  });
  document.addEventListener('keydown',function(e){if(e.key==='Escape'){document.querySelectorAll('.dd.o').forEach(function(d){d.classList.remove('o')})}});

  // reveal on scroll
  if('IntersectionObserver' in window){
    var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}})},{threshold:.1});
    document.querySelectorAll('.rv').forEach(function(el,i){el.style.transitionDelay=(i%4)*60+'ms';io.observe(el)});
  }else{document.querySelectorAll('.rv').forEach(function(el){el.classList.add('in')})}

  // goal filter on drip cards
  var goals=document.querySelectorAll('.goal'),cards=document.querySelectorAll('.cards .card');
  goals.forEach(function(g){g.addEventListener('click',function(){
    goals.forEach(function(x){x.setAttribute('aria-pressed','false')});g.setAttribute('aria-pressed','true');
    var f=g.dataset.f;cards.forEach(function(c){c.classList.toggle('hide',f!=='all'&&(' '+c.dataset.c+' ').indexOf(' '+f+' ')<0)});
  })});

  // symptom finder
  var syms=document.querySelectorAll('.sym');
  if(syms.length){
    var fK=document.getElementById('fK'),fN=document.getElementById('fN'),fP=document.getElementById('fP'),fD=document.getElementById('fD'),fB=document.getElementById('fB'),fL=document.getElementById('fL');
    syms.forEach(function(s){s.addEventListener('click',function(){
      syms.forEach(function(x){x.setAttribute('aria-pressed','false')});s.setAttribute('aria-pressed','true');
      var d=s.dataset;
      fK.textContent=d.price?'Suggested drip':"We'll individualize it";
      fN.textContent=d.name;fP.textContent=d.price||'';fP.hidden=!d.price;fD.textContent=d.desc;
      fB.href=d.sms;fB.querySelector('span').textContent=d.price?('Book '+d.name):'Text us your symptoms';
      if(d.url){fL.hidden=false;fL.href=d.url}else{fL.hidden=true}
    })});
  }
})();
