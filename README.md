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
| Academic service list | `content/home/service.md` |
| News items | `content/news/` (section currently disabled) |

Publications are ordered by the `weight` field in each paper's front matter
(smaller = higher up).

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
