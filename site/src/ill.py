"""Small line illustrations for the text-only Backlot cards (Findings, Taken out)."""
import re
A = '#728437'
def svg(b):
    return ('<span class="bl2-ill" aria-hidden="true"><svg viewBox="0 0 200 64" width="200" height="64" fill="none" stroke="currentColor" '
            'stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" focusable="false">' + b + '</svg></span>')
def lock(x, y, op):
    c = f' stroke="{A}"' if op else ''
    sh = f'M{x+2.5} {y+3} V{y+1.5} a2.5 2.5 0 0 1 5 0' + ('' if op else f' V{y+3}')
    return f'<rect x="{x}" y="{y+3}" width="10" height="7" rx="1.5"{c}/><path d="{sh}"{c}/>'
I = {}
# --- Findings
doc = lambda x, d='': f'<path d="M{x} 6 H{x+32} L{x+44} 18 V58 H{x} Z"{d}/><path d="M{x+32} 6 V18 H{x+44}"{d}/>'
I['Files arrive broken'] = svg(doc(8) + doc(78, f' stroke="{A}" stroke-dasharray="3 3"') + doc(148)
    + f'<text class="mv" x="93" y="44" font-size="18" font-weight="700" fill="{A}" stroke="none" font-family="Manrope,sans-serif">?</text>')
I['Almost every field'] = svg(''.join(f'<rect x="0" y="{4+i*20}" width="130" height="12" rx="4"/><rect class="{"mv" if i==2 else ""}" x="142" y="{2+i*20}" width="48" height="16" rx="8" stroke="{A if i==1 else "currentColor"}"/>'
    f'<text x="166" y="{14+i*20}" text-anchor="middle" font-size="9" font-weight="600" fill="currentColor" stroke="none" font-family="Manrope,sans-serif">{t}</text>' for i, t in enumerate(['DE', 'TR', 'US'])))
I['Mistakes hide'] = svg('<rect x="70" y="2" width="60" height="14" rx="4"/><path d="M100 16 V30 M40 30 H160 M40 30 V44 M100 30 V44 M160 30 V44"/>'
    + ''.join(f'<rect x="{x-20}" y="44" width="40" height="14" rx="4"/>' for x in (40, 100, 160))
    + f'<circle class="mv" cx="116" cy="9" r="3.5" fill="{A}" stroke="none"/>' + ''.join(f'<circle cx="{x+10}" cy="51" r="3.5"/>' for x in (40, 100, 160)))
I['Feedback doesn'] = svg(''.join(f'<rect x="0" y="{6+i*18}" width="96" height="10" rx="3"/>' for i in range(3))
    + f'<g class="mv"><rect x="118" y="4" width="76" height="30" rx="8" stroke="{A}"/><path d="M126 18 H170 M126 25 H156" stroke="{A}"/></g>'
    + f'<path d="M122 34 C 112 44, 108 48, 104 50" stroke="{A}" stroke-dasharray="3 3"/>')
I['One form'] = svg('<rect x="84" y="2" width="32" height="16" rx="4"/><path d="M92 8 H108 M92 12 H102"/><path d="M100 18 V26 M24 26 H176 M24 26 V32 M72 26 V32 M128 26 V32 M176 26 V32"/>'
    + ''.join(f'<circle class="r" style="animation-delay:{i*.8}s" cx="{x}" cy="44" r="11"' + (f' stroke="{A}"' if i == 0 else '') + f'/><text x="{x}" y="48" text-anchor="middle" font-size="11" font-weight="600" fill="currentColor" stroke="none" font-family="Manrope,sans-serif">{t}</text>' for i, (x, t) in enumerate([(24, 'A'), (72, 'O'), (128, 'M'), (176, 'D')])))
I['Sources side by side'] = svg(''.join(f'<path d="M0 {y} H78 M122 {y} H{200 if y != 40 else 170}"/>' for y in (10, 25, 55))
    + '<path d="M0 40 H78"/>' + ''.join(f'<path d="M92 {y-2} H108 M92 {y+2} H108"/>' for y in (10, 25, 55))
    + f'<g class="mv"><path d="M122 40 H162" stroke="{A}"/></g><path d="M92 38 H108 M92 42 H108 M96 45 L104 35" stroke="{A}"/>')
I['Registering is binding'] = svg('<circle cx="100" cy="32" r="27"/><path d="M100 8 V12 M124 32 H120 M100 56 V52 M76 32 H80"/>'
    + f'<path d="M100 5 A27 27 0 0 1 127 32" stroke="{A}" stroke-width="3"/><path d="M100 32 L100 18"/><path class="rot" d="M100 32 L112 38" stroke="{A}"/><circle cx="100" cy="32" r="2" fill="currentColor" stroke="none"/>')
def add(html):
    def f(m):
        t = m.group(3).replace('&rsquo;', '’')
        for k, v in I.items():
            if t.startswith(k):
                return m.group(1) + v + m.group(2) + '<h3>' + m.group(3)
        return m.group(0)
    return re.sub(r'(<div class="bl2-c">)(<span class="bl2-tag">(?:Finding|Decision \d)</span>)<h3>([^<]*)', f, html)
CSS = (".bl2-ill{display:block;order:-2;margin:0 0 18px;color:var(--ink);opacity:.85}.bl2-ill svg{display:block;width:min(100%,200px);height:auto;overflow:visible}"
       ".bl2-ill .mv{transition:transform .5s var(--ease),opacity .4s;transform-box:fill-box}.bl2-ill .rot{transition:transform 1.4s var(--ease);transform-origin:100px 32px}"
       ".bl2-c:hover .bl2-ill .mv{transform:translateX(5px)}.bl2-c:hover .bl2-ill .rot{transform:rotate(150deg)}"
       "@keyframes ill-cy{0%,100%{fill:none}35%,60%{fill:#728437;fill-opacity:.3}}.bl2-ill .r{animation:ill-cy 3.2s ease-in-out infinite;animation-play-state:paused}.bl2-c:hover .bl2-ill .r{animation-play-state:running}"
       "@media (prefers-reduced-motion:reduce){.bl2-ill .mv,.bl2-ill .rot{transition:none}.bl2-c:hover .bl2-ill .mv,.bl2-c:hover .bl2-ill .rot{transform:none}.bl2-ill .r{animation:none}}"
       # cards with an illustration: picture left, words right (two-column grids only); chip stays ink
       "@media(min-width:560px){.bl2-cards:not(.c3) .bl2-c:has(.bl2-ill){display:grid;grid-template-columns:clamp(120px,12vw,180px) minmax(0,1fr);column-gap:clamp(20px,2.2vw,36px);align-items:start;align-content:start}"
       ".bl2-cards:not(.c3) .bl2-c:has(.bl2-ill)>.bl2-ill{grid-column:1;grid-row:1/span 4;margin:2px 0 0}.bl2-cards:not(.c3) .bl2-c:has(.bl2-ill)>:not(.bl2-ill){grid-column:2}"
       ".bl2-cards:not(.c3) .bl2-c:has(.bl2-ill)>.bl2-tag{justify-self:start}}"
       ".bl2-c:has(.bl2-ill):hover .bl2-tag{background:var(--ink)}")
