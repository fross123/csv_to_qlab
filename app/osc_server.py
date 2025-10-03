from pythonosc.osc_server import AsyncIOOSCUDPServer
from pythonosc.dispatcher import Dispatcher
import asyncio
import json
from error_success_handler import handle_errors, count_success, ErrorHandler


def async_osc_server(ip, port, error_handler=None):
    """
    Start async OSC server to receive replies from QLab

    Args:
        ip: IP address to listen on
        port: Port to listen on
        error_handler: Optional ErrorHandler instance. If None, uses global handler.
    """
    # Use provided handler or fall back to global functions
    if error_handler:
        def filter_handler(address, *args):
            data = json.loads(args[0])
            if not data["status"] == "ok":
                error_handler.handle_errors(data["status"], f"{address}: {args}")
            else:
                error_handler.count_success(data["status"], f"{address}: {args}")
    else:
        def filter_handler(address, *args):
            data = json.loads(args[0])
            if not data["status"] == "ok":
                handle_errors(data["status"], f"{address}: {args}")
            else:
                count_success(data["status"], f"{address}: {args}")

    dispatcher = Dispatcher()
    dispatcher.map("/reply/*", filter_handler)

    async def loop():
        for i in range(1):
            await asyncio.sleep(0.05)

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
