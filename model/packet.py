import content


class Packet:
    """
    @:param author - Sender
    @:param content - List of contents --> merge contents
    @:param timestamp - datetime packet was added to network
    """

    def __init__(self, author: str, c: content, timestamp: str):
        self.author = author
        self.content = c  # content
        self.timestamp = timestamp
