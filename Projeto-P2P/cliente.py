import os
import socket
import time


#função para listar os arquivos disponiveis para compartilhar
def list_files():
    client.send(b'list_files')
    files = client.recv(10000).decode()
    print("="*5 +' Arquivos disponíveis '+ "="*6)
    print(files)

#Função responsavel pelo download dos arquivos
def download_file():
    client.send(b'download_file')
    filename = input('Digite o nome do arquivo que deseja baixar: ')
    client.send(filename.encode())
    response = client.recv(1024).decode()

    # Condicional para informar se o arquivo existe ou não
    if response == 'FileNotFound':
        print('Arquivo não encontrado.')
        return

    filepath = os.path.join("arquivos", "temp", filename)
    with open(filepath, 'wb') as file:
        while True:
            data = client.recv(1024)
            if not data:
                break
            file.write(data)

    # Aguarde um curto período de tempo antes de exibir a mensagem de conclusão
    time.sleep(0.1)

    print('{} recebido com sucesso!\n'.format(filename))

#Fazer conectividade com o tracker
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(('localhost', 5000))
print('Conectado!\n')

# While True para sempre ficar mostrando um menu para melhor interação do usuario
while True:
    print("="*13 +' Menu '+ "="*13)
    print('1 - Listar arquivos disponíveis')
    print('2 - Fazer download de um arquivo')
    print('3 - Sair')
    
    print("=" * 7 +' Selecione uma opção '+ "="*5 )
    option = input('Opção?')
   
    if option == '1':
        list_files()
    elif option == '2':
        download_file()
    elif option == '3':
        break
    else:
        print('Opção inválida. Por favor, tente novamente.\n')

client.close()
