import threading
from pythonosc.osc_server import AsyncIOOSCUDPServer, ThreadingOSCUDPServer
from pythonosc.dispatcher import Dispatcher
import asyncio
import json
from error_success_handler import handle_errors, count_success, store_cue_id


def filter_handler(address, *args):
    """
    Handles the replies from QLab.
    """

    data = json.loads(args[1])
    if not data["status"] == "ok":
        store_cue_id(data)
        handle_errors(data["status"], f"{address}: {args}")
    else:
        store_cue_id(data["data"])
        count_success(data["status"], f"{address}: {args}")


def async_osc_server(ip, port):
    """
    No longer in use. Deprecieated, will remove with next release.
    """
    dispatcher = Dispatcher()
    dispatcher.map("/reply/*", filter_handler)

    async def loop():
        for i in range(4):
            await asyncio.sleep(0.04)

    async def init_main():
        server = AsyncIOOSCUDPServer((ip, port), dispatcher, asyncio.get_event_loop())
        (
            transport,
            protocol,
        ) = (
            await server.create_serve_endpoint()
        )  # Create datagram endpoint and start serving

        await loop()  # Enter main loop of program

        transport.close()  # Clean up serve endpoint

    asyncio.run(init_main())


def threading_osc_server(ip, port):
    """
    Threading OSC Server.

    Dispatcher /reply/* -> filter_handler()

    Args: ip, port
    """
    dispatcher = Dispatcher()
    dispatcher.map("/reply/*", filter_handler, ip, port)

    server = ThreadingOSCUDPServer((ip, port), dispatcher)
    
    return server