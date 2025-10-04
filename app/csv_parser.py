import io
import csv

from pythonosc import osc_message_builder, osc_bundle_builder, udp_client, osc_server
from .osc_server import async_osc_server
from .osc_config import get_osc_config


def send_csv(ip, document, qlab_version, passcode, error_handler=None):
    """
    Sends the data in csv file to qlab workspace on machine with given ip.
    Uses dynamic configuration from qlab_osc_config.json

    Args:
        ip: IP address of QLab machine
        document: File-like object containing CSV data
        qlab_version: QLab version (4 or 5)
        passcode: Optional passcode for QLab connection
        error_handler: Optional ErrorHandler instance. If None, uses global handler.
    """
    # Get OSC configuration
    osc_config = get_osc_config()

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

    # Connect with passcode if provided
    if passcode:
        msg = osc_message_builder.OscMessageBuilder(address="/connect")
        msg.add_arg(passcode)
        client.send(msg.build())

    # Process each cue
    for cue in cues:
        bundle = osc_bundle_builder.OscBundleBuilder(osc_bundle_builder.IMMEDIATELY)

        # Create new cue
        cue_type = cue.get("type", "memo").lower()
        validated_cue_type = osc_config.check_cue_type(cue_type)

        if validated_cue_type:
            msg = osc_message_builder.OscMessageBuilder(address="/new")
            msg.add_arg(validated_cue_type)
            bundle.add_content(msg.build())
        else:
            # Cue type is invalid, create memo cue
            msg = osc_message_builder.OscMessageBuilder(address="/new")
            msg.add_arg("memo")
            bundle.add_content(msg.build())
            validated_cue_type = "memo"

        # Track properties that have been set to avoid duplicates
        processed_properties = set()

        # Process all properties dynamically using configuration
        for header, value in cue.items():
            # Skip if no value or already processed
            if not value or header in processed_properties or header == 'type':
                continue

            # Build OSC message using configuration
            osc_msg = osc_config.build_osc_message(
                property_name=header,
                value=value,
                cue_type=validated_cue_type,
                qlab_version=qlab_version,
                cue_data=cue
            )

            if osc_msg:
                bundle.add_content(osc_msg.build())
                processed_properties.add(header)

                # Check for auto-properties (e.g., doopacity when fadeopacity is set)
                auto_props = osc_config.get_auto_properties(header, validated_cue_type)
                for auto_prop_name, auto_prop_value in auto_props:
                    auto_msg = osc_config.build_osc_message(
                        property_name=auto_prop_name,
                        value=auto_prop_value,
                        cue_type=validated_cue_type,
                        qlab_version=qlab_version
                    )
                    if auto_msg:
                        bundle.add_content(auto_msg.build())

        # Send the bundle
        client.send(bundle.build())
        async_osc_server(ip, 53001, error_handler)
