---
sidebar_position: 2
---

# Prepare a CSV File

## Examples
- [Full Example Spreadsheet](https://github.com/fross123/csv_to_qlab/blob/main/app/static/example_file/example.csv)

- [Simple Example Spreadsheet](https://github.com/fross123/csv_to_qlab/blob/main/app/static/example_file/simple.csv)


## Required columns
- Number
- Type
- Name

| Number | Type | Name |
| ------ | ------ | ------ |
| 12 | start | Cue 12 GO |

----

## Optional Columns

#### Notes
Anything you would like to go in the "Notes" area of the cue.

#### Follow
:::tip
0, 1, 2 are the only options and the data must be a single number.
:::
- 0 - No Follow
- 1 - Auto-Continue
- 2 - Auto-Follow

#### Color
The color of the cue. See [QLab's Color Options](https://qlab.app/docs/v4/scripting/osc-dictionary-v4/#cuecue_numbercolorname-string)

#### Target
The cue's target. The cue being targeted must be above the cue being created.

#### File Target
The location of assets for QLab to retrieve.

Available types:
- Full paths, e.g. /Volumes/MyDisk/path/to/some/file.wav
- Paths beginning with a tilde, e.g. ~/path/to some/file.mov
- Relative paths, e.g. this/is/a/relative/path.mid
- Paths beginning with a tilde (~) will be expanded; the tilde signifies “relative to the user’s home directory”.

----

## Cue types with additional options

### Group Cues
#### Group Mode
:::info
Pre-Release - "Group Mode" is only available when run from source code.
:::

[Options](https://qlab.app/docs/v5/scripting/osc-dictionary-v5/#cuecue_numbermode-number):
- 0 - List
- 1 - Start first and enter
- 2 - Start first
- 3 - Timeline
- 4 - Start random
- 6 - Playlist
:::tip
This is not a typo, "6" is for Playlist type.
:::

----

### Text Cues
#### Text
The text to enter into the text cue.

----

### Fade Cues
#### Stop Target When Done
This accepts either "true" or "false" to check the box for "Stop Target When Done"

#### Fade Opacity
Per QLab Docs, only 0 or 1 is accepted.
:::tip
Also activates the checkbox next to opacity
:::

----

### Video Cues
#### Stage Number
The stage number in order of the list in the "video outputs" setting

:::tip
Stages are in QLab 5 only.
:::

----

### MIDI Cues

#### MIDI Message Type
- 1 - MIDI Voice Message ("Musical MIDI")
- 2 - MIDI Show Control Message (MSC)
- 3 - MIDI SysEx Message

#### MIDI Q Number
The number of the cue. Specific to MSC cue types.

#### MIDI Q List
The Cue List for the MSC cue.

#### MIDI Device ID
#### MIDI Control Number
#### MIDI Control Value
#### MIDI Patch Name
The Name of the MIDI Patch

#### MIDI Patch Number
The patch of the MIDI cue in order by the workspace settings. Index 1 means the first patch in the patch list in Workspace Settings.

#### MIDI Raw String
:::info
Pre-Release - "MIDI Raw String" is currently only available when run from source code.
:::
For Midi SysEx Messages

#### MIDI Command Format
[Reference QLab Docs](https://qlab.app/docs/v5/scripting/parameter-reference/#midi-show-control-command-format-types)

#### MIDI Command
[Reference QLab Docs](https://qlab.app/docs/v5/scripting/parameter-reference/#midi-show-control-commands)

----

### Network Cues
The way network cues work is slightly different in QLab 4 vs QLab 5

#### QLab 5
##### Network Patch Number
The number of the network patch.

##### Network Patch Name
The Name of the network patch.

##### Custom String
The best way to facilitate the vast amount of commands available in QLab 5 was to use custom string. You should be able to craft desired strings easily using common spreadsheet formulas and tools.

#### QLab 4
There are no plans to remove these features, but we will post here on this site if/when support for QLab 4 ends.

##### Message Type
Reference [QLab Docs](https://qlab.app/docs/v4/scripting/osc-dictionary-v4/#cuecue_numbermessagetype-number)

##### OSC Cue Number
Only if using QLab Message Type

##### Command
For QLab Messages, review the [QLab Docs](https://qlab.app/docs/v4/scripting/osc-dictionary-v4/#cuecue_numberqlabcommand-number)

For OSC Messages, you may now include a raw string in the column.
