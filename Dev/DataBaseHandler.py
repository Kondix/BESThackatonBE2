import MySQLdb


class RoomDataBaseHandler:
    def __init__(self):
        self.db = MySQLdb.connect("localhost", "root", "root", "roomDB")
        self.cursor = self.db.cursor()

    def addRoom(self, title, hostID, hostLvl, descr, maxUsr):
        self.cursor.execute("INSERT INTO Rooms (title, hostID, hostLvl, descr, maxUsr) VALUES (%s, %s, %s, %s, %s);", [title, hostID, hostLvl, descr, str(maxUsr)])
        self.db.commit()

    def getRoomByIdx(self, idx):
        self.cursor.execute("SELECT * FROM Rooms WHERE roomID = %s", [idx])
        room = self.cursor.fetchone()
        return room

    def getSimilarRecord(self, title, hostID):
        self.cursor.execute("SELECT * FROM Rooms WHERE title = %s and hostID = %s", [title, hostID])
        return self.cursor.fetchone()

    def getSimilarRecordHostIdx(self, rID):
        self.cursor.execute("SELECT * FROM Rooms WHERE roomID = %s", [str(rID)])
        return self.cursor.fetchone()

    def getRoomByTitle(self, title):
        self.cursor.execute("SELECT * FROM Rooms WHERE descr LIKE %s ", ["%" + title + "%"])
        rooms = self.cursor.fetchall()
        return rooms

    def getSpecificRoomByIdx(self, rID):
        self.cursor.execute("SELECT * FROM SpecRooms WHERE roomID = %s", [str(rID)])
        return self.cursor.fetchone()

    def addSpecificRoom(self, rID, user1 = 0, user2 = 0, user3 = 0, user4 = 0, user5 = 0):
        self.cursor.execute("INSERT INTO SpecRooms (roomID, user1, user2, user3, user4, user5) VALUES (%s, %s, %s, %s, %s, %s);", [str(rID), str(user1), str(user2), str(user3), str(user4), str(user5)])
        self.db.commit()

    def updateSpecificRoom(self, rID, user1 = 0, user2 = 0, user3 = 0, user4 = 0, user5 = 0):
        self.cursor.execute("UPDATE SpecRooms SET user1 = %s, user2 = %s, user3 = %s, user4 = %s, user5 = %s WHERE roomID = %s;", [str(user1), str(user2), str(user3), str(user4), str(user5), str(rID)])
        self.db.commit()

    def __del__(self):
        # disconnect from server
        self.db.close()
