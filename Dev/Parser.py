from Dev.Reqs.AddRequest import AddRequest
from Dev.Reqs.GetRequest import GetRequest
from Dev.Reqs.GetRoomRequest import GetRoomRequest
from Dev.Reqs.SpecificGetRequest import SpecificGetRequest
from Dev.Reqs.UpdateRoomRequest import UpdateRoomRequest
from Dev.Conversion.JsonToData import JsonToData
from Dev.Reqs.TagKeeper import TagKeeper


class Parser:

    def __init__(self, jsonData):
        self.jsonToData = JsonToData(jsonData)
        self.tagKeeper = TagKeeper()

    def Parse(self):
        tranObj = self.__GetTransactionObject()
        if tranObj is not None:
            return tranObj.Handle()
        return None

    def __GetTransactionObject(self):
        # TODO: convert to switch
        tranID = self.jsonToData.GetValueByTag(self.tagKeeper.tagID)
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
