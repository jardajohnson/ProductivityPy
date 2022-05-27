import pymongo

DATABASE = 'productivity_py'

# ! Connects to MongoDB Client and assigns connection to variable
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

# ! Connects to 'productivity' database and assigns to variable
db = myclient[DATABASE]
