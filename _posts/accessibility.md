---
name: "Corral"
short_name: "Corral"
title: "Accessibility statement | Corral"
description: "How corrallib.com is built to be accessible, how it is checked on every build, and how to report a barrier."
keywords: "corrallib accessibility, accessibility statement"
author: "Sebastien Rousseau"
date: "2026-10-25"
news_publication_date: "2026-10-25"
layout: "page"
language: "en-GB"
schema: "page"
changefreq: "monthly"
eyebrow: "Accessibility"
headline: "Accessibility statement"
lead: "corrallib.com aims to be usable by everyone, with any input device and any assistive technology."
---
## How is the site built for accessibility?

- The site uses the Prism theme, whose colour pairs are checked at a 7:1
  contrast ratio for text and 3:1 for other elements, in light and dark mode.
- Navigation works without JavaScript; the menus are disclosure buttons with
  their expanded state announced, and Escape closes them.
- Every page has a skip link, one level-one heading and a language attribute.
- Light, dark and system themes are available from the header.

## How is it checked?

Every build runs the site generator's audit, which includes its WCAG checks,
and the build fails if the generator's quality gate reports an issue.

## How do I report a barrier?

Use the [contact form](/contact/) or
[open an issue](https://github.com/sebastienrousseau/corrallib.github.io/issues)
describing the page and the problem, and it will be fixed.
