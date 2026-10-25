---
name: "Corral"
short_name: "Corral"
title: "How corralctl works: from forge API to worker pool | Corral"
description: "What happens in one corralctl run: the git pre-flight, authentication, concurrent paginated listing, layout rendering, the worker pool, smart-sync decisions and the state sidecar."
keywords: "corralctl architecture, how corralctl works, git clone worker pool, smart sync pushed_at"
author: "Sebastien Rousseau"
date: "2026-10-25"
news_publication_date: "2026-10-25"
layout: "page"
language: "en-GB"
schema: "page"
changefreq: "monthly"
eyebrow: "How it works"
headline: "What happens in one corralctl run"
lead: "A run is a fixed sequence of steps, and each one can be seen with --dry-run or --log-level debug."
nav_docs: "true"
---
## The steps of a run

1. **Pre-flight.** corralctl checks that `git` is on `PATH` and stops with a
   clear error if not.
2. **Authenticate.** It resolves credentials: an explicit token, the
   environment, or the `gh` CLI.
3. **List repositories.** It fetches the first page from the forge API, and
   if there are more, fetches the rest concurrently, up to five pages at once.
4. **Filter and select.** Visibility, language, fork and archive filters
   apply; with `-i`, you pick in the terminal dashboard.
5. **Render paths.** The layout template turns each repository into its
   `Collection/Bucket/Name` path.
6. **Dispatch to workers.** A pool of `--concurrency` workers takes each
   repository and decides: clone it, skip it, or sync it.
7. **Smart sync.** For an existing clone, the worker compares the forge's
   `pushed_at` with the value stored in `.corral-state.json`, and runs
   `git pull --rebase --autostash` only if it advanced.
8. **Record and clean up.** Each worker stamps the sidecar file; at the end,
   empty folders left from an older flat layout are removed, and with
   `--orphans`, clones that no longer exist upstream are reported.

## Why it is a single static binary

corralctl is written in Go with no C dependencies (`CGO_ENABLED=0`), so a
release binary carries no libc coupling and runs as one file. The same
binary is the CLI, the terminal dashboard and the MCP server.

## Where to read more

The design decisions are recorded as architecture decision records in the
[repository](https://github.com/sebastienrousseau/corralctl/tree/main/docs/adr),
and [docs/ARCHITECTURE.md](https://github.com/sebastienrousseau/corralctl/blob/main/docs/ARCHITECTURE.md)
covers the packages.
