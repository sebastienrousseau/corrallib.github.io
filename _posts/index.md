---
name: "Corral"
short_name: "Corral"
title: "Corral: clone and organise every repository you own"
description: "corralctl clones your repositories from GitHub, GitLab, Gitea, Forgejo, Codeberg and Bitbucket into one organised local layout, keeps them in sync, and serves them to AI coding agents over MCP."
keywords: "corralctl, clone all repositories, organise git repositories, multi-repo workspace, MCP server, git forge mirror"
author: "Sebastien Rousseau"
date: "2026-10-25"
news_publication_date: "2026-10-25"
layout: "index"
language: "en-GB"
schema: "page"
changefreq: "weekly"
eyebrow: "Open-source command-line tool"
headline: "Clone and organise every repository you own"
lead: "corralctl clones your repositories from six forges into one predictable layout, keeps them in sync, and lets AI coding agents search all of them at once."
---
## What is corralctl?

corralctl is a free, open-source command-line tool and MCP server, written in Go
and released under the GNU General Public License v3.0. Given an owner name, it
lists that owner's repositories on GitHub, GitLab, Gitea, Forgejo, Codeberg or
Bitbucket, clones the ones missing from your machine, pulls the ones that have
changed, and files every clone under `Public/`, `Private/` or `Forks/`, then by
language. Corral is the project; `corralctl` is the binary you run.

## How is it different from a clone script?

A loop over `git clone` gets the repositories onto disk once. corralctl keeps
them right afterwards:

- **It converges.** Run it again and it clones only what is new, pulls only
  what was pushed to since the last run, and leaves the rest untouched.
- **It previews.** `corralctl plan` shows what a run would do without
  changing anything.
- **It refuses before it deletes.** `corralctl prune` removes clones that no
  longer exist upstream, but declines any clone holding uncommitted,
  unpushed, stashed or gitignored work.
- **It reaches past one forge.** It clones from six hosts, and
  `corralctl sync` mirrors the organised tree back out to them.

## Who makes it?

Corral is written and maintained by
[Sebastien Rousseau](https://sebastienrousseau.com/), a payments leader with
19 years in banking who builds open-source tools for finance and for
developers. The source, the issue tracker and every signed release are on
[GitHub](https://github.com/sebastienrousseau/corralctl). Read more on the
[about page](/about/).
