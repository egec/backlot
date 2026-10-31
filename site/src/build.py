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
    fl = '<link href="https://fonts.googleapis.com/css2?family=Inter+Tight:wght@400;500;600;700;800&family=Reenie+Beanie&display=swap" rel="stylesheet">' if font else ''
    return f'''<!doctype html><html lang="en"{' class="f-it"' if font else ''}><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title}</title><meta name="description" content="{desc}">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&display=swap" rel="stylesheet">{fl}{css}</head><body class="case">
<header class="site-h"><div class="site-hi"><a class="site-logo" href="/" aria-label="Ege Coskun, home"><img src="{LOGO}" alt="Ege Coskun" width="140" height="43"></a>
<nav class="site-n" aria-label="Main"><a href="/work">Work</a><a href="/about">About</a><a href="#contact">Contact</a></nav></div></header>
{body}
<footer class="finalfooter" id="contact">{rem(rd('foot.html'))}</footer>{js}</body></html>'''

# ---------- building blocks ----------
def strip(on):
    return '<div class="bl2-strip">Cuts the loop at ' + '<b>→</b>'.join(
        '<i class="on">%s</i>' % x if x == on else '<i>%s</i>' % x for x in ['Deliver', 'Prepare', 'Review', 'Release']) + '</div>'

NOTE_ARROW = '<svg viewBox="0 0 96 56" aria-hidden="true"><path class="nb" d="M90 22 C 70 44, 34 40, 13 20" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/><path class="nh" d="M26.5 23.8 L13 20 L17.4 33.3" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg>'
NOTE_DOWN = '<svg viewBox="0 0 60 72" aria-hidden="true"><path class="nb" d="M8 8 C 32 10, 50 30, 44 64" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round"/><path class="nh" d="M34 54 L44 65 L52 52" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/></svg>'
def head(n, f, nav=False, note=''):
    hid = '<span class="cs-num bl2-x">05</span><span class="cs-title bl2-x">Features</span>' if nav else ''
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

def zoom(n, f, steps, medias, after='', nav=False, head_html=None, note=''):
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
                      for si, s in enumerate(steps) if s.get('m', 0) == i for (x, y, w, h) in s.get('hl', []))
        ms += f'<div class="zs-mw{on}" data-i="{i}">{el}{hls}</div>'
    bars = ''.join(f'<button type="button" aria-label="Step {i+1}"><i></i></button>' for i in range(len(steps)))
    has_video = any(m['type'] == 'video' for m in medias)
    ctl = ('<button type="button" class="zs-play" data-zplay><svg width="14" height="14" viewBox="0 0 24 24" aria-hidden="true"><path d="M8 5v14l11-7z" fill="currentColor"/></svg>'
           '<span>Play the whole video</span></button>') if has_video else ''
    hd = head_html if head_html is not None else head(n, f, nav=nav, note=note)
    return (f'<div class="bl2-t bl2-f{" first" if nav else ""}">{hd}<div class="zs" data-zs style="--n:{len(steps)}"><div class="zs-pin"><ol class="zs-steps">{lis}</ol>'
            f'<div class="zs-stick"><div class="zs-frame"><div class="zs-view" style="aspect-ratio:{medias[0]["w"]}/{medias[0]["h"]}">{ms}</div></div>'
            f'<div class="zs-foot"><div class="zs-bar">{bars}</div>{ctl}</div></div></div></div>{after}</div>')

IMG_SEASON = dict(type='img', src=GH + 'shots/thumbnails.webp', w=2880, h=1800, alt='Season 4 in Spain: region selector, readiness panel, personalized thumbnails')
IMG_EP2 = dict(type='img', src=GH + 'shots/ep2-shell.webp', w=2880, h=1800, alt='Episode 2 metadata page: needs your input, values from the delivery, AI flags')
IMG_REJ = dict(type='img', src=GH + 'shots/reject-v2.webp', w=1846, h=1154, alt='Publisher review of Sherlock Holmes: two flagged rows and a list of two rejection reasons')
IMG_UP3 = dict(type='img', src=GH + 'shots/upload-3.webp', w=1874, h=1172, alt='Upload drop zone open over the assets list')
IMG_UP15 = dict(type='img', src=GH + 'shots/upload-15.webp', w=1874, h=1172, alt='Season 4 in Spain with the upload result in the corner and 15 files waiting in the readiness panel')
IMG_AS = dict(type='img', src=GH + 'posters/assets-filters.jpg?v=11', w=2054, h=1284, alt='Assets: the delivery batch with a state per file, and the content list with completeness per title')
VID_UP = dict(type='video', src=GH + 'upload.mp4?v=12', poster=GH + 'posters/upload.jpg?v=12', w=1874, h=1172)
VID_AS = dict(type='video', src=GH + 'assets-filters.mp4?v=11', poster=GH + 'posters/assets-filters.jpg?v=11', w=2054, h=1284)

def changed():
    story = ('<div class="bl2-t"><span class="cs-num bl2-x">06</span><p class="k">What I changed</p>'
             '<h2 class="bl2-h cs-title">Why I moved from a single rejection modal to field-pinned reasons</h2>'
             '<div class="bl2-split bl2-split-first"><p class="k">The first version</p><div><p>The first version allowed one rejection reason per item, and I caught myself labelling rejected items “Multiple Issues”. '
             'That label was a symptom, not a reason, so reasons became a list, each pinned to a field and resolvable on its own.</p></div></div></div>')
    return (story + media_box(EMB('8a2ee889'))
            + '<div class="bl2-t">' + sub('What I took out', 'Most of what I added stayed. Four things didn’t.') + '</div>' + P['CARDS'])

def hero():
    h = P['411a7ea2-ad8e-e2d4-3a36-2ddce0bbd66d']
    rep = [('<h1>Rejections that tell the editor exactly what to fix</h1>', '<h1>From delivery to release, one region at a time</h1>'),
           ('<p class="lead">Backlot is where streaming services prepare films and series for release, one region at a time. I designed the review loop between editor and publisher, so a rejection is a list of reasons pinned to fields, not a vague note.</p>',
            '<p class="lead">Streaming teams use Backlot to take films and series from delivery to release, region by region. I designed the whole workflow for both sides: dashboards, upload and file matching, fields that fill from the file, the publisher’s review and artwork tests.</p>'),
           ('<b>Context</b>Solo concept. The take-home that got me hired for my last role, rebuilt and extended.', '<b>Context</b>The take-home that got me hired for my last role, rebuilt and extended.'),
           ('<b>Date</b>2026', '<b>Timeline</b>2026, 3 weeks')]
    for o, n in rep:
        assert o in h, o[:40]
        h = h.replace(o, n)
    return h

MINI = '<i></i><b>Pending Approval</b><u></u><u></u><u></u>'
def nbthumb(html, src, alt=''):
    assert MINI in html
    return html.replace(MINI, f'<img src="{src}" alt="{alt}" loading="lazy">')

def sec(k, label, inner):
    return f'<section data-bl2="{k}" data-nav-label="{label}">{inner}</section>'

def backlot():
    w1 = (sec('ov', 'Overview', hero())
          + sec('pr', 'The problem', problem())
          + sec('ns', 'North star', north_star())
          + sec('rs', 'Research', research())
          + sec('ro', 'Two roles', roles())
          + sec('fe', 'Features', features())
          + sec('ch', 'What I changed', changed()))
    ds = ds_build().replace('Lupin, S4-E2', 'Lupin · S4-E2').replace('Community, S6-E6', 'Community · S6-E6').replace('Long Story Short, S1-E3', 'Long Story Short · S1-E3') \
        .replace('Crime, Drama', 'Crime · Drama').replace('Edit requested, waiting', 'Edit requested · waiting').replace('Editor, Alex', 'Editor · Alex').replace('Publisher, Maya', 'Publisher · Maya')
    w2 = sec('re', "What's next", P['c2545a3c-0f01-ab8f-4f5f-45336f755274'])
    nb = nbthumb(P['78fe6fd2-fd22-0eb4-d2e4-629e35df69b3'], GH + 'shots/bilge/b-queue-th.webp').replace('href="/work"', 'href="/bilge"').replace('Customs approvals where every change carries a reason.', 'Container tracking for Turkish customs, designed from the system specs.')
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

def simple(n, f, media, nav=False, after=''):
    return f'<div class="bl2-t bl2-f{" first" if nav else ""}">{head(n, f, nav=nav)}{media_box(media)}{after}</div>'

IMG_ED_DASH = dict(type='img', src=GH + 'shots/roles/ed-dashboard.webp', w=2304, h=1440, alt='Editor dashboard: unassigned files banner, counts, items in progress, upcoming releases, activity and what is blocking')
IMG_PUB_DASH = dict(type='img', src=GH + 'shots/roles/pub-dashboard.webp', w=2304, h=1440, alt='Publisher dashboard: what airs this week, review counts, pending review, upcoming releases and deliveries this week')
IMG_ED_WORK = dict(type='img', src=GH + 'shots/roles/ed-workspace.webp', w=2304, h=1440, alt='Editor workspace: workflow table filtered by status, rejections as cards, uploads panel in the corner')
IMG_PUB_WORK = dict(type='img', src=GH + 'shots/roles/pub-reviews.webp', w=2304, h=1440, alt='Publisher reviews: review queue by status and review history')

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
                'Values read from the file can’t be edited. Values from the delivery unlock one field at a time, so every change is deliberate.',
                'Submit hands the episode to the publisher. Save keeps it under In progress, ready to pick up later.',
                '“4 of 8” tells the editor how much is left and where to start. “Incomplete” only says something is wrong.',
                'The season page lists what must be complete before the season can be scheduled.'])
    F.append(lambda n, nav: zoom(n, f_fill, [
        dict(h='Gaps come first', m=1, z=1.25, x=40, y=40, hl=[(5, 23.5, 68, 34.5)]),
        dict(h='Locked by its source', m=1, z=1.4, x=40, y=78, hl=[(14.6, 63.4, 5.4, 2.9), (36.1, 70.4, 2, 23), (70.1, 70.4, 2, 23)]),
        dict(h='Save is not submit', m=1, hl=[(62.8, 8.8, 9.9, 3.9), (66.6, 95.1, 5.7, 3.7)]),
        dict(h='Progress, not pass or fail', m=0, z=1.9, x=85, y=29, hl=[(91.6, 23.4, 5.6, 14.4), (91.4, 10.8, 6.2, 2.6)]),
        dict(h='Readiness for the season', m=0, z=1.5, x=78, y=20, hl=[(59.3, 8.7, 38.4, 8.7)])], [IMG_SEASON, IMG_EP2],
        after=sub('A season keeps its own metadata, apart from its episodes', 'Episodes, season metadata, season assets, deliveries per region and the audit log, with the readiness panel in view on every tab.') + media_box(EMB('137e3b55')), nav=nav))
    # upload, the unhappy path
    f_up = dict(t='Designed for the delivery that arrives broken',
             l='Deliveries often arrive incomplete or mislabelled. Processing assigns the files it can match, and the rest wait for the editor under Needs assignment.',
             r=['Processing reads each file’s technical metadata and links it to its episode. Files it can’t place go to Needs assignment.',
                'The upload folds into a panel in the corner, so the editor can open other pages and come back to it.',
                'The drop zone stays open, so files can be added while others are still uploading.',
                'Uploading, Processing, Ready, Needs assignment and Failed belong to the file, apart from the episode’s workflow status.'])
    F.append(lambda n, nav: zoom(n, f_up, [
        dict(h='Processing assigns what it can', m=0, hl=[(75.6, 46, 22.2, 7.2)], ctx=(75.6, 11, 22.2, 1)),
        dict(h='Keep working while it uploads', m=0, hl=[(74.6, 86.6, 23.8, 11.4)], ctx=(60, 60, 1, 1)),
        dict(h='Add files mid-upload', m=1, hl=[(27, 5.4, 46.2, 21.6)]),
        dict(h='Each file has its own state', m=2, hl=[(61.8, 30.4, 19.4, 26.8)], ctx=(5, 20.5, 80, 1))], [IMG_UP15, IMG_UP3, IMG_AS],
        after=sub('Resolving the files processing couldn’t place', 'Each problem gets its own fix: assign files in bulk, keep or replace a duplicate master, or create the episode a file points to.') + media_box(EMB('2f6c4fe9')),
        note='unhappy path', nav=nav))
    # rejection
    f_rej = dict(t='A rejection is a list of reasons',
             l='The publisher approves an item, or sends it back with reasons the editor can act on one by one. Each reason is pinned to its field.',
             r=['The publisher comments on the metadata row itself. Each comment becomes a reason with its field and a category.',
                'Flagged rows stay marked on the page, so the editor fixes them in place.',
                'Before anything is sent, Reject shows how many reasons there are and who gets the item back.'])
    F.append(lambda n, nav: zoom(n, f_rej, [
        dict(h='Comments become reasons', hl=[(69.5, 14.6, 28, 14.6), (5.6, 22.6, 61.4, 7.4)], ctx=(69.5, 10, 28, 1)),
        dict(h='Fixed in place', hl=[(5.6, 22.6, 61.4, 7.4), (5.6, 63.6, 61.4, 7)]),
        dict(h='Counted before it is sent', hl=[(70, 52.2, 27.4, 8.6)], ctx=(69.5, 10, 28, 1))], [IMG_REJ],
        after=sub('Try it', 'Flag two fields as the publisher, then fix them as the editor.') + media_box(EMB('f663202a')), nav=nav))
    # AI
    f_ai = dict(t='AI suggests, the editor accepts',
             l='The AI points at likely rejections before the publisher sees them and proposes values like keywords. Nothing is written until the editor accepts.',
             r=['It learns from past rejection reasons. Each reason carries a field and a category, so they can be counted per team and per region.',
                'A broken rule is a failed check, never a guess. The AI only raises judgement calls and says how sure it is.',
                'A flag opens its field, or gets dismissed with a reason that stays on record.'])
    F.append(lambda n, nav: zoom(n, f_ai, [
        dict(h='Learns from rejections', hl=[(76, 16, 22, 10.6)], ctx=(76, 12.5, 22, 1)),
        dict(h='Rules and AI stay apart', hl=[(76.8, 23.2, 6.4, 2.4), (76.8, 36.6, 6.4, 2.4), (76.8, 49.9, 6.4, 2.4)], ctx=(76, 12.5, 22, 1)),
        dict(h='Nothing written on its own', hl=[(95.2, 17, 2.6, 3.2), (95.2, 28.5, 2.6, 3.2), (95.2, 41.9, 2.6, 3.2)], ctx=(76, 12.5, 22, 41))], [IMG_EP2],
        after=sub('Rules and AI, side by side', 'Rule checks pass or fail. AI suggestions name their evidence, and a dismissed flag stays on record.') + media_box(EMB('e76ad60f')), nav=nav))
    # artwork
    f_art = dict(t='Artwork is chosen by taste, not by country',
             l='Most viewing starts from a recommendation, so the thumbnail does much of the selling. Taste predicts a click better than age or location, so each season carries one thumbnail per taste cluster.',
             r=['Action, drama, romance and mystery fans each see the scene most likely to make them click.',
                'Variants are tested against each other in each region, with the time left on the test, so the editor knows when the artwork is final.',
                'Each variant shows its click-through rate, and the leader is marked.'])
    F.append(lambda n, nav: zoom(n, f_art, [
        dict(h='One thumbnail per taste', hl=[(6.2, 44, 66.4, 20.4)], ctx=(6.2, 40.5, 1, 1)),
        dict(h='A/B tested per region', hl=[(55.4, 40.4, 17.4, 3.2), (33, 59.6, 6, 2.8), (49.8, 59.6, 6, 2.8), (66.6, 59.6, 6, 2.8)]),
        dict(h='Backed by click-through', hl=[(6.2, 59.2, 15.8, 5), (22.8, 61.2, 4.4, 2.4), (39.6, 61.2, 4.4, 2.4), (56.4, 61.2, 4.4, 2.4)], ctx=(6.2, 40.5, 1, 1))], [IMG_SEASON], nav=nav))
    # row actions
    f_row = dict(t='Each row offers only its next step',
             l='Review while an episode waits, Publish once it’s approved. Checks only prove the fields are filled; judgement on ratings, artwork and sync stays with the publisher.')
    F.append(lambda n, nav: simple(n, f_row, EMB('1ee3cd39'), nav=nav))
    # assets
    f_as = dict(t='Every file sits under the content it belongs to',
             l='A missing file shows as a gap on its film or episode, before the delivery gets rejected.',
             r=['Each film or episode shows how complete its files are, like 2 of 7.',
                'Content groups files under their film or episode; Files lists them all for bulk work. Language and type are filters.'])
    F.append(lambda n, nav: zoom(n, f_as, [
        dict(h='A file count on every row', hl=[(83.4, 70.8, 11.6, 22.6)]),
        dict(h='Two views, two filters', hl=[(5, 66.2, 55, 4.4), (87.2, 66.2, 11.4, 4.2)])], [IMG_AS],
        after=sub('Filtering down to one delivery', 'Content narrows the list to Lupin, Files lists every file in it, and the batch filter finds the files from one delivery.') + media_box(EMB('8364b5b0')), nav=nav))
    # locked
    f_lock = dict(t='Once review starts, content is locked',
             l='After approval, a change needs an edit request. It’s for news from outside, like a new regional age rating. Fixing approved work isn’t what it’s for.')
    F.append(lambda n, nav: simple(n, f_lock, EMB('59ab0c6b'), nav=nav))
    titles = [f_region['t'], f_fill['t'], f_up['t'], f_rej['t'], f_ai['t'], f_art['t'], f_row['t'], f_as['t'], f_lock['t']]
    ix = ''.join(f'<li><a href="#f-{i}"><em>{i:02d}</em><span>{t}</span></a></li>' for i, t in enumerate(titles, 1))
    index = ('<div class="bl2-t"><span class="cs-num bl2-x">05</span><span class="cs-title bl2-x">Features</span><p class="k">Features</p>'
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
            '<p class="bl2-big" data-big><span class="bl2-line">The work is not hard.</span><span class="bl2-line">The loop is.</span></p>'
            + split('The problem', '<p>Getting one episode ready for one region means matching its files, filling about forty fields and passing a publisher’s review. '
                    'Much of it is typing what the file already says, and mistakes only surface at review, where each one costs a round.</p>')
            + f'<div class="bl2-cards">{cards}</div></div>')

def north_star():
    return ('<div class="bl2-t"><span class="cs-num bl2-x">02</span><p class="k">North star</p>'
            '<h2 class="bl2-h cs-title">From delivery to release-ready, in fewer steps</h2>'
            '<p class="lead">Every decision on this page answers one question: does it get an episode release-ready sooner, with less typing and fewer rounds of review?</p>'
            + split('The bet', '<p>My bet: most of the delay is retyping and rework, not the work itself. If the file fills what it can and feedback points at fields, time to release-ready drops. I haven’t tested it with an editor yet.</p>')
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
    return ('<div class="bl2-t"><span class="cs-num bl2-x">03</span><p class="k">Research</p>'
            '<h2 class="bl2-h cs-title">Eight tools, each solving part of the job</h2>'
            '<p class="lead">Streaming CMSs are built in-house and rarely shown, so I studied the tools that cover pieces of the workflow: headless CMSs, a video platform, '
            'creative review tools, and GitHub’s pull request review, where a reviewer comments on an exact line and the author resolves each comment.</p></div>'
            + media_box(benchmark()))

# ---------- two roles: the screens as steps, dashboards then workspaces ----------
def roles():
    cards = ('<div class="bl2-roles">'
             '<div class="bl2-role"><div class="bl2-rh"><span>Editor</span><span class="bl2-pill">All day</span></div><p class="bl2-q">“What’s blocking release, and what can I clear today?”</p>'
             '<p class="bl2-sub">Works region by region, many episodes at once.</p><ul class="bl2-ck"><li>Files that still need an episode</li><li>What each region still needs</li><li>Which field a rejection points at</li></ul></div>'
             '<div class="bl2-role"><div class="bl2-rh"><span>Publisher</span><span class="bl2-pill">Per review</span></div><p class="bl2-q">“What airs first, and what changed since I last looked?”</p>'
             '<p class="bl2-sub">Decides before a release date, can’t re-check everything.</p><ul class="bl2-ck"><li>The queue sorted by release date</li><li>Only the fields that came back</li><li>Reasons tied to fields, not a note</li></ul></div></div>')
    top = ('<div class="bl2-t"><span class="cs-num bl2-x">04</span><p class="k">Two roles</p>'
           '<h2 class="bl2-h cs-title">One episode, two people asking different questions</h2>' + cards + '</div>')
    full = dict(z=1, x=50, y=50)
    dash = zoom(0, dict(r=['Blockers, counts and the work the editor left off, on one page.',
                           'What airs soon, what waits for review, and what each region has received.',
                           'The editor’s counts start with Rejected, the publisher’s with Pending review: each role sees first what needs them.',
                           'The editor’s banner names files that couldn’t be assigned. The publisher’s names the one item that airs within seven days and still needs a decision.',
                           'Missing fields grouped across everything assigned to the editor, so one pass fills the Spanish synopsis for seven items.',
                           'In place of blockers, the publisher sees each region’s deliveries this week and how far along they are.']),
                [dict(h='Editor dashboard', m=0, **full),
                 dict(h='Publisher dashboard', m=1, **full),
                 dict(h='Counts that follow the role', m=1, hl=[(19.3, 20.2, 54.4, 13)]),
                 dict(h='A banner for today’s blocker', m=0, hl=[(19.3, 10, 54.4, 7.6)]),
                 dict(h='What is blocking, grouped by field', m=0, hl=[(74.8, 55.4, 23.4, 41.6)]),
                 dict(h='Deliveries this week, per region', m=1, hl=[(74.8, 66.2, 23.4, 30.6)])],
                [IMG_ED_DASH, IMG_PUB_DASH], head_html=sub('Dashboards', 'Where each role starts the day.'))
    work = zoom(0, dict(r=['The editor’s work, sorted by status, with rejections underneath.',
                           'The publisher’s queue, with every past decision underneath.',
                           'Both rails use the same statuses, so editor and publisher talk about the same thing.',
                           'The publisher’s queue is sorted by release date and shows how long each item has waited. The editor’s table shows blockers in that place.',
                           'Rejected work sits as cards, so the reason shows before the item opens.',
                           'Every decision stays on record, with who decided and when.']),
                [dict(h='Editor workspace', m=0, **full),
                 dict(h='Publisher reviews', m=1, **full),
                 dict(h='The same statuses on both sides', m=0, hl=[(19.4, 24.6, 15.4, 31)]),
                 dict(h='Sorted by what airs first', m=1, hl=[(75.4, 24.6, 12, 36.4)]),
                 dict(h='Rejections as cards', m=0, hl=[(19.4, 64.6, 79, 28.6)]),
                 dict(h='Review history', m=1, hl=[(19.4, 64.4, 79, 33)])],
                [IMG_ED_WORK, IMG_PUB_WORK], head_html=sub('Workspaces', 'Where the work itself happens.'))
    return top + dash + work

def head2(n, k, h, lead=''):
    return (f'<span class="cs-num bl2-x">{n:02d}</span><p class="k">{k}</p><h2 class="bl2-h cs-title">{h}</h2>'
            + (f'<p class="lead">{lead}</p>' if lead else ''))

def bilge():
    hero = ('<div class="bl2-t bl2-hero"><span class="cs-num bl2-x">00</span><span class="cs-title bl2-x">Overview</span>'
            '<p class="k">BİLGE, the customs platform of the Turkish Ministry of Trade</p><h1>Container tracking for Turkish customs</h1>'
            '<div class="bl2-hg"><p class="lead">BİLGE is the Ministry of Trade’s customs platform, made of dozens of modules, and I designed across many of them. '
            'This page shows KLTS, container and port tracking, designed from the system specifications and backend rules so every screen offers only what the system allows.</p>'
            '<div class="bl2-meta"><div><b>Company</b>MilSOFT</div><div><b>Client</b>Turkish Ministry of Trade</div>'
            '<div><b>My role</b>UX/UI Designer</div><div><b>Date</b>2022 to 2023</div></div></div>'
            + media_box(f'<img class="bl2-img" src="{GH}shots/bilge/b-detail.webp" width="1920" height="1080" alt="Container tracking form detail as a customs officer sees it: the agent’s details above the containers and their parts">') + '</div>')
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
            + split('Team', '<p>Five designers, a product manager, a systems engineer, and back-end and front-end engineers with their team leads.</p>')
            + split('What I owned in KLTS', '<p>The agent’s form, the officer’s approval and query flows, time extensions, corrections, cancellations, the container history, the declaration comparison and closing a form with an official report: 107 screens in KLTS alone.</p>')
            + split('Design system', '<p>The platform’s design system was created by Dilmin Doğan and Gizem Turan Yücel. I added to it where these flows needed something it did not have.</p>')
            + '</div>')
    V = lambda k: dict(type='video', src=GH + f'bilge/{k}.mp4', poster=GH + f'bilge/{k}.jpg', w=1600, h=900)
    def flow(n, k, h, lead, steps, texts, medias, after=''):
        return zoom(0, dict(r=texts), steps, medias, head_html=head2(n, k, h, lead), after=after)
    POP = (37, 25, 26, 39)
    agent = flow(4, 'The agent files', 'General information first, then the containers',
                 'The agent picks the movement (foreign or domestic, entry or exit), fills in general information, then adds containers one by one or in bulk. Until an officer approves the form, the agent can still edit it.',
                 [dict(h='General information first', t=4.45, hl=[(33.5, 25.5, 36.5, 50)]),
                  dict(h='Parts sit under their container', t=28.5, hl=[(63.5, 53.5, 35.5, 9)]),
                  dict(h='Every container before sending', t=30.5, hl=[(34, 29, 63, 22)]),
                  dict(h='Register, not Save', t=32.3, hl=[POP]),
                  dict(h='Waiting for an officer', t=36.6, hl=[(42, 9, 31.5, 4.5), (20, 29.5, 72, 3)])],
                 ['Every container on the form shares it, so the agent fills it once. Picking a tax ID fills in the company details.',
                  'Each container carries its own parts and equipment, so nothing is filed against the wrong one.',
                  'The list shows each container’s route, weight and parts before anything is sent.',
                  'At the ministry’s request the last button says Register: from that moment the form is binding.',
                  'The confirmation gives the registration number, and the form moves to the pending list.'],
                 [V('a')])
    track = flow(5, 'Tracking a container', 'Every source and every event in one place',
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
    customs = flow(6, 'Customs decides', 'Officers and managers act from their queue',
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
    learned = ('<div class="bl2-t">' + head2(7, 'What I learned', 'In government software the wording is part of the design')
               + split('Wording', '<p>A word like Register carries legal weight, so ministry review shaped the design from the start.</p>')
               + split('Next time', '<p>Specs from the client were sometimes wrong, and we found out only after the screens were designed, which meant redesigns. Next time I would walk each flow through with the analyst against the regulation before designing it.</p>')
               + split('How I built this page', '<p>The flows, screens and design system additions are my work at MilSOFT. The real system holds customs data, so I rebuilt the screens in Claude Design from the originals with placeholder data and checked each one against them.</p>')
               + '</div>')
    w1 = (sec('ov', 'Overview', hero) + sec('gl', 'At a glance', glance) + sec('dm', 'Working from specs', specs) + sec('mr', 'My role', role)
          + sec('ag', 'The agent files', agent) + sec('tr', 'Tracking a container', track) + sec('cu', 'Customs decides', customs)
          + sec('le', 'What I learned', learned))
    nb = (nbthumb(P['78fe6fd2-fd22-0eb4-d2e4-629e35df69b3'], WF + '691de9a378fcaab7283af4c8_HomePage%20(1)%20(1)-p-1080.png').replace('href="/work"', 'href="/uwaverde"')
          .replace('<span>BİLGE</span>', '<span>UwaVerde</span>')
          .replace('Customs approvals where every change carries a reason.', 'NGO website and member portal.')
          )
    body = f'<main class="bl2-page"><div class="cs-wrap" data-bl2root="1"><nav class="bl-nav" aria-label="Case study sections"><ol></ol></nav>{w1}</div>{nb}</main>'
    return page('BİLGE container tracking case study | Ege Coskun',
                'BİLGE KLTS: container and port tracking for Turkish customs. Approval chains across agents, officers and managers, built on an existing design system.',
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
    nb = (P['78fe6fd2-fd22-0eb4-d2e4-629e35df69b3'].replace('href="/work"', 'href="/fieldfriends"')
          .replace('<span>BİLGE</span>', '<span>FieldFriends</span>')
          .replace('Customs approvals where every change carries a reason.', 'Precision farming app.')
          .replace('<b>Pending Approval</b>', '<b>Field map</b>'))
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
    write('assets/backlot.js', nav_js + '\n' + rd('bl2.js') + '\n' + vid_js + '\n' + rd('zoom.js') + '\n' + rd('roles.js') + '\n' + rd('pace.js'))
    write('assets/site.js', rd('site.js'))
    html = backlot()
    a, b = html.index('<main'), html.index('</main>')
    html = html[:a] + re.sub(r'<style>.*?</style>', '', html[a:b], flags=re.S) + html[b:]
    write('backlot/index.html', html)
    write('bilge/index.html', bilge())
    write('uwaverde/index.html', uwaverde())
    print('built', len(html))
