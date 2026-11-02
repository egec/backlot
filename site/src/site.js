// shared site behaviour (kept small; page scripts live next to their page)

/* Work: a case card plays its recording while the pointer is on it */
(function(){if(!matchMedia('(hover:hover)').matches)return;[].forEach.call(document.querySelectorAll('.wk-c'),function(c){var v=c.querySelector('video');if(!v)return;
c.addEventListener('mouseenter',function(){if(!v.src)v.src=v.dataset.src;c.classList.add('play');var p=v.play();if(p&&p.catch)p.catch(function(){})});
c.addEventListener('mouseleave',function(){c.classList.remove('play');v.pause()})})})();
