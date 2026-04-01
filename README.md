# Портфолио Oleg Devyatov — статический сайт

Репозиторий: https://github.com/olezhapth2/od

## GitHub Pages

Деплой через **GitHub Actions** → ветка **`gh-pages`** (workflow `Deploy to gh-pages`).

1. **Settings → Pages → Build and deployment**.
2. **Source:** **Deploy from a branch**.
3. **Branch:** выберите **`gh-pages`**, папка **`/ (root)`**, Save.

После каждого push в `main` workflow обновляет `gh-pages`. Подождите 1–3 минуты и откройте:

**https://olezhapth2.github.io/od/**

В `index.html` добавлен скрипт `<base>` только на `*.github.io`, чтобы CSS и картинки грузились из подпути `/od/` (в т.ч. если URL без завершающего `/`).

Файл **`.nojekyll`** отключает Jekyll.

## Локальный просмотр

```bash
cd od
python3 -m http.server 8080
```

Откройте http://127.0.0.1:8080

## Docker

Сборка и запуск:

```bash
docker build -t oleg-portfolio .
docker run --rm -p 8080:80 oleg-portfolio
```

Сайт: http://127.0.0.1:8080

## Публикация «бесплатно»

Подойдёт любой хостинг статики: **Cloudflare Pages**, **GitHub Pages**, **Netlify**, **Vercel** (static), **Render** (static). Загрузите содержимое папки `od` (файлы `index.html`, `styles.css`, каталог `images/`).

После деплоя проверьте переключение EN/RU и открытие кейсов по клику.

## Пересборка HTML

Правки карточек компетенций: `_comp_cards.html` → запустите `python3 assemble_index.py` (или правьте `assemble_index.py` и снова запустите скрипт).
