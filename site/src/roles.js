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

/* handwritten notes draw in once the title is a little way into view */
(function(){var ns=[].slice.call(document.querySelectorAll('[data-note]'));if(!ns.length)return;
if(!('IntersectionObserver' in window)){ns.forEach(function(n){n.classList.add('in')});return}
var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}})},{rootMargin:'0px 0px -30% 0px'});
ns.forEach(function(n){io.observe(n)})})();

/* interactive prototypes: when one first comes into view, ask it to show where to click first */
(function(){var fs=[].slice.call(document.querySelectorAll('.bl2-media.is-proto iframe'));if(!fs.length||!('IntersectionObserver' in window))return;
function ping(f){try{f.contentWindow.postMessage({blHint:1},'*')}catch(e){}}
var io=new IntersectionObserver(function(es){es.forEach(function(e){if(!e.isIntersecting)return;var f=e.target;io.unobserve(f);setTimeout(function(){ping(f)},700);setTimeout(function(){ping(f)},2400);f.addEventListener('load',function(){setTimeout(function(){ping(f)},900)},{once:true})})},{threshold:.4});
fs.forEach(function(f){io.observe(f)})})();

/* BİLGE: spec sheets land one by one as the section scrolls through the viewport */
(function(){var p=document.querySelector('[data-pile]');if(!p)return;var s=[].slice.call(p.querySelectorAll('.sp-s')),n=s.length;
if(matchMedia('(prefers-reduced-motion:reduce)').matches){s.forEach(function(x){x.classList.add('on')});return}
var raf=0;function up(){raf=0;var r=p.getBoundingClientRect(),h=innerHeight,t=(h*.95-r.top)/(h*.75);t=Math.max(0,Math.min(1,t));var k=Math.round(t*n);s.forEach(function(x,i){x.classList.toggle('on',i<k)})}
addEventListener('scroll',function(){if(!raf)raf=requestAnimationFrame(up)},{passive:true});addEventListener('resize',up);up()})();
