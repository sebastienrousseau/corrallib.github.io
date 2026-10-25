---
name: "Corral"
short_name: "Corral"
title: "Performance: what makes corralctl fast, and what was measured | Corral"
description: "The performance figures published for corralctl, how they were measured, and the settings that change how long a run takes."
keywords: "corralctl performance, fast git clone many repositories, cross-repository symbol lookup speed"
author: "Sebastien Rousseau"
date: "2026-10-25"
news_publication_date: "2026-10-25"
layout: "page"
language: "en-GB"
schema: "page"
changefreq: "monthly"
eyebrow: "Performance"
headline: "What makes corralctl fast"
lead: "Two figures are published, with how they were obtained. There is no wider benchmark suite yet, so this page claims nothing more."
---
## What has been measured?

- **Cross-repository symbol lookup: 6.9 s to 1.3 s** on a real
  187-repository workspace. Most of the gain came from searching repositories
  concurrently instead of one after another; the rest from caching extracted
  symbols under `$XDG_CACHE_HOME/corral/symbols`.
- **Smart syncing: 10 to 50 times faster syncs**, as stated in the project
  README, from skipping `git pull` for every clone whose forge reports no new
  push. The saving depends on how many of your repositories changed since the
  last run.

## What changes how long a run takes?

| Setting | Effect |
| :--- | :--- |
| `--concurrency` | More workers clone and pull at once; the default is 1 |
| `--no-sync` | Skips pulls entirely, for a clone-only run |
| `--clone-depth` | Shallow clones transfer less history |
| `--api-request-timeout` | Caps a single forge API request (30 s by default) |

Listing an owner's repositories is already concurrent: after the first page,
corralctl fetches up to five pages at once.
