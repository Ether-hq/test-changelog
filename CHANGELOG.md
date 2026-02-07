# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## 2026-02-07

### Added
- API documentation with OAuth2 authentication guide (#11)
- OAuth2 authentication service with support for Google and GitHub login providers (#9)

### Fixed
- Memory leak in background job processor by implementing automatic cleanup of completed tasks (#10)
