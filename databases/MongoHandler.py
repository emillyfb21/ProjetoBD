from pymongo import MongoClient

class MongoHandler:
    def __init__(self):
        self.client = MongoClient("mongodb+srv://emillyfbo:<arrozbom30>@consultas.wsqcv.mongodb.net/?retryWrites=true&w=majority&appName=Consultas")

    def connect(self, dabase_name):
        return self.client[dabase_name]
    def authenticate(self, email, password):
        db=self.connect("chat")
        user = db.users.find_one({"email": email, "password": password})
        if user:
            return True
        else:
            return False
