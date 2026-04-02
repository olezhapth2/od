#!/usr/bin/env python3
"""Сборка index.html из данных и сниппетов."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent

from matrix_data import MATRIX_ROWS
from projects_data import PROJECTS

comps_full = (ROOT / "_comp_cards_processed.html").read_text(encoding="utf-8")
exp = (ROOT / "_experience_snippet.html").read_text(encoding="utf-8")
exp = exp.replace("10 years,<br>from print to AI", "9+ years,<br>from print to AI")
exp = exp.replace("10 лет —<br>от типографии до AI", "9+ лет —<br>от типографии до AI")


def first_four_cards(html: str) -> str:
    parts = re.split(r"(?=\n    <div class=\"comp-card comp-card--strip)", html.strip())
    if len(parts) < 4:
        return html.strip()
    block = "\n".join(parts[:4])
    return block.replace("comp-card comp-card--strip", "comp-card comp-card--strip hero-comp-card", 4)

def first_n_cards(html: str, n: int) -> str:
    parts = re.split(r"(?=\n    <div class=\"comp-card comp-card--strip)", html.strip())
    if len(parts) < n:
        return html.strip()
    block = "\n".join(parts[:n])
    # Mark cards as hero cards so we can style them independently.
    return block.replace("comp-card comp-card--strip", "comp-card comp-card--strip hero-comp-card", n)


hero_core_cards = first_n_cards(comps_full, 10)


def esc(s: str) -> str:
    return s.replace("&", "&amp;").replace('"', "&quot;")


def proj_article(i: int, p: dict) -> str:
    pid = str(i)
    img = f"images/project-{i}.webp"
    return f"""    <article class="proj-card proj-card--horiz fade-in" id="project-card-{pid}" data-project-id="{pid}"
      onclick="openPop(this)"
      data-title-en="{esc(p['title_en'])}" data-title-ru="{esc(p['title_ru'])}"
      data-sub-en="{esc(p['sub_en'])}" data-sub-ru="{esc(p['sub_ru'])}"
      data-b1-en="{esc(p['b1_en'])}" data-b1-ru="{esc(p['b1_ru'])}"
      data-b2-en="{esc(p['b2_en'])}" data-b2-ru="{esc(p['b2_ru'])}"
      data-b3-en="{esc(p['b3_en'])}" data-b3-ru="{esc(p['b3_ru'])}">
      <div class="proj-img-wrap"><img src="{img}" alt="" loading="lazy" width="800" height="800"></div>
      <div class="proj-body">
        <div class="proj-body-inner">
          <div class="proj-name" data-en>{p["title_en"]}</div><div class="proj-name" data-ru>{p["title_ru"]}</div>
          <div class="proj-sub" data-en>{p["sub_en"]}</div><div class="proj-sub" data-ru>{p["sub_ru"]}</div>
          <div class="proj-desc" data-en>{esc(p["b1_en"])}</div><div class="proj-desc" data-ru>{esc(p["b1_ru"])}</div>
        </div>
      </div>
    </article>"""


proj_grid = "\n".join(proj_article(i + 1, PROJECTS[i]) for i in range(len(PROJECTS)))

matrix_js = ",\n".join(
    f"  {{ cat: '{cat}', proj: '{proj}', en: {json.dumps(en)}, ru: {json.dumps(ru)} }}"
    for cat, proj, en, ru in MATRIX_ROWS
)

html = f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<script>
(function(){{
  var h = location.hostname;
  if (!h.endsWith('github.io')) return;
  var parts = location.pathname.split('/').filter(Boolean);
  if (parts.length >= 1) {{
    document.write('<base href="' + '/' + parts[0] + '/' + '">');
  }}
}})();
</script>
<title>Oleg Devyatov — Senior Product Designer</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=Outfit:wght@300;400;500;600&family=Space+Grotesk:wght@400;500;600;700&family=DM+Mono:wght@400;500&display=swap" rel="stylesheet">
<link href="https://fonts.googleapis.com/icon?family=Material+Icons+Round" rel="stylesheet">
<link rel="stylesheet" href="styles.css">
</head>
<body class="lang-en">

<div class="blobs"><div class="blob b1"></div><div class="blob b2"></div><div class="blob b3"></div><div class="blob b4"></div></div>

<div class="popup-ov" id="popup" onclick="closePop(event)">
  <div class="popup-box popup-box--wide" onclick="event.stopPropagation()">
    <button type="button" class="popup-close" onclick="closePopDirect()" aria-label="Close"><span class="material-icons-round">close</span></button>
    <img class="popup-cover" id="pop-img" src="" alt="" style="display:none">
    <div class="popup-title" id="pop-title"></div>
    <div class="popup-meta" id="pop-meta"></div>
    <div class="popup-scroll" id="pop-scroll">
      <div class="popup-block" id="pop-b1"></div>
      <div class="popup-block" id="pop-b2"></div>
      <div class="popup-block" id="pop-b3"></div>
    </div>
    <div class="popup-ph-row" aria-hidden="true">
      <div class="popup-ph16"><span data-en>Visual 16:9 · placeholder</span><span data-ru>Визуал 16:9 · заглушка</span></div>
      <div class="popup-ph16"><span data-en>Visual 16:9 · placeholder</span><span data-ru>Визуал 16:9 · заглушка</span></div>
    </div>
    <a class="pill primary popup-cta" id="pop-cta" href="mailto:olegdevyatow@gmail.com"><span class="material-icons-round">mail</span><span data-en>olegdevyatow@gmail.com</span><span data-ru>olegdevyatow@gmail.com</span></a>
  </div>
</div>

<div class="topbar">
  <div class="topbar-loc">
    <span class="material-icons-round">location_on</span>
    <span class="topbar-loc-text" data-en>Bangkok, Thailand · Open to remote</span>
    <span class="topbar-loc-text" data-ru>Бангкок, Таиланд · Удалённая работа</span>
  </div>
  <div class="topbar-right">
    <div class="lang-bar">
      <button type="button" class="lang-btn active" onclick="setLang('en')">EN</button>
      <button type="button" class="lang-btn" onclick="setLang('ru')">RU</button>
    </div>
  </div>
</div>

<section id="hero">
  <div class="container">
    <div class="hero-head-row">
      <h1 class="hero-name">Oleg<br>Devyatov</h1>
      <div class="hero-head-text">
        <div class="hero-title" data-en>Senior Product Designer · UX · UI</div>
        <div class="hero-title" data-ru>Продакт-дизайнер · Senior · UX · UI</div>
        <p class="hero-bio" data-en>9+ years at the intersection of UX strategy, design systems, and AI workflows. Full-cycle products, scaled teams, internal tools that save hundreds of hours.</p>
        <p class="hero-bio" data-ru>9+ лет на пересечении UX-стратегии, дизайн-систем и AI-автоматизации. Продукты полного цикла, масштабирование команд, инструменты, экономящие сотни часов.</p>
      </div>
    </div>
    <div class="hero-scroll-outer">
      <div class="hero-scroll-fade hero-scroll-fade--l" aria-hidden="true"></div>
      <div class="hero-scroll-fade hero-scroll-fade--r" aria-hidden="true"></div>
      <div class="hero-scroll-inner">
{hero_core_cards}
      </div>
    </div>
    <div class="hero-contacts">
      <a class="pill primary" href="mailto:olegdevyatow@gmail.com"><span class="material-icons-round">mail</span><span data-en>olegdevyatow@gmail.com</span><span data-ru>olegdevyatow@gmail.com</span></a>
      <a class="pill" href="https://t.me/olegdevyatow" target="_blank" rel="noopener noreferrer"><span class="material-icons-round">send</span>Telegram</a>
      <a class="pill" href="https://www.linkedin.com/in/oleg-devyatow-653584367/" target="_blank" rel="noopener noreferrer"><span class="material-icons-round">work</span>LinkedIn</a>
      <a class="pill" href="https://www.behance.net/reesoonki" target="_blank" rel="noopener noreferrer"><span class="material-icons-round">palette</span>Behance</a>
    </div>
  </div>
</section>

<section id="projects">
<div class="container">
  <div class="sec-tag" data-en>Projects</div>
  <div class="sec-tag" data-ru>Проекты</div>
  <h2 class="sec-title" data-en>Selected work</h2>
  <h2 class="sec-title" data-ru>Избранные работы</h2>
  <div class="proj-grid proj-grid--6">
{proj_grid}
  </div>
</div>
</section>

<section id="skills-matrix" class="matrix-section">
<div class="container">
  <div class="sec-tag" data-en>Skills matrix</div>
  <div class="sec-tag" data-ru>Матрица навыков</div>
  <h2 class="sec-title" data-en>Research · Visual · Leadership · Art</h2>
  <h2 class="sec-title" data-ru>Исследования · Визуал · Лидерство · Художка</h2>
  <p class="matrix-lead" data-en>Hover a category to highlight. Click a skill to open the linked case study.</p>
  <p class="matrix-lead" data-ru>Наведите категорию — подсветка. Клик по навыку — кейс в попапе.</p>
  <div class="matrix-wrap" id="matrixWrap">
    <div class="matrix-cats">
      <button type="button" class="matrix-cat c1" data-cat="1"><span data-en>Research &amp; analytics</span><span data-ru>Исследования и аналитика</span></button>
      <button type="button" class="matrix-cat c2" data-cat="2"><span data-en>Visualization &amp; UI</span><span data-ru>Визуал и UI</span></button>
      <button type="button" class="matrix-cat c3" data-cat="3"><span data-en>Project leadership</span><span data-ru>Проекты и лидерство</span></button>
      <button type="button" class="matrix-cat c4" data-cat="4"><span data-en>Fine art foundation</span><span data-ru>Художественная база</span></button>
    </div>
    <div class="matrix-viewport-outer">
      <div class="matrix-viewport">
        <div class="matrix-grid" id="matrixGrid"></div>
      </div>
    </div>
  </div>

</div>
</section>

{exp}

<footer id="contact" class="site-footer">
  <div class="container footer-split">
    <div class="footer-left">
      <div class="footer-block-title" data-en>Education</div>
      <div class="footer-block-title" data-ru>Образование</div>
      <ul class="footer-edu-list">
        <li><span class="edu-years">2012–2016</span><span class="edu-line" data-en>Zinger Art School — Graphics &amp; Painting</span><span class="edu-line" data-ru>Худ. школа Зингера — графика и живопись</span></li>
        <li><span class="edu-years">2016–2019</span><span class="edu-line" data-en>International Market Institute — Management &amp; Marketing</span><span class="edu-line" data-ru>Международный институт рынка — менеджмент и маркетинг</span></li>
        <li><span class="edu-years">2020–2023</span><span class="edu-line" data-en>CONTENTED — Graphic &amp; UX/UI Design</span><span class="edu-line" data-ru>CONTENTED — графический и UX/UI-дизайн</span></li>
      </ul>
      <div class="footer-portfolio-btns">
        <a class="pill" href="https://olegdvtv.notion.site/CONTENTED-b8d2cdd858b24781bdc6bdd7b988fd26" target="_blank" rel="noopener noreferrer">Notion · CONTENTED</a>
        <a class="pill" href="https://olegdevyatow.tilda.ws" target="_blank" rel="noopener noreferrer">Tilda archive</a>
      </div>
      <div class="footer-socials">
        <a class="pill" href="mailto:olegdevyatow@gmail.com"><span class="material-icons-round">mail</span>olegdevyatow@gmail.com</a>
        <a class="pill" href="https://t.me/olegdevyatow" target="_blank" rel="noopener noreferrer"><span class="material-icons-round">send</span>Telegram</a>
        <a class="pill" href="https://www.linkedin.com/in/oleg-devyatow-653584367/" target="_blank" rel="noopener noreferrer"><span class="material-icons-round">work</span>LinkedIn</a>
        <a class="pill" href="https://www.behance.net/reesoonki" target="_blank" rel="noopener noreferrer"><span class="material-icons-round">palette</span>Behance</a>
      </div>
    </div>
    <div class="footer-right">
      <div class="footer-cta-animated">
        <div class="cta-glow"></div>
        <h3 data-en>Design that ships — tied to your metric</h3>
        <h3 data-ru>Дизайн в прод — под вашу метрику</h3>
        <p data-en>9+ years in fintech, SaaS, AI products. Brief me — I reply with a clear next step.</p>
        <p data-ru>9+ лет в fintech, SaaS и AI. Кратко опишите задачу — отвечу со следующим шагом.</p>
        <a class="pill primary" href="mailto:olegdevyatow@gmail.com"><span class="material-icons-round">mail</span><span data-en>olegdevyatow@gmail.com</span><span data-ru>olegdevyatow@gmail.com</span></a>
      </div>
    </div>
  </div>
  <div class="footer-copy-row">
    <span class="footer-copy" data-en>© Oleg Devyatov · Bangkok · Remote</span>
    <span class="footer-copy" data-ru>© Олег Девятов · Бангкок · Удалённо</span>
  </div>
</footer>

<script>
function setLang(l){{
  document.body.className = 'lang-' + l;
  document.querySelectorAll('.lang-btn').forEach(b => b.classList.toggle('active', b.textContent === l.toUpperCase()));
  document.documentElement.lang = l;
}}

function fillPopupFromEl(el) {{
  const isRu = document.body.classList.contains('lang-ru');
  document.getElementById('pop-title').textContent = isRu ? el.dataset.titleRu : el.dataset.titleEn;
  document.getElementById('pop-meta').textContent = isRu ? el.dataset.subRu : el.dataset.subEn;
  const img = document.getElementById('pop-img');
  const cardImg = el.querySelector('img');
  if (cardImg && cardImg.src) {{ img.src = cardImg.src; img.style.display = 'block'; }}
  else {{ img.style.display = 'none'; }}
  const b1 = document.getElementById('pop-b1');
  const b2 = document.getElementById('pop-b2');
  const b3 = document.getElementById('pop-b3');
  if (el.hasAttribute('data-b1-en') || el.hasAttribute('data-b1-ru')) {{
    b1.textContent = isRu ? (el.dataset.b1Ru || '') : (el.dataset.b1En || '');
    b2.textContent = isRu ? (el.dataset.b2Ru || '') : (el.dataset.b2En || '');
    b3.textContent = isRu ? (el.dataset.b3Ru || '') : (el.dataset.b3En || '');
  }} else {{
    const body = isRu ? el.dataset.bodyRu : el.dataset.bodyEn;
    b1.innerHTML = '<p>' + (body || '').replace(/\\n/g, '</p><p>') + '</p>';
    b2.textContent = '';
    b3.textContent = '';
  }}
}}

function openPop(el) {{
  fillPopupFromEl(el);
  document.getElementById('popup').classList.add('open');
  document.body.style.overflow = 'hidden';
}}

function openProjectById(pid) {{
  const el = document.getElementById('project-card-' + pid);
  if (el) openPop(el);
}}

function closePop(e) {{ if (e.target === document.getElementById('popup')) closePopDirect(); }}
function closePopDirect() {{
  document.getElementById('popup').classList.remove('open');
  document.body.style.overflow = '';
}}
document.addEventListener('keydown', e => {{ if (e.key === 'Escape') closePopDirect(); }});

function toggleExp(btn) {{
  const items = btn.nextElementSibling;
  const open = btn.classList.contains('open');
  document.querySelectorAll('.exp-year-btn.open').forEach(b => {{
    b.classList.remove('open');
    b.nextElementSibling.classList.remove('open');
  }});
  if (!open) {{ btn.classList.add('open'); items.classList.add('open'); }}
}}

const obs = new IntersectionObserver((entries) => {{
  entries.forEach((e, i) => {{
    if (e.isIntersecting) {{
      setTimeout(() => e.target.classList.add('vis'), i * 40);
      obs.unobserve(e.target);
    }}
  }});
}}, {{ threshold: 0.05, rootMargin: '0px 0px -28px 0px' }});
document.querySelectorAll('.fade-in').forEach(el => obs.observe(el));

const MATRIX_CHIPS = [
{matrix_js}
];

(function buildMatrix(){{
  const grid = document.getElementById('matrixGrid');
  if (!grid) return;
  MATRIX_CHIPS.forEach((row) => {{
    const el = document.createElement('button');
    el.type = 'button';
    el.className = 'mc';
    el.dataset.cat = row.cat;
    el.dataset.project = row.proj;
    el.innerHTML = '<span data-en>' + row.en + '</span><span data-ru>' + row.ru + '</span>';
    el.addEventListener('click', () => openProjectById(row.proj));
    grid.appendChild(el);
  }});
}})();

(function matrixHover(){{
  const wrap = document.getElementById('matrixWrap');
  if (!wrap) return;
  const cats = wrap.querySelectorAll('.matrix-cat');
  const chips = () => wrap.querySelectorAll('.mc');
  cats.forEach(btn => {{
    const enter = () => {{
      const c = btn.dataset.cat;
      wrap.classList.add('is-active', 'cat-' + c);
      chips().forEach(ch => {{
        const on = ch.dataset.cat === c;
        ch.classList.toggle('mc-lit', on);
        ch.classList.toggle('mc-dim', !on);
      }});
    }};
    const leave = () => {{
      wrap.classList.remove('is-active', 'cat-1', 'cat-2', 'cat-3', 'cat-4');
      chips().forEach(ch => ch.classList.remove('mc-lit', 'mc-dim'));
    }};
    btn.addEventListener('mouseenter', enter);
    btn.addEventListener('mouseleave', leave);
    btn.addEventListener('focus', enter);
    btn.addEventListener('blur', leave);
  }});
}})();

(function footerParallax3D(){{
  const el = document.querySelector('.footer-cta-animated');
  if (!el) return;
  el.style.setProperty('--px', '0px');
  el.style.setProperty('--py', '0px');
  el.style.setProperty('--rx', '0deg');
  el.style.setProperty('--ry', '0deg');

  let raf = null;
  let tx = 0;
  let ty = 0;
  let rx = 0;
  let ry = 0;

  function commit(){{
    el.style.setProperty('--px', tx.toFixed(2) + 'px');
    el.style.setProperty('--py', ty.toFixed(2) + 'px');
    el.style.setProperty('--rx', rx.toFixed(2) + 'deg');
    el.style.setProperty('--ry', ry.toFixed(2) + 'deg');
    raf = null;
  }}

  function onMove(e){{
    const r = el.getBoundingClientRect();
    const x = (e.clientX - r.left) / r.width - 0.5;
    const y = (e.clientY - r.top) / r.height - 0.5;
    tx = x * 26;
    ty = y * 20;
    rx = (-y) * 7;
    ry = (x) * 10;
    if (!raf) raf = requestAnimationFrame(commit);
  }}

  function reset(){{
    tx = 0;
    ty = 0;
    rx = 0;
    ry = 0;
    if (!raf) raf = requestAnimationFrame(commit);
  }}

  el.addEventListener('pointermove', onMove);
  el.addEventListener('pointerleave', reset);
}})();
</script>
</body>
</html>
"""

(ROOT / "index.html").write_text(html, encoding="utf-8")
print("Wrote index.html", len(html))
