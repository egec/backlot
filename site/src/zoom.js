(function(){
var mq=matchMedia('(min-width:992px)');
var PLAY='<svg width="14" height="14" viewBox="0 0 24 24" aria-hidden="true"><path d="M8 5v14l11-7z" fill="currentColor"/></svg>',PAUSE='<svg width="14" height="14" viewBox="0 0 24 24" aria-hidden="true"><path d="M7 5h3v14H7zM14 5h3v14h-3z" fill="currentColor"/></svg>';
[].forEach.call(document.querySelectorAll('[data-zs]'),function(z){
var st=[].slice.call(z.querySelectorAll('.zs-steps li')),ws=[].slice.call(z.querySelectorAll('.zs-mw')),hl=[].slice.call(z.querySelectorAll('.zs-hl')),bars=[].slice.call(z.querySelectorAll('.zs-bar i')),pb=z.querySelector('[data-zplay]'),free=false;
function vid(w){var m=w&&w.querySelector('video');if(!m)return null;if(!m.getAttribute('src')){m.src=m.dataset.zsrc;m.preload='auto'}return m}
function setBtn(v){if(!pb)return;var on=v&&!v.paused&&free;pb.innerHTML=(on?PAUSE:PLAY)+'<span>'+(on?'Pause':'Play the whole video')+'</span>'}
function act(n){var l=st[n];if(!l)return;free=false;z.classList.remove('is-free');var mi=+l.dataset.m||0;
st.forEach(function(s,i){s.classList.toggle('on',i===n)});bars.forEach(function(b,i){b.classList.toggle('on',i<=n)});
hl.forEach(function(h){h.classList.toggle('on',+h.dataset.s===n)});
ws.forEach(function(w,i){w.classList.toggle('on',i===mi);if(i!==mi){w.style.transform='';var o=w.querySelector('video');if(o)o.pause()}});
var w=ws[mi];if(mq.matches){var s=+l.dataset.z,c=function(v){return Math.max(1-s,Math.min(0,.5-s*v/100))*100};w.style.transform='translate('+c(+l.dataset.x)+'%,'+c(+l.dataset.y)+'%) scale('+s+')'}else w.style.transform='';
var v=vid(w);if(v&&l.dataset.t!=null){v.pause();var t=+l.dataset.t,seek=function(){try{v.currentTime=t}catch(e){}};if(v.readyState>=1)seek();else v.addEventListener('loadedmetadata',seek,{once:true})}setBtn(v)}
st.forEach(function(s,i){s.addEventListener('click',function(){act(i)})});
if(pb)pb.addEventListener('click',function(){var w=ws.filter(function(x){return x.classList.contains('on')})[0],v=vid(w);if(!v)return;if(free&&!v.paused){v.pause();setBtn(v);return}free=true;z.classList.add('is-free');w.style.transform='';v.loop=true;if(!z.dataset.played){try{v.currentTime=0}catch(e){}}z.dataset.played=1;var p=v.play();if(p&&p.then)p.then(function(){setBtn(v)});else setBtn(v)});
if('IntersectionObserver' in window){new IntersectionObserver(function(es,o){if(es[0].isIntersecting){ws.forEach(vid);act(0);o.disconnect()}},{rootMargin:'400px 0px'}).observe(z);
var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting&&mq.matches)act(st.indexOf(e.target))})},{rootMargin:'-45% 0px -45% 0px'});st.forEach(function(s){io.observe(s)})}else{ws.forEach(vid);act(0)}
});
/* full screen for the role screens: tabs come along */
[].forEach.call(document.querySelectorAll('[data-fs]'),function(b){b.addEventListener('click',function(){var f=b.closest('.blr-fs');if(!f)return;if(document.fullscreenElement)document.exitFullscreen();else if(f.requestFullscreen)f.requestFullscreen()})});
})();
