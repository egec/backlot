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
