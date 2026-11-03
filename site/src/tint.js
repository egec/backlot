/* big statement lines: letters take the project colour as the reader scrolls through, settle into ink, and lift a little as the colour passes */
(function(){var els=document.querySelectorAll('[data-tint]');if(!els.length)return;var RM=matchMedia('(prefers-reduced-motion:reduce)').matches;
function hex(h){h=h.replace('#','');return [parseInt(h.substr(0,2),16),parseInt(h.substr(2,2),16),parseInt(h.substr(4,2),16)]}
function mix(a,b,t){return [0,1,2].map(function(k){return Math.round(a[k]+(b[k]-a[k])*t)})}
var INK=hex('161616'),BG=hex('F7F7F5');
var items=[].map.call(els,function(el){var ac=hex(getComputedStyle(el).getPropertyValue('--ac').trim()||'#728437'),dark=mix(ac,INK,.55),pale=mix(ac,BG,.62);
  [].forEach.call(el.querySelectorAll('.bl2-line'),function(l){l.setAttribute('aria-hidden','true')});el.setAttribute('aria-label',el.textContent.replace(/\s+/g,' ').trim());
  var cs=[];[].forEach.call(el.querySelectorAll('.bl2-line'),function(l){var t=l.textContent;l.textContent='';t.split(' ').forEach(function(w,wi){if(wi)l.appendChild(document.createTextNode(' '));var ws=document.createElement('span');ws.className='tw';w.split('').forEach(function(c){var s=document.createElement('span');s.className='tc';s.textContent=c;ws.appendChild(s);cs.push(s)});l.appendChild(ws)})});
  return {el:el,cs:cs,ac:ac,dark:dark,pale:pale}});
function col(it,s){if(s<=0)return it.pale;if(s>=1)return INK;if(s<.35)return mix(it.pale,it.ac,s/.35);if(s<.7)return mix(it.ac,it.dark,(s-.35)/.35);return mix(it.dark,INK,(s-.7)/.3)}
var W=9;function draw(){raf=0;var vh=innerHeight;items.forEach(function(it){var r=it.el.getBoundingClientRect();if(r.bottom<-vh||r.top>vh*2)return;
  var p=RM?1:Math.max(0,Math.min(1,(vh*.88-r.top)/Math.max(1,vh*.55+r.height*.4))),n=it.cs.length,f=p*(n+W);
  it.cs.forEach(function(c,i){var s=Math.max(0,Math.min(1,(f-i)/W)),c3=col(it,s);c.style.color='rgb('+c3.join(',')+')';
    var b=RM?0:Math.sin(Math.PI*s);c.style.transform=b>.01?'translateY('+(-0.09*b).toFixed(3)+'em) rotate('+(((i%3)-1)*3*b).toFixed(2)+'deg)':''})})}
var raf=0;function q(){if(!raf)raf=requestAnimationFrame(draw)}addEventListener('scroll',q,{passive:true});addEventListener('resize',q);draw()})();
