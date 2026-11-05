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

LOGO = GH + 'logos/ege-coskun.png'
FULL_IC = '<svg width="14" height="14" viewBox="0 0 24 24" aria-hidden="true"><path d="M4 9V4h5M20 9V4h-5M4 15v5h5M20 15v5h-5" fill="none" stroke="currentColor" stroke-width="2"/></svg>'

def page(title, desc, body, css_files, js_files, font='it', cur='work'):
    css = ''.join('<link rel="stylesheet" href="../assets/%s">' % c for c in css_files)
    js = ''.join('<script src="../assets/%s" defer></script>' % j for j in js_files)
    fl = '<link href="https://fonts.googleapis.com/css2?family=Inter+Tight:wght@400;500;600;700;800&family=Reenie+Beanie&display=swap" rel="stylesheet">' if font else ''
    return f'''<!doctype html><html lang="en"{' class="f-it"' if font else ''}><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet">{fl}{css}</head><body class="case">
<header class="site-h"><div class="site-hi"><a class="site-logo" href="/" aria-label="Ege Coskun, home" style="--lg:url({LOGO})"><img src="{LOGO}" alt="Ege Coskun" width="140" height="23"><i class="site-lm" aria-hidden="true"></i></a>
<nav class="site-n" aria-label="Main"><a href="/#work"{' aria-current="page"' if cur == 'work' else ''}>Work</a><a href="/about"{' aria-current="page"' if cur == 'about' else ''}>About</a><a href="#contact">Contact</a></nav></div></header>
{body}
<footer class="finalfooter" id="contact">{rem(rd('foot.html'))}</footer>{js}</body></html>'''

# ---------- building blocks ----------
def strip(on):
    return '<div class="bl2-strip">Cuts the loop at ' + '<b>→</b>'.join(
        '<i class="on">%s</i>' % x if x == on else '<i>%s</i>' % x for x in ['Deliver', 'Prepare', 'Review', 'Release']) + '</div>'

NOTE_ARROW = '<svg viewBox="0 0 96 56" aria-hidden="true"><path class="nb" d="M90 22 C 70 44, 34 40, 13 20" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/><path class="nh" d="M26.5 23.8 L13 20 L17.4 33.3" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg>'
NOTE_DOWN = '<svg viewBox="0 0 60 72" aria-hidden="true"><path class="nb" d="M8 8 C 32 10, 50 30, 44 64" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/><path class="nh" d="M34 54 L44 65 L52 52" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg>'
def head(n, f, nav=False, note=''):
    hid = '<span class="cs-num bl2-x">03</span><span class="cs-title bl2-x">Features</span>' if nav else ''
    h2 = f'<h2 class="bl2-h">{f["t"]}</h2>'
    if note:  # a handwritten aside next to the title, drawn in when it scrolls into view
        h2 = f'<div class="bl2-hn"><h2 class="bl2-h">{f["t"]}</h2><span class="bl2-note" data-note aria-hidden="true">{NOTE_ARROW}<b>{note}</b></span></div>'
    return f'{hid}<p class="k">Feature {n:02d}</p>{h2}<p class="lead">{f["l"]}</p>'

def media_box(inner):
    cls = ''
    if re.search(r'proto/(rejection|region)/', inner):  # clickable prototypes carry a green stroke
        cls = ' is-proto'
    return f'<div class="bl2-media{cls}">{inner}</div>'

def sub(title, text='', note=''):
    """small heading that says what the next media shows; note adds a handwritten pointer down to it"""
    h3 = f'<h3>{title}</h3>'
    if note:
        return (f'<div class="bl2-subh"><div class="bl2-sw">{h3}' + (f'<p>{text}</p>' if text else '')
                + f'<span class="bl2-note down" data-note aria-hidden="true"><b>{note}</b>{NOTE_DOWN}</span></div></div>')
    return f'<div class="bl2-subh">{h3}' + (f'<p>{text}</p>' if text else '') + '</div>'

ZCAP = 1.5
PADX, PADY = 0.6, 0.96  # breathing room around every highlight, equal in pixels on a 1.6 screen
def padbox(b):
    x, y, w, h = b
    x0, y0 = max(0.25, x - PADX), max(0.4, y - PADY)
    x1, y1 = min(99.6, x + w + PADX), min(99.3, y + h + PADY)
    return (round(x0, 2), round(y0, 2), round(x1 - x0, 2), round(y1 - y0, 2))
def fit(s):
    """z, x, y from the highlight boxes plus an optional context box (ctx) that must stay in view, e.g. a heading."""
    if 'z' in s:
        return s
    bs = list(s.get('hl', [])) + ([s['ctx']] if 'ctx' in s else [])
    x0 = min(b[0] for b in bs); y0 = min(b[1] for b in bs)
    x1 = max(b[0] + b[2] for b in bs); y1 = max(b[1] + b[3] for b in bs)
    z = max(1, min(ZCAP, 85 / max(x1 - x0, y1 - y0)))
    return dict(s, z=round(z, 2), x=round((x0 + x1) / 2, 1), y=round((y0 + y1) / 2, 1))

def zoom(n, f, steps, medias, after='', nav=False, head_html=None, note='', show_hl=True):
    """Steps that move the screen. Each step can switch media (m), seek a video (t), zoom to a point (z, x, y in %)
    and highlight boxes (hl: list of (x, y, w, h) in % of the media). The text and the screen stay pinned while
    scrolling moves through the steps."""
    steps = [fit(dict(s, hl=[padbox(b) for b in s.get('hl', [])])) for s in steps]
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
                      for si, s in enumerate(steps) if show_hl and s.get('m', 0) == i for (x, y, w, h) in s.get('hl', []))
        ms += f'<div class="zs-mw{on}" data-i="{i}">{el}{hls}</div>'
    bars = ''.join(f'<button type="button" aria-label="Step {i+1}"><i></i></button>' for i in range(len(steps)))
    has_video = any(m['type'] == 'video' for m in medias)
    ctl = ('<button type="button" class="zs-play" data-zplay><svg width="14" height="14" viewBox="0 0 24 24" aria-hidden="true"><path d="M8 5v14l11-7z" fill="currentColor"/></svg>'
           '<span>Play the whole video</span></button>') if has_video else ''
    hd = head_html if head_html is not None else head(n, f, nav=nav, note=note)
    return (f'<div class="bl2-t bl2-f{" first" if nav else ""}">{hd}<div class="zs" data-zs style="--n:{len(steps)}"><div class="zs-pin"><ol class="zs-steps">{lis}</ol>'
            f'<div class="zs-stick"><div class="zs-frame"><div class="zs-view" style="aspect-ratio:{medias[0]["w"]}/{medias[0]["h"]}">{ms}</div></div>'
            f'<div class="zs-foot"><div class="zs-bar">{bars}</div>{ctl}</div></div></div></div>{after}</div>')

IMG_SEASON = dict(type='img', src=GH + 'shots/v2/season-assets.webp?v=5', w=2738, h=1712, alt='Season 4 in Spain: region selector, readiness panel, personalized thumbnails')
IMG_EP2 = dict(type='img', src=GH + 'shots/v2/ep2.webp?v=4', w=2880, h=1800, alt='Episode 2 metadata page: needs your input, values from the delivery, AI flags')
IMG_REJ = dict(type='img', src=GH + 'shots/v2/reject.webp?v=4', w=2880, h=1800, alt='Publisher review of Sherlock Holmes: two flagged rows and a list of two rejection reasons')
IMG_UP3 = dict(type='img', src=GH + 'shots/v2/upload-modal.webp?v=4', w=2738, h=1712, alt='Upload drop zone open over the assets list')
IMG_UP15 = dict(type='img', src=GH + 'shots/v2/upload-widget.webp?v=4', w=2738, h=1712, alt='Season 4 in Spain with the upload result in the corner and 15 files waiting in the readiness panel')
IMG_AS = dict(type='img', src=GH + 'shots/v2/assets.webp?v=4', w=2738, h=1712, alt='Assets: the delivery batch with a state per file, and the content list with completeness per title')
VID_UP = dict(type='video', src=GH + 'upload.mp4?v=23', poster=GH + 'posters/upload.jpg?v=23', w=2054, h=1284)
VID_AS = dict(type='video', src=GH + 'assets-filters.mp4?v=23', poster=GH + 'posters/assets-filters.jpg?v=23', w=2054, h=1284)

def changed():
    story = ('<div class="bl2-t"><span class="cs-num bl2-x">04</span><p class="k">What I changed</p>'
             '<h2 class="bl2-h cs-title">Why I moved from a single rejection modal to field-pinned reasons</h2>'
             '<div class="bl2-split bl2-split-first"><p class="k">The first version</p><div><p>The first version allowed one rejection reason per item, and I caught myself labelling rejected items “Multiple Issues”. '
             'That label said something was wrong without saying what, so reasons became a list, each pinned to a field and resolvable on its own.</p></div></div></div>')
    return (story + media_box(EMB('8a2ee889'))
            + '<div class="bl2-t">' + sub('What I took out', 'Most of what I added stayed. Four things didn’t.') + '</div>' + P['CARDS'])

def hero():
    h = P['411a7ea2-ad8e-e2d4-3a36-2ddce0bbd66d']
    rep = [('<b>Category</b>B2B SaaS, Enterprise CMS', '<b>Category</b>B2B SaaS, Streaming CMS'), ('<h1>Rejections that tell the editor exactly what to fix</h1>', '<h1>From delivery to release, one region at a time</h1>'),
           ('<p class="lead">Backlot is where streaming services prepare films and series for release, one region at a time. I designed the review loop between editor and publisher, so a rejection is a list of reasons pinned to fields, not a vague note.</p>',
            '<p class="lead">Streaming teams use Backlot to take films and series from delivery to release, region by region. I designed the whole workflow for both sides: dashboards, upload and file matching, fields that fill from the file, the publisher’s review and artwork tests.</p>'),
           ('<b>Context</b>Solo concept. The take-home that got me hired for my last role, rebuilt and extended.', '<b>Context</b>The take-home that got me hired for my last role, rebuilt and extended.'),
           ('<b>Date</b>2026', '<b>Date</b>2026, 3 weeks')]
    for o, n in rep:
        assert o in h, o[:40]
        h = h.replace(o, n)
    return h.replace(GH + 'shots/roles/ed-dashboard.webp', GH + 'shots/v2/ed-dashboard.webp?v=4')

MINI = '<i></i><b>Pending Approval</b><u></u><u></u><u></u>'
PROJ = [('backlot', 'Backlot', 'From delivery to release, one region at a time.', GH + 'shots/v2/ed-dashboard.webp?v=4'),
        ('bilge', 'BİLGE', 'Container tracking for Turkish customs, designed from the system specs.', GH + 'shots/bilge/b-queue-th.webp'),
        ('data-health', 'Data health', 'Telling marketers which data to trust before they build a segment.', GH + 'shots/dh/thumb.webp'),
        # ('uwaverde', 'UwaVerde', 'A website and member portal for&nbsp;an<br>NGO I co-founded.', 'https://s3.amazonaws.com/webflow-prod-assets/67a7e306e38056dfa249a42d/691de9a378fcaab7283af4c8_HomePage%20(1)%20(1)-p-1080.png')
        ]
def nextblock(cur):
    """next project as a sentence with its screen, then every project small, then the footer"""
    i = [p[0] for p in PROJ].index(cur); n = (i + 1) % len(PROJ); k, name, d, img = PROJ[n]
    ARW = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 12h15M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>'
    tiles = ''.join(f'<li><a href="/{pk}"' + (' aria-current="page"' if pk == cur else '') + f'><span><img src="{pi}" alt="" loading="lazy"></span><b>{j + 1:02d} / {pn}</b></a></li>'
                    for j, (pk, pn, _, pi) in enumerate(PROJ))
    return (f'<section class="nx" aria-label="Next project"><a class="nx-a" href="/{k}"><p class="nx-k">Next, {n + 1:02d} / {name}</p>'
            f'<div class="cs-wrap nx-in"><p class="nx-d">{d}</p><span class="nx-go">Read the case study {ARW}</span></div>'
            f'<span class="nx-im" aria-hidden="true"><img src="{img}" alt="" loading="lazy"></span></a>'
            f'<div class="nx-all"><p class="nx-l">All work</p><div class="cs-wrap"><ul>{tiles}</ul></div><a class="nx-top" href="#">Back to the top</a></div></section>')

def nbthumb(html, src, alt=''):
    assert MINI in html
    return html.replace(MINI, f'<img src="{src}" alt="{alt}" loading="lazy">')

def sec(k, label, inner):
    return f'<section data-bl2="{k}" data-nav-label="{label}">{inner}</section>'

def backlot():
    w1 = (sec('ov', 'Overview', hero())
          + sec('pr', 'Why it’s slow', problem() + north_star() + research())
          + sec('ro', 'Two roles', roles())
          + sec('fe', 'Features', features())
          + sec('ch', 'What I changed', changed()))
    ds = ds_build().replace('Lupin, S4-E2', 'Lupin · S4-E2').replace('Community, S6-E6', 'Community · S6-E6').replace('Long Story Short, S1-E3', 'Long Story Short · S1-E3') \
        .replace('Crime, Drama', 'Crime · Drama').replace('Edit requested, waiting', 'Edit requested · waiting').replace('Editor, Alex', 'Editor · Alex').replace('Publisher, Maya', 'Publisher · Maya')
    w2 = sec('re', "What's next", P['c2545a3c-0f01-ab8f-4f5f-45336f755274'])
    nb = nextblock('backlot')
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

def still(n, f, steps, medias, after='', nav=False, note=''):
    """one screen and the points as numbered cards under it, for features where scrolling through steps adds nothing"""
    m = medias[0]
    img = f'<img class="bl2-img" src="{m["src"]}" width="{m["w"]}" height="{m["h"]}" alt="{m["alt"]}" loading="lazy">'
    cards = ''.join(f'<div class="bl2-c"><span class="bl2-tag">{i:02d}</span><h3>{s["h"]}</h3><p>{t}</p></div>' for i, (s, t) in enumerate(zip(steps, f['r']), 1))
    cls = ' c3' if len(steps) == 3 else ''
    return f'<div class="bl2-t bl2-f">{head(n, f, nav=nav, note=note)}{media_box(img)}<div class="bl2-cards{cls}">{cards}</div>{after}</div>'

def simple(n, f, media, nav=False, after=''):
    return f'<div class="bl2-t bl2-f{" first" if nav else ""}">{head(n, f, nav=nav)}{media_box(media)}{after}</div>'

IMG_ED_DASH = dict(type='img', src=GH + 'shots/v2/ed-dashboard.webp?v=4', w=2880, h=1800, alt='Editor dashboard: unassigned files banner, counts, items in progress, upcoming releases, activity and what is blocking')
IMG_PUB_DASH = dict(type='img', src=GH + 'shots/v2/pub-dashboard.webp?v=4', w=2880, h=1800, alt='Publisher dashboard: what airs this week, review counts, pending review, upcoming releases and deliveries this week')
IMG_ED_WORK = dict(type='img', src=GH + 'shots/v2/ed-workspace.webp?v=4', w=2880, h=1800, alt='Editor workspace: workflow table filtered by status, rejections as cards, uploads panel in the corner')
IMG_PUB_WORK = dict(type='img', src=GH + 'shots/v2/pub-reviews.webp?v=5', w=2880, h=1800, alt='Publisher reviews: review queue by status and review history')

def features():
    """Nine features, most telling first, with an index so a skimmer sees all nine at once."""
    F = []
    # region (the old series tree folds in here)
    f = dict(t='Treating region as a structural scope, not just a filter',
             l='Title, synopsis, age rating, dates, rights, audio and subtitles all change by region. The editor picks a region first, and the whole page answers for it.')
    F.append(lambda n, nav: simple(n, f_region, EMB('faf58225'), nav=nav,
                    after=split('Every level', '<p>Series, season, episode and file each keep their own fields and status, so the editor can tell which level a change affects. '
                                'Age rating rolls up: a season takes the highest rating among its episodes in that region.</p>')))
    f_region = f
    # the editor only fills what is missing
    f_fill = dict(t='The editor only fills what is missing',
             l='Runtime, codec and audio are read from the file, and the delivery fills most of the rest. What is still missing sits at the top of the page.',
             r=['Every empty field is grouped in “Needs your input”, above what the upload already filled.',
                'Values from the delivery are locked. Each field unlocks on its own, so every change is deliberate.',
                'Submit hands the episode to the publisher. Save keeps it under In progress, ready to pick up later.',
                '“4 of 8” tells the editor how much is left and where to start. “Incomplete” would only say something is wrong.',
                'The season page lists what must be complete before the season can be scheduled.'])
    F.append(lambda n, nav: zoom(n, f_fill, [
        dict(h='Gaps come first', m=1, hl=[(5.4, 25, 67.2, 33.4)]),
        dict(h='Locked by its source', m=1, hl=[(5.4, 63.6, 67.2, 30.4)]),
        dict(h='Save is not submit', m=1, hl=[(62.8, 9, 9.8, 4.4), (66.6, 95.5, 5.8, 2.5)]),
        dict(h='Progress you can count', m=0, hl=[(76.6, 21, 21.2, 16.6)], ctx=(76, 10.5, 22, 1)),
        dict(h='Readiness for the season', m=0, hl=[(59.4, 9.2, 38.4, 8)])], [IMG_SEASON, IMG_EP2],
        after=sub('A season keeps its own metadata, apart from its episodes', 'Episodes, season metadata, season assets, deliveries per region and the audit log, with the readiness panel in view on every tab.') + media_box(EMB('137e3b55')), nav=nav))
    # upload, the unhappy path
    f_up = dict(t='Designed for the delivery that arrives broken',
             l='Deliveries often arrive incomplete or mislabelled. The design starts from that case, so a broken delivery never blocks the files that are fine.',
             r=['Processing reads each file’s technical metadata and links it to its episode. Files it can’t place go to Needs assignment.',
                'The upload folds into a panel in the corner, so the editor can open other pages and come back to it.',
                'The drop zone stays open, so files can be added while others are still uploading.',
                'Uploading, Processing, Ready, Needs assignment and Failed belong to the file, apart from the episode’s workflow status.'])
    F.append(lambda n, nav: zoom(n, f_up, [
        dict(h='Processing assigns what it can', m=0, hl=[(76.2, 46.6, 21.4, 6.8)], ctx=(76, 11, 22, 1)),
        dict(h='Keep working while it uploads', m=0, hl=[(74.8, 87.2, 23.6, 11.6)], ctx=(60, 60, 1, 1)),
        dict(h='Add files mid-upload', m=1, hl=[(28.4, 7.6, 43.4, 18)]),
        dict(h='Each file has its own state', m=2, hl=[(62.4, 30.2, 17.4, 27.4)], ctx=(5, 26.5, 75, 1))], [IMG_UP15, IMG_UP3, IMG_AS],
        after=sub('Resolving the files processing couldn’t place', 'Each problem gets its own fix: assign files in bulk, keep or replace a duplicate master, or create the episode a file points to.') + media_box(EMB('2f6c4fe9')),
        note='unhappy path', nav=nav))
    # rejection
    f_rej = dict(t='A rejection is a list of reasons',
             l='The publisher approves an item, or sends it back with reasons the editor can act on one by one. Each reason is pinned to its field.',
             r=['The publisher comments on the metadata row itself. Each comment becomes a reason with its field and a category.',
                'A flagged row stays marked on the page with the publisher’s note, so the editor fixes it in place.',
                'Before anything is sent, Reject shows how many reasons there are and who gets the item back.'])
    F.append(lambda n, nav: still(n, f_rej, [
        dict(h='Comments become reasons', hl=[(70, 15, 27.6, 30)], ctx=(70, 11, 28, 1)),
        dict(h='Fixed in place', hl=[(5.8, 75.6, 61.4, 5.4)]),
        dict(h='Counted before it is sent', hl=[(69.8, 52.6, 27.6, 8)])], [IMG_REJ],
        after=sub('Try it', 'Flag two fields as the publisher, then fix them as the editor.') + media_box(EMB('f663202a')), nav=nav))
    # AI
    f_ai = dict(t='AI suggests, the editor accepts',
             l='The AI points at likely rejections before the publisher sees them and proposes values like keywords. Nothing is written until the editor accepts.',
             r=['Suggestions come from past rejection reasons. Each reason carries a field and a category, so they can be counted per team and per region.',
                'Automatic checks pass or fail by rule. The AI sits apart and only raises judgement calls, saying how sure it is.',
                'Accept writes the value, Dismiss asks for a reason. Either way, the decision stays in the activity log.'])
    F.append(lambda n, nav: still(n, f_ai, [
        dict(h='Built on past rejections', hl=[(76, 55.6, 22, 9.6)], ctx=(76, 50, 22, 1)),
        dict(h='Rules and AI stay apart', hl=[(77.4, 21, 20.4, 16), (76, 55.6, 22, 9.6)]),
        dict(h='Nothing written on its own', hl=[(95.2, 55.2, 2.8, 3.8), (76.8, 62.8, 7, 2.4)], ctx=(76, 50, 22, 1))], [IMG_EP2],
        after=sub('Rules and AI, side by side', 'Rule checks pass or fail. AI suggestions name their evidence and how sure they are.') + media_box(EMB('e76ad60f')), nav=nav))
    # artwork
    f_art = dict(t='Artwork is chosen by taste, not by country',
             l='Most viewing starts from a recommendation, so the thumbnail does much of the selling. Taste predicts a click better than age or location, so each season carries one thumbnail per taste cluster. <span class="bl2-src">Sources: <a href="https://fortune.com/2016/03/27/netflix-predicts-taste/" target="_blank" rel="noopener">Netflix on taste clusters, Fortune</a>, <a href="https://www.dezeen.com/2017/12/20/netflix-targets-film-artwork-depending-users-viewing-habits-design-technology/" target="_blank" rel="noopener">Netflix on personalised artwork, Dezeen</a>.</span>',
             r=['Action, drama, romance and mystery fans each see the scene most likely to make them click.',
                'Variants are tested against each other in each region, with the time left on the test, so the editor knows when the artwork is final.',
                'Each variant shows its click-through rate, and the leader is marked.'])
    F.append(lambda n, nav: still(n, f_art, [
        dict(h='One thumbnail per taste', hl=[(6.2, 44.4, 66.4, 19.6)], ctx=(6.2, 41, 1, 1)),
        dict(h='A/B tested per region', hl=[(55.4, 40.6, 17.4, 2.8), (33.4, 60, 5.6, 2.6), (50.2, 60, 5.6, 2.6), (67, 60, 5.6, 2.6)]),
        dict(h='Backed by click-through', hl=[(6.2, 59.6, 15.8, 3.6), (23, 61.4, 4.4, 2.2), (39.8, 61.4, 4.4, 2.2), (56.6, 61.4, 4.4, 2.2)], ctx=(6.2, 41, 1, 1))], [IMG_SEASON], nav=nav))
    # row actions
    f_row = dict(t='Each row offers only its next step',
             l='Review while an episode waits, Publish once it’s approved: each row shows only the action its status allows.')
    F.append(lambda n, nav: simple(n, f_row, EMB('1ee3cd39'), nav=nav))
    # assets
    f_as = dict(t='Every file sits under the content it belongs to',
             l='A missing file shows as a gap on its film or episode, before the delivery gets rejected.',
             r=['Each film or episode shows how complete its files are, like 2 of 7.',
                'Content groups files under their film or episode; Files lists them all for bulk work. Language and type are filters.'])
    F.append(lambda n, nav: still(n, f_as, [
        dict(h='A file count on every row', hl=[(83.6, 72, 12.4, 26.4)]),
        dict(h='Two views, two filters', hl=[(5.4, 67, 93, 4.2)])], [IMG_AS],
        after=sub('Filtering down to one delivery', 'Content narrows the list to Lupin, Files lists every file in it, and the batch filter finds the files from one delivery.') + media_box(EMB('8364b5b0')), nav=nav))
    # locked
    f_lock = dict(t='Once review starts, content is locked',
             l='While the publisher reviews, every field is read-only. After approval, a change needs an edit request: it is meant for news from outside, like a new regional age rating, and it reopens one section at a time.')
    F.append(lambda n, nav: simple(n, f_lock, EMB('59ab0c6b'), nav=nav))
    titles = [f_region['t'], f_fill['t'], f_up['t'], f_rej['t'], f_ai['t'], f_art['t'], f_row['t'], f_as['t'], f_lock['t']]
    ix = ''.join(f'<li><a href="#f-{i}"><em>{i:02d}</em><span>{t}</span></a></li>' for i, t in enumerate(titles, 1))
    index = ('<div class="bl2-t"><span class="cs-num bl2-x">03</span><span class="cs-title bl2-x">Features</span><p class="k">Features</p>'
             '<h2 class="bl2-h">Nine decisions across the workflow</h2>'
             f'<ol class="fx-ix">{ix}</ol></div>')
    short = ['Region scope', 'Missing fields', 'Broken deliveries', 'Rejections', 'AI suggestions', 'Artwork', 'Row actions', 'Files', 'Locking']
    return index + ''.join(f'<div id="f-{i}" class="fx-a" data-nav-sub="{short[i-1]}">' + mk(i, False) + '</div>' for i, mk in enumerate(F, 1))

# ---------- problem, built on what the research found ----------
def problem():
    cards = ''.join(f'<div class="bl2-c"><span class="bl2-tag">Finding</span><h3>{t}</h3><p>{d}</p></div>' for t, d in [
        ('Files arrive broken', 'Deliveries come with missing, extra or mislabelled files, and each one has to be matched to its episode by hand.'),
        ('Almost every field changes by region', 'Title, synopsis, age rating, release date, rights, audio and subtitles each need their own version per region.'),
        ('Mistakes hide in the structure', 'Metadata entered on the wrong level, a season instead of an episode, only shows up at review.'),
        ('Feedback doesn’t point at a field', 'Most tools let a reviewer comment, but a rejection is still a note. The editor has to work out which field it means.')])
    return ('<div class="bl2-t"><span class="cs-num bl2-x">01</span><span class="cs-title bl2-x">The problem</span>'
            '<p class="bl2-big" data-tint style="--ac:#9184D9"><span class="bl2-line">The work is not hard.</span><span class="bl2-line">The loop is.</span></p>'
            + split('The problem', '<p>Getting one episode ready for one region means matching its files, filling about forty fields and passing a publisher’s review. '
                    'Much of it is typing what the file already says, and mistakes only surface at review, where each one costs a round.</p>')
            + f'<div class="bl2-cards">{cards}</div></div>')

def north_star():
    return ('<div class="bl2-t bl2-part"><p class="k">North star</p>'
            '<h2 class="bl2-h cs-title">Release-ready sooner, with less typing</h2>'
            '<p class="lead">Every decision on this page answers one question: does it get an episode release-ready sooner, with less typing and fewer rounds of review?</p>'
            + split('The bet', '<p>My bet: most of the delay is retyping and rework. In my design of Episode 2, the editor types 5 of its 41 fields; the file, the delivery and the season fill the rest. If feedback also points at fields, time to release-ready drops. I haven’t tested it with an editor yet.</p>')
            + '</div>')

# ---------- research: how I looked, and the benchmark ----------
DOT = {'y': '<i class="bd bd-y" role="img" aria-label="yes"></i>', 'n': '<i class="bd bd-n" role="img" aria-label="no"></i>'}
def benchmark():
    cols = ['Versions per language', 'Built-in approval workflow', 'Comments on a field or frame', 'Reads duration and codec from the file', 'Automatic checks before review']
    rows = [('Contentful', 'Headless CMS', 'yyyny'), ('Contentstack', 'Headless CMS', 'yyyny'), ('Strapi', 'Headless CMS', 'yynny'),
            ('Directus', 'Headless CMS', 'ynnny'), ('Brightcove', 'Video platform', 'ynnyn'), ('Frame.io', 'Video review', 'nyyyn'),
            ('Ziflow', 'Creative approval', 'nyynn'), ('GitHub pull requests', 'Code review, outside media', 'nyyny')]
    th = ''.join(f'<th>{c}</th>' for c in cols)
    tr = ''.join(f'<tr><td>{n}<span class="k">{k}</span></td>' + ''.join(f'<td>{DOT[v]}</td>' for v in vals) + '</tr>' for n, k, vals in rows)
    tr += '<tr class="me"><td>Backlot<span class="k">This case</span></td>' + ''.join(f'<td>{DOT["y"]}</td>' for _ in cols) + '</tr>'
    return (f'<div class="bm"><table><thead><tr><th>Tool</th>{th}</tr></thead><tbody>{tr}</tbody></table>'
            f'<p class="bm-l"><span>{DOT["y"]} yes</span><span>{DOT["n"]} no</span>'
            '<span>From each tool’s public documentation, May 2026. Contentful Workflows and Strapi Review Workflows need a paid plan. '
            'Directus can build an approval flow with custom permissions, but has none built in. Backlot pins comments to metadata fields; frame-accurate comments on video were out of scope for this case.</span></p></div>')

def research():
    return ('<div class="bl2-t bl2-part"><p class="k">Research</p>'
            '<h2 class="bl2-h cs-title">Eight tools, each solving part of the job</h2>'
            '<p class="lead">Streaming CMSs are built in-house and rarely shown, so I studied the tools that cover pieces of the workflow: headless CMSs, a video platform, '
            'creative review tools, and GitHub’s pull request review, where a reviewer comments on an exact line and the author resolves each comment.</p></div>'
            + media_box(benchmark()))

# ---------- two roles: the screens as steps, dashboards then workspaces ----------
def roles():
    def rc(q, needs, who, when, sub, ini):
        return (f'<div class="bl2-role"><p class="bl2-q">{q}</p>'
                + '<ul class="bl2-ck">' + ''.join(f'<li>{x}</li>' for x in needs) + '</ul>'
                + f'<div class="bl2-rf"><span class="bl2-av" aria-hidden="true">{ini}</span><div><b>{who}</b><span>{when}. {sub}</span></div></div></div>')
    cards = ('<div class="bl2-roles">'
             + rc('What’s blocking release, and what can I clear today?', ['Files that still need an episode', 'What each region still needs', 'Which field a rejection points at'],
                  'Editor', 'All day', 'Works region by region, many episodes at once.', 'E')
             + rc('What airs first, and what changed since I last looked?', ['The queue sorted by release date', 'Only the fields that came back', 'Reasons tied to fields'],
                  'Publisher', 'Per review', 'Decides before a release date and can’t re-check everything.', 'P')
             + '</div>')
    top = ('<div class="bl2-t"><span class="cs-num bl2-x">02</span><p class="k">Two roles</p>'
           '<h2 class="bl2-h cs-title">One episode, two people asking different questions</h2>' + cards + '</div>')
    full = dict(z=1, x=50, y=50)
    dash = zoom(0, dict(r=['Blockers, counts and the work the editor left off, on one page.',
                           'What airs soon, what waits for review, and what each region has received.',
                           'The editor’s counts start with Rejected, because that is the work that came back to them. The publisher’s start with Pending review: each role sees first what needs them.',
                           'The editor’s banner names files that couldn’t be assigned. The publisher’s names the one item that airs within seven days and still needs a decision.',
                           'Missing fields grouped across everything assigned to the editor, so one pass fills the Spanish synopsis for seven items.',
                           'In place of blockers, the publisher sees each region’s deliveries this week and how far along they are.']),
                [dict(h='Editor: dashboard', m=0, **full),
                 dict(h='Publisher: dashboard', m=1, **full),
                 dict(h='Counts that follow the role', m=1, hl=[(19.3, 20.2, 54.4, 13)]),
                 dict(h='A banner for today’s blocker', m=0, hl=[(19.3, 10.2, 54.4, 7)]),
                 dict(h='What is blocking, grouped by field', m=0, hl=[(74.8, 56, 23.4, 41)]),
                 dict(h='Deliveries this week, per region', m=1, hl=[(74.8, 66.2, 23.4, 30.6)])],
                [IMG_ED_DASH, IMG_PUB_DASH], head_html=sub('Dashboards', 'Where each role starts the day.'))
    work = zoom(0, dict(r=['The editor’s page is called Workspace: everything they are working on, sorted by status, with rejections underneath.',
                           'The publisher’s page is called Reviews: only what reaches them, with every past decision underneath.',
                           'The editor’s list runs through all eight statuses, from To do to Published.',
                           'To do and In progress are the editor’s, so the publisher’s list leaves them out and starts at Pending review. Scheduled stays: the publisher decides what goes live.',
                           'The publisher’s queue is sorted by what airs first and shows how long each item has waited. In the same place, the editor’s table shows Blockers.',
                           'The editor sees rejected work as cards, so each reason shows before the item opens.',
                           'The publisher keeps a record of every decision: who decided, when, and when it was released.']),
                [dict(h='Editor: Workspace', m=0, **full),
                 dict(h='Publisher: Reviews', m=1, **full),
                 dict(h='Editor: all eight statuses', m=0, hl=[(19.3, 24.6, 15.4, 37.2)]),
                 dict(h='Publisher: starts at review', m=1, hl=[(19.3, 24.2, 15.4, 37.2)]),
                 dict(h='Publisher: what has waited longest', m=1, hl=[(75.4, 24.6, 13.8, 36.4)]),
                 dict(h='Editor: rejections as cards', m=0, hl=[(19.4, 65.6, 79, 28.4)]),
                 dict(h='Publisher: review history', m=1, hl=[(19.4, 64.4, 79, 33)])],
                [IMG_ED_WORK, IMG_PUB_WORK], head_html=sub('Workspaces', 'Where the work itself happens.'))
    return top + dash + work

def head2(n, k, h, lead=''):
    return (f'<span class="cs-num bl2-x">{n:02d}</span><p class="k">{k}</p><h2 class="bl2-h cs-title">{h}</h2>'
            + (f'<p class="lead">{lead}</p>' if lead else ''))

def specpile():
    """hand-drawn spec sheets that pile up to the right as the section scrolls in, a nod to the documents behind every screen"""
    import random
    rnd = random.Random(7)
    j = lambda v, a=1.6: round(v + rnd.uniform(-a, a), 1)
    def rough_rect(w, h):
        p = [(4, 4), (w - 4, 4), (w - 4, h - 4), (4, h - 4)]
        d = f'M{j(p[0][0])} {j(p[0][1])}'
        for x, y in p[1:] + [p[0]]:
            d += f' L{j(x)} {j(y)}'
        return d
    def scribble(x, y, w):
        d = f'M{j(x, .6)} {j(y, .6)}'
        steps = max(3, int(w / 14))
        for k in range(1, steps + 1):
            d += f' Q{j(x + w * (k - .5) / steps, 1)} {j(y + rnd.choice([-1.6, 1.6]), .5)} {j(x + w * k / steps, .6)} {j(y, .6)}'
        return d
    names = ['Circular 2017/3', 'User guide', 'Requirements', 'Backend rules', 'Form statuses', 'Balance rules', 'Port messages', 'Change requests',
             'Requirements v2', 'Extension rules', 'Roles and rights', 'Field list', 'Validation', 'Requirements v3']
    sh = ''
    for i, n in enumerate(names):
        W, H = 150, 212
        g = f'<path d="{rough_rect(W, H)}" fill="#FDFDFC" stroke="none"/>'
        g += f'<path class="o" d="{rough_rect(W, H)}"/><path class="o o2" d="{rough_rect(W, H)}"/>'
        g += f'<text x="{j(14, 1)}" y="{j(30, 1)}" class="t">{n}</text>'
        g += f'<path class="u" d="{scribble(14, 36, min(110, 9 * len(n)))}"/>'
        y = 54
        rows = 6 + i % 4
        hi = (i * 5) % rows
        for r in range(rows):
            w = rnd.choice([118, 104, 96, 112, 84, 122]) if r != rows - 1 else rnd.choice([60, 72])
            if r == hi and i % 2 == 0:
                g += f'<path class="h" d="{scribble(14, y, w * .7)}"/>'
            g += f'<path class="l" d="{scribble(14, y, w)}"/>'
            y += 15
        if i % 3 == 1:   # a word circled with a note
            cx, cy = j(92, 6), j(70 + (i % 4) * 15, 3)
            g += f'<ellipse class="c" cx="{cx}" cy="{cy}" rx="{j(24, 2)}" ry="{j(9, 1)}" transform="rotate({rnd.uniform(-8, 6):.1f} {cx} {cy})"/>'
        if i % 4 == 2:   # a ticked list
            for r in range(3):
                yy = 150 + r * 14
                g += f'<path class="l" d="M16 {yy - 5} l6 0 0 6 -6 0 z"/><path class="k" d="M17 {yy - 2} l2 3 5 -7"/>'
        g += f'<text x="{W - 18}" y="{H - 12}" class="n">{i + 3}</text>'
        r = (i * 37 % 11) - 5; yv = (i * 13 % 7) * 6 - i * 4
        sh += f'<div class="sp-s" style="--i:{i};--r:{r}deg;--y:{yv}px"><svg viewBox="0 0 150 212" aria-hidden="true">{g}</svg></div>'
    return f'<div class="sp-pile" data-pile aria-hidden="true">{sh}</div>'

def bilge():
    hero = ('<div class="bl2-t bl2-hero"><span class="cs-num bl2-x">00</span><span class="cs-title bl2-x">Overview</span>'
            '<p class="k">BİLGE, the customs platform of the Turkish Ministry of Trade</p><h1>Container tracking for Turkish customs</h1>'
            '<div class="bl2-hg"><p class="lead">BİLGE is the Ministry of Trade’s customs platform, made of dozens of modules, and I designed across many of them. '
            'This page shows KLTS, container and port tracking, designed from the system specifications and backend rules so every screen offers only what the system allows.</p>'
            '<div class="bl2-meta"><div><b>Company</b><a class="bl2-co" href="https://www.milsoft.com.tr/index.php/home/" target="_blank" rel="noopener">MilSOFT <span aria-hidden="true">↗</span><span class="sr-only"> (opens in a new tab)</span></a></div><div><b>Client</b>Turkish Ministry of Trade</div>'
            '<div><b>My role</b>UX/UI Designer</div><div><b>Date</b>2022 to 2023</div></div></div>'
            + media_box(f'<img class="bl2-img" src="{GH}shots/bilge/b-detail.webp" width="1920" height="1080" alt="Container tracking form detail as a customs officer sees it: the agent’s details above the containers and their parts">') + '</div>')
    cards = ''.join(f'<div class="bl2-c"><span class="bl2-tag">Decision {i}</span><h3>{t}</h3><p>{d}</p></div>' for i, (t, d) in enumerate([
        ('One form, four roles', 'Agents and customs staff open the same form; what changes is what each can do with it. The header is blue on the agent’s side and red on the customs side, so everyone knows which side of the form they are on.'),
        ('Sources side by side', 'The carrier’s declaration and the port’s records sit next to each other, so a mismatch is visible at a glance.'),
        ('Registering is binding', 'Registering starts the clock on the container’s permitted time in the country, so at the ministry’s request the button says Register. The confirmation shows the registration number and the remaining prepaid balance.')], 1))
    glance = ('<div class="bl2-t bl2-part"><p class="bl2-big" data-tint style="--ac:#A31A28;font-size:clamp(36px,5.4vw,100px)"><span class="bl2-line">Four parties, one container.</span><span class="bl2-line">No shared record.</span></p><p class="k">At a glance</p><h2 class="bl2-h cs-title">One container, several sources, one form</h2>'
              + split('The problem', '<p>Every container that enters or leaves a Turkish seaport needs a Container Tracking Form. KLTS moved that form, and the records customs, port operators and agencies used to exchange on paper, into one system.</p>'
                      '<p>Up to four people work on one form, and from registration the container’s permitted time is running.</p>')
              + f'<div class="bl2-cards c3">{cards}</div>'
              + split('Constraints', '<p>Legal wording on every label and ministry review on every change. The work is under NDA, so the screens on this page are rebuilt from my designs with placeholder data.</p>')
              + '</div>')
    specs = ('<div class="bl2-t"><div class="sp-wrap"><div>' + head2(2, 'Working from specs', 'Designed from the system specifications',
             'Every screen started from the specs: the analysts’ requirements, the regulation and the backend rules behind each field and status. '
             'An exit can’t be registered without an entry, approval needs enough prepaid balance, and a container can’t leave the port without an approved form. '
             'I designed so the interface never offers an action the backend would refuse.') + '</div>' + specpile() + '</div></div>')
    role = ('<div class="bl2-t">' + head2(1, 'My role', 'One module of many',
            'I joined after BİLGE’s design system was in place and worked across many modules. KLTS is the one whose designs I still have.')
            + split('Team', '<p>Five designers, a product manager and a large engineering team: about half of MilSOFT worked on BİLGE.</p>')
            + split('What I owned in KLTS', '<p>The agent’s form, the officer’s approval and query flows, time extensions, corrections, cancellations, the container history, the declaration comparison and closing a form with an official report: 107 screens and states in KLTS alone.</p>')
            + split('Design system', '<p>The platform’s design system was created by Dilmin Doğan and Gizem Turan Yücel. I added to it where these flows needed something it did not have.</p>')
            + '</div>')
    V = lambda k: dict(type='video', src=GH + f'bilge/{k}.mp4', poster=GH + f'bilge/{k}.jpg', w=1600, h=900)
    def flow(n, k, h, lead, steps, texts, medias, after=''):
        return zoom(0, dict(r=texts), steps, medias, head_html=head2(n, k, h, lead), after=after, show_hl=False)
    POP = (37, 25, 26, 39)
    agent = flow(3, 'The agent files', 'General information first, then the containers',
                 'The agent picks the movement (foreign or domestic, entry or exit), fills in general information, then adds containers one by one or in bulk. Until an officer approves the form, the agent can still edit it.',
                 [dict(h='General information first', t=4.45, hl=[(33.5, 25.5, 36.5, 50)]),
                  dict(h='Parts sit under their container', t=28.5, hl=[(63.5, 53.5, 35.5, 9)]),
                  dict(h='A last look before sending', t=30.5, hl=[(34, 29, 63, 22)]),
                  dict(h='Register, not Save', t=32.3, hl=[POP]),
                  dict(h='Waiting for an officer', t=36.6, hl=[(42, 9, 31.5, 4.5), (20, 29.5, 72, 3)])],
                 ['Every container on the form shares it, so the agent fills it once. Picking a tax ID fills in the company details.',
                  'Each container carries its own parts and equipment, so nothing is filed against the wrong one.',
                  'The list shows each container’s route, weight and parts before anything is sent.',
                  'Register sends the form to an officer’s queue. From then on, only the officer can change it.',
                  'The confirmation gives the registration number, and the form moves to the pending list.'],
                 [V('a')])
    track = flow(4, 'Tracking a container', 'Every source and every event in one place',
                 'Two screens came straight from the specs. The container history puts every event on one timeline. The comparison sets the carrier’s summary declaration against the port’s records.',
                 [dict(h='One timeline per container', t=0.6, hl=[(20, 43, 77, 55)]),
                  dict(h='Each event keeps its record', t=2.6, hl=[(20, 70, 77, 22)]),
                  dict(h='Declaration against port data', t=4.3, hl=[(21, 59.5, 12, 19), (58.5, 59.5, 12, 19)]),
                  dict(h='A mismatch opens its record', t=7.5, hl=[(34.5, 59.5, 15.5, 25), (74.5, 59.5, 15.5, 25)])],
                 ['Gate moves, declarations and form approvals from different systems, newest first.',
                  'Opening an event shows its stage, package count, weight and the form it belongs to.',
                  'Shortfall lists containers the port recorded but the declaration missed. Surplus lists the reverse.',
                  'Selecting a container shows its notice, registration and bill of lading next to the other source.'],
                 [V('d')])
    customs = flow(5, 'Customs decides', 'Officers and managers act from their queue',
                   'Officers approve, edit or cancel registered forms; after approval, only customs can change them. Some changes need a second signature: time extensions and cancellations go to the manager, corrections to the deputy manager.',
                   [dict(h='The form at a glance', m=0, t=3.2, hl=[(20.5, 17, 77, 16.5)]),
                    dict(h='Approve some, reject the rest', m=0, t=6.0, hl=[(21.5, 49.5, 3, 22), (76.5, 37.5, 12.5, 4)]),
                    dict(h='Both sides counted', m=0, t=8.3, hl=[POP]),
                    dict(h='The balance after approval', m=0, t=11.4, hl=[POP]),
                    dict(h='Managers decide on the row', m=1, t=1.4, hl=[(20, 57, 77, 6)]),
                    dict(h='The result stays on the list', m=1, t=6.0, hl=[(42, 8.8, 32, 4.6), (82.5, 57.5, 5.5, 4)])],
                   ['The agent’s details sit above the containers, each with its parts and equipment.',
                    'The officer selects the containers that pass. Approving the selection rejects the others in the same step.',
                    'Before anything changes, the confirmation says how many containers are approved and how many rejected.',
                    'The success message shows how much of the agent’s prepaid balance is left.',
                    'Time extensions reach the manager as a list with the request and its reason. Approve and Reject sit on the row, behind a confirmation.',
                    'The status changes in place and a message confirms it, so the manager carries on with the queue.'],
                   [V('b'), V('c')],
                   after='<div class="bl2-t">' + split('Also in this flow', rules([
                       'Written reasons open in a side drawer, so the form stays in view.',
                       'Editing a form an agent registered warns that the agent’s record will change.'])) + '</div>')
    learned = ('<div class="bl2-t">' + head2(6, 'What I learned', 'In government software the wording is part of the design')
               + split('Wording', '<p>A word like Register carries legal weight, so ministry review shaped the design from the start.</p>')
               + split('When the spec was wrong', '<p>Sometimes the client described a rule wrongly. It surfaced when we presented the screens and the client brought in the customs officers who would use them: they spotted what did not match their work, and we redesigned. Since then I ask for the people who will use the screens as early as the client allows.</p>')
               + split('How I built this page', '<p>The flows, screens and design system additions are my work at MilSOFT. I rebuilt the screens in Claude Design from the originals and checked each one against them.</p>')
               + '</div>')
    w1 = (sec('ov', 'Overview', hero) + sec('mr', 'My role', role + glance) + sec('dm', 'Working from specs', specs)
          + sec('ag', 'The agent files', agent) + sec('tr', 'Tracking a container', track) + sec('cu', 'Customs decides', customs)
          + sec('le', 'What I learned', learned))
    nb = nextblock('bilge')
    body = f'<main class="bl2-page"><div class="cs-wrap" data-bl2root="1"><nav class="bl-nav" aria-label="Case study sections"><ol></ol></nav>{w1}</div>{nb}</main>'
    return page('BİLGE container tracking case study | Ege Coskun',
                'BİLGE KLTS: container and port tracking for Turkish customs. Approval chains across agents, officers and managers, built on an existing design system.',
                body, ['site.css', 'backlot.css'], ['site.js', 'backlot.js'])


# ---------- Data health (product work at Insider One): rebuilt screens, everything outside the components blurred ----------
def datahealth():
    def dh_img(name, alt):
        w, h = (2880, 1800)
        return f'<img class="bl2-img" src="{GH}shots/dh/{name}.webp?v=2" width="{w}" height="{h}" alt="{alt}" loading="lazy">'
    def dh_cards(items,c3=False):
        return f'<div class="bl2-cards{" c3" if c3 else ""}">'+''.join(f'<div class="bl2-c"><span class="bl2-tag">{i:02d}</span><h3>{h}</h3><p>{t}</p></div>' for i,(h,t) in enumerate(items,1))+'</div>'
    hero=('<div class="bl2-t bl2-hero"><span class="cs-num bl2-x">00</span><span class="cs-title bl2-x">Overview</span>'
     '<p class="k">Data health, product work at Insider One</p><h1>Telling marketers which data to trust before they build a segment</h1>'
     '<div class="bl2-hg"><p class="lead">Insider One is a customer data platform. Marketers build audiences from attributes and events that many sources send in. '
     'Requests reached me from customers through the PM. I designed three pieces: a per-source count on the attribute page, and a data health card in the segment builder, for attributes and for event parameters.</p>'
     '<div class="bl2-meta"><div><b>Company</b><a class="bl2-co" href="https://insiderone.com/" target="_blank" rel="noopener">Insider One <span aria-hidden="true">↗</span><span class="sr-only"> (opens in a new tab)</span></a></div><div><b>Category</b>B2B SaaS, customer data platform</div><div><b>My role</b>Product Designer</div><div><b>Date</b>2026</div></div></div>'
     + media_box(dh_img('o_b_issue','Segment builder with the attribute menu open and a data health card for Email Opt-in')) + '</div>')
    prob=('<div class="bl2-t"><span class="cs-num bl2-x">01</span><span class="cs-title bl2-x">The problem</span>'
     '<p class="bl2-big" data-tint style="--ac:#2D2ACF"><span class="bl2-line">The segment broke at the last step.</span></p>'
     + split('The problem','<p>An attribute page showed one number, Total collected, with no way to see which source sent what. '
       'If an attribute’s data was wrong, the marketer found out only at the last step of building a segment, after setting up everything else.</p>')+'</div>')
    f1=('<div class="bl2-t bl2-f"><span class="cs-num bl2-x">02</span><span class="cs-title bl2-x">Where data comes from</span><p class="k">Feature 01</p>'
     '<h2 class="bl2-h">The total, split by where the data comes from</h2><p class="lead">The total now sits next to a count for every source, so a source that stops sending shows up here first.</p>'
     + sub('Before','Only Total collected.') + media_box(dh_img('o_a_before','App Version attribute page, before: only the total'))
     + sub('After','The total, then each group of sources with its own count.') + media_box(dh_img('o_a_after','App Version attribute page, after: counts per source'))
     + dh_cards([('Grouped by how data arrives','SDK sources, external integrations and API sit in one group beside the total.'),
              ('Every source named','Mobile, Web, Shopify, Amplitude and API each show their own number.'),
              ('Help next to the label','Each label has a question mark that explains it on hover.')],True)+'</div>')
    f2=('<div class="bl2-t bl2-f"><span class="cs-num bl2-x">03</span><span class="cs-title bl2-x">Data health in the menu</span><p class="k">Feature 02</p>'
     '<h2 class="bl2-h">Data health shown inside the attribute menu</h2><p class="lead">The problem now shows while the marketer picks an attribute, not when the segment fails. Hovering an attribute opens a card with its sources, its volume and, if something is wrong, what and where.</p>'
     + sub('A healthy attribute') + media_box(dh_img('o_b_healthy','Language attribute card: string, four sources, 1.5k ingested in the last 30 days'))
     + sub('An attribute with a problem') + media_box(dh_img('o_b_issue','Email Opt-in card: incorrect data type from the Email source, with a link to Data Validation'))
     + dh_cards([('Healthy attributes stay quiet','A blue top line, the sources that send it, how much came in and over what period.'),
              ('A problem names its source','Email Opt-in gets a warning icon in the list, a yellow top line and a red Email chip. The card says the data type is wrong.'),
              ('Usable, with a way to fix it','The attribute can still be used. Go to Data Validation opens the place to correct the data point.')],True)
     + '</div>')
    f3=('<div class="bl2-t bl2-f"><span class="cs-num bl2-x">04</span><span class="cs-title bl2-x">Event parameters</span><p class="k">Feature 03</p>'
     '<h2 class="bl2-h">The same check for event parameters</h2><p class="lead">A segment can also filter on what users did. Event parameters break the same way attributes do, so the parameter menu shows the same warning and the same card, worded for a parameter.</p>'
     + media_box(dh_img('o_b_event','Event Source parameter card with an incorrect data type warning'))
     + '<div class="bl2-t">'+split('One card, many cases',rules(['Seven issue types: Incorrect Data Type, Invalid Value Format, Null Value, Missing Data, Abnormal Volume Change, Volume Threshold Reached, Multiple Issues.',
         'Five source states: Syncing, Not Used, Paused, Not Receiving Data, and no ingested data.']))+'</div></div>')
    nxt=('<div class="bl2-t"><span class="cs-num bl2-x">05</span><span class="cs-title bl2-x">What’s next</span><p class="k">What’s next</p>'
     '<h2 class="bl2-h cs-title">What I would measure</h2>'
     + split('Measure','<p>I don’t have numbers I can share. I would track how often a segment fails at the last step, and how often marketers open Data Validation from the card.</p>')
     + split('Confidentiality','<p>The product is under NDA, so these screens are rebuilt with placeholder data (acme-store), and everything outside my components is blurred. Layout, states and wording follow what shipped.</p>')+'</div>')
    body=('<main class="bl2-page"><div class="cs-wrap" data-bl2root="1"><nav class="bl-nav" aria-label="Case study sections"><ol></ol></nav>'
     + sec('ov','Overview',hero)+sec('pr','The problem',prob)+sec('f1','Where data comes from',f1)+sec('f2','Data health in the menu',f2)+sec('f3','Event parameters',f3)+sec('nx','What’s next',nxt)+'</div>' + nextblock('data-health') + '</main>')

    h = page('Data health case study | Ege Coskun', 'Data health in a customer data platform: where data comes from, and a warning in the segment builder.',
             body, ['site.css', 'backlot.css'], ['site.js', 'backlot.js'])
    return h.replace('<meta charset="utf-8">', '<meta charset="utf-8"><meta name="robots" content="noindex,nofollow,noarchive">', 1)

# ---------- Work: two lead cases side by side, the rest as a list ----------
def untangle():
    """a sentence that starts tangled and straightens as it scrolls into place"""
    import random
    rnd = random.Random(11)
    words = 'I like untangling the parts of a product nobody wants to own.'.split(' ')
    out = ''
    for w in words:
        ch = ''.join(f'<i style="--x:{rnd.uniform(-1, 1):.2f};--y:{rnd.uniform(-1, 1):.2f};--r:{rnd.uniform(-1, 1):.2f}">{c}</i>' for c in w)
        out += f'<span class="ut-w">{ch}</span> '
    return (f'<div class="ut" data-ut><p class="ut-s" aria-label="I like untangling the parts of a product nobody wants to own."><span aria-hidden="true">{out.strip()}</span></p></div>')

def work():
    ARW = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 12h15M13 6l6 6-6 6" fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"/></svg>'
    lead = [
        ('backlot', '01', 'Backlot, concept project', 'From delivery to release, one region at a time',
         'A CMS where streaming teams take films and series from delivery to release. I designed the whole workflow for editors and publishers.',
         ['B2B SaaS', 'Streaming CMS', '2026'], GH + 'shots/v2/ed-dashboard.webp?v=4', 'Backlot editor dashboard', GH + 'content-tour-fast.mp4'),
        ('bilge', '02', 'BİLGE', 'Container tracking for Turkish customs',
         'Customs software for the Ministry of Trade, designed from the system specifications and backend rules.',
         ['GovTech', 'Customs platform', '2022 to 2023'], GH + 'shots/bilge/b-detail.webp', 'BİLGE container tracking form detail', GH + 'bilge/preview.mp4'),
    ]
    def cc(n, u):
        return f'<a class="wk-cc" href="{u}" target="_blank" rel="noopener" aria-label="{n}, company website, opens in a new tab">{n} <span aria-hidden="true">↗</span></a>'
    CO = {'bilge': cc('MilSOFT', 'https://www.milsoft.com.tr/index.php/home/'), 'data-health': cc('Insider One', 'https://insiderone.com/')}
    def chips(k, tags):
        return '<span class="wk-tags">' + ''.join(f'<i>{x}</i>' for x in tags) + CO.get(k, '') + '</span>'
    # the title link stretches over the whole card, so the company chip can be its own link
    cards = ''.join(
        f'<div class="wk-c"><span class="wk-m"><img src="{img}" alt="{alt}" loading="lazy"><video data-src="{vid}" muted loop playsinline preload="none" aria-hidden="true"></video><em class="wk-pl">Hover to play</em></span>'
        f'<span class="wk-n">{name}</span><a class="wk-t wk-sl" href="/{k}">{t} {ARW}</a>' + chips(k, tags) + '</div>'
        for k, num, name, t, d, tags, img, alt, vid in lead)
    more = [
        ('data-health', '03', 'Data health', 'Telling marketers which data to trust before they build a segment.', ['B2B SaaS', 'Customer data platform', '2026'], GH + 'shots/dh/thumb.webp'),
        # ('uwaverde', '04', 'UwaVerde', 'A website and member portal for an NGO I co-founded.', ['Web', 'Portal', '2024'], WF + '691de9a378fcaab7283af4c8_HomePage%20(1)%20(1)-p-1080.png'),
    ]
    rows = ''.join(
        f'<li><div class="wk-r"><em>{num}</em><b><a class="wk-sl" href="/{k}">{name}</a></b><span class="wk-rd"><span>{t}</span>' + chips(k, tags)
        + f'</span><span class="wk-p" aria-hidden="true"><img src="{img}" alt="" loading="lazy"></span></div></li>'
        for k, num, name, t, tags, img in more)
    import about as _ab
    qa = ''.join(f'<details class="ax-q"><summary><span>{q}</span><i aria-hidden="true"></i></summary><p>{a}</p></details>' for q, a in _ab.QA)
    about = (f'<section class="ax-ask lt wk-qa"><p class="k">Things you might ask</p><div><div class="ax-qs">{qa}</div>'
             '<a class="wk-btn ec-btn ink" href="/about"><span>More about me</span></a></div></section>'
             '<style>' + _ab.QCSS + '.wk-qa{margin-top:clamp(96px,10vw,180px);padding:0;grid-template-columns:calc(33.33% - 16px) minmax(0,1fr);gap:16px;--h3:clamp(18px,1.3vw,24px)}'
             '.wk-qa .k{position:sticky;top:calc(4.75rem + 24px);align-self:start}.wk-qa .wk-btn{margin-top:32px}'
             '@media(max-width:899px){.wk-qa{grid-template-columns:1fr}.wk-qa .k{position:static}}</style>')
    body = (f'<main class="wk"><div class="cs-wrap"><div class="wk-hero"><p class="wk-open"><i></i>Open to product design roles, Berlin</p>'
            f'<h1>I learned design where there’s no Ctrl+Z.</h1>'
            f'<p class="wk-lead">A millimetre off in a bus interior part, and the tooling is already paid for. I design B2B data products now, and I still look for the edge case while it is a design problem, before it becomes a bug report.</p></div>'
            f'<div class="wk-sel" id="work"><p class="k">Selected work</p></div>'
            f'<div class="wk-g">{cards}</div><p class="k wk-k">More work</p><ul class="wk-l">{rows}</ul>{about}</div></main>')
    return page('Ege Coskun | Product designer, Berlin', 'Ege Coskun, product designer in Berlin: B2B tools for teams that review, approve and ship work. Case studies: Backlot, BİLGE, UwaVerde.',
                body, ['site.css', 'backlot.css'], ['site.js', 'backlot.js'])

# ---------- UwaVerde: same components ----------
WF = 'https://s3.amazonaws.com/webflow-prod-assets/67a7e306e38056dfa249a42d/'
def wimg(path, alt):
    return f'<img class="bl2-img" src="{WF}{path}" alt="{alt}" loading="lazy">'

def uwaverde():
    hero = ('<div class="bl2-t bl2-hero"><span class="cs-num bl2-x">00</span><span class="cs-title bl2-x">Overview</span>'
            '<p class="k">UwaVerde, a sustainability NGO</p><h1>A website and member portal for an NGO I co-founded</h1>'
            '<div class="bl2-hg"><p class="lead">UwaVerde ran on scattered tools. I designed one place to win collaborators and one to run the work: '
            'a public website and a member portal, with one visual identity across both.</p>'
            '<div class="bl2-meta"><div><b>Context</b>Volunteer work for an NGO I co-founded</div><div><b>Category</b>NGO, sustainability</div>'
            '<div><b>My role</b>UX/UI Designer, UX Writer</div><div><b>Date</b>2024</div></div></div>'
            + media_box(wimg('692b1295878b06826afa0925_uwaverdeproject-p-1600.png', 'UwaVerde website and member portal on several screens')) + '</div>')
    goals = ('<div class="bl2-t">' + head2(1, 'Goals', 'One place to win collaborators, one to run the work')
             + split('Goals', rules(['A website that introduces the mission and attracts collaborators and supporters.',
                                     'A member portal where members talk, share documents and manage project tasks.',
                                     'One visual identity across both: consistent, trustworthy, eco-conscious.'])) + '</div>')
    def page_(t, d, img, alt):
        return '<div class="bl2-t">' + sub(t, d) + '</div>' + media_box(wimg(img, alt))
    web = ('<div class="bl2-t">' + head2(2, 'The website', 'Short pages that lead to the projects') + '</div>'
           + page_('Landing page', 'Short on purpose, so visitors stay with the content that matters.', '691de9a378fcaab7283af4c8_HomePage%20(1)%20(1)-p-1080.png', 'UwaVerde landing page')
           + page_('Responsive', 'Every element was chosen to adapt across screen sizes, not only to shrink.', '6926e9cefb41a13b034b37ce_72278c3a79f3147b3a2ae7dba0432ca6_mobilelanding%20%282%29-p-1600.png', 'UwaVerde landing page on mobile')
           + page_('Tone of voice', 'Optimistic and inclusive. Precise enough for experts, easy enough for students.', '691df1d073017ca40db2391e_3db66b98896f0d38fe027efd3ab67d0e_Frame%201597884210-p-1600.png', 'UwaVerde tone of voice examples')
           + page_('About us', 'Mission, values and the people behind the work, in one scroll.', '692b236b8185d7a67e2e9364_AboutUs1920-min-p-1600.png', 'UwaVerde about us page')
           + page_('Projects', 'Every project in one list, opened one at a time.', '692b2476e9466303595860d6_Projects%201920-p-1600.png', 'UwaVerde projects page')
           + page_('Project detail', 'Each project reads the same way: goal, timeline, objectives, actions.', '692b267479e252bb68624e9a_Shell-p-1600.png', 'UwaVerde project detail page'))
    portal = ('<div class="bl2-t">' + head2(3, 'Member portal', 'One sign-in to talk, share documents and track tasks') + '</div>'
              + media_box(wimg('691dfe75ee34d04039507ee4_Group%20626307-p-1600.png', 'UwaVerde member portal screens'))
              + media_box(wimg('691dfecd6d12c81895dc188c_e8fc713202a389eda936347e9cee1835_Pro-Display-XDR--p-1600.png', 'UwaVerde member portal on a desktop display')))
    w1 = sec('ov', 'Overview', hero) + sec('go', 'Goals', goals) + sec('we', 'The website', web) + sec('po', 'Member portal', portal)
    nb = ''
    body = f'<main class="bl2-page"><div class="cs-wrap" data-bl2root="1"><nav class="bl-nav" aria-label="Case study sections"><ol></ol></nav>{w1}</div>{nb}</main>'
    return page('UwaVerde case study | Ege Coskun',
                'UwaVerde: a website and member portal for a sustainability NGO, from tone of voice to responsive landing, about and project pages.',
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
    emb_css = ''.join(re.findall(r'<style>(.*?)</style>', EMB('13941d11') + EMB('f6fe44e7') + EMB('020e6363'), re.S))
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
    write('assets/backlot.js', nav_js + '\n' + rd('bl2.js') + '\n' + rd('tint.js') + '\n' + vid_js.replace("rootMargin:'600px 0px'", "rootMargin:'1400px 0px'") + '\n' + rd('zoom.js') + '\n' + rd('roles.js') + '\n' + rd('pace.js'))
    write('assets/site.js', rd('site.js'))
    html = backlot()
    a, b = html.index('<main'), html.index('</main>')
    html = html[:a] + re.sub(r'<style>.*?</style>', '', html[a:b], flags=re.S) + html[b:]
    # prototypes load about two screens ahead instead of all at page load
    html = re.sub(r'<iframe data-blx src="([^"]+)"', r'<iframe data-blx data-lsrc="\1"', html)
    html = html.replace('</body>', '<script>(function(){var f=document.querySelectorAll("iframe[data-lsrc]");function go(e){e.src=e.dataset.lsrc;e.removeAttribute("data-lsrc")}if(!("IntersectionObserver" in window)){[].forEach.call(f,go);return}var o=new IntersectionObserver(function(x){x.forEach(function(e){if(e.isIntersecting){go(e.target);o.unobserve(e.target)}})},{rootMargin:"1600px 0px"});[].forEach.call(f,function(e){o.observe(e)})})();</script></body>', 1)
    write('backlot/index.html', html)
    write('bilge/index.html', bilge())
    write('uwaverde/index.html', uwaverde().replace('<meta charset="utf-8">', '<meta charset="utf-8"><meta name="robots" content="noindex,nofollow">', 1))
    write('data-health/index.html', datahealth())
    write('work/index.html', '<!doctype html><html lang="en"><head><meta charset="utf-8"><title>Work | Ege Coskun</title><link rel="canonical" href="/#work"><meta http-equiv="refresh" content="0;url=/#work"><script>location.replace("/#work")</script></head><body><a href="/#work">Work</a></body></html>')
    write('index.html', work())
    import about
    for k, iv in [('about-a', 'swing'), ('about-b', 'dock'), ('about', 'flip')]:
        h = page('About | Ege Coskun', 'Ege Coskun, product designer in Berlin: from industrial design to B2B data products.',
                 about.about3(iv), ['site.css', 'backlot.css'], ['site.js'], cur='about')
        if k != 'about':
            h = h.replace('<meta charset="utf-8">', '<meta charset="utf-8"><meta name="robots" content="noindex,nofollow">', 1)
        write(k + '/index.html', h)
    print('built', len(html))
