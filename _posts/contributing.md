---
name: "Corral"
short_name: "Corral"
title: "Contributing to corralctl | Corral"
description: "How to contribute to corralctl: the toolchain you need, the branch and pull-request rules, signed and signed-off commits, and the checks a change must pass."
keywords: "contribute to corralctl, corralctl development, corralctl pull request"
author: "Sebastien Rousseau"
date: "2026-10-25"
news_publication_date: "2026-10-25"
layout: "page"
language: "en-GB"
schema: "page"
changefreq: "monthly"
eyebrow: "Contributing"
headline: "Contributing to corralctl"
lead: "Contributions are welcome through pull requests on GitHub. The full guide is CONTRIBUTING.md in the repository; this is the short version."
---
## What do I need?

Go 1.26 or newer, Make and Git. `nix develop` gives a shell with every tool
the CI gates use, pinned by the repository's `flake.lock`.

## How do I make a change?

1. Fork and clone the repository.
2. Create a branch from `main` and open the pull request against `main`.
   Every workflow filters on pull requests into `main`, so a pull request
   aimed at another branch runs no CI.
3. Make your change, then run `make format`, `make test` and `make build`.
4. Commit, push and open the pull request.

## What does a pull request need?

- `make test` passes and `make build` succeeds.
- The README is updated if behaviour changed.
- Every commit is cryptographically signed.
- Every commit carries a Developer Certificate of Origin sign-off
  (`git commit -s`).

Read the full [CONTRIBUTING.md](https://github.com/sebastienrousseau/corralctl/blob/main/CONTRIBUTING.md)
before opening a large change, and report security problems privately as
described on the [security page](/security/).
