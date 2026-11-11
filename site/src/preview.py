"""Unlisted preview pages: About page + contact panel + footer in the footer test palettes 1, 5 and 9 (numbers as on /footer/)."""
import os, re
R = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..')
PL = {  # page number: (bg, tx, underline, buttons, kicker, accent on dark)
    1: ('#DCD0F8', '#56652A', '#672D37', '#56652A', '#56652A', '#DCD0F8'),
    5: ('#56652A', '#F2E5EF', '#D5DA8F', '#CDB1EA', '#F2E5EF', '#CDB1EA'),
    9: ('#E9CFD3', '#672D37', '#56652A', '#56652A', '#672D37', '#E9CFD3'),
}
def rgb(h): return ','.join(str(int(h[i:i + 2], 16)) for i in (1, 3, 5))
src = open(os.path.join(R, 'about', 'index.html'), encoding='utf-8').read()
for n, (bg, tx, ul, tb, tk, ac) in PL.items():
    h = src.replace('#DCD0F8', ac).replace('rgba(220,208,248,', f'rgba({rgb(ac)},').replace('#4F2550', tx).replace('rgba(79,37,80,', f'rgba({rgb(tx)},')
    css = f'''<style>html.pv{{--bg:{bg};--tx:{tx};--ul:{ul};--tb:{tb};--tk:{tk};--ac:{ac}}}
footer.finalfooter.pal{{background:var(--bg)}}.pal .ec-foot,.pal .ec-q{{color:var(--tx)}}.pal .ec-foot .ec-k{{color:color-mix(in srgb,var(--tk) 78%,var(--bg))}}
.pal .ec-mail{{color:var(--tx)!important;background-image:linear-gradient(var(--ul),var(--ul))}}.pal .ec-mail:hover{{color:var(--tx)!important}}
.pal .ec-btn{{border-color:color-mix(in srgb,var(--tb) 50%,transparent);color:var(--tb)!important}}.pal .ec-fl{{background:var(--tb)}}
.pal .ec-btn.on{{color:var(--bg)!important;border-color:var(--tb)}}.pal .ec-btn:focus-visible{{outline-color:var(--tb)}}.pal .ec-btn:active{{background:var(--tb);color:var(--bg)!important}}
.pal .ec-top,.pal .ec-top.lt{{color:var(--tx)}}
.ct{{background:var(--bg);color:var(--tx)}}.ct-a h2{{color:var(--tx)}}.ct-a p,.ct-c p{{color:color-mix(in srgb,var(--tx) 80%,transparent)}}
.ct-b{{border-top-color:color-mix(in srgb,var(--tx) 30%,transparent)}}.ct-b li{{border-bottom-color:color-mix(in srgb,var(--tx) 30%,transparent)}}
.ct-b a,.ct-b a:hover{{color:var(--tx)}}
.ct-cp{{border-color:color-mix(in srgb,var(--tb) 50%,transparent);color:var(--tb)}}.ct-cp:hover{{background:var(--tb);border-color:var(--tb);color:var(--bg)}}
.ct-x{{border-color:color-mix(in srgb,var(--tb) 50%,transparent);color:var(--tb)}}.ct-x:hover{{background:var(--tb);color:var(--bg)}}.ct :focus-visible,.ct-x:focus-visible{{outline-color:var(--tb)}}
html.pv .ck i{{background:var(--tx)}}html.pv.ck-d .ck i{{background:var(--ac)}}
html.pv:has(.ec-btn.on) .ck i,html.pv:has(.ct-cp:hover) .ck i,html.pv:has(.ct-x:hover) .ck i{{background:var(--bg)}}
.ax-say{{background:var(--tx)!important;color:var(--bg)!important;box-shadow:0 0 0 1px color-mix(in srgb,var(--bg) 50%,transparent)!important}}</style>'''
    h = h.replace('<html lang="en" class="f-it">', '<html lang="en" class="f-it pv">', 1).replace('<head>', '<head><meta name="robots" content="noindex,nofollow">', 1)
    h = h.replace('<footer class="finalfooter" id="contact">', '<footer class="finalfooter pal" id="contact">', 1)
    h = h.replace('</head>', css + '</head>', 1)
    d = os.path.join(R, f'footer-{n}'); os.makedirs(d, exist_ok=True)
    open(os.path.join(d, 'index.html'), 'w', encoding='utf-8').write(h)
    print('footer-%d' % n, len(h))
