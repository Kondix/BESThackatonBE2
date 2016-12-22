from Reqs.BaseRequest import BaseRequest


class AddRequest(BaseRequest):

    def Handle(self):
        return self.__AddToDb()


    def __AddToDb(self):
        title = self.jsonToData.GetTitle()
        hID = self.jsonToData.GetHostID()
        hLVL = self.jsonToData.GetHostLvl()
        descr = self.jsonToData.GetDescr()
        maxUsr = self.jsonToData.GetMaxUsr()

        if self.roomDbHandler.getSimilarRecord(title, hID) != None:
            return "{\"ID\":\"ADD_RESP_ERROR_ALREADY_IN_BASE\"}"
        else:
            self.roomDbHandler.addRoom(title, hID, hLVL, descr, maxUsr)
        return "{\"ID\":\"ADD_RESP\"}"

