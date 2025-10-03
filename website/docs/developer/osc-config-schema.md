---
sidebar_position: 3
---

# OSC Configuration Schema

Complete reference for the `qlab_osc_config.json` file structure.

## File Location

```
app/qlab_osc_config.json
```

This file is bundled with the application via PyInstaller (`application.spec:12`).

## Root Structure

```json
{
  "global_properties": { /* ... */ },
  "cue_type_properties": { /* ... */ },
  "valid_cue_types": [ /* ... */ ]
}
```

## Global Properties

Properties available for **all cue types**.

### Schema

```typescript
{
  "global_properties": {
    "<property_key>": {
      "osc_address": string,      // Required: OSC path
      "type": string,              // Required: "string" | "int" | "float" | "bool"
      "description": string,       // Required: Human-readable description
      "valid_range"?: [number, number],  // Optional: [min, max] for numbers
      "valid_values"?: string[]    // Optional: Allowed values for strings
    }
  }
}
```

### Example

```json
{
  "global_properties": {
    "number": {
      "osc_address": "/cue/selected/number",
      "type": "string",
      "description": "Cue number"
    },
    "continuemode": {
      "osc_address": "/cue/selected/continueMode",
      "type": "int",
      "description": "Continue mode (0=No continue, 1=Auto-continue, 2=Auto-follow)",
      "valid_range": [0, 2]
    },
    "color": {
      "osc_address": "/cue/selected/colorName",
      "type": "string",
      "description": "Cue color",
      "valid_values": ["none", "berry", "blue", "crimson", "cyan", "forest"]
    }
  }
}
```

## Cue Type Properties

Properties specific to certain cue types.

### Basic Cue Type Schema

```typescript
{
  "cue_type_properties": {
    "<cue_type>": {
      "<property_key>": {
        "osc_address": string,
        "type": string,
        "description": string,
        "valid_range"?: [number, number],
        "valid_values"?: string[],
        "auto_value"?: any,         // Auto-set value
        "condition"?: {             // Conditional sending
          "field": string,
          "value": string
        }
      }
    }
  }
}
```

### Example: Audio Cues

```json
{
  "cue_type_properties": {
    "audio": {
      "level": {
        "osc_address": "/cue/selected/level",
        "type": "float",
        "description": "Audio level/volume in dB"
      },
      "rate": {
        "osc_address": "/cue/selected/rate",
        "type": "float",
        "description": "Playback rate (0.03 to 33.0)"
      },
      "pitch": {
        "osc_address": "/cue/selected/pitch",
        "type": "bool",
        "description": "Preserve pitch when rate changes"
      }
    }
  }
}
```

### Version-Specific Properties

For cue types that differ between QLab versions (e.g., network cues):

```typescript
{
  "cue_type_properties": {
    "<cue_type>": {
      "qlab5": {
        "<property_key>": { /* ... */ }
      },
      "qlab4": {
        "<property_key>": { /* ... */ }
      }
    }
  }
}
```

### Example: Network Cues (Version-Specific)

```json
{
  "cue_type_properties": {
    "network": {
      "qlab5": {
        "customstring": {
          "osc_address": "/cue/selected/customString",
          "type": "string",
          "description": "Custom string for OSC message or plain text (QLab 5)"
        },
        "networkpatchnumber": {
          "osc_address": "/cue/selected/networkPatchNumber",
          "type": "int",
          "description": "Network patch number (QLab 5)"
        }
      },
      "qlab4": {
        "messagetype": {
          "osc_address": "/cue/selected/messageType",
          "type": "int",
          "description": "Message type (QLab 4)"
        },
        "rawstring": {
          "osc_address": "/cue/selected/rawString",
          "type": "string",
          "description": "Raw OSC string (QLab 4)",
          "condition": {
            "field": "messagetype",
            "value": "2"
          }
        }
      }
    }
  }
}
```

## Auto-Properties

Properties with `auto_value` are automatically set when a related property is used.

### Schema

```typescript
{
  "<property_key>": {
    "osc_address": string,
    "type": string,
    "description": string,
    "auto_value": any  // Value to auto-send
  }
}
```

### Example: Fade Opacity Auto-Enable

```json
{
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
```

**Behavior:**
- User sets: `Fade Opacity = 0.5`
- System auto-sends: `doOpacity = true`

:::note Current Implementation
Auto-property logic is currently hardcoded for `fadeopacity → doopacity` in `osc_config.py:154`. To extend this feature, modify the `get_auto_properties()` method.
:::

## Conditional Properties

Properties with `condition` are only sent if another field has a specific value.

### Schema

```typescript
{
  "<property_key>": {
    "osc_address": string,
    "type": string,
    "description": string,
    "condition": {
      "field": string,   // CSV column to check
      "value": string    // Required value
    }
  }
}
```

### Example: Conditional QLab Command

```json
{
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
```

**Behavior:**
- Only sends `command` if CSV has `messagetype = 1`
- If condition not met, property is skipped

## Valid Cue Types

Array of cue type strings accepted by QLab's `/new` command.

### Schema

```typescript
{
  "valid_cue_types": string[]
}
```

### Example

```json
{
  "valid_cue_types": [
    "audio",
    "mic",
    "video",
    "camera",
    "text",
    "light",
    "fade",
    "network",
    "midi",
    "midi file",
    "timecode",
    "group",
    "start",
    "stop",
    "pause",
    "load",
    "reset",
    "devamp",
    "goto",
    "target",
    "arm",
    "disarm",
    "wait",
    "memo",
    "script",
    "list",
    "cuelist",
    "cue list",
    "cart",
    "cuecart",
    "cue cart"
  ]
}
```

## Property Types

### String (`"type": "string"`)
- Sent as OSC string argument
- No conversion applied
- Example: cue name, notes, file paths

### Integer (`"type": "int"`)
- Converted to Python `int`
- Sent as OSC integer argument
- Example: continue mode (0-2), patch numbers

### Float (`"type": "float"`)
- Converted to Python `float`
- Sent as OSC float argument
- Example: level (dB), rate (0.03-33.0)

### Boolean (`"type": "bool"`)
- Accepts: `"true"`, `"1"`, `"yes"`, `"on"`, `true`
- Converts to Python `bool`
- Sent as OSC boolean argument
- Example: armed, flagged, auto-load

## Validation Rules

### `valid_range` (Numbers Only)

```json
{
  "patch": {
    "type": "int",
    "valid_range": [1, 16]
  }
}
```

- Values < 1 or > 16 are **rejected**
- Property not sent if validation fails

### `valid_values` (Strings Only)

```json
{
  "color": {
    "type": "string",
    "valid_values": ["red", "blue", "green"]
  }
}
```

- Case-insensitive matching
- Values not in list are **rejected**
- Property not sent if validation fails

## CSV Column Name Resolution

CSV headers are normalized before matching:

1. Convert to lowercase
2. Remove all spaces
3. Match against config keys

**Examples:**

| CSV Header | Normalized | Config Key |
|------------|-----------|------------|
| `Number` | `number` | `number` ✓ |
| `MIDI Device ID` | `midideviceid` | `midideviceid` ✓ |
| `Network Patch Number` | `networkpatchnumber` | `networkpatchnumber` ✓ |
| `Pre Wait` | `prewait` | `prewait` ✓ |
| `Continue Mode` | `continuemode` | `continuemode` ✓ |
| `Follow` | `follow` | `follow` ✓ |

## Configuration Loading

`osc_config.py` loads the configuration as a singleton:

```python
from osc_config import get_osc_config

config = get_osc_config()  # Loads JSON once

# Check cue type
if config.check_cue_type('audio'):
    # Valid cue type
    pass

# Build OSC message
msg = config.build_osc_message(
    property_name='level',
    value='-6.5',
    cue_type='audio',
    qlab_version=5
)

# Get auto-properties
auto_props = config.get_auto_properties('fadeopacity', 'fade')
# Returns: [('doopacity', True)]
```

## Full Example Configuration

```json
{
  "global_properties": {
    "number": {
      "osc_address": "/cue/selected/number",
      "type": "string",
      "description": "Cue number"
    },
    "name": {
      "osc_address": "/cue/selected/name",
      "type": "string",
      "description": "Cue name"
    },
    "continuemode": {
      "osc_address": "/cue/selected/continueMode",
      "type": "int",
      "description": "Continue mode",
      "valid_range": [0, 2]
    }
  },
  "cue_type_properties": {
    "audio": {
      "level": {
        "osc_address": "/cue/selected/level",
        "type": "float",
        "description": "Audio level/volume in dB"
      }
    },
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
    },
    "network": {
      "qlab5": {
        "customstring": {
          "osc_address": "/cue/selected/customString",
          "type": "string",
          "description": "Custom string for OSC message (QLab 5)"
        }
      }
    }
  },
  "valid_cue_types": [
    "audio", "video", "fade", "network", "midi"
  ]
}
```

## See Also

- [Adding New Properties Guide](./adding-properties.md)
- [Architecture Overview](./architecture.md)
- [QLab OSC Dictionary](https://qlab.app/docs/v5/scripting/osc-dictionary-v5/)
