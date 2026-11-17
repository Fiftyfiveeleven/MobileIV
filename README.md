# optimizediv.com — redesigned site

A 30-page static site (plain HTML/CSS/JS, no framework). Same logo, colors
(navy #0C2340, ocean #1E6FD9, aqua #2BC4E0, red accent #E2493B) and fonts
(Bricolage Grotesque + Figtree) as the original.

## Deploy (Netlify, the current host)
Drag this whole folder (or optimizediv-site.zip) into the site's Deploys tab
in Netlify. `netlify.toml` is included. Then submit
https://optimizediv.com/sitemap.xml in Google Search Console and Bing Webmaster Tools.

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
