---
sidebar_position: 2
---

# Prepare a CSV File

Some columns are required, some are optional.

## Required columns
- Number
- Type
- Name

| Number | Type | Name |
| ------ | ------ | ------ |
| 12 | start | Cue 12 GO |

## Optional Columns
<ul>
    <li>Page (Will be added to notes)</li>
    <li>Notes</li>
    <li>Follow (<a href="https://qlab.app/docs/v4/scripting/osc-dictionary-v4/#cuecue_numbercontinuemode-number" target="_blank">Options</a>)</li>
    <li>Color (<a href="https://qlab.app/docs/v4/scripting/osc-dictionary-v4/#cuecue_numbercolorname-string" target="_blank">Options</a>)</li>
    <li>Columns available for "midi" cue type:</li>
    <ul>
        <li>Midi Cue Number</li>
        <li>Device ID</li>
        <li>Message Type (<a href="https://qlab.app/docs/v4/scripting/osc-dictionary-v4/#cuecue_numbermessagetype-number-1" target="_blank">Options</a>)</li>
        <li>Command Format (<a href="https://qlab.app/docs/v4/scripting/osc-dictionary-v4/#cuecue_numbercommandformat-number" target="_blank">Options</a>)</li>
        <li>Command (<a href="https://qlab.app/docs/v4/scripting/osc-dictionary-v4/#cuecue_numbercommand-number" target="_blank">Options</a>)</li>
    </ul>
    <li>Columns available for "network" cue type:</li>
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

## Examples

- [Full Example Spreadsheet](https://github.com/fross123/csv_to_qlab/blob/master/static/example_file/example.csv)

- [Simple Example Spreadsheet](https://github.com/fross123/csv_to_qlab/blob/master/static/example_file/simple.csv)