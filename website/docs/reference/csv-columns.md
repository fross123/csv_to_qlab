---
sidebar_position: 1
---

# CSV Column Reference

This document lists all available CSV columns for creating QLab cues.

:::info
This documentation is automatically generated from the OSC configuration file.
:::

## Required Columns

All CSV files **must** include these three columns:

| Column | Description | Example |
|--------|-------------|---------|
| Number | Cue number | `1`, `LX 12`, `Q100` |
| Type | Cue type | `audio`, `video`, `midi`, `network` |
| Name | Cue name | `Cue 1 GO`, `Main Lights Up` |

## Global Properties (All Cue Types)

These columns can be used with any cue type:

| CSV Column Header | Description | Type | Valid Values |
|------------------|-------------|------|--------------|
| Armed | Armed state | bool | `true`, `false` |
| Auto Load | Auto-load state | bool | `true`, `false` |
| Color | Cue color | string | none, berry, blue, crimson, cyan, forest, gray, green, hot pink, indigo, lavender, magenta, midnight, olive, orange, peach, plum, purple, red, sky blue, yellow |
| Continue Mode | Continue mode | int | 0=No continue, 1=Auto-continue, 2=Auto-follow |
| Duration | Cue duration | int | Time in seconds |
| File Target | File target path | string | Full path, ~/path, or relative path |
| Flagged | Flagged state | bool | `true`, `false` |
| Follow | Follow mode (alias for Continue Mode) | int | 0-2 |
| Group Mode | Group mode | int | 0=List, 1=Start first and enter, 2=Start first, 3=Timeline, 4=Start random, 5=Cart, 6=Playlist |
| Name | Cue name | string | Any text |
| Notes | Cue notes | string | Any text |
| Number | Cue number | string | Any text/number |
| Post Wait | Post-wait time | int | Time in seconds |
| Pre Wait | Pre-wait time | int | Time in seconds |
| Target | Target cue number | string | Must reference existing cue |

## Cue-Type Specific Properties

### Audio Cues

| CSV Column Header | Description | Type | Valid Values |
|------------------|-------------|------|--------------|
| End Time | End time in seconds | float | Decimal number |
| Gang | Level gang/group name | string | Gang name |
| Infinite Loop | Infinite loop state | bool | `true`, `false` |
| Level | Audio level/volume in dB | float | Typically -60 to 12 |
| Patch | Audio patch number | int | 1-16 |
| Pitch | Preserve pitch when rate changes | bool | `true`, `false` |
| Play Count | Number of times to play | int | Positive integer |
| Rate | Playback rate | float | 0.03 to 33.0 |
| Start Time | Start time in seconds | float | Decimal number |

### Fade Cues

| CSV Column Header | Description | Type | Valid Values |
|------------------|-------------|------|--------------|
| Do Fade | Enable general fading | bool | `true`, `false` |
| Fade And Stop Others | Fade and stop mode | int | 0=None, 1=Peers, 2=List/cart, 3=All |
| Fade And Stop Others Time | Fade and stop others time | float | Time in seconds |
| Fade Opacity | Fade opacity | int | 0-1 |
| Stop Target When Done | Stop target when fade is done | bool | `true`, `false` |

:::tip Auto-Properties
When you set `Fade Opacity`, the `Do Opacity` checkbox is automatically enabled.
:::

### Mic Cues

| CSV Column Header | Description | Type | Valid Values |
|------------------|-------------|------|--------------|
| Level | Audio level/volume in dB | float | Typically -60 to 12 |
| Patch | Audio patch number | int | 1-16 |

### MIDI Cues

| CSV Column Header | Description | Type | Valid Values |
|------------------|-------------|------|--------------|
| MIDI Command | MIDI command | int | 0-127 |
| MIDI Command Format | MIDI command format | int | 0-127 |
| MIDI Control Number | MIDI control number | int | 0-16383 |
| MIDI Control Value | MIDI control value | int | 0-16383 |
| MIDI Device ID | MIDI device ID | int | 0-127 |
| MIDI Message Type | MIDI message type | int | 1=Voice, 2=MSC, 3=SysEx |
| MIDI Patch Name | MIDI patch name | string | Patch name from workspace |
| MIDI Patch Number | MIDI patch number | int | Index in workspace settings |
| MIDI Q List | MIDI Q list | string | MSC cue list number |
| MIDI Q Number | MIDI Q number | string | MSC cue number |
| MIDI Raw String | MIDI SysEx raw string | string | Hex string (no F0/F7) |
| MIDI Status | MIDI status | int | 0=Note Off, 1=Note On, 2=Key Pressure, 3=Control Change, 4=Program Change, 5=Channel Pressure, 6=Pitch Bend |

:::info MIDI Resources
See [QLab MIDI Reference](https://qlab.app/docs/v5/scripting/parameter-reference/#midi-show-control-commands) for command details.
:::

### Network Cues

Network cues work differently in QLab 4 vs QLab 5. Choose the columns based on your QLab version.

#### QLab 5 Properties

| CSV Column Header | Description | Type |
|------------------|-------------|------|
| Custom String | Custom string for OSC message or plain text | string |
| Network Patch Name | Network patch name | string |
| Network Patch Number | Network patch number | int |

:::tip QLab 5 Custom Strings
Use spreadsheet formulas to craft complex OSC messages in the Custom String column.
:::

#### QLab 4 Properties

| CSV Column Header | Description | Type |
|------------------|-------------|------|
| Command | QLab command | int |
| Message Type | Message type | int |
| OSC Cue Number | OSC cue number | string |
| Raw String | Raw OSC string | string |

:::note
QLab 4 support is maintained but may be deprecated in future releases.
:::

### Text Cues

| CSV Column Header | Description | Type | Valid Values |
|------------------|-------------|------|--------------|
| Text | Text content for text cue | string | Any text |

### Video Cues

| CSV Column Header | Description | Type | Valid Values |
|------------------|-------------|------|--------------|
| End Time | End time in seconds | float | Decimal number |
| Infinite Loop | Infinite loop state | bool | `true`, `false` |
| Level | Video audio level/volume in dB | float | Typically -60 to 12 |
| Patch | Video patch number | int | 1-16 |
| Play Count | Number of times to play | int | Positive integer |
| Rate | Playback rate | float | 0.03 to 33.0 |
| Stage Number | Video stage number | int | Stage index from workspace settings |
| Start Time | Start time in seconds | float | Decimal number |

:::tip Video Stages
Stages are only available in QLab 5.
:::

## Valid Cue Types

Use these values in the `Type` column:

- `audio`
- `mic`
- `video`
- `camera`
- `text`
- `light`
- `fade`
- `network`
- `midi`
- `midi file`
- `timecode`
- `group`
- `start`
- `stop`
- `pause`
- `load`
- `reset`
- `devamp`
- `goto`
- `target`
- `arm`
- `disarm`
- `wait`
- `memo`
- `script`
- `list`, `cuelist`, `cue list`
- `cart`, `cuecart`, `cue cart`

## See Also

- [Prepare CSV File Tutorial](../tutorial-basics/prepare-csv-file.md)
- [OSC Configuration Schema](../developer/osc-config-schema.md)
