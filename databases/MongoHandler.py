from pymongo import MongoClient

class MongoHandler:
    def __init__(self):
        self.client = MongoClient(
        "mongodb+srv://emillyfbo:arrozbom30@consultas.wsqcv.mongodb.net/?retryWrites=true&w=majority&appName=Consultas")  # Coloque sua string de conexão aqui

    def connect(self, db_name):
        return self.client[db_name]

    def authenticate(self, email, password):
        db = self.connect("ChatPython")
        login = db.login.find_one({"email": email, "password": password})
        return login is not None

    def add_new_message(self, message):
        db = self.connect("ChatPython")
        db.messages.insert_one({
            "nickname_from": message.nickname_from,
            "nickname_to": message.nickname_to,
            "content": message.content  # Aqui a mensagem já está criptografada
        })

    def get_messages(self, nickname):
        db = self.connect("ChatPython")
        return list(db.messages.find({"nickname_to": nickname}))


