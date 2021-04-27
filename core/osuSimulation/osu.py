
class osu(object):

    """
    版本号（VER）、支路端口号（TPN）、帧类型（FT）

    """

    def __init__(self,VER,TPN,FT,PB):
        self.VER = VER
        self.TPN = TPN
        self.FT = FT
        self.PB = PB

    def  bandwidthIncrease(self):
        pass

    def bandwidthReduction(self):
        pass

    def bandwidthFallback(self):
        pass

    pass


class PB(object):

    def __init__(self,TPN,bandwidth,OSUflex):
        self.TPN = TPN
        self.bandwidth = bandwidth
        self.OSUflex = OSUflex
    pass