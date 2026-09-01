---
name: "Corral"
short_name: "corrallib"
title: "Security Architecture: Zero Telemetry, Credential Safety & SBOM"
description: "Security guarantees, credential isolation, memory safety, and CycloneDX SBOM provenance."
keywords: "corral security, zero telemetry git tool"
author: "Sebastien Rousseau"
date: "2026-09-01"
language: "en-GB"
layout: "page"
permalink: "https://corrallib.com/security/index.html"
logo: "https://cloudcdn.pro/cmn/v1/logos/cmn.svg"
banner: "https://cloudcdn.pro/stocks/images/quantum-computer-room-1200.webp"
banner_alt: "Corral — High-Performance Repository & Workspace Engine"
---

# Security Architecture & Trust Guarantees

## Core Security Pillars

### 1. 100% Zero-Telemetry Guarantee
Corral contains no analytics SDKs, no tracking pixels, and no remote telemetry. All workspace orchestration occurs entirely on your local machine.

### 2. Credential Isolation
Corral does not store or log Git passwords, SSH passphrases, or personal access tokens. It delegates authentication directly to your system's native `ssh-agent` and Git credential helper.

### 3. Supply Chain Security & Sigstore Signing
Every release binary is signed with Sigstore Cosign and accompanied by a CycloneDX Software Bill of Materials (SBOM).
