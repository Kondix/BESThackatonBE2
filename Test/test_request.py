from Dev.Reqs.GetRequest import GetRequest
from Dev.Conversion.JsonToData import JsonToData
from Dev.Conversion.DataToJson import DataToJson
from Dev.Reqs.TagKeeper import TagKeeper
import unittest


class RequestTest(unittest.TestCase):

    def test_basicGetRequest(self):
        dataToJson = DataToJson()
        dataToJson.AddFieldByTag(TagKeeper.tagID, TagKeeper.tranAVL)
        msg = dataToJson.ParseToJson()
        jsonToData = JsonToData(msg)
        getRequest = GetRequest(jsonToData)
        responseID = JsonToData(getRequest.Handle()).GetValueByTag(TagKeeper.tagID)

        self.assertEquals(responseID, TagKeeper.tranAVL + TagKeeper.tagResponse)
