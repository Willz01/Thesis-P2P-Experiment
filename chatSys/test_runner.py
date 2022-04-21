import subprocess

import os
import sys

script = '../chatSys/chatSys.py'


def spin_nodes() -> None:
    print(os.environ.get('nodeCon'))


if __name__ == '__main__':
    spin_nodes()
