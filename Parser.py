import json
from DataBaseHandler import RoomDataBaseHandler
from Reqs.GetRequest import GetRequest
from Reqs.SpecificGetRequest import SpecificGetRequest
from Reqs.AddRequest import AddRequest
from Reqs.GetRoomRequest import GetRoomRequest

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
        elif self.GetTransactionID(self.jsonData) == "UPDATE_ROOM":
            return self.HandleUpdateRoom()
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
        return None

    def HandleUpdateRoom(self):
        rID = self.GetRoomID(self.jsonData)
        specRoom = self.roomDBHandler.getSpecificRoomByIdx(rID)
        if specRoom != None:
            self.roomDBHandler.updateSpecificRoom(rID, self.GetUsr(self.jsonData, 1), self.GetUsr(self.jsonData, 2),
                                               self.GetUsr(self.jsonData, 3), self.GetUsr(self.jsonData, 4),
                                               self.GetUsr(self.jsonData, 5))
            return "{\"ID\":\"UPDATE_ROOM_RESP\"}"
        else:
            self.roomDBHandler.addSpecificRoom(rID, self.GetUsr(self.jsonData, 1), self.GetUsr(self.jsonData, 2), self.GetUsr(self.jsonData, 3), self.GetUsr(self.jsonData, 4), self.GetUsr(self.jsonData, 5))
            return "{\"ID\":\"ADD_ROOM_RESP\"}"


    def GetTransactionID(self, item):
        return item["ID"]

    def GetRoomID(self, item):
        return item["rID"]
