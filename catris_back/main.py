import asyncio
import socket


HOST_ADDR = 'localhost'
HOST_PORT = 12345


async def handle_client(reader, writer):
    while True:
        data = await reader.read(100)
        if data:
            print("Received:", data.decode('utf-8'))
            print("Sending data back to the client")
            writer.write(data)
            await writer.drain()
        else:
            print("Closing the connection")
            writer.close()
            break


async def main():
    server = await asyncio.start_server(
        handle_client, HOST_ADDR, HOST_PORT)

    addr = server.sockets[0].getsockname()
    print(f'listening on {addr}')

    async with server:
        await server.serve_forever()


if __name__ == '__main__':
    asyncio.run(main())