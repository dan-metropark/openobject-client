import pythoncom

class DataIStream:
    """Simple implementation of COM IStream.
    """
    _public_methods_ = [ 'Read', 'Write', 'Seek' ]
    _com_interfaces_ = [ pythoncom.IID_IStream ]

    def __init__(self, data):
        self.data = data
        self.index = 0

    def Read(self, amount):
        result = self.data[self.index : self.index + amount]
        self.index = self.index + amount
        return result

    def Write(self, data):
        self.data = data
        self.index = 0
        return len(data)

    def Seek(self, dist, origin):
        if origin==pythoncom.STREAM_SEEK_SET:
            self.index = dist
        elif origin==pythoncom.STREAM_SEEK_CUR:
            self.index = self.index + dist
        elif origin==pythoncom.STREAM_SEEK_END:
            self.index = len(self.data)+dist
        else:
            raise ValueError, 'Unknown Seek type: ' +str(origin)
        if self.index < 0:
            self.index = 0
        else:
            self.index = min(self.index, len(self.data))
        return self.index                        