from Conversion.JsonToData import JsonToData
from Conversion.DataToJson import DataToJson
from DataBaseHandler import RoomDataBaseHandler



class BaseRequest():

    def __init__(self, request):
        self.jsonToData = JsonToData(request)
        self.dataToJson = DataToJson()
        self.roomDbHandler = RoomDataBaseHandler()
        self.maxQuerySize = 15

    def Handle(self):
        pass

