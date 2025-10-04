#!/usr/bin/env python3
"""
Generate CSV column documentation from qlab_osc_config.json

This script reads the OSC configuration and outputs a markdown table
showing all available CSV columns for each cue type.
"""

import json
from helper import resource_path


def format_header_name(config_key):
    """Convert config key back to human-readable header name"""
    # Handle special cases and known prefixes
    special_mappings = {
        'midi': 'MIDI',
        'osc': 'OSC',
        'qlab': 'QLab',
        'id': 'ID',
        'prewait': 'Pre Wait',
        'postwait': 'Post Wait',
        'filetarget': 'File Target',
        'groupmode': 'Group Mode',
        'continuemode': 'Continue Mode',
        'autoload': 'Auto Load',
        'stoptargetwhendone': 'Stop Target When Done',
        'fadeopacity': 'Fade Opacity',
        'stagenumber': 'Stage Number',
        'infiniteloop': 'Infinite Loop',
        'playcount': 'Play Count',
        'starttime': 'Start Time',
        'endtime': 'End Time',
        'dovolume': 'Do Volume',
        'dofade': 'Do Fade',
        'doopacity': 'Do Opacity',
        'fadeandstopothers': 'Fade And Stop Others',
        'fadeandstopotherstime': 'Fade And Stop Others Time',
        'customstring': 'Custom String',
        'networkpatchname': 'Network Patch Name',
        'networkpatchnumber': 'Network Patch Number',
        'osccuenumber': 'OSC Cue Number',
        'rawstring': 'Raw String',
        # MIDI specific
        'midicommand': 'MIDI Command',
        'midicommandformat': 'MIDI Command Format',
        'midicontrolnumber': 'MIDI Control Number',
        'midicontrolvalue': 'MIDI Control Value',
        'midideviceid': 'MIDI Device ID',
        'midimessagetype': 'MIDI Message Type',
        'midipatchname': 'MIDI Patch Name',
        'midipatchnumber': 'MIDI Patch Number',
        'midiqlist': 'MIDI Q List',
        'midiqnumber': 'MIDI Q Number',
        'midirawstring': 'MIDI Raw String',
        'midistatus': 'MIDI Status'
    }

    # Check for exact match first
    if config_key in special_mappings:
        return special_mappings[config_key]

    # Handle MIDI prefixed properties
    if config_key.startswith('midi'):
        rest = config_key[4:]  # Remove 'midi' prefix
        rest_formatted = format_header_name(rest) if rest else ''
        return f"MIDI {rest_formatted}".strip()

    # Default: capitalize each word
    return " ".join(word.capitalize() for word in config_key.split())


def load_config():
    """Load the OSC configuration"""
    config_path = resource_path("qlab_osc_config.json")
    with open(config_path, 'r') as f:
        return json.load(f)


def generate_docs():
    """Generate documentation for all CSV columns"""
    config = load_config()

    print("# CSV Column Reference\n")
    print("This document lists all available CSV columns for creating QLab cues.\n")
    print("*This documentation is automatically generated from the OSC configuration.*\n")

    # Global Properties
    print("## Global Properties (All Cue Types)\n")
    print("These columns can be used with any cue type:\n")
    print("| CSV Column Header | Description | Type | Valid Values |")
    print("|------------------|-------------|------|--------------|")

    for key, prop in sorted(config['global_properties'].items()):
        header = format_header_name(key)
        description = prop.get('description', '')
        prop_type = prop.get('type', 'string')

        valid_values = ""
        if 'valid_range' in prop:
            valid_values = f"{prop['valid_range'][0]}-{prop['valid_range'][1]}"
        elif 'valid_values' in prop:
            # Show first few values
            values = prop['valid_values'][:5]
            valid_values = ", ".join(values)
            if len(prop['valid_values']) > 5:
                valid_values += "..."

        print(f"| {header} | {description} | {prop_type} | {valid_values} |")

    # Cue-Type Specific Properties
    print("\n## Cue-Type Specific Properties\n")

    for cue_type, properties in sorted(config['cue_type_properties'].items()):
        print(f"### {cue_type.capitalize()} Cues\n")

        # Handle nested structures (like network cues with qlab versions)
        if cue_type == 'network':
            for version, version_props in sorted(properties.items()):
                print(f"#### {version.upper()} Properties\n")
                print("| CSV Column Header | Description | Type |")
                print("|------------------|-------------|------|")

                for key, prop in sorted(version_props.items()):
                    header = format_header_name(key)
                    description = prop.get('description', '')
                    prop_type = prop.get('type', 'string')
                    print(f"| {header} | {description} | {prop_type} |")
                print()
        else:
            print("| CSV Column Header | Description | Type | Valid Values |")
            print("|------------------|-------------|------|--------------|")

            for key, prop in sorted(properties.items()):
                # Skip auto-properties (they're set automatically)
                if 'auto_value' in prop:
                    continue

                header = format_header_name(key)
                description = prop.get('description', '')
                prop_type = prop.get('type', 'string')

                valid_values = ""
                if 'valid_range' in prop:
                    valid_values = f"{prop['valid_range'][0]}-{prop['valid_range'][1]}"

                print(f"| {header} | {description} | {prop_type} | {valid_values} |")
            print()

    # Valid Cue Types
    print("## Valid Cue Types\n")
    print("Use these values in the `Type` column:\n")
    for cue_type in config['valid_cue_types']:
        print(f"- `{cue_type}`")


if __name__ == "__main__":
    generate_docs()
