from socket import *

HOST = "localhost"
PORT = 12345

s = socket(AF_INET, SOCK_STREAM)
s.connect((HOST, PORT))

print("Conectado ao servidor.")
print("Digite 'exit' para encerrar a comunicação.\n")

while True:
    msg = input("Digite uma frase para enviar ao servidor: ")
    s.send(msg.encode())

    if msg.lower() == "exit":
        print("Encerrando cliente...")
        break

    # recebe menu do servidor
    menu = s.recv(1024).decode()
    print(menu)

    # envia escolha
    opcao = input()
    s.send(opcao.encode())

    # recebe resposta
    resposta = s.recv(1024).decode()
    print("Resposta do servidor:", resposta, "\n")

s.close()

