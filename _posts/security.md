---
name: "Corral"
short_name: "Corral"
title: "Security: how corralctl protects your workspace and credentials | Corral"
description: "corralctl's security model: credentials kept out of argv and .git/config, non-interactive git, deletions that refuse unpublished work, a sandboxed MCP server, and signed, reproducible releases."
keywords: "corralctl security, git credentials safety, MCP server sandbox, cosign signed releases, SLSA provenance"
author: "Sebastien Rousseau"
date: "2026-10-25"
news_publication_date: "2026-10-25"
layout: "page"
language: "en-GB"
schema: "page"
changefreq: "monthly"
eyebrow: "Security"
headline: "Built to limit the damage a mistake can do"
lead: "corralctl runs with your own credentials on your own machine, so its job is to keep a mistake small: in its commands, in its MCP server and in its releases."
nav_security: "true"
---
## How are my credentials handled?

- **Never in `argv` or `.git/config`.** The GitHub token is passed to git as
  an `http.extraheader` scoped to `https://github.com/`, so a submodule on
  another host cannot see it.
- **Never in logs.** Clone errors leave out their arguments, so a token
  embedded in a URL cannot reach a log.
- **Never prompted for.** Git always runs non-interactively, so an
  unattended run fails instead of hanging on a password prompt.

## Can corralctl delete my work?

Only clones that pass every check. `prune` and the MCP delete tool refuse any
clone with working-tree changes, commits on a branch no remote has, stashes,
local-only tags, gitignored files such as `.env` or local databases, or
submodules with unpublished commits, and they name the reason for each
refusal.

## How is the MCP server contained?

It is read-only by default, writes need `--enable-mutations`, deletion needs a
second flag and a person's approval for each clone, and every path is checked
against one sandbox root. The [MCP server page](/mcp-server/) has the detail.

## How do I know a release is genuine?

- Releases are signed with **keyless cosign**.
- Each carries **SLSA build provenance** and a **CycloneDX SBOM**.
- Builds use `-trimpath` and a commit-pinned timestamp, so two builds of the
  same commit are byte-identical.
- Every GitHub Action is pinned by commit SHA, and `govulncheck` runs on
  every push.

## Is it fuzz-tested?

Yes, at the boundaries that parse input or resolve paths: layout evaluation,
language normalisation, remote-URL parsing and the sandbox check. The fuzz
targets run on every push. corralctl is not enrolled in OSS-Fuzz.

## How do I report a vulnerability?

Privately, never in a public issue: follow
[SECURITY.md](https://github.com/sebastienrousseau/corralctl/security/policy)
in the repository. For this website, write to sebastian.rousseau@gmail.com.
