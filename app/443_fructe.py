from flask import Flask, url_for
from lib.biblioteca_fructe import *

app = Flask(__name__)


@app.route("/", methods=["GET"])
def index():
    ret = "<h1>Fructe</h1>"

    ret += f"<a href={url_for('view_ananas')}>Ananas - Crisan Ioan-Bogdan</a> <br/>"

    return ret


@app.route("/ananas", methods=["GET"])
def view_ananas():
    culoare = culoare_ananas()
    descriere = descriere_ananas()

    ret = "<h1>Ananas</h1>"

    # Linkuri
    ret += f"<a href={url_for('index')}>[fructe]</a> | "
    ret += f"<a href={url_for('view_culoare_ananas')}>[culoare]</a> | "
    ret += f"<a href={url_for('view_descriere_ananas')}>[descriere]</a>"

    ret += "<h2>Descriere: </h2>"

    ret += descriere

    ret += "<h2>Culoare: </h2>"
    ret += culoare

    return ret


@app.route("/ananas/culoare", methods=["GET"])
def view_culoare_ananas():
    culoare = culoare_ananas()

    ret = "<h1>Culoarea ananas:</h1>"
    ret += f"<a href={url_for('index')}>[fructe]</a> | "
    ret += f"<a href={url_for('view_ananas')}>[ananas]</a> <br/> <br/>"
    ret += culoare

    return ret


@app.route("/ananas/descriere", methods=["GET"])
def view_descriere_ananas():
    descriere = descriere_ananas()

    ret = "<h1>Descriere ananas:</h1>"
    ret += f"<a href={url_for('index')}>[fructe]</a> | "
    ret += f"<a href={url_for('view_ananas')}>[ananas]</a> <br/> <br/>"
    ret += descriere

    return ret


@app.cli.command()
def test():
    """
    Rulare 'unit tests'

    Apelare pytest din aplicatia systest, cu ajutorul comenzii flask.

    """
    import pytest

    sys.exit(pytest.main(["."]))


if __name__ == "__main__":
    app.run(host="127.0.0.1")
