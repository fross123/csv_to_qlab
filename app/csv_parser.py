import io
import csv

from pythonosc import osc_message_builder, osc_bundle_builder, udp_client, osc_server
from osc_server import async_osc_server
from qlab_osc_dictionary import *


def check_cue_type(type):
    """Return the valid type of cue, or False"""
    valid_types = [
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
        "cue cart",
    ]
    type = type.lower()
    if type not in valid_types:
        return False
    else:
        return type


def check_color_type(color):
    """Returns the valid color, or false"""
    valid_colors = ["none", "red", "orange", "green", "blue", "purple"]
    color = color.lower()
    if color not in valid_colors:
        return False
    else:
        return color


def send_csv(ip, document, ql5_passcode):
    """
    Sends the data in csv file to qlab workspace on machine with given ip.
    """
    client = udp_client.UDPClient(ip, 53000)

    stream = io.StringIO(document.stream.read().decode("UTF8"), newline="")
    reader = csv.reader(stream)

    # Retrieve row one from csv document and use as headers.
    headers = [x.lower().replace(" ", "") for x in next(reader)]

    cues = []

    # Build cue list to be sent to qlab.
    for line in reader:
        count = 0
        cue = {}
        for header in headers:
            cue[header] = line[count]
            count += 1
        cues.append(cue)

    if ql5_passcode:
        msg = osc_message_builder.OscMessageBuilder(address="/connect")
        msg.add_arg(ql5_passcode)
        client.send(msg.build())

    for cue in cues:
        bundle = osc_bundle_builder.OscBundleBuilder(osc_bundle_builder.IMMEDIATELY)
        msg = osc_message_builder.OscMessageBuilder(address="/new")
        if check_cue_type(cue["type"]):
            bundle.add_content(new_cue(check_cue_type(cue["type"])).build())
        else:
            # Cue type is invalid, create memo cue.
            bundle.add_content(new_cue("memo").build())

        # Number
        if cue.get("number"):
            bundle.add_content(cue_number(f"{cue['number']}").build())

        # Name
        bundle.add_content(cue_name(f"{cue['name']}").build())

        # Page/Notes
        if cue.get("notes"):
            bundle.add_content(cue_notes(cue["notes"]).build())

        # Continue Mode/Follow
        if cue.get("follow") or cue.get("continueMode"):
            continue_mode = cue.get("continueMode")
            bundle.add_content(cue_continueMode(continue_mode).build())
        
        # Target
        if cue.get("target"):
            bundle.add_content(cue_cueTargetNumber(f"{cue['target']}").build())

        # File Target
        if cue.get("filetarget"):
            bundle.add_content(cue_fileTarget(f"{cue['filetarget']}"))

        # Color
        if cue.get("color"):
            bundle.add_content(cue_colorName(check_color_type(cue["color"])).build())

        # Midi Cues
        if check_cue_type(cue["type"]) == "midi":
            if cue.get("midimessagetype"):
                bundle.add_content(
                    midi_messageType(int(cue["midimessagetype"])).build()
                )

            if cue.get("midicommandformat"):
                bundle.add_content(
                    midi_commandFormat(int(cue["midicommandformat"])).build()
                )

            if cue.get("midicommand"):
                bundle.add_content(midi_command(int(cue["midicommand"])).build())

            if cue.get("midideviceid"):
                bundle.add_content(midi_deviceID(int(cue["midideviceid"])).build())

            if cue.get("midicontrolnumber"):
                bundle.add_content(
                    midi_controlNumber(int(cue["midicontrolnumber"])).build()
                )

            if cue.get("midicontrolvalue"):
                bundle.add_content(
                    midi_controlValue(int(cue["midicontrolvalue"])).build()
                )

            if cue.get("midipatchname"):
                bundle.add_content(midi_midiPatchName(cue["midipatchname"]).build())

            if cue.get("midipatchnumber"):
                bundle.add_content(
                    midi_midiPatchNumber(int(cue["midipatchnumber"])).build()
                )

            if cue.get("midiqlist"):
                bundle.add_content(midi_qList(cue["midiqlist"]).build())

            if cue.get("midiqnumber"):
                bundle.add_content(midi_qNumber(cue["midiqnumber"]).build())

        # Network Cues
        if check_cue_type(cue["type"]) == "network":
            if cue.get("message type"):
                msg = osc_message_builder.OscMessageBuilder(
                    address="/cue/selected/messageType"
                )
                msg.add_arg(int(cue["message type"]))
                bundle.add_content(msg.build())

            if cue.get("message type") == "1":
                # For a qlab message
                if cue.get("command"):
                    msg = osc_message_builder.OscMessageBuilder(
                        address="/cue/selected/qlabCommand"
                    )
                    msg.add_arg(int(cue["command"]))
                    bundle.add_content(msg.build())

                if cue.get("osc cue number"):
                    msg = osc_message_builder.OscMessageBuilder(
                        address="/cue/selected/qlabCueNumber"
                    )
                    msg.add_arg(cue["osc cue number"])
                    bundle.add_content(msg.build())

                else:
                    msg = osc_message_builder.OscMessageBuilder(
                        address="/cue/selected/qlabCueNumber"
                    )
                    msg.add_arg(cue["number"])
                    bundle.add_content(msg.build())

            elif cue.get("message type") == "2":
                # For an OSC message
                if cue.get("command"):
                    msg = osc_message_builder.OscMessageBuilder(
                        address="/cue/selected/rawString"
                    )
                    msg.add_arg(cue["command"])
                    bundle.add_content(msg.build())

            else:
                # TODO: Handle UDP messages
                pass

        

        client.send(bundle.build())
        async_osc_server(ip, 53001)
