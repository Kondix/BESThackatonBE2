from Reqs.BaseRequest import BaseRequest


class GetRequest(BaseRequest):

    roomTags = ["rId", "title", "hID", "hLVL", "descr", "maxUsr"]

    def Handle(self):
        return self.__PrepareResponse(self.__GetFromDB())


    def __GetFromDB(self):

        roomsData = []
        for idx in range(1, self.maxQuerySize):
            foundRoom = self.roomDbHandler.getRoomByIdx(idx)
            if foundRoom is None:
                break
            roomsData.append(foundRoom)
        return roomsData

    def __PrepareResponse(self, roomsData):

        roomList = []
        for room in roomsData:
            roomList.append(self.dataToJson.CreateDict(GetRequest.roomTags, room))

        self.dataToJson.AddFieldByTag("ID", "AVL_RESP")
        self.dataToJson.AddFieldByTag("COUNT", len(roomsData))
        self.dataToJson.AddFieldByTag("ROOMS", roomList)

        return self.dataToJson.ParseToJson()
