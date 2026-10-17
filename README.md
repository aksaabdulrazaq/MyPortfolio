# MyPortfolio

Personal portfolio website built with **Django** and **Tailwind CSS**. Content (bio, education, skills, projects) is managed through the Django admin panel and exported as a static site with **django-distill**, so it can be hosted for free on GitHub Pages or Netlify.

## Tech stack

- Python 3.10+ / Django
- SQLite (content storage)
- Tailwind CSS (via CDN) for styling
- django-distill (static site generation)

## Project structure

```
MyPortfolio/
├── manage.py
├── requirements.txt
├── myportfolio/        # Project config: settings, urls, homepage view
├── bio/                # Bio app (name, job title, photo, description)
├── education/          # Education app (degrees)
├── skills/             # Skills app (skill + proficiency %)
├── experience/         # Experience app (jobs and projects)
├── templates/
│   └── index.html      # The single-page portfolio template
├── fixtures/
│   └── portfolio_data.json   # Starter content (loaded into the database)
├── media/              # Uploaded images (profile photo)
└── public/             # Generated static site (this is what gets deployed)
```

## Run locally

```bash
# 1. Create and activate a virtual environment
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate

# 2. Install dependencies
pip install -r requirements.txt

# 3. Create the database and load the starter content
python manage.py migrate
python manage.py loaddata fixtures/portfolio_data.json

# 4. Create an admin account
python manage.py createsuperuser

# 5. Start the server
python manage.py runserver
```

- Portfolio: http://127.0.0.1:8000/
- Admin panel: http://127.0.0.1:8000/admin/

## Editing your content

Log in to `/admin/` and edit **Bios**, **Degrees**, **Skills**, **Jobs** and **Projects**. Changes show up on the homepage immediately.

To save your current content back into the starter file:

```bash
python manage.py dumpdata bio education skills experience --indent 2 > fixtures/portfolio_data.json
```

## Build the static site

```bash
python manage.py distill-local public --collectstatic --force
```

This regenerates the `public/` folder (`index.html` + `media/`). Commit and deploy that folder.

## Deploy

**GitHub Pages:** the site links images with root-relative paths (`/media/...`), so it works when served from the root of a domain. Name the repository `<your-username>.github.io` (or use a custom domain), then publish the contents of `public/` (for example with a GitHub Actions workflow or by pointing Pages at that folder).

**Netlify:** set the publish directory to `public`.

## Environment variables (optional)

| Variable | Default | Purpose |
|---|---|---|
| `DJANGO_SECRET_KEY` | dev-only key | Set a real secret in any public deployment |
| `DJANGO_DEBUG` | `1` | Set to `0` in production |
| `DJANGO_ALLOWED_HOSTS` | `localhost,127.0.0.1` | Comma-separated list of hosts |

## License

Personal project. Feel free to use it as inspiration for your own portfolio.
