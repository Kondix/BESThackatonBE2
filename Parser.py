import json
from Reqs.GetRequest import GetRequest
from Reqs.SpecificGetRequest import SpecificGetRequest
from Reqs.AddRequest import AddRequest
from Reqs.GetRoomRequest import GetRoomRequest
from Reqs.UpdateRoomRequest import UpdateRoomRequest
from Reqs.TagKeeper import TagKeeper


class Parser:

    def __init__(self, jsonData = None):
        self.request = jsonData
        self.tagKeeper = TagKeeper()
        self.jsonData = json.loads(jsonData)

    def Parse(self):
        tranObj = self.__GetTransactionObject()
        if tranObj is not None:
            return tranObj.Handle()
        return None

    def __GetTransactionObject(self):
        # TODO: convert to switch
        tranID = self.GetTransactionID(self.jsonData)
        if tranID == self.tagKeeper.tranAVL:
            return GetRequest(self.request)
        elif tranID == self.tagKeeper.tranSpecAVL:
            return SpecificGetRequest(self.request)
        elif tranID == self.tagKeeper.tranADD:
            return AddRequest(self.request)
        elif tranID == self.tagKeeper.tranRoomAVL:
            return GetRoomRequest(self.request)
        elif tranID == self.tagKeeper.tranRoomUPDATE:
            return UpdateRoomRequest(self.request)
        return None

    def GetTransactionID(self, item):
        return item[self.tagKeeper.tagID]
