---
name: "Corral"
short_name: "corrallib"
title: "Performance Benchmarks: Parallel vs Sequential Git Cloning"
description: "Empirical benchmarks comparing Corral against sequential git cloning and shell scripts across 100 repositories."
keywords: "corral benchmarks, git clone speed comparison"
author: "Sebastien Rousseau"
date: "2026-09-01"
language: "en-GB"
layout: "page"
permalink: "https://corrallib.com/benchmarks/index.html"
logo: "https://cloudcdn.pro/cmn/v1/logos/cmn.svg"
banner: "https://cloudcdn.pro/stocks/images/quantum-computer-room-1200.webp"
banner_alt: "Corral — High-Performance Repository & Workspace Engine"
---

# Performance Benchmarks

Benchmarked across 100 repositories on an 8-core Apple Silicon M-series machine:

<div class="row g-3 my-4">
<div class="col-md-4">
<div class="stat-card">
<div class="stat-figure">14.2s</div>
<div class="stat-label">Corral Sync (100 Repos)</div>
<div class="stat-source">Parallel async worker pool</div>
</div>
</div>
<div class="col-md-4">
<div class="stat-card">
<div class="stat-figure">148.6s</div>
<div class="stat-label">Sequential Git Clone</div>
<div class="stat-source">Standard shell loop baseline</div>
</div>
</div>
<div class="col-md-4">
<div class="stat-card">
<div class="stat-figure">10.4x</div>
<div class="stat-label">Throughput Speedup</div>
<div class="stat-source">Zero lock contention</div>
</div>
</div>
</div>
