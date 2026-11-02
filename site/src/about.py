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
function go(i){{var run=d.offsetHeight-d.querySelector('.dl-pin').offsetHeight,top=d.getBoundingClientRect().top+pageYOffset;scrollTo({{top:Math.round(top+run*i/(n-1))+(i===0?0:1),behavior:matchMedia('(prefers-reduced-motion:reduce)').matches?'auto':'smooth'}})}}
ys.forEach(function(y,i){{y.addEventListener('click',function(){{go(i)}})}});
/* inside the dial one wheel gesture or swipe moves exactly one year, then waits; at either end the page scrolls on as usual */
var lock=0;function step(dir){{var k=Math.round(prog()*(n-1)),t=k+dir;if(t<0||t>n-1)return false;if(Date.now()<lock)return true;lock=Date.now()+700;go(t);return true}}
function inside(){{var r=d.getBoundingClientRect(),pin=d.querySelector('.dl-pin').offsetHeight;return r.top<=2&&r.bottom>=pin+innerHeight*0-2}}
addEventListener('wheel',function(e){{if(!inside()||Math.abs(e.deltaY)<4)return;if(step(e.deltaY>0?1:-1))e.preventDefault()}},{{passive:false}});
var ty=null;addEventListener('touchstart',function(e){{ty=e.touches[0].clientY}},{{passive:true}});
addEventListener('touchmove',function(e){{if(ty==null||!inside())return;var dy=ty-e.touches[0].clientY;if(Math.abs(dy)<30){{if(Math.round(prog()*(n-1))>0&&Math.round(prog()*(n-1))<n-1)e.preventDefault();return}}if(step(dy>0?1:-1)){{e.preventDefault();ty=null}}}},{{passive:false}});
addEventListener('scroll',function(){{if(!raf)raf=requestAnimationFrame(draw)}},{{passive:true}});addEventListener('resize',draw);draw()}})();
</script>'''


def drawer():
    """the drawer poster: tabs stand behind and in front of one big page; picking a tab puts its card on that page"""
    work = [(i, x) for i, x in enumerate(PATH) if x[1] == 'work'][::-1]
    edu = [(i, x) for i, x in enumerate(PATH) if x[1] == 'edu'][::-1]
    def tab(i, x, side, row):
        y, k, t, p, d, ls = x
        short = {'Middle East Technical University': 'METU', 'MilSOFT Software Technologies': 'MilSOFT', 'Hochschule Anhalt': 'Hochschule Anhalt'}
        nm = p.split(",")[0].split(" (")[0]
        return f'<button class="dx-t {side}" type="button" data-i="{i}" style="--r:{row}"><span>{short.get(nm, nm)}</span></button>'
    back = ''.join(tab(i, x, 'l', r) for r, (i, x) in enumerate(work)) + ''.join(tab(i, x, 'r', r) for r, (i, x) in enumerate(edu))
    pages = ''.join(
        f'<article class="dx-p" data-i="{i}"><div class="dx-ph"><span class="dx-bk">{y}</span><span class="dx-kd">{KIND[k]}</span></div>'
        f'<h2>{t}</h2><p class="dx-pl">{p}</p><div class="dx-row"><span>Dates</span><b>{d}</b></div>'
        + ''.join(f'<p class="dx-l">{x}</p>' for x in ls) + '</article>'
        for i, (y, k, t, p, d, ls) in enumerate(PATH))
    return f'''<main class="ab"><div class="cs-wrap ab-top"><p class="k">About</p><h1>Hi, I’m Ege.</h1><p class="ab-lead">{INTRO}</p></div>
<section class="cs-wrap dx-sec" aria-label="My path"><div class="dx" data-dx>
<div class="dx-lab"><span>EXPERIENCE</span><span>EDUCATION</span></div>
<div class="dx-tabs">{back}</div>
<div class="dx-page">{pages}</div>
<div class="dx-front" aria-hidden="true"><i></i><i></i><i></i></div></div>
<p class="dx-hint">Pick a tab</p></section></main>
<style>
.ab .k{{font-size:13px;color:var(--mute);margin:0}}
.ab-top{{padding-top:clamp(40px,6vw,96px)}}
.ab h1{{margin:10px 0 0;font-size:clamp(34px,3.6vw,60px);line-height:1.04;letter-spacing:-.03em;font-weight:600}}
.ab-lead{{margin:18px 0 0;max-width:34em;font-size:clamp(16px,1.2vw,20px);line-height:1.45;color:#3a3936;text-wrap:pretty}}
.dx-sec{{padding-top:clamp(32px,4vw,64px);padding-bottom:clamp(64px,7vw,120px)}}
.dx{{--L:#161616;position:relative;max-width:860px;margin:0 auto}}
.dx-lab{{display:flex;justify-content:space-between;padding:0 6%;font:600 11px/1 "Inter Tight",sans-serif;letter-spacing:.16em;color:var(--mute)}}
.dx-tabs{{position:relative;height:calc(3 * 30px + 26px);margin:22px 4% 0}}
.dx-t{{position:absolute;bottom:calc(var(--r) * 30px);height:44px;width:46%;padding:0 22px;background:#FBFAF6;border:1.5px solid var(--L);border-bottom:0;border-radius:14px 14px 0 0;
  font:600 12px/1 "Inter Tight",sans-serif;letter-spacing:.1em;text-transform:uppercase;color:var(--ink);cursor:pointer;display:flex;align-items:flex-start;padding-top:12px;z-index:calc(10 - var(--r));transition:transform .3s var(--ease),background .2s,color .2s}}
.dx-t.l{{left:calc(var(--r) * 2%)}}.dx-t.r{{right:calc(var(--r) * 2%);justify-content:flex-end}}
.dx-t:hover{{transform:translateY(-6px)}}
.dx-t.on{{background:var(--ink);color:#fff;transform:translateY(-8px)}}
.dx-t:focus-visible{{outline:2px solid var(--ink);outline-offset:3px}}
.dx-page{{position:relative;margin:-2px 0 0;height:clamp(380px,40vw,460px);background:#FBFAF6;border:1.5px solid var(--L);border-radius:12px;overflow:hidden;z-index:12}}
.dx-page:before{{content:"";position:absolute;inset:14px;border:1px dashed #C9C6BF;border-radius:6px;pointer-events:none}}
.dx-p{{position:absolute;inset:0;padding:clamp(28px,4vw,52px);opacity:0;transform:translateY(24px);transition:opacity .3s,transform .45s var(--ease);pointer-events:none}}
.dx-p.on{{opacity:1;transform:none;pointer-events:auto}}
.dx-ph{{display:flex;align-items:center;gap:12px}}
.dx-bk{{padding:8px 14px;background:var(--ink);color:#fff;font:600 clamp(20px,2vw,28px)/1 "Inter Tight",sans-serif;letter-spacing:.04em}}
.dx-kd{{padding:7px 10px;border:1.5px solid var(--L);font:600 11px/1 "Inter Tight",sans-serif;letter-spacing:.14em;text-transform:uppercase}}
.dx-p h2{{margin:clamp(20px,2.4vw,32px) 0 0;font-size:clamp(28px,3vw,46px);line-height:1.04;letter-spacing:-.025em;font-weight:600;text-wrap:balance}}
.dx-pl{{margin:8px 0 0;font-size:16px;color:#3a3936}}
.dx-row{{display:flex;gap:16px;margin:18px 0 12px;padding:10px 0;border-top:1.5px solid var(--L);border-bottom:1.5px solid var(--L);font-size:13px}}
.dx-row span{{color:var(--mute);text-transform:uppercase;letter-spacing:.1em;font-size:11px;line-height:19px}}
.dx-l{{margin:8px 0 0;max-width:38em;font-size:15px;line-height:1.45;color:#3a3936}}
.dx-front{{position:relative;margin:-30px -3% 0;height:clamp(110px,12vw,150px);background:#F4F2EE;border:1.5px solid var(--L);border-radius:8px;z-index:13;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:3px}}
.dx-front i{{display:block;width:110px;height:10px;border:1.5px solid var(--L);border-radius:0 0 12px 12px;background:#FBFAF6}}
.dx-hint{{text-align:center;margin:14px 0 0;font-size:12px;color:var(--mute)}}
@media(max-width:767px){{.dx-t{{width:48%;padding:10px 10px 0;font-size:10px;letter-spacing:.06em}}.dx-page{{height:520px}}}}
@media (prefers-reduced-motion:reduce){{.dx-p,.dx-t{{transition:none}}}}
</style>
<script>
(function(){{var w=document.querySelector('[data-dx]');if(!w)return;var ts=[].slice.call(w.querySelectorAll('.dx-t')),ps=[].slice.call(w.querySelectorAll('.dx-p'));
function pick(i){{ts.forEach(function(t){{var on=t.dataset.i==i;t.classList.toggle('on',on);t.setAttribute('aria-pressed',on)}});ps.forEach(function(p){{p.classList.toggle('on',p.dataset.i==i)}})}}
ts.forEach(function(t){{t.addEventListener('click',function(){{pick(t.dataset.i)}})}});pick({len(PATH)-1})}})();
</script>'''


def tunnel():
    """time runs backwards: today's text first, then each scroll pulls the next older year out of a hand-drawn tunnel"""
    import random
    rnd = random.Random(3)
    def ring(k):
        # a wobbly rounded frame, drawn twice for a sketched line
        s = ''
        for pas in range(2):
            j = lambda v: round(v + rnd.uniform(-5, 5), 1)
            s += (f'<path d="M{j(80)} {j(40)} Q{j(500)} {j(10)} {j(920)} {j(40)} Q{j(990)} {j(300)} {j(920)} {j(560)} Q{j(500)} {j(590)} {j(80)} {j(560)} Q{j(10)} {j(300)} {j(80)} {j(40)}Z"'
                  f' class="{"a" if pas == 0 else "b"}"/>')
        return f'<g class="tn-r" data-k="{k}">{s}</g>'
    rings = ''.join(ring(k) for k in range(14))
    items = PATH[::-1]
    stops = ''.join(
        f'<article class="tn-s" data-i="{i}"><p class="tn-y">{y}</p><div class="tn-c"><p class="tn-k">{KIND[k]}</p><h2>{t}</h2><p class="tn-p">{p}, {d}</p>'
        + ''.join(f'<p class="tn-l">{x}</p>' for x in ls) + '</div></article>'
        for i, (y, k, t, p, d, ls) in enumerate(items))
    return f'''<main class="ab tn-main"><section class="tn" data-tunnel style="--n:{len(items)}" aria-label="My path, from now back to 2016">
<div class="tn-pin"><svg class="tn-svg" viewBox="0 0 1000 600" preserveAspectRatio="none" aria-hidden="true">{rings}</svg>
<div class="tn-now"><p class="k">About</p><h1>Hi, I’m Ege.</h1><p class="ab-lead">{INTRO}</p><p class="tn-go">Scroll to go back in time</p></div>
<div class="tn-ss">{stops}</div><p class="tn-clock" aria-hidden="true"><span>2026</span></p></div></section></main>
<style>
.tn-main .k{{font-size:13px;color:var(--mute);margin:0}}
.tn{{position:relative;height:calc((var(--n) + 1) * 90svh + 100svh)}}
.tn-pin{{position:sticky;top:4.75rem;height:calc(100svh - 4.75rem);overflow:hidden}}
.tn-svg{{position:absolute;inset:0;width:100%;height:100%;overflow:visible;-webkit-mask-image:radial-gradient(ellipse 46% 42% at 50% 50%,transparent 55%,#000 100%);mask-image:radial-gradient(ellipse 46% 42% at 50% 50%,transparent 55%,#000 100%)}}
.tn-r{{transform-origin:500px 300px;transform-box:view-box}}
.tn-r path{{fill:none;stroke:#2B2A28;vector-effect:non-scaling-stroke;stroke-linejoin:round}}
.tn-r path.a{{stroke-width:1.4}}.tn-r path.b{{stroke-width:.7;opacity:.55}}
.tn-now{{position:absolute;left:50%;top:50%;width:min(640px,86%);transform:translate(-50%,-50%);text-align:center;transition:opacity .3s,transform .5s var(--ease)}}
.tn-now h1{{margin:10px 0 0;font-size:clamp(34px,3.6vw,60px);line-height:1.04;letter-spacing:-.03em;font-weight:600}}
.tn-now .ab-lead{{margin:16px auto 0;max-width:30em;font-size:clamp(16px,1.2vw,20px);line-height:1.45;color:#3a3936}}
.tn-go{{margin:22px 0 0;font:400 30px/1 "Reenie Beanie",cursive;color:#56652A}}
.tn-ss{{position:absolute;inset:0;pointer-events:none}}
.tn-s{{position:absolute;left:50%;top:50%;width:min(620px,86%);transform:translate(-50%,-50%);text-align:center;opacity:0}}
.tn-y{{margin:0;font-size:clamp(64px,9vw,150px);line-height:.9;letter-spacing:-.05em;font-weight:700;color:var(--ink)}}
.tn-c{{margin-top:14px}}
.tn-k{{margin:0;font:400 26px/1 "Reenie Beanie",cursive;color:#56652A}}
.tn-s h2{{margin:6px 0 0;font-size:clamp(22px,2vw,32px);line-height:1.1;letter-spacing:-.02em;font-weight:600}}
.tn-p{{margin:6px 0 0;font-size:14px;color:var(--mute)}}
.tn-l{{margin:8px auto 0;max-width:30em;font-size:15px;line-height:1.45;color:#3a3936}}
.tn-clock{{position:absolute;right:var(--pad);bottom:20px;margin:0;font-size:12px;color:var(--mute);font-variant-numeric:tabular-nums}}
.tn-clock span:before{{content:"Year ";}}
@media (prefers-reduced-motion:reduce){{.tn{{height:auto}}.tn-pin{{position:static;height:auto;overflow:visible}}.tn-svg{{display:none}}.tn-now,.tn-s{{position:static;transform:none;opacity:1;margin:48px auto}}}}
</style>
<script>
(function(){{var d=document.querySelector('[data-tunnel]');if(!d||matchMedia('(prefers-reduced-motion:reduce)').matches)return;
var rs=[].slice.call(d.querySelectorAll('.tn-r')),ss=[].slice.call(d.querySelectorAll('.tn-s')),now=d.querySelector('.tn-now'),clk=d.querySelector('.tn-clock span'),n=ss.length,raf=0,R=rs.length;
var Y=ss.map(function(s){{return +s.querySelector('.tn-y').textContent}});
function prog(){{var r=d.getBoundingClientRect(),run=d.offsetHeight-d.querySelector('.tn-pin').offsetHeight;return Math.max(0,Math.min(1,-r.top/Math.max(1,run)))}}
/* each stop holds still for a while: progress becomes stepped with short glides between */
function stepped(p){{var s=p*n,k=Math.floor(s),f=s-k,g=f<.55?0:(f-.55)/.45;g=g*g*(3-2*g);return k+g}}
function draw(){{raf=0;var t=stepped(prog());/* t: 0 = now, 1 = first stop ... n */
rs.forEach(function(r,i){{var z=((i/R)+t*0.5)%1,sc=0.08+Math.pow(z,2.2)*2.4;r.style.transform='scale('+sc+')';r.style.opacity=z<.05?z*20:(sc>2?Math.max(0,1-(sc-2)/.5):1)}});
now.style.opacity=Math.max(0,1-t*1.6);now.style.transform='translate(-50%,-50%) scale('+(1+t*.8)+')';
ss.forEach(function(s,i){{var dz=t-(i+1);/* 0 = arriving, <0 still deep in the tunnel, >0 passed */
var sc=dz<0?Math.max(.15,1+dz*.85):1+dz*1.6,op=dz<-0.9?0:dz<0?1+dz/0.9:Math.max(0,1-dz*2.2);s.style.opacity=op;s.style.transform='translate(-50%,-50%) scale('+sc+')'}});
var k=Math.min(n-1,Math.max(0,Math.round(t)-1));clk.textContent=t<.5?'2026':Y[k]}}
addEventListener('scroll',function(){{if(!raf)raf=requestAnimationFrame(draw)}},{{passive:true}});addEventListener('resize',draw);draw()}})();
</script>'''
