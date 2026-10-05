from flask import Flask, render_template
from flask_socketio import SocketIO


# Cria a aplicação Flask responsável pelo servidor web.
app = Flask(__name__)


# Adiciona suporte à comunicação em tempo real com Socket.IO.
socketio = SocketIO(app)


@app.route("/")
def index():
    """
    Exibe a página principal do chat.

    Returns:
        str: página HTML renderizada pelo Flask.
    """
    return render_template("index.html")


if __name__ == "__main__":
    # Inicia o servidor Flask com suporte ao Socket.IO.
    socketio.run(app, debug=True)