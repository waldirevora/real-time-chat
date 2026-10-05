# Real-Time Chat

Aplicação de chat em tempo real desenvolvida com Python, Flask e Flask-SocketIO como parte dos estudos de comunicação em tempo real com Flask na Rocketseat.

O projeto permite que múltiplos usuários conectados ao servidor enviem e recebam mensagens instantaneamente utilizando Socket.IO.

## Objetivo

O objetivo deste projeto é praticar a comunicação em tempo real entre navegador e servidor, compreendendo como eventos podem ser enviados pelo cliente, processados pelo Flask e distribuídos para os usuários conectados.

## Tecnologias

- Python
- Flask
- Flask-SocketIO
- Socket.IO
- HTML
- JavaScript
- Git
- GitHub

## Funcionalidades

- Interface web para envio de mensagens.
- Comunicação em tempo real com Socket.IO.
- Recebimento de mensagens pelo servidor Flask.
- Distribuição das mensagens para clientes conectados.
- Suporte a múltiplas janelas ou usuários simultaneamente.
- Renderização da interface utilizando templates do Flask.

## Estrutura do projeto

```text
real-time-chat/
│
├── .gitignore
├── README.md
├── app.py
├── requirements.txt
│
└── templates/
    └── index.html
```

## Como funciona

O navegador se conecta ao servidor utilizando Socket.IO.

Quando um usuário envia uma mensagem, o cliente dispara um evento `message`.

O Flask-SocketIO recebe esse evento através da função responsável pelo tratamento da mensagem.

Depois, o servidor retransmite a mensagem para os clientes conectados.

Fluxo simplificado:

```text
Cliente A
    │
    │ envia mensagem
    ▼
Socket.IO
    │
    ▼
Flask-SocketIO
    │
    ▼
Servidor
    │
    ├──────────────► Cliente A
    │
    └──────────────► Cliente B
```

Dessa forma, uma mensagem enviada em uma janela do navegador pode ser visualizada pelas demais janelas conectadas ao mesmo servidor.

## Organização do código

O projeto foi mantido propositalmente simples, de acordo com o escopo do desafio.

A organização busca seguir boas práticas de código e princípios SOLID quando aplicáveis, principalmente o princípio de responsabilidade única.

### `app.py`

Responsável por:

- criar a aplicação Flask;
- configurar o Flask-SocketIO;
- definir a rota principal;
- receber eventos de mensagem;
- retransmitir mensagens;
- iniciar o servidor.

### `templates/index.html`

Responsável por:

- exibir a interface do chat;
- conectar o navegador ao Socket.IO;
- capturar o envio de mensagens;
- enviar mensagens ao servidor;
- receber mensagens do servidor;
- adicionar as mensagens recebidas à interface.

## Pré-requisitos

Para executar o projeto é necessário possuir:

- Python instalado;
- Git instalado;
- navegador web.

## Instalação

Clone o repositório:

```powershell
git clone https://github.com/waldirevora/real-time-chat.git
```

Entre na pasta do projeto:

```powershell
cd real-time-chat
```

Crie um ambiente virtual:

```powershell
python -m venv .venv
```

Ative o ambiente virtual no Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

Instale as dependências:

```powershell
pip install -r requirements.txt
```

## Executando a aplicação

Com o ambiente virtual ativo, execute:

```powershell
python app.py
```

O servidor será iniciado localmente.

Acesse no navegador:

```text
http://127.0.0.1:5000
```

## Testando o chat em tempo real

Para validar o funcionamento:

1. Inicie o servidor com `python app.py`.
2. Abra `http://127.0.0.1:5000` em uma janela do navegador.
3. Abra o mesmo endereço em uma segunda janela ou aba.
4. Envie uma mensagem pela primeira janela.
5. Verifique se a mensagem aparece nas duas janelas.
6. Envie outra mensagem pela segunda janela.
7. Verifique novamente a comunicação entre os clientes.

Esse teste confirma que o servidor está recebendo e distribuindo mensagens em tempo real.

## Implementação principal

A rota principal renderiza a interface do chat:

```python
@app.route("/")
def index():
    """
    Exibe a página principal do chat.

    Returns:
        str: página HTML renderizada pelo Flask.
    """
    return render_template("index.html")
```

O evento `message` recebe uma mensagem enviada pelo cliente e a retransmite:

```python
@socketio.on("message")
def handle_message(message):
    """
    Recebe uma mensagem enviada por um cliente e a retransmite
    para todos os clientes conectados ao chat.

    Args:
        message (str): mensagem enviada pelo usuário.
    """

    # Envia a mensagem recebida para os clientes conectados.
    socketio.send(message)
```

## SOLID

Neste projeto, os princípios SOLID são utilizados como orientação, sem adicionar abstrações desnecessárias para um projeto pequeno.

O principal princípio aplicado neste estágio é:

### Single Responsibility Principle

Cada função possui uma responsabilidade clara.

A função `index()` é responsável apenas por renderizar a página principal.

A função `handle_message()` é responsável por tratar e retransmitir mensagens recebidas pelo Socket.IO.

A arquitetura pode evoluir e ganhar novas separações caso o projeto cresça e novas responsabilidades sejam adicionadas.

## Dependências

As dependências Python utilizadas pelo projeto ficam registradas em:

```text
requirements.txt
```

Elas podem ser instaladas novamente com:

```powershell
pip install -r requirements.txt
```

Entre as principais dependências estão:

- Flask
- Flask-SocketIO
- python-socketio
- python-engineio
- simple-websocket

## Versionamento

O projeto utiliza Git para controle de versão e GitHub como repositório remoto.

Repositório:

```text
https://github.com/waldirevora/real-time-chat
```

O desenvolvimento é registrado através de commits incrementais para manter o histórico das funcionalidades implementadas.

## Aprendizados

Este projeto permite praticar conceitos como:

- criação de aplicações web com Flask;
- criação de rotas HTTP;
- utilização de templates HTML;
- comunicação em tempo real;
- eventos com Socket.IO;
- Flask-SocketIO;
- comunicação cliente-servidor;
- múltiplos clientes conectados;
- ambientes virtuais Python;
- gerenciamento de dependências;
- princípios básicos de SOLID;
- Git;
- GitHub.

## Limitações atuais

Esta implementação possui escopo educacional e ainda não inclui:

- autenticação de usuários;
- identificação por nome;
- persistência das mensagens;
- banco de dados;
- salas privadas;
- histórico de conversas;
- deploy em ambiente de produção.

Esses recursos podem ser adicionados futuramente caso o projeto seja expandido.

## Contexto acadêmico

Projeto desenvolvido durante os estudos de Python com Flask da Rocketseat, no módulo de comunicação em tempo real.

O desafio tem como objetivo implementar um chat utilizando Flask e Socket.IO para compreender o funcionamento da comunicação baseada em eventos entre cliente e servidor.

## Status

Projeto funcional.

A comunicação em tempo real foi validada utilizando duas janelas do navegador conectadas simultaneamente ao servidor.

## Autor

Waldir Évora

GitHub:

```text
https://github.com/waldirevora
```
