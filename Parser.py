from Reqs.GetRequest import GetRequest
from Reqs.SpecificGetRequest import SpecificGetRequest
from Reqs.AddRequest import AddRequest
from Reqs.GetRoomRequest import GetRoomRequest
from Reqs.UpdateRoomRequest import UpdateRoomRequest
from Reqs.TagKeeper import TagKeeper
from Conversion.JsonToData import JsonToData


class Parser:

    def __init__(self, jsonData = None):
        self.jsonToData = JsonToData(jsonData)
        self.tagKeeper = TagKeeper()

    def Parse(self):
        tranObj = self.__GetTransactionObject()
        if tranObj is not None:
            return tranObj.Handle()
        return None

    def __GetTransactionObject(self):
        # TODO: convert to switch
        tranID = self.jsonToData.GetTransactionID()
        if tranID == self.tagKeeper.tranAVL:
            return GetRequest(self.jsonToData)
        elif tranID == self.tagKeeper.tranSpecAVL:
            return SpecificGetRequest(self.jsonToData)
        elif tranID == self.tagKeeper.tranADD:
            return AddRequest(self.jsonToData)
        elif tranID == self.tagKeeper.tranRoomAVL:
            return GetRoomRequest(self.jsonToData)
        elif tranID == self.tagKeeper.tranRoomUPDATE:
            return UpdateRoomRequest(self.jsonToData)
        return None
