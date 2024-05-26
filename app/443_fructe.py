from flask import Flask, url_for
from lib.biblioteca_fructe import *

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    ret = "<h1>Fructe</h1>"
    
    ret += f"<a href={url_for('view_grapefruit')}>Grapefruit - Banica Dragos Marius</a> <br/>"

    return ret


    
@app.route('/grapefruit', methods=['GET'])
def view_grapefruit():
	culoare = culoare_grapefruit()
	descriere = descriere_grapefruit() 
	
	ret = "<h1>Grapefruit</h1>"
	
	#Linkuri
	ret += f"<a href={url_for('index')}>[fructe]</a> | "
	ret += f"<a href={url_for('view_culoare_grapefruit')}>[culoare]</a> | "
	ret += f"<a href={url_for('view_descriere_grapefruit')}>[descriere]</a>"
	
	ret += "<h2>Descriere: </h2>"
	
	ret += descriere 
	
	ret += "<h2>Culoare: </h2>"
	ret += culoare
	
	
	
	return ret


@app.route('/grapefruit/culoare', methods=['GET'])
def view_culoare_grapefruit():
    culoare = culoare_grapefruit()  
    
    ret = "<h1>Culoarea grapefruit:</h1>"
    ret += f"<a href={url_for('index')}>[fructe]</a> | "
    ret += f"<a href={url_for('view_grapefruit')}>[grapefruit]</a> <br/> <br/>"
    ret += culoare
    
    return ret

@app.route('/grapefruit/descriere', methods=['GET'])
def view_descriere_grapefruit():
    descriere = descriere_grapefruit()  
    
    ret = "<h1>Descriere grapefruit:</h1>"
    ret += f"<a href={url_for('index')}>[fructe]</a> | "
    ret += f"<a href={url_for('view_grapefruit')}>[grapefruit]</a> <br/> <br/>"
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
