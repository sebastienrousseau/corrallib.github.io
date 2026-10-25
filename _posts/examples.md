---
name: "Corral"
short_name: "Corral"
title: "Examples: forges, profiles, exec, mirroring and JSON output | Corral"
description: "Copy-paste corralctl commands for GitLab, Codeberg and self-hosted Gitea, multi-owner profiles, running a command in every clone, mirroring with a dry run, and machine-readable output."
keywords: "corralctl examples, clone gitlab group, clone codeberg repositories, git exec all repos, mirror github to gitlab"
author: "Sebastien Rousseau"
date: "2026-10-25"
news_publication_date: "2026-10-25"
layout: "page"
language: "en-GB"
schema: "page"
changefreq: "monthly"
eyebrow: "Examples"
headline: "corralctl commands you can copy"
lead: "Each example is a real command from the corralctl documentation. Swap in your own owner names."
nav_docs: "true"
---
## Clone from forges other than GitHub

```bash
corralctl my-group --forge gitlab
corralctl my-user --forge codeberg
corralctl my-org --forge gitea --forge-url https://git.example.com
corralctl my-workspace --forge bitbucket
```

## Pick repositories before cloning

```bash
corralctl -i my-username
```

## Run a command in every clone

```bash
corralctl exec "git status -s" --languages go,rust --visibility private
```

## Mirror to two other forges, previewing first

```bash
export GITLAB_TOKEN=...
export GITEA_TOKEN=...
corralctl sync --to gitlab --to gitea@https://git.example.com --dry-run
corralctl sync --to gitlab --to gitea@https://git.example.com
```

## Keep your existing folder structure

```bash
corralctl my-org --layout "OWNER/NAME"
```

`OWNER` and `NAME` stand for the `.Owner` and `.Name` template placeholders;
the [features page](/features/#organised-layout) lists them all.

## Machine-readable results

```bash
corralctl my-username --output json --log-level error > repos.json
```

## Housekeeping

```bash
corralctl status --base-dir ~/Code
corralctl doctor ~/Code --prune-worktrees
corralctl prune my-username --dry-run
```
