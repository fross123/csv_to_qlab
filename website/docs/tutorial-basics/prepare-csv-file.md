---
sidebar_position: 2
---

# Prepare a CSV File

Some columns are required, some are optional.

:::warning
Some of these headers changed with version 2023.2! Please check your CSV headers.
:::

## Required columns
- Number
- Type
- Name

| Number | Type | Name |
| ------ | ------ | ------ |
| 12 | start | Cue 12 GO |

## Optional Columns
<ul>
    <li>Notes</li>
    <li>Follow</li>
    <ul>
        <li>0 - No Follow</li>
        <li>1 - Auto-Continue</li>
        <li>2 - Auto-Follow</li>
    </ul>
    <li>Color (<a href="https://qlab.app/docs/v4/scripting/osc-dictionary-v4/#cuecue_numbercolorname-string" target="_blank">Options</a>)</li>
    <li>Columns available for "midi" cue type:</li>
    <ul>
        <li>MIDI Q Number</li>
        <li>MIDI Device ID</li>
        <li>MIDI Message Type</li>
        <li>MIDI Control Number</li>
        <li>MIDI Control Value</li>
        <li>MIDI Patch Channel</li>
        <li>MIDI Patch Number</li>
        <li>MIDI Q List</li>
        <ul>
            <li>1 - MIDI Voice Message ("Musical MIDI")</li>
            <li>2 - MIDI Show Control Message (MSC)</li>
            <li>3 - MIDI SysEx Message</li>
        </ul>
        <li>MIDI Command Format (<a href="https://qlab.app/docs/v5/scripting/parameter-reference/#midi-show-control-command-format-types" target="_blank">Options</a>)</li>
        <li>MIDI Command (<a href="https://qlab.app/docs/v5/scripting/parameter-reference/#midi-show-control-commands" target="_blank">Options</a>)</li>
    </ul>
    <li>Columns available for "network" cue type:</li>
    <ul>
        <li>QLab 5</li>
        <ul>
            <li>Network Patch Number</li>
            <li>Network Patch Channel</li>
            <li>Custom String</li>
        </ul>
        <li>QLab 4</li>
        <ul>
            <li>Message Type (<a href="https://qlab.app/docs/v4/scripting/osc-dictionary-v4/#cuecue_numbermessagetype-number" target="_blank">Options</a>)</li>
            <li>OSC Cue Number (Only if using QLab Message Type)</li>
            <li>Command
                <ul>
                    <li>For QLab Messages (<a href="https://qlab.app/docs/v4/scripting/osc-dictionary-v4/#cuecue_numberqlabcommand-number" target="_blank">Options</a>)
                    </li>
                    <li>For an OSC message, you may now include a raw string in this column</li>
                </ul>
            </li>
        </ul>
    </ul>
</ul>

## Examples

- [Full Example Spreadsheet](https://github.com/fross123/csv_to_qlab/blob/master/static/example_file/example.csv)

- [Simple Example Spreadsheet](https://github.com/fross123/csv_to_qlab/blob/master/static/example_file/simple.csv)