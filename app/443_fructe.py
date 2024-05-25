from flask import Flask, url_for
from lib.biblioteca_fructe import *

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    ret = "<h1>Fructe</h1>"
    
    ret += f"<a href={url_for('view_acai')}>Acai - Belu Florentina-Alexandra</a> <br/>"
    ret += f"<a href={url_for('view_pitaya')}>Pitaya - Tanasescu Andrei</a> <br/>"
    
    return ret

@app.route('/acai', methods=['GET'])
def view_acai():
    culoare = culoare_acai()
    descriere = descriere_acai()
    
    ret = "<h1>Acai</h1>"
    
    # Linkuri
    ret += f"<a href={url_for('index')}>[fructe]</a> | "
    ret += f"<a href={url_for('view_culoare_acai')}>[culoare]</a> | "
    ret += f"<a href={url_for('view_descriere_acai')}>[descriere]</a>"
    
    ret += "<h2>Descriere: </h2>"
    ret += descriere
    
    ret += "<h2>Culoare: </h2>"
    ret += culoare
    
    return ret

@app.route('/acai/culoare', methods=['GET'])
def view_culoare_acai():
    culoare = culoare_acai()
    
    ret = "<h1>Culoarea acai:</h1>"
    ret += f"<a href={url_for('index')}>[fructe]</a> | "
    ret += f"<a href={url_for('view_acai')}>[acai]</a> <br/> <br/>"
    ret += culoare
    
    return ret

@app.route('/acai/descriere', methods=['GET'])
def view_descriere_acai():
    descriere = descriere_acai()
    
    ret = "<h1>Descriere acai:</h1>"
    ret += f"<a href={url_for('index')}>[fructe]</a> | "
    ret += f"<a href={url_for('view_acai')}>[acai]</a> <br/> <br/>"
    ret += descriere
    
    return ret

@app.route('/pitaya', methods=['GET'])
def view_pitaya():
    culoare = culoare_pitaya()
    descriere = descriere_pitaya()
    
    ret = "<h1>Pitaya</h1>"
    
    
    ret += f"<a href={url_for('index')}>[fructe]</a> | "
    ret += f"<a href={url_for('view_culoare_pitaya')}>[culoare]</a> | "
    ret += f"<a href={url_for('view_descriere_pitaya')}>[descriere]</a>"
    
    ret += "<h2>Descriere: </h2>"
    ret += descriere
    
    ret += "<h2>Culoare: </h2>"
    ret += culoare
    
    return ret

@app.route('/pitaya/culoare', methods=['GET'])
def view_culoare_pitaya():
    culoare = culoare_pitaya()
    
    ret = "<h1>Culoarea pitaya:</h1>"
    ret += f"<a href={url_for('index')}>[fructe]</a> | "
    ret += f"<a href={url_for('view_pitaya')}>[pitaya]</a> <br/> <br/>"
    ret += culoare
    
    return ret

@app.route('/pitaya/descriere', methods=['GET'])
def view_descriere_pitaya():
    descriere = descriere_pitaya()
    
    ret = "<h1>Descriere pitaya:</h1>"
    ret += f"<a href={url_for('index')}>[fructe]</a> | "
    ret += f"<a href={url_for('view_pitaya')}>[pitaya]</a> <br/> <br/>"
    ret += descriere
    
    return ret

@app.cli.command()
def test():
    """
    Rulare 'unit tests'
    
    Apelare pytest din aplicatia systest, cu ajutorul comenzii flask.
    """
    import pytest
    import sys
    sys.exit(pytest.main(["."]))

if __name__ == '__main__':
    app.run(host='127.0.0.1')

