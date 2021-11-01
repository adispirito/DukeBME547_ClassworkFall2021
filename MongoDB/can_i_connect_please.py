from pymodm import connect, MongoModel, fields

URL = "mongodb+srv://ad424:4lm9DHHOKRWUSdgj@bme547.3vytl.mongodb.net/TestDB?retryWrites=true&w=majority"
connect(URL)

class User(MongoModel):
    name = fields.CharField()

x = User(name = "David")
x.save()
