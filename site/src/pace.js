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
