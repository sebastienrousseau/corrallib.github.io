---
name: "Corral"
short_name: "corrallib"
title: "CLI Command Reference & Manifest Syntax"
description: "Comprehensive CLI documentation for corral commands including sync, status, exec, and init."
keywords: "corral documentation, corral CLI commands, Corral.toml syntax"
author: "Sebastien Rousseau"
date: "2026-09-01"
language: "en-GB"
layout: "page"
permalink: "https://corrallib.com/documentation/index.html"
logo: "https://cloudcdn.pro/cmn/v1/logos/cmn.svg"
banner: "https://cloudcdn.pro/stocks/images/quantum-computer-room-1200.webp"
banner_alt: "Corral — High-Performance Repository & Workspace Engine"
---

# CLI Command Reference & Manifest Syntax

## Commands

### `corral sync`
Synchronizes all repositories defined in `Corral.toml`.
- `--threads <N>`: Number of concurrent worker threads (default: CPU core count).
- `--depth <N>`: Create shallow clones with history truncated to specified commits.
- `--force`: Discard local uncommitted changes and reset to remote HEAD.

### `corral status`
Generates a tabular health report of all workspace repositories:
- Untracked files
- Uncommitted modifications
- Ahead / Behind commit counters vs remote branch

### `corral exec`
Executes an arbitrary command across all managed repositories in parallel:
```bash
corral exec -- git pull --rebase
corral exec -- cargo test
```
