---
sidebar_position: 2
---

# Adding New OSC Properties

This guide shows you how to add support for new QLab OSC properties without writing any Python code.

## Overview

All OSC properties are defined in `app/qlab_osc_config.json`. Adding a new property is as simple as adding a JSON entry.

## Step-by-Step Guide

### 1. Find the OSC Address

Consult the [QLab OSC Dictionary](https://qlab.app/docs/v5/scripting/osc-dictionary-v5/) to find:
- The OSC address (e.g., `/cue/selected/propertyName`)
- The expected data type (string, number, boolean)
- Valid values or ranges
- Which cue types support it

### 2. Determine Property Scope

Decide if the property is:
- **Global** - Available for all cue types → Add to `global_properties`
- **Cue-Specific** - Only for certain types → Add to `cue_type_properties`
- **Version-Specific** - Different in QLab 4 vs 5 → Use nested structure

### 3. Add to Configuration

#### Example 1: Global Property

Let's add support for the `armed` property:

```json
{
  "global_properties": {
    "armed": {
      "osc_address": "/cue/selected/armed",
      "type": "bool",
      "description": "Armed state of the cue"
    }
  }
}
```

**CSV Usage:**
```csv
Number,Type,Name,Armed
1,audio,Music Cue,true
```

#### Example 2: Cue-Specific Property

Add `level` for audio cues:

```json
{
  "cue_type_properties": {
    "audio": {
      "level": {
        "osc_address": "/cue/selected/level",
        "type": "float",
        "description": "Audio level/volume in dB"
      }
    }
  }
}
```

**CSV Usage:**
```csv
Number,Type,Name,Level
1,audio,Music Cue,-6.5
```

#### Example 3: Property with Validation

Add `continueMode` with valid range:

```json
{
  "global_properties": {
    "continuemode": {
      "osc_address": "/cue/selected/continueMode",
      "type": "int",
      "description": "Continue mode (0=No continue, 1=Auto-continue, 2=Auto-follow)",
      "valid_range": [0, 2]
    }
  }
}
```

Values outside 0-2 will be rejected.

#### Example 4: Property with Valid Values

Add `color` with specific options:

```json
{
  "global_properties": {
    "color": {
      "osc_address": "/cue/selected/colorName",
      "type": "string",
      "description": "Cue color",
      "valid_values": [
        "none", "berry", "blue", "crimson", "cyan",
        "forest", "gray", "green", "hot pink", "indigo"
      ]
    }
  }
}
```

Only listed colors will be accepted (case-insensitive).

#### Example 5: Conditional Property

Add a property that only applies when another field has a specific value:

```json
{
  "cue_type_properties": {
    "network": {
      "qlab4": {
        "command": {
          "osc_address": "/cue/selected/qlabCommand",
          "type": "int",
          "description": "QLab command (QLab 4)",
          "condition": {
            "field": "messagetype",
            "value": "1"
          }
        }
      }
    }
  }
}
```

The `command` property only sends if `messagetype` equals `"1"`.

### 4. Auto-Properties

Some properties automatically enable related settings. For example, setting a fade value should enable its checkbox.

```json
{
  "cue_type_properties": {
    "fade": {
      "fadeopacity": {
        "osc_address": "/cue/selected/opacity",
        "type": "int",
        "description": "Fade opacity (0-1)"
      },
      "doopacity": {
        "osc_address": "/cue/selected/doOpacity",
        "type": "bool",
        "description": "Enable opacity fading",
        "auto_value": true
      }
    }
  }
}
```

When user sets `Fade Opacity`, the system automatically sends `doOpacity: true`.

**Current auto-property logic** (`osc_config.py:154`):
```python
if property_name == 'fadeopacity' and prop_key == 'doopacity':
    auto_props.append((prop_key, prop_config['auto_value']))
```

To extend this, modify the `get_auto_properties()` method.

### 5. Version-Specific Properties

Network cues work differently in QLab 4 vs 5:

```json
{
  "cue_type_properties": {
    "network": {
      "qlab5": {
        "customstring": {
          "osc_address": "/cue/selected/customString",
          "type": "string",
          "description": "Custom string for OSC message (QLab 5)"
        }
      },
      "qlab4": {
        "rawstring": {
          "osc_address": "/cue/selected/rawString",
          "type": "string",
          "description": "Raw OSC string (QLab 4)"
        }
      }
    }
  }
}
```

The system automatically picks the right property based on the QLab version parameter.

## Property Configuration Options

### Required Fields

| Field | Type | Description |
|-------|------|-------------|
| `osc_address` | string | Full OSC path (e.g., `/cue/selected/name`) |
| `type` | string | Data type: `string`, `int`, `float`, `bool` |
| `description` | string | Human-readable description |

### Optional Fields

| Field | Type | Description |
|-------|------|-------------|
| `valid_range` | array | `[min, max]` for numeric validation |
| `valid_values` | array | List of allowed string values |
| `condition` | object | `{field, value}` - only send if condition met |
| `auto_value` | any | Value to auto-set when this property is triggered |

## CSV Column Name Mapping

CSV headers are automatically normalized:
- Converted to lowercase
- Spaces removed
- Matched against config keys

**Examples:**
- CSV: `"MIDI Device ID"` → Config: `"midideviceid"`
- CSV: `"Network Patch Number"` → Config: `"networkpatchnumber"`
- CSV: `"Pre Wait"` → Config: `"prewait"`

## Testing Your Property

1. **Add to config** - Edit `app/qlab_osc_config.json`
2. **Create test CSV** - Include your new column
3. **Run app** - `python3 application.py` (from project root)
4. **Upload CSV** - Test with an empty QLab workspace
5. **Verify in QLab** - Check that the property was set correctly

## Documentation Updates

After adding properties:

1. **Auto-generated reference** - Run to update docs:
   ```bash
   cd app
   python3 generate_column_docs.py > ../website/docs/reference/csv-columns.md
   ```

2. **Manual docs** - Update `website/docs/tutorial-basics/prepare-csv-file.md` with examples

## Common Mistakes

❌ **Wrong CSV header case**
```csv
midi device id  # Won't match
```
✅ **Use exact capitalization or any case (normalized)**
```csv
MIDI Device ID  # Matches "midideviceid"
```

❌ **Type mismatch**
```json
{"type": "int"}  // Config expects integer
```
```csv
Level,5.5  // CSV has float - will fail
```

❌ **Missing from valid_values**
```json
{"valid_values": ["red", "blue"]}
```
```csv
Color,green  // Rejected, not in list
```

## Advanced: Adding New Cue Types

To add support for a completely new cue type:

1. Add to `valid_cue_types` array:
```json
{
  "valid_cue_types": [
    "audio", "video", "midi", "yournewtype"
  ]
}
```

2. Add cue-specific properties:
```json
{
  "cue_type_properties": {
    "yournewtype": {
      "customproperty": {
        "osc_address": "/cue/selected/customProperty",
        "type": "string"
      }
    }
  }
}
```

3. Test with QLab to ensure it accepts the cue type via `/new yournewtype`

## Need Help?

- [QLab OSC Dictionary](https://qlab.app/docs/v5/scripting/osc-dictionary-v5/)
- [OSC Configuration Schema](./osc-config-schema.md)
- [Architecture Overview](./architecture.md)
- [GitHub Issues](https://github.com/fross123/csv_to_qlab/issues)
