#!/bin/sh
# shellcheck disable=SC2039
# shellcheck disable=SC2034
for i in {1..5} ; do
   python3 chat.py -p 8001 -d /ip4/127.0.0.1/tcp/8000/p2p/QmYpt7hKFUWTo2TqQtq5jwFJzH4XSfaiYn2gT58T6iLT36
done

