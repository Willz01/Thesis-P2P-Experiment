import subprocess

from chat import main
import os
import sys

script = '../chatSys/chatSys.py'


def spin_nodes() -> None:
    os.popen(
        'python3 chat.py -p 8001 -d /ip4/127.0.0.1/tcp/8000/p2p/QmZ7VNWEVZfeoN44xnQ1qEUmvF9UuuxpujjqzQ9GcQKBg6')


if __name__ == '__main__':
    spin_nodes()
