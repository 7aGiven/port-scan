import asyncio

class Protocol:
    def connection_made(self, transport):
        self.sockname = transport.get_extra_info("sockname")
    def datagram_received(self, data, addr):
        print(self.sockname)

async def main():
    try:
        for port in range(10000, 20000):
            await loop.create_datagram_endpoint(Protocol, ("::", port))
    except Exception as e:
        print(port)
        print(repr(e))
        return
    await asyncio.sleep(6 * 60 * 60)

loop = asyncio.new_event_loop()
loop.run_until_complete(main())