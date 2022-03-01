from datetime import datetime
from blake3 import blake3


class Content:
    """
    @:param content_name  - Name
    @:param data - data block
    @:param descriptors -  descriptor tags of content
    @:param content_type - Content type -> JSON, ZIP, MP3, MP4
    @:param created - date created
    @:param query - requesting query
    """

    def __init__(self, content_name: str, data: [], descriptors: [], query: str, content_type: str):
        self.content_name = content_name
        self.data = data  # serialize
        h = blake3()  # blake3
        h.update(data)
        self.cid = h.hexdigest()
        self.size = len(data)
        self.descriptors = descriptors
        self.query = query
        self.created = datetime.now()
        self.content_type = content_type

    def __repr__(self):
        return f"""
         Content-name : {self.content_name},
         Data : {self.data},
         CID : {self.cid},
         Descriptors : {self.descriptors},
         Query : {self.query},
         Content-type : {self.content_type},
         Created : {self.created}
         """
