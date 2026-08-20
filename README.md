<!-- SPDX-License-Identifier: Apache-2.0 -->

# corrallib.com

Source of [corrallib.com](https://corrallib.com) — the website for
[corral](https://github.com/sebastienrousseau/corral), a command-line tool that
clones and organises every repository you own into a tidy, predictable
workspace.

## Layout

| path | purpose |
| --- | --- |
| `docs/` | the published site — GitHub Pages serves this directory from `main` |
| `docs/CNAME` | the custom domain, `corrallib.com` |

## Publishing

GitHub Pages is configured with source `main` / `docs`. Pushing to `main`
publishes.

`docs/CNAME` must contain `corrallib.com` and must survive every build. GitHub
Pages provisions the TLS certificate for that domain, and a build that drops the
file silently un-configures the custom domain, which takes the certificate with
it.

## A note on Cloudflare

`corrallib.com` sits behind Cloudflare. The apex records have to be **DNS-only**
(grey cloud) while GitHub Pages provisions its certificate — the ACME challenge
resolves to Cloudflare's edge otherwise and never reaches GitHub, so the
certificate never issues and Cloudflare returns `526` in Full (strict) mode.

Once "Enforce HTTPS" is available in Settings → Pages, the apex can be proxied
again and Full (strict) is the correct setting to keep.

Verify the origin certificate with:

```bash
echo | openssl s_client -connect 185.199.108.153:443 \
  -servername corrallib.com 2>&1 | grep ^subject=
```

It should report `CN=corrallib.com`, not `CN=*.github.io`.

## Licence

Apache-2.0. See [LICENSE](LICENSE).
