---
name: "Corral"
short_name: "corrallib"
title: "Frequently Asked Questions (FAQ): Corral"
description: "Common questions about Corral, Git submodules comparison, CI/CD usage, and authentication."
keywords: "corral FAQ, git workspace questions"
author: "Sebastien Rousseau"
date: "2026-09-01"
language: "en-GB"
layout: "faqs"
permalink: "https://corrallib.com/faqs/index.html"
logo: "https://cloudcdn.pro/cmn/v1/logos/cmn.svg"
banner: "https://cloudcdn.pro/stocks/images/quantum-computer-room-1200.webp"
banner_alt: "Corral — High-Performance Repository & Workspace Engine"
---

# Frequently Asked Questions

<div class="apple-faq-section my-4">
<div class="apple-faq-header">
<h2 class="apple-faq-title">Questions? Answers.</h2>
<button type="button" class="apple-faq-expand-btn" id="faqExpandAllBtn" aria-expanded="false">
<span class="apple-faq-btn-text">Expand all</span>
<svg class="apple-faq-expand-chevron" width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"></polyline></svg>
</button>
</div>

<div class="apple-faq-list">
<details class="apple-faq-item">
<summary class="apple-faq-summary">
<span class="apple-faq-question">How does Corral handle merge conflicts during sync?</span>
<span class="apple-faq-icon"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"></polyline></svg></span>
</summary>
<div class="apple-faq-body">
<p>By default, Corral performs fast-forward updates. If a repository has local uncommitted changes or divergent history, Corral safely leaves the local branch intact and flags the repository in the status summary.</p>
</div>
</details>

<details class="apple-faq-item">
<summary class="apple-faq-summary">
<span class="apple-faq-question">Is Corral compatible with private GitHub/GitLab enterprise servers?</span>
<span class="apple-faq-icon"><svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="6 9 12 15 18 9"></polyline></svg></span>
</summary>
<div class="apple-faq-body">
<p>Yes. Any standard Git remote URL (HTTPS or SSH) is fully supported, including self-hosted GitLab, GitHub Enterprise Server, and Gitea.</p>
</div>
</details>
</div>
</div>
