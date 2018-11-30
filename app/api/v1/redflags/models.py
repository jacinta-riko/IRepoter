class DB():
    """initialize an empty dictionary"""
    def __init__(self):
        self.db = [{}]
redflags = DB()

 class Incident():
     def __init__(self, createdOn, createdBy,type,location,status, images,videos, title, comment):
         self.id = id,
         self.createdOn = createdOn,
         self.createdBy = createdBy,
         self.type = type,
         self.location = location,
         self.status = status,
         self.images = images,
         self.videos = videos,
         self.title = title,
         self.comment = comment,

    def save (self):
        self.id = len(incidents) + 1
        self.redflags.append(incidents)
        return.self.redflags

    

    

