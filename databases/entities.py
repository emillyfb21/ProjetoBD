class login:
    def __init__(self, email: str, password: str):
        self.email = email
        self.password = password


class message:
    def __init__(self, nickname_from: str, nickname_to: str, content: str):
        self.nickname_from = nickname_from
        self.nickname_to = nickname_to
        self.content = content

