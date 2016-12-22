from Conversion.JsonToData import JsonToData
from Conversion.DataToJson import DataToJson
from DataBaseHandler import RoomDataBaseHandler
from Reqs.TagKeeper import TagKeeper



class BaseRequest():

    def __init__(self, jsonToData):
        self.jsonToData = jsonToData
        self.dataToJson = DataToJson()
        self.roomDbHandler = RoomDataBaseHandler()
        self.tagKeeper = TagKeeper()
        self.maxQuerySize = 15

    def Handle(self):
        pass

