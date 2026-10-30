"""Builds the static site into site/ (served by Vercel as-is).
Run: python3 site/src/build.py
"""
import json, os, re
from ds import build as ds_build, CSS as DS_CSS

SRC = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(SRC)
GH = 'https://egec.github.io/backlot/'
rd = lambda p: open(os.path.join(SRC, p), encoding='utf-8').read()
EMB = lambda k: rd('embeds/%s.html' % k)
P = json.load(open(os.path.join(SRC, 'parts.json'), encoding='utf-8'))
FE = json.load(open(os.path.join(SRC, 'feats.json'), encoding='utf-8'))

def rem(css):
    """font-size px -> rem, so type scales with the root size."""
    def fs(m):
        v = re.sub(r'(\d*\.?\d+)px', lambda n: ('%.4g' % (float(n.group(1)) / 16)) + 'rem', m.group(2))
        return m.group(1) + v
    css = re.sub(r'(font-size:)([^;}"]+)', fs, css)
    css = re.sub(r'(font:\s*\d{3}\s+)(\d*\.?\d+)px', lambda m: m.group(1) + ('%.4g' % (float(m.group(2)) / 16)) + 'rem', css)
    return css

LOGO = 'https://s3.amazonaws.com/webflow-prod-assets/67a7e306e38056dfa249a42d/67a7e87a22185065ca4c8d61_Ege%20Coskun%20(2).png'
FULL_IC = '<svg width="14" height="14" viewBox="0 0 24 24" aria-hidden="true"><path d="M4 9V4h5M20 9V4h-5M4 15v5h5M20 15v5h-5" fill="none" stroke="currentColor" stroke-width="2"/></svg>'

def page(title, desc, body, css_files, js_files):
    css = ''.join('<link rel="stylesheet" href="../assets/%s">' % c for c in css_files)
    js = ''.join('<script src="../assets/%s" defer></script>' % j for j in js_files)
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet">{css}</head><body>
<header class="site-h"><div class="site-hi"><a class="site-logo" href="/" aria-label="Ege Coskun, home"><img src="{LOGO}" alt="Ege Coskun" width="140" height="43"></a>
<nav class="site-n" aria-label="Main"><a href="/work">Work</a><a href="/about">About</a><a href="#contact">Contact</a></nav></div></header>
{body}
<footer class="finalfooter" id="contact">{rem(rd('foot.html'))}</footer>{js}</body></html>'''

# ---------- building blocks ----------
def strip(on):
    return '<div class="bl2-strip">Cuts the loop at ' + '<b>→</b>'.join(
        '<i class="on">%s</i>' % x if x == on else '<i>%s</i>' % x for x in ['Deliver', 'Prepare', 'Review', 'Release']) + '</div>'

def head(n, f, nav=False):
    hid = '<span class="cs-num bl2-x">05</span><span class="cs-title bl2-x">Features</span>' if nav else ''
    return f'{hid}<p class="k">Feature {n:02d}</p><h2 class="bl2-h">{f["t"]}</h2><p class="lead">{f["l"]}</p>'

def media_box(inner):
    return f'<div class="bl2-media">{inner}</div>'

def sub(title, text=''):
    """small heading that says what the next media shows"""
    return f'<div class="bl2-subh"><h3>{title}</h3>' + (f'<p>{text}</p>' if text else '') + '</div>'

def simple(n, f, media, nav=False):
    return f'<div class="bl2-t bl2-f{" first" if nav else ""}">{head(n, f, nav=nav)}{strip(f["on"])}{media_box(media)}</div>'

def zoom(n, f, steps, medias, after='', nav=False):
    """Steps that move the screen. Each step can switch media (m), seek a video (t), zoom to a point (z, x, y in %)
    and highlight boxes (hl: list of (x, y, w, h) in % of the media)."""
    lis = ''.join(
        f'<li data-m="{s.get("m", 0)}" data-z="{s["z"]}" data-x="{s["x"]}" data-y="{s["y"]}"' + (f' data-t="{s["t"]}"' if 't' in s else '') +
        f'><em>{i+1:02d}</em><strong>{s["h"]}</strong><span>{t}</span></li>'
        for i, (s, t) in enumerate(zip(steps, f['r'])))
    ms = ''
    for i, m in enumerate(medias):
        on = ' on' if i == 0 else ''
        if m['type'] == 'img':
            el = f'<img class="zs-m" src="{m["src"]}" width="{m["w"]}" height="{m["h"]}" alt="{m["alt"]}" loading="lazy">'
        else:
            el = f'<video class="zs-m" data-zsrc="{m["src"]}" poster="{m["poster"]}" width="{m["w"]}" height="{m["h"]}" muted playsinline preload="none"></video>'
        hls = ''.join(f'<i class="zs-hl" data-s="{si}" style="left:{x}%;top:{y}%;width:{w}%;height:{h}%"></i>'
                      for si, s in enumerate(steps) if s.get('m', 0) == i for (x, y, w, h) in s.get('hl', []))
        ms += f'<div class="zs-mw{on}" data-i="{i}">{el}{hls}</div>'
    bars = ''.join('<i></i>' for _ in steps)
    has_video = any(m['type'] == 'video' for m in medias)
    ctl = ('<button type="button" class="zs-play" data-zplay><svg width="14" height="14" viewBox="0 0 24 24" aria-hidden="true"><path d="M8 5v14l11-7z" fill="currentColor"/></svg>'
           '<span>Play the whole video</span></button>') if has_video else ''
    return (f'<div class="bl2-t bl2-f{" first" if nav else ""}">{head(n, f, nav=nav)}<div class="zs" data-zs><ol class="zs-steps">{lis}</ol>'
            f'<div class="zs-stick">{strip(f["on"])}<div class="zs-frame"><div class="zs-view">{ms}</div></div>'
            f'<div class="zs-foot"><div class="zs-bar" aria-hidden="true">{bars}</div>{ctl}</div></div></div>{after}</div>')

IMG_SEASON = dict(type='img', src=GH + 'shots/thumbnails.webp', w=2880, h=1800, alt='Season 4 in Spain: region selector, readiness panel, personalized thumbnails')
IMG_EP2 = dict(type='img', src=GH + 'shots/ep2-shell.webp', w=2880, h=1800, alt='Episode 2 metadata page: needs your input, values from the delivery, AI flags')
IMG_REJ = dict(type='img', src=GH + 'posters/rejection-flow.jpg', w=1844, h=1168, alt='Publisher review page for Sherlock Holmes with metadata rows')
VID_UP = dict(type='video', src=GH + 'upload.mp4?v=12', poster=GH + 'posters/upload.jpg?v=12', w=1874, h=1172)
VID_AS = dict(type='video', src=GH + 'assets-filters.mp4?v=11', poster=GH + 'posters/assets-filters.jpg?v=11', w=2054, h=1284)

def features():
    F = FE
    o = []
    o.append(zoom(1, F[0], [
        dict(h='Comments become reasons', z=1.5, x=52, y=78, hl=[(5.7, 74.8, 92.2, 4.6)]),
        dict(h='Fixed in place', z=2, x=86, y=51, hl=[(89.6, 49.2, 8.4, 3.7)]),
        dict(h='Counted before it is sent', z=2, x=86, y=14, hl=[(91.2, 9.8, 6.8, 4.1)]),
        dict(h='Publishers can be wrong', z=1.5, x=80, y=74, hl=[(88.7, 62, 2.6, 37)])], [IMG_REJ],
        after=sub('Try it', 'Flag two fields as the publisher, then fix them as the editor.') + media_box(EMB('f663202a')), nav=True))
    o.append(simple(2, F[1], EMB('faf58225')))
    o.append(simple(3, F[2], EMB('f6fe44e7')))
    o.append(zoom(4, F[3], [
        dict(h='Readiness per region', m=0, z=1.5, x=78, y=20, hl=[(59.5, 8.9, 13.7, 3.9), (75.6, 9.4, 22, 7.8)]),
        dict(h='Progress, not pass or fail', m=0, z=1.9, x=85, y=29, hl=[(91.6, 23.4, 5.6, 14.4), (91.4, 10.8, 6.2, 2.6)]),
        dict(h='Gaps come first', m=1, z=1.25, x=40, y=40, hl=[(5, 23.5, 68, 34.5)]),
        dict(h='Locked by its source', m=1, z=1.4, x=40, y=78, hl=[(14.6, 63.4, 5.4, 2.9), (36.1, 70.4, 2, 23), (70.1, 70.4, 2, 23)]),
        dict(h='Save is not submit', m=1, z=1.05, x=50, y=52, hl=[(62.8, 8.8, 9.9, 3.9), (66.6, 95.1, 5.7, 3.7)])], [IMG_SEASON, IMG_EP2],
        after=sub('The whole page in one pass', 'A walkthrough from the season to the episode that blocks it.') + media_box(EMB('137e3b55'))))
    o.append(zoom(5, F[4], [
        dict(h='Learns from rejections', z=1.8, x=87, y=24, hl=[(76, 15.5, 22, 9.6)]),
        dict(h='Rules and AI stay apart', z=1.9, x=86, y=36, hl=[(76.8, 23.2, 7.2, 2.4), (76.8, 36.5, 7.2, 2.4), (76.8, 50.2, 7.2, 2.4)]),
        dict(h='Nothing written on its own', z=1.9, x=88, y=32, hl=[(95.1, 17.2, 2.6, 3.4), (95.1, 28.6, 2.6, 3.4), (95.1, 41.9, 2.6, 3.4)])], [IMG_EP2],
        after=sub('Rules and AI, side by side', 'Rule checks pass or fail. AI suggestions name their evidence, and a dismissed flag stays on record.') + media_box(EMB('e76ad60f'))))
    o.append(zoom(6, F[5], [
        dict(h='Matched on upload', t=9, z=2, x=86, y=92, hl=[(74, 86.5, 24.5, 11)]),
        dict(h='One line of results', t=15, z=1.8, x=20, y=13, hl=[(3, 7.5, 25, 7)]),
        dict(h='Drop more any time', t=3, z=1.6, x=46, y=20, hl=[(28.5, 12.5, 35, 13.5)]),
        dict(h='Files have their own states', t=15, z=1.3, x=40, y=52, hl=[(3, 28, 70, 52)])], [VID_UP]))
    o.append(zoom(7, F[6], [
        dict(h='Completeness per title', t=0, z=1.7, x=86, y=85, hl=[(83, 74, 15, 26)]),
        dict(h='Two views, two filters', t=0, z=1.4, x=55, y=68, hl=[(5, 65.5, 93, 6)])], [VID_AS]))
    o.append(zoom(8, F[7], [
        dict(h='One thumbnail per taste', z=1.4, x=40, y=52, hl=[(6, 43, 67, 19)]),
        dict(h='Tested per region', z=1.5, x=55, y=52, hl=[(54, 40.4, 19.5, 3), (33, 59.4, 8.2, 3.2), (50, 59.4, 8.2, 3.2), (67, 59.4, 8.2, 3.2)]),
        dict(h='Backed by click-through', z=2, x=20, y=58, hl=[(6, 58.4, 15.5, 5.6)])], [IMG_SEASON]))
    o.append(simple(9, F[8], EMB('1ee3cd39')))
    o.append(simple(10, F[9], EMB('59ab0c6b')))
    return ''.join(o)

# ---------- research: findings with a small product visual each ----------
def research():
    def card(vis, finding, decision):
        return (f'<div class="rs-c"><div class="rv">{vis}</div><div class="rs-t"><p class="rs-k">Finding</p><p>{finding}</p>'
                f'<p class="rs-k rs-d"><span aria-hidden="true">→</span> Decision</p><p class="rs-dec">{decision}</p></div></div>')
    tree = ('<div class="rv-tree"><div class="rv-l">Series <span>Lupin</span></div><div class="rv-l l2">Season 4</div>'
            '<div class="rv-l l3 on">Episode 2 <b>Age rating lives here</b></div><div class="rv-l l4">Files <span>video, subtitles, audio</span></div></div>')
    reg = ('<div class="rv-reg"><div class="rv-chips"><span class="on">ES</span><span>FR</span><span>DE</span></div>'
           '<div class="rv-f"><small>Localised title (ES)</small>El collar de la reina</div><div class="rv-f"><small>Age rating (ES)</small>16</div></div>')
    rsn = ('<div class="rv-rsn"><div class="rv-top"><span class="rv-chip">Rejected</span><b>2 reasons</b></div>'
           '<div class="rv-r"><span>Age rating</span><i>Compliance</i></div><div class="rv-r"><span>Synopsis (ES)</span><i>Localization</i></div></div>')
    return ('<div class="bl2-t"><span class="cs-num bl2-x">03</span><div class="bl2-head"><div><p class="k">Research</p>'
            '<h2 class="bl2-h cs-title">What the domain taught me, and what it changed</h2></div>'
            '<p class="lead">CMS tools are built in-house and rarely shown, so I studied products that each solve part of the job, and one from outside media: code review on GitHub.</p></div>'
            '<div class="rs-g">'
            + card(tree, 'Mistakes come from structure the editor can’t see, like metadata on the wrong level.', 'Every field shows the level it lives on.')
            + card(reg, 'Almost every field changes by region, from title to audio.', 'Region comes first. Everything under it shows for that region only.')
            + card(rsn, 'Every tool lets you comment on a field. None turns a rejection into data.', 'A rejection is a list of reasons, pinned to fields and counted.')
            + '</div><p class="bl2-strong">Field comments exist. A rejection made of reasons that teach the next check does not.</p></div>')

def roles_viewer():
    e = EMB('13941d11')
    e = e.replace('<div class="blr-bar"', '<div class="blr-fs"><div class="blr-bar"', 1)
    e = e.replace('Publisher reviews</button></div>', 'Publisher reviews</button><button type="button" class="blr-full" data-fs aria-label="Full screen" title="Full screen">' + FULL_IC + '</button></div>', 1)
    e = e.replace('</div></div><script>', '</div></div></div><script>', 1)
    return e

def changed():
    story = ('<div class="bl2-t"><span class="cs-num bl2-x">06</span><p class="k">What I changed</p>'
             '<h2 class="bl2-h cs-title">One label showed me the first version was wrong</h2>'
             '<div class="bl2-split bl2-split-first"><p class="k">The first version</p><div><p>The first version allowed one rejection reason per item, and I caught myself labelling rejected items “Multiple Issues”. '
             'That label was a symptom, not a reason, so reasons became a list, each pinned to a field and resolvable on its own.</p></div></div></div>')
    return (story + '<div class="bl2-t">' + sub('Version 1 and version 2', 'The same rejection, first with one reason, then with reasons pinned to fields.') + '</div>'
            + media_box(EMB('8a2ee889'))
            + '<div class="bl2-t">' + sub('What I took out', 'Most of what I added stayed. Four things didn’t.') + '</div>' + P['CARDS'])

def sec(k, label, inner):
    return f'<section data-bl2="{k}" data-nav-label="{label}">{inner}</section>'

def backlot():
    w1 = (sec('ov', 'Overview', P['411a7ea2-ad8e-e2d4-3a36-2ddce0bbd66d'])
          + sec('pr', 'The problem', P['cf0faf68-fe6a-067e-c1f5-2da983ff1039'])
          + sec('ns', 'North star', P['1f11a2c4-c927-6c80-452e-1af7129ee08d'])
          + sec('rs', 'Research', research() + media_box(EMB('c3c045d7')))
          + sec('ro', 'Two roles', P['a5644849-2272-9536-b83b-9657f2bbdb98'] + roles_viewer())
          + sec('fe', 'Features', features())
          + sec('ch', 'What I changed', changed()))
    ds = ds_build().replace('Lupin, S4-E2', 'Lupin · S4-E2').replace('Community, S6-E6', 'Community · S6-E6').replace('Long Story Short, S1-E3', 'Long Story Short · S1-E3') \
        .replace('Crime, Drama', 'Crime · Drama').replace('Edit requested, waiting', 'Edit requested · waiting').replace('Editor, Alex', 'Editor · Alex').replace('Publisher, Maya', 'Publisher · Maya')
    w2 = sec('re', "What's next", P['c2545a3c-0f01-ab8f-4f5f-45336f755274'])
    nb = P['78fe6fd2-fd22-0eb4-d2e4-629e35df69b3'].replace('href="/work"', 'href="/"')
    body = (f'<main class="bl2-page"><div class="cs-wrap" data-bl2root="1"><nav class="bl-nav" aria-label="Case study sections"><ol></ol></nav>{w1}</div>'
            f'{ds}<div class="cs-wrap" data-bl2root="2">{w2}</div>{nb}</main>')
    return page('Backlot case study | Ege Coskun',
                'Backlot, a B2B SaaS CMS for streaming services: review and approval workflows, region-specific metadata and an AI check that flags likely rejections.',
                body, ['site.css', 'backlot.css'], ['site.js', 'backlot.js'])

def split_nav():
    s = rd('nav.html')
    css = re.search(r'<style>(.*?)</style>', s, re.S).group(1)
    js = re.search(r'<script>(.*?)</script>', s, re.S).group(1)
    css = re.sub(r'@media \(min-width:992px\)\{.*?\n\}\n', '', css, flags=re.S)
    css = re.sub(r'@media \(min-width:1200px\)\{.*?\n\}\n', '', css, flags=re.S)
    return css, js

def styles():
    nav_css, nav_js = split_nav()
    emb_css = ''.join(re.findall(r'<style>(.*?)</style>', EMB('c3c045d7') + EMB('13941d11') + EMB('f6fe44e7') + EMB('020e6363'), re.S))
    return rem(rd('bl2.css') + '\n' + nav_css + emb_css + DS_CSS + '\n' + rd('page.css')), nav_js

def write(path, s):
    p = os.path.join(OUT, path)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, 'w', encoding='utf-8').write(s)

if __name__ == '__main__':
    css, nav_js = styles()
    write('assets/backlot.css', css)
    write('assets/site.css', rem(rd('site.css')))
    vid_js = re.search(r'<script>(.*?)</script>', EMB('020e6363'), re.S).group(1)
    write('assets/backlot.js', nav_js + '\n' + rd('bl2.js') + '\n' + vid_js + '\n' + rd('zoom.js'))
    write('assets/site.js', rd('site.js'))
    html = backlot()
    a, b = html.index('<main'), html.index('</main>')
    html = html[:a] + re.sub(r'<style>.*?</style>', '', html[a:b], flags=re.S) + html[b:]
    write('backlot/index.html', html)
    print('built', len(html))
