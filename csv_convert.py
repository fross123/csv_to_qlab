import io
import csv
import os
import time

from pythonosc import osc_message_builder, osc_bundle_builder, udp_client

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

    stream = io.StringIO(document.stream.read().decode("UTF8"), newline='')
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
        bundle = osc_bundle_builder.OscBundleBuilder(osc_bundle_builder.IMMEDIATELY)
        msg = osc_message_builder.OscMessageBuilder(address = "/new")
        if check_cue_type(cue["type"]):
            msg.add_arg(check_cue_type(cue["type"]))
        else:
            msg.add_arg("memo")
        bundle.add_content(msg.build())
        
        if cue.get('number'):
            msg = osc_message_builder.OscMessageBuilder(address = "/cue/selected/number")
            if cue.get('number prefix'):
                msg.add_arg(f"{cue['number prefix']}{cue['number']}")
            else:
                msg.add_arg(f"{cue['number']}")
            bundle.add_content(msg.build())

        msg = osc_message_builder.OscMessageBuilder(address = "/cue/selected/name")
        msg.add_arg(f"{cue['name']}")
        bundle.add_content(msg.build())

        if cue.get('page') or cue.get('notes'):
            msg = osc_message_builder.OscMessageBuilder(address = "/cue/selected/notes")
            if cue["page"] and cue["notes"]:
                msg.add_arg(f"p:{cue['page']} Notes: {cue['notes']}")
            elif cue["page"]:
                msg.add_arg(f"p:{cue['page']}")
            elif cue["notes"]:
                msg.add_arg(f"{cue['notes']}")
            bundle.add_content(msg.build())

        if cue.get('follow'):
            msg = osc_message_builder.OscMessageBuilder(address="/cue/selected/continueMode")
            msg.add_arg(int(cue["follow"]))
            bundle.add_content(msg.build())

        if check_cue_type(cue["type"]) == "midi":
            if cue.get('message type'):
                msg = osc_message_builder.OscMessageBuilder(address = "/cue/selected/messageType")
                msg.add_arg(int(cue["message type"]))
                bundle.add_content(msg.build())
                

            if cue.get("command format"):
                msg = osc_message_builder.OscMessageBuilder(address = "/cue/selected/commandFormat")
                msg.add_arg(int(cue['command format']))
                bundle.add_content(msg.build())
                

            if cue.get("command"):
                msg = osc_message_builder.OscMessageBuilder(address="/cue/selected/command")
                msg.add_arg(int(cue["command"]))
                bundle.add_content(msg.build())
                

            if cue.get("device id"):
                msg = osc_message_builder.OscMessageBuilder(address = "/cue/selected/deviceID")
                msg.add_arg(int(cue["device id"]))
                bundle.add_content(msg.build())
                

            if cue.get('midi cue number'):
                msg = osc_message_builder.OscMessageBuilder(address = "/cue/selected/qNumber")
                msg.add_arg(f"{cue['midi cue number']}")
                bundle.add_content(msg.build())
                
        
        if check_cue_type(cue["type"]) == "network":            
            msg = osc_message_builder.OscMessageBuilder(address = "/cue/selected/messageType")
            msg.add_arg(int(cue["message type"]))
            bundle.add_content(msg.build())

            if cue.get("message type") != "2":
                if cue.get('command'):
                    msg = osc_message_builder.OscMessageBuilder(address="/cue/selected/qlabCommand")
                    msg.add_arg(int(cue["command"]))
                    bundle.add_content(msg.build())
                    

                if cue.get('osc cue number'):
                    msg = osc_message_builder.OscMessageBuilder(address="/cue/selected/qlabCueNumber")
                    msg.add_arg(cue["osc cue number"])
                    bundle.add_content(msg.build())
                    
                else:
                    msg = osc_message_builder.OscMessageBuilder(address="/cue/selected/qlabCueNumber")
                    msg.add_arg(cue["number"])
                    bundle.add_content(msg.build())

            elif cue.get("message type") == "2":
                msg = osc_message_builder.OscMessageBuilder(address="/cue/selected/rawString")
                msg.add_arg(f"/eos/cue/01/{cue['number']}/fire")
                bundle.add_content(msg.build())

        if cue.get('target'):
            msg = osc_message_builder.OscMessageBuilder(address = "/cue/selected/cueTargetNumber")
            msg.add_arg(f"{cue['target']}")
            bundle.add_content(msg.build())
            

        msg = osc_message_builder.OscMessageBuilder(address = "/cue/selected/colorName")
        if cue.get('color'):
            msg.add_arg(check_color_type(cue['color']))
        else:
            msg.add_arg("none")
        bundle.add_content(msg.build())
    
        client.send(bundle.build())
