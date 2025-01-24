# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/en/1.0.0/)
and this project adheres to [Semantic Versioning](http://semver.org/spec/v2.0.0.html).

## [Unreleased]

## [2.0.0] - 2025-01-16
### Added
- Declare compatibility with `python3.11` & `python3.12` in package's metadata.

### Changed
- Raise `RuntimeError` instead of `Exception` when libc's `dlinfo` function fails.
- Update maintainer and repository's URL in package's metadata.

### Removed
- Compatibility with `python3.5`, `python3.6`, `python3.7` & `python3.8`
  (reached end-of-life)

## [1.2.1] - 2021-04-21 
### Fixed
- Update package metadata: maintainer, repo url, python version classifiers

## [1.2.0] - 2019-11-05
### Added
- Support for Mac OS X

## [1.1.0] - 2019-09-03
### Added
- Prepare push to pypi.org
  - Converted readme from markdown to ReSructuredText format
  - Added module metadata (author, maintainer, url)

## [1.0.0] - 2019-09-03
### Added
- Class `DLInfo`
  - Property `path` returns absolute path to dynamically loaded library

[Unreleased]: https://github.com/cloudflightio/python-dlinfo/compare/v2.0.0...HEAD
[2.0.0]: https://github.com/cloudflightio/python-dlinfo/compare/v1.2.1...v2.0.0
[1.2.1]: https://github.com/cloudflightio/python-dlinfo/compare/v1.2.0...v1.2.1
[1.2.0]: https://github.com/cloudflightio/python-dlinfo/compare/v1.1.0...v1.2.0
[1.1.0]: https://github.com/cloudflightio/python-dlinfo/compare/v1.0.0...v1.1.0
[1.0.0]: https://github.com/cloudflightio/python-dlinfo/releases/tag/v1.0.0
