import io
import csv
import os
import time

from pythonosc import osc_message_builder, udp_client

def send_csv(ip, document, device_ID):
    client = udp_client.UDPClient(ip, 53000)

    stream = io.StringIO(document.stream.read().decode("UTF8"), newline=None)
    reader = csv.reader(stream)

    for Cue, Page, Name, Notes in reader:
        msg = osc_message_builder.OscMessageBuilder(address = "/new")
        msg.add_arg("midi")
        msg = msg.build()
        client.send(msg)

        msg = osc_message_builder.OscMessageBuilder(address = "/cue/selected/number")
        msg.add_arg(f"LX{Cue}")
        msg = msg.build()
        client.send(msg)

        msg = osc_message_builder.OscMessageBuilder(address = "/cue/selected/name")
        msg.add_arg(f"{Name}")
        msg = msg.build()
        client.send(msg)

        msg = osc_message_builder.OscMessageBuilder(address = "/cue/selected/notes")
        msg.add_arg(f"p:{Page} Notes: {Notes}")
        msg = msg.build()
        client.send(msg)

        msg = osc_message_builder.OscMessageBuilder(address = "/cue/selected/messageType")
        msg.add_arg(2)
        msg = msg.build()
        client.send(msg)

        msg = osc_message_builder.OscMessageBuilder(address = "/cue/selected/commandFormat")
        msg.add_arg(1)
        msg = msg.build()
        client.send(msg)

        msg = osc_message_builder.OscMessageBuilder(address = "/cue/selected/deviceID")
        msg.add_arg(int(device_ID))
        msg = msg.build()
        client.send(msg)

        msg = osc_message_builder.OscMessageBuilder(address = "/cue/selected/qNumber")
        msg.add_arg(f"{Cue}")
        msg = msg.build()
        client.send(msg)

        msg = osc_message_builder.OscMessageBuilder(address = "/cue/selected/colorName")
        msg.add_arg("purple")
        msg = msg.build()
        client.send(msg)
