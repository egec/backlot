// Shared table fitting + thin scrollbars. Loaded by backlot -Dark.dc.html and every animation page.
// Tables: the Status column always fits its widest chip; when a row would overflow its container,
// columns hide in priority order (Updated → Languages → Publishers), then the title truncates.
// Bars (animations only, window.BACKLOT_FIT_BARS): the backlot Dark table scrollbar — thin thumb 8px from the
// container's right edge, starting below a sticky header, on areas that scroll inside a card (never the page, never paginated lists).
(function () {
  if (window.BacklotFit) return;
  const HSEL = '[style*="grid-template-columns"][style*="uppercase"]';
  const HIDE = [/^updated/, /^languages?/, /^publishers?/];
  const gs = (e) => getComputedStyle(e);
  const split = (s) => { const out = []; let d = 0, cur = ''; for (const ch of s) { if (ch === '(') d++; if (ch === ')') d--; if (ch === ' ' && !d) { if (cur) out.push(cur); cur = ''; } else cur += ch; } if (cur) out.push(cur); return out; };
  const maxPart = (t) => { const m = /^minmax\(([^,]+),\s*(.+)\)$/.exec(t); return m ? m[2].trim() : (/fr$/.test(t) ? t : null); };
  const cellsOf = (r) => [...r.children].filter((c) => !c.hasAttribute('data-pl-thumb') && gs(c).position !== 'absolute');
  const label = (c) => (c.textContent || '').trim().toLowerCase();
  const tables = new Map();
  const ro = new ResizeObserver((es) => { es.forEach((e) => { tables.forEach((tb, h) => { if (tb.box === e.target) tb.dirty = true; }); }); schedule(); });
  const rowsOf = (h) => { const tpl = h.__gt0; return [h, ...[...h.parentElement.querySelectorAll('[style*="grid-template-columns"]')].filter((r) => r !== h && (r.__gt0 || r.style.gridTemplateColumns) === tpl)]; };
  const fitOne = (h) => {
    if (!h.isConnected || !h.offsetWidth) return;
    const rows = rowsOf(h); const n = cellsOf(h).length; if (n < 4) return;
    rows.forEach((r) => { if (r.__gt0 == null || (r.__gtW != null && r.style.gridTemplateColumns !== r.__gtW)) r.__gt0 = r.style.gridTemplateColumns; });
    const t0 = split(h.__gt0); if (t0.length !== n) return;
    const good = rows.filter((r) => cellsOf(r).length === n);
    const labels = cellsOf(h).map(label);
    const apply = (tr, hid) => {
      const tpl = tr.filter((_, i) => !hid.has(i)).join(' ');
      good.forEach((r) => { r.style.gridTemplateColumns = tpl; r.__gtW = r.style.gridTemplateColumns; cellsOf(r).forEach((c, i) => { if (c.__fd == null) c.__fd = c.style.display; c.style.display = hid.has(i) ? 'none' : c.__fd; }); });
    };
    const fits = () => good.every((r) => r.scrollWidth <= r.clientWidth + 1);
    const tr = t0.slice(), hid = new Set();
    const si = labels.findIndex((l) => l === 'status');
    if (si >= 0) {
      const tmp = tr.slice(); tmp[si] = 'max-content'; apply(tmp, hid);
      const w = Math.ceil(Math.max(...good.map((r) => cellsOf(r)[si].offsetWidth)));
      const am = (/^minmax\(([\d.]+)px/.exec(t0[si]) || [])[1];
      tr[si] = 'minmax(' + Math.max(w, am ? +am : 0) + 'px, ' + (maxPart(t0[si]) || '1fr') + ')';
    }
    apply(tr, hid);
    for (const re of HIDE) { if (fits()) break; const i = labels.findIndex((l) => re.test(l)); if (i < 0) continue; hid.add(i); apply(tr, hid); }
    if (!fits()) { const ti = labels.findIndex((l) => /^(title|content|file|name)$/.test(l)); if (ti >= 0) { tr[ti] = 'minmax(0, ' + (maxPart(t0[ti]) || '1fr') + ')'; apply(tr, hid); } }
  };
  const discover = () => {
    document.querySelectorAll(HSEL).forEach((h) => {
      if (tables.has(h)) return;
      if (/grid/.test(gs(h).display) === false) return;
      if (h.__gt0 == null) h.__gt0 = h.style.gridTemplateColumns;
      const box = h.parentElement; tables.set(h, { box, dirty: true }); ro.observe(box);
    });
    tables.forEach((tb, h) => { if (!h.isConnected) { tables.delete(h); } });
  };
  // Bars (animations)
  const PAGE = 'rgb(18, 18, 18)';
  const paged = (el) => [el, el.parentElement].some((a) => a && a.parentElement && [...a.parentElement.children].some((s) => s !== a && /\d+[–-]\d+ of [\d,]+/.test(s.textContent || '')));
  const hostOf = (el) => { for (let a = el; a && a !== document.body; a = a.parentElement) { const b = gs(a).backgroundColor; if (b !== 'rgba(0, 0, 0, 0)' && b !== PAGE && b !== 'transparent') return a; } return null; };
  const bars = () => {
    if (!window.BACKLOT_FIT_BARS) return;
    document.querySelectorAll('[style*="overflow"],[style*="height"]').forEach((el) => {
      if (el.__tb) { el.__tbUp && el.__tbUp(); return; }
      const s = gs(el); if (!/(auto|scroll|hidden)/.test(s.overflowY)) return;
      if (el.scrollHeight <= el.clientHeight + 1 || el.clientHeight < 60) return;
      const f = el.firstElementChild, sticky = f && gs(f).position === 'sticky';
      if (s.overflowY === 'hidden' && !sticky) return;
      const host = hostOf(el); if (!host || paged(el)) return;
      el.__tb = 1;
      if (gs(host).position === 'static') host.style.position = 'relative';
      const th = document.createElement('div'); th.setAttribute('aria-hidden', 'true'); th.setAttribute('data-pl-thumb', '');
      th.style.cssText = 'position:absolute;top:0;left:0;width:5px;border-radius:999px;background:rgba(255,255,255,.22);pointer-events:none;z-index:40;display:none';
      host.appendChild(th);
      const up = () => {
        if (th.parentNode !== host) host.appendChild(th);
        const ch = el.clientHeight, sh = el.scrollHeight; if (sh <= ch + 1 || !el.offsetWidth) { th.style.display = 'none'; return; }
        const ff = el.firstElementChild, hh = ff && ff !== th && gs(ff).position === 'sticky' ? ff.offsetHeight : 0;
        const inset = 3, track = ch - hh - inset * 2, h = Math.max(24, track * (ch - hh) / (sh - hh));
        let y0 = el.scrollTop;
        if (host !== el) { const hr = host.getBoundingClientRect(), er = el.getBoundingClientRect(), k = hr.width / host.offsetWidth || 1; y0 = (er.top - hr.top) / k - host.clientTop + el.clientTop; }
        const top = y0 + hh + inset + (track - h) * (el.scrollTop / Math.max(1, sh - ch));
        th.style.display = 'block'; th.style.height = h + 'px'; th.style.transform = 'translate(' + (host.clientWidth - 8) + 'px,' + top + 'px)';
      };
      el.__tbUp = up; el.addEventListener('scroll', up, { passive: true }); new ResizeObserver(up).observe(el); up();
    });
  };
  let q = false, all = false;
  const run = () => { q = false; discover(); tables.forEach((tb, h) => { if (all || tb.dirty) { tb.dirty = false; fitOne(h); } }); all = false; bars(); };
  const schedule = (full) => { if (full) all = true; if (q) return; q = true; queueMicrotask(run); };
  const mo = new MutationObserver((recs) => {
    let any = false;
    for (const r of recs) {
      if (r.type === 'attributes' && (r.target.__gtW == null || r.target.style.gridTemplateColumns === r.target.__gtW)) continue;
      const t = r.target.nodeType === 1 ? r.target : r.target.parentElement; if (!t) continue;
      if (r.type === 'childList' && [...r.addedNodes].every((n) => n.nodeType === 1 && n.hasAttribute && n.hasAttribute('data-pl-thumb'))) continue;
      any = true; tables.forEach((tb, h) => { if (!tb.dirty && (tb.box.contains(t) || t.contains(h))) tb.dirty = true; });
    }
    if (any) schedule();
  });
  const start = () => { mo.observe(document.body, { childList: true, subtree: true, characterData: true, attributes: true, attributeFilter: ['style'] }); all = true; run(); setTimeout(() => schedule(true), 0); setTimeout(() => schedule(true), 600); };
  if (document.body) start(); else document.addEventListener('DOMContentLoaded', start);
  if (document.fonts && document.fonts.ready) document.fonts.ready.then(() => schedule(true));
  addEventListener('load', () => schedule(true));
  window.BacklotFit = { refit: () => schedule(true), fitOne };
})();
