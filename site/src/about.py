"""About page drafts. Two ways to tell the same path: a dial that turns with the scroll, and a card drawer."""

GH = 'https://egec.github.io/backlot/'
LI = 'https://www.linkedin.com/feed/update/urn:li:activity:7354498102185058306/'
PV = ('<span class="ab-pv" aria-hidden="true"><span class="ab-pv-h"><i>HA</i><b>Hochschule Anhalt</b><em>Reposted by Ege Coskun</em></span>'
      '<span class="ab-pv-t">The Department of Design has honored two students with the DessauDesignAward 2025 for their outstanding theses.</span>'
      '<span class="ab-pv-f">View the post on LinkedIn</span></span>')
AWARD = f'<a class="ab-aw" href="{LI}" target="_blank" rel="noopener">Dessau Design Award{PV}</a>'
PATH = [
    # (year label, kind, title, place, dates, lines)
    ('2016', 'edu', 'Industrial Design, B.Sc.', 'Middle East Technical University, Ankara', 'Oct 2016 to Jul 2021',
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
    ('2026', 'work', 'Product Designer', 'Insider One, remote from Berlin', 'May 2026 to Sep 2026',
     ['Data health for a customer data platform: where each attribute’s data comes from, and a warning in the segment builder before a segment breaks.']),
]
INTRO = ('I learned design where there’s no Ctrl+Z: a millimetre off in a bus interior part and the tooling is already paid for. '
         'I design B2B data products now, and the habit came with me.')
KIND = {'edu': 'Education', 'work': 'Experience'}
AB_LEAD = ('Every project began in a domain I didn’t know: customs regulation, naval radar, customer data, maternal and fetal health. That first stretch is my favourite part. Before I draw anything, I want to know how the work is really done, who pays when it goes wrong, and which rule the backend will never bend.',
           'Most of what I need is already written down by someone who isn’t a designer. So I read the specs, sit with the system engineers, and take a PM’s request apart until I find the customer problem underneath it. When a decision costs one side something, I say so in the room instead of hiding it in the layout. When the call goes the other way, I want it written down, so we can come back to it once real usage shows who was right.',
           'The fastest way to settle those conversations is usually to show something. AI is part of how I work every day: I explore and prototype with Claude, and I built and shipped this site in code with Claude Code, live prototypes included. Often the first thing a PM sees from me is something they can try.',
           'I’m based in Berlin and open to relocation. I’m looking for a team with high standards and bad jokes.')


HOW = [('No playbook, no problem', 'Customs, naval radar, customer data, prenatal health. Each domain was new to me and none came with a playbook. I learned how the work is really done and who does it, then turned messy requests into clear flows.'),
       ('Design for the unhappy path', 'Most products work when everything goes right. I spend more of my time on the other cases: the action that fails, the data that is missing, the step someone skips. That is where people decide whether they can trust a tool.'),
       ('Systems that hold<br>as the product grows', 'I’ve extended and maintained design systems at two companies: adding components when a flow needed them and fixing the ones that broke in real use, so the product stays consistent as it changes.'),
       ('AI that people can check', 'When a feature uses AI, I design for review: what it suggests, how sure it is, and a quick way to accept, change or reject it. Nothing is written without a person.'),
       ('Decisions with evidence', 'Support tickets, session replays and watching people work tell me more than a brief. Every decision needs a reason I can defend, and the trade-off goes on the table.')]
TOOLS = [('Figma', 'figma'), ('Claude Design', 'claude-icon'), ('Claude Code', 'claude-code'), ('Storybook', 'storybook-icon'), ('Jira', 'jira'), ('Confluence', 'confluence'),
         ('Webflow', 'webflow'), ('Miro', 'miro-icon'), ('Notion', 'notion-icon'), ('Illustrator', 'adobe-illustrator'), ('Photoshop', 'adobe-photoshop'), ('InDesign', 'adobe-indesign')]

def top():
    lead = ''.join(f'<p class="ab-lead">{x}</p>' for x in AB_LEAD)
    return f'<div class="cs-wrap ab-top"><p class="k">About</p><h1>Hi, I’m <span class="ax-nm" tabindex="0">Ege<span class="ax-say" role="tooltip">[eh-GEH]</span></span>.</h1>{lead}</div>'

def more():
    def chars(t):
        return ' '.join('<span class="hw-w">' + ''.join(f'<span class="hw-m"><span style="--d:{j}">{c}</span></span>' for j, c in enumerate(w)) + '</span>' for w in t.split(' '))
    how = ''.join(f'<article class="hw-c" style="--i:{i}"><i class="hw-ln" aria-hidden="true"></i><p class="hw-k">{i + 1:02d}</p><div class="hw-b">'
                  f'<h3 class="hw-h" aria-label="{t}"><span aria-hidden="true">{chars(t)}</span></h3><p class="hw-p">{d}</p></div></article>'
                  for i, (t, d) in enumerate(HOW))
    tools = ''.join(f'<li><img src="{GH}logos/tc/{f if '.' in f else f + '.svg'}" width="22" height="22" alt="" loading="lazy"><span>{t}</span></li>' for t, f in TOOLS)
    return (f'<section class="cs-wrap hw" aria-labelledby="hw-t"><h2 class="hw-t" id="hw-t">How I work</h2>{how}</section>'
            f'<section class="cs-wrap ab-more">'
            f'<div class="ab-row"><p class="k">Tools</p><ul class="ab-tools">{tools}</ul></div></section>'
            '''<style>
.ab-more{padding-bottom:clamp(72px,8vw,140px)}
/* how I work: cards stack as you scroll, each keeps its label row in view; the heading's letters rise in when its card arrives */
.hw{position:relative;padding-top:clamp(56px,6vw,104px);padding-bottom:0}.hw-c:last-child{min-height:0}
.hw+.ab-more .ab-row:first-child{margin-top:clamp(24px,3vw,48px)}
.hw-t{margin:0 0 clamp(24px,3vw,48px);font-size:clamp(28px,2.6vw,44px);line-height:1.05;letter-spacing:-.025em;font-weight:600}
.hw-c{--row:52px;position:sticky;top:calc(4.75rem + var(--i) * var(--row));background:var(--bg);border-top:1px solid #D3D3CF;min-height:min(56svh,520px);padding-bottom:clamp(40px,5vw,72px)}
.hw-ln{position:absolute;left:0;top:-1px;height:2px;width:calc(var(--p,0) * 100%);background:var(--g)}
.hw-k{display:flex;justify-content:space-between;align-items:center;font-variant-numeric:tabular-nums;height:var(--row);margin:0;font-size:13px;color:var(--mute)}
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
.ab-ph{margin:0;aspect-ratio:1/1.05;border-radius:14px;overflow:hidden;background:#E7E6E1}
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
@media(hover:none),(max-width:767px){.ab-pv{display:none}}
@media(max-width:767px){.ab-row{grid-template-columns:1fr}.ab-how li{grid-template-columns:32px 1fr}.ab-how p{grid-column:2}}
</style>
<script>(function(){var cs=document.querySelectorAll('.hw-c');if(!cs.length)return;if(!('IntersectionObserver' in window)){cs.forEach(function(c){c.classList.add('in')});return}
var io=new IntersectionObserver(function(es){es.forEach(function(e){if(e.isIntersecting){e.target.classList.add('in');io.unobserve(e.target)}})},{rootMargin:'0px 0px -30% 0px'});cs.forEach(function(c){io.observe(c)});
/* each card's line fills as the card travels up to its resting place */
var raf=0;function ln(){raf=0;var vh=innerHeight;cs.forEach(function(c){var r=c.getBoundingClientRect(),stop=parseFloat(getComputedStyle(c).top)||0;c.style.setProperty('--p',Math.max(0,Math.min(1,(vh-r.top)/Math.max(1,vh-stop))).toFixed(3))})}
addEventListener('scroll',function(){if(!raf)raf=requestAnimationFrame(ln)},{passive:true});addEventListener('resize',ln);ln()})();</script>''')

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
<div class="dl-pin"><div class="ab-in"><p class="k">About</p><h1>Hi, I’m <span class="ax-nm" tabindex="0">Ege<span class="ax-say" role="tooltip">[eh-GEH]</span></span>.</h1>{lead}</div><div class="dl-wheel" aria-hidden="true"><svg class="dl-arc" viewBox="0 0 1000 1000"><circle cx="500" cy="500" r="499" fill="none" stroke="currentColor" stroke-width="1.2" vector-effect="non-scaling-stroke"/></svg>
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
.dl-k i{{width:8px;height:8px;border-radius:50%;background:#3B1223}}.dl-k i.edu{{background:transparent;box-shadow:inset 0 0 0 1.5px #3B1223}}
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
.ab-dl .dl-pin{{--L:clamp(20px,2.4vw,44px);--W:min(600px,34vw);--T:calc(var(--L) + var(--W));--R:min(42svh,24vw)}}
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
dts.forEach(function(d,i){{d.addEventListener('click',function(){{go(i)}})}});
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
<svg class="dx-box" viewBox="0 0 1000 260" preserveAspectRatio="none" aria-hidden="true"><path d="M30 2 H970 L996 30 V258 H4 V30 Z" fill="#F2F1ED" stroke="#161616" stroke-width="1.6" vector-effect="non-scaling-stroke"/><path d="M4 30 H996" fill="none" stroke="#161616" stroke-width="1.2" vector-effect="non-scaling-stroke"/></svg>
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
<div class="tn-now"><p class="k">About</p><h1>Hi, I’m <span class="ax-nm" tabindex="0">Ege<span class="ax-say" role="tooltip">[eh-GEH]</span></span>.</h1><p class="ab-lead">{INTRO}</p><p class="tn-go">Scroll to go back in time</p></div>
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
.tn-go{{margin:22px 0 0;font:400 30px/1 "Reenie Beanie",cursive;color:#3B1223}}
.tn-ss{{position:absolute;inset:0;pointer-events:none}}
.tn-s{{position:absolute;left:50%;top:50%;width:min(620px,86%);transform:translate(-50%,-50%);text-align:center;opacity:0}}
.tn-y{{margin:0;font-size:clamp(64px,9vw,150px);line-height:.9;letter-spacing:-.05em;font-weight:700;color:var(--ink)}}
.tn-c{{margin-top:14px}}
.tn-k{{margin:0;font:400 26px/1 "Reenie Beanie",cursive;color:#3B1223}}
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


QA = [('What’s the hardest workflow you’ve designed?', 'Backlot, the case study that got me my last job: an editor prepares content, a publisher approves it, and the complexity is in the rules between them. The decision I’d defend anywhere: rejection reasons are a fixed list, not free text. You can’t count free-form comments, and if you can’t count them, you can’t tell an editor what they keep getting wrong.'),
      ('When did a technical constraint change your design?', 'At MilSOFT the customs backend was fixed and there was no product brief. Most of the work was separating fields that were written in sequence but weren’t actually dependent, so the form follows what an officer knows at each point. Where the model did force an order, a blocked field says what has to happen first instead of sitting there greyed out.'),
      ('What do you do when you have to compromise?', 'Put the trade-off on the table instead of quietly optimising for one side. If the call goes the other way, I ask for it to be written down and design the chosen version as well as I can. Real usage usually settles it later.'),
      ('How do you use AI?', 'Every day, for real work: exploring, prototyping, and building this site in code. I still make every decision, and I check what the AI makes against how the system actually behaves, because my assumption about the data is usually the thing that’s wrong.'),
      ('When can you start?', 'Within two weeks of signing. I’m based in Berlin and open to relocation.')]



EVENTS = [(2016.8, 2021.55, '2016 to 2021', 'Industrial Design, B.Sc.', 'Middle East Technical University, Ankara', 'Five years of making things that have to be built: sketches, foam and clay models, prototypes.', ''),
          (2021.95, 2022.45, '2021 to 2022', 'Industrial Designer', 'MAN Truck & Bus, Ankara', 'Bus interior parts, designed within tooling cost, lead time and the production schedule.', ''),
          (2022.7, 2023.8, '2022 to 2023', 'UX/UI Designer', 'MilSOFT Software Technologies, Ankara', 'BİLGE, the customs platform of the Turkish Ministry of Trade, and radar screens for naval systems.', ''),
          (2023.8, 2025.55, '2023 to 2025', 'Integrated Design, M.A.', 'Hochschule Anhalt, Dessau', 'First in class. Thesis: a wearable for continuous monitoring in high-risk pregnancies. ' + AWARD + '.',
           '<div class="ax-side"><p class="ax-sk">From 2024, alongside</p><p class="ax-sh">Founding member, Product Designer</p><p>UwaVerde (NGO): the organisation’s first design work, a website and a member portal. Still going.</p></div>'),
          (2026.35, 2026.7, '2026', 'Product Designer', 'Insider One, remote from Berlin', 'Data health in a customer data platform.', ''),
          (2026.85, 2026.95, 'Now', 'Looking for my next team', 'Within Germany, currently in Berlin', 'Open to product design roles.<br>If the domain is new to me, even better.', '')]

QCSS = """.ax-ask{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.6fr);gap:clamp(32px,5vw,96px);padding-top:clamp(32px,4vw,64px);padding-bottom:clamp(64px,7vw,120px)}
.ax-ask h2{position:sticky;top:calc(4.75rem + 24px);align-self:start}
.ax-qs{display:flex;flex-direction:column;gap:10px;--qbg:#262624;--qbd:rgba(255,255,255,.18);--qtx:#F2F2EF;--abg:#30302d}
.ax-ask.lt .ax-qs{--qbg:#E7E6E1;--qbd:#D2D1CC;--qtx:var(--ink);--abg:#fff}
.ax-q summary{display:inline-flex;align-items:center;max-width:100%;box-sizing:border-box;padding:16px 24px;border-radius:22px;background:var(--qbg);border:1px solid transparent;color:var(--qtx);cursor:pointer;list-style:none;font-size:var(--h3);font-weight:500;letter-spacing:-.01em;line-height:1.3;transition:border-color .3s,background .3s}
.ax-q summary::-webkit-details-marker{display:none}
.ax-q summary:hover{border-color:var(--qbd)}
.ax-q[open]:not(.cl) summary{background:transparent;border-color:var(--qtx);border-bottom-left-radius:0}
.ax-q summary:focus-visible{outline:2px solid #D492EC;outline-offset:3px}
.ax-a{overflow:hidden}
.ax-ai{display:flex;justify-content:flex-end;padding:10px 12px 6px 0}
.ax-a p{position:relative;margin:0!important;max-width:36em;padding:18px 24px;background:var(--abg);border-radius:22px 22px 0 22px;color:var(--qtx)!important;font-size:var(--fs,16px);line-height:1.5}
.ax-ask.lt{color:var(--ink)}
.ax-qc{margin:20px 0 0;font-size:14px;line-height:1.6;color:var(--mute)}.ax-qc a{color:var(--ink);text-underline-offset:3px}
@media(max-width:899px){.ax-ask{grid-template-columns:1fr}.ax-ask h2,.wk-qa .k{position:static}}
@media (prefers-reduced-motion:reduce){.ax-q summary{transition:none}}
"""
NMCSS = """.ax-nm{position:relative;cursor:help;text-decoration:underline dotted 2px;text-decoration-color:var(--line);text-underline-offset:6px}.ax-say{position:absolute;left:50%;bottom:calc(100% + 8px);transform:translate(-50%,6px);padding:6px 10px;border-radius:8px;background:#3B1223;color:#D492EC;font-size:14px;font-weight:500;letter-spacing:0;white-space:nowrap;opacity:0;pointer-events:none;transition:opacity .2s,transform .2s}.ax-nm:hover .ax-say,.ax-nm:focus .ax-say{opacity:1;transform:translate(-50%,0)}"""
QJS = """<script>(function(){var R=matchMedia('(prefers-reduced-motion:reduce)').matches;
function rise(a){var p=a.querySelector('p');if(!p||p._r)return;p._r=1;var src=p.innerHTML,ws=[];(function w(n){[].slice.call(n.childNodes).forEach(function(c){if(c.nodeType===3){var f=document.createDocumentFragment();c.nodeValue.split(/(\\s+)/).forEach(function(t){if(!t)return;if(/^\\s+$/.test(t)){f.appendChild(document.createTextNode(t));return}var s=document.createElement('span');s.textContent=t;s.style.cssText='display:inline-block';ws.push(s);f.appendChild(s)});c.parentNode.replaceChild(f,c)}else if(c.nodeType===1)w(c)})})(p);var ln=-1,top=null;ws.forEach(function(s){var t=s.offsetTop;if(top===null||Math.abs(t-top)>4){ln++;top=t}s._l=ln;s.style.opacity=0;s.style.transform='translateY(.7em)'});var last=0;ws.forEach(function(s){var d=120+s._l*70;last=Math.max(last,d);s.animate([{opacity:0,transform:'translateY(.7em)'},{opacity:1,transform:'none'}],{duration:520,delay:d,easing:'cubic-bezier(.2,.8,.2,1)',fill:'both'})});setTimeout(function(){p.innerHTML=src;p._r=0},last+560)}
function op(d){d.open=true;if(R)return;var a=d.querySelector('.ax-a');a.animate([{height:'0px'},{height:a.scrollHeight+'px'}],{duration:450,easing:'cubic-bezier(.2,.8,.2,1)'});rise(a)}
function cl(d){if(R){d.open=false;return}var a=d.querySelector('.ax-a');if(d._x)return;d.classList.add('cl');var x=a.animate([{height:a.offsetHeight+'px',opacity:1},{height:'0px',opacity:0}],{duration:450,easing:'cubic-bezier(.2,.8,.2,1)',fill:'forwards'});d._x=x;x.onfinish=function(){d.open=false;d.classList.remove('cl');x.cancel();d._x=null}}
[].forEach.call(document.querySelectorAll('.ax-qs'),function(g){[].forEach.call(g.querySelectorAll('.ax-q'),function(d){d.querySelector('summary').addEventListener('click',function(e){e.preventDefault();if(d.open){cl(d);return}[].forEach.call(g.querySelectorAll('.ax-q[open]'),cl);op(d)})})})})();</script>"""

def qa_html():
    return ''.join(f'<details class="ax-q"><summary>{q}</summary><div class="ax-a"><div class="ax-ai"><p>{a}</p></div></div></details>' for q, a in QA)



CENTER_CSS = """.ax-c{position:relative;display:block;text-align:center;min-height:clamp(380px,34vw,500px);box-sizing:border-box}
.ax-ct{margin:0 auto;max-width:min(36em,calc(100% - 2 * var(--bw) - 48px))}.ax-c .ax-tx{max-width:none}
.abx{--bw:clamp(150px,13vw,200px)}
.ax-bp img,.ax-dp img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;pointer-events:none;-webkit-user-drag:none}
.ax-bp .ax-p,.ax-dp .ax-p{opacity:0;transition:opacity .4s}.ax-sw:hover .ax-p,.ax-dock:hover .ax-p{opacity:1}
@media(max-width:899px){.ax-ct{max-width:36em}.ax-c{min-height:0}}
"""
SIGN = '<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Mrs+Saint+Delafield&display=swap">'
SWING_CSS = """.ax-c.sw{overflow:hidden;min-height:600px}
.ax-hang{position:absolute;left:-4px;top:-70px;width:270px;height:650px;z-index:2;pointer-events:none}
.ax-sw{position:absolute;inset:0;transform-origin:50% 50%;animation:axsw 1.6s .25s both}
@keyframes axsw{0%{transform:translate(-179px,-243px) rotate(45deg);animation-timing-function:cubic-bezier(.3,.6,.3,1)}
 70%{transform:none;animation-timing-function:ease-in-out}82%{transform:rotate(5deg);animation-timing-function:ease-in-out}100%{transform:none}}
.ax-rope{position:absolute;left:0;top:0;width:270px;height:320px;overflow:visible}
.ax-rope path{fill:none;stroke:#1c1c1c;stroke-width:1.3}
.ax-card{position:absolute;left:0;top:310px;width:260px;height:340px;border-radius:18px;overflow:hidden;background:rgba(214,214,211,.62);-webkit-backdrop-filter:blur(3px);backdrop-filter:blur(3px)}
.ax-slot{position:absolute;left:34px;right:62px;top:22px;height:12px;border-radius:8px;background:#fff}
.ax-cp{position:absolute;left:32px;top:54px;width:172px;height:172px;border-radius:50%;overflow:hidden;background:#ddd}
.ax-cp img{width:100%;height:100%;object-fit:cover;display:block}
.ax-card .ax-sg{position:absolute;font-family:"Mrs Saint Delafield",cursive!important;color:#262626;font-weight:400;line-height:1;white-space:nowrap}
.ax-cr{left:30px;top:234px;font-size:36px;-webkit-text-stroke:.4px #262626;padding:0 26px 4px 2px;border-bottom:1px solid #262626;transform:rotate(-4deg);transform-origin:0 100%}
.ax-cn{left:34px;bottom:-34px;font-size:150px;color:#B3B3B0!important;-webkit-text-stroke:2.5px #B3B3B0;letter-spacing:-.02em}
@media(max-width:899px){.ax-c.sw{min-height:0}.ax-hang{position:relative;left:calc(-1 * var(--px) / .72 - 10px);top:auto;zoom:.72;margin:-120px 0 40px}}
@media (prefers-reduced-motion:reduce){.ax-sw{animation:none}}
"""
DOCK_CSS = """.ax-print{position:absolute;left:var(--px);bottom:clamp(24px,3vw,48px);width:var(--bw);margin:0;padding:10px 10px 50px;background:#fff;border:4px solid #1c1c1c;border-radius:3px;box-shadow:0 12px 30px rgba(0,0,0,.12)}
.ax-print img{display:block;width:100%;height:auto;aspect-ratio:4/5;object-fit:cover}
.ax-rv{position:absolute;width:6px;height:6px;border-radius:50%;background:#d6d6d3;box-shadow:inset 0 -1px 1px rgba(0,0,0,.35)}
.ax-rv:nth-child(1){left:-5px;top:-5px}.ax-rv:nth-child(2){right:-5px;top:-5px}.ax-rv:nth-child(3){left:-5px;bottom:-5px}.ax-rv:nth-child(4){right:-5px;bottom:-5px}
.ax-print .ax-sg{position:absolute;left:22px;bottom:6px;font-family:"Mrs Saint Delafield",cursive!important;font-size:clamp(30px,2.6vw,40px);line-height:1;color:#1c1c1c;transform:rotate(-4deg);white-space:nowrap}
@media(max-width:899px){.ax-print{position:relative;left:auto;bottom:auto;width:180px;margin:32px 0 8px}}
"""

ROWS = [('What I like to own', 'The whole arc of a feature: the first interview, the flows, the prototype, and the review of what developers built against the design.'), ('Working with clients', 'I bring options to a review instead of arguing for one: the version I recommend, next to the one I expect them to ask for. The client feels heard, the decision comes faster, and I get back to the work with what I need.')]
DARK_CSS = """body:has(.abx.dk),body:has(.abx.dk) .site-h{background:#161616}body:has(.abx.dk) .site-h{color:#F2F2EF}body:has(.abx.dk) .site-h a{color:#F2F2EF}body:has(.abx.dk) .site-h img{filter:invert(1)}
.abx.dk{--ink:#F2F2EF;--line:rgba(255,255,255,.14);--mute:#9B9A96;background:#161616;color:#F2F2EF}.abx.dk .ax-tx p,.abx.dk .ax-pd p{color:#CFCECA}.abx.dk .ax-tq{border-color:#3a3a37}.abx.dk .ax-tq.y{border-color:#6a6a66}.abx.dk .ax-side{background:#222220}.abx.dk .ax-end{background:#F2F2EF}
.ax-ia{display:grid;grid-template-columns:minmax(0,.85fr) minmax(0,1fr);gap:clamp(32px,5vw,96px);padding-top:clamp(40px,6vh,96px);padding-bottom:clamp(56px,7vh,112px)}.ax-l{display:flex;flex-direction:column;justify-content:space-between;gap:40px}
.abx .ax-big{margin:0;max-width:16em;font-size:clamp(22px,1.9vw,34px)!important;line-height:1.15!important;letter-spacing:-.02em;font-weight:500;color:#6E6D68!important}
.ax-ia .ax-r{max-width:36em}.ax-ia .ax-rows{grid-column:2;max-width:36em;margin-top:8px}.ax-ia .ax-tx p:last-child{margin-bottom:0}.ax-ia .ax-rows dd{font-size:var(--fs)}@media(max-width:899px){.ax-ia .ax-rows{grid-column:1}}.abx .ax-nmw h1,.abx .ax-nmw .ax-sub{display:inline}.abx .ax-sub{margin:0;font-size:clamp(18px,1.4vw,24px);line-height:1.3;font-weight:600;letter-spacing:-.015em;color:#D492EC!important;max-width:20em}.abx .ax-l h1{font-size:clamp(18px,1.4vw,24px)!important;line-height:1.3!important;font-weight:600!important;letter-spacing:-.015em!important;margin:0;font-size:clamp(30px,2.6vw,46px);color:#6E6D68}.abx .ax-l .ax-nm{text-decoration-color:#3a3a37}.abx .ax-role{margin:0;font-size:clamp(18px,1.4vw,24px)!important;color:#8E8D88!important}
.ax-fr{position:relative;margin:0;width:clamp(190px,18vw,270px);aspect-ratio:900/995}.ax-fr img{display:block;width:100%;height:100%;object-fit:cover;object-position:50% 38%}.ax-fr .fr-l{position:absolute;left:-5.93%;top:-5.37%;width:111.85%;height:110.5%;overflow:visible;pointer-events:none}
.ax-ph{width:clamp(120px,11vw,180px);aspect-ratio:1;border-radius:50%;overflow:hidden;margin:0}.ax-ph img{width:100%;height:100%;object-fit:cover;display:block}
.ax-ib{display:grid;grid-template-columns:minmax(0,1.5fr) minmax(0,.8fr);gap:clamp(32px,5vw,96px);padding-top:clamp(40px,5vw,88px);padding-bottom:clamp(56px,6vw,104px)}
.ax-ib .ax-lead{font-size:clamp(18px,1.3vw,22px);line-height:1.45;color:#CFCECA;margin:0 0 28px;max-width:34em}
.ax-rows{margin:0;border-top:1px solid var(--line)}.ax-rows>div{display:grid;grid-template-columns:minmax(0,.55fr) minmax(0,1fr);gap:24px;padding:18px 0;border-bottom:1px solid var(--line)}
.ax-rows dt{font-size:14px;color:var(--mute)}.ax-rows dd{margin:0;font-size:clamp(16px,1.1vw,19px);line-height:1.5}
.ax-ib .ax-ph{position:static;width:100%;max-width:300px;aspect-ratio:4/5;border-radius:14px;align-self:start;justify-self:end}
@media(max-width:899px){.ax-ia,.ax-ib{grid-template-columns:1fr;min-height:0}.ax-ph{position:static;margin-top:8px}.ax-ib .ax-ph{justify-self:start;max-width:220px}.ax-rows>div{grid-template-columns:1fr;gap:4px}}
"""
def about3(intro="flip"):
    """intro with a portrait; experience on a moving crosshair that turns the page dark; then How I work, questions and tools on dark"""
    lead = ''.join(f'<p>{x}</p>' for x in AB_LEAD)
    n = len(EVENTS)
    Y0 = 2016
    ticks = ''.join(f'<i class="ax-tq{" y" if q % 4 == 0 else ""}" style="--o:{q / 4}"></i>' for q in range(0, 11 * 4 + 1))
    bars = ''
    tmin, tmax = EVENTS[0][0], EVENTS[-1][0]
    fr = lambda v: max(0, min(1, (v - tmin) / (tmax - tmin)))
    dots = ''.join(f'<button type="button" class="ax-dt" data-i="{i}" style="--f:{fr(ev[0]):.4f}" aria-label="{ev[3]}"><span>{ev[2].split(" ")[0]}</span></button>' for i, ev in enumerate(EVENTS))
    nxt = [fr(EVENTS[i + 1][0]) if i + 1 < len(EVENTS) else fr(EVENTS[i][1]) for i in range(len(EVENTS))]
    chipf = lambda ti: '<span class="ax-chip">Bachelor’s</span>' if 'B.Sc' in ti else ('<span class="ax-chip">Master’s</span>' if 'M.A.' in ti else '')
    cards = ''.join(f'<article class="ax-pc{" edu" if ("B.Sc" in ti or "M.A." in ti) else ""}" data-t="{t - Y0}" data-e="{e - Y0}" data-fa="{fr(t):.4f}" data-fb="{nxt[i]:.4f}" style="--fa:{fr(t):.4f}"><p class="ax-when">{w}{chipf(ti)}</p><div class="ax-pg2"><div class="ax-ti"><h3>{ti}</h3><p class="ax-pp">{pl}</p></div><div class="ax-pd"><p>{tx}</p>{x}</div></div></article>'
                    for i, (t, e, w, ti, pl, tx, x) in enumerate(EVENTS))
    how = ''.join(f'<article class="ax-hc{" g" if i % 2 else ""}" style="--i:{i};--r:{[-6, 4, -3, 7, -5][i % 5]}deg;--r2:{[14, -18, 10, -12, 16][i % 5]}deg;--dy:{[0, 26, 8, 34, 14][i % 5]}px"><h3>{t}</h3><p class="ax-ht">{d}</p><p class="ax-hn">{i + 1:02d}.</p></article>' for i, (t, d) in enumerate(HOW))
    qa = qa_html()
    TD = [('Figma', ['figma'], ''),
          ('Claude Design', ['claude-icon'], ''),
          ('Claude Code', ['claude-code'], ''),
          ('Jira', ['jira'], ''),
          ('Confluence', ['confluence'], ''),
          ('Webflow', ['webflow'], ''),
          ('Miro', ['miro-icon'], ''),
          ('Notion', ['notion-icon'], ''),
          ('Fullstory', ['fullstory.png'], ''),
          ('Adobe', ['adobe-illustrator', 'adobe-photoshop', 'adobe-indesign'], '')]
    card = lambda t, ics, d: ('<li class="tlc"><span class="tlc-i">' + ''.join(f'<img src="{GH}logos/tc/{f if '.' in f else f + '.svg'}" width="22" height="22" alt="" loading="lazy">' for f in ics)
                              + f'</span><b>{t}</b>' + (f'<p>{d}</p>' if d else '') + '</li>')
    row = ''.join(card(*x) for x in TD)
    tools = f'<div class="tlc-m" data-tcm><ul class="tlc-r">{row}</ul><ul class="tlc-r" aria-hidden="true">{row}</ul></div>'
    me = f'<img class="ax-d" src="{GH}me/ege-drawn.webp" width="900" height="900" alt="A drawing of Ege Coskun"><img class="ax-p" src="{GH}me/ege-photo.webp" width="900" height="900" alt="" aria-hidden="true" loading="lazy">'
    txt = f'<h1>Hi, I’m <span class="ax-nm" tabindex="0">Ege<span class="ax-say" role="tooltip">[eh-GEH]</span></span>.</h1><div class="ax-tx">{lead}</div>'
    nm = '<h1>Hi, I’m <span class="ax-nm" tabindex="0">Ege<span class="ax-say" role="tooltip">[eh-GEH]</span></span>.</h1>'
    if intro == 'a':
        rows = ''.join(f'<div><dt>{t}</dt><dd>{d}</dd></div>' for t, d in ROWS if True)
        intro_html = (f'<section class="ax-w ax-ia"><div class="ax-l"><figure class="ax-fr"><img src="{GH}me/ege-portrait.webp?v=1" width="900" height="995" alt="Ege Coskun"><svg class="fr-l" viewBox="-16 -16 302 330" aria-hidden="true" fill="none" stroke="#D492EC" stroke-linecap="round" stroke-linejoin="round"><path d="M-10.5 -9.2 L49.2 -10.1 L105.0 -8.7 L165.2 -9.9 L221.4 -11.2 L276.8 -10.6 L279.4 41.1 L280.3 94.8 L277.8 147.0 L281.2 203.1 L280.7 255.5 L276.9 307.2 L221.4 306.3 L165.8 307.4 L104.7 309.4 L46.9 309.9 L-9.2 308.2 L-9.7 254.9 L-10.4 200.0 L-7.4 147.8 L-7.8 94.7 L-6.9 44.7 Z" stroke-width="1.5"/></svg></figure><div class="ax-nmw">{nm} <p class="ax-sub">People tell me what they want.<br>I like to design what they meant.</p></div></div>'
                      f'<div class="ax-r"><div class="ax-tx">{lead}</div></div><dl class="ax-rows">{rows}</dl></section>')
    elif intro == 'b':
        rows = ''.join(f'<div><dt>{t}</dt><dd>{d}</dd></div>' for t, d in ROWS)
        intro_html = (f'<section class="ax-w ax-ib"><div>{nm}<p class="ax-lead">I’ve spent every role designing for people who know their domain far better than I do: customs officers, marketers, streaming editors.</p><dl class="ax-rows">{rows}</dl></div>'
                      f'<figure class="ax-ph"><img src="{GH}me/ege-print.webp" width="480" height="600" alt="Ege Coskun"></figure></section>')
    elif intro == 'swing':
        rope = ('<svg class="ax-rope" viewBox="0 0 270 320" aria-hidden="true"><path d="M232 -10C222 60 150 92 96 104C40 116 24 170 40 226C52 268 64 296 72 318"/>'
                '<path d="M250 -10C236 70 170 104 118 98C58 90 30 140 34 200C38 256 58 292 66 318"/><path d="M98 300c-6 4-6 14 0 20" style="stroke-width:2.2"/></svg>')
        intro_html = (f'{SIGN}<section class="ax-w ax-intro ax-c sw"><div class="ax-hang" aria-hidden="true"><div class="ax-sw">{rope}'
                      f'<div class="ax-card"><i class="ax-slot"></i><div class="ax-cp"><img src="{GH}me/ege-badge.webp" width="480" height="480" alt=""></div>'
                      f'<span class="ax-sg ax-cr">Product designer</span><span class="ax-sg ax-cn">ege</span></div></div></div><div class="ax-ct">{txt}</div></section>')
    elif intro == 'dock':
        intro_html = (f'{SIGN}<section class="ax-w ax-intro ax-c"><div class="ax-ct">{txt}</div>'
                      f'<figure class="ax-print"><i class="ax-rv"></i><i class="ax-rv"></i><i class="ax-rv"></i><i class="ax-rv"></i><img src="{GH}me/ege-print.webp" width="480" height="600" alt="Ege Coskun"><span class="ax-sg" aria-hidden="true">Ege Coskun</span></figure></section>')
    else:
        intro_html = f'<section class="ax-w ax-intro"><div>{txt}</div><figure class="ax-me"><div class="ax-fl">{me}</div></figure></section>'
    xcss = {'swing': CENTER_CSS + SWING_CSS, 'dock': CENTER_CSS + DOCK_CSS, 'a': DARK_CSS, 'b': DARK_CSS}.get(intro, '')
    xjs = ''
    dk = ' dk' if intro in ('a', 'b') else ''
    return f"""<main class="ab abx{dk}">
{intro_html}
<div class="ax-dark">
<section class="ax-how" style="--n:{len(HOW)}" data-axhow><div class="ax-hpin"><h2 class="ax-w">How I work</h2><div class="ax-hcs">{how}</div></div></section>
<section class="ax-w ax-tl tl2"><h2>Tools</h2>{tools}</section>
</div>
<section class="ax-path" style="--n:{n}" data-axpath><div class="ax-pin"><h2 class="ax-w">Education and Experience</h2>
<div class="ax-st"><div class="ax-hl"><i class="ax-ln" aria-hidden="true"></i><i class="ax-sg" aria-hidden="true"></i>{dots}</div><div class="ax-win" aria-hidden="true"><div class="ax-rl">{ticks}</div></div><i class="ax-now" aria-hidden="true"></i><i class="ax-end" aria-hidden="true"></i><div class="ax-pcs">{cards}</div></div></div></section></main>
<style>
/* type scale: h1 56, section titles 26, item titles 36, h3 24, body 16 (18 on very large screens) */
.abx{{--fs:16px;--h1:clamp(40px,3.4vw,56px);--h2:clamp(20px,1.3vw,26px);--h2b:clamp(26px,1.9vw,36px);--h3:clamp(20px,1.3vw,24px);--px:clamp(20px,2.4vw,44px);--dk:#161616;font-family:"Inter Tight",system-ui,sans-serif}}
@media(min-width:2200px){{.abx{{--fs:18px}}}}
.abx *{{font-family:inherit}}
.ax-w{{padding-left:var(--px);padding-right:var(--px)}}
.abx h1{{margin:0 0 24px;font-size:var(--h1);line-height:1;letter-spacing:-.035em;font-weight:600}}
.abx h2{{margin:0;font-size:var(--h2);line-height:1.1;letter-spacing:-.025em;font-weight:600}}
.abx h3{{margin:0;font-size:var(--h3);line-height:1.2;letter-spacing:-.015em;font-weight:600}}
.abx p{{font-size:var(--fs);line-height:1.55}}
.ax-intro{{display:grid;grid-template-columns:minmax(0,1.3fr) minmax(0,1fr);gap:clamp(32px,5vw,96px);align-items:center;padding-top:clamp(40px,5vw,88px);padding-bottom:clamp(64px,7vw,120px)}}
.ax-tx{{max-width:40em}}.ax-tx p{{margin:0 0 .9em;color:#2b2a28}}
.ax-me{{position:relative;margin:0;justify-self:end;width:min(100%,480px);aspect-ratio:1;perspective:1400px}}
.ax-fl{{position:absolute;inset:0;transform-style:preserve-3d;transition:transform .9s var(--ease)}}.ax-me:hover .ax-fl{{transform:rotateY(180deg)}}
.ax-me img{{position:absolute;inset:0;width:100%;height:100%;object-fit:cover;border-radius:50%;backface-visibility:hidden;-webkit-backface-visibility:hidden;background:#F1E4CC}}
.ax-p{{transform:rotateY(180deg)}}
/* experience: a short ruler slides under a fixed line, past to present; only the date beside the line changes */
.ax-path{{--ph:min(calc(100svh - 4.75rem),500px);--tl:84px;height:calc(var(--n) * 45svh + var(--ph));border-top:1px solid var(--line)}}
.ax-pin{{position:sticky;top:max(4.75rem,calc(50svh - var(--ph) / 2 + 2.4rem));height:var(--ph);display:flex;flex-direction:column;padding-top:clamp(28px,3vw,48px);box-sizing:border-box;overflow:hidden}}
.ax-st{{--yh:12svh;position:relative;flex:1}}
.ax-win{{position:absolute;left:var(--px);top:0;bottom:0;width:60px;overflow:hidden;-webkit-mask-image:linear-gradient(transparent,#000 25%,#000 75%,transparent);mask-image:linear-gradient(transparent,#000 25%,#000 75%,transparent)}}
.ax-rl{{position:absolute;left:0;top:var(--tl);width:60px;transition:transform .7s var(--ease)}}
.ax-tq{{position:absolute;left:20px;top:calc(var(--o) * var(--yh));width:14px;border-top:1px solid #C9C8C3}}
.ax-tq.y{{left:8px;width:26px;border-color:#8E8D88}}
.ax-side{{margin-top:18px;padding:14px 16px;border-left:3px solid var(--g);background:#EEEEEB;border-radius:0 10px 10px 0}}.ax-side p{{margin:0 0 .3em}}.ax-sk{{font-size:13px!important;color:var(--g)!important;font-weight:600}}.ax-sh{{font-weight:600}}
.ax-now,.ax-end{{position:absolute;left:0;right:0;top:var(--tl);height:1px;background:var(--g)}}.ax-end{{top:calc(var(--tl) + var(--ch,220px) + 28px);background:var(--ink);opacity:.25;transition:top .5s var(--ease)}}
.ax-now:before{{content:"";position:absolute;left:calc(var(--px) - 2px);top:-5px;border:5px solid transparent;border-left:7px solid var(--g)}}
.ax-pcs{{position:absolute;left:calc(var(--px) + 120px);right:var(--px);top:var(--tl)}}
.ax-pc{{position:absolute;left:0;right:0;top:0;opacity:0;transition:opacity .35s;pointer-events:none}}
.ax-pc.on{{opacity:1;pointer-events:auto}}
.ax-when{{position:absolute;bottom:calc(100% + 10px);left:0;margin:0;font-size:14px!important;font-weight:600;color:var(--g)!important;font-variant-numeric:tabular-nums}}
.ax-pg2{{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1fr);gap:clamp(24px,4vw,80px);padding-top:24px;transform:translateY(12px);transition:transform .5s var(--ease)}}
.ax-pc.on .ax-pg2{{transform:none}}
.ax-pc h3{{font-size:var(--h2b);letter-spacing:-.025em}}
.ax-pd{{max-width:30em}}.ax-pd p{{margin:0 0 .4em;color:#2b2a28}}.ax-pp{{font-weight:600}}
/* experience: every stop stays on the page, stacked; the line lights up only along the one in view */
.ax-path{{height:auto;margin-bottom:clamp(48px,6vw,96px)}}
.ax-pin{{position:static;height:auto;overflow:visible;display:block;padding-bottom:clamp(8px,2vw,32px)}}
.ax-st{{flex:none}}
.ax-hl,.ax-win,.ax-now,.ax-end{{display:none!important}}
.ax-pcs{{position:relative;left:auto;right:auto;top:auto;bottom:auto;padding:clamp(28px,3vw,48px) var(--px) 0}}
.ax-pc{{position:relative;left:auto;right:auto;top:auto;bottom:auto;opacity:1;pointer-events:auto;display:grid;grid-template-columns:clamp(110px,11vw,190px) minmax(0,1fr);gap:clamp(20px,3vw,56px);padding:0 0 clamp(40px,5vw,72px) clamp(28px,3vw,44px)}}
.ax-pc:before{{content:"";position:absolute;left:0;top:.7em;bottom:-.7em;width:1px;background:#3a3a37;transition:background .4s,width .4s,left .4s}}
.ax-pc:last-child:before{{display:none}}
.ax-pc:after{{content:"";position:absolute;left:-5px;top:.45em;width:11px;height:11px;border-radius:50%;background:#55544f;transition:background .4s,transform .4s var(--ease)}}
.ax-pc.on:before{{left:-1px;width:3px;border-radius:3px;background:#D492EC}}
.ax-pc.on:after{{background:#D492EC;transform:scale(1.3)}}
.ax-when{{position:static!important;margin:0!important;padding-top:.2em;font-size:14px!important;font-weight:600;color:var(--mute)!important;transition:color .4s}}
.ax-pc.on .ax-when{{color:#D492EC!important}}
.ax-pg2{{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.15fr);gap:clamp(20px,3vw,56px);align-items:start;padding:0;transform:none}}.ax-ti h3{{margin:0 0 .35em}}.ax-ti .ax-pp{{margin:0;color:var(--mute)}}.ax-pd p:first-child{{margin-top:.15em}}
.ax-pc h3{{position:static;margin:0 0 .5em;font-size:22px;letter-spacing:-.015em;transform:none;transition:color .4s}}
.ax-pc.edu,.ax-pc.edu h3,.ax-pc.edu .ax-pd p,.ax-pc.edu .ax-pp,.ax-pc.edu .ax-when{{color:#D492EC!important}}.ax-pc.edu:after{{background:#D492EC}}.ax-pc.on .ax-when{{color:#F2F2EF!important}}.ax-pc.edu.on .ax-when{{color:#D492EC!important}}
.ax-ia .ax-nmw h1,.ax-ia .ax-nmw .ax-nm{{color:#D492EC!important;font-size:clamp(18px,1.4vw,24px);font-weight:600;letter-spacing:-.015em;line-height:1.3}}.ax-ia .ax-nm{{text-decoration-color:rgba(212,146,236,.45)}}
.ax-pd{{max-width:none}}
.ax-side{{border-left-color:#D492EC}}.ax-sk{{color:#D492EC!important}}
@media(max-width:899px){{.ax-pc{{grid-template-columns:1fr;gap:6px}}.ax-pg2{{grid-template-columns:1fr;gap:10px}}}}
.ab-aw{{position:relative;color:inherit;text-decoration:underline;text-decoration-thickness:1px;text-underline-offset:3px}}
.ab-aw:hover{{text-decoration-color:var(--ink)}}
.ab-pv{{position:absolute;left:50%;bottom:calc(100% + 12px);z-index:20;width:300px;display:flex;flex-direction:column;gap:8px;padding:14px;border-radius:12px;background:#fff;border:1px solid var(--line);box-shadow:0 18px 50px rgba(0,0,0,.16);font-size:13px;line-height:1.45;color:#3a3936;text-align:left;
  opacity:0;pointer-events:none;transform:translate(-50%,6px) rotate(-1.5deg);transition:opacity .25s,transform .45s var(--ease)}}
.ab-aw:hover .ab-pv,.ab-aw:focus-visible .ab-pv{{opacity:1;transform:translate(-50%,0) rotate(-1.5deg)}}
.ab-pv-h{{display:grid;grid-template-columns:32px 1fr;column-gap:10px;align-items:center}}
.ab-pv-h i{{grid-row:span 2;width:32px;height:32px;border-radius:6px;background:#161616;color:#fff;font:600 11px/32px "Inter Tight",sans-serif;font-style:normal;text-align:center}}
.ab-pv-h b{{font-size:13px;color:var(--ink);font-weight:600}}.ab-pv-h em{{font-style:normal;font-size:11px;color:var(--mute)}}
.ab-pv-t{{display:block}}.ab-pv-f{{display:block;font-size:12px;font-weight:600;color:#0A66C2}}
.ab-pv img{{display:block;width:100%;border-radius:8px}}
@media(hover:none),(max-width:767px){{.ab-pv{{display:none}}}}
/* dark from here on */
.ax-dark{{background:var(--dk);color:#F2F2EF}}
.ax-dark p{{color:#CFCECA}}
.ax-how{{height:calc(var(--n) * 45svh + 60svh)}}
.ax-hpin{{position:sticky;top:4.75rem;height:calc(100svh - 4.75rem);overflow:hidden;padding-top:clamp(20px,2.4vw,40px);box-sizing:border-box}}
.ax-hcs{{position:absolute;left:var(--px);right:var(--px);top:clamp(100px,14svh,150px);bottom:clamp(16px,3svh,40px)}}
.ax-hc{{--w:min(25vw,400px);position:absolute;top:var(--dy,0px);left:calc(var(--i) * (100% - var(--w)) / (var(--n) - 1));width:var(--w);height:min(calc(100% - 48px),520px);box-sizing:border-box;display:flex;flex-direction:column;padding:clamp(20px,1.8vw,32px);background:#161616;color:#F2F2EF;border:1.5px solid #D492EC;border-radius:18px;
  transform:translateY(calc((1 - var(--e,0)) * 130%)) rotate(calc(var(--r) + (1 - var(--e,0)) * var(--r2)));opacity:min(1,calc(var(--e,0) * 4))}}
.ax-hc h3{{font-size:clamp(20px,1.5vw,26px);line-height:.98;letter-spacing:-.03em;font-weight:800;text-transform:uppercase;text-wrap:balance}}
.ax-hc .ax-ht{{margin:16px 0 0;font-size:15px!important;line-height:1.5!important;color:#CFCECA!important}}
.ax-hc .ax-hn{{margin:auto 0 0!important;font-size:clamp(48px,4.4vw,80px)!important;line-height:.9!important;font-weight:800;letter-spacing:-.05em;color:rgba(255,255,255,.14)!important}}
.ax-tl{{display:grid;grid-template-columns:minmax(0,1fr) minmax(0,1.6fr);gap:clamp(32px,5vw,96px);padding-top:clamp(32px,4vw,64px);padding-bottom:clamp(64px,7vw,120px);border-top:1px solid rgba(255,255,255,.14)}}
.ax-tools{{list-style:none;margin:0;padding:0;display:flex;flex-wrap:wrap;gap:8px;align-content:start}}
.ax-tools li{{display:inline-flex;align-items:center;gap:8px;padding:9px 14px 9px 10px;border-radius:99px;background:#262624;font-size:14px;font-weight:500}}
.ax-tools img{{width:18px;height:18px;object-fit:contain}}
@media(max-width:899px){{.ax-intro,.ax-ask,.ax-tl{{grid-template-columns:1fr}}.ax-me{{justify-self:start;width:min(70vw,320px)}}.ax-ask h2{{position:static}}
.ax-path,.ax-how{{height:auto}}.ax-pin,.ax-hpin{{position:static;height:auto;overflow:visible}}.ax-win,.ax-now,.ax-end,.ax-hl{{display:none}}
.ax-st{{flex:none}}.ax-pcs{{position:static;padding:24px var(--px) 24px}}.ax-pc{{position:relative;opacity:1;margin-bottom:0}}.ax-when{{position:static;margin-bottom:6px}}.ax-pg2{{display:block;padding-top:0;transform:none}}.ax-pc h3{{margin-bottom:10px}}
.ax-hcs{{position:static;display:grid;gap:12px;padding:24px var(--px) 48px}}.ax-hc{{position:static;width:auto;height:auto;transform:none;opacity:1;--w:auto}}.ax-hc .ax-hn{{margin-top:20px!important}}}}
@media (prefers-reduced-motion:reduce){{.ax-path,.ax-how{{height:auto}}.ax-pin,.ax-hpin{{position:static;height:auto;overflow:visible}}.ax-win,.ax-now,.ax-end,.ax-hl{{display:none}}.ax-pcs{{position:static}}.ax-pc{{position:relative;opacity:1;margin-bottom:0}}.ax-when{{position:static}}.ax-pg2{{transform:none}}.ax-hcs{{position:static;display:grid;gap:12px}}.ax-hc{{position:static;width:auto;height:auto;transform:none;opacity:1}}}}
.ax-chip{{display:block;width:max-content;margin-top:8px;padding:2px 10px;border-radius:99px;background:rgba(212,146,236,.14);color:#D492EC;font-size:12px;font-weight:600;line-height:1.55;letter-spacing:0}}
.ax-side.ax-rv{{clip-path:inset(0 calc(100% - 3px) 0 0);transition:clip-path 1s cubic-bezier(.2,.8,.2,1)}}.ax-side.ax-rv>*{{opacity:0;transition:opacity .5s ease .4s}}.ax-side.ax-rv.in{{clip-path:inset(0 0 0 0)}}.ax-side.ax-rv.in>*{{opacity:1}}
.tlc-m{{cursor:grab;touch-action:pan-y;-webkit-user-select:none;user-select:none}}.tlc-m.dr{{cursor:grabbing}}.tlc img{{pointer-events:none;-webkit-user-drag:none}}
{QCSS}{xcss}{NMCSS}.tlc-i img[src$='.png']{{border-radius:5px}}.tl2>h2{{margin-bottom:clamp(28px,2.6vw,40px)!important}}.ax-ask .wk-qk{{position:sticky;top:calc(4.75rem + 24px);align-self:start}}.abx.dk .ax-qc a{{color:#F2F2EF}}.ax-when{{bottom:calc(100% + 8px)!important;left:calc(-120px + 22px)!important;font-weight:500!important;line-height:1.2}}</style>
<script>
(function(){{
var P=document.querySelector('[data-axpath]'),pc=[].slice.call(P.querySelectorAll('.ax-pc'));
var H=document.querySelector('[data-axhow]'),hc=[].slice.call(H.querySelectorAll('.ax-hc')),R=matchMedia('(prefers-reduced-motion:reduce)').matches;
function run(s){{return s.offsetHeight-s.querySelector('.ax-hpin').offsetHeight}}
var raf=0,cur=-2;
function draw(){{raf=0;
  /* experience: all entries stay in view, the line lights up only along the one nearest the middle of the screen */
  var pr=P.getBoundingClientRect(),k=-1;
  if(pr.top<innerHeight&&pr.bottom>0){{var mid=innerHeight*.5,bd=1e9;pc.forEach(function(c,i){{var r=c.getBoundingClientRect(),d=(r.top<=mid&&r.bottom>=mid)?0:Math.min(Math.abs(r.top-mid),Math.abs(r.bottom-mid));if(d<bd){{bd=d;k=i}}}})}}
  if(k!==cur){{cur=k;pc.forEach(function(c,i){{c.classList.toggle('on',i===k)}})}}
  if(innerWidth<900||R)return;
  var hr=H.getBoundingClientRect(),hv=innerHeight*.5,q=Math.max(0,(hv-hr.top)/(hv+run(H)))*(hc.length+.3);hc.forEach(function(c,i){{c.style.setProperty('--e',Math.max(0,Math.min(1,q-i)).toFixed(3))}})}}
addEventListener('scroll',function(){{if(!raf)raf=requestAnimationFrame(draw)}},{{passive:true}});addEventListener('resize',function(){{cur=-2;draw()}});draw()}})();
/* UwaVerde card wipes out from its left stroke when it comes into view */
(function(){{var e=document.querySelector('.ax-side');if(!e||matchMedia('(prefers-reduced-motion:reduce)').matches||!('IntersectionObserver' in window))return;e.classList.add('ax-rv');var io=new IntersectionObserver(function(l){{l.forEach(function(x){{if(x.isIntersecting){{e.classList.add('in');io.disconnect()}}}})}},{{rootMargin:'0px 0px -22% 0px',threshold:0}});io.observe(e)}})();
/* tools drift on their own and can be dragged either way */
(function(){{var m=document.querySelector('[data-tcm]');if(!m||matchMedia('(prefers-reduced-motion:reduce)').matches)return;var rs=[].slice.call(m.querySelectorAll('.tlc-r'));if(rs.length<2)return;rs.forEach(function(r){{r.style.animation='none'}});
var x=0,w=0,dn=false,hv=false,sx=0,x0=0,t0=performance.now();
function meas(){{w=rs[0].offsetWidth+(parseFloat(getComputedStyle(m).columnGap)||12)}}
function wrap(){{if(w){{x=((x%w)-w)%w}}}}
function set(){{rs.forEach(function(r){{r.style.transform='translateX('+x+'px)'}})}}
function tick(t){{var dt=Math.min(64,t-t0);t0=t;if(!dn&&!hv){{x-=w/60000*dt}}wrap();set();requestAnimationFrame(tick)}}
m.addEventListener('pointerdown',function(e){{if(e.button)return;dn=true;sx=e.clientX;x0=x;m.classList.add('dr');try{{m.setPointerCapture(e.pointerId)}}catch(_){{}}}});
m.addEventListener('pointermove',function(e){{if(dn){{x=x0+(e.clientX-sx);wrap();set()}}}});
function up(){{dn=false;m.classList.remove('dr')}}
m.addEventListener('pointerup',up);m.addEventListener('pointercancel',up);
m.addEventListener('mouseenter',function(){{hv=true}});m.addEventListener('mouseleave',function(){{hv=false}});
addEventListener('resize',meas);meas();requestAnimationFrame(tick)}})();
</script>{xjs}{QJS}"""
