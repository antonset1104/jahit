"""Build the independent bilingual Jahit Terukur site into dist/."""
from __future__ import annotations

import html
import json
import shutil
from pathlib import Path
from xml.etree.ElementTree import Element, ElementTree, SubElement

from content import GUIDES, SOURCES

ROOT = Path(__file__).resolve().parent
OUT = ROOT / "dist"
SITE = "https://jahit.vijeron.com"
UPDATED = "2026-10-09"
URLS: list[str] = []

T = {
    "id": {
        "name": "Jahit Terukur", "home": "Beranda", "guides": "Panduan", "tools": "Alat", "method": "Metode & sumber", "about": "Tentang", "privacy": "Privasi", "contact": "Kontak", "skip": "Lewati ke isi", "read": "Baca panduan", "use": "Gunakan alat", "refs": "Rujukan", "next": "Baca berikutnya", "updated": "Diperbarui 9 Oktober 2026", "eyebrow": "VIJERON / RUANG POTONG", "hero": "Dari ukuran ke potongan, tanpa menebak.", "hero_desc": "Panduan menjahit dan alat perencanaan kain yang memperlihatkan rumus, asumsi, serta batas hasil. Cocok untuk panel persegi panjang dan kebutuhan pita tepi sederhana.",
        "hero_cta": "Mulai dari ukuran jadi", "tools_cta": "Coba alat", "art_alt": "Sketsa panel kain dengan garis potong, garis jahit, dan ukuran 42 kali 52 sentimeter", "art_cut": "GARIS POTONG", "art_seam": "GARIS JAHIT", "art_note": "40 × 50 cm ukuran jadi · kampuh 1 cm", "note_label": "Prinsip kerja", "note_title": "Ukuran jadi tidak sama dengan ukuran potong", "note_body": "Sebelum menghitung panjang kain, tentukan tepi yang dijahit, lebar kain yang dapat dipakai, serta arah serat dan motif. Alat akan menunjukkan aritmetika; sketsa Anda menentukan apakah susunannya masuk akal.",
        "steps_title": "Tiga catatan sebelum memotong", "step1": "Ukur benda jadi dan tandai perlakuan setiap tepi.", "step2": "Tentukan ukuran potong serta arah serat atau motif.", "step3": "Susun potongan pada lebar kain efektif; simpan alasan tambahan panjang.", "tool_title": "Dua alat untuk rencana sederhana", "tool_intro": "Angka masukan dan hasil dihitung di peramban Anda. Tidak ada ukuran proyek yang dikirim ke server Vijeron.", "panel": "Perencana panel kain", "panel_desc": "Hitung panel per baris, jumlah baris, dan panjang kain untuk satu ukuran potongan persegi panjang.", "edge": "Pita tepi persegi panjang", "edge_desc": "Hitung keliling, panjang tambahan sambungan, dan gulung pita dari ukuran yang Anda masukkan.", "guide_title": "Delapan panduan dari sketsa ke daftar belanja", "guide_intro": "Pelajari ukuran jadi, kampuh, lebar kain, arah serat, susunan panel, motif, penyusutan, dan lembar rencana. Contoh adalah aritmetika yang dapat Anda ulang.", "editorial": "Catatan editorial", "editorial_body": "Ditulis khusus untuk Vijeron. Sumber memeriksa konsep; tidak ada pola, gambar, proyek, atau hasil uji pihak lain yang diterbitkan ulang.", "worked": "Contoh yang dapat dihitung ulang", "pitfall": "Hal yang perlu dihindari", "footer": "Panduan perencanaan potong, bukan pola pakaian siap pakai, jasa jahit, atau jaminan kebutuhan bahan.",
        "panel_title": "Hitung panjang kain untuk panel berulang", "panel_intro": "Masukkan ukuran potong satu panel, jumlah panel, lebar kain efektif, dan tambahan panjang yang Anda pilih. Alat tidak memutar potongan atau mencocokkan motif.", "edge_title": "Hitung pita tepi untuk panel persegi panjang", "edge_intro": "Masukkan ukuran pada garis pemasangan pita, tambahan untuk sambungan, serta panjang tiap gulung. Keempat tepi dianggap akan dilapisi.", "cut_width": "Lebar potong panel (cm)", "cut_length": "Panjang potong panel (cm)", "count": "Jumlah panel", "usable_width": "Lebar kain efektif (cm)", "extra": "Tambahan panjang (cm)", "panel_width": "Lebar panel pada garis pita (cm)", "panel_length": "Panjang panel pada garis pita (cm)", "join_extra": "Tambahan sambungan (cm)", "roll_length": "Panjang pita per gulung (cm)", "calculate": "Hitung rencana", "result": "Hasil rencana", "empty": "Masukkan angka lalu hitung. Angka tetap di peramban.", "formula": "Rumus dan batas", "panel_formula": "Panel/baris = bulat ke bawah (lebar efektif ÷ lebar potong). Baris = bulat ke atas (jumlah panel ÷ panel/baris). Panjang rencana = baris × panjang potong + tambahan panjang.", "edge_formula": "Keliling = 2 × (lebar + panjang). Pita rencana = keliling + tambahan sambungan. Gulung = bulat ke atas (pita rencana ÷ panjang tiap gulung).", "panel_limit": "Hanya satu ukuran persegi panjang, satu orientasi, dan baris seragam. Tidak mensimulasikan motif, arah serat, cacat, susut, atau ukuran jual toko.", "edge_limit": "Hanya keempat sisi persegi panjang. Tidak menghitung lebar pita, ketebalan kain, teknik sudut, atau sambungan tambahan yang belum Anda masukkan.",
        "method_title": "Metode, rumus, dan rujukan", "method_desc": "Asumsi perhitungan, asal contoh, dan batas penggunaan situs.", "about_title": "Tentang Jahit Terukur", "about_desc": "Sumber belajar Vijeron untuk merencanakan potongan sederhana dengan angka yang terlihat.", "privacy_title": "Kebijakan privasi", "privacy_desc": "Penjelasan data alat, analitik, iklan, dan pilihan persetujuan.",
    },
    "en": {
        "name": "Measured Sewing", "home": "Home", "guides": "Guides", "tools": "Tools", "method": "Method & sources", "about": "About", "privacy": "Privacy", "contact": "Contact", "skip": "Skip to content", "read": "Read guide", "use": "Use tool", "refs": "References", "next": "Read next", "updated": "Updated 9 October 2026", "eyebrow": "VIJERON / CUTTING ROOM", "hero": "From measurements to cuts, without guesswork.", "hero_desc": "Sewing guides and fabric planning tools with visible formulas, assumptions and limitations. Designed for rectangular panels and simple edging tape estimates.",
        "hero_cta": "Start with finished size", "tools_cta": "Try the tools", "art_alt": "Fabric panel diagram showing a cut line, stitch line and 42 by 52 centimetre dimensions", "art_cut": "CUT LINE", "art_seam": "STITCH LINE", "art_note": "40 × 50 cm finished · 1 cm seam", "note_label": "Working principle", "note_title": "Finished size differs from cut size", "note_body": "Before calculating fabric length, decide which edges will be sewn, how much width is usable and which way the grain and print run. The tools show arithmetic; your sketch decides whether the layout is practical.",
        "steps_title": "Three notes before cutting", "step1": "Measure the finished object and mark each edge treatment.", "step2": "Decide cut dimensions and grain or print direction.", "step3": "Arrange pieces across usable fabric width; explain any extra length.", "tool_title": "Two tools for simple plans", "tool_intro": "Inputs and results are calculated in your browser. Project measurements are not sent to a Vijeron server.", "panel": "Fabric panel planner", "panel_desc": "Find pieces per row, row count and fabric length for one repeated rectangular cut size.", "edge": "Rectangular edging tape", "edge_desc": "Find perimeter, joining allowance and tape rolls from the dimensions you enter.", "guide_title": "Eight guides from sketch to buying note", "guide_intro": "Learn finished size, seam allowance, fabric width, grain, panel layout, prints, shrinkage and planning notes. The examples are reproducible arithmetic.", "editorial": "Editorial note", "editorial_body": "Written for Vijeron. Sources check concepts; no other party's pattern, image, project or test result is republished.", "worked": "Worked example", "pitfall": "Pitfall to avoid", "footer": "A cutting-plan guide, not a ready-made clothing pattern, sewing service or fabric-quantity guarantee.",
        "panel_title": "Plan fabric length for repeated panels", "panel_intro": "Enter one panel's cut dimensions, count, usable fabric width and extra length you choose. The tool does not rotate pieces or match prints.", "edge_title": "Plan edging tape for a rectangle", "edge_intro": "Enter dimensions at the tape installation line, extra joining length and length per roll. All four sides are assumed bound.", "cut_width": "Panel cut width (cm)", "cut_length": "Panel cut length (cm)", "count": "Number of panels", "usable_width": "Usable fabric width (cm)", "extra": "Extra length (cm)", "panel_width": "Width at tape line (cm)", "panel_length": "Length at tape line (cm)", "join_extra": "Extra joining length (cm)", "roll_length": "Tape length per roll (cm)", "calculate": "Calculate plan", "result": "Planning result", "empty": "Enter numbers and calculate. Values stay in your browser.", "formula": "Formula and limits", "panel_formula": "Pieces/row = floor(usable width ÷ cut width). Rows = ceil(piece count ÷ pieces/row). Planned length = rows × cut length + extra length.", "edge_formula": "Perimeter = 2 × (width + length). Planned tape = perimeter + joining allowance. Rolls = ceil(planned tape ÷ length per roll).", "panel_limit": "One rectangular cut size, one orientation and uniform rows only. Does not simulate print matching, grain, defects, shrinkage or shop cut sizes.", "edge_limit": "All four sides of one rectangle only. Does not calculate tape width, fabric bulk, corner technique or joins you did not enter.",
        "method_title": "Method, formulas and references", "method_desc": "Calculation assumptions, examples and usage limits.", "about_title": "About Measured Sewing", "about_desc": "A Vijeron learning resource for planning simple cuts with visible numbers.", "privacy_title": "Privacy policy", "privacy_desc": "How tools, analytics, ads and consent choices work.",
    },
}


def e(value: object) -> str:
    return html.escape(str(value), quote=True)


def route(lang: str, suffix: str = "") -> str:
    return ("/en/" if lang == "en" else "/") + suffix


def write(path: str, body: str) -> None:
    target = OUT / path.lstrip("/")
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(body, encoding="utf-8")


def add_url(lang: str, suffix: str = "") -> None:
    URLS.append(SITE + route(lang, suffix))


def head(lang: str, suffix: str, title: str, desc: str, kind: str = "WebPage", ads: bool = True) -> str:
    url = SITE + route(lang, suffix)
    schema = {"@context": "https://schema.org", "@type": kind, "name": title, "description": desc, "url": url, "inLanguage": lang,
              "datePublished": UPDATED, "dateModified": UPDATED, "author": {"@type": "Organization", "name": "Vijeron", "url": "https://vijeron.com/"},
              "publisher": {"@type": "Organization", "name": "Vijeron", "url": "https://vijeron.com/"},
              "isPartOf": {"@type": "WebSite", "name": "Jahit Terukur | Vijeron", "url": SITE + "/"}}
    alternates = "".join(f"<link rel='alternate' hreflang='{code}' href='{e(SITE + route(code, suffix))}'>" for code in ("id", "en"))
    alternates += f"<link rel='alternate' hreflang='x-default' href='{e(SITE + route('id', suffix))}'>"
    consent = ("<script>window.dataLayer=window.dataLayer||[];function gtag(){dataLayer.push(arguments)}"
               "gtag('consent','default',{ad_storage:'denied',analytics_storage:'denied',ad_user_data:'denied',ad_personalization:'denied',wait_for_update:500});</script>"
               "<script async src='https://fundingchoicesmessages.google.com/i/pub-6180580801533680?ers=1'></script>"
               "<script async src='https://www.googletagmanager.com/gtag/js?id=G-79X7K7H4MJ'></script>"
               "<script>gtag('js',new Date());gtag('config','G-79X7K7H4MJ');</script>"
               "<script async crossorigin='anonymous' src='https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6180580801533680'></script>") if ads else ""
    return (f"<!doctype html><html lang='{lang}'><head><meta charset='utf-8'><meta name='viewport' content='width=device-width,initial-scale=1'>"
            f"<title>{e(title)} | Vijeron</title><meta name='description' content='{e(desc)}'><meta name='theme-color' content='#40252f'>"
            f"<link rel='canonical' href='{e(url)}'>{alternates}<link rel='icon' type='image/svg+xml' href='/assets/icon.svg'>"
            f"<link rel='stylesheet' href='/assets/site.css'><meta property='og:type' content='{'article' if kind == 'Article' else 'website'}'>"
            f"<meta property='og:title' content='{e(title)}'><meta property='og:description' content='{e(desc)}'><meta property='og:url' content='{e(url)}'>"
            f"<script type='application/ld+json'>{json.dumps(schema, ensure_ascii=False).replace('<', '\\u003c')}</script>{consent}</head><body>")


def chrome(lang: str, suffix: str) -> str:
    t = T[lang]
    other = "en" if lang == "id" else "id"
    return (f"<a class='skip' href='#main'>{e(t['skip'])}</a><header class='site-header'><div class='wrap header-inner'>"
            f"<a class='brand' href='{route(lang)}' aria-label='{e(t['name'])}'><span class='brand-icon' aria-hidden='true'>✂</span>"
            "<span class='brand-name'>JAHIT <b>TERUKUR</b><small>BY VIJERON</small></span></a>"
            f"<nav aria-label='{e(t['guides'])}'><a href='{route(lang)}#panduan'>{e(t['guides'])}</a>"
            f"<a href='{route(lang)}#alat'>{e(t['tools'])}</a><a href='{route(lang, 'metode/')}'>{e(t['method'])}</a></nav>"
            f"<div class='lang' aria-label='Language / Bahasa'><a href='{route(lang, suffix)}' aria-current='page'>{lang.upper()}</a>"
            f"<span>·</span><a href='{route(other, suffix)}'>{other.upper()}</a></div></div></header>")


def finish(lang: str, script: bool = False) -> str:
    t = T[lang]
    js = "<script defer src='/assets/calculator.js'></script>" if script else ""
    return (f"<footer class='site-footer'><div class='wrap footer-inner'><div><strong>{e(t['name'])}</strong><p>{e(t['footer'])}</p></div>"
            f"<nav><a href='{route(lang, 'metode/')}'>{e(t['method'])}</a><a href='{route(lang, 'tentang/')}'>{e(t['about'])}</a>"
            f"<a href='{route(lang, 'privasi/')}'>{e(t['privacy'])}</a><a href='https://vijeron.com/kontak.html'>{e(t['contact'])}</a>"
            "<a href='https://vijeron.com/'>Vijeron.com</a></nav></div><div class='wrap footer-bottom'>© Vijeron · "
            f"{e(t['updated'])}</div></footer>{js}</body></html>")


def sources(keys: list[str]) -> str:
    return "<ul class='source-list'>" + "".join(f"<li><a href='{e(SOURCES[k][1])}' rel='noopener noreferrer'>{e(SOURCES[k][0])} ↗</a></li>" for k in keys) + "</ul>"


def home(lang: str) -> None:
    t = T[lang]
    cards = "".join(f"<article class='guide-card'><span class='serial'>{i+1:02d} / 08</span>"
                    f"<h3><a href='{route(lang, 'panduan/' + g['slug'] + '/')}'>{e(g[lang]['title'])}</a></h3>"
                    f"<p>{e(g[lang]['summary'])}</p><a class='text-link' href='{route(lang, 'panduan/' + g['slug'] + '/')}'>{e(t['read'])} ↗</a></article>"
                    for i, g in enumerate(GUIDES))
    steps = "".join(f"<li><span>0{i}</span><p>{e(t['step'+str(i)])}</p></li>" for i in (1, 2, 3))
    body = (f"<main id='main'><section class='hero'><div class='wrap hero-grid'><div class='hero-copy'><p class='eyebrow'>{e(t['eyebrow'])}</p>"
            f"<h1>{e(t['hero'])}</h1><p class='lead'>{e(t['hero_desc'])}</p><div class='actions'><a class='button' href='{route(lang, 'panduan/ukuran-jadi-dan-ukuran-potong/')}'>{e(t['hero_cta'])} ↗</a>"
            f"<a class='button button-outline' href='#alat'>{e(t['tools_cta'])}</a></div></div>"
            f"<div class='fabric-art' role='img' aria-label='{e(t['art_alt'])}'><div class='ruler ruler-top'>0 <span>10</span> <span>20</span> <span>30</span> <span>40</span></div>"
            f"<div class='fabric-cut'><span class='cut-label'>{e(t['art_cut'])}</span><div class='fabric-stitch'><span>{e(t['art_seam'])}</span><strong>42 × 52 <small>cm</small></strong></div></div>"
            f"<p>{e(t['art_note'])}</p></div></div></section>"
            f"<section class='wrap note-band'><span class='eyebrow'>{e(t['note_label'])}</span><h2>{e(t['note_title'])}</h2><p>{e(t['note_body'])}</p></section>"
            f"<section class='wrap section steps'><div class='section-head'><span class='eyebrow'>01 / {e(t['method'])}</span><h2>{e(t['steps_title'])}</h2></div><ol>{steps}</ol></section>"
            f"<section class='tools-section' id='alat'><div class='wrap section'><div class='section-head'><span class='eyebrow'>02 / {e(t['tools'])}</span><h2>{e(t['tool_title'])}</h2><p>{e(t['tool_intro'])}</p></div>"
            f"<div class='tool-cards'><article><span class='serial'>01 / cm</span><h3>{e(t['panel'])}</h3><p>{e(t['panel_desc'])}</p><a href='{route(lang, 'alat/panel-kain/')}'>{e(t['use'])} ↗</a></article>"
            f"<article><span class='serial'>02 / cm</span><h3>{e(t['edge'])}</h3><p>{e(t['edge_desc'])}</p><a href='{route(lang, 'alat/pita-tepi/')}'>{e(t['use'])} ↗</a></article></div></div></section>"
            f"<section class='wrap section' id='panduan'><div class='section-head'><span class='eyebrow'>03 / {e(t['guides'])}</span><h2>{e(t['guide_title'])}</h2><p>{e(t['guide_intro'])}</p></div><div class='guide-grid'>{cards}</div></section>"
            f"<section class='wrap source-note'><span class='eyebrow'>{e(t['editorial'])}</span><p>{e(t['editorial_body'])}</p><a href='{route(lang, 'metode/')}'>{e(t['method'])} ↗</a></section></main>")
    write(route(lang) + "index.html", head(lang, "", t["name"], t["hero_desc"]) + chrome(lang, "") + body + finish(lang))
    add_url(lang)


def guide_page(lang: str, guide: dict, index: int) -> None:
    t, item = T[lang], guide[lang]
    suffix = "panduan/" + guide["slug"] + "/"
    following = GUIDES[(index + 1) % len(GUIDES)]
    sections = "".join(f"<section class='prose-section'><h2>{e(h)}</h2><p>{e(p)}</p></section>" for h, p in item["sections"])
    body = (f"<main id='main' class='wrap article-layout'><article><nav class='crumb'><a href='{route(lang)}'>{e(t['home'])}</a> / {e(t['guides'])} {index+1:02d}</nav>"
            f"<header class='article-head'><p class='eyebrow'>{e(t['guides'])} / {index+1:02d}—08</p><h1>{e(item['title'])}</h1><p class='lead'>{e(item['summary'])}</p><p class='byline'>Vijeron · {e(t['updated'])}</p></header>"
            f"<div class='prose'>{sections}<aside class='example'><span class='eyebrow'>{e(t['worked'])}</span><p>{e(item['example'])}</p></aside>"
            f"<aside class='pitfall'><strong>{e(t['pitfall'])}</strong><p>{e(item['pitfall'])}</p></aside><section class='references'><h2>{e(t['refs'])}</h2>{sources(guide['sources'])}</section></div>"
            f"<p class='next-guide'><span>{e(t['next'])}</span><a href='{route(lang, 'panduan/' + following['slug'] + '/')}'>{e(following[lang]['title'])} ↗</a></p></article>"
            f"<aside class='article-aside'><div class='aside-panel'><span class='eyebrow'>{e(t['tools'])} / 01—02</span><h2>{e(t['tool_title'])}</h2><p>{e(t['tool_intro'])}</p>"
            f"<a href='{route(lang, 'alat/panel-kain/')}'>{e(t['panel'])} ↗</a><a href='{route(lang, 'alat/pita-tepi/')}'>{e(t['edge'])} ↗</a></div>"
            f"<div class='aside-panel'><h2>{e(t['method'])}</h2><p>{e(t['editorial_body'])}</p><a href='{route(lang, 'metode/')}'>{e(t['read'])} ↗</a></div></aside></main>")
    write(route(lang, suffix) + "index.html", head(lang, suffix, item["title"], item["summary"], "Article") + chrome(lang, suffix) + body + finish(lang))
    add_url(lang, suffix)


def field(name: str, label: str, value: str, maximum: str, minimum: str = "0", step: str = "any") -> str:
    return (f"<label class='field' for='{name}'><span>{e(label)}</span><input id='{name}' name='{name}' type='number' required inputmode='decimal'"
            f" min='{minimum}' max='{maximum}' step='{step}' value='{value}'></label>")


def tool_page(lang: str, kind: str) -> None:
    t = T[lang]
    panel = kind == "panel-kain"
    suffix = "alat/" + kind + "/"
    title = t["panel_title"] if panel else t["edge_title"]
    intro = t["panel_intro"] if panel else t["edge_intro"]
    fields = (field("cut-width", t["cut_width"], "42", "1000", "0.1") + field("cut-length", t["cut_length"], "52", "10000", "0.1") +
              field("count", t["count"], "6", "10000", "1", "1") + field("usable-width", t["usable_width"], "144", "1000", "0.1") +
              field("extra", t["extra"], "10", "100000")) if panel else (
              field("panel-width", t["panel_width"], "40", "100000", "0.1") + field("panel-length", t["panel_length"], "50", "100000", "0.1") +
              field("join-extra", t["join_extra"], "20", "100000") + field("roll-length", t["roll_length"], "150", "100000", "0.1"))
    formula = t["panel_formula"] if panel else t["edge_formula"]
    limit = t["panel_limit"] if panel else t["edge_limit"]
    related = GUIDES[3 if panel else 4]
    body = (f"<main id='main' class='wrap tool-page'><nav class='crumb'><a href='{route(lang)}'>{e(t['home'])}</a> / {e(t['tools'])}</nav>"
            f"<header class='tool-head'><p class='eyebrow'>{e(t['tools'])} / {'01' if panel else '02'}</p><h1>{e(title)}</h1><p class='lead'>{e(intro)}</p></header>"
            f"<div class='calculator-grid'><form id='calculator' data-kind='{kind}' data-lang='{lang}'><div class='fields'>{fields}</div>"
            f"<button class='button' type='submit'>{e(t['calculate'])} ↗</button></form><div class='result-panel' id='result' role='status' aria-live='polite'>"
            f"<span class='eyebrow'>{e(t['result'])}</span><strong>—</strong><p>{e(t['empty'])}</p></div></div>"
            f"<div class='tool-explain'><section><h2>{e(t['formula'])}</h2><p>{e(formula)}</p><p>{e(limit)}</p><a href='{route(lang, 'metode/')}'>{e(t['method'])} ↗</a></section>"
            f"<section><h2>{e(t['next'])}</h2><p>{e(related[lang]['summary'])}</p><a href='{route(lang, 'panduan/' + related['slug'] + '/')}'>{e(related[lang]['title'])} ↗</a></section></div></main>")
    write(route(lang, suffix) + "index.html", head(lang, suffix, title, intro) + chrome(lang, suffix) + body + finish(lang, True))
    add_url(lang, suffix)


def info_page(lang: str, kind: str) -> None:
    t = T[lang]
    info = {
        "metode": (t["method_title"], t["method_desc"], [
            (("Perhitungan panel" if lang == "id" else "Panel arithmetic"), ("Lebar potong panel dibagi ke lebar kain efektif tanpa rotasi. Jumlah panel per baris dibulatkan ke bawah, jumlah baris ke atas, lalu dikalikan panjang potong. Tambahan panjang bersifat opsional dan dipilih pengguna. Alat menolak panel yang lebih lebar dari kain efektif." if lang == "id" else "The cut width fits across usable fabric width without rotation. Pieces per row are rounded down, rows rounded up, then multiplied by cut length. Extra length is optional and user-selected. The tool rejects a panel wider than usable fabric.")),
            (("Perhitungan pita tepi" if lang == "id" else "Edging arithmetic"), ("Empat sisi persegi panjang dijumlahkan sebagai 2 × (lebar + panjang). Tambahan sambungan dari pengguna ditambahkan, kemudian kebutuhan gulung dibulatkan ke atas. Hasil ini tidak menghitung teknik sudut atau lebar pita." if lang == "id" else "All four sides of a rectangle total 2 × (width + length). A user-supplied joining allowance is added, then required rolls are rounded up. This does not calculate corner technique or tape width.")),
            (("Proses editorial" if lang == "id" else "Editorial process"), ("Teks, contoh angka, dan sketsa dibuat untuk Vijeron pada 9 Oktober 2026. Tautan rujukan memeriksa konsep kampuh, pengukuran, arah kain, dan penyusutan. Kami tidak mengklaim pernah menguji kain, menerbitkan pola pakaian, atau memiliki sertifikasi menjahit. Perubahan penting tercatat di Git." if lang == "id" else "Text, numerical examples and diagrams were made for Vijeron on 9 October 2026. References check seam, measurement, grain and shrinkage concepts. We claim no fabric tests, garment patterns or sewing certification. Material changes are recorded in Git.")),
        ]),
        "tentang": (t["about_title"], t["about_desc"], [
            (("Tujuan" if lang == "id" else "Purpose"), ("Jahit Terukur membantu pembaca merencanakan panel kain dan pita tepi sederhana dari angka yang dapat diperiksa. Proyek ini bukan toko kain, jasa potong, kursus bersertifikat, atau pola pakaian siap pakai. Kesesuaian bahan serta hasil jahit bergantung pada proyek Anda." if lang == "id" else "Measured Sewing helps readers plan simple fabric panels and edging tape from checkable numbers. It is not a fabric shop, cutting service, certified course or ready-made clothing pattern. Fabric suitability and sewing results depend on your project.")),
            (("Penerbit dan koreksi" if lang == "id" else "Publisher and corrections"), ("Vijeron menerbitkan situs ini sebagai bagian dari katalog di vijeron.com. Organisasi yang ditautkan sebagai rujukan tidak berafiliasi dengan kami. Kirim koreksi melalui halaman kontak portal dengan URL dan bagian yang perlu diperiksa." if lang == "id" else "Vijeron publishes this site within its catalog at vijeron.com. Referenced organizations are not affiliated with us. Send corrections through the portal contact page with a URL and the passage to review.")),
            (("Iklan" if lang == "id" else "Advertising"), ("Kode Google AdSense ada pada halaman konten. Penayangan bergantung pada status akun dan pilihan privasi yang berlaku. Iklan tidak menentukan rumus dan tidak ada tautan afiliasi produk pada peluncuran ini." if lang == "id" else "Google AdSense code is present on content pages. Serving depends on account status and applicable privacy choices. Ads do not determine the formulas, and this launch has no product affiliate links.")),
        ]),
        "privasi": (t["privacy_title"], t["privacy_desc"], [
            (("Data alat" if lang == "id" else "Tool data"), ("Ukuran potong, jumlah panel, lebar kain, panjang tambahan, dan ukuran pita diproses di peramban. Situs ini tidak mengirim atau menyimpan angka tersebut pada server Vijeron." if lang == "id" else "Cut dimensions, panel count, fabric width, extra length and tape dimensions are processed in your browser. This site does not transmit or store those numbers on a Vijeron server.")),
            (("Analitik" if lang == "id" else "Analytics"), ("Google Analytics 4 mengukur kunjungan dan peristiwa penggunaan alat. Peristiwa hanya berisi nama alat dan bahasa halaman, tanpa angka masukan atau hasil. Pengukuran bergantung pada pilihan persetujuan yang berlaku." if lang == "id" else "Google Analytics 4 measures visits and tool-use events. Events include the tool name and page language only, without input or result numbers. Measurement depends on applicable consent choices.")),
            (("Iklan dan persetujuan" if lang == "id" else "Ads and consent"), ("Kode AdSense dan Google Funding Choices dapat dimuat pada halaman konten. Penyimpanan iklan, personalisasi, dan analitik dimulai dalam keadaan ditolak sampai pilihan persetujuan yang berlaku diperoleh. Google dapat memproses data menurut kebijakan layanannya." if lang == "id" else "AdSense and Google Funding Choices code may load on content pages. Ad storage, personalization and analytics storage start denied until applicable consent is obtained. Google may process data under its service policies.")),
            (("Kontak" if lang == "id" else "Contact"), ("Gunakan halaman kontak Vijeron untuk pertanyaan privasi atau koreksi. Jangan mengirim ukuran badan atau informasi pribadi yang tidak diperlukan." if lang == "id" else "Use the Vijeron contact page for privacy questions or corrections. Do not send unnecessary body measurements or personal information.")),
        ]),
    }
    title, desc, sections = info[kind]
    suffix = kind + "/"
    paragraphs = "".join(f"<section class='prose-section'><h2>{e(h)}</h2><p>{e(p)}</p></section>" for h, p in sections)
    refs = f"<section class='references'><h2>{e(t['refs'])}</h2>{sources(list(SOURCES))}</section>" if kind == "metode" else ""
    body = (f"<main id='main' class='wrap info-page'><nav class='crumb'><a href='{route(lang)}'>{e(t['home'])}</a> / {e(title)}</nav>"
            f"<p class='eyebrow'>{e(t['eyebrow'])}</p><h1>{e(title)}</h1><p class='lead'>{e(desc)}</p><div class='prose'>{paragraphs}{refs}</div></main>")
    write(route(lang, suffix) + "index.html", head(lang, suffix, title, desc, ads=kind != "privasi") + chrome(lang, suffix) + body + finish(lang))
    add_url(lang, suffix)


def main() -> None:
    if OUT.exists():
        shutil.rmtree(OUT)
    (OUT / "assets").mkdir(parents=True)
    for asset in ("site.css", "calculator.js", "icon.svg"):
        shutil.copy2(ROOT / "assets" / asset, OUT / "assets" / asset)
    for lang in ("id", "en"):
        home(lang)
        for index, guide in enumerate(GUIDES):
            guide_page(lang, guide, index)
        for kind in ("panel-kain", "pita-tepi"):
            tool_page(lang, kind)
        for kind in ("metode", "tentang", "privasi"):
            info_page(lang, kind)
    write("404.html", "<!doctype html><html lang='id'><meta charset='utf-8'><title>Halaman tidak ditemukan | Vijeron</title><link rel='stylesheet' href='/assets/site.css'><main class='wrap info-page'><h1>Halaman tidak ditemukan</h1><p>Kembali ke <a href='/'>Jahit Terukur</a>.</p></main></html>")
    write("robots.txt", "User-agent: *\nAllow: /\nSitemap: https://jahit.vijeron.com/sitemap.xml\n")
    write("ads.txt", "google.com, pub-6180580801533680, DIRECT, f08c47fec0942fa0\n")
    write("_headers", "/*\n  X-Content-Type-Options: nosniff\n  Referrer-Policy: strict-origin-when-cross-origin\n  X-Frame-Options: SAMEORIGIN\n  Permissions-Policy: camera=(), microphone=(), geolocation=()\n  Cache-Control: public, max-age=0, must-revalidate\n\n/assets/*\n  Cache-Control: public, max-age=3600, must-revalidate\n\n/sitemap.xml\n  Content-Type: application/xml; charset=utf-8\n\n/ads.txt\n  Content-Type: text/plain; charset=utf-8\n")
    xml = Element("urlset", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")
    for url in URLS:
        node = SubElement(xml, "url")
        SubElement(node, "loc").text = url
        SubElement(node, "lastmod").text = UPDATED
    ElementTree(xml).write(OUT / "sitemap.xml", encoding="utf-8", xml_declaration=True)
    print(f"Built {len(URLS)} public pages in {OUT}")


if __name__ == "__main__":
    main()
