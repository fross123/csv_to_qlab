import io
import csv
import os
import time

from pythonosc import osc_message_builder, udp_client

def check_cue_type(type):
    """ Return the valid type of cue, or False """
    valid_types = ["audio", "mic", "video", "camera", "text", "light", "fade", "network", "midi", "midi file", "timecode", "group", "start", "stop", "pause", "load", "reset", "devamp", "goto", "target", "arm", "disarm", "wait", "memo", "script", "list", "cuelist", "cue list", "cart", "cuecart", "cue cart"]
    type = type.lower()
    if type not in valid_types:
        return False
    else:
        return type

def check_color_type(color):
    """ Returns the valid color, or false """
    valid_colors = ["none", "red", "orange", "green", "blue", "purple"]
    color = color.lower()
    if color not in valid_colors:
        return False
    else:
        return color

def send_csv(ip, document):
    client = udp_client.UDPClient(ip, 53000)

    stream = io.StringIO(document.stream.read().decode("UTF8"), newline=None)
    reader = csv.reader(stream)
    headers = [x.lower() for x in next(reader)]
    cues = []

    for line in reader:
        count = 0
        cue = {}
        for header in headers:
            cue[header] = line[count]
            count+=1
        cues.append(cue)

    for cue in cues:
        msg = osc_message_builder.OscMessageBuilder(address = "/new")
        if check_cue_type(cue["type"]):
            msg.add_arg(check_cue_type(cue["type"]))
        else:
            msg.add_arg("memo")
        msg = msg.build()
        client.send(msg)
        
        msg = osc_message_builder.OscMessageBuilder(address = "/cue/selected/number")
        msg.add_arg(f"{cue['number']}")
        msg = msg.build()
        client.send(msg)

        msg = osc_message_builder.OscMessageBuilder(address = "/cue/selected/name")
        msg.add_arg(f"{cue['name']}")
        msg = msg.build()
        client.send(msg)

        msg = osc_message_builder.OscMessageBuilder(address = "/cue/selected/notes")
        msg.add_arg(f"p:{cue['page']} Notes: {cue['notes']}")
        msg = msg.build()
        client.send(msg)

        if check_cue_type(cue["type"]) == "midi":
            if cue["message type"]:
                msg = osc_message_builder.OscMessageBuilder(address = "/cue/selected/messageType")
                msg.add_arg(int(cue["message type"]))
                msg = msg.build()
                client.send(msg)

            if cue["command format"]:
                msg = osc_message_builder.OscMessageBuilder(address = "/cue/selected/commandFormat")
                msg.add_arg(int(cue['command format']))
                msg = msg.build()
                client.send(msg)

            if cue["command"]:
                msg = osc_message_builder.OscMessageBuilder(address="/cue/selected/command")
                msg.add_arg(int(cue["command"]))
                msg = msg.build()
                client.send(msg)

            if cue["device id"]:
                msg = osc_message_builder.OscMessageBuilder(address = "/cue/selected/deviceID")
                msg.add_arg(int(cue["device id"]))
                msg = msg.build()
                client.send(msg)

            if cue['midi cue number']:
                msg = osc_message_builder.OscMessageBuilder(address = "/cue/selected/qNumber")
                msg.add_arg(f"{cue['midi cue number']}")
                msg = msg.build()
                client.send(msg)
        
        if check_cue_type(cue["type"]) == "network":
            if cue["message type"]:
                msg = osc_message_builder.OscMessageBuilder(address = "/cue/selected/messageType")
                msg.add_arg(int(cue["message type"]))
                msg = msg.build()
                client.send(msg)

            if cue["command"]:
                msg = osc_message_builder.OscMessageBuilder(address="/cue/selected/qlabCommand")
                msg.add_arg(int(cue["command"]))
                msg = msg.build()
                client.send(msg)

            if cue["osc cue number"]:
                msg = osc_message_builder.OscMessageBuilder(address="/cue/selected/qlabCueNumber")
                msg.add_arg(cue["osc cue number"])
                msg = msg.build()
                client.send(msg)
            else:
                msg = osc_message_builder.OscMessageBuilder(address="/cue/selected/qlabCueNumber")
                msg.add_arg(cue["number"])
                msg = msg.build()
                client.send(msg)

        if cue['target']:
            msg = osc_message_builder.OscMessageBuilder(address = "/cue/selected/cueTargetNumber")
            msg.add_arg(f"{cue['target']}")
            msg = msg.build()
            client.send(msg)

        msg = osc_message_builder.OscMessageBuilder(address = "/cue/selected/colorName")
        if check_color_type(cue['color']):
            msg.add_arg(check_color_type(cue['color']))
        else:
            msg.add_arg("none")
        msg = msg.build()
        client.send(msg)
