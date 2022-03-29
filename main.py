import argparse
import sys
from datetime import datetime
import pickle
import os

import multiaddr
import trio

from libp2p import new_host  # peer
from libp2p.crypto.secp256k1 import create_new_key_pair  # check
from libp2p.network.stream.net_stream_interface import INetStream  # stream
from libp2p.peer.peerinfo import info_from_p2p_addr  # peer info
from libp2p.typing import TProtocol

from utils.filehandler import exist, read_content, read_desc
from model.content import Content
from model.packet import Packet
from detection.checker import check_packet

commands = dict({
    'search': b'\x0A',  # search for file on network - via connected nodes
    'download': b'\x0B',  # download file from network
    'peer-info': b'\x0C',  # get peer-info on connected* peer: live,....
    'delete': b'\x0D',  # check
    'disconnect': b'\x0E',  # disconnect from a connected peer
    'list': b'\x0F'  # list files
})

PROTOCOL_ID = TProtocol("/genZ/1.0.0")


def handle_command(author: str) -> Packet:
    print("Enter command: ")
    line = input()
    stripped = line.split(" ")

    try:
        c = stripped[0]  # command
        f = stripped[1]  # file name
        # print(f)
        # print(exist(f))
        # print(read_content(f))

        if c in commands and exist(f):
            #  print("Command   || value")
            # print(line, commands.get(c))
            # print(sys.getsizeof(commands.get(c)))
            p = construct_packet(c, read_content(f), author, f)
            return p
        else:
            print("Command not available")
            print("Available commands: ", commands.keys())
            # return 'empty'

    except IndexError:
        print("Invalid input")


def construct_packet(command, file, author, filename) -> Packet:
    content = Content(content_name=filename, data=file.encode(), descriptors=None, query=f"{command} {filename}",
                      content_type=command)
    #  p = Packet(author=author, c=content, timestamp=str(datetime.now()))
    p = Packet(data=file.encode(), author=author, descriptors=None, query=f"{command} {filename}", packet_name=filename)
    return p


def search():
    # get list of connected peers
    # loop over file packets
    # check matches
    # get peers with searched content
    # check Hash table of flags
    # download from the safest peer depending on flag variable
    download(False)
    pass


# user command

def download(kick):
    """
        if @param kick is True - search() is called since the file content has to be
        search for on connected peers before been downloaded.

        @:parameter kick is False - download() was called from search() following a
        search command. Packet download is launched.
    """
    if kick:
        search()
    else:
        temp = "Ert"
        # download code
    pass


def disconnect():
    pass


def list_contents():
    pass


def get_peer_info(host):
    return host.P
    pass


def handle_read_packet(stream_txt) -> None:
    msg_split = stream_txt.decode().split(" ")
    print(msg_split)
    print(sys.getsizeof(msg_split[0]))
    # print(f"{commands.get(msg_split[0])} {msg_split[1]}")


async def read_packet(stream: INetStream) -> None:
    # get stream
    stream_obj = await stream.read()

    # handle_read_packet(stream_txt)

    # cast/get packet obj
    p = pickle.loads(stream_obj)

    print("Read stream: ", repr(p))

    # apply detection tech
    print('TEST: ', check_packet(p))
    # stats logger
    # close stream
    await stream.close()
    pass


async def write_packet(stream: INetStream, author: str) -> None:
    # write packet on stream
    result = handle_command(author)
    if result == 'empty':
        print('invalid command')
        await stream.close()
    else:
        await stream.write(pickle.dumps(result))  # check : xor bytes? + checksum


async def run(port: int, destination: str, seed: int = None) -> None:
    localhost_ip = "127.0.0.1"
    listen_addr = multiaddr.Multiaddr(f"/ip4/0.0.0.0/tcp/{port}")

    if seed:
        import random

        random.seed(seed)
        secret_number = random.getrandbits(32 * 8)
        secret = secret_number.to_bytes(length=32, byteorder="big")
    else:
        import secrets

        secret = secrets.token_bytes(32)

    host = new_host(key_pair=create_new_key_pair(secret))

    async with host.run(listen_addrs=[listen_addr]), trio.open_nursery() as nursery:

        print(f"I am {host.get_id().to_string()}")

        if not destination:  # its the server

            host.set_stream_handler(PROTOCOL_ID, read_packet)

            print(
                f"Run 'python3 main.py "
                f"-p {int(port) + 1} "
                f"-d /ip4/{localhost_ip}/tcp/{port}/p2p/{host.get_id().pretty()}' "
                "on another console."
            )
            print("Waiting for incoming connections...")
            await trio.sleep_forever()

        else:  # its the client
            maddr = multiaddr.Multiaddr(destination)
            info = info_from_p2p_addr(maddr)
            # Associate the peer with local ip address
            await host.connect(info)

            # Start a stream with the destination.
            # Multiaddress of the destination peer is fetched from the peerstore using 'peerId'.
            stream = await host.new_stream(info.peer_id, [PROTOCOL_ID])
            print(f"Connected to peer {info.addrs[0]}")

            await write_packet(stream=stream, author=f"/ip4/{localhost_ip}/tcp/{port}/p2p/{host.get_id().pretty()}'")


def main() -> None:
    description = """
    Mini network setup.'python ./chat -p <PORT>', where <PORT> is the port number.
    Then, run another host with 'python ./chat -p <ANOTHER_PORT> -d <DESTINATION>' to connect with this.
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
