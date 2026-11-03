"""About page drafts. Two ways to tell the same path: a dial that turns with the scroll, and a card drawer."""

GH = 'https://egec.github.io/backlot/'
LI = 'https://www.linkedin.com/feed/update/urn:li:activity:7354498102185058306/'
PV = ('<span class="ab-pv" aria-hidden="true"><span class="ab-pv-h"><i>HA</i><b>Hochschule Anhalt</b><em>Reposted by Ege Coskun</em></span>'
      '<span class="ab-pv-t">The Department of Design has honored two students with the DessauDesignAward 2025 for their outstanding theses.</span>'
      '<span class="ab-pv-f">View the post on LinkedIn</span></span>')
AWARD = f'<a class="ab-aw" href="{LI}" target="_blank" rel="noopener">Dessau Design Award{PV}</a>'
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
     ['Ranked first in class.', 'Thesis: a wearable for continuous monitoring in high-risk pregnancies. ' + AWARD + '.']),
    ('2024', 'work', 'Founding member, Product Designer', 'UwaVerde (NGO), remote', 'Jul 2024 to now',
     ['The organisation’s first design work, with no budget and nothing to inherit: the website and a member portal.']),
]
INTRO = ('I learned design where there’s no Ctrl+Z: a millimetre off in a bus interior part and the tooling is already paid for. '
         'I design B2B data products now, and the habit came with me.')
KIND = {'edu': 'Education', 'work': 'Experience'}
AB_LEAD = ('I design the parts of B2B software where a wrong click costs something: approvals, data that other teams depend on, decisions that are hard to undo.',
           'At MilSOFT I designed customs declarations and naval radar displays, and at UwaVerde I built the design function from nothing. Each time the domain was new to me, and learning it properly before designing for it is still the part I enjoy most.',
           'I studied Industrial Design at METU and finished a Master’s in Integrated Design at Hochschule Anhalt in 2025, first in my class. My thesis, a wearable that continuously monitors maternal and fetal health in high-risk pregnancies, won the ' + AWARD + '. It is still the clearest example of what I like doing: taking complex medical data and turning it into something a person can wear without thinking about it.')


HOW = [('Learn the domain first', 'Customs declarations, naval radar displays, data tools, a prenatal monitoring wearable. Each time, I learned how the work is really done, and by whom, before I started designing.'),
       ('Design for the unhappy path', 'Most products work when everything goes right. I spend more of my time on the other cases: the action that fails, the data that is missing, the step someone skips. That is where people decide whether they can trust a tool.'),
       ('A reason for every decision', 'If I cannot say why something sits where it does, it moves or goes. Hierarchy, colour and wording all need a reason I could defend in a review.'),
       ('User needs and business goals', 'A design is done when it works for the person using it and for the business paying for it. I keep both in the room, and when they pull in different directions, I make the trade-off visible instead of hiding it.')]
TOOLS = [('Figma', 'figma'), ('Claude Design', 'claude-icon'), ('Claude Code', 'claude-code'), ('Storybook', 'storybook-icon'), ('Jira', 'jira'), ('Confluence', 'confluence'),
         ('Webflow', 'webflow'), ('Miro', 'miro-icon'), ('Notion', 'notion-icon'), ('Illustrator', 'adobe-illustrator'), ('Photoshop', 'adobe-photoshop'), ('InDesign', 'adobe-indesign')]

def top():
    lead = ''.join(f'<p class="ab-lead">{x}</p>' for x in AB_LEAD)
    return f'<div class="cs-wrap ab-top"><p class="k">About</p><h1>Hi, I’m Ege.</h1>{lead}</div>'

def more():
    def chars(t):
        return ' '.join('<span class="hw-w">' + ''.join(f'<span class="hw-m"><span style="--d:{j}">{c}</span></span>' for j, c in enumerate(w)) + '</span>' for w in t.split(' '))
    how = ''.join(f'<article class="hw-c" style="--i:{i}"><p class="hw-k">How I work <em>{i + 1:02d}</em></p><div class="hw-b">'
                  f'<h3 class="hw-h" aria-label="{t}"><span aria-hidden="true">{chars(t)}</span></h3><p class="hw-p">{d}</p></div></article>'
                  for i, (t, d) in enumerate(HOW))
    tools = ''.join(f'<li><img src="{GH}logos/tc/{f}.svg" width="22" height="22" alt="" loading="lazy"><span>{t}</span></li>' for t, f in TOOLS)
    return (f'<section class="cs-wrap hw" aria-label="How I work">{how}</section>'
            f'<section class="cs-wrap ab-more">'
            f'<div class="ab-row"><p class="k">Tools</p><ul class="ab-tools">{tools}</ul></div></section>'
            '''<style>
.ab-more{padding-bottom:clamp(72px,8vw,140px)}
/* how I work: cards stack as you scroll, each keeps its label row in view; the heading's letters rise in when its card arrives */
.hw{position:relative;padding-top:clamp(56px,6vw,104px);padding-bottom:clamp(40px,10vh,120px)}
.hw-c{--row:52px;position:sticky;top:calc(4.75rem + var(--i) * var(--row));background:var(--bg);border-top:1px solid var(--line);min-height:min(56svh,520px);padding-bottom:clamp(40px,5vw,72px)}
.hw-k{display:flex;justify-content:space-between;align-items:center;height:var(--row);margin:0;font-size:13px;color:var(--mute)}
.hw-k em{font-style:normal;font-variant-numeric:tabular-nums}
.hw-b{display:flex;justify-content:space-between;align-items:flex-start;gap:clamp(24px,5vw,96px);padding-top:clamp(8px,1.4vw,20px)}
.hw-h{margin:0;max-width:9.5em;font-size:clamp(34px,4.6vw,78px);line-height:.92;letter-spacing:-.03em;font-weight:700;text-transform:uppercase;color:var(--g)}
.hw-w{display:inline-block;white-space:nowrap}
.hw-m{display:inline-block;overflow:hidden;vertical-align:top;padding-bottom:.04em}
.hw-m>span{display:inline-block;transform:translateY(105%);transition:transform .7s cubic-bezier(.23,1,.32,1);transition-delay:calc(var(--d) * 22ms)}
.hw-c.in .hw-m>span{transform:none}
.hw-p{margin:0;max-width:28em;padding-top:.4em;font-size:clamp(15px,1.15vw,19px);line-height:1.5;color:#3a3936;text-wrap:pretty}
@media(max-width:767px){.hw-c{--row:44px;min-height:0}.hw-b{flex-direction:column}.hw-h{font-size:clamp(30px,9vw,44px)}}
@media(prefers-reduced-motion:reduce){.hw-m>span{transform:none;transition:none}}
.ab-row{display:grid;grid-template-columns:calc(33.33% - 16px) minmax(0,1fr);gap:16px;padding-top:24px;margin-top:clamp(48px,5vw,88px);border-top:1px solid var(--line)}
.ab-tools{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:10px}
.ab-tools li{display:flex;align-items:center;gap:10px;padding:12px 14px;border:1px solid var(--line);border-radius:12px;background:var(--card2,#FCFCFB);font-size:14px;font-weight:500;transition:transform .3s var(--ease),border-color .2s}
.ab-tools li:hover{transform:translateY(-2px);border-color:#B9B6AE}
.ab-tools img{width:22px;height:22px;flex:none;object-fit:contain}
.ab-how{list-style:none;margin:0;padding:0}
.ab-how li{display:grid;grid-template-columns:48px minmax(0,1fr) minmax(0,1.4fr);gap:16px;padding:22px 0;border-bottom:1px solid var(--line)}
.ab-how li:first-child{padding-top:0}
.ab-how em{font-style:normal;font-size:13px;line-height:26px;color:var(--mute);font-variant-numeric:tabular-nums}
.ab-how h3{margin:0;font-size:clamp(18px,1.4vw,22px);line-height:1.25;font-weight:600;letter-spacing:-.01em;text-wrap:balance}
.ab-how p{margin:0;font-size:15px;line-height:1.5;color:#3a3936;text-wrap:pretty}
.ab-lead+.ab-lead{margin-top:12px;font-size:clamp(15px,1.05vw,17px);color:#55524c}
.ab-hero{display:grid;grid-template-columns:minmax(0,1.35fr) minmax(0,1fr);gap:clamp(32px,5vw,96px);align-items:end}
.ab-ph{margin:0;aspect-ratio:1/1.05;border-radius:14px;overflow:hidden;background:#ECECEA}
.ab-ph img{display:block;width:100%;height:100%;object-fit:cover;object-position:50% 30%}
.ab-aw{position:relative;color:inherit;text-decoration:underline;text-decoration-thickness:1px;text-underline-offset:3px}
.ab-aw:hover{text-decoration-color:var(--ink)}
.ab-pv{position:absolute;left:50%;bottom:calc(100% + 12px);z-index:20;width:300px;display:flex;flex-direction:column;gap:8px;padding:14px;border-radius:12px;background:#fff;border:1px solid var(--line);box-shadow:0 18px 50px rgba(0,0,0,.16);font-size:13px;line-height:1.45;color:#3a3936;text-align:left;
  opacity:0;pointer-events:none;transform:translate(-50%,6px) rotate(-1.5deg);transition:opacity .25s,transform .45s var(--ease)}
.ab-aw:hover .ab-pv,.ab-aw:focus-visible .ab-pv{opacity:1;transform:translate(-50%,0) rotate(-1.5deg)}
.ab-pv-h{display:grid;grid-template-columns:32px 1fr;column-gap:10px;align-items:center}
.ab-pv-h i{grid-row:span 2;width:32px;height:32px;border-radius:6px;background:#161616;color:#fff;font:600 11px/32px "Inter Tight",sans-serif;font-style:normal;text-align:center}
.ab-pv-h b{font-size:13px;color:var(--ink);font-weight:600}.ab-pv-h em{font-style:normal;font-size:11px;color:var(--mute)}
.ab-pv-t{display:block}.ab-pv-f{display:block;font-size:12px;font-weight:600;color:#0A66C2}
.ab-pv img{display:block;width:100%;border-radius:8px}
@media(max-width:991px){.ab-hero{grid-template-columns:1fr}.ab-ph{max-width:420px}}
@media(hover:none){.ab-pv{display:none}}
@media(max-width:767px){.ab-row{grid-template-columns:1fr}.ab-how li{grid-template-columns:32px 1fr}.ab-how p{grid-column:2}}
</style>
<script>(function(){var cs=document.querySelectorAll('.hw-c');if(!cs.length)return;if(!('IntersectionObserver' in window)){cs.forEach(function(c){c.classList.add('in')});return}
var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}})},{rootMargin:'0px 0px -30% 0px'});cs.forEach(function(c){io.observe(c)})})();</script>''')

def dial():
    items = ''.join(
        f'<button class="dl-y" type="button" data-i="{i}" aria-label="{y}, {t}"><span>{y}</span></button>' for i, (y, k, t, p, d, ls) in enumerate(PATH))
    cards = ''.join(
        f'<article class="dl-c" data-i="{i}"><p class="dl-k"><i class="{k}"></i>{KIND[k]}</p><h2>{t}</h2><p class="dl-p">{p}</p>'
        f'<p class="dl-d">{d}</p>' + ''.join(f'<p class="dl-l">{x}</p>' for x in ls) + '</article>'
        for i, (y, k, t, p, d, ls) in enumerate(PATH))
    lead = ''.join(f'<p class="ab-lead">{x}</p>' for x in AB_LEAD)
    return f'''<main class="ab ab-dl"><div class="ab-m">{top()}</div>
<section class="dl" data-dial style="--n:{len(PATH)}" aria-label="My path, from 2016 to now">
<div class="dl-pin"><div class="ab-in"><p class="k">About</p><h1>Hi, I’m Ege.</h1>{lead}</div><div class="dl-wheel" aria-hidden="true"><svg class="dl-arc" viewBox="0 0 1000 1000"><circle cx="500" cy="500" r="499" fill="none" stroke="currentColor" stroke-width="1.2" vector-effect="non-scaling-stroke"/></svg>
<i class="dl-dot"></i></div><div class="dl-ys">{items}</div><div class="dl-cs">{cards}</div>
<p class="dl-hint">Scroll to turn</p></div></section>{more()}</main>
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
.ab-in{{display:none}}
/* wide screens: the text sits on the left of the pinned dial, the wheel turns beside it */
@media(min-width:1100px){{
.ab-m{{display:none}}
.ab-dl .dl{{margin-top:0}}
.ab-dl .dl-pin{{--L:max(var(--pad),calc((100% - var(--w)) / 2));--W:min(600px,34vw);--T:calc(var(--L) + var(--W));--R:min(42svh,24vw)}}
.ab-in{{display:block;position:absolute;left:var(--L);top:50%;transform:translateY(-50%);width:var(--W);z-index:2}}
.ab-in h1{{font-size:clamp(34px,3.2vw,56px)}}
.ab-in .ab-lead{{font-size:clamp(15px,1.1vw,18px)}}
.ab-in .ab-lead+.ab-lead{{font-size:clamp(14px,.98vw,16px)}}
.ab-dl .dl-wheel{{left:calc(var(--T) - var(--R) * 1.3);clip-path:inset(-20px -20px -20px calc(var(--R) * 1.3 + 28px))}}
.ab-dl .dl-cs{{left:calc(var(--T) + var(--R) * .7 + 40px + 13vw);right:var(--L);max-width:30em}}
.ab-dl .dl-y{{font-size:clamp(26px,2.6vw,46px)}}
}}
</style>
<script>
(function(){{var d=document.querySelector('[data-dial]');if(!d)return;var ys=[].slice.call(d.querySelectorAll('.dl-y')),cs=[].slice.call(d.querySelectorAll('.dl-c')),wh=d.querySelector('.dl-wheel'),n=ys.length,STEP=19,cur=-1,raf=0;
function prog(){{var r=d.getBoundingClientRect(),run=d.offsetHeight-d.querySelector('.dl-pin').offsetHeight;return Math.max(0,Math.min(1,-r.top/Math.max(1,run)))}}
function draw(){{raf=0;var f=prog()*(n-1),w=wh.getBoundingClientRect(),pin=d.querySelector('.dl-pin').getBoundingClientRect(),R=w.width/2,cx=w.left-pin.left+R,cy=w.top-pin.top+R;
d.classList.toggle('moved',f>.15);
ys.forEach(function(y,i){{var a=(i-f)*STEP*Math.PI/180,x=cx+(R+40)*Math.cos(a),yy=cy+(R+40)*Math.sin(a),vis=Math.abs(i-f)<(innerWidth>=1100?3.1:4.2);
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
    """the drawer poster: index cards behind and in front of one big page; pointing at a tab puts that card on the page"""
    work = [(i, x) for i, x in enumerate(PATH) if x[1] == 'work'][::-1]
    edu = [(i, x) for i, x in enumerate(PATH) if x[1] == 'edu'][::-1]
    short = {'Middle East Technical University': 'METU', 'MilSOFT Software Technologies': 'MilSOFT', 'MAN Truck & Bus': 'MAN Truck & Bus', 'UwaVerde (NGO)': 'UwaVerde'}
    def nm(p):
        n = p.split(",")[0]
        return short.get(n, n)
    def row(i, x, k, side, front):
        y, kd, t, p, d, ls = x
        return (f'<div class="dx-r{" f" if front else ""}" style="--k:{k}"><button class="dx-t {side}" type="button" data-i="{i}" aria-label="{t}, {nm(p)}, {y}">'
                f'<span>{nm(p)}</span></button></div>')
    back = '<div class="dx-r" style="--k:0"><span class="dx-t l me">EGE COSKUN / 2016 TO NOW</span></div>' + ''.join(
        row(i, x, k + 1, 'r' if k % 2 == 0 else 'l', False) for k, (i, x) in enumerate(work))
    front = ''.join(row(i, x, k, 'r' if k % 2 else 'l', True) for k, (i, x) in enumerate(edu))
    pages = ''.join(
        f'<article class="dx-p" data-i="{i}"><div class="dx-ph"><span class="dx-bk">{t}</span><span class="dx-yr">{y}</span></div>'
        f'<div class="dx-cols"><div><p class="dx-lb">{KIND[k]}</p><p class="dx-pl">{p}</p><p class="dx-d">{d}</p></div><div>'
        + ''.join(f'<p class="dx-l">{x}</p>' for x in ls) + '</div></div></article>'
        for i, (y, k, t, p, d, ls) in enumerate(PATH))
    return f'''<main class="ab">{top()}
<section class="cs-wrap dx-sec" aria-label="My path, from 2016 to now"><div class="dx" data-dx>
<div class="dx-back">{back}</div>
<div class="dx-page"><div class="dx-in">{pages}</div></div>
<div class="dx-front">{front}</div>
<svg class="dx-box" viewBox="0 0 1000 260" preserveAspectRatio="none" aria-hidden="true"><path d="M30 2 H970 L996 30 V258 H4 V30 Z" fill="#F7F7F5" stroke="#161616" stroke-width="1.6" vector-effect="non-scaling-stroke"/><path d="M4 30 H996" fill="none" stroke="#161616" stroke-width="1.2" vector-effect="non-scaling-stroke"/></svg>
<span class="dx-hd" aria-hidden="true"><i></i><i></i><i></i></span>
</div></section>{more()}</main>
<style>
.ab .k{{font-size:13px;color:var(--mute);margin:0}}
.ab-top{{padding-top:clamp(40px,6vw,96px)}}
.ab h1{{margin:10px 0 0;font-size:clamp(34px,3.6vw,60px);line-height:1.04;letter-spacing:-.03em;font-weight:600}}
.ab-lead{{margin:18px 0 0;max-width:36em;font-size:clamp(16px,1.2vw,20px);line-height:1.45;color:#3a3936;text-wrap:pretty}}

.dx-sec{{padding-top:clamp(40px,5vw,80px)}}
.dx{{--L:#161616;--W:min(100%,820px);position:relative;width:var(--W);margin:0 auto;padding-bottom:clamp(120px,13vw,170px)}}
.dx-back{{position:relative;height:calc(4 * 26px + 30px)}}
.dx-r{{position:absolute;left:calc(9% - var(--k) * 1.2%);right:calc(9% - var(--k) * 1.2%);top:calc(var(--k) * 26px);height:90px;background:#FDFDFC;border:1.5px solid var(--L);border-radius:10px 10px 0 0}}
.dx-front{{position:relative;margin-top:calc(-1 * (2 * 30px + 70px));height:calc(2 * 30px + 70px);z-index:4}}
.dx-r.f{{left:calc(1% - var(--k) * 1.2%);right:calc(1% - var(--k) * 1.2%);top:calc(var(--k) * 30px);height:120px}}
.dx-t{{position:absolute;top:-25px;height:26px;min-width:30%;padding:0 22px;background:#FDFDFC;border:1.5px solid var(--L);border-bottom:0;border-radius:14px 14px 0 0;display:flex;align-items:center;justify-content:center;
  font:600 12px/1 "Inter Tight",sans-serif;letter-spacing:.14em;text-transform:uppercase;color:var(--ink);cursor:pointer;transition:background .2s,color .2s,transform .3s var(--ease)}}
.dx-t.l{{left:12%}}.dx-t.r{{right:12%}}
.dx-t:before{{content:"";position:absolute;left:-1.5px;right:-1.5px;bottom:-3px;height:4px;background:inherit}}
.dx-t.me{{background:var(--ink);color:#fff;cursor:default;letter-spacing:.12em}}
button.dx-t:hover,button.dx-t:focus-visible,button.dx-t.on{{background:var(--ink);color:#fff}}
button.dx-t:hover{{transform:translateY(-3px)}}
button.dx-t:focus-visible{{outline:2px solid var(--ink);outline-offset:4px}}
.dx-page{{position:relative;z-index:3;margin:-58px 4% 0;height:clamp(440px,44vw,500px);background:#FDFDFC;border:1.5px solid var(--L);border-radius:6px;padding:16px}}
.dx-in{{position:relative;height:100%;border:1.5px solid var(--L);border-radius:2px;background:#fff;overflow:hidden}}
.dx-in:before{{content:"";position:absolute;inset:12px;border:1px dashed #B9B6AE;pointer-events:none}}
.dx-p{{position:absolute;inset:0;padding:clamp(26px,3vw,40px) clamp(26px,3vw,40px) 140px;opacity:0;transition:opacity .25s}}
.dx-p.on{{opacity:1}}
.dx-ph{{display:flex;align-items:stretch;border:1.5px solid var(--L)}}
.dx-bk{{flex:1;padding:10px 14px;background:var(--ink);color:#fff;font:600 clamp(18px,2.2vw,30px)/1.1 "Inter Tight",sans-serif;letter-spacing:.06em;text-transform:uppercase}}
.dx-yr{{display:flex;align-items:center;padding:0 16px;font:600 clamp(18px,2.2vw,30px)/1 "Inter Tight",sans-serif;letter-spacing:.06em;font-variant-numeric:tabular-nums}}
.dx-cols{{display:grid;grid-template-columns:minmax(0,.8fr) minmax(0,1.2fr);gap:20px;margin-top:20px;padding-top:16px;border-top:1.5px dotted var(--L)}}
.dx-lb{{margin:0;font:600 11px/1 "Inter Tight",sans-serif;letter-spacing:.14em;text-transform:uppercase;color:var(--mute)}}
.dx-pl{{margin:10px 0 0;font-size:16px;font-weight:600;line-height:1.3}}
.dx-d{{margin:6px 0 0;font-size:13px;color:var(--mute)}}
.dx-l{{margin:0 0 8px;font-size:15px;line-height:1.45;color:#3a3936;text-wrap:pretty}}
.dx-box{{position:absolute;left:-2%;right:-2%;bottom:0;width:104%;height:clamp(150px,16vw,200px);z-index:5}}
.dx-hd{{position:absolute;left:50%;bottom:clamp(50px,5.5vw,70px);transform:translateX(-50%);z-index:6;display:flex;flex-direction:column;gap:3px}}
.dx-hd i{{display:block;width:120px;height:11px;border:1.5px solid var(--L);border-radius:0 0 14px 14px;background:#FDFDFC}}
@media(max-width:767px){{.dx-t{{min-width:0;padding:0 10px;font-size:10px;letter-spacing:.08em}}.dx-t.l{{left:4%}}.dx-t.r{{right:4%}}.dx-page{{height:600px}}.dx-cols{{grid-template-columns:1fr}}.dx-t.me{{font-size:9px}}}}
@media (prefers-reduced-motion:reduce){{.dx-p,.dx-t{{transition:none}}}}
</style>
<script>
(function(){{var w=document.querySelector('[data-dx]');if(!w)return;var ts=[].slice.call(w.querySelectorAll('button.dx-t')),ps=[].slice.call(w.querySelectorAll('.dx-p'));
function pick(i){{ts.forEach(function(t){{var on=t.dataset.i==i;t.classList.toggle('on',on);t.setAttribute('aria-pressed',on)}});ps.forEach(function(p){{p.classList.toggle('on',p.dataset.i==i)}})}}
ts.forEach(function(t){{t.addEventListener('mouseenter',function(){{pick(t.dataset.i)}});t.addEventListener('focus',function(){{pick(t.dataset.i)}});t.addEventListener('click',function(){{pick(t.dataset.i)}})}});pick({len(PATH)-1})}})();
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
