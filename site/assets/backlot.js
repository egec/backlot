
(function(){
  var nav=document.querySelector('.bl-nav');
  if(!nav)return;
  var list=nav.querySelector('ol'), OFFSET=96, items=[], last=-1, RM=matchMedia('(prefers-reduced-motion:reduce)').matches;
  function visible(el){return !!(el.offsetWidth||el.offsetHeight||el.getClientRects().length);}
  function flowTop(s){var p=s.style.position;s.style.position='relative';var y=s.getBoundingClientRect().top+window.pageYOffset;s.style.position=p;return y;}
  function add(s,label){
    if(!s.id)s.id='s-'+items.length;
    var a=document.createElement('a');
    a.href='#'+s.id;
    a.innerHTML='<span class="bl-bar"><span class="bl-fill"></span></span><span class="bl-label"></span>';
    a.querySelector('.bl-label').textContent=label;
    a.addEventListener('click',function(e){
      e.preventDefault();
      window.scrollTo({top:flowTop(s)-OFFSET,behavior:'smooth'});
      if(history.replaceState)history.replaceState(null,'','#'+s.id);
    });
    var li=document.createElement('li');li.appendChild(a);list.appendChild(li);
    items.push({sec:s,link:a,bar:a.querySelector('.bl-bar'),fill:a.querySelector('.bl-fill'),lab:a.querySelector('.bl-label')});
  }
  function build(){
    var hero=document.querySelector('.cs-hero');
    if(hero&&visible(hero))add(hero,'Overview');
    [].forEach.call(document.querySelectorAll('section'),function(s){
      var num=s.querySelector('.cs-num'), title=s.querySelector('.cs-title');
      if(!num||!title||!visible(s))return;
      add(s,s.getAttribute('data-nav-label')||title.textContent.trim());
    });
  }
  function sizes(){
    if(!items.length)return;
    var total=Math.min(window.innerHeight*0.6,520)-items.length*6, sum=0;
    items.forEach(function(it){it.h=it.sec.offsetHeight;sum+=it.h;});
    items.forEach(function(it){it.bar.style.height=Math.max(16,Math.round(total*it.h/sum))+'px';});
  }
  function gutter(){
    if(window.innerWidth<1200)return;
    var r=nav.getBoundingClientRect();
    document.documentElement.style.setProperty('--bl-gutter',Math.ceil(r.right+96)+'px');
  }
  function fly(it){
    if(RM||window.innerWidth<1200)return;
    var t=it.sec.querySelector('[data-bl2]>.w-embed>.bl2-t>.k,.bl2-t>.k,.bl2-t>.bl2-head .k,.cs-dsec-head .cs-title');
    if(!t)return;
    var f=it.lab.getBoundingClientRect(),to=t.getBoundingClientRect();
    if(to.top<0||to.top>window.innerHeight)return;
    var c=document.createElement('span');c.className='bl-fly';c.textContent=it.lab.textContent;document.body.appendChild(c);
    var sc=parseFloat(getComputedStyle(t).fontSize)/11;
    t.style.transition='opacity .25s';t.style.opacity='0';
    var an=c.animate([{transform:'translate('+f.left+'px,'+f.top+'px) scale(1)',opacity:1},{transform:'translate('+to.left+'px,'+to.top+'px) scale('+sc+')',opacity:1}],{duration:650,easing:'cubic-bezier(.23,1,.32,1)'});
    an.onfinish=function(){t.style.opacity='';c.remove();};
  }
  function update(){
    if(!items.length)return;
    var mark=window.innerHeight*0.35, active=-1, rs=items.map(function(it){return it.sec.getBoundingClientRect();});
    items.forEach(function(it,i){
      var r=rs[i];
      var p=Math.max(0,Math.min(1,(mark-r.top)/Math.max(1,r.height)));
      if(rs[i+1]&&rs[i+1].top<=mark)p=1;
      it.fill.style.transform='scaleY('+p+')';
      it.link.classList.toggle('is-read',p>=1);
      if(r.top<=mark)active=i;
    });
    if(active<0)active=0;
    items.forEach(function(it,i){it.link.classList.toggle('is-active',i===active);});
    last=active;
    var nr=nav.getBoundingClientRect(), off=false;
    var darks=[].map.call(document.querySelectorAll('.cs-quote,.cs-dsec'),function(q){return q.getBoundingClientRect();});
    items.forEach(function(it){
      var r=it.link.getBoundingClientRect(), cy=r.top+r.height/2, d=false;
      darks.forEach(function(q){if(cy>=q.top&&cy<=q.bottom)d=true;});
      it.link.classList.toggle('is-dark',d);
    });
    [].forEach.call(document.querySelectorAll('footer,.finalfooter'),function(f){
      if(!visible(f))return;
      if(f.getBoundingClientRect().top<nr.bottom+24)off=true;
    });
    nav.classList.toggle('is-off',off);
  }
  var raf=0;function q(){if(!raf)raf=requestAnimationFrame(function(){raf=0;update();});}
  function init(){
    build();sizes();gutter();update();
    window.addEventListener('scroll',q,{passive:true});
    window.addEventListener('resize',function(){sizes();gutter();update();});
    window.addEventListener('load',function(){sizes();update();});
    if(document.fonts&&document.fonts.ready)document.fonts.ready.then(function(){gutter();update();});
  }
  if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',init);else init();
})();

(function(){function go(){document.querySelectorAll('[data-big]').forEach(function(e){if(e.dataset.done)return;e.dataset.done=1;e.innerHTML=e.textContent.split(' ').map(function(w){return '<span>'+w+'</span>'}).join(' ');e.querySelectorAll('span').forEach(function(s,i){s.style.transitionDelay=(i*60)+'ms'});if(!('IntersectionObserver' in window)){e.classList.add('in');return}new IntersectionObserver(function(x,o){if(x[0].isIntersecting){e.classList.add('in');o.disconnect()}},{threshold:.4}).observe(e)});var cp=document.querySelector('[data-copy]');if(cp)cp.addEventListener('click',function(){if(navigator.clipboard)navigator.clipboard.writeText('a.egecoskun@gmail.com');cp.textContent='Copied'})}var q=location.search,h=document.documentElement;if(/font=archivo/.test(q)){var l=document.createElement('link');l.rel='stylesheet';l.href='https://fonts.googleapis.com/css2?family=Archivo:wght@400;500;600;700;800&display=swap';document.head.appendChild(l);h.classList.add('f-archivo')}function st(){var nb=document.querySelector('[data-nb]');if(nb){if('IntersectionObserver' in window)new IntersectionObserver(function(x,o){if(x[0].isIntersecting){nb.classList.add('in');o.disconnect()}},{threshold:.35}).observe(nb);else nb.classList.add('in')}
if(!matchMedia('(prefers-reduced-motion:reduce)').matches){var w=document.querySelector('[data-bl2root="1"]');if(w){var ss=[].filter.call(w.children,function(e){return e.matches('section[data-bl2]')}),rf=0;
for(var a=w.parentElement;a&&a!==document.documentElement;a=a.parentElement){var cs=getComputedStyle(a);if(/hidden|auto|scroll/.test(cs.overflowY+cs.overflowX))a.style.overflow='clip'}
function pd(){var c=getComputedStyle(w),vh=innerHeight;w.style.setProperty('--pl',c.paddingLeft);w.style.setProperty('--pr',c.paddingRight);ss.forEach(function(x){x.style.setProperty('--st',Math.min(0,vh-x.offsetHeight)+'px')})}
function up(){rf=0;var vh=innerHeight;ss.forEach(function(x,i){var n=ss[i+1],o=1;if(n){var t=n.getBoundingClientRect().top;if(t<vh&&t>0)o=1-.45*(vh-t)/vh;else if(t<=0)o=.55}var v=o.toFixed(3);if(x._o!==v){x._o=v;x.style.setProperty('--o',v)}})}
function q(){if(!rf)rf=requestAnimationFrame(up)}
pd();up();addEventListener('scroll',q,{passive:true});addEventListener('resize',function(){pd();q()});addEventListener('load',function(){pd();q()});if('ResizeObserver' in window){var ro=new ResizeObserver(function(){pd();q()});ss.forEach(function(x){ro.observe(x)})}}}
}function all(){go();st()}if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',all);else all()})();
(function(){if(window.blVid)return;window.blVid=1;var PAUSE='<svg width="14" height="14" viewBox="0 0 24 24" aria-hidden="true"><path d="M7 5h3v14H7zM14 5h3v14h-3z" fill="currentColor"/></svg>',PLAY='<svg width="14" height="14" viewBox="0 0 24 24" aria-hidden="true"><path d="M8 5v14l11-7z" fill="currentColor"/></svg>',FULL='<svg width="14" height="14" viewBox="0 0 24 24" aria-hidden="true"><path d="M4 9V4h5M20 9V4h-5M4 15v5h5M20 15v5h-5" fill="none" stroke="currentColor" stroke-width="2"/></svg>',REST='<svg width="14" height="14" viewBox="0 0 24 24" aria-hidden="true"><path d="M4 12a8 8 0 1 0 2.4-5.7M4 4v4h4" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/></svg>';function mk(l,h){var b=document.createElement('button');b.type='button';b.setAttribute('aria-label',l);b.title=l;b.innerHTML=h;return b}function sync(v){if(!v.blPP)return;var p=v.paused;v.blPP.innerHTML=p?PLAY:PAUSE;var l=p?'Play video':'Pause video';v.blPP.setAttribute('aria-label',l);v.blPP.title=l;}function controls(v){if(v.blCtl)return;var c=document.createElement('div');c.className='bl-vctl';var rs=mk('Restart video',REST),pp=mk('Pause video',PAUSE),fs=mk('Open video full screen',FULL);rs.onclick=function(){load(v);try{v.currentTime=0;}catch(e){}v.blUser=false;v.play();if(v.blBtn){v.blBtn.remove();v.blBtn=null;}};pp.onclick=function(){if(v.paused){v.blUser=false;load(v);v.play();if(v.blBtn){v.blBtn.remove();v.blBtn=null;}}else{v.blUser=true;v.pause();}};fs.onclick=function(){load(v);var f=v.requestFullscreen||v.webkitRequestFullscreen||v.webkitEnterFullscreen;if(f)f.call(v);};c.appendChild(rs);c.appendChild(pp);c.appendChild(fs);v.parentNode.insertBefore(c,v);v.parentNode.classList.add('bl-vwrap');v.blCtl=c;v.blPP=pp;v.addEventListener('play',function(){sync(v);});v.addEventListener('pause',function(){sync(v);});sync(v);}function btn(v){if(v.blBtn)return;var w=v.parentNode;var b=document.createElement('button');b.type='button';b.setAttribute('aria-label','Play video');b.style.cssText='position:absolute;left:50%;top:50%;transform:translate(-50%,-50%);width:64px;height:64px;border-radius:50%;border:0;background:rgba(18,18,18,.72);cursor:pointer;display:flex;align-items:center;justify-content:center';b.innerHTML='<svg width="22" height="22" viewBox="0 0 24 24"><path d="M8 5v14l11-7z" fill="#fff"/></svg>';b.onclick=function(){v.blUser=false;v.play();b.remove();v.blBtn=null};w.appendChild(b);v.blBtn=b;}function load(v){if(!v.getAttribute('src')){v.src=v.getAttribute('data-src');v.preload='auto';}}function start(v){if(v.blUser)return;load(v);if(v.blLeft){try{v.currentTime=0;}catch(e){}v.blLeft=false;}var p=v.play();if(p&&p.catch)p.catch(function(){btn(v);});}function init(){var vs=[].slice.call(document.querySelectorAll('video[data-src]'));vs.forEach(function(v){v.blLeft=true;controls(v);});if(!('IntersectionObserver' in window)){vs.forEach(start);return;}var pre=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting)load(e.target);});},{rootMargin:'600px 0px'});var vis=new IntersectionObserver(function(es){es.forEach(function(e){var v=e.target;if(!e.isIntersecting||e.intersectionRatio===0){if(!v.paused)v.pause();v.blLeft=true;}else if(e.intersectionRatio>=0.4&&v.paused){start(v);}});},{threshold:[0,0.4]});vs.forEach(function(v){pre.observe(v);vis.observe(v);});}if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',init);else init();})();
(function(){
var mq=matchMedia('(min-width:768px)');
var PLAY='<svg width="14" height="14" viewBox="0 0 24 24" aria-hidden="true"><path d="M8 5v14l11-7z" fill="currentColor"/></svg>',PAUSE='<svg width="14" height="14" viewBox="0 0 24 24" aria-hidden="true"><path d="M7 5h3v14H7zM14 5h3v14h-3z" fill="currentColor"/></svg>';
var all=[];
[].forEach.call(document.querySelectorAll('[data-zs]'),function(z){
var st=[].slice.call(z.querySelectorAll('.zs-steps li')),ws=[].slice.call(z.querySelectorAll('.zs-mw')),hl=[].slice.call(z.querySelectorAll('.zs-hl')),bars=[].slice.call(z.querySelectorAll('.zs-bar button')),pb=z.querySelector('[data-zplay]'),free=false,cur=-1,n=st.length;
function vid(w){var m=w&&w.querySelector('video');if(!m)return null;if(!m.getAttribute('src')){m.src=m.dataset.zsrc;m.preload='auto'}return m}
function setBtn(v){if(!pb)return;var on=v&&!v.paused&&free;pb.innerHTML=(on?PAUSE:PLAY)+'<span>'+(on?'Pause':'Play the whole video')+'</span>'}
function act(i,force){var l=st[i];if(!l||(i===cur&&!force))return;cur=i;free=false;z.classList.remove('is-free');var mi=+l.dataset.m||0;
st.forEach(function(s,j){s.classList.toggle('on',j===i);s.querySelector('button').setAttribute('aria-current',j===i?'step':'false')});
bars.forEach(function(b,j){b.classList.toggle('on',j<=i)});
hl.forEach(function(h){h.classList.toggle('on',+h.dataset.s===i)});
ws.forEach(function(w,j){w.classList.toggle('on',j===mi);if(j!==mi){w.style.transform='';var o=w.querySelector('video');if(o)o.pause()}});
var w=ws[mi];if(mq.matches){var s=+l.dataset.z,c=function(v){return Math.max(1-s,Math.min(0,.5-s*v/100))*100};w.style.transform='translate('+c(+l.dataset.x)+'%,'+c(+l.dataset.y)+'%) scale('+s+')'}else w.style.transform='';
var v=vid(w);if(v&&l.dataset.t!=null){v.pause();var t=+l.dataset.t,seek=function(){try{v.currentTime=t}catch(e){}};if(v.readyState>=1)seek();else v.addEventListener('loadedmetadata',seek,{once:true})}setBtn(v)}
/* the pinned area scrolls through the steps: one step per share of the extra height */
function range(){var r=z.getBoundingClientRect(),pin=z.querySelector('.zs-pin'),run=z.offsetHeight-pin.offsetHeight;return {top:r.top-parseFloat(getComputedStyle(pin).top||0),run:Math.max(1,run)}}
function onScroll(){if(!mq.matches||free)return;var g=range(),p=Math.min(.999,Math.max(0,-g.top/g.run));act(Math.floor(p*n))}
function go(i){if(!mq.matches){act(i);return}var g=range(),y=window.pageYOffset+g.top+(i+.5)/n*g.run;if(window.__pace)window.__pace(y);else window.scrollTo({top:Math.max(0,y),behavior:'smooth'})}
st.forEach(function(s,i){s.querySelector('button').addEventListener('click',function(){go(i)})});
bars.forEach(function(b,i){b.addEventListener('click',function(){go(i)})});
if(pb)pb.addEventListener('click',function(){var w=ws.filter(function(x){return x.classList.contains('on')})[0],v=vid(w);if(!v)return;if(free&&!v.paused){v.pause();setBtn(v);return}free=true;z.classList.add('is-free');w.style.transform='';v.loop=true;if(!z.dataset.played){try{v.currentTime=0}catch(e){}}z.dataset.played=1;var p=v.play();if(p&&p.then)p.then(function(){setBtn(v)});else setBtn(v)});
act(0,true);
all.push({sc:onScroll,rs:function(){act(cur,true);onScroll()}});
(window.__zs=window.__zs||[]).push({el:z,n:n,range:range,cur:function(){return cur},y:function(i){var g=range();return window.pageYOffset+g.top+(i+.5)/n*g.run}});
});
var raf=0;
window.addEventListener('scroll',function(){if(raf)return;raf=requestAnimationFrame(function(){raf=0;all.forEach(function(a){a.sc()})})},{passive:true});
window.addEventListener('resize',function(){all.forEach(function(a){a.rs()})});
all.forEach(function(a){a.sc()});
/* full screen for the role screens: tabs come along */
[].forEach.call(document.querySelectorAll('[data-fs]'),function(b){b.addEventListener('click',function(){var f=b.closest('.blr-fs');if(!f)return;if(document.fullscreenElement)document.exitFullscreen();else if(f.requestFullscreen)f.requestFullscreen()})});
})();

/* role screens: tabs on the left pick the screen; the text beside them and the screen below follow */
(function(){
[].forEach.call(document.querySelectorAll('[data-blr]'),function(w){
var T=JSON.parse(w.querySelector('.blr-data').textContent),k='ed-work',tabs=[].slice.call(w.querySelectorAll('.blr-t'));
function esc(s){return s.replace(/[&<>]/g,function(c){return {'&':'&amp;','<':'&lt;','>':'&gt;'}[c]})}
function draw(){tabs.forEach(function(b){var on=b.dataset.k===k;b.setAttribute('aria-selected',on);b.tabIndex=on?0:-1});
[].forEach.call(w.querySelectorAll('img[data-k]'),function(i){i.classList.toggle('on',i.dataset.k===k)});
w.querySelector('.blr-c').textContent=T[k][0];
w.querySelector('.blr-rs').innerHTML=T[k][1].map(function(t){return '<p>'+esc(t)+'</p>'}).join('')}
tabs.forEach(function(b,i){b.addEventListener('click',function(){k=b.dataset.k;draw()});
b.addEventListener('keydown',function(e){var d={ArrowDown:1,ArrowRight:1,ArrowUp:-1,ArrowLeft:-1}[e.key];if(!d)return;e.preventDefault();var n=tabs[(i+d+tabs.length)%tabs.length];n.click();n.focus()})});
draw()});
})();

/* One gesture, one move: a scroll gesture (wheel, trackpad or finger) moves one step in a pinned feature,
   or lands the next section with its top under the header. Inside long sections the page scrolls normally. */
(function(){
var RM=matchMedia('(prefers-reduced-motion:reduce)').matches,root=document.documentElement;
var secs=[].slice.call(document.querySelectorAll('[data-bl2root] > section[data-bl2]'));
var lastWheel=0,lockUntil=0,busy=0,bt=0,ft=[];
/* section tops in the page flow (sections are sticky, so their boxes can sit elsewhere on screen) */
function measure(){var Y=pageYOffset;ft=secs.map(function(s){var p=s.style.position;s.style.position='relative';var t=s.getBoundingClientRect().top+Y;s.style.position=p;return t})}
measure();addEventListener('load',measure);addEventListener('resize',measure);if('ResizeObserver' in window)new ResizeObserver(measure).observe(document.body);
function top(i){return ft[i]-pageYOffset}
function hh(){var h=document.querySelector('.site-h');return h?h.offsetHeight:0}
function zs(){return (window.__zs||[]).filter(function(z){var p=z.el.querySelector('.zs-pin');return p&&getComputedStyle(p).position==='sticky'})}
/* stop: on touch, also kill the momentum the finger left behind */
function to(y,smooth,stop){y=Math.max(0,Math.min(Math.round(y),root.scrollHeight-innerHeight));var sm=smooth&&!RM,t0=Date.now();busy=1;
  var go=function(){scrollTo({top:y,behavior:sm?'smooth':'auto'});
    (function wait(){if(Math.abs(pageYOffset-y)<2||Date.now()-t0>900){busy=0;lastY=pageYOffset;return}requestAnimationFrame(wait)})()};
  if(stop){root.style.overflow='hidden';requestAnimationFrame(function(){root.style.overflow='';go()})}else go()}
window.__pace=function(y){to(y,true,false)};
/* what a move of dy pixels should do; null lets the page scroll as usual */
function plan(dy){
  var d=dy>0?1:-1,vh=innerHeight,h=hh(),Y=pageYOffset,Z=zs();
  for(var k=0;k<Z.length;k++){var z=Z[k],g=z.range();
    if(g.top<=1&&-g.top<=g.run+1){var n=z.cur()+d;if(n>=0&&n<z.n)return {y:z.y(n)};continue}
    if(d>0&&g.top>1&&g.top-dy<=1)return {y:Y+g.top,snap:1};
    if(d<0&&-g.top>g.run+1&&-(g.top-dy)<=g.run+1)return {y:Y+g.top+g.run,snap:1}}
  for(var i=1;i<secs.length;i++){var t=top(i);
    if(d>0&&t>h+2&&t-dy<vh)return {y:Y+t-h};
    if(d<0&&t>=h-2&&t<vh-2)return {y:Y-(vh-t)};
    if(d<0&&t<h-2&&t-dy>h-2)return {y:Y+t-h,snap:1}}
  return null}
var absorb=0,moveT=0,lastAbs=0;
addEventListener('wheel',function(e){if(e.ctrlKey)return;var now=Date.now(),gap=now-lastWheel;lastWheel=now;
  var dy=e.deltaMode===1?e.deltaY*16:e.deltaMode===2?e.deltaY*innerHeight:e.deltaY,abs=Math.abs(dy);
  if(Math.abs(e.deltaX)>abs)return;  /* sideways: tables and carousels */
  var prev=lastAbs;lastAbs=abs;
  if(busy){e.preventDefault();return}
  /* after a move the page holds still until the gesture that caused it has ended: a pause starts the next move */
  if(absorb){if(gap>220||now-moveT>3000)absorb=0;else{e.preventDefault();return}}
  if(!dy)return;var p=plan(dy);if(!p)return;e.preventDefault();absorb=1;moveT=now;to(p.y,!p.snap,false)},{passive:false});
/* touch: one swipe, one move */
var y0=0,x0=0,ly=0,moved=0,side=0,finger=0,endT=0,lastY=pageYOffset;
addEventListener('touchstart',function(e){finger=1;moved=0;side=0;y0=ly=e.touches[0].clientY;x0=e.touches[0].clientX},{passive:true});
addEventListener('touchmove',function(e){var y=e.touches[0].clientY,inc=ly-y;ly=y;
  if(side)return;if(!moved&&Math.abs(e.touches[0].clientX-x0)>Math.abs(y-y0)&&Math.abs(e.touches[0].clientX-x0)>6){side=1;return}
  if(moved||busy){e.preventDefault();return}if(!inc)return;
  var p=plan(inc);if(!p)return;e.preventDefault();
  if(!p.snap&&Math.abs(y0-y)<12)return;moved=1;to(p.y,!p.snap,true)},{passive:false});
addEventListener('touchend',function(){finger=0;endT=Date.now()},{passive:true});
/* a flick keeps scrolling after the finger lifts: stop it at the next section top or feature */
addEventListener('scroll',function(){var Y=pageYOffset,dY=Y-lastY;lastY=Y;
  if(finger||busy||!dY||Date.now()-endT>2500)return;var h=hh(),Z=zs();
  for(var k=0;k<Z.length;k++){var g=Z[k].range(),gp=g.top+dY;
    if(gp>1&&g.top<=1){to(Y+g.top,false,true);return}
    if(-gp>g.run+1&&-g.top<=g.run+1){to(Y+g.top+g.run,false,true);return}}
  for(var i=1;i<secs.length;i++){var t=top(i),tp=t+dY;
    if((tp-h)*(t-h)<0){to(Y+t-h,false,true);return}}},{passive:true});
})();
