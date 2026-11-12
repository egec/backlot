"""Backup previews (noindex): one page, tabs at the bottom, each tab shows only the section being compared."""
import re

NOINDEX = '<meta charset="utf-8"><meta name="robots" content="noindex,nofollow">'

# ---- animated grain (reference: Funtown, a flat dark grey with a very fine, slowly moving film grain) ----
def _noise(rgb):
    return ("url(\"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='180' height='180'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='.9' numOctaves='2' stitchTiles='stitch'/%3E%3CfeColorMatrix values='0 0 0 0 " + rgb + " 0 0 0 0 " + rgb + " 0 0 0 0 " + rgb + " 0 0 0 1.6 -.3'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)'/%3E%3C/svg%3E\")")

LB_CSS = (
    '.lb{position:relative;isolation:isolate;overflow:hidden;background-color:var(--lbc)!important}'
    '.lb::after{content:"";position:absolute;inset:-90px;z-index:-1;pointer-events:none;opacity:var(--lbo);background:var(--lbn);animation:lbg .6s steps(1) infinite}'
    '@keyframes lbg{0%{transform:translate(0,0)}17%{transform:translate(-47px,23px)}33%{transform:translate(31px,-61px)}50%{transform:translate(-23px,-37px)}67%{transform:translate(59px,17px)}83%{transform:translate(-11px,67px)}}'
    '@media(prefers-reduced-motion:reduce){.lb::after{animation:none}}'
    '.lb-d{--lbc:#1F2025;--lbn:' + _noise('1') + ';--lbo:.07}'
    '.lb-l{--lbc:#EEE9FB;--lbn:' + _noise('0') + ';--lbo:.07}'
)

# ---- works: sticky title at the bottom of the left column, image and text on the right ----
W1_CSS = (
    '.wk-wrap{display:grid;grid-template-columns:calc(33.33% - 16px) minmax(0,1fr);gap:16px;margin-top:clamp(32px,4vw,64px)}'
    '.wk-wrap .wk-sel{position:sticky;top:calc(100svh - 7rem);align-self:start;margin:0!important;border:0;padding:0}'
    '.wk-wrap .wk-sel .k.k{font-size:clamp(20px,1.3vw,26px)!important}'
    '.wk-wrap .wk-g.vb{margin-top:0}'
    '.wk-wrap .wk-g.vb>.wk-c{grid-template-columns:minmax(0,1.15fr) minmax(0,1fr);grid-template-rows:1fr auto auto 1fr;grid-template-areas:"m ." "m t" "m tg" "m .";column-gap:clamp(24px,3vw,56px);padding:clamp(24px,2.6vw,48px) 0}'
    '.wk-wrap .wk-g.vb>.wk-c .wk-t{font-size:clamp(20px,1.9vw,30px)!important;line-height:1.15}'
    '.wk-wrap .wk-g.vb>.wk-c>.wk-tags{margin:16px 0 0}.wk-wrap .wk-lab{display:none}'
    '@media(max-width:899px){.wk-wrap{grid-template-columns:1fr;gap:0}.wk-wrap .wk-sel{position:static}.wk-wrap .wk-g.vb{margin-top:20px}'
    '.wk-wrap .wk-g.vb>.wk-c{grid-template-columns:1fr;grid-template-rows:none;grid-template-areas:"m" "t" "tg"}.wk-wrap .wk-g.vb>.wk-c .wk-t{margin-top:16px}}'
)

def _works_wrap(html):
    a = '<div class="wk-sel" id="work"><p class="k">Selected work</p></div><div class="wk-g vb">'
    b = '</div></div></div><div class="wk-dk">'
    assert a in html and b in html
    html = html.replace(a, '<div class="wk-wrap"><div class="wk-sel" id="work"><p class="k">Selected works</p></div><div class="wk-g vb">', 1)
    return html.replace(b, '</div></div></div></div><div class="wk-dk">', 1)

# ---- features: the step under the pointer opens, scroll keeps working as before ----
FH1_CSS = (
    '@media(min-width:768px){.zs-steps{border-bottom:0!important}.zs-steps li{position:relative;border-top:0!important;padding-left:22px}'
    '.zs-steps li:before{content:"";position:absolute;left:0;top:0;bottom:0;width:2px;background:var(--line)}'
    '.zs-steps li:after{content:"";position:absolute;left:0;top:0;bottom:0;width:2px;background:var(--gd);transform:scaleY(0);transform-origin:top;transition:transform 1.1s cubic-bezier(.22,1,.36,1)}'
    '.zs-steps li.on:after,.zs-steps li:hover:after{transform:scaleY(1)}'
    '.zs-steps li button{cursor:default;padding:16px 0}'
    '.zs-d{transition:grid-template-rows 1.1s cubic-bezier(.22,1,.36,1)}.zs-d span{opacity:0;transform:translateY(-4px);transition:opacity 1s .12s ease,transform 1s .12s cubic-bezier(.22,1,.36,1)}'
    '.zs-steps li.on .zs-d span{opacity:1;transform:none}}'
)
FH2_CSS = (
    '@media(min-width:768px){.zs-steps li{border-top:1px solid var(--line)}.zs-steps{border-bottom:1px solid var(--line)}'
    '.zs-steps li button{display:grid!important;grid-template-columns:44px minmax(0,1fr) 24px;align-items:center;gap:0!important;padding:20px 0!important;cursor:pointer}'
    '.zs-steps em{width:auto!important;font-size:15px!important;font-weight:500!important}'
    '.zs-steps strong{font-size:clamp(19px,1.5vw,24px)!important;letter-spacing:-.02em}'
    '.zs-steps li button:after{content:"";width:9px;height:9px;border-right:2px solid var(--mute);border-bottom:2px solid var(--mute);transform:rotate(45deg) translate(-2px,-2px);justify-self:end;margin-right:6px;transition:transform .5s cubic-bezier(.22,1,.36,1),border-color .3s}'
    '.zs-steps li.on button:after{transform:rotate(-135deg) translate(-2px,-2px);border-color:var(--ink)}'
    '.zs-steps li:hover button:after{border-color:var(--ink)}'
    '.zs-steps li:hover strong{color:var(--ink)}'
    '.zs-d{transition:grid-template-rows .9s cubic-bezier(.22,1,.36,1)}.zs-d span{padding-left:44px!important;padding-right:24px;max-width:34em!important}}'
)

def hover_js(js):
    c = "st.forEach(function(s,i){s.querySelector('button').addEventListener('click',function(){unfree();act(i,true);go(i)})});"
    assert c in js
    return js.replace(c, c + "st.forEach(function(s,i){s.addEventListener('pointerenter',function(e){if(e.pointerType==='mouse'&&mq.matches&&i!==cur){unfree();act(i,true)}})});")

# ---- crop: show only the part being compared ----
KEEP_JS = ('(function(){function keep(a){var k=[];a.forEach(function(e){for(var n=e;n&&n!==document.body;n=n.parentElement)k.push(n)});'
           'a.forEach(function(e){for(var n=e;n&&n.parentElement&&n!==document.body;n=n.parentElement){[].slice.call(n.parentElement.children).forEach(function(s){'
           'if(k.indexOf(s)<0&&!/^(SCRIPT|STYLE|LINK|svg|SVG)$/.test(s.tagName)&&!s.classList.contains("site-h"))s.remove()})}})}%s})();')

def crop(html, expr, css='', extra_js='', extra_after=''):
    js = KEEP_JS % ("var d=document.querySelector('.wk-dk');if(d)d.style.cssText='position:fixed;top:100vh;height:0;overflow:hidden;visibility:hidden';keep(" + expr + '.concat(d?[d]:[]));' + extra_js)
    html = html.replace('<meta charset="utf-8">', NOINDEX, 1).replace('../assets/', '/assets/')
    return html.replace('</body>', '<style>' + css + '</style><script>' + js + '</script>' + extra_after + '</body>')

SOKO = 'footer.finalfooter{--fb:#D492EC;--ft:#3B1223;--fl:rgba(59,18,35,.28)}'

# add (key, label) pairs here when she asks for backups; empty means no /preview page is built
TABS = [('home3', 'Home: 3.ss')]

SHELL = ('<!doctype html><html lang="tr"><head>' + NOINDEX + '<meta name="viewport" content="width=device-width,initial-scale=1"><title>Onizleme</title>'
         '<style>html,body{margin:0;height:100%;background:#161616;font-family:system-ui,-apple-system,"Segoe UI",sans-serif}'
         'iframe{position:fixed;left:0;top:0;width:100%;height:calc(100% - 58px);border:0;background:#F2F1ED}'
         'nav{position:fixed;left:0;right:0;bottom:0;height:58px;display:flex;gap:8px;align-items:center;padding:0 12px;background:#161616;overflow-x:auto;box-sizing:border-box}'
         'button{flex:none;height:36px;padding:0 16px;border-radius:99px;border:1px solid #4a4a47;background:transparent;color:#d8d8d4;font:500 14px/1 inherit;cursor:pointer}'
         'button:hover{border-color:#aaa}button.on{background:#F2F2EF;border-color:#F2F2EF;color:#161616}</style></head><body>'
         '<iframe id="f" title="Onizleme"></iframe><nav id="n">@@NAV@@</nav>'
         '<script>(function(){var T=@@TABS@@,f=document.getElementById("f"),n=document.getElementById("n");'
         'function go(k){[].forEach.call(n.children,function(b){b.classList.toggle("on",b.dataset.k===k)});f.src=T[k];try{history.replaceState(null,"","#"+k)}catch(e){}}'
         '[].forEach.call(n.children,function(b){b.addEventListener("click",function(){go(b.dataset.k)})});'
         'var h=location.hash.slice(1);go(T[h]?h:Object.keys(T)[0])})();</script></body></html>')

def make_all(write, home_html, backlot_html, work_fn, bjs, hero3=''):
    import json
    if not TABS:
        return
    keys = [k for k, _ in TABS]
    if 'home3' in keys:
        write('preview/home3/index.html', crop(work_fn(hero=hero3), "[].slice.call(document.querySelectorAll('.wk-hero,.wk-sel,.hb-fly,body>.hb-pt,.ckl,.ck'))", '.wk-rv{padding-bottom:0}'))
    base = work_fn(hero=' ') if [k for k in keys if k in ('works', 'ftsoko', 'ftold')] else ''
    if 'works' in keys:
        write('preview/works/index.html', crop(_works_wrap(base), "[document.querySelector('.wk-wrap')]", W1_CSS + '.wk-rv{padding-bottom:0}'))
    sel = "[].slice.call(document.querySelectorAll('.bl2-media:not(.is-img)')).filter(function(e){return e.querySelector('video,iframe')}).slice(0,2)"
    for k, cls in (('bgd', 'lb lb-d'), ('bgl', 'lb lb-l')):
        if k not in keys:
            continue
        js = "var s=" + sel + ";s.forEach(function(e){e.className+=' %s'});keep(s);" % cls
        h = backlot_html.replace('<meta charset="utf-8">', NOINDEX, 1).replace('../assets/', '/assets/')
        js_all = KEEP_JS % js
        write('preview/%s/index.html' % k, h.replace('</body>', '<style>' + LB_CSS + '</style><script>' + js_all + '</script></body>'))
    if 'ftsoko' in keys:
        write('preview/ftsoko/index.html', crop(base, "[document.querySelector('.finalfooter')]", SOKO))
    if 'ftold' in keys:
        write('preview/ftold/index.html', crop(base, "[document.querySelector('.finalfooter')]"))
    tabs = {k: ('/footer/' if k == 'ftall' else '/preview/%s/' % k) for k in keys}
    btn = ''.join('<button type="button" data-k="%s">%s</button>' % (k, t) for k, t in TABS)
    write('preview/index.html', SHELL.replace('@@NAV@@', btn).replace('@@TABS@@', json.dumps(tabs)))
