import asyncio


class Server:

    def __init__(self):
        asyncio.run(self.main())

    async def main(self):
        server = await asyncio.start_server(
            self.handle_echo, '127.0.0.1', 8080)

        addr = server.sockets[0].getsockname()
        print(f'Serving on {addr}')

        async with server:
            await server.serve_forever()

    async def handle_echo(self, reader, writer):

        while True:
            data = await reader.read(100)
            message = data.decode()
            addr = writer.get_extra_info('peername')

            print(f"Received {message!r} from {addr!r}")
            if(data == "/shut"):
                print("Close the connection")
                writer.close()
            else:
                print(f"Send: {message!r}")
                writer.write(data)
                await writer.drain()

s = Server()