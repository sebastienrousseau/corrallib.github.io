---
name: "Corral"
short_name: "corrallib"
title: "Getting Started with Corral: Installation & Quickstart"
description: "How to install Corral via Cargo, Homebrew, and Docker alongside step-by-step workspace initialization guides."
keywords: "install corral, cargo corrallib, git workspace setup"
author: "Sebastien Rousseau"
date: "2026-09-01"
language: "en-GB"
layout: "page"
permalink: "https://corrallib.com/getting-started/index.html"
logo: "https://cloudcdn.pro/cmn/v1/logos/cmn.svg"
banner: "https://cloudcdn.pro/stocks/images/quantum-computer-room-1200.webp"
banner_alt: "Corral — High-Performance Repository & Workspace Engine"
---

# Getting Started with Corral

Corral provides a unified developer workflow for multi-repository codebases.

## 1. Installation

### Install via Cargo (Rust)
```bash
cargo install corrallib
```

### Run via Docker
```bash
docker run --rm -v $(pwd):/workspace ghcr.io/sebastienrousseau/corrallib:latest sync
```

---

## 2. Quickstart Workflow

### Initialize a Workspace
```bash
cd ~/Code/Workspaces
corral init
```

This generates a template `Corral.toml` manifest in the current directory:

```toml
[workspace]
name = "financial-services-stack"
version = "0.0.1"

[[repositories]]
name = "kyberlib"
url = "https://github.com/sebastienrousseau/kyberlib.git"
branch = "main"
destination = "crypto/kyberlib"

[[repositories]]
name = "bankstatementparser"
url = "https://github.com/sebastienrousseau/bankstatementparser.git"
branch = "main"
destination = "parsers/bankstatementparser"
```

### Sync All Repositories
```bash
corral sync
```
