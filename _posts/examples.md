---
name: "Corral"
short_name: "corrallib"
title: "Workspace Configuration Examples & Manifests"
description: "Sample Corral.toml configurations for microservices, financial pipelines, and open-source ecosystems."
keywords: "corral examples, Corral.toml examples"
author: "Sebastien Rousseau"
date: "2026-09-01"
language: "en-GB"
layout: "page"
permalink: "https://corrallib.com/examples/index.html"
logo: "https://cloudcdn.pro/cmn/v1/logos/cmn.svg"
banner: "https://cloudcdn.pro/stocks/images/quantum-computer-room-1200.webp"
banner_alt: "Corral — High-Performance Repository & Workspace Engine"
---

# Workspace Examples

## 1. Financial Systems Workspace Example

```toml
[workspace]
name = "cib-financial-infrastructure"
version = "0.0.1"

[[repositories]]
name = "kyberlib"
url = "git@github.com:sebastienrousseau/kyberlib.git"
branch = "main"
destination = "libs/crypto/kyberlib"

[[repositories]]
name = "bankstatementparser"
url = "git@github.com:sebastienrousseau/bankstatementparser.git"
branch = "main"
destination = "libs/parsers/bankstatementparser"

[[repositories]]
name = "hsh"
url = "git@github.com:sebastienrousseau/hsh.git"
branch = "main"
destination = "libs/crypto/hsh"
```
