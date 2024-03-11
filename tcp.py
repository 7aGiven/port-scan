import asyncio
import socket

class Protocol(asyncio.Protocol):
    def connection_made(self, transport):
        sockname = transport.get_extra_info("sockname")
        print(sockname)
        transport.close()

async def main():
    try:
        for port in range(1024, 10000):
            await loop.create_server(Protocol, "::", port, family=socket.AF_INET6)
    except Exception as e:
        print(port)
        print(e)
        return
    await asyncio.sleep(6 * 60 * 60)

loop = asyncio.new_event_loop()
loop.run_until_complete(main())