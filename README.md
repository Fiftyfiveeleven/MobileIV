# optimizediv.com — redesigned site

A 30-page static site (plain HTML/CSS/JS, no framework). Same logo, colors
(navy #0C2340, ocean #1E6FD9, aqua #2BC4E0, red accent #E2493B) and fonts
(Bricolage Grotesque + Figtree) as the original.

## Deploy (Vercel)
1. In Vercel: Add New > Project > import this GitHub repo.
2. Framework Preset: **Other**. Leave Build Command and Install Command empty;
   Root directory is the repo root. No build step is needed.
3. Deploy. Then in Project > Settings > Domains add `optimizediv.com` and
   `www.optimizediv.com` (redirect www to the apex), and update DNS as Vercel shows.
4. Submit https://optimizediv.com/sitemap.xml in Google Search Console and Bing Webmaster Tools.

`vercel.json` serves the folder-based pages at clean URLs with trailing slashes
(matching the canonical URLs), sets caching/security headers, and Vercel serves
`404.html` automatically. `.vercelignore` keeps `_build/` and this README off the live site.

## Edit content
All copy lives in `_build/build.py` (drips, prices, ingredients, towns, FAQ,
guides). Change it, then run:

    python3 _build/build.py

## Page map
- /                        Home
- /iv-menu/                Menu + price comparison
- /iv-menu/<drip>/         7 drip pages (Service + Offer + FAQ schema)
- /ingredients/            Ingredient glossary (DefinedTerm schema)
- /how-it-works/           HowTo schema
- /group-iv-therapy/       Bridal parties, households, teams
- /service-areas/ + 8 town pages
- /about/  /safety/  /faq/  /contact/
- /guides/ + 4 articles (Article schema)
- sitemap.xml, robots.txt (allows AI crawlers), llms.txt (AI summary)
