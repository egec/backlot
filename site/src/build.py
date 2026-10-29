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
    """font-size px -> rem, so type scales with the root size (16px at 1440, 18px at 1920)."""
    def fs(m):
        v = re.sub(r'(\d*\.?\d+)px', lambda n: ('%.4g' % (float(n.group(1)) / 16)) + 'rem', m.group(2))
        return m.group(1) + v
    css = re.sub(r'(font-size:)([^;}"]+)', fs, css)
    css = re.sub(r'(font:\s*\d{3}\s+)(\d*\.?\d+)px', lambda m: m.group(1) + ('%.4g' % (float(m.group(2)) / 16)) + 'rem', css)
    return css

LOGO = 'https://s3.amazonaws.com/webflow-prod-assets/67a7e306e38056dfa249a42d/67a7e87a22185065ca4c8d61_Ege%20Coskun%20(2).png'

def page(title, desc, body, css_files, js_files, extra_head=''):
    css = ''.join('<link rel="stylesheet" href="/assets/%s">' % c for c in css_files)
    js = ''.join('<script src="/assets/%s" defer></script>' % j for j in js_files)
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet">{css}{extra_head}</head><body>
<header class="site-h"><div class="site-hi"><a class="site-logo" href="/" aria-label="Ege Coskun, home"><img src="{LOGO}" alt="Ege Coskun" width="140" height="43"></a>
<nav class="site-n" aria-label="Main"><a href="/work">Work</a><a href="/about">About</a><a href="#contact">Contact</a></nav></div></header>
{body}
<footer class="finalfooter" id="contact">{rem(rd('foot.html'))}</footer>{js}</body></html>'''

# ---------- feature building blocks ----------
def strip(on):
    return '<div class="bl2-strip">Cuts the loop at ' + '<b>→</b>'.join(
        '<i class="on">%s</i>' % x if x == on else '<i>%s</i>' % x for x in ['Deliver', 'Prepare', 'Review', 'Release']) + '</div>'

def head(n, f, first=False, nav=False):
    hid = '<span class="cs-num bl2-x">05</span><span class="cs-title bl2-x">Features</span>' if nav else ''
    return f'{hid}<p class="k">Feature {n:02d}</p><h2 class="bl2-h">{f["t"]}</h2><p class="lead">{f["l"]}</p>'

def media_box(inner):
    return f'<div class="bl2-media">{inner}</div>'

def simple(n, f, media, nav=False):
    return f'<div class="bl2-t bl2-f{" first" if nav else ""}">{head(n, f, nav=nav)}{strip(f["on"])}{media_box(media)}</div>'

def points(n, f, heads, media, nav=False):
    lis = ''.join(f'<li><strong>{h}</strong>{t}</li>' for h, t in zip(heads, f['r']))
    return (f'<div class="bl2-t bl2-f{" first" if nav else ""}"><div class="fp-row"><div>{head(n, f, nav=nav)}</div><ol class="fp-list">{lis}</ol></div>'
            f'{strip(f["on"])}{media_box(media)}</div>')

def zoom(n, f, steps, medias, after='', nav=False):
    """Steps that move the screen: each step can switch media, seek a video and zoom to a point (x,y in %)."""
    lis = ''.join(
        f'<li data-m="{s.get("m", 0)}" data-z="{s["z"]}" data-x="{s["x"]}" data-y="{s["y"]}"' + (f' data-t="{s["t"]}"' if 't' in s else '') +
        f'><strong><em>{i+1:02d}</em>{s["h"]}</strong><span>{t}</span></li>'
        for i, (s, t) in enumerate(zip(steps, f['r'])))
    ms = ''
    for i, m in enumerate(medias):
        on = ' on' if i == 0 else ''
        if m['type'] == 'img':
            ms += f'<img class="zs-m{on}" data-i="{i}" src="{m["src"]}" width="{m["w"]}" height="{m["h"]}" alt="{m["alt"]}" loading="lazy">'
        else:
            ms += f'<video class="zs-m{on}" data-i="{i}" data-zsrc="{m["src"]}" poster="{m["poster"]}" width="{m["w"]}" height="{m["h"]}" muted playsinline preload="none"></video>'
    bars = ''.join('<i></i>' for _ in steps)
    has_video = any(m['type'] == 'video' for m in medias)
    ctl = '<button type="button" class="zs-play" data-zplay><svg width="14" height="14" viewBox="0 0 24 24" aria-hidden="true"><path d="M8 5v14l11-7z" fill="currentColor"/></svg><span>Play the whole video</span></button>' if has_video else ''
    return (f'<div class="bl2-t bl2-f{" first" if nav else ""}">{head(n, f, nav=nav)}<div class="zs" data-zs><ol class="zs-steps">{lis}</ol>'
            f'<div class="zs-stick">{strip(f["on"])}<div class="zs-frame"><div class="zs-view">{ms}</div></div><div class="zs-foot"><div class="zs-bar" aria-hidden="true">{bars}</div>{ctl}</div></div></div>{after}</div>')

IMG_SEASON = dict(type='img', src=GH + 'shots/thumbnails.webp', w=2880, h=1800, alt='Season 4 in Spain: readiness panel, personalized thumbnails and artwork')
IMG_EP2 = dict(type='img', src=GH + 'shots/ep2-shell.webp', w=2880, h=1800, alt='Episode 2 metadata page: needs your input, values from the delivery and AI flags')
VID_UP = dict(type='video', src=GH + 'upload.mp4?v=12', poster=GH + 'posters/upload.jpg?v=12', w=1874, h=1172)
VID_AS = dict(type='video', src=GH + 'assets-filters.mp4?v=11', poster=GH + 'posters/assets-filters.jpg?v=11', w=2054, h=1284)

def features():
    F = FE
    out = []
    out.append(points(1, F[0], ['Comments become reasons', 'Fixed in place', 'Counted before it is sent', 'Publishers can be wrong'], EMB('f663202a'), nav=True))
    out.append(simple(2, F[1], EMB('faf58225')))
    out.append(simple(3, F[2], EMB('f6fe44e7')))
    out.append(zoom(4, F[3], [
        dict(h='Readiness per region', m=0, z=1.9, x=86, y=26),
        dict(h='Progress, not pass or fail', m=0, z=2.4, x=85, y=29),
        dict(h='Gaps come first', m=1, z=1.6, x=38, y=40),
        dict(h='Locked by its source', m=1, z=1.6, x=38, y=78),
        dict(h='Save is not submit', m=1, z=2.2, x=68, y=11)], [IMG_SEASON, IMG_EP2],
        after=media_box(EMB('137e3b55'))))
    out.append(zoom(5, F[4], [
        dict(h='Learns from rejections', m=0, z=1.9, x=87, y=30),
        dict(h='Rules and AI stay apart', m=0, z=2.4, x=82, y=24),
        dict(h='Nothing written on its own', m=0, z=2.2, x=87, y=45)], [IMG_EP2],
        after=media_box(EMB('e76ad60f'))))
    out.append(zoom(6, F[5], [
        dict(h='Matched on upload', t=9, z=2.2, x=86, y=92),
        dict(h='One line of results', t=15, z=2.0, x=18, y=11),
        dict(h='Drop more any time', t=3, z=1.8, x=48, y=15),
        dict(h='Files have their own states', t=15, z=1.5, x=40, y=50)], [VID_UP]))
    out.append(zoom(7, F[6], [
        dict(h='Completeness per title', t=0, z=1.9, x=88, y=85),
        dict(h='Two views, two filters', t=0, z=1.6, x=62, y=68)], [VID_AS]))
    out.append(zoom(8, F[7], [
        dict(h='One thumbnail per taste', m=0, z=1.6, x=33, y=52),
        dict(h='Tested per region', m=0, z=1.7, x=62, y=50),
        dict(h='Backed by click-through', m=0, z=2.2, x=22, y=61)], [IMG_SEASON]))
    out.append(simple(9, F[8], EMB('1ee3cd39')))
    out.append(simple(10, F[9], EMB('59ab0c6b')))
    return ''.join(out)

def sec(k, label, inner):
    return f'<section data-bl2="{k}" data-nav-label="{label}">{inner}</section>'

def backlot():
    w1 = (sec('ov', 'Overview', P['411a7ea2-ad8e-e2d4-3a36-2ddce0bbd66d'])
          + sec('pr', 'The problem', P['cf0faf68-fe6a-067e-c1f5-2da983ff1039'] + media_box(EMB('08e54bfa')))
          + sec('ns', 'North star', P['1f11a2c4-c927-6c80-452e-1af7129ee08d'])
          + sec('rs', 'Research', P['741505c8-29bd-2c89-ccf0-3fb494512923'] + media_box(EMB('c3c045d7')))
          + sec('ro', 'Two roles', P['a5644849-2272-9536-b83b-9657f2bbdb98'] + EMB('13941d11'))
          + sec('fe', 'Features', features())
          + sec('ch', 'What I changed', P['0d287716-73cc-287f-06e0-b21f3dec472a'] + media_box(EMB('8a2ee889')) + P['CARDS']))
    ds = ds_build().replace('Lupin, S4-E2', 'Lupin · S4-E2').replace('Community, S6-E6', 'Community · S6-E6').replace('Long Story Short, S1-E3', 'Long Story Short · S1-E3') \
        .replace('Crime, Drama', 'Crime · Drama').replace('Edit requested, waiting', 'Edit requested · waiting').replace('Editor, Alex', 'Editor · Alex').replace('Publisher, Maya', 'Publisher · Maya')
    w2 = sec('re', "What's next", P['c2545a3c-0f01-ab8f-4f5f-45336f755274'])
    nb = P['78fe6fd2-fd22-0eb4-d2e4-629e35df69b3'].replace('href="/work"', 'href="/"')
    body = (f'<main class="bl2-page"><div class="cs-wrap" data-bl2root="1">{nav_html()}{w1}</div>{ds}<div class="cs-wrap" data-bl2root="2">{w2}</div>{nb}</main>')
    return page('Backlot case study | Ege Coskun',
                'Backlot, a B2B SaaS CMS for streaming services: review and approval workflows, region-specific metadata and an AI check that flags likely rejections.',
                body, ['site.css', 'backlot.css'], ['site.js', 'backlot.js'])

def nav_html():
    # side progress nav: markup only (style lives in backlot.css, script in backlot.js)
    return '<nav class="bl-nav" aria-label="Case study sections"><ol></ol></nav>'

def split_nav():
    s = rd('nav.html')
    css = re.search(r'<style>(.*?)</style>', s, re.S).group(1)
    js = re.search(r'<script>(.*?)</script>', s, re.S).group(1)
    css = re.sub(r'@media \(min-width:992px\)\{.*?\n\}\n', '', css, flags=re.S)
    css = re.sub(r'@media \(min-width:1200px\)\{.*?\n\}\n', '', css, flags=re.S)
    return css, js

def styles():
    nav_css, nav_js = split_nav()
    emb_css = ''.join(re.findall(r'<style>(.*?)</style>', EMB('08e54bfa') + EMB('c3c045d7') + EMB('13941d11') + EMB('f6fe44e7') + EMB('020e6363'), re.S))
    bl = rd('bl2.css') + '\n' + rd('page.css')
    return rem(bl + nav_css + emb_css + DS_CSS), nav_js

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
    # embeds carry their own <style> blocks; they are already in backlot.css, so drop duplicates from the page
    a, b = html.index('<main'), html.index('</main>')
    html = html[:a] + re.sub(r'<style>.*?</style>', '', html[a:b], flags=re.S) + html[b:]
    # the video-control embed is loaded from backlot.js
    write('backlot/index.html', html)
    print('built', len(html))
