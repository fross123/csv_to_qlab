from pythonosc.osc_server import AsyncIOOSCUDPServer
from pythonosc.dispatcher import Dispatcher
import asyncio
import json
from error_handler import handle_errors, count_success


def filter_handler(address, *args):
    data = json.loads(args[0])
    if not data["status"] == "ok":
        handle_errors(data["status"], f"{address}: {args}")
    else:
        count_success(data["status"], f"{address}: {args}")


def async_osc_server(ip, port):
    dispatcher = Dispatcher()
    dispatcher.map("/reply/*", filter_handler)

    async def loop():
        """Example main loop that only runs for 10 iterations before finishing"""
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
