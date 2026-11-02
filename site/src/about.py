"""About page drafts. Two ways to tell the same path: a dial that turns with the scroll, and a card drawer."""

PATH = [
    # (year label, kind, title, place, dates, lines)
    ('2016', 'edu', 'Industrial Design, B.Sc', 'Middle East Technical University, Ankara', 'Oct 2016 to Jul 2021',
     ['Five years of making things that have to be built: sketches, foam and clay models, prototypes.']),
    ('2021', 'work', 'Industrial Designer', 'MAN Truck & Bus, Ankara', 'Dec 2021 to Jun 2022',
     ['Bus interior parts, designed within tooling cost, lead time and the production schedule.',
      'Where I learned that a millimetre off is already paid for.']),
    ('2022', 'work', 'UX/UI Designer', 'MilSOFT Software Technologies, Ankara', 'Sep 2022 to Oct 2023',
     ['BİLGE, the customs platform of the Turkish Ministry of Trade, designed from backend rule documents.',
      'Radar screens for naval systems, signed off before build.']),
    ('2023', 'edu', 'Integrated Design, M.A.', 'Hochschule Anhalt, Dessau', 'Oct 2023 to Jul 2025',
     ['Ranked first in class.', 'Thesis: a wearable for continuous monitoring in high-risk pregnancies. Dessau Design Award.']),
    ('2024', 'work', 'Founding member, Product Designer', 'UwaVerde (NGO), remote', 'Jul 2024 to now',
     ['The organisation’s first design work, with no budget and nothing to inherit: the website and a member portal.']),
    ('2026', 'work', 'Product Designer', 'Insider One, remote', '2026',
     ['The customer data layer of a B2B platform used by more than 2,000 brands.']),
]
INTRO = ('I learned design where there’s no Ctrl+Z: a millimetre off in a bus interior part and the tooling is already paid for. '
         'I design B2B data products now, and the habit came with me.')
KIND = {'edu': 'Education', 'work': 'Experience'}


def dial():
    items = ''.join(
        f'<button class="dl-y" type="button" data-i="{i}" aria-label="{y}, {t}"><span>{y}</span></button>' for i, (y, k, t, p, d, ls) in enumerate(PATH))
    cards = ''.join(
        f'<article class="dl-c" data-i="{i}"><p class="dl-k"><i class="{k}"></i>{KIND[k]}</p><h2>{t}</h2><p class="dl-p">{p}</p>'
        f'<p class="dl-d">{d}</p>' + ''.join(f'<p class="dl-l">{x}</p>' for x in ls) + '</article>'
        for i, (y, k, t, p, d, ls) in enumerate(PATH))
    return f'''<main class="ab"><div class="cs-wrap ab-top"><p class="k">About</p><h1>Hi, I’m Ege.</h1><p class="ab-lead">{INTRO}</p></div>
<section class="dl" data-dial style="--n:{len(PATH)}" aria-label="My path, from 2016 to now">
<div class="dl-pin"><div class="dl-wheel" aria-hidden="true"><svg class="dl-arc" viewBox="0 0 1000 1000"><circle cx="500" cy="500" r="499" fill="none" stroke="currentColor" stroke-width="1.2" vector-effect="non-scaling-stroke"/></svg>
<i class="dl-dot"></i></div><div class="dl-ys">{items}</div><div class="dl-cs">{cards}</div>
<p class="dl-hint">Scroll to turn</p></div></section></main>
<style>
.ab .k{{font-size:13px;color:var(--mute);margin:0}}
.ab-top{{padding-top:clamp(40px,6vw,96px)}}
.ab h1{{margin:10px 0 0;font-size:clamp(34px,3.6vw,60px);line-height:1.04;letter-spacing:-.03em;font-weight:600}}
.ab-lead{{margin:18px 0 0;max-width:34em;font-size:clamp(16px,1.2vw,20px);line-height:1.45;color:#3a3936;text-wrap:pretty}}
.dl{{position:relative;height:calc(var(--n) * 70svh + 100svh);margin-top:clamp(24px,4vw,64px)}}
.dl-pin{{--R:min(44svh,28vw);--X:clamp(60px,10vw,180px);position:sticky;top:4.75rem;height:calc(100svh - 4.75rem);overflow:hidden}}
.dl-wheel{{position:absolute;left:calc(var(--R) * -1.12 + var(--X));top:50%;width:calc(var(--R) * 2);height:calc(var(--R) * 2);margin-top:calc(var(--R) * -1);color:#CFCCC5}}
.dl-arc{{width:100%;height:100%;display:block}}
.dl-dot{{position:absolute;right:-5px;top:50%;width:10px;height:10px;margin-top:-5px;border-radius:50%;background:var(--ink)}}
.dl-ys{{position:absolute;inset:0;pointer-events:none}}
.dl-y{{position:absolute;left:0;top:0;pointer-events:auto;border:0;background:none;padding:6px;cursor:pointer;font:600 clamp(28px,3vw,52px)/1 "Inter Tight",system-ui,sans-serif;letter-spacing:-.03em;color:#C9C6BF;font-variant-numeric:tabular-nums;transform-origin:0 50%;transition:color .3s}}
.dl-y span{{display:block;transition:transform .3s var(--ease)}}
.dl-y.on{{color:var(--ink)}}.dl-y.on span{{transform:scale(1.9)}}
.dl-y:hover:not(.on){{color:#8E8B84}}
.dl-y:focus-visible{{outline:2px solid var(--ink);outline-offset:4px;border-radius:6px}}
.dl-cs{{position:absolute;left:calc(var(--X) + var(--R) * .88 + clamp(190px,17vw,300px));right:var(--pad);top:50%;transform:translateY(-50%);max-width:30em}}
.dl-c{{position:absolute;left:0;top:50%;width:100%;opacity:0;transform:translateY(calc(-50% + 18px));transition:opacity .35s,transform .5s var(--ease);pointer-events:none}}
.dl-c.on{{opacity:1;transform:translateY(-50%);pointer-events:auto}}
.dl-k{{display:inline-flex;align-items:center;gap:8px;margin:0;font-size:13px;color:var(--mute)}}
.dl-k i{{width:8px;height:8px;border-radius:50%;background:#728437}}.dl-k i.edu{{background:transparent;box-shadow:inset 0 0 0 1.5px #728437}}
.dl-c h2{{margin:10px 0 0;font-size:clamp(24px,2.2vw,36px);line-height:1.1;letter-spacing:-.02em;font-weight:600;text-wrap:balance}}
.dl-p{{margin:6px 0 0;font-size:16px;color:#3a3936}}
.dl-d{{margin:4px 0 14px;font-size:13px;color:var(--mute);font-variant-numeric:tabular-nums}}
.dl-l{{margin:6px 0 0;font-size:15px;line-height:1.45;color:#3a3936;text-wrap:pretty}}
.dl-hint{{position:absolute;right:var(--pad);bottom:20px;margin:0;font-size:12px;color:var(--mute);transition:opacity .3s}}
.dl.moved .dl-hint{{opacity:0}}
@media(max-width:767px){{.dl-pin{{--R:46vw;--X:90px}}.dl-wheel{{left:calc(var(--R) * -1.35 + var(--X));top:34%}}.dl-y{{font-size:24px}}.dl-y.on span{{transform:scale(1.5)}}
.dl-cs{{left:var(--pad);top:auto;bottom:24px;transform:none;height:46%}}.dl-c{{top:0;transform:translateY(18px)}}.dl-c.on{{transform:none}}.dl-hint{{display:none}}}}
@media (prefers-reduced-motion:reduce){{.dl-c,.dl-y span{{transition:none}}}}
</style>
<script>
(function(){{var d=document.querySelector('[data-dial]');if(!d)return;var ys=[].slice.call(d.querySelectorAll('.dl-y')),cs=[].slice.call(d.querySelectorAll('.dl-c')),wh=d.querySelector('.dl-wheel'),n=ys.length,STEP=19,cur=-1,raf=0;
function prog(){{var r=d.getBoundingClientRect(),run=d.offsetHeight-d.querySelector('.dl-pin').offsetHeight;return Math.max(0,Math.min(1,-r.top/Math.max(1,run)))}}
function draw(){{raf=0;var f=prog()*(n-1),w=wh.getBoundingClientRect(),pin=d.querySelector('.dl-pin').getBoundingClientRect(),R=w.width/2,cx=w.left-pin.left+R,cy=w.top-pin.top+R;
d.classList.toggle('moved',f>.15);
ys.forEach(function(y,i){{var a=(i-f)*STEP*Math.PI/180,x=cx+(R+40)*Math.cos(a),yy=cy+(R+40)*Math.sin(a),vis=Math.abs(i-f)<4.2;
y.style.transform='translate('+x+'px,'+yy+'px) translateY(-50%) rotate('+(a*180/Math.PI)+'deg)';y.style.opacity=vis?Math.max(.15,1-Math.abs(i-f)*.22):0;y.tabIndex=vis?0:-1}});
var k=Math.round(f);if(k!==cur){{cur=k;ys.forEach(function(y,i){{y.classList.toggle('on',i===k)}});cs.forEach(function(c,i){{c.classList.toggle('on',i===k)}})}}}}
function go(i){{var run=d.offsetHeight-d.querySelector('.dl-pin').offsetHeight,top=d.getBoundingClientRect().top+pageYOffset;scrollTo({{top:top+run*i/(n-1)+2,behavior:matchMedia('(prefers-reduced-motion:reduce)').matches?'auto':'smooth'}})}}
ys.forEach(function(y,i){{y.addEventListener('click',function(){{go(i)}})}});
addEventListener('scroll',function(){{if(!raf)raf=requestAnimationFrame(draw)}},{{passive:true}});addEventListener('resize',draw);draw()}})();
</script>'''


def drawer():
    def card(i, y, k, t, p, d, ls):
        return (f'<article class="dw-c {k}" data-i="{i}" style="--i:{i}"><button class="dw-tab" type="button" aria-expanded="false"><span>{p.split(",")[0]}</span></button>'
                f'<div class="dw-in"><div class="dw-h"><p class="dw-k">{KIND[k]} / {y}</p><p class="dw-d">{d}</p></div><h2>{t}</h2><p class="dw-p">{p}</p>'
                + ''.join(f'<p class="dw-l">{x}</p>' for x in ls) + '<span class="dw-st" aria-hidden="true">' + ('STUDIED' if k == 'edu' else 'WORKED') + '</span></div></article>')
    cards = ''.join(card(i, *x) for i, x in enumerate(PATH))
    return f'''<main class="ab"><div class="cs-wrap ab-top"><p class="k">About</p><h1>Hi, I’m Ege.</h1><p class="ab-lead">{INTRO}</p></div>
<section class="cs-wrap dw-sec" aria-label="My path"><div class="dw-f" role="group" aria-label="Show">
<button type="button" class="on" data-f="all">Everything</button><button type="button" data-f="work">Experience</button><button type="button" data-f="edu">Education</button></div>
<div class="dw" data-drawer><div class="dw-cards">{cards}</div><div class="dw-front" aria-hidden="true"><span class="dw-lbl">EGE COSKUN / 2016 TO NOW</span><span class="dw-hd"><i></i><i></i></span></div></div>
<p class="dw-hint">Pick a card</p></section></main>
<style>
.ab .k{{font-size:13px;color:var(--mute);margin:0}}
.ab-top{{padding-top:clamp(40px,6vw,96px)}}
.ab h1{{margin:10px 0 0;font-size:clamp(34px,3.6vw,60px);line-height:1.04;letter-spacing:-.03em;font-weight:600}}
.ab-lead{{margin:18px 0 0;max-width:34em;font-size:clamp(16px,1.2vw,20px);line-height:1.45;color:#3a3936;text-wrap:pretty}}
.dw-sec{{padding-top:clamp(32px,4vw,64px);padding-bottom:clamp(72px,8vw,140px)}}
.dw-f{{display:flex;gap:6px;flex-wrap:wrap;justify-content:center;position:relative;z-index:40}}
.dw-f button{{height:36px;padding:0 16px;border-radius:99px;border:1px solid var(--ink);background:transparent;font:500 14px/1 "Inter Tight",system-ui,sans-serif;color:var(--ink);cursor:pointer;transition:background .2s,color .2s}}
.dw-f button.on,.dw-f button:hover{{background:var(--ink);color:#fff}}
.dw{{--L:#161616;--H:clamp(270px,24vw,330px);position:relative;max-width:880px;margin:calc(var(--H) + 150px) auto 0;height:calc(var(--H) + 40px)}}
.dw-cards{{position:absolute;left:4%;right:4%;bottom:0;height:100%}}
.dw-c{{position:absolute;left:calc(var(--i) * 1.2%);right:calc((5 - var(--i)) * 1.2%);bottom:calc(var(--i) * -18px + 110px);height:var(--H);background:#FBFAF6;border:1.5px solid var(--L);border-radius:10px 10px 0 0;
  transition:transform .6s var(--ease),opacity .35s,bottom .6s var(--ease);z-index:calc(var(--i) + 1)}}
.dw-tab{{position:absolute;top:-30px;left:calc(8% + var(--i) * 14%);height:31px;padding:0 18px;border:1.5px solid var(--L);border-bottom:0;border-radius:10px 10px 0 0;background:#FBFAF6;
  font:600 11px/1 "Inter Tight",system-ui,sans-serif;letter-spacing:.08em;text-transform:uppercase;color:var(--ink);cursor:pointer;white-space:nowrap}}
.dw-c.edu .dw-tab{{background:#E9EDDC}}
.dw-c:hover .dw-tab{{background:#56652A;color:#fff}}
.dw-tab:focus-visible{{outline:2px solid var(--ink);outline-offset:3px}}
.dw-in{{position:absolute;inset:0;padding:clamp(20px,2.6vw,36px);opacity:0;transition:opacity .3s}}
.dw-h{{display:flex;justify-content:space-between;gap:12px;padding-bottom:12px;border-bottom:1px dashed #B9B6AE;font-size:12px;letter-spacing:.06em;text-transform:uppercase;color:var(--mute)}}
.dw-h p{{margin:0}}
.dw-c h2{{margin:18px 0 0;font-size:clamp(22px,2.2vw,34px);line-height:1.1;letter-spacing:-.02em;font-weight:600}}
.dw-p{{margin:6px 0 10px;font-size:15px;color:#3a3936}}
.dw-l{{margin:6px 0 0;max-width:36em;font-size:15px;line-height:1.45;color:#3a3936}}
.dw-st{{position:absolute;right:clamp(18px,2.6vw,36px);bottom:clamp(18px,2.4vw,32px);padding:6px 10px;border:2px solid #56652A;border-radius:4px;color:#56652A;font:700 13px/1 "Inter Tight",sans-serif;letter-spacing:.14em;transform:rotate(-8deg) scale(1.4);opacity:0;transition:opacity .2s .35s,transform .35s .35s cubic-bezier(.3,1.6,.5,1)}}
.dw-c.open{{transform:translateY(calc(-1 * (var(--H) + 46px + var(--i) * 18px)));z-index:20}}
.dw-c.open .dw-in{{opacity:1;transition-delay:.15s}}
.dw-c.open .dw-st{{opacity:.9;transform:rotate(-8deg)}}
.dw-c.open .dw-tab{{background:var(--ink);color:#fff}}
.dw-c.dim{{opacity:.35}}.dw-c.dim .dw-tab{{pointer-events:none}}
.dw-front{{position:absolute;left:0;right:0;bottom:0;height:clamp(150px,16vw,200px);background:#F4F2EE;border:1.5px solid var(--L);border-radius:6px;z-index:30;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:16px}}
.dw-front:before{{content:"";position:absolute;inset:10px;border:1px solid #CFCCC5;border-radius:3px}}
.dw-lbl{{position:relative;padding:5px 10px;border:1px solid var(--L);font:600 11px/1 "Inter Tight",sans-serif;letter-spacing:.14em;background:#FBFAF6}}
.dw-hd{{position:relative;display:flex;flex-direction:column;gap:3px}}.dw-hd i{{display:block;width:120px;height:9px;border:1.5px solid var(--L);border-radius:0 0 12px 12px;background:#FBFAF6}}
.dw-hint{{text-align:center;margin:14px 0 0;font-size:12px;color:var(--mute)}}
@media(max-width:767px){{.dw{{--H:330px}}.dw-tab{{left:calc(4% + var(--i) * 13%);padding:0 9px;font-size:9px}}}}
@media (prefers-reduced-motion:reduce){{.dw-c,.dw-in,.dw-st{{transition:none}}}}
</style>
<script>
(function(){{var w=document.querySelector('[data-drawer]');if(!w)return;var cs=[].slice.call(w.querySelectorAll('.dw-c')),fb=[].slice.call(document.querySelectorAll('.dw-f button'));
function open(c){{cs.forEach(function(x){{var o=x===c&&!x.classList.contains('open');x.classList.toggle('open',o);x.querySelector('.dw-tab').setAttribute('aria-expanded',o)}})}}
cs.forEach(function(c){{c.querySelector('.dw-tab').addEventListener('click',function(){{open(c)}})}});
fb.forEach(function(b){{b.addEventListener('click',function(){{fb.forEach(function(x){{x.classList.toggle('on',x===b)}});var f=b.dataset.f,first=null;
cs.forEach(function(c){{var hit=f==='all'||c.classList.contains(f);c.classList.toggle('dim',!hit);if(hit)first=c}});open(null);if(f!=='all'&&first)open(first)}})}});
setTimeout(function(){{if(!w.querySelector('.open'))open(cs[cs.length-1])}},700)}})();
</script>'''
