# Baofu Han's Homepage

Source of [https://hanbaofu.github.io](https://hanbaofu.github.io), built with
[Hugo](https://gohugo.io/) and deployed automatically to GitHub Pages by
`.github/workflows/gh-pages.yml` on every push to `main`.

## Where to edit what

| What | File |
|---|---|
| Site title / URL | `config/_default/config.yaml` |
| Theme, footer, SEO, repo link | `config/_default/params.yaml` |
| Navigation bar | `config/_default/menus.yaml` |
| Bio, photo, interests, education, social links | `content/authors/admin/` |
| Publications (one folder per paper) | `content/publications/` |
| Homepage sections (on/off + order) | `content/home/` |
| News items | `content/news/` (one folder per item) |

## Updating the publication list

`content/publications/` is generated from Google Scholar by the
[scholar-collector](https://github.com/simongravelle/scholar-collector) submodule:

```bash
./update-publications.sh
```

It only adds folders that don't exist yet, so manual edits are kept. Papers that
Google Scholar doesn't know about yet can be added by hand in the same format
(see `content/publications/2026_Tu_ICCAD_.../index.md`).

Needs Python 3.12+ and `pip install scholarly numpy`.

## Build locally

```bash
hugo server
```

Requires Hugo **extended** (the CI uses 0.140.2).

## Credit

This site is based on the academic template by
[Simon Gravelle](https://github.com/simongravelle/simongravelle.github.io),
itself adapted from [wowchemy](https://wowchemy.com/) with custom CSS from
[nickballousite](https://github.com/nballou).
