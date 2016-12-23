import json

class DataToJson():

    def __init__(self):
        self.__dataDict = {}

    def AddFieldByTag(self, tag, value):
        self.__dataDict[tag] = value

    def CreateDict(self, tags, values):

        tempDict = {}
        if len(tags) != len(values):
            return None

        for idx in range(len(tags)):
            tempDict[tags[idx]] = values[idx]

        return tempDict

    def ParseToJson(self):
        return json.dumps(self.__dataDict, separators=(',', ':'))