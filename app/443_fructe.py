from flask import Flask, url_for
from lib.biblioteca_fructe import *

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    ret = "<h1>Fructe</h1>"
    
    ret += f"<a href={url_for('view_acai')}>Corcoduse - Tufeanu Razvan-Vladian</a> <br/>"

    return ret


    
@app.route('/corcoduse', methods=['GET'])
def view_acai():
	culoare = culoare_corcoduse()
	descriere = descriere_corcoduse() 
	
	ret = "<h1>Corcoduse</h1>"
	
	#Linkuri
	ret += f"<a href={url_for('index')}>[fructe]</a> | "
	ret += f"<a href={url_for('view_culoare_corcoduse')}>[culoare]</a> | "
	ret += f"<a href={url_for('view_descriere_corcoduse')}>[descriere]</a>"
	
	ret += "<h2>Descriere: </h2>"
	
	ret += descriere 
	
	ret += "<h2>Culoare: </h2>"
	ret += culoare
	
	
	
	return ret


@app.route('/corcoduse/culoare', methods=['GET'])
def view_culoare_corcoduse():
    culoare = culoare_corcoduse()  
    
    ret = "<h1>Culoarea corcoduse:</h1>"
    ret += f"<a href={url_for('index')}>[fructe]</a> | "
    ret += f"<a href={url_for('view_corcoduse')}>[corcoduse]</a> <br/> <br/>"
    ret += culoare
    
    return ret

@app.route('/corcoduse/descriere', methods=['GET'])
def view_descriere_corcoduse():
    descriere = descriere_corcoduse()  
    
    ret = "<h1>Descriere corcoduse:</h1>"
    ret += f"<a href={url_for('index')}>[fructe]</a> | "
    ret += f"<a href={url_for('view_corcoduse')}>[corcoduse]</a> <br/> <br/>"
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
