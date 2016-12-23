from Dev.Reqs.TagKeeper import TagKeeper
from Dev.Reqs.BaseRequest import BaseRequest


class SpecificGetRequest(BaseRequest):

    def Handle(self):
        return self.__PrepareResponse(self.__GetSpecificRoomsFromDB())

    def __GetSpecificRoomsFromDB(self):
        return self.roomDbHandler.getRoomByTitle(self.jsonToData.GetDescr())

    def __PrepareResponse(self, roomsData):
        self.dataToJson.AddFieldByTag(self.tagKeeper.tagID, self.tagKeeper.tranSpecAVL + self.tagKeeper.tagResponse)
        self.dataToJson.AddFieldByTag(self.tagKeeper.tagCount, len(roomsData))
        self.dataToJson.AddFieldByTag(self.tagKeeper.tagRooms, self.__GetListOfRooms(roomsData))

        return self.dataToJson.ParseToJson()

    def __GetListOfRooms(self, roomsData):
        roomList = []
        for room in roomsData:
            roomList.append(self.dataToJson.CreateDict(TagKeeper.roomTags, room))
        return roomList

