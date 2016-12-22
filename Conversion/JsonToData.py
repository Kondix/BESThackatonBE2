import json
from Reqs.TagKeeper import TagKeeper

class JsonToData():

    def __init__(self, request):
        self.__tagKeeper = TagKeeper()
        self.__request = json.loads(request)

    #TODO: change to GetValueByTag
    def GetTransactionID(self):
        return self.__request[self.__tagKeeper.tagID]

    def GetDescr(self):
        return self.__request[self.__tagKeeper.tagDescr]

    def GetRoomID(self):
        return self.__request[self.__tagKeeper.tagRoomID]

    def GetTitle(self):
        return self.__request[self.__tagKeeper.tagTitle]

    def GetHostID(self):
        return self.__request[self.__tagKeeper.tagHostID]

    def GetHostLvl(self):
        return self.__request[self.__tagKeeper.tagHostLvl]

    def GetMaxUsr(self):
        return self.__request[self.__tagKeeper.tagMaxUsers]

    def GetUsr(self, idx):
        return self.__request[self.__tagKeeper.tagUser+str(idx)]