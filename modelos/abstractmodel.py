from abc import ABC

class abstractmodel(ABC):
    def __init__(self,data):
        setattr(self,data)
