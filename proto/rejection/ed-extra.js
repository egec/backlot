/* editor side of the rejection prototype: arrival notification, resubmit confirmation, status after resubmit */
(function(){
if(window.BLX)return;
const d=document,emit=(e,x)=>{try{window.onEd&&window.onEd(e,x)}catch(_){}};
const css=d.createElement('style');
css.textContent=`
.blx-n{position:fixed;right:22px;top:68px;z-index:50;width:340px;display:flex;gap:10px;padding:12px 14px;border-radius:10px;background:#1F1E1D;box-shadow:0 0 0 1px #3a3937,0 16px 40px rgba(0,0,0,.5);font:400 12.5px/1.45 Manrope,system-ui,sans-serif;color:#edebe8;opacity:0;transform:translateY(-8px);transition:opacity .15s,transform .15s;pointer-events:none}
.blx-n.on{opacity:1;transform:none;pointer-events:auto;transition:opacity .2s cubic-bezier(.23,1,.32,1),transform .2s cubic-bezier(.23,1,.32,1)}
.blx-n img{width:28px;height:28px;border-radius:50%;flex:none}
.blx-n b{font-weight:500}.blx-n small{display:block;color:#96938d;font-size:11.5px;margin-top:2px}
.blx-n button{margin-left:auto;align-self:flex-start;width:24px;height:24px;border:0;border-radius:6px;background:transparent;color:#96938d;cursor:pointer;display:flex;align-items:center;justify-content:center}.blx-n button:hover{background:#2a2927;color:#edebe8}
.blx-dot{position:absolute;right:-1px;top:-1px;width:7px;height:7px;border-radius:50%;background:#F0A19A;box-shadow:0 0 0 2px #121212}
.blx-s{position:fixed;inset:0;z-index:60;background:rgba(9,9,9,.62);display:flex;align-items:center;justify-content:center;opacity:0;pointer-events:none;transition:opacity .15s}
.blx-s.on{opacity:1;pointer-events:auto;transition:opacity .2s cubic-bezier(.23,1,.32,1)}
.blx-m{width:460px;background:#1F1E1D;border-radius:14px;box-shadow:0 0 0 1px #3a3937,0 24px 64px rgba(0,0,0,.55);font:400 12.5px/1.45 Manrope,system-ui,sans-serif;color:#edebe8;transform:scale(.96);transition:transform .2s cubic-bezier(.23,1,.32,1)}
.blx-s.on .blx-m{transform:none}
.blx-m h3{margin:0;padding:18px 18px 0;font-size:15px;font-weight:500}
.blx-m p{margin:6px 18px 0;color:#b5b3ae}
.blx-m ul{list-style:none;margin:14px 18px 0;padding:0;display:flex;flex-direction:column;gap:8px}
.blx-m li{display:flex;align-items:center;gap:8px;border:1px solid #3a3937;border-radius:8px;padding:9px 12px}
.blx-m li span{display:inline-flex;align-items:center;height:24px;padding:0 8px;border-radius:6px;background:#2a2927;color:#d4d2cf;font-size:12px}
.blx-m li em{font-style:normal;color:#8FD4A6;font-size:12px;margin-left:auto}
.blx-f{display:flex;align-items:center;gap:8px;padding:16px 18px;margin-top:16px;border-top:1px solid color-mix(in srgb,#edebe8 10%,transparent)}
.blx-f .who{display:flex;align-items:center;gap:8px;color:#b5b3ae;margin-right:auto}.blx-f .who img{width:24px;height:24px;border-radius:50%}.blx-f .who b{color:#edebe8;font-weight:500}
.blx-b{height:32px;padding:0 14px;border-radius:8px;border:1px solid transparent;background:transparent;color:#d2cefd;font:500 12px/1 Manrope,sans-serif;cursor:pointer;display:inline-flex;align-items:center;gap:6px;transition:background .15s}
.blx-b:hover{background:color-mix(in srgb,#9184d9 12%,transparent)}
.blx-b.p{background:#9184d9;border-color:#9184d9;color:#121212}.blx-b.p:hover{background:#b5abfc;border-color:#b5abfc}
.blx-t{position:fixed;left:50%;bottom:28px;z-index:70;transform:translate(-50%,8px);display:flex;align-items:center;gap:8px;padding:10px 14px;border-radius:10px;background:#1F1E1D;box-shadow:0 0 0 1px #3a3937,0 16px 40px rgba(0,0,0,.5);font:400 12.5px/1.45 Manrope,system-ui,sans-serif;color:#edebe8;opacity:0;transition:opacity .15s,transform .15s;pointer-events:none}
.blx-t.on{opacity:1;transform:translate(-50%,0);transition:opacity .2s cubic-bezier(.23,1,.32,1),transform .2s cubic-bezier(.23,1,.32,1)}
.blx-t i{color:#8FD4A6}
@keyframes blxin{from{opacity:0;transform:translateY(-4px)}}
.blx-act{display:flex;gap:10px;padding:0 0 14px;font-size:12.5px;color:#edebe8}.blx-act img{width:24px;height:24px;border-radius:50%}.blx-act small{display:block;color:#78756f;font-size:11.5px}
`;
d.head.appendChild(css);
const el=(h)=>{const t=d.createElement('div');t.innerHTML=h.trim();return t.firstChild};
const n=el('<div class="blx-n" role="status"><img src="avatars/pub.png" alt=""><div><b>Maya Okafor</b> rejected Episode 2<small>2 reasons to fix, each on its field</small></div><button type="button" aria-label="Dismiss"><i class="ph ph-x"></i></button></div>');
const s=el('<div class="blx-s"><div class="blx-m" role="dialog" aria-modal="true"><h3>Submit Episode 2 for review?</h3><p>Maya Okafor will re-check the 2 fields you changed for Spain (ES). The rest of the episode stays approved.</p><ul><li><span>Age rating</span>Set to 16<em>Resolved</em></li><li><span>Synopsis (ES)</span>Written<em>Resolved</em></li></ul><div class="blx-f"><span class="who"><img src="avatars/pub.png" alt=""><span><b>Maya Okafor</b> will be notified</span></span><button class="blx-b" type="button" data-c>Cancel</button><button class="blx-b p" type="button" data-ok>Submit for review</button></div></div></div>');
const t=el('<div class="blx-t" role="status"><i class="ph ph-check-circle"></i><span>Submitted. Maya Okafor re-checks 2 fields.</span></div>');
[n,s,t].forEach(x=>d.body.appendChild(x));
let nt=0,done=false;
const sub=()=>[...d.querySelectorAll('[role=button]')].find(e=>e.textContent.trim()==='Submit for review'&&e.getAttribute('aria-disabled')!=='true'&&e.offsetParent);
function notify(){const b=d.querySelector('.ph-bell');if(b&&!b.querySelector('.blx-dot')){b.style.position='relative';b.appendChild(el('<span class="blx-dot"></span>'))}n.classList.add('on');clearTimeout(nt);nt=setTimeout(()=>n.classList.remove('on'),5000)}
n.querySelector('button').onclick=()=>n.classList.remove('on');
function openM(){s.classList.add('on');emit('modal')}
function closeM(){s.classList.remove('on');emit('modalclose')}
function submitted(){
 done=true;closeM();
 const chip=[...d.querySelectorAll('span')].find(e=>e.children.length===2&&e.lastElementChild.textContent==='Rejected');
 if(chip){chip.style.background='#2A1B23';chip.style.borderColor='#3D2A34';chip.style.color='#E8A6C4';chip.firstElementChild.outerHTML='<svg viewBox="0 0 16 16" aria-hidden="true" style="display:block;width:14px;height:14px;flex:none;color:#E8A6C4"><circle cx="8" cy="8" r="6" fill="none" stroke="currentColor" stroke-width="1.6"/><path d="M8 5v3.2l2 1.3" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/></svg>';chip.lastElementChild.textContent='Pending review'}
 const b=sub();if(b){const c=b.cloneNode(false);c.setAttribute('aria-disabled','true');c.removeAttribute('tabindex');c.style.opacity='.45';c.style.cursor='default';c.innerHTML='<i class="ph ph-check"></i>Submitted';b.style.display='none';b.parentNode.insertBefore(c,b)}
 const first=[...d.querySelectorAll('div')].find(e=>e.getAttribute('style')==='display:flex;gap:9px'&&/rejected/.test(e.textContent));
 if(first){const r=first.cloneNode(true);const av=r.firstElementChild;av.style.backgroundImage="url('avatars/rivard.png')";const tx=r.lastElementChild.firstElementChild;const sp=tx.querySelector('span');tx.textContent='You resubmitted ';if(sp)tx.appendChild(sp);const tm=r.lastElementChild.lastElementChild;if(tm)tm.textContent='Just now';r.style.animation='blxin .25s cubic-bezier(.23,1,.32,1)';first.parentNode.insertBefore(r,first)}
 t.classList.add('on');setTimeout(()=>t.classList.remove('on'),2600);
 emit('submitted');
}
d.addEventListener('click',e=>{
 if(s.contains(e.target)){if(e.target.closest('[data-ok]'))submitted();else if(e.target.closest('[data-c]')||e.target===s)closeM();return}
 const b=e.target.closest('[role=button]');
 if(b&&!done&&b.textContent.trim()==='Submit for review'&&b.getAttribute('aria-disabled')!=='true'){e.preventDefault();e.stopPropagation();openM();return}
 if(e.target.closest('button,[role=button],select,textarea,input,a,.blx-n'))return;
 emit('miss');
},true);
d.addEventListener('keydown',e=>{if(e.key==='Escape'&&s.classList.contains('on'))closeM()});
d.addEventListener('scroll',()=>emit('scroll'),true);
window.BLX={notify,sub,modalOk:()=>s.querySelector('[data-ok]'),done:()=>done};
})();
