// shared site behaviour (kept small; page scripts live next to their page)

/* Work: a case card plays its recording while the pointer is on it */
(function(){if(!matchMedia('(hover:hover)').matches)return;[].forEach.call(document.querySelectorAll('.wk-c'),function(c){var v=c.querySelector('video');if(!v)return;
c.addEventListener('mouseenter',function(){if(!v.src)v.src=v.dataset.src;c.classList.add('play');var p=v.play();if(p&&p.catch)p.catch(function(){})});
c.addEventListener('mouseleave',function(){c.classList.remove('play');v.pause()})})})();

/* home: letters drift back into the sentence as it scrolls in */
(function(){var u=document.querySelector('[data-ut]');if(!u||matchMedia('(prefers-reduced-motion:reduce)').matches)return;var s=u.querySelector('.ut-s'),raf=0;
function up(){raf=0;var r=u.getBoundingClientRect(),h=innerHeight,p=(h*.9-r.top)/(r.height-h*.25);p=Math.max(0,Math.min(1,p));var t=1-p;t=t*t*(3-2*t);s.style.setProperty('--tt',t);[].forEach.call(s.querySelectorAll('i'),function(i){i.style.setProperty('--t',t)})}
addEventListener('scroll',function(){if(!raf)raf=requestAnimationFrame(up)},{passive:true});addEventListener('resize',up);up()})();

/* logo: a green spot follows the pointer over the wordmark */
(function(){var l=document.querySelector('.site-logo'),m=l&&l.querySelector('.site-lm');if(!m||!matchMedia('(hover:hover)').matches)return;
l.addEventListener('mousemove',function(e){var r=l.getBoundingClientRect();m.style.setProperty('--mx',(e.clientX-r.left)+'px');m.style.setProperty('--my',(e.clientY-r.top)+'px');m.style.setProperty('--rr','34px')});
l.addEventListener('mouseleave',function(){m.style.setProperty('--rr','0px')})})();
