import socket
import asyncio

from notebook.notebookapp import raw_input


class Client:
    def __init__(self, server):
        self.server = server
        asyncio.run(self.start_con())

    async def start_con(self):
        self.reader, self.writer = await asyncio.open_connection(self.server[0], self.server[1])
        print("Connected!!!")

        while True:
            try:
                # message = input('Message: ')
                # if message == 'quit':
                #     print("Closed manually\n")
                #     print('Close the connection')
                #     self.writer.close()
                #     await self.writer.wait_closed()
                #     break

                message = "Hello World!!!!"
                self.writer.write(bytes((message+"\n"), "Utf-8"))
                await self.writer.drain()
                data = await self.reader.read(1024)
                print(f'Received: {data.decode()!r}')
            except Exception as ex:
                print("Closed due to the error\n", ex)
                print('Close the connection')
                self.writer.close()
                await self.writer.wait_closed()
                break

c = Client(('172.31.1.147', 8080))
# 172.31.1.250


