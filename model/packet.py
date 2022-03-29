from datetime import datetime
from blake3 import blake3


class Packet:
    """
    @:param author - Sender
    @:param content - List of contents --> merge contents
    @:param timestamp - datetime packet was added to network
    """

    def __init__(self, data: [], author: str, descriptors: [], query: str, packet_name: str):
        # self.author = author
        self.data = data  # serialize
        h = blake3()  # blake3
        h.update(data)
        self.cid = h.hexdigest()
        self.author = author
        self.timestamp = datetime.now()
        self.descriptors = descriptors
        self.query = query
        self.size = len(data)
        self.packet_name = packet_name

    def __repr__(self):
        return f""" 
        Author : '{self.author}',
        Size  : {self.size}, 
        Data  : {self.data},
        Descriptors : [{self.descriptors}],
        Packet name : {self.packet_name},
        Query : {self.query},
        CID   : {self.cid},
        Timestamp : {self.timestamp}
         """
