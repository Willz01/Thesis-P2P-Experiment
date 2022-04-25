import argparse
import sys
import os
import multiaddr
import trio

from libp2p import new_host
from libp2p.network.stream.net_stream_interface import INetStream
from libp2p.peer.peerinfo import info_from_p2p_addr
from libp2p.typing import TProtocol

from cosine import get_index
from engcheck import both
from sem import pred

PROTOCOL_ID = TProtocol("/chatSys/1.0.0")
MAX_READ_LEN = 2 ** 32 - 1

HOST_STR = ""


async def read_data(stream: INetStream) -> None:
    while True:
        read_bytes = await stream.read(MAX_READ_LEN)
        if read_bytes is not None:
            read_string = read_bytes.decode()
            if read_string != "\n":
                if read_string.split(" ")[0] == "request":
                    print(read_string)
                    print(get_index(read_string))
                else:
                    print(read_string)
                    pred(read_string)  # semantic analysis
                    both(read_string)  # English scoring


async def write_data(stream: INetStream) -> None:
    async_f = trio.wrap_file(sys.stdin)
    while True:
        line = await async_f.readline()
        await stream.write(line.encode())


async def run(port: int, destination: str) -> None:
    localhost_ip = "127.0.0.1"
    listen_addr = multiaddr.Multiaddr(f"/ip4/0.0.0.0/tcp/{port}")
    host = new_host()
    async with host.run(listen_addrs=[listen_addr]), trio.open_nursery() as nursery:
        if not destination:  # its the server

            async def stream_handler(stream: INetStream) -> None:
                nursery.start_soon(read_data, stream)
                nursery.start_soon(write_data, stream)

            host.set_stream_handler(PROTOCOL_ID, stream_handler)

            c = f" 'python3 chat.py -p {int(port) + 1} -d /ip4/{localhost_ip}/tcp/{port}/p2p/{host.get_id().pretty()}"
            print(
                f"Run 'python3 chat.py "
                f"-p {int(port) + 1} "
                f"-d /ip4/{localhost_ip}/tcp/{port}/p2p/{host.get_id().pretty()}' "
                "on another console."
            )

            os.environ['nodeCon'] = c
            # print(os.environ['nodeCon'])
            print("Waiting for incoming connection...")

        else:  # its the client
            maddr = multiaddr.Multiaddr(destination)
            info = info_from_p2p_addr(maddr)
            # Associate the peer with local ip address
            await host.connect(info)
            # Start a stream with the destination.
            # Multiaddress of the destination peer is fetched from the peerstore using 'peerId'.
            stream = await host.new_stream(info.peer_id, [PROTOCOL_ID])

            nursery.start_soon(read_data, stream)
            nursery.start_soon(write_data, stream)
            print(f"Connected to peer {info.addrs[0]}", host.get_addrs())

        await trio.sleep_forever()


def main() -> None:
    description = """
    This program demonstrates a simple p2p chatSys application using libp2p.
    To use it, first run 'python ./chatSys -p <PORT>', where <PORT> is the port number.
    Then, run another host with 'python ./chatSys -p <ANOTHER_PORT> -d <DESTINATION>',
    where <DESTINATION> is the multiaddress of the previous listener host.
    """
    example_maddr = (
        "/ip4/127.0.0.1/tcp/8000/p2p/QmQn4SwGkDZKkUEpBRBvTmheQycxAHJUNmVEnjA2v1qe8Q"
    )
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument(
        "-p", "--port", default=8000, type=int, help="source port number"
    )
    parser.add_argument(
        "-d",
        "--destination",
        type=str,
        help=f"destination multiaddr string, e.g. {example_maddr}",
    )
    args = parser.parse_args()

    if not args.port:
        raise RuntimeError("was not able to determine a local port")

    try:
        trio.run(run, *(args.port, args.destination))
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    main()
