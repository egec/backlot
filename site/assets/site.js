// shared site behaviour (kept small; page scripts live next to their page)

/* Work: a case card plays its recording while the pointer is on it */
/* touch screens have no hover: a card's preview plays while most of it is on screen */
(function(){if(matchMedia('(hover:hover)').matches||!('IntersectionObserver' in window))return;[].forEach.call(document.querySelectorAll('.wk-c'),function(c){var v=c.querySelector('video');if(!v)return;
new IntersectionObserver(function(x){var e=x[0];if(e.isIntersecting&&e.intersectionRatio>=.55){if(!v.src)v.src=v.dataset.src;c.classList.add('play');var p=v.play();if(p&&p.catch)p.catch(function(){})}else{c.classList.remove('play');v.pause()}},{threshold:[0,.55,1]}).observe(c.querySelector('.wk-m')||c)})})();
/* Ctrl Z keycaps: a tap presses and releases the key, nothing stays down or selected */
(function(){[].forEach.call(document.querySelectorAll('.wk-cz kbd'),function(k){var t=0;k.addEventListener('pointerdown',function(){clearTimeout(t);k.classList.add('pr')});['pointerup','pointercancel','pointerleave'].forEach(function(ev){k.addEventListener(ev,function(){clearTimeout(t);t=setTimeout(function(){k.classList.remove('pr')},120)})})})})();
/* About: the name tooltip closes when you tap anywhere else */
document.addEventListener('pointerdown',function(e){var a=document.activeElement;if(a&&a.classList&&a.classList.contains('ax-nm')&&!a.contains(e.target))a.blur()},true);
(function(){if(!matchMedia('(hover:hover)').matches)return;[].forEach.call(document.querySelectorAll('.wk-c'),function(c){var v=c.querySelector('video');if(!v)return;
/* fetch the preview while the card scrolls in, so the first hover plays at once */
if('IntersectionObserver' in window)new IntersectionObserver(function(x,o){if(x[0].isIntersecting){if(!v.src){v.preload='auto';v.src=v.dataset.src}o.disconnect()}},{rootMargin:'800px 0px'}).observe(c);
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

/* Contact opens a panel from the top of the page */
(function(){var a=document.querySelector('.site-n a[href="#contact"]');if(!a)return;
var p=document.createElement('div');p.className='ct';p.id='ct';p.setAttribute('role','dialog');p.setAttribute('aria-modal','true');p.setAttribute('aria-labelledby','ct-t');p.hidden=true;
p.innerHTML='<div class="ct-in"><div class="ct-a"><h2 id="ct-t">Bring me the messy brief.</h2><p>Based in Berlin, open to relocation, free to start within two weeks.</p></div>'
+'<ul class="ct-b"><li><a href="mailto:a.egecoskun@gmail.com">a.egecoskun@gmail.com</a><button type="button" class="ct-cp">Copy</button></li><li><a href="https://www.linkedin.com/in/ege-coskun/" target="_blank" rel="noopener">LinkedIn <span aria-hidden="true">↗</span></a></li></ul>'
+'</div><button type="button" class="ct-x" aria-label="Close"><svg width="14" height="14" viewBox="0 0 24 24" aria-hidden="true"><path d="M5 5l14 14M19 5L5 19" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"/></svg></button>';
var s=document.createElement('div');s.className='ct-s';s.hidden=true;document.body.appendChild(s);document.body.appendChild(p);
var last=null;function open(e){if(e)e.preventDefault();last=document.activeElement;p.hidden=false;s.hidden=false;requestAnimationFrame(function(){document.documentElement.classList.add('ct-on')});setTimeout(function(){p.setAttribute('tabindex','-1');p.focus({preventScroll:true})},50)}
function close(){document.documentElement.classList.remove('ct-on');setTimeout(function(){if(!document.documentElement.classList.contains('ct-on')){p.hidden=true;s.hidden=true}},420);if(last&&last.focus)last.focus({preventScroll:true})}
a.addEventListener('click',open);s.addEventListener('click',close);p.querySelector('.ct-x').addEventListener('click',close);
document.addEventListener('keydown',function(e){if(e.key==='Escape'&&document.documentElement.classList.contains('ct-on'))close()});
p.querySelector('.ct-cp').addEventListener('click',function(){var b=this;try{navigator.clipboard.writeText('a.egecoskun@gmail.com').then(function(){b.textContent='Copied';setTimeout(function(){b.textContent='Copy'},1600)})}catch(x){}})})();

/* cursor: a soft trail that swaps the site's own colours under it (bone and black, orchid and plum), so text stays readable inside it */
(function(){if(!matchMedia('(hover:hover) and (pointer:fine)').matches||matchMedia('(prefers-reduced-motion:reduce)').matches)return;var N=60,LAG=3.5,H=[],hx=-100,hy=-100,mx=-100,my=-100,on=false,R=document.documentElement;
/* the exact swap needs an SVG filter on the backdrop (Chromium); other browsers keep a plain trail that never inverts */
var LENS=/Chrome\//.test(navigator.userAgent)&&window.CSS&&CSS.supports&&CSS.supports('backdrop-filter','url(#ckA)'),w=document.createElement('div'),d=[];w.setAttribute('aria-hidden','true');
if(LENS){w.className='ckl'}else{w.className='ck';for(var i=0;i<N;i++){var e=document.createElement('i');e.style.transform='translate(-100px,-100px)';w.appendChild(e);d.push(e)}}document.body.appendChild(w);
var RAD=document.querySelector('nav.bl-nav')?7:13;
var dkT=0;function dk(x,y){var el=document.elementFromPoint(x,y),c,m='bone';while(el&&el!==R){c=getComputedStyle(el).backgroundColor.match(/[\d.]+/g);if(c&&(c.length<4||+c[3]>.5)){var r=+c[0],g=+c[1],b=+c[2];m=(r>180&&b>200&&g<170)?'orchid':((r*.299+g*.587+b*.114)<110?'dark':'bone');break}el=el.parentElement}if(R.dataset.ck!==m)R.dataset.ck=m}
function mv(x,y){mx=x;my=y;if(!dkT){dkT=setTimeout(function(){dkT=0;dk(mx,my)},90)}if(!on){on=true;hx=x;hy=y;H.length=0}}
addEventListener('mousemove',function(e){var c=e.getCoalescedEvents?e.getCoalescedEvents():null;if(c&&c.length)for(var i=0;i<c.length;i++)mv(c[i].clientX,c[i].clientY);else mv(e.clientX,e.clientY)},{passive:true});
R.addEventListener('mouseleave',function(){on=false;mx=my=hx=hy=-100;H.length=0});
function at(t){var n=H.length;if(!n)return[hx,hy];if(t>=H[n-1][0])return[H[n-1][1],H[n-1][2]];if(t<=H[0][0])return[H[0][1],H[0][2]];var lo=0,hi=n-1;while(hi-lo>1){var m=(lo+hi)>>1;if(H[m][0]<=t)lo=m;else hi=m}var a=H[lo],b=H[hi],k=(t-a[0])/(b[0]-a[0]||1);return[a[1]+(b[1]-a[1])*k,a[2]+(b[2]-a[2])*k]}
function cir(x,y,r){return'M'+(x-r).toFixed(1)+' '+y.toFixed(1)+'a'+r.toFixed(1)+' '+r.toFixed(1)+' 0 1 0 '+(2*r).toFixed(1)+' 0a'+r.toFixed(1)+' '+r.toFixed(1)+' 0 1 0 '+(-2*r).toFixed(1)+' 0z'}
var last=performance.now(),Q=window.__ckp=[],shown=1;
(function t(now){var dt=Math.min(40,now-last);last=now;hx+=(mx-hx)*(1-Math.exp(-dt/22));hy+=(my-hy)*(1-Math.exp(-dt/22));H.push([now,hx,hy]);while(H.length>2&&H[1][0]<now-N*LAG-60)H.shift();
var i,p;for(i=0;i<N;i++){p=at(now-i*LAG);Q[i]=[p[0],p[1],1-i*.0125]}
if(!LENS){for(i=0;i<N;i++)d[i].style.transform='translate('+Q[i][0].toFixed(1)+'px,'+Q[i][1].toFixed(1)+'px) scale('+Q[i][2].toFixed(3)+')'}
else if(!on){if(shown){w.style.display='none';shown=0}}
else{var x0=1e9,y0=1e9,x1=-1e9,y1=-1e9,r;for(i=0;i<N;i++){r=RAD*Q[i][2];x0=Math.min(x0,Q[i][0]-r);y0=Math.min(y0,Q[i][1]-r);x1=Math.max(x1,Q[i][0]+r);y1=Math.max(y1,Q[i][1]+r)}x0=Math.floor(x0)-1;y0=Math.floor(y0)-1;
/* the outline: one circle per sample, joined by a band, all wound the same way so they add up */
var u=cir(Q[0][0]-x0,Q[0][1]-y0,RAD),px=Q[0][0],py=Q[0][1],pr=RAD,ax,ay,l,nx,ny;
for(i=1;i<N;i++){ax=Q[i][0]-px;ay=Q[i][1]-py;l=Math.sqrt(ax*ax+ay*ay);if(l<.6&&i<N-1)continue;r=RAD*Q[i][2];u+=cir(Q[i][0]-x0,Q[i][1]-y0,r);
if(l>.01){nx=-ay/l;ny=ax/l;u+='M'+(px+nx*pr-x0).toFixed(1)+' '+(py+ny*pr-y0).toFixed(1)+'L'+(Q[i][0]+nx*r-x0).toFixed(1)+' '+(Q[i][1]+ny*r-y0).toFixed(1)+'L'+(Q[i][0]-nx*r-x0).toFixed(1)+' '+(Q[i][1]-ny*r-y0).toFixed(1)+'L'+(px-nx*pr-x0).toFixed(1)+' '+(py-ny*pr-y0).toFixed(1)+'z'}px=Q[i][0];py=Q[i][1];pr=r}
if(!shown){w.style.display='';shown=1}w.style.transform='translate('+x0+'px,'+y0+'px)';w.style.width=Math.ceil(x1-x0+2)+'px';w.style.height=Math.ceil(y1-y0+2)+'px';w.style.clipPath='path("'+u+'")'}
requestAnimationFrame(t)})(performance.now())})();

/* overscroll at the very bottom: the page canvas takes the footer colour, so no bone strip shows under the orchid footer on phones */
(function(){var f=document.querySelector('.ec-foot');if(!f)return;var d=document.documentElement,on=false;function bg(){var c=getComputedStyle(f).backgroundColor;return c&&c!=='rgba(0, 0, 0, 0)'&&c!=='transparent'?c:'#D492EC'}function u(){var h=Math.max(d.scrollHeight,document.body.scrollHeight),y=window.pageYOffset||d.scrollTop,e=y>0&&y+window.innerHeight>=h-2;if(e!==on){on=e;d.style.backgroundColor=e?bg():''}}addEventListener('scroll',u,{passive:true});addEventListener('resize',u);u()})();
