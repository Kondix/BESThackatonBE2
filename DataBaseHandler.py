import MySQLdb


class RoomDataBaseHandler:
    def __init__(self):
        self.db = MySQLdb.connect("localhost", "root", "admin", "roomDB")
        self.cursor = self.db.cursor()

    def addRoom(self, rID, title, hostID, hostLvl, descr):
        self.cursor.execute("INSERT INTO Rooms (roomID, title, hostID, hostLvl, descr) VALUES (%s, %s, %s, %s, %s);", [rID, title, hostID, hostLvl, descr])
        self.db.commit()

    def getRoomByIdx(self, idx):
        self.cursor.execute("SELECT * FROM Rooms WHERE roomID = %s", [idx])
        room = self.cursor.fetchone()
        return room

    def getRoomByTitle(self, title):
        self.cursor.execute("SELECT * FROM Rooms WHERE title LIKE %s ", [title])
        room = self.cursor.fetchone()
        return room

    def __del__(self):
        # disconnect from server
        self.db.close()
