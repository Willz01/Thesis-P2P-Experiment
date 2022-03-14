from datetime import datetime
from blake3 import blake3


class Packet:
    """
    @:param author - Sender
    @:param content - List of contents --> merge contents
    @:param timestamp - datetime packet was added to network
    """

    def __init__(self, data: [], descriptors: [], query: str):
        # self.author = author
        self.data = data  # serialize
        h = blake3()  # blake3
        h.update(data)
        self.cid = h.hexdigest()
        self.timestamp = datetime.now()
        self.descriptors = descriptors
        self.query = query
        self.size = len(data)

    def __repr__(self):
        return f""" 
        Size  : {self.size}, 
        Data  : {self.data},
        Descriptors : [{self.descriptors}],
        Query : {self.query},
        CID   : {self.cid},
        Timestamp : {self.timestamp}
         """
