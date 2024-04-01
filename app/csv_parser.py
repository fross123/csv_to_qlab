import io
import csv

from pythonosc import osc_message_builder, osc_bundle_builder, udp_client
from osc_server import async_osc_server
from qlab_osc_dictionary import *
from error_success_handler import handle_errors, retrieve_previous_cue_id


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
    valid_colors = [
        "none",
        "berry",
        "blue",
        "crimson",
        "cyan",
        "forest",
        "gray",
        "green",
        "hot pink",
        "indigo",
        "lavender",
        "magenta",
        "midnight",
        "olive",
        "orange",
        "peach",
        "plum",
        "purple",
        "red",
        "sky blue",
        "yellow",
    ]
    color = color.lower()
    if color not in valid_colors:
        return False
    else:
        return color

groups = {}

def group_map_helper(qlab_group_id, human_group_id):

    groups[human_group_id] = qlab_group_id


def send_csv(ip, document, qlab_version, passcode):
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

    if passcode:
        msg = osc_message_builder.OscMessageBuilder(address="/connect")
        msg.add_arg(passcode)
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

        # Group Mode
        if cue.get("groupmode"):
            bundle.add_content(group_mode(cue["groupmode"]).build())

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
            bundle.add_content(cue_fileTarget(f"{cue['filetarget']}").build())

       

        # Color
        if cue.get("color"):
            bundle.add_content(cue_colorName(check_color_type(cue["color"])).build())

        if cue.get("text"):
            bundle.add_content(text_text(cue['text']).build())

        # fade cues
        if check_cue_type(cue["type"]) == "fade":
            # Stop Target When Done
            if cue.get("stoptargetwhendone"):
                if cue.get("stoptargetwhendone") == "true":
                    bundle.add_content(fade_stopTargetWhenDone(bool(cue['stoptargetwhendone'])).build())

            if cue.get("fadeopacity"):
                bundle.add_content(fade_opacity(int(cue["fadeopacity"])).build())
                bundle.add_content(fade_do_opacity().build())

        # Video Cues
        if check_cue_type(cue["type"]) == "video":
            # Set video stage
            if cue.get("stagenumber"):
                bundle.add_content(vid_stageNumber(cue["stagenumber"]).build())
            

        # Midi Cues
        if check_cue_type(cue["type"]) == "midi":
            if cue.get("midimessagetype"):
                bundle.add_content(
                    midi_messageType(int(cue["midimessagetype"])).build()
                )

            if cue.get("midirawstring"):
                bundle.add_content(
                    midi_rawString(cue["midirawstring"]).build()
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
            if qlab_version == 5:
                # QLab 5 only supports custom strings or key/value pairs.
                if cue.get("networkpatchnumber"):
                    bundle.add_content(
                        nw_networkPatchNumber(int(cue["networkpatchnumber"])).build()
                    )

                if cue.get("networkpatchname"):
                    bundle.add_content(
                        nw_networkPatchName(cue["networkpatchname"]).build()
                    )

                if cue.get("customstring"):
                    bundle.add_content(nw_customString(cue["customstring"]).build())

            elif qlab_version == 4:
                if cue.get("messagetype"):
                    msg = osc_message_builder.OscMessageBuilder(
                        address="/cue/selected/messageType"
                    )
                    msg.add_arg(int(cue["messagetype"]))
                    bundle.add_content(msg.build())

                if cue.get("messagetype") == "1":
                    # For a qlab message
                    if cue.get("command"):
                        msg = osc_message_builder.OscMessageBuilder(
                            address="/cue/selected/qlabCommand"
                        )
                        msg.add_arg(int(cue["command"]))
                        bundle.add_content(msg.build())

                    if cue.get("osccuenumber"):
                        msg = osc_message_builder.OscMessageBuilder(
                            address="/cue/selected/qlabCueNumber"
                        )
                        msg.add_arg(cue["osccuenumber"])
                        bundle.add_content(msg.build())

                    else:
                        msg = osc_message_builder.OscMessageBuilder(
                            address="/cue/selected/qlabCueNumber"
                        )
                        msg.add_arg(cue["number"])
                        bundle.add_content(msg.build())

                elif cue.get("messagetype") == "2":
                    # For an OSC message
                    if cue.get("command"):
                        msg = osc_message_builder.OscMessageBuilder(
                            address="/cue/selected/rawString"
                        )
                        msg.add_arg(cue["command"])
                        bundle.add_content(msg.build())

        client.send(bundle.build())
        async_osc_server(ip, 53001)

        if cue.get("groupid"):
            if cue.get("type") == "group":
                group_map_helper(retrieve_previous_cue_id(), int(cue["groupid"]))
            else:
                try:
                    group_id = int(cue["groupid"])
                    client.send(move_cue(retrieve_previous_cue_id(), -1, groups[group_id]).build())
                except KeyError:
                    handle_errors("KeyError", "A cue has a Group ID for a group that was not created.")