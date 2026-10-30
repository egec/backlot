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
