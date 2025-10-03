---
sidebar_position: 1
---

# Architecture Overview

CSV to QLab is built with a configuration-driven architecture that makes it easy to add support for new QLab OSC properties without modifying code.

## System Architecture

```
CSV File Upload
      ↓
CSV Parser (csv_parser.py)
      ↓
OSC Config Loader (osc_config.py)
      ↓
OSC Message Builder
      ↓
UDP Client (python-osc) → QLab (port 53000)
      ↓
OSC Server (port 53001) ← QLab Replies
      ↓
Error/Success Handler
      ↓
User Feedback (Flask UI)
```

## Core Components

### 1. Flask Application (`application.py`)
- Web server providing the UI
- Runs inside a PyWebView native window
- Handles file uploads and form submission
- Routes: `/` (upload), `/success` (results)

### 2. CSV Parser (`csv_parser.py`)
The main processing pipeline:

1. **Parse CSV** - Reads CSV file into list of dictionaries
2. **Normalize headers** - Converts to lowercase, removes spaces
3. **Validate cue types** - Checks against valid types in config
4. **Build OSC bundles** - For each cue:
   - Create `/new {cue_type}` message
   - Build property messages using config
   - Handle auto-properties (e.g., fadeopacity → doopacity)
5. **Send to QLab** - UDP transmission with async reply handling

### 3. OSC Configuration System (`osc_config.py`)

**Configuration-Driven Design:**
- All OSC properties defined in `qlab_osc_config.json`
- No hardcoded OSC addresses in business logic
- Easy to add new properties or cue types

**Key Methods:**
```python
get_property_config(property_name, cue_type, qlab_version)
# Returns config for a property

build_osc_message(property_name, value, cue_type, qlab_version)
# Builds OSC message from config

get_auto_properties(property_name, cue_type)
# Returns properties to auto-enable
```

### 4. OSC Server (`osc_server.py`)
- Async UDP server listening on port 53001
- Receives QLab reply messages
- Parses JSON responses for status
- Routes to error/success handlers

### 5. PyWebView Desktop Wrapper
- Creates native macOS app window
- Frameless design (300x465px)
- Bundles with PyInstaller for distribution

## Data Flow Example

**CSV Input:**
```csv
Number,Type,Name,Follow,Color
1,audio,Main Music,2,blue
```

**Processing:**
1. Parse: `{'number': '1', 'type': 'audio', 'name': 'Main Music', 'follow': '2', 'color': 'blue'}`
2. Build Bundle:
   - `/new` → `"audio"`
   - `/cue/selected/number` → `"1"`
   - `/cue/selected/name` → `"Main Music"`
   - `/cue/selected/continueMode` → `2` (from config: follow → continueMode)
   - `/cue/selected/colorName` → `"blue"`
3. Send bundle via UDP
4. Receive reply: `{"status": "ok", "workspace_id": "..."}`
5. Display success

## Configuration Schema

### Global Properties
Available for all cue types:
```json
{
  "property_name": {
    "osc_address": "/cue/selected/...",
    "type": "int|float|bool|string",
    "description": "Human-readable description",
    "valid_range": [min, max],  // optional
    "valid_values": ["...", "..."]  // optional
  }
}
```

### Cue-Type Properties
Specific to certain cue types:
```json
{
  "cue_type_properties": {
    "audio": {
      "level": {
        "osc_address": "/cue/selected/level",
        "type": "float"
      }
    }
  }
}
```

### Version-Specific Properties
Handle QLab 4 vs 5 differences:
```json
{
  "network": {
    "qlab5": { /* v5 properties */ },
    "qlab4": { /* v4 properties */ }
  }
}
```

## Auto-Property System

Some properties automatically enable related settings. For example:

**User sets:** `Fade Opacity = 0.5`

**System automatically adds:**
- `Do Opacity = true` (enables the opacity checkbox)

This is configured with `"auto_value": true` in the JSON config.

## Validation

The system validates:
1. **Cue types** - Must be in `valid_cue_types` array
2. **Property ranges** - Checked against `valid_range` if specified
3. **Property values** - Checked against `valid_values` if specified
4. **Conditional properties** - Only set if condition is met

Invalid values are silently skipped (message not sent).

## Error Handling

**Global Error/Success Tracking:**
- `error_success_handler.py` maintains global lists
- Each OSC reply is categorized as success or error
- Displayed to user after all cues processed

**OSC Reply Format:**
```json
{
  "workspace_id": "ABC123",
  "address": "/new",
  "status": "ok"  // or error message
}
```

## Adding New Features

To add support for a new QLab property:

1. **No code changes needed!**
2. Add property to `app/qlab_osc_config.json`
3. Documentation auto-generated from config

See [Adding Properties Guide](./adding-properties.md) for details.

## Technology Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| Backend | Python 3.9+ | Core logic |
| Web Framework | Flask 3.0.3 | HTTP server |
| Desktop UI | PyWebView 5.1 | Native window |
| OSC Protocol | python-osc 1.8.3 | QLab communication |
| Build Tool | PyInstaller | macOS app bundling |
| Docs | Docusaurus | Documentation site |

## QLab Communication

**Ports:**
- `53000` - Send OSC messages to QLab (UDP)
- `53001` - Receive QLab replies (UDP)
- `53535` - QLab's plain text OSC listener (not used)

**Connection Flow:**
1. Send `/connect {passcode}` if provided
2. Send `/alwaysReply 1` to enable replies (implicit)
3. Send cue creation bundles
4. Receive status replies
5. Close connection (auto-timeout after 61s on UDP)

## Design Principles

1. **Configuration over Code** - Properties defined in JSON, not Python
2. **Fail Gracefully** - Invalid properties skipped, processing continues
3. **Minimal Dependencies** - Small footprint, quick startup
4. **Type Safety** - Validation at config level
5. **Version Agnostic** - Same codebase supports QLab 4 & 5
