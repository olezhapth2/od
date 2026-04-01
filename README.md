# Портфолио Oleg Devyatov — статический сайт

Репозиторий: https://github.com/olezhapth2/od

## GitHub Pages

Сайт раздаётся **напрямую из ветки `main`** (без Actions-артефактов — так стабильнее).

1. **Settings → Pages → Build and deployment**.
2. **Source:** выберите **Deploy from a branch** (не GitHub Actions).
3. **Branch:** `main`, папка **`/ (root)`**, Save.

Файл **`.nojekyll`** в корне отключает Jekyll, чтобы не ломалась раздача статики.

Публичный URL: **https://olezhapth2.github.io/od/** (после сохранения настроек подождите 1–3 минуты).

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
