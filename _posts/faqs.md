---
name: "Corral"
short_name: "Corral"
title: "Frequently asked questions about corralctl | Corral"
description: "Answers about corralctl: what it is, which forges it supports, whether it deletes anything, running it unattended, Windows, backups, the MCP server and the licence."
keywords: "corralctl faq, corralctl questions, does corralctl delete repositories, corralctl windows"
author: "Sebastien Rousseau"
date: "2026-10-25"
news_publication_date: "2026-10-25"
layout: "page"
language: "en-GB"
schema: "page"
changefreq: "monthly"
eyebrow: "FAQ"
headline: "Frequently asked questions"
lead: "Short answers first; each links to the page with the detail where there is one."
nav_faqs: "true"
---
## What is corralctl?

corralctl is a free, open-source command-line tool and MCP server, written in Go under the GPL-3.0, that clones your repositories from six forges into one organised local layout and keeps them in sync.

## Which forges does it work with?

GitHub, GitLab, Gitea, Forgejo, Codeberg and Bitbucket. Repositories cloned by hand from any other host still work with the index, the MCP server and symbol lookup.

## Does it delete repositories that were deleted on the forge?

Not during a normal run. --orphans reports them, and the explicit prune command removes only those that pass the unpublished-work checks, after you confirm with --yes.

## Can I run it from cron or a systemd timer?

Yes. It runs non-interactively by default and every git credential prompt is turned off, so a scheduled run never hangs waiting for input.

## Where do repositories with no primary language go?

Into the Other ecosystem folder, for example Public/Other/my-repo.

## Does it work on Windows?

Binaries are published for Windows, but macOS Finder tags do nothing there and it is less tested than on macOS and Linux; WSL is the better-tested route.

## Is it a backup tool?

No. It clones working copies to read and edit. For archival copies that keep every ref, use git clone --mirror or a purpose-built backup tool.

## Does the MCP server send my code anywhere?

Not in its default read-only mode: it makes no network calls and never contacts the GitHub API. Only the opt-in clone and sync tools reach the network, through git.

## How much does it cost?

Nothing. corralctl is free software under the GNU General Public License v3.0.

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "FAQPage",
  "mainEntity": [
    {
      "@type": "Question",
      "name": "What is corralctl?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "corralctl is a free, open-source command-line tool and MCP server, written in Go under the GPL-3.0, that clones your repositories from six forges into one organised local layout and keeps them in sync."
      }
    },
    {
      "@type": "Question",
      "name": "Which forges does it work with?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "GitHub, GitLab, Gitea, Forgejo, Codeberg and Bitbucket. Repositories cloned by hand from any other host still work with the index, the MCP server and symbol lookup."
      }
    },
    {
      "@type": "Question",
      "name": "Does it delete repositories that were deleted on the forge?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Not during a normal run. --orphans reports them, and the explicit prune command removes only those that pass the unpublished-work checks, after you confirm with --yes."
      }
    },
    {
      "@type": "Question",
      "name": "Can I run it from cron or a systemd timer?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Yes. It runs non-interactively by default and every git credential prompt is turned off, so a scheduled run never hangs waiting for input."
      }
    },
    {
      "@type": "Question",
      "name": "Where do repositories with no primary language go?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Into the Other ecosystem folder, for example Public/Other/my-repo."
      }
    },
    {
      "@type": "Question",
      "name": "Does it work on Windows?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Binaries are published for Windows, but macOS Finder tags do nothing there and it is less tested than on macOS and Linux; WSL is the better-tested route."
      }
    },
    {
      "@type": "Question",
      "name": "Is it a backup tool?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "No. It clones working copies to read and edit. For archival copies that keep every ref, use git clone --mirror or a purpose-built backup tool."
      }
    },
    {
      "@type": "Question",
      "name": "Does the MCP server send my code anywhere?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Not in its default read-only mode: it makes no network calls and never contacts the GitHub API. Only the opt-in clone and sync tools reach the network, through git."
      }
    },
    {
      "@type": "Question",
      "name": "How much does it cost?",
      "acceptedAnswer": {
        "@type": "Answer",
        "text": "Nothing. corralctl is free software under the GNU General Public License v3.0."
      }
    }
  ]
}
</script>
