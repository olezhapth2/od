#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parent

comps = (ROOT / "_comp_cards_processed.html").read_text(encoding="utf-8")
exp = (ROOT / "_experience_snippet.html").read_text(encoding="utf-8")
exp = exp.replace("10 years,<br>from print to AI", "9+ years,<br>from print to AI")
exp = exp.replace("10 лет —<br>от типографии до AI", "9+ лет —<br>от типографии до AI")

# 8 projects — paths webp
projects_meta = [
    ("Game UI · In-game Shop", "Game UI · Внутриигровой магазин", "Game Interface Design · Post-apocalyptic shooter · 2023–2024", "Игровой интерфейс · Постапокалиптический шутер · 2023–2024",
     "Full game UI system for a post-apocalyptic shooter — HUD, in-game shop, inventory, queue system, and trade screens. Built around extreme information density and fast-paced decision-making under pressure.",
     "Полная система игрового UI для постапокалиптического шутера — HUD, магазин, инвентарь, очередь, торговые экраны. Плотность информации и быстрые решения под давлением."),
    ("Gate19", "Gate19", "Affiliate platform · 20+ products · MiraiTech · 2022–2025", "Аффилиат-платформа · 20+ продуктов · MiraiTech · 2022–2025",
     "Full-cycle design for an affiliate tools ecosystem — brand to dashboards. Unified library for 20+ products: −60% handoff, launch under 1 week, White Label in 5 min. Foundation for AI landing pipeline. Live: pnb.agency",
     "Полный цикл для аффилиат-экосистемы — от бренда до дашбордов. Единая библиотека для 20+ продуктов: −60% хэндофф, запуск за неделю, White Label за 5 мин. Основа AI-лендингов. Live: pnb.agency"),
    ("White Label System", "White Label система", "Landing template engine · MiraiTech · 2022–2025", "Движок лендинг-шаблонов · MiraiTech · 2022–2025",
     "White-label templates: branded site launch from days to 5 minutes, zero dev. Built on Gate19 DS. Powered AI landing generator with 100+ niche variants.",
     "White-label: запуск бренд-сайта с дней до 5 минут без разработчика. На базе Gate19. Стала основой AI-генератора с 100+ вариантами."),
    ("JAVHD", "JAVHD", "SaaS Video Platform · Monetization · MiraiTech · 2022–2025", "SaaS-видео · Монетизация · MiraiTech · 2022–2025",
     "100+ landings, 50 monetization screens. AI promo pipeline ~−70% production time. Full funnel: entry → streaming → retention → win-back.",
     "100+ лендингов, 50 экранов монетизации. AI-промо ~−70% времени производства. Воронка: вход → стриминг → retention."),
    ("Corgday HR CRM", "Corgday HR CRM", "Internal HR tooling · MiraiTech · 2022–2025", "Внутренний HR · MiraiTech · 2022–2025",
     "Complex tables & forms for HR. IA around real workflows. Slack alerts −40% manual follow-ups.",
     "Сложные таблицы и формы. ИА вокруг процессов. Slack-алерты −40% ручных follow-up."),
    ("ShugarAi", "ShugarAi", "AI characters · Generative UX · MiraiTech · 2023–2025", "AI-персонажи · Генеративный UX · MiraiTech · 2023–2025",
     "Photo/video/audio generation & live chats with AI characters. Generation flows, gallery, chat, onboarding — engagement depth.",
     "Генерация фото/видео/аудио и чаты с персонажами. Флоу генерации, галерея, чат, онбординг."),
    ("Adbot", "Adbot", "Telegram ad placement · 2021", "Реклама в Telegram · 2021",
     "End-to-end UX/UI: logo, flows, proto, web + mobile. Flow: register → post → venues → pay → analytics.",
     "Полный UX/UI: логотип, флоу, прототипы, веб и мобайл. Регистрация → пост → площадки → оплата → аналитика."),
    ("PNB Agency · Web", "PNB Agency · Сайт", "MiraiTech ecosystem · Agency · 2024–2025", "Экосистема MiraiTech · Агентство · 2024–2025",
     "Agency-facing presence for the MiraiTech / PNB ecosystem — positioning and paths into live Gate19, White Label, and AI pipelines.",
     "Сайт экосистемы MiraiTech / PNB — позиционирование и связка с Gate19, White Label и AI-пайплайнами."),
]

def esc(s):
    return (s.replace("&", "&amp;").replace('"', "&quot;"))

def proj_block(i, p):
    te, tr, se, sr, be, br = p
    img = f"images/project-{i}.webp"
    return f"""    <div class="proj-card fade-in" onclick="openPop(this)"
      data-title-en="{esc(te)}" data-title-ru="{esc(tr)}"
      data-sub-en="{esc(se)}" data-sub-ru="{esc(sr)}"
      data-body-en="{esc(be)}" data-body-ru="{esc(br)}">
      <div class="proj-img-wrap"><img src="{img}" alt="" loading="lazy" width="800" height="800"></div>
      <div class="proj-body">
        <div>
          <div class="proj-name" data-en>{te}</div><div class="proj-name" data-ru>{tr}</div>
          <div class="proj-sub" data-en>{se}</div><div class="proj-sub" data-ru>{sr}</div>
          <div class="proj-tags"><span class="ptag" data-en>Case study</span><span class="ptag" data-ru>Кейс</span></div>
        </div>
      </div>
    </div>"""

proj_html = "\n".join(proj_block(i + 1, projects_meta[i]) for i in range(8))
proj_grids = f"""<div class="proj-blocks">
  <div class="proj-grid">
{chr(10).join(proj_block(i + 1, projects_meta[i]) for i in range(4))}
  </div>
  <div class="proj-grid">
{chr(10).join(proj_block(i + 1, projects_meta[i]) for i in range(4, 8))}
  </div>
</div>"""

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
  <div class="popup-box" onclick="event.stopPropagation()">
    <button type="button" class="popup-close" onclick="closePopDirect()" aria-label="Close"><span class="material-icons-round">close</span></button>
    <img class="popup-img" id="pop-img" src="" alt="" style="display:none">
    <div class="popup-title" id="pop-title"></div>
    <div class="popup-meta" id="pop-meta"></div>
    <div class="popup-body" id="pop-body"></div>
  </div>
</div>

<div class="lang-bar">
  <button type="button" class="lang-btn active" onclick="setLang('en')">EN</button>
  <button type="button" class="lang-btn" onclick="setLang('ru')">RU</button>
</div>

<nav>
  <a class="nav-logo" href="#hero">OD</a>
  <ul class="nav-links">
    <li><a href="#projects" data-en>Projects</a><a href="#projects" data-ru>Проекты</a></li>
    <li><a href="#experience" data-en>Experience</a><a href="#experience" data-ru>Опыт</a></li>
    <li><a href="#skills-matrix" data-en>Skills matrix</a><a href="#skills-matrix" data-ru>Матрица навыков</a></li>
    <li><a href="#contact" data-en>Contact</a><a href="#contact" data-ru>Контакты</a></li>
  </ul>
</nav>

<section id="hero">
  <div class="container">
    <div class="hero-layout">
      <div class="hero-col-left">
        <div class="hero-intro">
          <div class="hero-label"><span class="material-icons-round">location_on</span><span data-en>Bangkok, Thailand · Open to remote</span><span data-ru>Бангкок, Таиланд · Удалённая работа</span></div>
          <h1 class="hero-name">Oleg<br>Devyatov</h1>
          <div class="hero-title" data-en>Senior Product Designer · UX · UI</div>
          <div class="hero-title" data-ru>Продакт-дизайнер · Senior · UX · UI</div>
          <p class="hero-bio" data-en>9+ years at the intersection of UX strategy, design systems, and AI workflows. Full-cycle products, scaled teams, internal tools that save hundreds of hours.</p>
          <p class="hero-bio" data-ru>9+ лет на пересечении UX-стратегии, дизайн-систем и AI-автоматизации. Продукты полного цикла, масштабирование команд, инструменты, экономящие сотни часов.</p>
        </div>
        <div class="hero-contacts">
          <a class="pill primary" href="mailto:olegdevyatow@gmail.com"><span class="material-icons-round">mail</span><span data-en>olegdevyatow@gmail.com</span><span data-ru>olegdevyatow@gmail.com</span></a>
          <a class="pill" href="https://t.me/olegdevyatow" target="_blank" rel="noopener noreferrer"><span class="material-icons-round">send</span>Telegram</a>
          <a class="pill" href="https://www.linkedin.com/in/olegdevyatow" target="_blank" rel="noopener noreferrer"><span class="material-icons-round">work</span>LinkedIn</a>
          <a class="pill" href="https://www.behance.net/reesoonki" target="_blank" rel="noopener noreferrer"><span class="material-icons-round">palette</span>Behance</a>
        </div>
      </div>
      <div class="hero-col-right">
        <div class="hero-scroll-hint"><span data-en>Core competencies · scroll</span><span data-ru>Ключевые компетенции · скролл</span></div>
        <div class="hero-scroll-outer">
          <div class="hero-scroll-fade hero-scroll-fade--l" aria-hidden="true"></div>
          <div class="hero-scroll-fade hero-scroll-fade--r" aria-hidden="true"></div>
          <div class="hero-scroll-inner">
{comps}
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<section id="projects">
<div class="container">
  <div class="sec-tag" data-en>Projects</div>
  <div class="sec-tag" data-ru>Проекты</div>
  <h2 class="sec-title" data-en>Work that shipped<br>&amp; worked</h2>
  <h2 class="sec-title" data-ru>Работа в проде<br>и с метриками</h2>
{proj_grids}
  <div class="archives-row">
    <p data-en><strong>Earlier portfolios</strong> — context on how the craft evolved (kept compact).</p>
    <p data-ru><strong>Прошлые портфолио</strong> — контекст, как копился опыт (компактно).</p>
    <div class="archives-links">
      <a class="arch-link" href="https://olegdvtv.notion.site/CONTENTED-b8d2cdd858b24781bdc6bdd7b988fd26" target="_blank" rel="noopener noreferrer">Notion · CONTENTED</a>
      <a class="arch-link" href="https://olegdevyatow.tilda.ws" target="_blank" rel="noopener noreferrer">Tilda archive</a>
    </div>
  </div>
</div>
</section>

{exp}

<section id="skills-matrix" class="matrix-section">
<div class="container">
  <div class="sec-tag" data-en>Capability matrix · 16:9</div>
  <div class="sec-tag" data-ru>Матрица компетенций · 16:9</div>
  <h2 class="sec-title" data-en>Research · Visual · Delivery · Art</h2>
  <h2 class="sec-title" data-ru>Исследования · Визуал · Доставка · Художка</h2>
  <div class="matrix-wrap" id="matrixWrap">
    <div class="matrix-cats">
      <button type="button" class="matrix-cat c1" data-cat="1"><span data-en>Research &amp; analytics</span><span data-ru>Исследования и аналитика</span></button>
      <button type="button" class="matrix-cat c2" data-cat="2"><span data-en>Visualization &amp; UI</span><span data-ru>Визуал и UI</span></button>
      <button type="button" class="matrix-cat c3" data-cat="3"><span data-en>Project leadership</span><span data-ru>Проекты и лидерство</span></button>
      <button type="button" class="matrix-cat c4" data-cat="4"><span data-en>Fine art foundation</span><span data-ru>Художественная база</span></button>
    </div>
    <div class="matrix-viewport">
      <div class="matrix-grid" id="matrixGrid"></div>
    </div>
  </div>
  <div class="core-skills">
    <div class="core-skills-head" data-en>Core skills · what clients hire for</div>
    <div class="core-skills-head" data-ru>Ключевые навыки · за что нанимают</div>
    <div class="core-skills-grid">
      <span class="core-pill"><span data-en>Design systems at scale</span><span data-ru>Дизайн-системы в масштабе</span></span>
      <span class="core-pill"><span data-en>AI-augmented delivery</span><span data-ru>AI в продакшене</span></span>
      <span class="core-pill"><span data-en>Metric-led UX research</span><span data-ru>UX-исследования под метрику</span></span>
      <span class="core-pill"><span data-en>Cross-functional leadership</span><span data-ru>Кросс-функциональное лидерство</span></span>
      <span class="core-pill"><span data-en>Figma · prototyping · handoff</span><span data-ru>Figma · прототипы · хэндофф</span></span>
    </div>
  </div>
</div>
</section>

<footer id="contact" class="site-footer">
  <div class="container">
    <div class="footer-cta">
      <h2 data-en>Need design tied to your metric — not a pretty deck?</h2>
      <h2 data-ru>Нужен дизайн под вашу метрику — а не «красивую презентацию»?</h2>
      <p data-en>9+ years shipping fintech, SaaS, and AI products. Tell me the job-to-be-done — I’ll reply with a concrete next step.</p>
      <p data-ru>9+ лет в fintech, SaaS и AI-продуктах. Опишите задачу — отвечу с понятным следующим шагом.</p>
      <a class="pill primary" href="mailto:olegdevyatow@gmail.com"><span class="material-icons-round">mail</span><span data-en>Write to olegdevyatow@gmail.com</span><span data-ru>Написать на olegdevyatow@gmail.com</span></a>
    </div>
    <div class="sec-tag" data-en>Education</div>
    <div class="sec-tag" data-ru>Образование</div>
    <h2 class="sec-title" data-en>Art + Marketing + Design</h2>
    <h2 class="sec-title" data-ru>Искусство + маркетинг + дизайн</h2>
    <div class="edu-grid">
      <div class="edu-card fade-in"><div class="edu-yr">2012–2016</div><div class="edu-ico"><span class="material-icons-round">brush</span></div><div class="edu-school" data-en>Zinger Art School</div><div class="edu-school" data-ru>Художественная школа им. Г.Е. Зингера</div><div class="edu-deg" data-en>Graphics &amp; Painting</div><div class="edu-deg" data-ru>Графика и живопись</div></div>
      <div class="edu-card fade-in"><div class="edu-yr">2016–2019</div><div class="edu-ico"><span class="material-icons-round">trending_up</span></div><div class="edu-school" data-en>International Market Institute</div><div class="edu-school" data-ru>Международный институт рынка</div><div class="edu-deg" data-en>Management &amp; Marketing</div><div class="edu-deg" data-ru>Менеджмент и маркетинг</div></div>
      <div class="edu-card fade-in"><div class="edu-yr">2020–2023</div><div class="edu-ico"><span class="material-icons-round">devices</span></div><div class="edu-school">CONTENTED</div><div class="edu-deg" data-en>Graphic &amp; UX/UI Design</div><div class="edu-deg" data-ru>Графический и UX/UI-дизайн</div></div>
    </div>
    <div class="footer-about">
      <p data-en>Senior product designer with a marketing degree and a strong art-school foundation — I connect narrative, systems, and measurable outcomes. Based in Bangkok, open to remote partnerships worldwide.</p>
      <p data-ru>Senior product designer с маркетинговым образованием и сильной художественной базой — связываю нарратив, системы и измеримый результат. Бангкок, открыт к удалённым партнёрствам.</p>
    </div>
    <div class="footer-name">Oleg Devyatov</div>
    <div class="footer-links">
      <a href="mailto:olegdevyatow@gmail.com"><span class="material-icons-round">mail</span><span data-en>Email</span><span data-ru>Почта</span></a>
      <a href="https://t.me/olegdevyatow" target="_blank" rel="noopener noreferrer"><span class="material-icons-round">send</span>Telegram</a>
      <a href="https://www.linkedin.com/in/olegdevyatow" target="_blank" rel="noopener noreferrer"><span class="material-icons-round">work</span>LinkedIn</a>
      <a href="https://www.behance.net/reesoonki" target="_blank" rel="noopener noreferrer"><span class="material-icons-round">palette</span>Behance</a>
      <a href="https://miraitech.co" target="_blank" rel="noopener noreferrer"><span class="material-icons-round">open_in_new</span><span data-en>MiraiTech</span><span data-ru>MiraiTech</span></a>
    </div>
    <div class="footer-copy" data-en>© Oleg Devyatov · Product design · Bangkok · Remote</div>
    <div class="footer-copy" data-ru>© Олег Девятов · Продуктовый дизайн · Бангкок · Удалённо</div>
  </div>
</footer>

<script>
function setLang(l){{
  document.body.className = 'lang-' + l;
  document.querySelectorAll('.lang-btn').forEach(b => b.classList.toggle('active', b.textContent === l.toUpperCase()));
  document.documentElement.lang = l;
}}

function openPop(el){{
  const isRu = document.body.classList.contains('lang-ru');
  const title = isRu ? el.dataset.titleRu : el.dataset.titleEn;
  const sub = isRu ? el.dataset.subRu : el.dataset.subEn;
  const body = isRu ? el.dataset.bodyRu : el.dataset.bodyEn;
  document.getElementById('pop-title').textContent = title || '';
  document.getElementById('pop-meta').textContent = sub || '';
  const img = document.getElementById('pop-img');
  const cardImg = el.querySelector('img');
  if (cardImg && cardImg.src) {{ img.src = cardImg.src; img.style.display = 'block'; }}
  else {{ img.style.display = 'none'; }}
  document.getElementById('pop-body').innerHTML = '<p>' + (body || '').replace(/\\n/g, '</p><p>') + '</p>';
  document.getElementById('popup').classList.add('open');
  document.body.style.overflow = 'hidden';
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
      setTimeout(() => e.target.classList.add('vis'), i * 50);
      obs.unobserve(e.target);
    }}
  }});
}}, {{ threshold: 0.06, rootMargin: '0px 0px -32px 0px' }});
document.querySelectorAll('.fade-in').forEach(el => obs.observe(el));

const MATRIX_CHIPS = [
  {{ cat: '1', en: 'User research planning', ru: 'Планирование исследований' }},
  {{ cat: '1', en: 'Surveys · interviews · observation', ru: 'Опросы · интервью · наблюдение' }},
  {{ cat: '1', en: 'Pattern & trend analysis', ru: 'Паттерны и тренды в данных' }},
  {{ cat: '1', en: 'Usability testing', ru: 'Юзабилити-тесты' }},
  {{ cat: '1', en: 'GA · Hotjar · Tableau mindset', ru: 'Аналитика и визуализация данных' }},
  {{ cat: '1', en: 'Design decision measurement', ru: 'Оценка эффективности дизайна' }},
  {{ cat: '1', en: 'Stakeholder-ready research decks', ru: 'Презентации исследований' }},
  {{ cat: '2', en: 'Hi-fi prototypes', ru: 'Прототипы hi-fi' }},
  {{ cat: '2', en: 'Layouts & composition', ru: 'Композиция и макеты' }},
  {{ cat: '2', en: 'Brand systems & guidelines', ru: 'Бренд-системы и гайды' }},
  {{ cat: '2', en: 'Illustration · icons · photo', ru: 'Иллюстрации · иконки · фото' }},
  {{ cat: '2', en: 'Typography & palette', ru: 'Типографика и палитры' }},
  {{ cat: '2', en: 'Motion & micro-interactions', ru: 'Моушн и микровзаимодействия' }},
  {{ cat: '2', en: 'Responsive UI', ru: 'Адаптивные интерфейсы' }},
  {{ cat: '2', en: 'Visual storytelling', ru: 'Визуальный сторителлинг' }},
  {{ cat: '2', en: 'AI in UI copy & assets', ru: 'AI в UI и контенте' }},
  {{ cat: '2', en: 'Social content scaling', ru: 'Контент для соцсетей' }},
  {{ cat: '3', en: 'Cross-functional collaboration', ru: 'Кросс-функциональные команды' }},
  {{ cat: '3', en: 'Timelines & resource focus', ru: 'Сроки и ресурсы' }},
  {{ cat: '3', en: 'Mentoring & leadership', ru: 'Менторство и лидерство' }},
  {{ cat: '3', en: 'Continuous learning culture', ru: 'Культура обучения' }},
  {{ cat: '3', en: 'Professional ownership', ru: 'Ответственность за результат' }},
  {{ cat: '4', en: 'Drawing & painting craft', ru: 'Рисунок и живопись' }},
  {{ cat: '4', en: 'Color & composition eye', ru: 'Цвет и композиция' }},
  {{ cat: '4', en: 'Visual hierarchy intuition', ru: 'Иерархия и ритм' }},
  {{ cat: '4', en: 'Hand-made → digital translation', ru: 'От руки к цифре' }}
];

(function buildMatrix(){{
  const grid = document.getElementById('matrixGrid');
  if (!grid) return;
  MATRIX_CHIPS.forEach((row) => {{
    const el = document.createElement('span');
    el.className = 'mc';
    el.dataset.cat = row.cat;
    el.innerHTML = '<span data-en>' + row.en + '</span><span data-ru>' + row.ru + '</span>';
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
</script>
</body>
</html>
"""

(ROOT / "index.html").write_text(html, encoding="utf-8")
print("Wrote index.html", len(html))
