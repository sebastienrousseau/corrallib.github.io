---
name: "Corral"
short_name: "Corral"
title: "MCP server for AI coding agents | Corral"
description: "corralctl mcp serves your local clones to Claude Code, Cursor, Cline and other MCP clients: read-only by default, sandboxed to one root, with cross-repository symbol and code search."
keywords: "corralctl mcp, MCP server git repositories, model context protocol workspace, claude code mcp repositories, cross-repository code search"
author: "Sebastien Rousseau"
date: "2026-10-25"
news_publication_date: "2026-10-25"
layout: "page"
language: "en-GB"
schema: "page"
changefreq: "monthly"
eyebrow: "MCP server"
headline: "Your local workspace, served to AI coding agents"
lead: "corralctl mcp gives an agent every clone on the machine to search and read, without contacting the GitHub API and without writing anything unless you allow it."
---
## What does the MCP server do?

`corralctl mcp` is a Model Context Protocol server over the repositories
corralctl has cloned. Where a forge's own MCP server covers the remote API
(issues, pull requests, search), corralctl covers the local copies, organised
by visibility and language. **In its default read-only mode it makes no
network calls at all.**

## Which tools does it offer?

Nine read-only tools:

| Tool | Answers |
| :--- | :--- |
| `corral_list_repos` | Local clones filtered by visibility, language, name or sync state |
| `corral_find_repo` | One clone from a fuzzy name, or the candidates |
| `corral_get_repo_metadata` | Full metadata for one clone, including its branch |
| `corral_status_summary` | Counts by visibility and language |
| `corral_workspace_index` | The whole workspace in one structured call |
| `corral_find_symbol` | Where a symbol is declared, across every clone |
| `corral_search_code` | Where text appears, across every clone |
| `corral_repo_overview` | One repository's shape in a single call |
| `corral_discover_repos` | Repositories on disk that corralctl does not manage yet |

With `--enable-mutations`, four more: `corral_sync_repo`, `corral_clone_repo`,
`corral_adopt_repo` and, only with `--enable-destructive-mutations` as well,
`corral_delete_repo`.

## How do I add it to Claude Code or Cursor?

Claude Code:

```bash
claude mcp add corral -- corralctl mcp
```

Cursor or Cline, in `mcp.json`:

```json
{
  "mcpServers": {
    "corral": { "command": "corralctl", "args": ["mcp"] }
  }
}
```

A container image, `ghcr.io/sebastienrousseau/corralctl`, runs the same
server against a read-only mount of your workspace; the
[README](https://github.com/sebastienrousseau/corralctl#install) has the
configuration.

## What stops an agent doing damage?

- **Read-only by default.** Writes need `--enable-mutations`; deletion needs
  a second flag.
- **Deletion fails closed.** A clone with uncommitted, unpushed, stashed,
  submodule or gitignored work is refused, with the reason written to the
  audit log.
- **A person approves each deletion** over MCP elicitation, unless you pass
  `--no-confirm-deletes` for a workspace you are willing to lose.
- **Sandboxed paths.** File lookups canonicalise symlinks and block `..`, so
  an agent cannot read outside the root.
- **Audited.** Every mutation writes an intent record before it runs and a
  completion record after, to `~/.local/state/corral/mutations.log`.
- **Local by default.** The standard transport is stdio. The HTTP transports
  bind loopback only and refuse `0.0.0.0` unless you pass `--allow-remote`.
