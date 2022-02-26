from datetime import datetime
from hashlib import blake2b


class Content:
    """
    @:param content_name  - Name
    @:param data - data block
    @:param descriptors -  descriptor tags of content
    @:param content_type - Content type -> JSON, ZIP, MP3, MP4
    @:param created - date created
    @:param query - requesting query
    """

    def __init__(self, content_name: str, data: [], descriptors: [], query: str, created: datetime, content_type: str):
        self.content_name = content_name
        self.data = data
        h = blake2b()
        h.update(data)
        self.cid = h.hexdigest()
        self.size = len(data)
        self.descriptors = descriptors
        self.query = query
        self.created = datetime.now()
        self.content_type = content_type
