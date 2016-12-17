import json
from DataBaseHandler import RoomDataBaseHandler

class Parser:
    def __init__(self, jsonData = None):
        self.jsonData = json.loads(jsonData)
        self.roomDBHandler = RoomDataBaseHandler()
        self.maxQuerySize = 5
        self.rooms = []

    def Parse(self):
        if self.GetTransactionID() == "AVL":
            return self.HandleAvl()
        if self.GetTransactionID() == "ADD":
            return self.HandleAdd()
        return None

    def HandleAvl(self):
        self.GetAllRooms()
        return self.PrepareAvlResponse()

    def HandleAdd(self):
        rID = self.getRoomID()
        title = self.GetTitle()
        hID = self.GetHostID()
        hLVL = self.GetHostLvl()
        descr = self.GetDescr()
        self.roomDBHandler.addRoom(rID, title, hID, hLVL, descr)

    def GetAllRooms(self):
        for idx in range(1, self.maxQuerySize):
            if self.roomDBHandler.getRoomByIdx(idx) == None:
                break
            self.rooms.append(self.roomDBHandler.getRoomByIdx(idx))

    def PrepareAvlResponse(self):
        roomsTable = []
        roomSize = len(self.rooms)
        for i in range (0, roomSize):
            roomsTable.append({"rID" : self.rooms[i][0],
                               "title" : self.rooms[i][1],
                               "hID": self.rooms[i][2],
                               "hLVL": self.rooms[i][3],
                               "descr": self.rooms[i][4]
                               })

        return json.dumps([{"ID": "AVL_RESP", "COUNT": roomSize, "ROOMS": roomsTable}], separators=(',', ':'))

    def GetTransactionID(self):
        return self.jsonData["ID"]

    def GetRoomID(self):
        return self.jsonData["rID"]

    def GetTitle(self):
        return self.jsonData["title"]

    def GetHostID(self):
        return self.jsonData["hID"]

    def GetHostLvl(self):
        return self.jsonData["hLVL"]

    def GetDescr(self):
        return self.jsonData["descr"]
