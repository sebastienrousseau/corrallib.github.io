---
name: "Corral"
short_name: "Corral"
title: "Command reference: corralctl commands and flags | Corral"
description: "Every corralctl subcommand, the flags that change what a run does, sync options, multi-owner profiles, and where the full manual and Go API reference live."
keywords: "corralctl commands, corralctl flags, corralctl sync options, corralctl profiles, corralctl manual"
author: "Sebastien Rousseau"
date: "2026-10-25"
news_publication_date: "2026-10-25"
layout: "page"
language: "en-GB"
schema: "page"
changefreq: "monthly"
eyebrow: "Command reference"
headline: "corralctl commands and flags"
lead: "The commands you will use, the flags that change what they do, and where to find the rest."
nav_docs: "true"
---
## Commands

| Command | Does |
| :--- | :--- |
| `corralctl clone <owner>` | Clone what is missing and pull what is stale, into the organised layout |
| `corralctl plan <owner>` | Preview that reconciliation without touching disk |
| `corralctl status` | Inventory local clones and their state |
| `corralctl doctor <dir>` | Audit workspace hygiene, worktrees, disk budget and Finder tags |
| `corralctl prune <owner>` | Remove clones no longer upstream, refusing any with unpublished work |
| `corralctl adopt <dir>` | Find untracked local repositories and link them to a forge |
| `corralctl exec "<cmd>"` | Run a command across every clone |
| `corralctl sync --to <forge>` | Mirror the organised tree to other forges |
| `corralctl profile <name>` | Run a saved multi-owner profile |
| `corralctl mcp` | Serve the workspace to AI agents |

`corralctl <owner>` on its own is the same as `corralctl clone <owner>`.

## Flags that change a run

| Flag | Default | Effect |
| :--- | :--- | :--- |
| `--base-dir` | `$HOME/Code` | Root directory for clones |
| `--concurrency`, `-c` | `1` | Number of workers |
| `--dry-run`, `-n` | off | Show what would happen, change nothing |
| `--protocol`, `-p` | `https` | Clone over `https` or `ssh` |
| `--forge` | `github` | `gitlab`, `gitea`, `forgejo`, `codeberg` or `bitbucket` |
| `--visibility` | `all` | `public` or `private` only |
| `--languages` | | Comma-separated languages to include |
| `--include-forks` | on | Include forks, under `Forks/` |
| `--include-archived` | on | Include archived repositories |
| `--no-sync` / `--force-sync` | off | Never pull, or always pull |
| `--interactive`, `-i` | off | Pick repositories in the terminal dashboard |
| `--output` | `text` | `text`, `json` or `ndjson` |
| `--log-level` | `info` | Diagnostics on stderr: `error`, `warn`, `info`, `debug` |

Results go to stdout and diagnostics to stderr, so `--output json` stays
pipeable however noisy the run.

## Credentials

GitHub uses an explicit token, then `GITHUB_TOKEN`, then the `gh` CLI. Other
forges read `GITLAB_TOKEN`, `GITEA_TOKEN`, `FORGEJO_TOKEN`,
`CODEBERG_TOKEN` or `BITBUCKET_TOKEN`, each also accepted with a `CORRAL_`
prefix.

## Multi-owner profiles

Profiles live in `~/.config/corral/config.json` and run with
`corralctl profile <name>`. A profile sets its owners, base directory,
concurrency and, if needed, its own forge, so one config covers owners on
several hosts.

## Full documentation

- **User manual:** [doc.corrallib.com](https://doc.corrallib.com/)
- **Man pages:** `man corralctl`, and one per subcommand such as `man corralctl-mcp`
- **Go package reference:** [pkg.go.dev](https://pkg.go.dev/github.com/sebastienrousseau/corralctl)
- **Source and README:** [GitHub](https://github.com/sebastienrousseau/corralctl)
