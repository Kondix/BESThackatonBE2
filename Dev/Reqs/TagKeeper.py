class TagKeeper:

    #Transactions:
    tranAVL = "AVL"
    tranSpecAVL = "SPEC_AVL"
    tranADD = "ADD"
    tranRoomAVL = "AVL_ROOM"
    tranRoomUPDATE = "UPDATE_ROOM"

    #JSON tags:
    tagID = "ID"
    tagRoomID = "rID"
    tagHostID = "hID"
    tagTitle = "title"
    tagHostLvl = "hLVL"
    tagDescr = "descr"
    tagMaxUsers = "maxUsr"
    tagUser = "user"

    tagCount = "COUNT"
    tagRooms = "ROOMS"

    #Common tags:
    tagError = "Error"
    tagResponse = "_RESPONSE"

    roomTags = [tagRoomID, tagTitle, tagHostID, tagHostLvl, tagDescr, tagMaxUsers]
    # TODO: convert to dynamic table
    roomAvlTags = [tagRoomID, "user1", "user2", "user3", "user4", "user5"]
    # TODO: add strings as variables