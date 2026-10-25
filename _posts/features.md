---
name: "Corral"
short_name: "Corral"
title: "Features: layout, smart syncing, exec, mirroring and symbol lookup | Corral"
description: "What corralctl does: an organised Public/Private/Forks layout with Finder tags, smart syncing that skips unchanged clones, concurrent exec, mirroring to other forges, and cross-repository symbol lookup."
keywords: "corralctl features, smart sync git, git exec all repositories, mirror git forges, cross-repository symbol search"
author: "Sebastien Rousseau"
date: "2026-10-25"
news_publication_date: "2026-10-25"
layout: "page"
language: "en-GB"
schema: "page"
changefreq: "monthly"
eyebrow: "Features"
headline: "Six things corralctl does for your repositories"
lead: "Each section answers what the feature does, the command that runs it and where it stops. The MCP server has a page of its own."
nav_features: "true"
---
## Organised layout

**corralctl puts every clone at a predictable path:**
`Collection/Bucket/Name`. The collection is `Public`, `Private` or `Forks`; the
bucket is a Finder-friendly ecosystem name such as `Go`, `Rust`, `Python` or
`Web`. Repositories with no primary language go to `Other`, and
`.github.io` repositories always go to `Web`.

```text
~/Code/
├── Public/
│   ├── Go/corral/
│   └── Web/project.github.io/
├── Private/Python/internal-tool/
└── Forks/Rust/upstream-project/
```

Existing flat layouts are migrated into this structure and the empty folders
left behind are removed. If a fixed path matters to you, `--layout` takes a
template built from the placeholders `.Owner`, `.Name`, `.Collection`,
`.Bucket`, `.Language` and `.Visibility`.

On macOS, corralctl also writes native Finder tags (lifecycle colours plus
visibility, ecosystem, owner, fork, archive, template and mirror metadata)
without replacing tags you added yourself. Turn it off with
`--finder-tags=false`.

## Smart syncing

**corralctl skips `git pull` when nothing new was pushed.** Next to each
clone's `.git/` folder it keeps a `.corral-state.json` sidecar recording the
forge's `pushed_at` time. When the forge reports the same value on the next
run, the pull is skipped entirely. The project's README puts the saving at
10 to 50 times on syncs.

- `--force-sync` pulls every clone regardless.
- `--no-sync` clones what is missing and updates nothing.

## Exec mode

**`corralctl exec` runs one shell command across every clone concurrently.**
Narrow it with the same filters as cloning:

```bash
corralctl exec "git status -s" --languages go,rust --visibility private
```

## Mirror to other forges

**`corralctl sync` pushes the organised tree out to other forges.** For each
repository and destination it creates the remote repository if needed, with
the visibility its folder says (`Public/` or `Private/`), then pushes every
branch and tag in one round trip.

```bash
corralctl sync --to gitlab --to gitea@https://git.example.com --dry-run
```

Branches are never force-pushed: a destination that has moved on is refused
and reported. Two local repositories with the same name, a push back to a
repository's own origin, and a destination with the other visibility are all
refused rather than guessed at. Results come as text, JSON or NDJSON, and the
exit code is non-zero if any repository failed.

## Interactive selection

**`corralctl -i <owner>` opens a terminal dashboard** to search, sort and pick
the repositories to clone before anything runs. Space toggles a repository,
`/` enters command mode (`/sort language`, `/all`, `/none`), and Enter starts
the run.

## Cross-repository symbol lookup

**corralctl answers where something is declared across every clone on the
machine,** not only in the repository an editor has open. Through the
[MCP server](/mcp-server/), `corral_find_symbol` returns the repository, file,
line and kind of a declaration; `corral_search_code` finds where text is
written; `corral_repo_overview` summarises one repository in a single call.

- **Indexed languages:** Go, Python, TypeScript, JavaScript and Rust. Go is
  parsed with the Go compiler's own parser; the others with a line scanner
  that ignores comments and string contents.
- **Measured:** on a real 187-repository workspace, a cross-repository
  lookup went from 6.9 s to 1.3 s, mostly from searching repositories
  concurrently and the rest from a symbol cache.
- **Limits:** it does not resolve types, find references or rename. A
  language server does that, one project at a time.
