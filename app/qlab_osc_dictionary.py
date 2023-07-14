from pythonosc import osc_message_builder, osc_bundle_builder


def alwaysReply(number):
    """
    By default, QLab will only reply to an incoming OSC message
    if that message generates a reply to send. For example,
    /go does not generate a reply.

    Read: If number is not given, return the alwaysReply status
    for the sending client.

    Write: If number is given and is not zero, send a reply for
    every OSC message received from the client. Messages that would
    not normally generate a reply will generate one with a JSON
    string argument that contains:

    {
        "workspace_id" : {string},
        "address": "/osc/message/that/was/sent",
        "status": {"ok" or "error"}
    }
    If number is given and is 0, stop sending replies to messages
    that do not generate replies.
    """
    msg = osc_message_builder.OscMessageBuilder(address="/alwaysReply")
    msg.add_arg(int(number))
    return msg


def disconnect():
    """
    Disconnect from QLab. Clients should send this message when
    they will no longer be sending messages to QLab.

    If you are communicating with QLab via UDP, QLab will automatically
    disconnect your client if it has not heard any messages from it in
    the last 61 seconds. Any message (e.g. /thump) will serve to keep
    the client connected, or you can send /forgetMeNot or /udpKeepAlive
    (see below) to override this 61-second timeout. If you are disconnected,
    you will need to reconnect before further commands will be accepted.
    If you are using a connection with a passcode, the passcode needs to be
    sent again, just as though you were connecting for the first time.

    If you are communicating with QLab via TCP, QLab will not automatically
    disconnect your client, because TCP is nice like that. Clients will
    remain connected until they send /disconnect or until the TCP connection
    itself is disconnected.
    """
    msg = osc_message_builder.OscMessageBuilder(address="/disconnect")
    return msg


def liveFadePreview(boolean):
    """
    Enable or disable live fade preview. See details on booleans at the
    beginning of this section. If no argument is given, return the current
    status of live fade preview.
    """
    msg = osc_message_builder.OscMessageBuilder(address="/liveFadePreview")
    return msg


def new_cue(cue_type):
    """
    Create a new cue. cue_type is a string stating the type of cue to create.
    Supported strings include:
    audio, mic, video, camera, text, light, fade, network, midi, midi file,
    timecode, group, start, stop, pause, load, reset, devamp, goto, target,
    arm, disarm, wait, memo, script, list, cuelist, cue list, cart, cuecart,
    or cue cart.

    This method returns the unique ID of the new cue. The newly created cue
    will also be selected, so subsequent commands can address the new cue
    either using the unique ID or simply by addressing the currently selected cue.

    This method has three optional additional arguments:

    /workspace/{id}/new {cue_type} {cue_ID} {cart_row} {cart_column}

    If {cue_ID} is supplied, the new cue will be created after that cue.

    If {cue_ID} specifies a cart, the new cue will be created within the cart.
    You must then specify the position in the cart using {cart_row} and
    {cart_column}, which must be integers.
    """

    msg = osc_message_builder.OscMessageBuilder(address="/new")
    msg.add_arg(cue_type)
    return msg


def cue_armed(boolean):
    """
    Read: If no argument is given, return the armed state of the specified cue.

    Write: If boolean is true, arm the specified cue. If false, disarm the
    specified cue. See details on booleans at the beginning of this section.
    """

    msg = osc_message_builder.OscMessageBuilder(address="/cue/selected/armed")
    msg.add_arg(bool(boolean))
    return msg


def cue_autoLoad(boolean):
    """
    Read: If no argument is given, return the auto-load state of the specified cue.

    Write: If boolean is true, set the specified cue to auto-load. If false, set
    the specified cue to not auto-load. See details on booleans at the beginning
    of this section.
    """

    msg = osc_message_builder.OscMessageBuilder(address="/cue/selected/autoLoad")
    msg.add_arg(bool(boolean))
    return msg


def cue_colorName(string):
    """
    Read: If no argument is given, return the color of the specified cue.

    Write: If string is given, set the color of the specified cue to string.
    As of QLab 5.2, valid colors are:

    berry
    blue
    crimson
    cyan
    forest
    gray
    green
    hot pink
    indigo
    lavender
    magenta
    midnight
    olive
    orange
    peach
    plum
    purple
    red
    sky blue
    yellow

    and

    none

    """

    msg = osc_message_builder.OscMessageBuilder(address="/cue/selected/colorName")
    msg.add_arg(string)
    return msg


def cue_continueMode(number):
    """
    Read: If no argument is given, return the continue mode of the specified cue.

    Write: If number is given, set the continue mode of the specified cue to number.
    Valid continue modes are:

    0 - No continue
    1 - Auto-continue
    2 - Auto-follow
    """

    msg = osc_message_builder.OscMessageBuilder(address="/cue/selected/continueMode")
    msg.add_arg(int(number))
    return msg


def cue_cueTargetNumber(string):
    """
    Read: If no argument is given, return the cue number of the target of the specified cue.
    Empty string ("") means that the cue has no cue target.

    Write: If string is given, and if the specified cue can have cue targets,
    set the target of the specified cue to string.
    string must be a valid cue number of a cue in the workspace.
    """

    msg = osc_message_builder.OscMessageBuilder(address="/cue/selected/cueTargetNumber")
    msg.add_arg(string)
    return msg


def cue_duration(number):
    """
    Read: If no argument is given, return the duration of the specified cue.

    Write: If number is given, and the selected cue has an editable duration,
    set the duration of the specified cue to number.
    """

    msg = osc_message_builder.OscMessageBuilder(address="/cue/selected/duration")
    msg.add_arg(int(number))
    return msg


def cue_fadeAndStopOthers(number):
    """
    Read: If no argument is given, return the Fade and stop mode of the specified cue.

    Write: If number is given, set the Fade and stop mode of the specified cue to number.
    Valid modes are:

    0 - None
    1 - Peers
    2 - List or cart
    3 - All
    Mode 0 is equivalent to the Fade and stop checkbox being unchecked.
    """

    if number < 3:
        msg = osc_message_builder.OscMessageBuilder(
            address="/cue/selected/fadeAndStopOthers"
        )
        msg.add_arg(int(number))
        return msg
    else:
        return ValueError(
            "Fade and Stop Others Number not valid. Must be 0-3. See QLab OSC Dictionary."
        )


def cue_fadeAndStopOthersTime(number):
    """
    Read: If no argument is given, return the Fade and stop others time of the specified cue.

    Write: If number is given, set the Fade and stop others time of the specified cue to number.
    """

    msg = osc_message_builder.OscMessageBuilder(
        address="/cue/selected/fadeAndStopOthersTime"
    )
    msg.add_arg(int(number))
    return msg


def cue_fileTarget(string):
    """
    Read: If no argument is given, return the target of the specified cue. Empty string ("")
    means that the cue has no file target.

    Write: If string is given, and if the specified cue can have file targets, set the target
    of the specified cue to string. If string is "none" or empty (""), unset the file target.
    If string is anything else, string should be a file path and name in any of the following
    three forms:

    Full paths, e.g. /Volumes/MyDisk/path/to/some/file.wav
    Paths beginning with a tilde, e.g. ~/path/to some/file.mov
    Relative paths, e.g. this/is/a/relative/path.mid
    Paths beginning with a tilde (~) will be expanded; the tilde signifies “relative to the
    user’s home directory”.

    Relative paths will be interpreted according to the current working directory.
    Use the /workingDirectory application message to set or get the current working directory.
    """

    msg = osc_message_builder.OscMessageBuilder(address="/cue/selected/fileTarget")
    msg.add_arg(string)
    return msg


def cue_flagged(boolean):
    """
    Read: If no argument is given, return the state of the Flagged checkbox of the specified cue.

    Write: Set the flagged state of the specified cue. See details on booleans at the
    beginning of this section.
    """
    msg = osc_message_builder.OscMessageBuilder(address="/cue/selected/flagged")
    msg.add_arg(bool(boolean))
    return msg


def cue_name(string):
    """
    Read: If no argument is given, return the name of the specified cue.

    Write: If string is given, set the name of the specified cue to string.
    """

    msg = osc_message_builder.OscMessageBuilder(address="/cue/selected/name")
    msg.add_arg(string)
    return msg


def cue_notes(string):
    """
    Read: If no argument is given, return the notes of the specified cue.

    Write: If string is given, set the notes of the specified cue to string.
    """

    msg = osc_message_builder.OscMessageBuilder(address="/cue/selected/notes")
    msg.add_arg(string)
    return msg


def cue_number(string):
    """
    Read: If no argument is given, return the cue number of the specified cue.

    Write: If string is given, set the cue number of the specified cue to string.
    """

    msg = osc_message_builder.OscMessageBuilder(address="/cue/selected/number")
    msg.add_arg(string)
    return msg


def cue_postWait(number):
    """
    Read: If no argument is given, return the post-wait of the specified cue.

    Write: If number is given, set the post-wait of the specified cue to number.
    """

    msg = osc_message_builder.OscMessageBuilder(address="/cue/selected/postWait")
    msg.add_arg(int(number))
    return msg


def cue_preWait(number):
    """
    Read: If no argument is given, return the pre-wait of the specified cue.

    Write: If number is given, set the pre-wait of the specified cue to number.
    """

    msg = osc_message_builder.OscMessageBuilder(address="/cue/selected/preWait")
    msg.add_arg(int(number))
    return msg


# def cue_midi(command_num, commandFormat_num):
#     midi_bundle = osc_bundle_builder.OscBundleBuilder(osc_bundle_builder.IMMEDIATELY)
#     return


def midi_command(command_num):
    """
    Read: If no argument is given, return the MSC command of the specified cue.

    Write: If number is given, set the MSC command of the specified cue to number.
    number must be a whole number from 0 to 127 representing the index of an MSC
    command, a list of which can be found in the Parameter Reference page of this manual.
    """

    if command_num < 127 and command_num > 0:
        msg = osc_message_builder.OscMessageBuilder(address="/cue/selected/command")
        msg.add_arg(int(command_num))
        return msg
    else:
        return ValueError(
            "MIDI Command must be a number from 0-127. See QLab OSC Dictionary."
        )


def midi_commandFormat(commandFormat_num):
    """
    Read: If no argument is given, return the MSC command format of the specified cue.

    Write: If number is given, set the MSC command format of the specified cue to number.
    number must be a whole number from 0 to 127 representing the index of an MSC command
    format, a list of which can be found in the Parameter Reference page of this manual.
    """
    if commandFormat_num < 127 and commandFormat_num > 0:
        msg = osc_message_builder.OscMessageBuilder(
            address="/cue/selected/commandFormat"
        )
        msg.add_arg(int(commandFormat_num))
        return msg
    else:
        return ValueError(
            "MIDI Command Format must be a number from 0-127. See QLab OSC Dictionary."
        )


def midi_controlNumber(controlNumber):
    if controlNumber < 16383 and controlNumber > 0:
        msg = osc_message_builder.OscMessageBuilder(
            address="/cue/selected/controlNumber"
        )
        msg.add_arg(int(controlNumber))
        return msg
    else:
        return ValueError(
            "MIDI Control Number must be a number from 0-16383. See QLab OSC Dictionary."
        )


def midi_controlValue(number):
    if number < 16383 and number > 0:
        msg = osc_message_builder.OscMessageBuilder(
            address="/cue/selected/controlValue"
        )
        msg.add_arg(int(number))
        return msg
    else:
        return ValueError(
            "MIDI Control Value must be a number from 0-16383. See QLab OSC Dictionary."
        )


def midi_deviceID(number):
    """
    Read: If no argument is given, return the outgoing MSC device ID of the specified cue.

    Write: If number is given, set the outgoing MSC device ID of the specified cue to number.
    number must be a whole number from 0 to 127.
    """
    if number < 127 and number > 0:
        msg = osc_message_builder.OscMessageBuilder(address="/cue/selected/deviceID")
        msg.add_arg(int(number))
        return msg
    else:
        return ValueError(
            "MIDI Device ID must be a number from 0-127. See QLab OSC Dictionary."
        )


def midi_messageType(number):
    """
    Read: If no argument is given, return the message type of the specified cue.

    Write: If number is given, set the message type of the specified cue to number.
    Valid message types are:

    1 - MIDI Voice Message ("Musical MIDI")
    2 - MIDI Show Control Message (MSC)
    3 - MIDI SysEx Message
    """
    msg = osc_message_builder.OscMessageBuilder(address="/cue/selected/messageType")
    msg.add_arg(int(number))
    return msg


def midi_midiPatchName(string):
    """
    Read: If no argument is given, return the name of the MIDI patch currently in use by the specified cue.
    String "none" means that the cue is un-patched.

    Write: If string is given and matches the name of a MIDI patch in the workspace,
    set the MIDI patch of the specified cue to that patch. If string is "none" or empty (""),
    un-patch the specified cue. If string is anything else, this message has no effect.
    """

    msg = osc_message_builder.OscMessageBuilder(address="/cue/selected/midiPatchName")
    msg.add_arg(string)
    return msg


def midi_midiPatchNumber(number):
    """
    Read: If no argument is given, return the index of the MIDI patch currently in use by the specified cue.
    Index 0 means that the cue is un-patched, index 1 means the first patch in the patch list in Workspace Settings,
    2 means the second patch, and so on.

    Write: If number is given, set the MIDI patch of the specified cue to that patch.
    If number is 0, un-patch the specified cue. If number is greater than the number of MIDI patches in the workspace,
    this message has no effect. number must be a whole number
    """

    msg = osc_message_builder.OscMessageBuilder(address="/cue/selected/midiPatchNumber")
    msg.add_arg(int(number))
    return msg


def midi_qList(string):
    """
    Read: If no argument is given, return the outgoing MSC cue list number of the specified cue.

    Write: If number is given, set the outgoing MSC cue list number of the specified cue to number.
    """

    msg = osc_message_builder.OscMessageBuilder(address="/cue/selected/qList")
    msg.add_arg(string)
    return msg


def midi_qNumber(string):
    """
    Read: If no argument is given, return the outgoing MSC cue number of the specified cue.

    Write: If number is given, set the outgoing MSC cue number of the specified cue to number.
    """
    msg = osc_message_builder.OscMessageBuilder(address="/cue/selected/qNumber")
    msg.add_arg(string)
    return msg


def midi_qPath(string):
    """
    Read: If no argument is given, return the outgoing MSC cue path number of the specified cue.

    Write: If number is given, set the outgoing MSC cue path number of the specified cue to number.
    """
    msg = osc_message_builder.OscMessageBuilder(address="/cue/selected/qPath")
    msg.add_arg(string)
    return msg


def midi_rawString(string):
    """
    Read: If no argument is given, return the MIDI SysEx string of the specified cue.

    Write: If string is given, set the MIDI SysEx string of the specified cue to string.
    string must be a valid SysEx string, formatted in hexadecimal, and omitting the starting F0 and ending F7.
    """

    msg = osc_message_builder.OscMessageBuilder(address="/cue/selected/rawString")
    msg.add_arg(string)
    return msg


def midi_status(number):
    """
    Read: If no argument is provided, return the MIDI message type of the specified cue.

    Write: If number is given, set the MIDI message type of the specified cue to number. Valid message types are:

    0 - Note Off
    1 - Note On
    2 - Key Pressure (Aftertouch)
    3 - Control Change
    4 - Program Change
    5 - Channel Pressure Change
    6 - Pitch Bend Change
    """

    if number < 6 and number > 0:
        msg = osc_message_builder.OscMessageBuilder(address="/cue/selected/status")
        msg.add_arg(int(number))
        return msg
    else:
        return ValueError("Midi Status must be 0-6. See QLab OSC Dictionary.")


def nw_customString(string):
    """
    Read: If no argument is given, return the message of the specified cue.

    Write: If string is given, and the specified cue’s patch is set to
    “OSC Message,” set the OSC message of the specified cue to string.
    If string is given, and the specified cue’s patch is set to “Plain Text,”
    set the text of the specified cue to string. In all other cases,
    this message has no effect.
    """

    msg = osc_message_builder.OscMessageBuilder(address="/cue/selected/customString")
    msg.add_arg(string)
    return msg


def nw_networkPatchName(string):
    """
    Read: If no argument is given, return the name of the network patch
    currently in use by the specified cue. String "none" means that the cue is un-patched.

    Write: If string is given and matches the name of a network patch
    in the workspace, set the network patch of the specified cue to that patch.
    If string is "none" or empty (""), un-patch the specified cue.
    If string is anything else, this message has no effect.
    """

    msg = osc_message_builder.OscMessageBuilder(
        address="/cue/selected/networkPatchName"
    )
    msg.add_arg(string)
    return msg


def nw_networkPatchNumber(number):
    """
    Read: If no argument is given, return the index of the network patch currently in use by the specified cue. Index 0 means that the cue is un-patched, index 1 means the first patch in the patch list in Workspace Settings, 2 means the second patch, and so on.

    Write: If number is given, set the network patch of the specified cue to that patch. If number is 0, un-patch the specified cue. If number is greater than the number of network patches in the workspace, this message has no effect. number must be a whole number.
    """
    msg = osc_message_builder.OscMessageBuilder(
        address="/cue/selected/networkPatchNumber"
    )
    msg.add_arg(number)
    return msg