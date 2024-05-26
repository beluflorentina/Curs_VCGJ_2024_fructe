from flask import Flask, url_for
from app.lib.biblioteca_fructe import *

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    ret = "<h1>Fructe</h1>"
    ret += f"<a href={url_for('view_caisa')}>Caisa - Funda Gheorghe</a> <br/>"

    return ret



@app.route('/caisa',methods=['GET'])
def view_caisa():
    istorie = istorie_caisa()
    descriere = descriere_caisa()

    ret = "<h1>Caisa</h1>"

    #Linkuri
    ret += f"<a href={url_for('index')}>[fructe]</a> | "
    ret += f"<a href={url_for('view_istorie_caisa')}>[istorie]</a> | "
    ret += f"<a href={url_for('view_descriere_caisa')}>[descriere]</a>"

    ret += "<h2>Descriere: </h2>"

    ret += descriere

    ret += "<h2>Istorie: </h2>"
    ret += istorie



    return ret


@app.route('/caisa/istorie', methods=['GET'])
def view_istorie_caisa():
    istorie = istorie_caisa()

    ret = "<h1>Istorie caisa:</h1>"
    ret += f"<a href={url_for('index')}>[fructe]</a> | "
    ret += f"<a href={url_for('view_caisa')}>[caisa]</a> <br/> <br/>"
    ret += istorie

    return ret

@app.route('/caisa/descriere', methods=['GET'])
def view_descriere_caisa():
    descriere = descriere_caisa()

    ret = "<h1>Descriere caisa:</h1>"
    ret += f"<a href={url_for('index')}>[fructe]</a> | "
    ret += f"<a href={url_for('view_caisa')}>[caisa]</a> <br/> <br/>"
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

if __name__ == '__main__':
    app.run(host='127.0.0.1')
