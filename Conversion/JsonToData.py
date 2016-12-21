import json

class JsonToData():

    def __init__(self, request):
        self.__request = json.loads(request)

    def GetTransactionID(self):
        return self.__request["ID"]

    def GetDescr(self):
        return self.__request["descr"]