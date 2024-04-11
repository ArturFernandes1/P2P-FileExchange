# P2P File Exchange

O projeto P2P File Exchange é uma aplicação Python projetada para permitir a troca de arquivos de maneira
descentralizada entre usuários na mesma rede. Utilizando a tecnologia Peer-to-Peer (P2P), este sistema garante
uma forma eficiente e segura para o compartilhamento de arquivos sem a necessidade de um servidor central.

## Características Principais
- **Comunicação Direta**: Troca de arquivos diretamente entre os usuários sem intervenção de servidores intermediários.
- **Descentralização**: Não depende de uma infraestrutura central, reduzindo o risco de pontos de falha e aumentando a privacidade.
- **Interface Simples**: Uma interface de linha de comando (CLI) fácil de usar e acessível para usuários técnicos e não técnicos.
- **Segurança**: Implementação de criptografia para garantir a segurança dos arquivos trocados entre os pares.
- **Suporte a múltiplos formatos de arquivo**: Capaz de lidar com diversos tipos de arquivos, incluindo documentos, imagens, vídeos e arquivos executáveis.

## Dependências
Para rodar o P2P File Exchange, você precisará de Python 3.6+ e algumas bibliotecas externas, listadas abaixo:

- `socket`
- `threading`
- `os`
- `cryptography`

## Instalação

Clone o repositório usando git:

```bash
git clone https://github.com/seunome/p2p-file-exchange.git
cd p2p-file-exchange
```

Instale as dependências necessárias:

```bash
pip install -r requirements.txt
```

## Uso
Para iniciar o programa, execute o script principal do Python:

```bash
python main.py
```

Na interface do usuário, você poderá escolher se deseja atuar como servidor (host) ou cliente (peer).
Como servidor, você irá disponibilizar arquivos para download. Como cliente, você poderá conectar-se a um servidor e baixar os arquivos disponíveis.

### Configurações
- **IP e Porta**: É necessário definir o endereço IP e a porta para estabelecer a conexão P2P.
- **Diretório de Arquivos**: Especifique o diretório de onde os arquivos serão compartilhados.


