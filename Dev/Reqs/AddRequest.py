from Dev.Reqs.BaseRequest import BaseRequest


class AddRequest(BaseRequest):

    def Handle(self):
        return self.__AddToDb()


    def __AddToDb(self):
        title = self.jsonToData.GetValueByTag(self.tagKeeper.tagTitle)
        hID = self.jsonToData.GetValueByTag(self.tagKeeper.tagHostID)
        hLVL = self.jsonToData.GetValueByTag(self.tagKeeper.tagHostLvl)
        descr = self.jsonToData.GetValueByTag(self.tagKeeper.tagDescr)
        maxUsr = self.jsonToData.GetValueByTag(self.tagKeeper.tagMaxUsers)

        if self.roomDbHandler.getSimilarRecord(title, hID) != None:
            return "{\"ID\":\"ADD_RESP_ERROR_ALREADY_IN_BASE\"}"
        else:
            self.roomDbHandler.addRoom(title, hID, hLVL, descr, maxUsr)
        return "{\"ID\":\"ADD_RESP\"}"

