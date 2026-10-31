# Design system showcase for the Backlot case study (ported from the Webflow section).
P16 = 'viewBox="0 0 16 16" aria-hidden="true"'
P256 = 'viewBox="0 0 256 256" fill="currentColor" aria-hidden="true"'
CIRC = '<circle cx="8" cy="8" r="6" fill="none" stroke="currentColor" stroke-width="1.6"/>'
DASH = '<circle cx="8" cy="8" r="6" fill="none" stroke="currentColor" stroke-width="1.6" stroke-dasharray="2.6 2.1"/>'
ICON = {
 'todo': CIRC,
 'prog': DASH,
 'pend': DASH + '<path fill="currentColor" d="M8 8V4.2A3.8 3.8 0 0 1 11.8 8Z"/>',
 'rev': CIRC + '<path fill="currentColor" d="M8 4.2a3.8 3.8 0 0 1 0 7.6Z"/>',
 'appr': '<circle cx="8" cy="8" r="6.8" fill="currentColor"/><path d="M5.3 8.2l1.8 1.8 3.6-3.8" fill="none" stroke="#16241b" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round"/>',
 'sched': '<circle cx="8" cy="8" r="6.8" fill="currentColor"/><path d="M8 4.8V8l2.3 1.4" fill="none" stroke="#241d28" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"/>',
 'pub': '<circle cx="8" cy="8" r="4" fill="currentColor"/>',
 'rej': CIRC + '<path d="M5.9 5.9l4.2 4.2M10.1 5.9l-4.2 4.2" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/>',
}
CHIP = {'todo': ('To do', 'c-todo'), 'prog': ('In progress', 'c-prog'), 'pend': ('Pending review', 'c-pend'), 'rev': ('In review', 'c-rev'),
        'appr': ('Approved', 'c-appr'), 'sched': ('Scheduled', 'c-sched'), 'pub': ('Published', 'c-pub'), 'rej': ('Rejected', 'c-rej')}
def chip(k, extra=''):
    label, cls = CHIP[k]
    return f'<span class="ds-chip {cls}{extra}"><svg {P16}>{ICON[k]}</svg><span>{label}</span></span>'

PH = {
 'verified': 'M225.86,102.82c-3.77-3.94-7.67-8-9.14-11.57-1.36-3.27-1.44-8.69-1.52-13.94-.15-9.76-.31-20.82-8-28.51s-18.75-7.85-28.51-8c-5.25-.08-10.67-.16-13.94-1.52-3.56-1.47-7.63-5.37-11.57-9.14C146.28,23.51,138.44,16,128,16s-18.27,7.51-25.18,14.14c-3.94,3.77-8,7.67-11.57,9.14C88,40.64,82.56,40.72,77.31,40.8c-9.76.15-20.82.31-28.51,8S41,67.55,40.8,77.31c-.08,5.25-.16,10.67-1.52,13.94-1.47,3.56-5.37,7.63-9.14,11.57C23.51,109.72,16,117.56,16,128s7.51,18.27,14.14,25.18c3.77,3.94,7.67,8,9.14,11.57,1.36,3.27,1.44,8.69,1.52,13.94.15,9.76.31,20.82,8,28.51s18.75,7.85,28.51,8c5.25.08,10.67.16,13.94,1.52,3.56,1.47,7.63,5.37,11.57,9.14C109.72,232.49,117.56,240,128,240s18.27-7.51,25.18-14.14c3.94-3.77,8-7.67,11.57-9.14,3.27-1.36,8.69-1.44,13.94-1.52,9.76-.15,20.82-.31,28.51-8s7.85-18.75,8-28.51c.08-5.25.16-10.67,1.52-13.94,1.47-3.56,5.37-7.63,9.14-11.57C232.49,146.28,240,138.44,240,128S232.49,109.73,225.86,102.82Zm-11.55,39.29c-4.79,5-9.75,10.17-12.38,16.52-2.52,6.1-2.63,13.07-2.73,19.82-.1,7-.21,14.33-3.32,17.43s-10.39,3.22-17.43,3.32c-6.75.1-13.72.21-19.82,2.73-6.35,2.63-11.52,7.59-16.52,12.38S132,224,128,224s-9.15-4.92-14.11-9.69-10.17-9.75-16.52-12.38c-6.1-2.52-13.07-2.63-19.82-2.73-7-.1-14.33-.21-17.43-3.32s-3.22-10.39-3.32-17.43c-.1-6.75-.21-13.72-2.73-19.82-2.63-6.35-7.59-11.52-12.38-16.52S32,132,32,128s4.92-9.15,9.69-14.11,9.75-10.17,12.38-16.52c2.52-6.1,2.63-13.07,2.73-19.82.1-7,.21-14.33,3.32-17.43S70.51,56.9,77.55,56.8c6.75-.1,13.72-.21,19.82-2.73,6.35-2.63,11.52-7.59,16.52-12.38S124,32,128,32s9.15,4.92,14.11,9.69,10.17,9.75,16.52,12.38c6.1,2.52,13.07,2.63,19.82,2.73,7,.1,14.33.21,17.43,3.32s3.22,10.39,3.32,17.43c.1,6.75.21,13.72,2.73,19.82,2.63,6.35,7.59,11.52,12.38,16.52S224,124,224,128,219.08,137.15,214.31,142.11ZM173.66,98.34a8,8,0,0,1,0,11.32l-56,56a8,8,0,0,1-11.32,0l-24-24a8,8,0,0,1,11.32-11.32L112,148.69l50.34-50.35A8,8,0,0,1,173.66,98.34Z',
 'source': 'M223.68,66.15,135.68,18a15.88,15.88,0,0,0-15.36,0l-88,48.17a16,16,0,0,0-8.32,14v95.64a16,16,0,0,0,8.32,14l88,48.17a15.88,15.88,0,0,0,15.36,0l88-48.17a16,16,0,0,0,8.32-14V80.18A16,16,0,0,0,223.68,66.15ZM128,32l80.34,44-29.77,16.3-80.35-44ZM128,120,47.66,76l33.9-18.56,80.34,44ZM40,90l80,43.78v85.79L40,175.82Zm176,85.78h0l-80,43.79V133.82l32-17.51V152a8,8,0,0,0,16,0V107.55L216,90v85.77Z',
 'unlock': 'M208,80H96V56a32,32,0,0,1,32-32c15.37,0,29.2,11,32.16,25.59a8,8,0,0,0,15.68-3.18C171.32,24.15,151.2,8,128,8A48.05,48.05,0,0,0,80,56V80H48A16,16,0,0,0,32,96V208a16,16,0,0,0,16,16H208a16,16,0,0,0,16-16V96A16,16,0,0,0,208,80Zm0,128H48V96H208V208Z',
 'lock': 'M208,80H176V56a48,48,0,0,0-96,0V80H48A16,16,0,0,0,32,96V208a16,16,0,0,0,16,16H208a16,16,0,0,0,16-16V96A16,16,0,0,0,208,80ZM96,56a32,32,0,0,1,64,0V80H96ZM208,208H48V96H208V208Z',
 'spark': 'M197.58,129.06,146,110l-19-51.62a15.92,15.92,0,0,0-29.88,0L78,110l-51.62,19a15.92,15.92,0,0,0,0,29.88L78,178l19,51.62a15.92,15.92,0,0,0,29.88,0L146,178l51.62-19a15.92,15.92,0,0,0,0-29.88ZM137,164.22a8,8,0,0,0-4.74,4.74L112,223.85,91.78,169A8,8,0,0,0,87,164.22L32.15,144,87,123.78A8,8,0,0,0,91.78,119L112,64.15,132.22,119a8,8,0,0,0,4.74,4.74L191.85,144ZM144,40a8,8,0,0,1,8-8h16V16a8,8,0,0,1,16,0V32h16a8,8,0,0,1,0,16H184V64a8,8,0,0,1-16,0V48H152A8,8,0,0,1,144,40ZM248,88a8,8,0,0,1-8,8h-8v8a8,8,0,0,1-16,0V96h-8a8,8,0,0,1,0-16h8V72a8,8,0,0,1,16,0v8h8A8,8,0,0,1,248,88Z',
 'check': 'M229.66,77.66l-128,128a8,8,0,0,1-11.32,0l-56-56a8,8,0,0,1,11.32-11.32L96,188.69,218.34,66.34a8,8,0,0,1,11.32,11.32Z',
 'pencil': 'M227.31,73.37,182.63,28.68a16,16,0,0,0-22.63,0L36.69,152A15.86,15.86,0,0,0,32,163.31V208a16,16,0,0,0,16,16H92.69A15.86,15.86,0,0,0,104,219.31L227.31,96a16,16,0,0,0,0-22.63ZM92.69,208H48V163.31l88-88L180.69,120ZM192,108.68,147.31,64l24-24L216,84.68Z',
 'chat': 'M128,24A104,104,0,0,0,36.18,176.88L24.83,210.93a16,16,0,0,0,20.24,20.24l34.05-11.35A104,104,0,1,0,128,24Zm0,192a87.87,87.87,0,0,1-44.06-11.81,8,8,0,0,0-6.54-.67L40,216,52.47,178.6a8,8,0,0,0-.66-6.54A88,88,0,1,1,128,216Z',
 'clock': 'M128,24A104,104,0,1,0,232,128,104.11,104.11,0,0,0,128,24Zm0,192a88,88,0,1,1,88-88A88.1,88.1,0,0,1,128,216Zm64-88a8,8,0,0,1-8,8H128a8,8,0,0,1-8-8V72a8,8,0,0,1,16,0v48h48A8,8,0,0,1,192,128Z',
 'plus': 'M224,128a8,8,0,0,1-8,8H136v80a8,8,0,0,1-16,0V136H40a8,8,0,0,1,0-16h80V40a8,8,0,0,1,16,0v80h80A8,8,0,0,1,224,128Z',
 'upload': 'M224,144v64a8,8,0,0,1-8,8H40a8,8,0,0,1-8-8V144a8,8,0,0,1,16,0v56H208V144a8,8,0,0,1,16,0ZM93.66,77.66,120,51.31V144a8,8,0,0,0,16,0V51.31l26.34,26.35a8,8,0,0,0,11.32-11.32l-40-40a8,8,0,0,0-11.32,0l-40,40A8,8,0,0,0,93.66,77.66Z',
 'send': 'M227.32,28.68a16,16,0,0,0-15.66-4.08l-.15,0L19.57,82.84a16,16,0,0,0-2.49,29.8L102,154l41.3,84.87A15.86,15.86,0,0,0,157.74,248q.69,0,1.38-.06a15.88,15.88,0,0,0,14-11.51l58.2-191.94c0-.05,0-.1,0-.15A16,16,0,0,0,227.32,28.68ZM157.83,231.85l-.05.14,0-.07-40.06-82.3,48-48a8,8,0,0,0-11.31-11.31l-48,48L24.08,98.25l-.07,0,.14,0L216,40Z',
 'palette': 'M200.77,53.89A103.27,103.27,0,0,0,128,24h-1.07A104,104,0,0,0,24,128c0,43,26.58,79.06,69.36,94.17A32,32,0,0,0,136,192a16,16,0,0,1,16-16h46.21a31.81,31.81,0,0,0,31.2-24.88,104.43,104.43,0,0,0,2.59-24A103.28,103.28,0,0,0,200.77,53.89Zm13,93.71A15.89,15.89,0,0,1,198.21,160H152a32,32,0,0,0-32,32,16,16,0,0,1-21.31,15.07C62.49,194.3,40,164,40,128a88,88,0,0,1,87.09-88h.9a88.35,88.35,0,0,1,88,87.25A88.86,88.86,0,0,1,213.81,147.6ZM140,76a12,12,0,1,1-12-12A12,12,0,0,1,140,76ZM96,100A12,12,0,1,1,84,88,12,12,0,0,1,96,100Zm0,56a12,12,0,1,1-12-12A12,12,0,0,1,96,156Zm88-56a12,12,0,1,1-12-12A12,12,0,0,1,184,100Z',
}
def ph(k, cls='ds-ic'):
    return f'<svg class="{cls}" {P256}><path d="{PH[k]}"/></svg>'

def field(label, value, kind='plain', icon=None):
    box = {'plain': 'ds-f', 'filled': 'ds-f ds-f-on', 'ai': 'ds-f ds-f-ai'}[kind]
    ic = ph(icon, 'ds-ic ds-mute') if icon else ''
    return f'<div class="ds-fl"><span class="ds-k">{label}</span><div class="{box}"><span class="ds-v">{value}</span>{ic}</div></div>'

def note(t): return f'<span class="ds-note">{t}</span>'
def cell(*parts): return '<div class="ds-cell">' + ''.join(parts) + '</div>'

def build():
    chips = ''.join(chip(k) for k in CHIP)
    avail = '''<div class="ds-avail"><p class="ds-rl">Progress</p><div class="ds-g"><div><span class="ds-av"><svg viewBox="0 0 16 16" aria-hidden="true"><circle cx="8" cy="8" r="6" fill="none" stroke="currentColor" stroke-width="1.4"/></svg>Not started</span><p>Nothing delivered to this region yet.</p></div><div><span class="ds-av"><svg viewBox="0 0 16 16" aria-hidden="true"><circle cx="8" cy="8" r="6" fill="none" stroke="currentColor" stroke-width="1.4"/><path d="M8 4.5a3.5 3.5 0 0 0 0 7z" fill="currentColor"/></svg>Partial</span><p>Some of the region is ready, not all of it.</p></div><div><span class="ds-av"><svg viewBox="0 0 16 16" aria-hidden="true"><circle cx="8" cy="8" r="6.5" fill="currentColor"/></svg>Ready</span><p>Everything for this region is ready.</p></div></div><p class="ds-ac">Workflow status says where the work is. Progress says how much of a region is ready.</p></div>
<div class="ds-avail"><p class="ds-rl">Availability</p><div class="ds-g"><div><span class="ds-av"><i class="ds-av-on"></i>On air</span><p>The series is still releasing episodes in this region.</p></div><div><span class="ds-av"><i class="ds-av-end"></i>Ended</span><p>Every episode is released and still watchable.</p></div><div><span class="ds-av ds-av-x"><svg viewBox="0 0 16 16" aria-hidden="true"><rect x="2.5" y="3" width="11" height="3" rx="1" fill="none" stroke="currentColor" stroke-width="1.3"/><path d="M3.5 6v6.5h9V6M6.5 9h3" fill="none" stroke="currentColor" stroke-width="1.3" stroke-linecap="round"/></svg>Expired</span><p>The rights window ended in this region. Off the service, all data kept, read-only.</p></div></div><p class="ds-ac">Not a status. Shown only on series, season and film headers and in the content library, never in a work queue. Neutral outline, no status colour.</p></div>'''
    def srow(th, name, k, date, why, spine):
        return f'<div class="ds-sr {spine}"><div class="ds-th" style="background-image:url(https://egec.github.io/backlot/ds/{th})"></div><div class="ds-nm">{name}</div><div>{chip(k)}</div><div class="ds-dt"><span>{date}</span><small>{why}</small></div></div>'
    spine = ('<div class="ds-panel"><div class="ds-spine"><div class="ds-sh"><div>Art</div><div>Content</div><div>Status</div><div>Release</div></div>'
             + srow('lupin-s4.jpg', 'Lupin, S4-E2', 'rev', '14 Feb (2d)', 'Within 7 days: amber spine', 'sp-amber')
             + srow('community.jpg', 'Community, S6-E6', 'appr', '10 Feb (2d overdue)', 'Past release, not Published: red spine', 'sp-red')
             + srow('lss.jpg', 'Long Story Short, S1-E3', 'pend', '8 Mar (24d)', 'More than 7 days out: no spine', '')
             + '</div>' + note('Driven by days until release, never by row position or waiting time. The status chip stays the same.') + '</div>')
    def prov(tag, tagcls, icon, f, n):
        return f'<div class="ds-cell"><span class="ds-tag {tagcls}">{ph(icon)}{tag}</span>{f}{note(n)}</div>'
    provs = ('<div class="ds-panel ds-prov">'
             + prov('Verified', '', 'verified', field('Runtime', '24:31'), 'Read from the media file. Cannot be edited.')
             + prov('Source', '', 'source', field('Genre', 'Crime, Drama', icon='unlock'), 'From the delivery. Unlock to edit.')
             + prov('Suggested', 'ds-tag-ai', 'spark', '<div class="ds-fl"><span class="ds-k">Keywords</span><div class="ds-f ds-f-ai">' + ph('spark', 'ds-ic ds-ai') + '<span class="ds-v ds-strong">Heist, Paris, revenge</span>' + ph('check', 'ds-ic ds-ai') + '</div></div>', 'Proposed by the system. Nothing is written until you accept.')
             + prov('Manual', '', 'pencil', field('Localised title (ES)', '<span class="ds-strong">El collar de la reina</span>', 'filled'), 'Typed by an editor. Pinned against the next delivery.')
             + '</div>')
    lockf = lambda: field('Age rating', '12', icon='lock')
    def prow(label, ch, a, b, last=False):
        return f'<div class="ds-pr{" ds-pr-last" if last else ""}"><div class="ds-cell"><span class="ds-pl">{label}</span>{ch}</div>{a}{b}</div>'
    review_row = ('<div class="ds-cell"><div class="ds-fl"><span class="ds-k ds-ghost">Age rating</span><div class="ds-rr"><span class="ds-k">Age rating</span><span class="ds-strong">12</span><span class="ds-rra">'
                  + ph('check', 'ds-ic ds-dim') + '<span class="ds-addc">' + ph('chat', 'ds-ic ds-sm') + 'Add comment</span></span></div></div>'
                  + note('The review row from the publisher review screen. Add comment appears on hover or keyboard focus.') + '</div>')
    req = ('<div class="ds-cell"><div class="ds-req"><span class="ds-reqn">Season details</span><span class="ds-reqb">' + ph('lock', 'ds-ic ds-sm') + 'Requested</span></div>'
           + '<span class="ds-reqs">' + ph('clock', 'ds-ic ds-sm') + 'Edit requested, waiting for Maya Okafor</span>' + lockf() + note('One Unlock per section. It sends a request, not an edit.') + '</div>')
    req2 = ('<div class="ds-cell"><div class="ds-req ds-ghost"><span class="ds-reqn">Season details</span><span class="ds-reqb">Requested</span></div><span class="ds-reqs ds-ghost">Edit requested</span>'
            + lockf() + note('The request reaches Maya Okafor. The section stays locked until she reopens it.') + '</div>')
    btn = lambda t, ic=None, cls='ds-btn': f'<span class="{cls}">' + (ph(ic) if ic else '') + t + '</span>'
    act1 = ('<div class="ds-cell"><div class="ds-acts"><span class="ds-k">Dashboard</span>' + btn('Create', 'plus') + '<span class="ds-k">Content page</span>' + btn('Upload', 'upload')
            + '<span class="ds-k">In progress</span>' + btn('Submit for review') + '</div>' + note('One primary per view: Create on dashboards, Upload once a content item is open, Submit for review in the page body.') + '</div>')
    act2 = ('<div class="ds-cell"><div class="ds-acts"><span class="ds-k">In review</span><div class="ds-pair">' + btn('Reject', cls='ds-btn2') + btn('Approve', 'check', 'ds-btn ds-btn-s')
            + '</div><span class="ds-k">Approved</span>' + btn('Publish', 'send') + '</div>' + note('One primary per view: Approve while reviewing (Reject beside it, same height), Publish once approved.') + '</div>')
    perms = ('<div class="ds-panel ds-perm"><div class="ds-ph"><span></span><span class="ds-who"><i style="background-image:url(https://egec.github.io/backlot/ds/rivard.png)"></i>Editor, Alex Rivard</span><span class="ds-who"><i style="background-image:url(https://egec.github.io/backlot/ds/okafor.png)"></i>Publisher, Maya Okafor</span></div>'
             + prow('Editable', chip('prog'), cell(field('Age rating', '<span class="ds-strong">12</span>', 'filled'), note('Editable until the editor submits.')), cell(field('Age rating', '12'), note('Visible, not editable. Nothing to review yet.')))
             + prow('Locked once review starts', chip('rev'), cell(lockf(), note('The same row, locked while Maya Okafor reviews.')), review_row)
             + prow('Read-only', chip('appr'), cell(lockf(), note('Approved and locked. No per-field unlock.')), cell(lockf(), note('Approved 3 Feb by Maya Okafor. Locked here too.')))
             + prow('Edit request', chip('appr'), req, req2)
             + prow('Primary action', '', act1, act2, True)
             + '</div>')
    sw = lambda c, extra='': f'<i class="ds-sw" style="background:{c}{extra}"></i>'
    found = ('<div class="ds-panel ds-found"><span class="ds-tag">' + ph('palette') + 'Colour by meaning</span>'
             + '<div class="ds-cell"><span class="ds-k">Status</span><div class="ds-sws">' + ''.join(sw(c) for c in ['#A9B6C6', '#E8A6C4', '#8FC2EF', '#8FD4A6', '#D4B0E8', '#F0A19A', '#A3A196', '#89887D']) + '</div>' + note('One hue per status, except Published, which stays neutral. Never accent, never amber.') + '</div>'
             + '<div class="ds-cell"><span class="ds-k">Provenance</span><div class="ds-sws"><i class="ds-sw" style="border:1px solid #3A3937"></i><i class="ds-sw ds-sw-ai">' + ph('spark', 'ds-ic ds-ai ds-sm') + '</i><i class="ds-sw" style="background:#191919;border:1px solid #5C5954"></i></div>' + note('Measured and asserted share a quiet edge. Suggested gets an accent edge and a sparkle. Manual lifts one step.') + '</div>'
             + '<div class="ds-cell"><span class="ds-k">AI</span><div class="ds-sws"><i class="ds-sw" style="background:#D2CEFD"></i><i class="ds-sw" style="background:rgba(145,132,217,.12);border:1px solid #423A6A"></i></div>' + note('Accent 300 ink and the 12% tint. A proposal, never a fill.') + '</div>'
             + '<div class="ds-cell"><span class="ds-k">Urgency</span><div class="ds-sws"><i class="ds-sw" style="background:#D2983F"></i><i class="ds-sw" style="background:#EC5B57"></i></div>' + note('Amber inside 7 days of release. Red once release has passed.') + '</div></div>')
    sec = lambda t, lead, body: f'<div class="ds-sec"><h3 class="ds-title">{t}</h3>' + (f'<p class="ds-lead">{lead}</p>' if lead else '') + body + '</div>'
    return ('<section class="cs-dsec" data-nav-label="Design system" id="design-system"><div class="ds-in"><div class="ds-head"><span class="cs-num">07</span><h2 class="cs-title">Design system</h2></div><div class="ds-show">'
            + sec('Eight states, one icon family.', 'Status tells you where the work is. Availability tells you what viewers can see. Two layers, and availability is never a ninth status.',
                  '<div class="ds-panel ds-chips"><p class="ds-rl">Workflow status</p>' + chips + '</div>' + avail)
            + sec('Only the release date earns a spine.', 'The release date is the only thing the team cannot move, so it is the only thing that raises urgency.', spine)
            + sec('Verified means measured. Source means asserted.', 'Only a source value can be wrong, so only a source value can be unlocked.', provs)
            + sec('Permissions change the component, not the page.', '', perms)
            + sec('Every colour stands for one thing.', 'Published has no hue, because most of the library ends up there. Amber and red mean urgency, nothing else.', found)
            + '</div></div></section>')

CSS = '''
.cs-dsec{position:relative;background:#121212;color:#fff;margin-top:var(--sec);padding:clamp(72px,8vw,140px) 0 clamp(96px,10vw,160px);font-family:Manrope,sans-serif}
.ds-in{width:100%;max-width:calc(var(--w) + var(--pad)*2);margin:0 auto;padding:0 var(--pad)}
@media(min-width:1200px){.ds-in{padding-left:max(var(--gut),calc((100% - var(--w)) / 2))}}
.ds-head{margin-bottom:clamp(56px,6vw,96px)}
.ds-head .cs-num{display:none}
.ds-head .cs-title{font-size:clamp(1.75rem,2.4vw,2.75rem);line-height:1.12;letter-spacing:-.022em;font-weight:600;margin:0;color:#fff}
.ds-show{display:flex;flex-direction:column;gap:clamp(72px,8vw,112px);color:#EDEBE8;zoom:var(--dz,1)}
@media(min-width:1680px){.ds-show{--dz:1.0625}}@media(min-width:1920px){.ds-show{--dz:1.125}}@media(min-width:2400px){.ds-show{--dz:1.25}}
.ds-sec{display:flex;flex-direction:column;align-items:center;gap:40px}
.ds-title{margin:0;color:#EDEBE8;text-align:center;letter-spacing:-.01em;font-size:24px;line-height:1.2;font-weight:400}
.ds-lead{margin:-24px 0 0;max-width:640px;color:#B5B3AE;text-align:center;font-size:18px;line-height:28px;text-wrap:balance}
.ds-panel{width:100%;background:#191919;border:1px solid #2A2927;border-radius:12px;padding:40px 48px}
.ds-rl{width:100%;margin:0 0 4px;color:#96938D;text-align:center;letter-spacing:.08em;text-transform:uppercase;font-size:11px;line-height:16px;font-weight:500}
.ds-chips{display:flex;flex-wrap:wrap;justify-content:center;align-items:center;gap:12px}
.ds-chip{display:inline-flex;align-items:center;gap:6px;height:24px;padding:0 10px 0 8px;border:1px solid;border-radius:6px;font-size:12px;line-height:16px;font-weight:500;white-space:nowrap;flex:none}
.ds-chip svg{width:14px;height:14px;flex:none}
.c-todo{color:#B5B3AE;background:#1F1E1D;border-color:#34332E}
.c-prog{color:#A9B6C6;background:#1C2028;border-color:#2C323C}
.c-pend{color:#E8A6C4;background:#2A1B23;border-color:#3D2A34}
.c-rev{color:#8FC2EF;background:#16222E;border-color:#243444}
.c-appr{color:#8FD4A6;background:#16241B;border-color:#24382B}
.c-sched{color:#D4B0E8;background:#241D28;border-color:#382D3E}
.c-pub{color:#C8C7C0;background:#201F1D;border-color:#3A3936}.c-pub svg{color:#A2A197}
.c-rej{color:#F0A19A;background:#2A1817;border-color:#3D2523}
.ds-avail{width:100%;margin-top:-24px;background:#191919;border:1px solid #2A2927;border-radius:12px;padding:32px 48px 36px;display:flex;flex-direction:column;align-items:center}
.ds-avail+.ds-avail{margin-top:-24px}
.ds-avail .ds-rl{margin-bottom:20px}
.ds-g{width:100%;display:grid;grid-template-columns:repeat(3,1fr);gap:24px}
.ds-g>div{display:flex;flex-direction:column;align-items:center;text-align:center}
.ds-g p{margin:12px 0 0;max-width:260px;color:#C8C7C0;font-size:13px;line-height:19px;text-wrap:balance}
.ds-av{display:inline-flex;align-items:center;gap:7px;height:24px;padding:0 10px 0 8px;border:1px solid #3A3934;border-radius:6px;color:#C8C7C0;font-size:12px;line-height:16px;font-weight:500}
.ds-av svg{width:13px;height:13px}.ds-av i{display:block;width:7px;height:7px;border-radius:50%}
.ds-av-on{background:#EDEBE8}.ds-av-end{border:1.5px solid #C8C7C0}.ds-av-x{color:#7D7A74}
.ds-ac{max-width:560px;margin:24px 0 0;text-align:center;color:#96938D;font-size:12px;line-height:18px;text-wrap:balance}
.ds-spine{background:#121212;border:1px solid #2A2927;border-radius:8px;overflow:hidden;margin-bottom:16px}
.ds-sh,.ds-sr{display:grid;grid-template-columns:48px 2fr 1fr 1fr;gap:16px;align-items:center;padding:9px 14px}
.ds-sh{color:#78756F;letter-spacing:.06em;text-transform:uppercase;font-size:10px;border-bottom:1px solid #2A2927}
.ds-sr{color:#D4D2CF;font-size:12px;border-bottom:1px solid #2A2927}.ds-sr:last-child{border-bottom:0}
.sp-amber{box-shadow:inset 2px 0 #D2983F}.sp-red{box-shadow:inset 2px 0 #EC5B57}
.ds-th{height:28px;border-radius:4px;background:#3A3937 50% 25%/cover}
.ds-nm{color:#EDEBE8;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.ds-dt{display:flex;flex-direction:column;gap:2px}.ds-dt small{color:#96938D;font-size:11px}
.ds-note{color:#96938D;font-size:12px;line-height:1.5}
.ds-cell{display:flex;flex-direction:column;gap:12px;min-width:0}
.ds-prov{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:24px}
.ds-tag{display:flex;align-items:center;gap:6px;color:#B5B3AE;font-size:12px;font-weight:500}.ds-tag-ai{color:#D2CEFD}
.ds-ic{width:14px;height:14px;flex:none;display:block}.ds-sm{width:12px;height:12px}.ds-mute{color:#96938D}.ds-ai{color:#D2CEFD}.ds-dim{color:#78756F;width:13px;height:13px}
.ds-fl{display:flex;flex-direction:column;gap:6px}
.ds-k{color:#96938D;font-size:12px}
.ds-f{display:flex;align-items:center;gap:10px;border:1px solid #3A3937;border-radius:8px;padding:9px 11px}
.ds-f-on{background:#191919;border-color:#5C5954}
.ds-f-ai{background:rgba(145,132,217,.12);border-color:#796CBF}
.ds-v{flex:1;min-width:0;color:#B5B3AE;font-size:13px;white-space:nowrap;overflow:hidden;text-overflow:ellipsis}
.ds-strong{color:#EDEBE8}
.ds-perm{display:flex;flex-direction:column}
.ds-ph,.ds-pr{display:grid;grid-template-columns:200px 1fr 1fr;gap:32px}
.ds-ph{padding-bottom:16px;border-bottom:1px solid #3A3937}
.ds-who{display:flex;align-items:center;gap:8px;color:#B5B3AE;font-size:12px;font-weight:500}
.ds-who i{width:24px;height:24px;border-radius:50%;background:#3A3937 50%/cover;flex:none}
.ds-pr{padding:24px 0;border-bottom:1px solid #2A2927;align-items:start}.ds-pr-last{border-bottom:0;padding-bottom:0}
.ds-pl{color:#EDEBE8;font-size:13px;font-weight:500}
.ds-pr .ds-chip{align-self:flex-start}
.ds-ghost{opacity:0;pointer-events:none}
.ds-rr{display:grid;grid-template-columns:110px 1fr auto;gap:14px;align-items:center;background:#1F1E1D;border:1px solid #2A2927;border-radius:8px;padding:10px 15px;font-size:12.5px}
.ds-rr .ds-k{font-size:11.5px}
.ds-rra{display:flex;align-items:center;gap:8px}
.ds-addc{display:inline-flex;align-items:center;gap:4px;color:#96938D;font-size:11px;white-space:nowrap}
.ds-req{display:flex;align-items:center;gap:10px}
.ds-reqn{color:#B5B3AE;font-size:13px;font-weight:500;white-space:nowrap}
.ds-reqb{margin-left:auto;display:inline-flex;align-items:center;justify-content:center;gap:6px;min-width:64px;height:28px;padding:0 10px;border:1px solid #3A3937;border-radius:8px;color:#D4D2CF;font-size:11.5px;font-weight:500;opacity:.45}
.ds-reqs{display:flex;align-items:center;gap:6px;color:#96938D;font-size:11px;white-space:nowrap}
.ds-acts{display:grid;grid-template-columns:96px auto;gap:12px;justify-items:start;align-items:center}
.ds-pair{display:flex;gap:9px}
.ds-btn,.ds-btn2{display:inline-flex;align-items:center;justify-content:center;gap:6px;height:36px;min-width:96px;padding:0 16px;border-radius:8px;font-size:12.5px;font-weight:500;white-space:nowrap}
.ds-btn{background:#9184D9;border:1px solid #9184D9;color:#121212}
.ds-btn-s,.ds-btn2{height:32px;min-width:80px;padding:0 14px;font-size:12px}
.ds-btn2{border:1px solid #3A3937;color:#D4D2CF}
.ds-found{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:16px 32px;align-items:start}
.ds-found>.ds-tag{grid-column:1/-1}
.ds-sws{display:flex;flex-wrap:wrap;gap:8px}
.ds-sw{display:flex;align-items:center;justify-content:center;width:32px;height:24px;border-radius:8px;flex:none}
.ds-sw-ai{background:rgba(145,132,217,.12);border:1px solid #796CBF}
@media(max-width:991px){.ds-panel,.ds-avail{padding:24px 20px}.ds-prov{grid-template-columns:1fr 1fr;row-gap:32px}.ds-found{grid-template-columns:1fr 1fr}.ds-perm{overflow-x:auto}.ds-ph,.ds-pr{min-width:760px}.ds-spine{overflow-x:auto}.ds-sh,.ds-sr{min-width:620px}.ds-title{font-size:22px}}
@media(max-width:767px){.ds-lead{font-size:16px;line-height:24px}.ds-g{grid-template-columns:1fr;gap:20px}}
@media(max-width:479px){.ds-prov,.ds-found{grid-template-columns:1fr}}
'''
