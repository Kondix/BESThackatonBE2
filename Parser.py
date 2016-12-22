import json
from DataBaseHandler import RoomDataBaseHandler
from Reqs.GetRequest import GetRequest
from Reqs.SpecificGetRequest import SpecificGetRequest
from Reqs.AddRequest import AddRequest
from Reqs.GetRoomRequest import GetRoomRequest
from Reqs.UpdateRoomRequest import UpdateRoomRequest


class Parser:

    def __init__(self, jsonData = None):
        self.request = jsonData
        self.jsonData = json.loads(jsonData)
        self.roomDBHandler = RoomDataBaseHandler()
        self.maxQuerySize = 150

    def Parse(self):
        tranObj = self.__GetTransactionObject()
        if tranObj is not None:
            return tranObj.Handle()
        return None

    def __GetTransactionObject(self):
        # TODO: convert to switch
        if self.GetTransactionID(self.jsonData) == "AVL":
            return GetRequest(self.request)
        if self.GetTransactionID(self.jsonData) == "SPEC_AVL":
            return SpecificGetRequest(self.request)
        if self.GetTransactionID(self.jsonData) == "ADD":
            return AddRequest(self.request)
        if self.GetTransactionID(self.jsonData) == "AVL_ROOM":
            return GetRoomRequest(self.request)
        if self.GetTransactionID(self.jsonData) == "UPDATE_ROOM":
            return UpdateRoomRequest(self.request)
        return None


    def GetTransactionID(self, item):
        return item["ID"]
