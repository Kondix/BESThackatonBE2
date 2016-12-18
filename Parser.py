import json
from DataBaseHandler import RoomDataBaseHandler

class Parser:

    def __init__(self, jsonData = None):
        self.jsonData = json.loads(jsonData)
        self.roomDBHandler = RoomDataBaseHandler()
        self.maxQuerySize = 150
        self.rooms = []
        self.GetAllRooms()
        self.roomCnt = len(self.rooms)+1

    def Parse(self):
        if self.GetTransactionID(self.jsonData) == "AVL":
            return self.HandleAvl()
        if self.GetTransactionID(self.jsonData) == "SPEC_AVL":
            return self.HandleSpecAvl(self.GetDescr(self.jsonData))
        if self.GetTransactionID(self.jsonData) == "ADD":
            return self.HandleAdd()
        return None

    def HandleAvl(self):
        self.GetAllRooms()
        return self.PrepareAvlResponse()

    def HandleSpecAvl(self, descr):
        self.GetAllRoomsWhere(descr)
        return self.PrepareAvlResponse()

    def HandleAdd(self):
        #rID = self.GetRoomID(dict(self.jsonData["ROOMS"][0]))
        rID = self.roomCnt
        title = self.GetTitle(dict(self.jsonData["ROOMS"][0]))
        hID = self.GetHostID(dict(self.jsonData["ROOMS"][0]))
        hLVL = self.GetHostLvl(dict(self.jsonData["ROOMS"][0]))
        descr = self.GetDescr(dict(self.jsonData["ROOMS"][0]))
        maxUsr = self.GetMaxUsr(dict(self.jsonData["ROOMS"][0]))
        if self.roomDBHandler.getSimilarRecord(title, hID) != None:
            return "{\"ID\":\"ADD_RESP_ERROR_ALREADY_IN_BASE\"}"
        else:
            self.roomDBHandler.addRoom(rID, title, hID, hLVL, descr, maxUsr)
            self.roomCnt += 1
            return "{\"ID\":\"ADD_RESP\"}"


    def GetAllRooms(self):
        for idx in range(1, self.maxQuerySize):
            if self.roomDBHandler.getRoomByIdx(idx) == None:
                break
            self.rooms.append(self.roomDBHandler.getRoomByIdx(idx))

    def GetAllRoomsWhere(self, descr):
        print(descr)
        self.rooms.append(self.roomDBHandler.getRoomByTitle(descr))

    def PrepareAvlResponse(self):
        roomsTable = []
        roomSize = len(self.rooms)
        for i in range (0, roomSize):
            roomsTable.append({"rID" : self.rooms[i][0],
                               "title" : self.rooms[i][1],
                               "hID": self.rooms[i][2],
                               "hLVL": self.rooms[i][3],
                               "descr": self.rooms[i][4],
                               "maxUsr": self.rooms[i][5]
                               })

        return json.dumps([{"ID": "AVL_RESP", "COUNT": roomSize, "ROOMS": roomsTable}], separators=(',', ':'))

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
