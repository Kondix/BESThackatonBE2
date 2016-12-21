from Reqs.BaseRequest import BaseRequest
from Reqs.TagKeeper import TagKeeper


class SpecificGetRequest(BaseRequest):

    def Handle(self):
        return self.__PrepareResponse(self.__GetSpecificRoomsFromDB())

    def __GetSpecificRoomsFromDB(self):
        return self.roomDbHandler.getRoomByTitle(self.jsonToData.GetDescr())

    def __PrepareResponse(self, roomsData):
        self.dataToJson.AddFieldByTag("ID", "AVL_SPEC_RESP")
        self.dataToJson.AddFieldByTag("COUNT", len(roomsData))
        self.dataToJson.AddFieldByTag("ROOMS", self.__GetListOfRooms(roomsData))

        return self.dataToJson.ParseToJson()

    def __GetListOfRooms(self, roomsData):
        roomList = []
        for room in roomsData:
            roomList.append(self.dataToJson.CreateDict(TagKeeper.roomTags, room))
        return roomList

