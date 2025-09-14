from socket import *

HOST = "localhost"
PORT = 12345

s = socket(AF_INET, SOCK_STREAM)
s.bind((HOST, PORT))
s.listen(1)

print(f"Servidor rodando em {HOST}:{PORT}...")

(conn, addr) = s.accept()
print("Conectado por", addr)

while True:
    data = conn.recv(1024)  # recebe mensagem
    if not data:
        break

    frase = data.decode().strip()
    if frase.lower() == "exit":  # cliente pediu para encerrar
        print("Encerrando conexão com o cliente.")
        break

    print(f"Mensagem recebida: {frase}")

    # envia menu de opções
    menu = (
        "\nEscolha um serviço:\n"
        "1 - Converter para MAIÚSCULAS\n"
        "2 - Concatenar palavras (remover espaços)\n"
        "3 - Contar número de letras\n"
        "Digite a opção: "
    )
    conn.send(menu.encode())

    # recebe escolha do cliente
    opcao = conn.recv(1024).decode().strip()
    if not opcao:
        break

    if opcao == "1":
        resposta = frase.upper()
    elif opcao == "2":
        resposta = "".join(frase.split())
    elif opcao == "3":
        resposta = f"A frase possui {len(frase.replace(' ', ''))} letras."
    else:
        resposta = "Opção inválida."

    # envia resposta final
    conn.send(resposta.encode())

conn.close()
s.close()
print("Servidor encerrado.")

