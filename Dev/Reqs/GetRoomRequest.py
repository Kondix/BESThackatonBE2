from Dev.Reqs.TagKeeper import TagKeeper
from Dev.Reqs.BaseRequest import BaseRequest


class GetRoomRequest(BaseRequest):

    def Handle(self):
        rID = self.jsonToData.GetValueByTag(self.tagKeeper.tagRoomID)
        specRoom = self.roomDbHandler.getSpecificRoomByIdx(rID)
        if specRoom == None:
            return "{\"ID\":\"AVL_ROOM_ERROR\"}"
        return self.PrepareRoomAvlResponse(specRoom)

    def PrepareRoomAvlResponse(self, specRoom):

        self.dataToJson.AddFieldByTag(self.tagKeeper.tagID, self.tagKeeper.tranRoomAVL + self.tagKeeper.tagResponse)
        for idx in range(len(TagKeeper.roomAvlTags)):
            self.dataToJson.AddFieldByTag(TagKeeper.roomAvlTags[idx], specRoom[idx])

        return self.dataToJson.ParseToJson()
