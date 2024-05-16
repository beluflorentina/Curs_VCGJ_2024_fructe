from flask import Flask, url_for
from lib.biblioteca_fructe import *

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    ret = "<h1>Fructe</h1>"
    
    ret += f"<a href={url_for('view_durian')}>Durian - Rinciog Florin</a> <br/>"

    return ret


    
@app.route('/durian', methods=['GET'])
def view_durian():
	culoare = culoare_durian()
	descriere = descriere_durian() 
	
	ret = "<h1>Durian</h1>"
	
	#Linkuri
	ret += f"<a href={url_for('index')}>[fructe]</a> | "
	ret += f"<a href={url_for('view_culoare_durian')}>[culoare]</a> | "
	ret += f"<a href={url_for('view_descriere_durian')}>[descriere]</a>"
	
	ret += "<h2>Descriere: </h2>"
	
	ret += descriere 
	
	ret += "<h2>Culoare: </h2>"
	ret += culoare 
	
	
	
	return ret


@app.route('/durian/culoare', methods=['GET'])
def view_culoare_durian():
    culoare = culoare_durian()  
    
    ret = "<h1>Culoare durian:</h1>"
    ret += f"<a href={url_for('index')}>[fructe]</a> | "
    ret += f"<a href={url_for('view_durian')}>[durian]</a> <br/> <br/>"
    ret += culoare
    
    return ret

@app.route('/durian/descriere', methods=['GET'])
def view_descriere_durian():
    descriere = descriere_durian()  
    
    ret = "<h1>Descriere durian:</h1>"
    ret += f"<a href={url_for('index')}>[fructe]</a> | "
    ret += f"<a href={url_for('view_durian')}>[durian]</a> <br/> <br/>"
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
