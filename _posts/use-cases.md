---
name: "Corral"
short_name: "Corral"
title: "Use cases: many repositories, AI agents, forge migration and unattended syncs | Corral"
description: "Four jobs corralctl does: keeping hundreds of repositories cloned and current, giving AI coding agents the whole workspace, mirroring between forges, and running syncs from cron or systemd."
keywords: "clone all github repositories, manage many git repositories, MCP for coding agents, migrate github to gitlab, git sync cron"
author: "Sebastien Rousseau"
date: "2026-10-25"
news_publication_date: "2026-10-25"
layout: "page"
language: "en-GB"
schema: "page"
changefreq: "monthly"
eyebrow: "Use cases"
headline: "Four jobs corralctl does well"
lead: "And, at the end, the jobs it is the wrong tool for."
nav_use_cases: "true"
---
<h2 id="many-repositories">Keeping hundreds of repositories cloned and current</h2>

If you own or work across hundreds of repositories, the hard part is not
cloning them once but keeping the copies right. `corralctl clone <owner>`
clones what is missing, pulls what changed and skips the rest, so a daily run
is cheap. `--concurrency` raises the number of workers, and `--languages`,
`--visibility` and `--include-forks` narrow what is fetched.

<h2 id="ai-coding-agents">Giving an AI coding agent the whole workspace</h2>

A coding agent usually sees the one repository it was opened in.
`corralctl mcp` exposes every clone on the machine over the Model Context
Protocol, so the agent can ask which repository declares a symbol, search
code across all of them, and read a repository's shape before opening files.
It is read-only unless you opt in, and deletion asks a person to approve each
clone. See the [MCP server page](/mcp-server/).

<h2 id="moving-between-forges">Moving or mirroring between forges</h2>

Clone from GitHub, GitLab, Gitea, Forgejo, Codeberg or Bitbucket, then run
`corralctl sync --to <forge>` to mirror the organised tree onto any of the
others, with each repository's visibility preserved. Start with `--dry-run`
to see every repository that would be created or pushed.

<h2 id="unattended-syncs">Running syncs from cron or systemd</h2>

corralctl runs every git call without prompts, so an unattended run that hits
a credential problem fails instead of hanging. Results go to stdout as text,
JSON or NDJSON, diagnostics go to stderr, and the exit code is non-zero when
any repository failed, which is what a scheduler needs to alert on.

## When not to use corralctl

- **For a full backup.** It clones working copies; use `git clone --mirror`
  or a purpose-built tool for archival copies.
- **For a forge it does not list from.** Clones from any host work with the
  index and the MCP server, but listing an owner works only on the six forges.
- **If your repositories must stay where they are.** Its value is a
  consistent layout; `--layout` can match your tree, or another tool may suit.
- **For code intelligence.** It finds declarations, not references or types.
- **On Windows without WSL.** Binaries are published, but Finder tags do
  nothing there and it is less tested than on macOS and Linux.

The [comparison page](/compare/) shows which tool fits each of these jobs.
