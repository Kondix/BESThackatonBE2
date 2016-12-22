from Reqs.BaseRequest import BaseRequest
from Reqs.TagKeeper import TagKeeper

class GetRoomRequest(BaseRequest):

    def Handle(self):
        rID = self.jsonToData.GetRoomID()
        specRoom = self.roomDbHandler.getSpecificRoomByIdx(rID)
        if specRoom == None:
            return "{\"ID\":\"AVL_ROOM_ERROR\"}"
        return self.PrepareRoomAvlResponse(specRoom)

    def PrepareRoomAvlResponse(self, specRoom):

        self.dataToJson.AddFieldByTag("ID", "AVL_ROOM_RESP")
        for idx in range(len(TagKeeper.roomAvlTags)):
            self.dataToJson.AddFieldByTag(TagKeeper.roomAvlTags[idx], specRoom[idx])

        return self.dataToJson.ParseToJson()
