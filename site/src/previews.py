"""Backup preview pages (noindex): works layout, feature hover options, animated backgrounds."""
import re

NOINDEX = '<meta charset="utf-8"><meta name="robots" content="noindex,nofollow">'

NOISE_W = "url(\"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='240' height='240'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.85' numOctaves='2' stitchTiles='stitch'/%3E%3CfeColorMatrix values='0 0 0 0 1 0 0 0 0 1 0 0 0 0 1 0 0 0 1.4 -.2'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E\")"
NOISE_K = NOISE_W.replace('values=\'0 0 0 0 1 0 0 0 0 1 0 0 0 0 1', 'values=\'0 0 0 0 0 0 0 0 0 0 0 0 0 0 0')

# ---- animated background for prototype and animation frames (grain + dot grid + soft cursor light) ----
LB_SEL = '.bl2-media:not(.is-img):has(video,iframe)'
LB_CSS = (
    '.lb{position:relative;isolation:isolate;overflow:hidden;background-color:var(--lbc)!important;'
    'background-image:radial-gradient(circle,var(--lbd) 1.2px,transparent 1.7px)!important;background-size:30px 30px!important}'
    '.lb::before{content:"";position:absolute;inset:0;z-index:-1;pointer-events:none;opacity:0;transition:opacity .5s;'
    'background:radial-gradient(circle,var(--lbh) 1.5px,transparent 2px) 0 0/30px 30px;'
    '-webkit-mask-image:radial-gradient(220px circle at var(--mx,-999px) var(--my,-999px),#000,transparent);mask-image:radial-gradient(220px circle at var(--mx,-999px) var(--my,-999px),#000,transparent)}'
    '.lb:hover::before{opacity:1}'
    '.lb::after{content:"";position:absolute;inset:-60px;z-index:-1;pointer-events:none;opacity:var(--lbo,.08);background:var(--lbn);animation:lbg .8s steps(1) infinite}'
    '@keyframes lbg{0%{transform:translate(0,0)}16%{transform:translate(-31px,19px)}33%{transform:translate(23px,-37px)}50%{transform:translate(-17px,-23px)}66%{transform:translate(37px,11px)}83%{transform:translate(-5px,41px)}}'
    '@media(prefers-reduced-motion:reduce){.lb::after{animation:none}}'
    '.lb-k{--lbc:#111214;--lbd:rgba(255,255,255,.13);--lbh:rgba(255,255,255,.6);--lbn:' + NOISE_W + ';--lbo:.07}'
    '.lb-g{--lbc:#56652A;--lbd:rgba(220,208,248,.26);--lbh:rgba(220,208,248,.95);--lbn:' + NOISE_W + ';--lbo:.08}'
    '.lb-l{--lbc:#DCD0F8;--lbd:rgba(86,101,42,.26);--lbh:rgba(86,101,42,.85);--lbn:' + NOISE_K + ';--lbo:.07}'
)
LB_JS = ('(function(){function m(e){var r=this.getBoundingClientRect();this.style.setProperty("--mx",(e.clientX-r.left)+"px");this.style.setProperty("--my",(e.clientY-r.top)+"px")}'
         '[].forEach.call(document.querySelectorAll(".lb"),function(b){b.addEventListener("pointermove",m)})})();')

def bg_test(html):
    js = ('(function(){var c=["lb lb-k","lb lb-g","lb lb-l"],b=document.querySelectorAll(\'' + LB_SEL + '\');for(var i=0;i<3&&i<b.length;i++)b[i].className+=" "+c[i]})();' + LB_JS)
    return html.replace('<meta charset="utf-8">', NOINDEX, 1).replace('</body>', '<style>' + LB_CSS + '</style><script>' + js + '</script></body>')

# ---- works: sticky title on the left, image and text on the right ----
W1_CSS = (
    '.wk-wrap{display:grid;grid-template-columns:calc(33.33% - 16px) minmax(0,1fr);gap:16px;margin-top:clamp(64px,8vw,140px)}'
    '.wk-wrap .wk-sel{position:sticky;top:calc(4.75rem + 24px);align-self:start;margin:0!important;border:0;padding:0}'
    '.wk-wrap .wk-sel .k.k{font-size:clamp(20px,1.3vw,26px)!important}'
    '.wk-wrap .wk-g.vb{margin-top:0}'
    '.wk-wrap .wk-g.vb>.wk-c{grid-template-columns:minmax(0,1.15fr) minmax(0,1fr);grid-template-rows:1fr auto auto 1fr;grid-template-areas:"m ." "m t" "m tg" "m .";column-gap:clamp(24px,3vw,56px);padding:clamp(24px,2.6vw,48px) 0}'
    '.wk-wrap .wk-g.vb>.wk-c .wk-t{font-size:clamp(20px,1.9vw,30px)!important;line-height:1.15}'
    '.wk-wrap .wk-g.vb>.wk-c>.wk-tags{margin:16px 0 0}.wk-wrap .wk-lab{display:none}'
    '@media(max-width:899px){.wk-wrap{grid-template-columns:1fr;gap:0}.wk-wrap .wk-sel{position:static}.wk-wrap .wk-g.vb{margin-top:20px}'
    '.wk-wrap .wk-g.vb>.wk-c{grid-template-columns:1fr;grid-template-rows:none;grid-template-areas:"m" "t" "tg"}.wk-wrap .wk-g.vb>.wk-c .wk-t{margin-top:16px}}'
)

def works_1(html):
    a = '<div class="wk-sel" id="work"><p class="k">Selected work</p></div><div class="wk-g vb">'
    b = '</div></div></div><div class="wk-dk">'
    assert a in html and b in html
    html = html.replace(a, '<div class="wk-wrap"><div class="wk-sel" id="work"><p class="k">Selected works</p></div><div class="wk-g vb">', 1)
    html = html.replace(b, '</div></div></div></div><div class="wk-dk">', 1)
    return html.replace('<meta charset="utf-8">', NOINDEX, 1).replace('</body>', '<style>' + W1_CSS + '</style></body>')

# ---- features: steps follow the pointer instead of the scroll ----
FH_BASE = (
    '@media(min-width:768px){.zs{height:auto!important}.zs-pin{position:static!important}}'
)
FH1_CSS = FH_BASE + (
    '@media(min-width:768px){.zs-steps{border-bottom:0!important}.zs-steps li{position:relative;border-top:0!important;padding-left:22px}'
    '.zs-steps li:before{content:"";position:absolute;left:0;top:0;bottom:0;width:2px;background:var(--line)}'
    '.zs-steps li:after{content:"";position:absolute;left:0;top:0;bottom:0;width:2px;background:var(--gd);transform:scaleY(0);transform-origin:top;transition:transform 1.1s cubic-bezier(.22,1,.36,1)}'
    '.zs-steps li.on:after{transform:scaleY(1)}.zs-steps li:hover:after{transform:scaleY(1)}'
    '.zs-steps li button{cursor:default;padding:16px 0}'
    '.zs-d{transition:grid-template-rows 1.1s cubic-bezier(.22,1,.36,1)}.zs-d span{opacity:0;transform:translateY(-4px);transition:opacity 1s .12s ease,transform 1s .12s cubic-bezier(.22,1,.36,1)}'
    '.zs-steps li.on .zs-d span{opacity:1;transform:none}}'
)
FH2_CSS = FH_BASE + (
    '@media(min-width:768px){.zs-steps li{border-top:1px solid var(--line)}.zs-steps{border-bottom:1px solid var(--line)}'
    '.zs-steps li button{display:grid!important;grid-template-columns:44px minmax(0,1fr) 24px;align-items:center;gap:0!important;padding:20px 0!important;cursor:pointer}'
    '.zs-steps em{width:auto!important;font-size:15px!important;font-weight:500!important}'
    '.zs-steps strong{font-size:clamp(19px,1.5vw,24px)!important;letter-spacing:-.02em}'
    '.zs-steps li button:after{content:"";width:9px;height:9px;border-right:2px solid var(--mute);border-bottom:2px solid var(--mute);transform:rotate(45deg) translate(-2px,-2px);justify-self:end;margin-right:6px;transition:transform .5s cubic-bezier(.22,1,.36,1),border-color .3s}'
    '.zs-steps li.on button:after{transform:rotate(-135deg) translate(-2px,-2px);border-color:var(--ink)}'
    '.zs-steps li button:hover:after{border-color:var(--ink)}'
    '.zs-d span{padding-left:44px!important;padding-right:24px;max-width:34em!important}}'
)

def feat(html, css, js_name):
    html = html.replace('<meta charset="utf-8">', NOINDEX, 1).replace('</body>', '<style>' + css + '</style></body>')
    assert 'backlot.js' in html
    return html.replace('backlot.js', js_name)

def hover_js(js, pointer):
    a = 'function onScroll(){if(!mq.matches)return;'
    b = 'function go(i){if(!mq.matches){act(i);return}'
    assert a in js and b in js
    js = js.replace(a, 'function onScroll(){return;').replace(b, 'function go(i){act(i);return;')
    if pointer:
        c = "st.forEach(function(s,i){s.querySelector('button').addEventListener('click',function(){unfree();act(i,true);go(i)})});"
        assert c in js
        js = js.replace(c, c + "st.forEach(function(s,i){s.addEventListener('pointerenter',function(e){if(e.pointerType==='mouse'){unfree();act(i,true)}})});")
    return js
