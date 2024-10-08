import hashlib
from databases.MongoHandler import MongoHandler
from databases.entities import login, message  # Importa as classes Login e Message
from databases.MongoHandler import MongoHandler  # Importa a classe MongoHandler


# Função para criptografar a mensagem
def criptografar_mensagem(mensagem):
    return hashlib.sha256(mensagem.encode()).hexdigest()


# Função para o menu de login
def menu_login(handler):
    print("=== Bem-vindo ao sistema de login ===")

    email = input("Digite seu e-mail: ")
    password = input("Digite sua senha: ")

    # Cria um Login
    usuario = login(email=email, password=password)

    # Chama para verificar se as credenciais estão corretas
    auth = handler.authenticate(email=usuario.email, password=usuario.password)

    if auth:
        print("Login bem-sucedido!")
        return usuario.email
    else:
        print("Falha no login. E-mail ou senha incorretos.")
        return None


# Função para enviar uma mensagem
def enviar_mensagem(handler, remetente):
    destinatario = input("Digite o nickname do destinatário: ")
    conteudo = input("Digite a mensagem: ")

    # Criptografa a mensagem antes de armazenar
    conteudo_criptografado = criptografar_mensagem(conteudo)

    # Cria um objeto Message e adiciona ao banco
    mensagem = message(nickname_from=remetente, nickname_to=destinatario, content=conteudo_criptografado)
    handler.add_new_message(mensagem)  # Adiciona a nova mensagem ao banco
    print("Mensagem enviada com sucesso!")


# Função para receber mensagens
def receber_mensagens(handler, nickname):
    mensagens = handler.get_messages(nickname)  # Recupera mensagens do banco
    if mensagens:
        print("Mensagens recebidas:")
        for msg in mensagens:
            print(f"{msg['nickname_from']} -> {msg['nickname_to']}: {msg['content']}")
    else:
        print("Nenhuma mensagem encontrada.")


# Função principal do menu
def menu_principal(handler, remetente):
    while True:
        print("\n-- Menu Principal --")
        print("1. Enviar Mensagem")
        print("2. Receber Mensagens")
        print("3. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            enviar_mensagem(handler, remetente)
        elif opcao == "2":
            receber_mensagens(handler, remetente)
        elif opcao == "3":
            print("Saindo do sistema...")
            break
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == '__main__':
    handler = MongoHandler()

    # Chama o menu de login
    sucesso_login = menu_login(handler)

    if sucesso_login:
        nickname = input("Digite seu nickname: ")  # Obtém o nickname do usuário que está logado
        menu_principal(handler, nickname)
    else:
        print("Tente novamente mais tarde.")