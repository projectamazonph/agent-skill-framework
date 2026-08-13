# Chromium Browser Plugin

**Version:** 0.1.1  
**License:** MIT  
**Source:** https://github.com/nicholasgriffintn/opencode-chromium-browser-plugin (approx.)

## What It Does

OpenCode browser automation for Chromium-based browsers using a readable extension and native messaging host. Provides the `chromium-browser` skill for controlling Chrome/Chromium.

## Installation

1. Install the Chrome extension from the `extension/` directory
2. Install the native messaging host
3. Add to your agent config

## Provided Skills
- `chromium-browser` — Control Chrome/Chromium through the OpenCode Browser extension

## Architecture
- Chrome extension provides accessibility-tree snapshots
- Native host bridges extension ↔ agent communication
- Supports full page automation: navigation, forms, screenshots, data extraction
