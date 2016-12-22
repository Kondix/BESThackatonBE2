import json
from DataBaseHandler import RoomDataBaseHandler
from Reqs.GetRequest import GetRequest
from Reqs.SpecificGetRequest import SpecificGetRequest
from Reqs.AddRequest import AddRequest

class Parser:

    def __init__(self, jsonData = None):
        self.request = jsonData
        self.jsonData = json.loads(jsonData)
        self.roomDBHandler = RoomDataBaseHandler()
        self.maxQuerySize = 150
        self.rooms = []
        self.GetAllRooms()
        self.roomCnt = len(self.rooms)+1

    def Parse(self):
        tranObj = self.__GetTransactionObject()
        if tranObj is not None:
            return tranObj.Handle()
        elif self.GetTransactionID(self.jsonData) == "UPDATE_ROOM":
            return self.HandleUpdateRoom()
        elif self.GetTransactionID(self.jsonData) == "AVL_ROOM":
            return self.HandleAvlRoom()
        return None

    def __GetTransactionObject(self):
        # TODO: convert to switch
        if self.GetTransactionID(self.jsonData) == "AVL":
            return GetRequest(self.request)
        if self.GetTransactionID(self.jsonData) == "SPEC_AVL":
            return SpecificGetRequest(self.request)
        if self.GetTransactionID(self.jsonData) == "ADD":
            return AddRequest(self.request)
        return None

    def HandleAvlRoom(self):
        rID = self.GetRoomID(self.jsonData)
        specRoom = self.roomDBHandler.getSpecificRoomByIdx(rID)
        if specRoom != None:
            self.PrepareRoomAvlResponse(specRoom)
        else:
            return "{\"ID\":\"AVL_ROOM_ERROR\"}"

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

    def PrepareRoomAvlResponse(self, specRoom):

        return json.dumps([{"ID": "ROOM_AVL_RESP", "rID" : specRoom[0], "user1" : specRoom[1],
                               "user2": specRoom[2],"user3": specRoom[3], "user4": specRoom[4],
                               "user5": specRoom[5]}], separators=(',', ':'))

    def GetAllRooms(self):
        for idx in range(1, self.maxQuerySize):
            if self.roomDBHandler.getRoomByIdx(idx) == None:
                break
            self.rooms.append(self.roomDBHandler.getRoomByIdx(idx))

    def GetTransactionID(self, item):
        return item["ID"]

    def GetRoomID(self, item):
        return item["rID"]

    def GetTitle(self, item):
        return item["title"]

    def GetHostID(self, item):
        return item["hID"]

    def GetHostLvl(self, item):
        return item["hLVL"]

    def GetDescr(self, item):
        return item["descr"]

    def GetMaxUsr(self, item):
        return item["maxUsr"]

    def GetUsr(self, item, idx):
        return item["user"+str(idx)]
