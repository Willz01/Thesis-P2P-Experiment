import argparse
import sys

import multiaddr
import trio

from model import content, packet

from libp2p import new_host
from libp2p.network.stream.net_stream_interface import INetStream
from libp2p.peer.peerinfo import info_from_p2p_addr
from libp2p.typing import TProtocol


def search():
    # get peers with searched content
    # check Hash table of flags
    # download from safest peer depending on flag variable
    pass


def read_packet(stream: INetStream):
    # get stream
    # cast/get packet obj
    # apply detection tech
    # stats logger
    # close stream
    pass


def write_packet(stream: INetStream):
    # write packet on stream
    # close stream
    pass


def run(port: int, destination: str):
    # runner
    pass


def main():
    pass
