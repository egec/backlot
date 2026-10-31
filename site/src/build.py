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

def page(title, desc, body, css_files, js_files, font='it'):
    css = ''.join('<link rel="stylesheet" href="../assets/%s">' % c for c in css_files)
    js = ''.join('<script src="../assets/%s" defer></script>' % j for j in js_files)
    fl = '<link href="https://fonts.googleapis.com/css2?family=Inter+Tight:wght@400;500;600;700;800&display=swap" rel="stylesheet">' if font else ''
    return f'''<!doctype html><html lang="en"{' class="f-it"' if font else ''}><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet">{fl}{css}</head><body>
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
    cls = ''
    if re.search(r'proto/(rejection|region)/', inner):  # clickable prototypes stand out on her green
        cls = ' is-proto'
        inner = re.sub(r'(proto/(?:rejection|region)/)"', r'\1?on=green"', inner)
    return f'<div class="bl2-media{cls}">{inner}</div>'

def sub(title, text=''):
    """small heading that says what the next media shows"""
    return f'<div class="bl2-subh"><h3>{title}</h3>' + (f'<p>{text}</p>' if text else '') + '</div>'

def simple(n, f, media, nav=False):
    return f'<div class="bl2-t bl2-f{" first" if nav else ""}">{head(n, f, nav=nav)}{media_box(media)}</div>'

ZCAP = 1.5
def fit(s):
    """z, x, y from the highlight boxes plus an optional context box (ctx) that must stay in view, e.g. a heading."""
    if 'z' in s:
        return s
    bs = list(s.get('hl', [])) + ([s['ctx']] if 'ctx' in s else [])
    x0 = min(b[0] for b in bs); y0 = min(b[1] for b in bs)
    x1 = max(b[0] + b[2] for b in bs); y1 = max(b[1] + b[3] for b in bs)
    z = max(1, min(ZCAP, 85 / max(x1 - x0, y1 - y0)))
    return dict(s, z=round(z, 2), x=round((x0 + x1) / 2, 1), y=round((y0 + y1) / 2, 1))

def zoom(n, f, steps, medias, after='', nav=False):
    """Steps that move the screen. Each step can switch media (m), seek a video (t), zoom to a point (z, x, y in %)
    and highlight boxes (hl: list of (x, y, w, h) in % of the media). The text and the screen stay pinned while
    scrolling moves through the steps."""
    steps = [fit(s) for s in steps]
    lis = ''.join(
        f'<li data-m="{s.get("m", 0)}" data-z="{s["z"]}" data-x="{s["x"]}" data-y="{s["y"]}"' + (f' data-t="{s["t"]}"' if 't' in s else '') +
        f'><button type="button"><em>{i+1:02d}</em><strong>{s["h"]}</strong></button><div class="zs-d"><span>{t}</span></div></li>'
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
    bars = ''.join(f'<button type="button" aria-label="Step {i+1}"><i></i></button>' for i in range(len(steps)))
    has_video = any(m['type'] == 'video' for m in medias)
    ctl = ('<button type="button" class="zs-play" data-zplay><svg width="14" height="14" viewBox="0 0 24 24" aria-hidden="true"><path d="M8 5v14l11-7z" fill="currentColor"/></svg>'
           '<span>Play the whole video</span></button>') if has_video else ''
    return (f'<div class="bl2-t bl2-f{" first" if nav else ""}">{head(n, f, nav=nav)}<div class="zs" data-zs style="--n:{len(steps)}"><div class="zs-pin"><ol class="zs-steps">{lis}</ol>'
            f'<div class="zs-stick"><div class="zs-frame"><div class="zs-view">{ms}</div></div>'
            f'<div class="zs-foot"><div class="zs-bar">{bars}</div>{ctl}</div></div></div></div>{after}</div>')

IMG_SEASON = dict(type='img', src=GH + 'shots/thumbnails.webp', w=2880, h=1800, alt='Season 4 in Spain: region selector, readiness panel, personalized thumbnails')
IMG_EP2 = dict(type='img', src=GH + 'shots/ep2-shell.webp', w=2880, h=1800, alt='Episode 2 metadata page: needs your input, values from the delivery, AI flags')
IMG_REJ = dict(type='img', src=GH + 'shots/reject-v2.webp', w=1846, h=1154, alt='Publisher review of Sherlock Holmes: two flagged rows and a list of two rejection reasons')
IMG_UP3 = dict(type='img', src=GH + 'shots/upload-3.webp', w=1874, h=1172, alt='Upload drop zone open over the assets list')
IMG_UP15 = dict(type='img', src=GH + 'shots/upload-15.webp', w=1874, h=1172, alt='Season 4 in Spain with the upload result in the corner and 15 files waiting in the readiness panel')
IMG_AS = dict(type='img', src=GH + 'posters/assets-filters.jpg?v=11', w=2054, h=1284, alt='Assets: the delivery batch with a state per file, and the content list with completeness per title')
VID_UP = dict(type='video', src=GH + 'upload.mp4?v=12', poster=GH + 'posters/upload.jpg?v=12', w=1874, h=1172)
VID_AS = dict(type='video', src=GH + 'assets-filters.mp4?v=11', poster=GH + 'posters/assets-filters.jpg?v=11', w=2054, h=1284)

def features():
    F = FE
    o = []
    o.append(zoom(1, F[0], [
        dict(h='Comments become reasons', hl=[(69.5, 14.6, 28, 14.6), (5.6, 22.6, 61.4, 7.4)], ctx=(69.5, 10, 28, 1)),
        dict(h='Fixed in place', hl=[(5.6, 22.6, 61.4, 7.4), (5.6, 63.6, 61.4, 7)]),
        dict(h='Counted before it is sent', hl=[(86.6, 56.4, 10.6, 4.2), (70.2, 52.4, 20, 3.4)], ctx=(69.5, 10, 28, 1)),
        dict(h='Publishers can be wrong', hl=[(61.4, 24.6, 5.6, 4.4), (61.4, 64.8, 5.6, 4.4)], ctx=(18, 24, 49, 1))], [IMG_REJ],
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
        dict(h='Learns from rejections', hl=[(76, 16, 22, 10.6)], ctx=(76, 12.5, 22, 1)),
        dict(h='Rules and AI stay apart', hl=[(76.8, 23.2, 6.4, 2.4), (76.8, 36.6, 6.4, 2.4), (76.8, 49.9, 6.4, 2.4)], ctx=(76, 12.5, 22, 1)),
        dict(h='Nothing written on its own', hl=[(95.2, 17, 2.6, 3.2), (95.2, 28.5, 2.6, 3.2), (95.2, 41.9, 2.6, 3.2)], ctx=(76, 12.5, 22, 41))], [IMG_EP2],
        after=sub('Rules and AI, side by side', 'Rule checks pass or fail. AI suggestions name their evidence, and a dismissed flag stays on record.') + media_box(EMB('e76ad60f'))))
    o.append(zoom(6, F[5], [
        dict(h='Matched on upload', m=0, hl=[(75.6, 46, 22.2, 7.2)], ctx=(75.6, 11, 22.2, 1)),
        dict(h='One line of results', m=0, hl=[(74.6, 87, 23.8, 11.2)]),
        dict(h='Drop more any time', m=1, hl=[(27.2, 5.6, 45.8, 21.2)]),
        dict(h='Files have their own states', m=2, hl=[(62.2, 30.6, 18.6, 26.4)], ctx=(5, 20.5, 80, 1))], [IMG_UP15, IMG_UP3, IMG_AS],
        after=sub('The whole upload', 'From the drop to the files that need the editor.') + media_box(EMB('2f6c4fe9'))))
    o.append(zoom(7, F[6], [
        dict(h='Completeness per title', hl=[(88.8, 71.6, 9.8, 28.4)], ctx=(60, 66, 1, 1)),
        dict(h='Two views, two filters', hl=[(5.2, 66.4, 53, 4.6), (87.4, 66.6, 11.2, 4.2)])], [IMG_AS],
        after=sub('Switching views and filters', 'Content and Files, then Language and Type as filters.') + media_box(EMB('8364b5b0'))))
    o.append(zoom(8, F[7], [
        dict(h='One thumbnail per taste', hl=[(6.2, 44, 66.4, 20.4)], ctx=(6.2, 40.5, 1, 1)),
        dict(h='Tested per region', hl=[(55.4, 40.4, 17.4, 3.2), (33, 59.6, 6, 2.8), (49.8, 59.6, 6, 2.8), (66.6, 59.6, 6, 2.8)]),
        dict(h='Backed by click-through', hl=[(6.2, 59.2, 15.8, 5), (22.8, 61.2, 4.4, 2.4), (39.6, 61.2, 4.4, 2.4), (56.4, 61.2, 4.4, 2.4)], ctx=(6.2, 40.5, 1, 1))], [IMG_SEASON]))
    o.append(simple(9, F[8], EMB('1ee3cd39')))
    o.append(simple(10, F[9], EMB('59ab0c6b')))
    return ''.join(o)

# ---------- research: findings with a small product visual each ----------
def crop(img, w, h, x0, y0, x1, y1, alt):
    """a part of a real screen, as a background crop (coordinates in % of the image)"""
    cw, ch = x1 - x0, y1 - y0
    pos = lambda v, c: 0 if c >= 100 else v / (100 - c) * 100
    return (f'<div class="rs-v" role="img" aria-label="{alt}" style="aspect-ratio:{cw * w / 100:.0f}/{ch * h / 100:.0f};'
            f'background-image:url({GH}shots/{img});background-size:{10000 / cw:.2f}% auto;background-position:{pos(x0, cw):.2f}% {pos(y0, ch):.2f}%"></div>')

def research():
    def card(vis, finding, decision):
        return (f'<div class="rs-c">{vis}<div class="rs-t"><p class="rs-k">Finding</p><p>{finding}</p>'
                f'<p class="rs-k rs-d">Decision</p><p class="rs-dec">{decision}</p></div></div>')
    a = crop('ep2-shell.webp', 2880, 1800, 3.5, 0, 45, 23.5, 'Episode 2 header with the breadcrumb Content library, Lupin, Season 4, Episode 2')
    b = crop('thumbnails.webp', 2880, 1800, 58.5, 7, 99, 30, 'Spain selected as the region, with readiness in Spain beside it')
    c = crop('reject-v2.webp', 1846, 1154, 68.5, 9, 98.5, 26, 'Rejection reasons: Age rating under Compliance, with the publisher comment')
    return ('<div class="bl2-t"><span class="cs-num bl2-x">03</span><div class="bl2-head"><div><p class="k">Research</p>'
            '<h2 class="bl2-h cs-title">What the domain taught me, and what it changed</h2></div>'
            '<p class="lead">CMS tools are built in-house and rarely shown, so I studied products that each solve part of the job, and one from outside media: code review on GitHub.</p></div>'
            '<div class="rs-g">'
            + card(a, 'Mistakes come from structure the editor can’t see, like metadata on the wrong level.', 'Every field shows the level it lives on.')
            + card(b, 'Almost every field changes by region, from title to audio.', 'Region comes first. Everything under it shows for that region only.')
            + card(c, 'Every tool lets you comment on a field. None turns a rejection into data.', 'A rejection is a list of reasons, pinned to fields and counted.')
            + '</div><p class="bl2-strong">The gap: every tool takes comments, none learns from a rejection.</p></div>')

def roles_viewer():
    e = EMB('13941d11')
    T = re.search(r'T=(\{.*?\]\]\})', e, re.S)
    imgs = re.search(r'<div class="blr-stage">(.*?)</div></div><script>', e, re.S).group(1)
    sel = lambda k: ' aria-selected="true"' if k == 'ed-work' else ' aria-selected="false" tabindex="-1"'
    tab = lambda k, t, full: f'<button class="blr-t" role="tab" data-k="{k}" aria-label="{full}"{sel(k)}>{t}</button>'
    bar = ('<div class="blr-bar" role="tablist" aria-label="Screen">'
           '<div class="blr-grp" role="presentation"><span class="blr-g">Editor</span>' + tab('ed-dash', 'Dashboard', 'Editor dashboard') + tab('ed-work', 'Workspace', 'Editor workspace') + '</div>'
           '<div class="blr-grp" role="presentation"><span class="blr-g">Publisher</span>' + tab('pub-dash', 'Dashboard', 'Publisher dashboard') + tab('pub-work', 'Reviews', 'Publisher reviews') + '</div></div>')
    return (f'<div class="blr" data-blr><div class="blr-fs"><div class="blr-l">{bar}'
            f'<div class="blr-txt"><p class="blr-c" aria-live="polite"></p><div class="blr-rs"></div></div>'
            f'<button type="button" class="blr-full" data-fs>{FULL_IC}<span>Full screen</span></button></div>'
            f'<div class="blr-stage">{imgs}</div></div>'
            f'<script type="application/json" class="blr-data">{T.group(1)}</script></div>')

def changed():
    story = ('<div class="bl2-t"><span class="cs-num bl2-x">06</span><p class="k">What I changed</p>'
             '<h2 class="bl2-h cs-title">Why I moved from a single rejection modal to field-pinned reasons</h2>'
             '<div class="bl2-split bl2-split-first"><p class="k">The first version</p><div><p>The first version allowed one rejection reason per item, and I caught myself labelling rejected items “Multiple Issues”. '
             'That label was a symptom, not a reason, so reasons became a list, each pinned to a field and resolvable on its own.</p></div></div></div>')
    return (story + media_box(EMB('8a2ee889'))
            + '<div class="bl2-t">' + sub('What I took out', 'Most of what I added stayed. Four things didn’t.') + '</div>' + P['CARDS'])

def north_star():
    h = P['1f11a2c4-c927-6c80-452e-1af7129ee08d']
    lead = re.search(r'<div class="bl2-nst">.*?<p>(.*?)</p></div>', h, re.S).group(1)
    lead = lead.replace(' Each feature below shows which part of the loop it cuts.', '')
    a = h.index('<div class="bl2-ns">'); b = h.index('<div class="bl2-split">')
    return h[:a] + f'<p class="lead">{lead}</p>' + h[b:]

def sec(k, label, inner):
    return f'<section data-bl2="{k}" data-nav-label="{label}">{inner}</section>'

def backlot():
    w1 = (sec('ov', 'Overview', P['411a7ea2-ad8e-e2d4-3a36-2ddce0bbd66d'])
          + sec('pr', 'The problem', P['cf0faf68-fe6a-067e-c1f5-2da983ff1039'] + media_box(EMB('08e54bfa')))
          + sec('ns', 'North star', north_star())
          + sec('rs', 'Research', research() + media_box(EMB('c3c045d7')))
          + sec('ro', 'Two roles', P['a5644849-2272-9536-b83b-9657f2bbdb98'] + roles_viewer())
          + sec('fe', 'Features', features())
          + sec('ch', 'What I changed', changed()))
    ds = ds_build().replace('Lupin, S4-E2', 'Lupin · S4-E2').replace('Community, S6-E6', 'Community · S6-E6').replace('Long Story Short, S1-E3', 'Long Story Short · S1-E3') \
        .replace('Crime, Drama', 'Crime · Drama').replace('Edit requested, waiting', 'Edit requested · waiting').replace('Editor, Alex', 'Editor · Alex').replace('Publisher, Maya', 'Publisher · Maya')
    w2 = sec('re', "What's next", P['c2545a3c-0f01-ab8f-4f5f-45336f755274'])
    nb = P['78fe6fd2-fd22-0eb4-d2e4-629e35df69b3'].replace('href="/work"', 'href="/bilge"').replace('Customs approvals where every change carries a reason.', 'Container tracking for Turkish customs, designed from the system specs.')
    body = (f'<main class="bl2-page"><div class="cs-wrap" data-bl2root="1"><nav class="bl-nav" aria-label="Case study sections"><ol></ol></nav>{w1}</div>'
            f'{ds}<div class="cs-wrap" data-bl2root="2">{w2}</div>{nb}</main>')
    return page('Backlot case study | Ege Coskun',
                'Backlot, a B2B SaaS CMS for streaming services: review and approval workflows, region-specific metadata and an AI check that flags likely rejections.',
                body, ['site.css', 'backlot.css'], ['site.js', 'backlot.js'], font='it')

# ---------- BİLGE: same components as Backlot ----------
def ph(label):
    """placeholder until the Claude Design screens are in"""
    return media_box(f'<div class="bl2-ph"><span>{label}</span></div>')

def split(k, html):
    return f'<div class="bl2-split"><p class="k">{k}</p><div>{html}</div></div>'

def rules(items):
    return '<div class="blr-rs">' + ''.join(f'<p>{t}</p>' for t in items) + '</div>'

def head2(n, k, h, lead=''):
    return (f'<span class="cs-num bl2-x">{n:02d}</span><p class="k">{k}</p><h2 class="bl2-h cs-title">{h}</h2>'
            + (f'<p class="lead">{lead}</p>' if lead else ''))

def bilge():
    hero = ('<div class="bl2-t bl2-hero"><span class="cs-num bl2-x">00</span><span class="cs-title bl2-x">Overview</span>'
            '<p class="k">BİLGE, the customs platform of the Turkish Ministry of Trade</p><h1>Tracking every container through Turkish customs, designed from the system specs</h1>'
            '<div class="bl2-hg"><p class="lead">BİLGE is the Ministry of Trade’s customs platform, made of dozens of modules, and I designed across many of them. '
            'This page shows KLTS, container and port tracking, designed from the system specifications and backend rules so every screen offers only what the system allows.</p>'
            '<div class="bl2-meta"><div><b>Company</b>MilSOFT</div><div><b>Client</b>Turkish Ministry of Trade</div>'
            '<div><b>My role</b>UX/UI Designer</div><div><b>Date</b>2022 to 2023</div></div></div>'
            + ph('Hero screen from Claude Design') + '</div>')
    cards = ''.join(f'<div class="bl2-c"><span class="bl2-tag">Decision {i}</span><h3>{t}</h3><p>{d}</p></div>' for i, (t, d) in enumerate([
        ('One form, four roles', 'Agents and customs staff open the same form; what changes is what each can do with it. Blue and red headers separate the agent side from customs.'),
        ('Sources side by side', 'The carrier’s declaration and the port’s records sit next to each other, so a mismatch is visible at a glance.'),
        ('Registering is binding', 'Registering starts the clock on the container’s permitted time in the country, so at the ministry’s request the button says Register. The confirmation shows the registration number and the remaining prepaid balance.')], 1))
    glance = ('<div class="bl2-t"><span class="cs-num bl2-x">01</span><p class="k">At a glance</p><h2 class="bl2-h cs-title">One container, several sources, one form</h2>'
              + split('The problem', '<p>Every container that enters or leaves a Turkish seaport needs a Container Tracking Form. KLTS moved that form, and the records customs, port operators and agencies used to exchange on paper, into one system.</p>'
                      '<p>Up to four people work on one form, and from registration the container’s permitted time is running.</p>')
              + f'<div class="bl2-cards c3">{cards}</div>'
              + split('Constraints', '<p>Legal wording on every label, ministry review on every change, and customs data I can’t show.</p>')
              + '</div>')
    specs = ('<div class="bl2-t">' + head2(2, 'Working from specs', 'Designed from the system specifications',
             'Every screen started from the specs: the analysts’ requirements, the regulation and the backend rules behind each field and status. '
             'An exit can’t be registered without an entry, approval needs enough prepaid balance, and a container can’t leave the port without an approved form. '
             'I designed so the interface never offers an action the backend would refuse.') + '</div>')
    role = ('<div class="bl2-t">' + head2(3, 'My role', 'One module of many',
            'I joined after BİLGE’s design system was in place and worked across many modules. KLTS is the one whose designs I still have.')
            + split('Team', '<p>TODO: team size and who was in it, and who you worked with day to day.</p>')
            + split('What I owned in KLTS', '<p>The agent’s form, the officer’s approval and query flows, time extensions, corrections, cancellations, the container history, the declaration comparison and closing a form with an official report. TODO: number of screens and states.</p>')
            + split('Design system', '<p>TM-22 was created by Dilmin Doğan and Gizem Turan Yücel. I extended it with: TODO.</p>')
            + '</div>')
    def flow(n, k, h, lead, shot, items):
        return ('<div class="bl2-t">' + head2(n, k, h, lead) + '</div>' + ph(shot)
                + ('<div class="bl2-t">' + split('Decisions', rules(items)) + '</div>' if items else ''))
    agent = flow(4, 'The agent files', 'General information first, then the containers',
                 'The agent picks the movement (foreign or domestic, entry or exit), fills in general information, then adds containers one by one or in bulk, each with its parts and equipment. Until an officer approves it, the agent can still edit the form.',
                 'Page A walkthrough: Add Container, Register', [
                     'General information comes first, because every container on the form shares it.',
                     'Parts and equipment sit under their container, so nothing is filed against the wrong one.',
                     'Register, not Save: once sent, the form is binding.'])
    track = flow(5, 'Tracking a container', 'Every source and every event in one place',
                 'Two screens came straight from the specs. One compares the carrier’s summary declaration with the port’s records. The other, the container history, puts every event on one timeline.',
                 'Container lookup (page D) and declaration comparison', [])
    customs = flow(6, 'Customs decides', 'Officers and managers act from their queue',
                   'Officers approve, edit or cancel registered forms; after approval, only customs can change them. Some changes need a second signature: time extensions and cancellations go to the manager, corrections to the deputy manager.',
                   'Pages B and C walkthrough', [
                       'An officer can approve some containers on a form and reject the rest in one step.',
                       'Written reasons open in a side drawer, so the form stays in view.',
                       'Managers decide on the row, and the result appears on the same list.',
                       'Editing a form an agent registered warns that the agent’s record will change.'])
    ba = ('<div class="bl2-t">' + head2(7, 'Before and after', 'Closing a form with an official report',
          'One of the screens I redesigned. TODO: what the old screen made hard, what you changed, and why.') + '</div>'
          + ph('Before and after: old screen and page E'))
    learned = ('<div class="bl2-t">' + head2(8, 'What I learned', 'In government software the wording is part of the design')
               + split('Wording', '<p>A word like Register carries legal weight, so ministry review shaped the design from the start.</p>')
               + split('Next time', '<p>TODO: one thing that went wrong or that you would do differently, and what you changed because of it.</p>')
               + split('How I built this page', '<p>The flows, screens and design system additions are my work at MilSOFT. The real system holds customs data, so I rebuilt the screens in Claude Design from the originals with placeholder data and checked each one against them.</p>')
               + '</div>')
    w1 = (sec('ov', 'Overview', hero) + sec('gl', 'At a glance', glance) + sec('dm', 'Working from specs', specs) + sec('mr', 'My role', role)
          + sec('ag', 'The agent files', agent) + sec('tr', 'Tracking a container', track) + sec('cu', 'Customs decides', customs)
          + sec('ba', 'Before and after', ba) + sec('le', 'What I learned', learned))
    nb = (P['78fe6fd2-fd22-0eb4-d2e4-629e35df69b3'].replace('href="/work"', 'href="/uwaverde"')
          .replace('<span>BİLGE</span>', '<span>UwaVerde</span>')
          .replace('Customs approvals where every change carries a reason.', 'NGO website and member portal.')
          .replace('<b>Pending Approval</b>', '<b>Member portal</b>'))
    body = f'<main class="bl2-page"><div class="cs-wrap" data-bl2root="1"><nav class="bl-nav" aria-label="Case study sections"><ol></ol></nav>{w1}</div>{nb}</main>'
    return page('BİLGE container tracking case study | Ege Coskun',
                'BİLGE KLTS: container and port tracking for Turkish customs. Approval chains across agents, officers and managers, built on an existing design system.',
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
    emb_css = ''.join(re.findall(r'<style>(.*?)</style>', EMB('08e54bfa') + EMB('c3c045d7') + EMB('13941d11') + EMB('f6fe44e7') + EMB('020e6363'), re.S))
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
    write('assets/backlot.js', nav_js + '\n' + rd('bl2.js') + '\n' + vid_js + '\n' + rd('zoom.js') + '\n' + rd('roles.js') + '\n' + rd('pace.js'))
    write('assets/site.js', rd('site.js'))
    html = backlot()
    a, b = html.index('<main'), html.index('</main>')
    html = html[:a] + re.sub(r'<style>.*?</style>', '', html[a:b], flags=re.S) + html[b:]
    write('backlot/index.html', html)
    write('bilge/index.html', bilge())
    print('built', len(html))
