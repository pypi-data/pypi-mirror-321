# QuickDrop CLI

A command-line interface tool for deploying HTML content with automatic resource bundling. QuickDrop CLI automatically bundles your CSS, JavaScript, and image resources into a single, deployable HTML file.

## Features

- **Resource Bundling**: Automatically bundles CSS and JavaScript files
- **Asset Embedding**: Converts image references in CSS to data URIs
- **Version Control**: Track and manage different versions of your deployments
- **Simple Authentication**: Easy login system with token management
- **Rollback Support**: Revert to previous versions when needed

## Installation

```bash
pip install quickdrop-cli
```

# AI Helper code

```bash
find . -type f ! -path '*/\.*' -print0 | while IFS= read -r -d '' f; do echo "=== $f ==="; cat "$f"; echo -e "\n"; done | pbcopy
```