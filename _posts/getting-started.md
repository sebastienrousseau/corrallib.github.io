---
name: "Corral"
short_name: "Corral"
title: "Getting started: install corralctl and organise your repositories | Corral"
description: "Install corralctl with mise, Homebrew, the AUR, Nix or go install, sign in to GitHub, and clone and organise every repository you own with one command."
keywords: "install corralctl, corralctl homebrew, corralctl quick start, clone all repositories github"
author: "Sebastien Rousseau"
date: "2026-10-25"
news_publication_date: "2026-10-25"
layout: "page"
language: "en-GB"
schema: "page"
changefreq: "monthly"
eyebrow: "Getting started"
headline: "Install corralctl and organise your repositories"
lead: "You need git 2.30 or newer. Installing takes one command, and so does your first organised workspace."
nav_docs: "true"
---
## Install

Pick the method that matches how you manage tools.

**mise (macOS and Linux)**

```bash
mise use -g github:sebastienrousseau/corralctl
```

**Homebrew (macOS)**

```bash
brew install sebastienrousseau/tap/corralctl
```

**Arch Linux (AUR)**

```bash
yay -S corralctl-bin
```

**Nix (any platform)**

```bash
nix profile install github:sebastienrousseau/corralctl
```

**Go toolchain**

```bash
go install github.com/sebastienrousseau/corralctl/cmd/corralctl@latest
```

A binary built with `go install` reports its version as `dev`; use a release
build if you need `--version`. On Linux you can also install the `.deb` or
`.rpm` packages attached to each
[release](https://github.com/sebastienrousseau/corralctl/releases/latest).

## Quick start

```bash
# Sign in to the GitHub CLI once (or set GITHUB_TOKEN)
gh auth login

# Clone and organise every repository you own
corralctl clone my-username
```

Clones land under `~/Code` by default, in `Public/`, `Private/` and `Forks/`,
then by language. Run the same command again later and it only clones what is
new and pulls what changed.

## What to run next

| Command | Does |
| :--- | :--- |
| `corralctl plan <owner>` | Preview a run without touching disk |
| `corralctl status` | Inventory the clones and their state |
| `corralctl exec "<cmd>"` | Run a command in every clone |
| `corralctl sync --to <forge>` | Mirror the tree to another forge |
| `corralctl prune <owner>` | Remove clones gone upstream, refusing unpublished work |
| `corralctl mcp` | Serve the workspace to AI agents |

Other forges take `--forge`, for example
`corralctl my-group --forge gitlab`. The full list of commands and flags is in
the [command reference](/documentation/), and `man corralctl` works offline
once it is installed.
