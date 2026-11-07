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
# --- Taken out
I['Availability as a ninth'] = svg(''.join(f'<rect x="{i*22}" y="24" width="16" height="16" rx="8"/>' for i in range(8))
    + f'<g class="mv"><rect x="178" y="24" width="16" height="16" rx="8" stroke="{A}" stroke-dasharray="3 3"/><path d="M174 46 L198 18" stroke="{A}"/></g>')
I['An AI score'] = svg('<rect x="0" y="26" width="140" height="12" rx="6"/>' + f'<rect x="0" y="26" width="100" height="12" rx="6" fill="{A}" fill-opacity=".28" stroke="none"/>'
    + '<text x="152" y="38" font-size="15" font-weight="600" fill="currentColor" stroke="none" font-family="Manrope,sans-serif">72%</text>'
    + f'<path class="mv" d="M148 46 L196 20" stroke="{A}"/>')
I['Rejections first'] = svg('<rect x="0" y="14" width="58" height="24" rx="8"/><rect x="66" y="14" width="58" height="24" rx="8"/><rect x="132" y="14" width="58" height="24" rx="8"/>'
    + '<path d="M12 26 H34 M78 26 H100 M144 26 H166"/>' + f'<circle cx="46" cy="26" r="3" fill="{A}" stroke="none"/>'
    + f'<g class="mv"><path d="M29 50 C 70 62, 130 62, 161 50" stroke="{A}"/><path d="M155 46 L162 50 L154 54" stroke="{A}"/></g>')
I['Bulk unlock'] = svg(''.join(f'<rect x="0" y="{3+i*16}" width="150" height="10" rx="3"/>' for i in range(4))
    + ''.join(f'<g class="{"mv" if i == 0 else ""}">' + lock(166, 3 + i*16, i == 0) + '</g>' for i in range(4)))
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
I['One form'] = svg('<rect x="0" y="2" width="120" height="60" rx="6"/><rect x="12" y="14" width="96" height="8" rx="3"/><rect x="12" y="29" width="96" height="8" rx="3"/><rect x="12" y="44" width="60" height="8" rx="3"/>'
    + ''.join(f'<circle cx="{150+i%2*30}" cy="{18+i//2*28}" r="11"' + (f' stroke="{A}" fill="{A}" fill-opacity=".22"' if i == 0 else '') + '/>' for i in range(4)))
I['Sources side by side'] = svg('<rect x="0" y="4" width="90" height="56" rx="6"/><rect x="110" y="4" width="90" height="56" rx="6"/>'
    + ''.join(f'<path d="M12 {y} H78 M122 {y} H188"/>' for y in (18, 46))
    + f'<g class="mv"><path d="M12 32 H78" stroke="{A}"/><path d="M122 32 H160" stroke="{A}"/></g><path d="M94 32 H106" stroke="{A}" stroke-dasharray="2 3"/>')
I['Registering is binding'] = svg('<rect x="0" y="20" width="84" height="24" rx="12"/><path d="M20 32 H56"/><path d="M50 27 L57 32 L50 37"/>'
    + f'<g class="mv"><circle cx="150" cy="32" r="24" stroke="{A}"/><path d="M150 18 V32 L160 38" stroke="{A}"/></g><path d="M92 32 H120" stroke-dasharray="2 3"/>')
def add(html):
    def f(m):
        t = m.group(3).replace('&rsquo;', '’')
        for k, v in I.items():
            if t.startswith(k):
                return m.group(1) + v + m.group(2) + '<h3>' + m.group(3)
        return m.group(0)
    return re.sub(r'(<div class="bl2-c">)(<span class="bl2-tag">(?:Finding|Taken out|Decision \d)</span>)<h3>([^<]*)', f, html)
CSS = (".bl2-ill{display:block;order:-2;margin:0 0 18px;color:var(--ink);opacity:.85}.bl2-ill svg{display:block;width:min(100%,200px);height:auto;overflow:visible}"
       ".bl2-ill .mv{transition:transform .5s var(--ease),opacity .4s;transform-box:fill-box}"
       ".bl2-c:hover .bl2-ill .mv{transform:translateX(5px)}"
       "@media (prefers-reduced-motion:reduce){.bl2-ill .mv{transition:none}.bl2-c:hover .bl2-ill .mv{transform:none}}")
