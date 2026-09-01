---
name: "Corral"
short_name: "corrallib"
title: "API Reference: Rust Crate (corrallib)"
description: "Programmatic API documentation for embedding corrallib in custom developer tools and CI pipelines."
keywords: "corrallib API, rust git crate"
author: "Sebastien Rousseau"
date: "2026-09-01"
language: "en-GB"
layout: "page"
permalink: "https://corrallib.com/api/index.html"
logo: "https://cloudcdn.pro/cmn/v1/logos/cmn.svg"
banner: "https://cloudcdn.pro/stocks/images/quantum-computer-room-1200.webp"
banner_alt: "Corral — High-Performance Repository & Workspace Engine"
---

# API Reference

Embed Corral directly in your Rust applications.

```rust
use corrallib::{Workspace, SyncOptions};
use std::path::Path;

#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let workspace = Workspace::from_file(Path::new("Corral.toml"))?;
    
    let options = SyncOptions::builder()
        .threads(8)
        .depth(Some(1))
        .build();

    workspace.sync_all(&options).await?;
    Ok(())
}
```
