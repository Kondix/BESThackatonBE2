import json

class JsonToData():

    def __init__(self, request):
        self.__request = json.loads(request)

    def GetTransactionID(self):
        return self.__request["ID"]

    def GetDescr(self):
        return self.__request["descr"]

    def GetRoomID(self):
        return self.__request["rID"]

    def GetTitle(self):
        return self.__request["title"]

    def GetHostID(self):
        return self.__request["hID"]

    def GetHostLvl(self):
        return self.__request["hLVL"]

    def GetMaxUsr(self):
        return self.__request["maxUsr"]

    def GetUsr(self, idx):
        return self.__request["user"+str(idx)]