# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Fixed

- Fixed crash in Python 3.8 (#12)

## [v1.0.0] - 2024-04-06

### Added

- Added dependabot
- Added Action for publishing to PyPi
- Added CHANGELOG.md - Retroactively updated previous version releases

### Changed

- Refactored comments to align with more recent coding practices
- Refactored structure of method definitions to align with more recent coding practices
- Refactored the logic for converting tuples and non-tuples to its own method called `_convert_keys_to_list`. this can be useful for inherited classes that may want to use this function. (#9)

### Fixed

- Fixed an empty config file being created on the file system when `file_must_exist = False` is used when instantiating the `Config` class. (#8)

## [v0.0.4] - 2023-06-15

### Fixed

- Fixed excessive print statement (#1)

## [v0.0.3] - 2023-03-13

### Added

- Added tests

### Changed

- Updated documentation

## [v0.0.2] - 2023-03-08

Initial release