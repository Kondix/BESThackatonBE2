from Reqs.BaseRequest import BaseRequest
from Reqs.TagKeeper import TagKeeper

class UpdateRoomRequest(BaseRequest):

    def Handle(self):
        rID = self.jsonToData.GetRoomID()
        specRoom = self.roomDbHandler.getSpecificRoomByIdx(rID)

        if specRoom != None:
            self.roomDbHandler.updateSpecificRoom(rID,
                                                  self.jsonToData.GetUsr(1),
                                                  self.jsonToData.GetUsr(2),
                                                  self.jsonToData.GetUsr(3),
                                                  self.jsonToData.GetUsr(4),
                                                  self.jsonToData.GetUsr(5))
            return "{\"ID\":\"UPDATE_ROOM_RESP\"}"
        else:
            self.roomDbHandler.addSpecificRoom(rID,
                                               self.jsonToData.GetUsr(1),
                                               self.jsonToData.GetUsr(2),
                                               self.jsonToData.GetUsr(3),
                                               self.jsonToData.GetUsr(4),
                                               self.jsonToData.GetUsr(5))
            return "{\"ID\":\"ADD_ROOM_RESP\"}"