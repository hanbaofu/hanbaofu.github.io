---
widget: pages

# This file represents a page section.
headless: true

# Order that this section appears on the page.
weight: 40

title: Publications
subtitle: 'See also my [Scholar](https://scholar.google.com/citations?user=hjrZh74AAAAJ&hl) profile'

content:
  # Filter on criteria
  filters:
    folders:
      - publications
    tag: 'first-author'
    category: ''
    publication_type: ''
    author: ''
    exclude_featured: false
    exclude_future: false
    exclude_past: false
  # Choose how many pages you would like to display (0 = all pages)
  count: 6
  # Choose how many pages you would like to offset by
  offset: 0
  # Page order: descending (desc) or ascending (asc) date.
  order: desc
  # Always link to the full publication list, not just when truncated.
  archive:
    enable: true
    link: /publications/
    text: See all publications
design:
  # Choose a view for the listings:
  view: citation
  columns: '2'
---
