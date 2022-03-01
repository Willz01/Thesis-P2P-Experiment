from model.content import Content


class Packet:
    """
    @:param author - Sender
    @:param content - List of contents --> merge contents
    @:param timestamp - datetime packet was added to network
    """

    def __init__(self, author: str, c: Content, timestamp: str):
        self.author = author
        self.content = c  # content
        self.timestamp = timestamp

    def __repr__(self):
        return f""" 
        Author  : {self.author}, 
        Content : [{self.content}],
        TimeStamp : {self.timestamp}
         """
