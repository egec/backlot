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
AB_LEAD = ('I design the parts of B2B software where a wrong click costs something: approvals, data that other teams depend on, decisions that are hard to undo.',
           'At MilSOFT I designed customs declarations and naval radar displays, and at UwaVerde I built the design function from nothing. Each time the domain was new to me, and learning it properly before designing for it is still the part I enjoy most.')


HOW = [('Learn the domain first', 'Customs declarations, naval radar displays, data tools, a prenatal monitoring wearable. Each time, I learned how the work is really done, and by whom, before I started designing.'),
       ('Design for the unhappy path', 'Most products work when everything goes right. I spend more of my time on the other cases: the action that fails, the data that is missing, the step someone skips. That is where people decide whether they can trust a tool.'),
       ('A reason for every decision', 'If I cannot say why something sits where it does, it moves or goes. Hierarchy, colour and wording all need a reason I could defend in a review.'),
       ('User needs and business goals', 'A design is done when it works for the person using it and for the business paying for it. I keep both in the room, and when they pull in different directions, I make the trade-off visible instead of hiding it.')]
TOOLS = [('Figma', '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="#F24E1E" d="M15.852 8.981h-4.588V0h4.588c2.476 0 4.49 2.014 4.49 4.49s-2.014 4.491-4.49 4.491zM12.735 7.51h3.117c1.665 0 3.019-1.355 3.019-3.019s-1.355-3.019-3.019-3.019h-3.117V7.51zm0 1.471H8.148c-2.476 0-4.49-2.014-4.49-4.49S5.672 0 8.148 0h4.588v8.981zm-4.587-7.51c-1.665 0-3.019 1.355-3.019 3.019s1.354 3.02 3.019 3.02h3.117V1.471H8.148zm4.587 15.019H8.148c-2.476 0-4.49-2.014-4.49-4.49s2.014-4.49 4.49-4.49h4.588v8.98zM8.148 8.981c-1.665 0-3.019 1.355-3.019 3.019s1.355 3.019 3.019 3.019h3.117V8.981H8.148zM8.172 24c-2.489 0-4.515-2.014-4.515-4.49s2.014-4.49 4.49-4.49h4.588v4.441c0 2.503-2.047 4.539-4.563 4.539zm-.024-7.51a3.023 3.023 0 0 0-3.019 3.019c0 1.665 1.365 3.019 3.044 3.019 1.705 0 3.093-1.376 3.093-3.068v-2.97H8.148zm7.704 0h-.098c-2.476 0-4.49-2.014-4.49-4.49s2.014-4.49 4.49-4.49h.098c2.476 0 4.49 2.014 4.49 4.49s-2.014 4.49-4.49 4.49zm-.097-7.509c-1.665 0-3.019 1.355-3.019 3.019s1.355 3.019 3.019 3.019h.098c1.665 0 3.019-1.355 3.019-3.019s-1.355-3.019-3.019-3.019h-.098z"/></svg>'), ('Claude Code', '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="#D97757" d="m4.7144 15.9555 4.7174-2.6471.079-.2307-.079-.1275h-.2307l-.7893-.0486-2.6956-.0729-2.3375-.0971-2.2646-.1214-.5707-.1215-.5343-.7042.0546-.3522.4797-.3218.686.0608 1.5179.1032 2.2767.1578 1.6514.0972 2.4468.255h.3886l.0546-.1579-.1336-.0971-.1032-.0972L6.973 9.8356l-2.55-1.6879-1.3356-.9714-.7225-.4918-.3643-.4614-.1578-1.0078.6557-.7225.8803.0607.2246.0607.8925.686 1.9064 1.4754 2.4893 1.8336.3643.3035.1457-.1032.0182-.0728-.164-.2733-1.3539-2.4467-1.445-2.4893-.6435-1.032-.17-.6194c-.0607-.255-.1032-.4674-.1032-.7285L6.287.1335 6.6997 0l.9957.1336.419.3642.6192 1.4147 1.0018 2.2282 1.5543 3.0296.4553.8985.2429.8318.091.255h.1579v-.1457l.1275-1.706.2368-2.0947.2307-2.6957.0789-.7589.3764-.9107.7468-.4918.5828.2793.4797.686-.0668.4433-.2853 1.8517-.5586 2.9021-.3643 1.9429h.2125l.2429-.2429.9835-1.3053 1.6514-2.0643.7286-.8196.85-.9046.5464-.4311h1.0321l.759 1.1293-.34 1.1657-1.0625 1.3478-.8804 1.1414-1.2628 1.7-.7893 1.36.0729.1093.1882-.0183 2.8535-.607 1.5421-.2794 1.8396-.3157.8318.3886.091.3946-.3278.8075-1.967.4857-2.3072.4614-3.4364.8136-.0425.0304.0486.0607 1.5482.1457.6618.0364h1.621l3.0175.2247.7892.522.4736.6376-.079.4857-1.2142.6193-1.6393-.3886-3.825-.9107-1.3113-.3279h-.1822v.1093l1.0929 1.0686 2.0035 1.8092 2.5075 2.3314.1275.5768-.3218.4554-.34-.0486-2.2039-1.6575-.85-.7468-1.9246-1.621h-.1275v.17l.4432.6496 2.3436 3.5214.1214 1.0807-.17.3521-.6071.2125-.6679-.1214-1.3721-1.9246L14.38 17.959l-1.1414-1.9428-.1397.079-.674 7.2552-.3156.3703-.7286.2793-.6071-.4614-.3218-.7468.3218-1.4753.3886-1.9246.3157-1.53.2853-1.9004.17-.6314-.0121-.0425-.1397.0182-1.4328 1.9672-2.1796 2.9446-1.7243 1.8456-.4128.164-.7164-.3704.0667-.6618.4008-.5889 2.386-3.0357 1.4389-1.882.929-1.0868-.0062-.1579h-.0546l-6.3385 4.1164-1.1293.1457-.4857-.4554.0608-.7467.2307-.2429 1.9064-1.3114Z"/></svg>'), ('Storybook', '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="#FF4785" d="M16.71.243l-.12 2.71a.18.18 0 00.29.15l1.06-.8.9.7a.18.18 0 00.28-.14l-.1-2.76 1.33-.1a1.2 1.2 0 011.279 1.2v21.596a1.2 1.2 0 01-1.26 1.2l-16.096-.72a1.2 1.2 0 01-1.15-1.16l-.75-19.797a1.2 1.2 0 011.13-1.27L16.7.222zM13.64 9.3c0 .47 3.16.24 3.59-.08 0-3.2-1.72-4.89-4.859-4.89-3.15 0-4.899 1.72-4.899 4.29 0 4.45 5.999 4.53 5.999 6.959 0 .7-.32 1.1-1.05 1.1-.96 0-1.35-.49-1.3-2.16 0-.36-3.649-.48-3.769 0-.27 4.03 2.23 5.2 5.099 5.2 2.79 0 4.969-1.49 4.969-4.18 0-4.77-6.099-4.64-6.099-6.999 0-.97.72-1.1 1.13-1.1.45 0 1.25.07 1.19 1.87z"/></svg>'), ('Jira', '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="#0052CC" d="M11.571 11.513H0a5.218 5.218 0 0 0 5.232 5.215h2.13v2.057A5.215 5.215 0 0 0 12.575 24V12.518a1.005 1.005 0 0 0-1.005-1.005zm5.723-5.756H5.736a5.215 5.215 0 0 0 5.215 5.214h2.129v2.058a5.218 5.218 0 0 0 5.215 5.214V6.758a1.001 1.001 0 0 0-1.001-1.001zM23.013 0H11.455a5.215 5.215 0 0 0 5.215 5.215h2.129v2.057A5.215 5.215 0 0 0 24 12.483V1.005A1.001 1.001 0 0 0 23.013 0Z"/></svg>'), ('Confluence', '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="#172B4D" d="M.87 18.257c-.248.382-.53.875-.763 1.245a.764.764 0 0 0 .255 1.04l4.965 3.054a.764.764 0 0 0 1.058-.26c.199-.332.454-.763.733-1.221 1.967-3.247 3.945-2.853 7.508-1.146l4.957 2.337a.764.764 0 0 0 1.028-.382l2.364-5.346a.764.764 0 0 0-.382-1 599.851 599.851 0 0 1-4.965-2.361C10.911 10.97 5.224 11.185.87 18.257zM23.131 5.743c.249-.405.531-.875.764-1.25a.764.764 0 0 0-.256-1.034L18.675.404a.764.764 0 0 0-1.058.26c-.195.335-.451.763-.734 1.225-1.966 3.246-3.945 2.85-7.508 1.146L4.437.694a.764.764 0 0 0-1.027.382L1.046 6.422a.764.764 0 0 0 .382 1c1.039.49 3.105 1.467 4.965 2.361 6.698 3.246 12.392 3.029 16.738-4.04z"/></svg>'), ('Webflow', '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="#146EF5" d="m24 4.515-7.658 14.97H9.149l3.205-6.204h-.144C9.566 16.713 5.621 18.973 0 19.485v-6.118s3.596-.213 5.71-2.435H0V4.515h6.417v5.278l.144-.001 2.622-5.277h4.854v5.244h.144l2.72-5.244H24Z"/></svg>'), ('Miro', '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="#050038" d="M17.392 0H13.9L17 4.808 10.444 0H6.949l3.102 6.3L3.494 0H0l3.05 8.131L0 24h3.494L10.05 6.985 6.949 24h3.494L17 5.494 13.899 24h3.493L24 3.672 17.392 0z"/></svg>'), ('Notion', '<svg viewBox="0 0 24 24" aria-hidden="true"><path fill="#000000" d="M4.459 4.208c.746.606 1.026.56 2.428.466l13.215-.793c.28 0 .047-.28-.046-.326L17.86 1.968c-.42-.326-.981-.7-2.055-.607L3.01 2.295c-.466.046-.56.28-.374.466zm.793 3.08v13.904c0 .747.373 1.027 1.214.98l14.523-.84c.841-.046.935-.56.935-1.167V6.354c0-.606-.233-.933-.748-.887l-15.177.887c-.56.047-.747.327-.747.933zm14.337.745c.093.42 0 .84-.42.888l-.7.14v10.264c-.608.327-1.168.514-1.635.514-.748 0-.935-.234-1.495-.933l-4.577-7.186v6.952L12.21 19s0 .84-1.168.84l-3.222.186c-.093-.186 0-.653.327-.746l.84-.233V9.854L7.822 9.76c-.094-.42.14-1.026.793-1.073l3.456-.233 4.764 7.279v-6.44l-1.215-.139c-.093-.514.28-.887.747-.933zM1.936 1.035l13.31-.98c1.634-.14 2.055-.047 3.082.7l4.249 2.986c.7.513.934.653.934 1.213v16.378c0 1.026-.373 1.634-1.68 1.726l-15.458.934c-.98.047-1.448-.093-1.962-.747l-3.129-4.06c-.56-.747-.793-1.306-.793-1.96V2.667c0-.839.374-1.54 1.447-1.632z"/></svg>'), ('Illustrator', '<svg viewBox="0 0 24 24" aria-hidden="true"><rect width="24" height="24" rx="5" fill="#300"/><text x="12" y="16.2" text-anchor="middle" font-family="Inter Tight,Arial,sans-serif" font-size="11" font-weight="700" fill="#FF9A00">Ai</text></svg>'), ('Photoshop', '<svg viewBox="0 0 24 24" aria-hidden="true"><rect width="24" height="24" rx="5" fill="#001E36"/><text x="12" y="16.2" text-anchor="middle" font-family="Inter Tight,Arial,sans-serif" font-size="11" font-weight="700" fill="#31A8FF">Ps</text></svg>'), ('InDesign', '<svg viewBox="0 0 24 24" aria-hidden="true"><rect width="24" height="24" rx="5" fill="#49021F"/><text x="12" y="16.2" text-anchor="middle" font-family="Inter Tight,Arial,sans-serif" font-size="11" font-weight="700" fill="#FF3366">Id</text></svg>')]

def more():
    how = ''.join(f'<li><em>{i:02d}</em><h3>{t}</h3><p>{d}</p></li>' for i, (t, d) in enumerate(HOW, 1))
    tools = ''.join(f'<li>{svg}<span>{t}</span></li>' for t, svg in TOOLS)
    return (f'<section class="cs-wrap ab-more"><div class="ab-row"><p class="k">Tools</p><ul class="ab-tools">{tools}</ul></div>'
            f'<div class="ab-row"><p class="k">How I work</p><ol class="ab-how">{how}</ol></div></section>'
            '''<style>
.ab-more{padding-bottom:clamp(72px,8vw,140px)}
.ab-row{display:grid;grid-template-columns:calc(33.33% - 16px) minmax(0,1fr);gap:16px;padding-top:24px;margin-top:clamp(48px,5vw,88px);border-top:1px solid var(--line)}
.ab-tools{list-style:none;margin:0;padding:0;display:grid;grid-template-columns:repeat(auto-fill,minmax(150px,1fr));gap:10px}
.ab-tools li{display:flex;align-items:center;gap:10px;padding:12px 14px;border:1px solid var(--line);border-radius:12px;background:var(--card2,#FAF9F7);font-size:14px;font-weight:500;transition:transform .3s var(--ease),border-color .2s}
.ab-tools li:hover{transform:translateY(-2px);border-color:#B9B6AE}
.ab-tools svg{width:22px;height:22px;flex:none}
.ab-how{list-style:none;margin:0;padding:0}
.ab-how li{display:grid;grid-template-columns:48px minmax(0,1fr) minmax(0,1.4fr);gap:16px;padding:22px 0;border-bottom:1px solid var(--line)}
.ab-how li:first-child{padding-top:0}
.ab-how em{font-style:normal;font-size:13px;line-height:26px;color:var(--mute);font-variant-numeric:tabular-nums}
.ab-how h3{margin:0;font-size:clamp(18px,1.4vw,22px);line-height:1.25;font-weight:600;letter-spacing:-.01em;text-wrap:balance}
.ab-how p{margin:0;font-size:15px;line-height:1.5;color:#3a3936;text-wrap:pretty}
@media(max-width:767px){.ab-row{grid-template-columns:1fr}.ab-how li{grid-template-columns:32px 1fr}.ab-how p{grid-column:2}}
</style>''')

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
    lead = ''.join(f'<p class="ab-lead">{x}</p>' for x in AB_LEAD)
    return f'''<main class="ab"><div class="cs-wrap ab-top"><p class="k">About</p><h1>Hi, I’m Ege.</h1>{lead}</div>
<section class="cs-wrap dx-sec" aria-label="My path, from 2016 to now"><div class="dx" data-dx>
<div class="dx-back">{back}</div>
<div class="dx-page"><div class="dx-in">{pages}</div></div>
<div class="dx-front">{front}</div>
<svg class="dx-box" viewBox="0 0 1000 260" preserveAspectRatio="none" aria-hidden="true"><path d="M30 2 H970 L996 30 V258 H4 V30 Z" fill="#F4F2EE" stroke="#161616" stroke-width="1.6" vector-effect="non-scaling-stroke"/><path d="M4 30 H996" fill="none" stroke="#161616" stroke-width="1.2" vector-effect="non-scaling-stroke"/></svg>
<span class="dx-hd" aria-hidden="true"><i></i><i></i><i></i></span>
</div></section>{more()}</main>
<style>
.ab .k{{font-size:13px;color:var(--mute);margin:0}}
.ab-top{{padding-top:clamp(40px,6vw,96px)}}
.ab h1{{margin:10px 0 0;font-size:clamp(34px,3.6vw,60px);line-height:1.04;letter-spacing:-.03em;font-weight:600}}
.ab-lead{{margin:18px 0 0;max-width:36em;font-size:clamp(16px,1.2vw,20px);line-height:1.45;color:#3a3936;text-wrap:pretty}}
.ab-lead+.ab-lead{{margin-top:10px;font-size:clamp(15px,1.05vw,17px);color:var(--mute)}}
.dx-sec{{padding-top:clamp(40px,5vw,80px)}}
.dx{{--L:#161616;--W:min(100%,820px);position:relative;width:var(--W);margin:0 auto;padding-bottom:clamp(120px,13vw,170px)}}
.dx-back{{position:relative;height:calc(4 * 26px + 30px)}}
.dx-r{{position:absolute;left:calc(9% - var(--k) * 1.2%);right:calc(9% - var(--k) * 1.2%);top:calc(var(--k) * 26px);height:90px;background:#FBFAF6;border:1.5px solid var(--L);border-radius:10px 10px 0 0}}
.dx-front{{position:relative;margin-top:calc(-1 * (2 * 30px + 70px));height:calc(2 * 30px + 70px);z-index:4}}
.dx-r.f{{left:calc(1% - var(--k) * 1.2%);right:calc(1% - var(--k) * 1.2%);top:calc(var(--k) * 30px);height:120px}}
.dx-t{{position:absolute;top:-25px;height:26px;min-width:30%;padding:0 22px;background:#FBFAF6;border:1.5px solid var(--L);border-bottom:0;border-radius:14px 14px 0 0;display:flex;align-items:center;justify-content:center;
  font:600 12px/1 "Inter Tight",sans-serif;letter-spacing:.14em;text-transform:uppercase;color:var(--ink);cursor:pointer;transition:background .2s,color .2s,transform .3s var(--ease)}}
.dx-t.l{{left:12%}}.dx-t.r{{right:12%}}
.dx-t:before{{content:"";position:absolute;left:-1.5px;right:-1.5px;bottom:-3px;height:4px;background:inherit}}
.dx-t.me{{background:var(--ink);color:#fff;cursor:default;letter-spacing:.12em}}
button.dx-t:hover,button.dx-t:focus-visible,button.dx-t.on{{background:var(--ink);color:#fff}}
button.dx-t:hover{{transform:translateY(-3px)}}
button.dx-t:focus-visible{{outline:2px solid var(--ink);outline-offset:4px}}
.dx-page{{position:relative;z-index:3;margin:-58px 4% 0;height:clamp(440px,44vw,500px);background:#FBFAF6;border:1.5px solid var(--L);border-radius:6px;padding:16px}}
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
.dx-hd i{{display:block;width:120px;height:11px;border:1.5px solid var(--L);border-radius:0 0 14px 14px;background:#FBFAF6}}
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
