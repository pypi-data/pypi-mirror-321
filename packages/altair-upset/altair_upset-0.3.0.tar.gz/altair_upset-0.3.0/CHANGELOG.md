# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- Type hints for better IDE support and code safety
- Theme support for customizing chart appearance
- Comprehensive documentation with examples
- GitHub Actions CI/CD pipeline
- Pre-commit hooks for code quality
- MIT License
- Proper package metadata and PyPI configuration
- Support for Python 3.8-3.11
- Interactive tooltips with set information
- Customizable chart dimensions and styling
- Proper error handling with descriptive messages

### Changed

- Improved API with better parameter organization
- Updated dependencies to latest stable versions
- Enhanced documentation with more examples
- Better code organization and modularity
- Stricter input validation

### Fixed

- Input validation for data types and values
- Error handling for invalid parameters
- Documentation formatting and examples

## [0.2.0] - 2024-01-18

### Changed

- Updated to support Altair 5.0.0 and Vega-Lite 5
- Replaced `alt.selection_multi()` with `alt.selection_point()` for legend selection
- Removed width/height properties from VConcatChart level
- Set width/height properties on individual chart components for proper validation
- Updated PNG snapshot generation to use Altair's built-in saving capabilities

### Added

- Comprehensive documentation in `docs.md`
- Detailed API reference with parameter descriptions
- Interactive features documentation
- Usage examples in documentation

### Fixed

- Fixed deprecation warning for selection_multi
- Fixed PNG snapshot generation and tracking
- Resolved validation errors for chart sizing in Altair 5

## [0.1.1] - 2024-01-18

### Changed

- Split the original function into separate files for division of concerns

## [0.1.0] - 2024-01-18

### Added

- Initial implementation of UpSetAltair
- Basic set visualization functionality
- Interactive features (hover highlighting, legend filtering)
- Support for customization (colors, sizes, sorting)
