from Reqs.BaseRequest import BaseRequest
from Reqs.TagKeeper import TagKeeper

class GetRequest(BaseRequest):

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
        self.dataToJson.AddFieldByTag(self.tagKeeper.tagID, self.tagKeeper.tranAVL + self.tagKeeper.tagResponse)
        self.dataToJson.AddFieldByTag(self.tagKeeper.tagCount, len(roomsData))
        self.dataToJson.AddFieldByTag(self.tagKeeper.tagRooms, self.__GetListOfRooms(roomsData))

        return self.dataToJson.ParseToJson()

    def __GetListOfRooms(self, roomsData):
        roomList = []
        for room in roomsData:
            roomList.append(self.dataToJson.CreateDict(TagKeeper.roomTags, room))
        return roomList
