import json

from Dev.Reqs.TagKeeper import TagKeeper


class JsonToData():

    def __init__(self, request):
        self.__tagKeeper = TagKeeper()
        self.__request = json.loads(request)

    def GetValueByTag(self, tag):
        return self.__request[tag]

    #TODO: get rid of GetUsr
    def GetUsr(self, idx):
        return self.__request[self.__tagKeeper.tagUser+str(idx)]