(() => {
  'use strict';
  const form = document.getElementById('calculator');
  const result = document.getElementById('result');
  if (!form || !result) return;

  const lang = form.dataset.lang === 'en' ? 'en' : 'id';
  const kind = form.dataset.kind;
  const fmt = (number, digits = 0) => new Intl.NumberFormat(lang === 'id' ? 'id-ID' : 'en-US', {
    maximumFractionDigits: digits, minimumFractionDigits: digits,
  }).format(number);
  const value = (name) => Number(form.elements.namedItem(name).value);
  const labels = lang === 'id' ? {
    fit: 'Panel per baris', rows: 'Jumlah baris', base: 'Panjang dasar', total: 'Panjang rencana',
    perimeter: 'Keliling', tape: 'Pita rencana', rolls: 'Gulung utuh',
    invalid: 'Periksa masukan: ukuran, jumlah, dan panjang gulung harus lebih dari nol; tambahan tidak boleh negatif.',
    tooWide: 'Lebar potong panel melebihi lebar kain efektif. Ubah orientasi hanya jika pola mengizinkan, atau pilih kain lain.',
    panelNote: 'Periksa arah serat, motif, susut, cacat, dan aturan potong toko sebelum membeli.',
    edgeNote: 'Periksa teknik sudut dan sambungan; jumlah gulung dibulatkan ke atas.',
  } : {
    fit: 'Panels per row', rows: 'Number of rows', base: 'Base length', total: 'Planned length',
    perimeter: 'Perimeter', tape: 'Planned tape', rolls: 'Whole rolls',
    invalid: 'Check inputs: dimensions, count and roll length must be above zero; extra length cannot be negative.',
    tooWide: 'The cut panel is wider than usable fabric. Rotate it only if the pattern allows, or choose different fabric.',
    panelNote: 'Check grain, print, shrinkage, defects and the shop cutting rules before buying.',
    edgeNote: 'Check corners and joins; whole rolls are rounded up.',
  };
  const row = (label, number, unit, digits = 0) => {
    const item = document.createElement('div'); item.className = 'result-row';
    const name = document.createElement('span'); name.textContent = label;
    const amount = document.createElement('b'); amount.textContent = `${fmt(number, digits)} ${unit}`;
    item.append(name, amount); return item;
  };
  const render = (headline, rows, note) => {
    result.replaceChildren();
    const eyebrow = document.createElement('span'); eyebrow.className = 'eyebrow';
    eyebrow.textContent = lang === 'id' ? 'HASIL RENCANA' : 'PLANNING RESULT';
    const title = document.createElement('strong'); title.textContent = headline;
    const list = document.createElement('div'); list.className = 'result-rows';
    rows.forEach((item) => list.append(item));
    const detail = document.createElement('p'); detail.textContent = note;
    result.append(eyebrow, title, list, detail);
  };
  const fail = (message) => render('—', [], message);

  form.addEventListener('submit', (event) => {
    event.preventDefault();
    if (!form.reportValidity()) return;
    if (kind === 'panel-kain') {
      const width = value('cut-width'), length = value('cut-length');
      const count = value('count'), usable = value('usable-width'), extra = value('extra');
      if (![width, length, count, usable, extra].every(Number.isFinite) ||
          Math.min(width, length, count, usable) <= 0 || !Number.isInteger(count) || extra < 0) {
        fail(labels.invalid); return;
      }
      const fit = Math.floor(usable / width);
      if (fit < 1) { fail(labels.tooWide); return; }
      const rows = Math.ceil(count / fit);
      const base = rows * length;
      const total = base + extra;
      render(`${fmt(total, 1)} cm`, [
        row(labels.fit, fit, lang === 'id' ? 'panel' : 'panels'),
        row(labels.rows, rows, lang === 'id' ? 'baris' : 'rows'),
        row(labels.base, base, 'cm', 1), row(labels.total, total, 'cm', 1),
      ], labels.panelNote);
    } else if (kind === 'pita-tepi') {
      const width = value('panel-width'), length = value('panel-length');
      const extra = value('join-extra'), roll = value('roll-length');
      if (![width, length, extra, roll].every(Number.isFinite) ||
          Math.min(width, length, roll) <= 0 || extra < 0) { fail(labels.invalid); return; }
      const perimeter = 2 * (width + length);
      const tape = perimeter + extra;
      const rolls = Math.ceil(tape / roll);
      render(`${fmt(rolls)} ${lang === 'id' ? 'gulung' : 'rolls'}`, [
        row(labels.perimeter, perimeter, 'cm', 1), row(labels.tape, tape, 'cm', 1),
        row(labels.rolls, rolls, lang === 'id' ? 'gulung' : 'rolls'),
      ], labels.edgeNote);
    }
    if (typeof window.gtag === 'function') {
      window.gtag('event', 'use_sewing_calculator', {tool_name: kind, page_language: lang});
    }
  });
})();
