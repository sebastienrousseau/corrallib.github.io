# Changelog

All notable changes to corrallib.com are documented here. The format is
based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/). The site
ships in lockstep with corralctl; iterations before 0.0.55 were never
tagged and are recorded in pull requests #1 to #5.

## [0.0.55]

### Changed

- Built with ssg 0.0.76, the latest release, up from 0.0.69. Both
  workflows pin the 0.0.76 archive by SHA-256.
- `VERSION` moves to 0.0.55, the corral family's version: the site was
  never tagged, so it first ships at the family's version.

### Added

- `.github/dependabot.yml`, so the SHA-pinned actions get update PRs.
