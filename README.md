# Портфолио Oleg Devyatov — статический сайт

Репозиторий: https://github.com/olezhapth2/od

## GitHub Pages (после первого push)

1. На GitHub: **Settings → Pages → Build and deployment**.
2. В поле **Source** выберите **GitHub Actions** (не «Deploy from a branch»).
3. Дождитесь зелёного workflow **Deploy to GitHub Pages** во вкладке **Actions**.

Публичный URL обычно такой: **https://olezhapth2.github.io/od/** (может открыться через 1–3 минуты после успешного деплоя).

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
