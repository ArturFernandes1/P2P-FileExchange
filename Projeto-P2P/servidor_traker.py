import socket
import os
from threading import Thread
import time

clients = []

def list_files(client):
    directory = os.path.join("arquivos", "download")
    files = os.listdir(directory)
    files_str = '\n'.join(files)
    client.send(files_str.encode())


def download_file(client, filename):
    filepath = os.path.join("arquivos", "download", filename)
    if not os.path.exists(filepath):
        client.send(b'FileNotFound')
        return

    client.send(b'FileFound')

    with open(filepath, 'rb') as file:
        while True:
            data = file.read(1024)
            if not data:
                break
            client.send(data)

    # Aguarde um curto período de tempo antes de enviar a mensagem de conclusão
    time.sleep(0.1)

    # Envie a mensagem de aviso quando o download for concluído com sucesso
    msg_recebida = "Download do arquivo '{}' concluído com sucesso.".format(filename)
    client.send(msg_recebida.encode())

#Função para lidar com a comunicao de Tracker e cliemte, por isso esta loop infinito.
def handle_client(client):
    while True:
        request = client.recv(1024).decode()

        if request == 'list_files':
            list_files(client)
        elif request == 'download_file':
            filename = client.recv(1024).decode()
            download_file(client, filename)
        else:
            break

    client.close()
    clients.remove(client)

#Cria o servidor Tracker, define a endereco como LocalHost, porta 5000
def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 5000))
    server.listen()

    print('Tracker iniciado, aguardando conexões...')

# Permite que varios clientes se conecte, e rode em paralelo
    while True:
        client, address = server.accept()
        print('Conexão estabelecida com', address)
        clients.append(client)
        client_thread = Thread(target=handle_client, args=(client,))
        client_thread.start()

start_server()
