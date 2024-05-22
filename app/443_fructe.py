from flask import Flask, url_for
from lib.biblioteca_fructe import *

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    ret = "<h1>Fructe</h1>"
    
    ret += f"<a href={url_for('view_pruna')}>Pruna - Busicescu_Mihai</a> <br/>"

    return ret


    
@app.route('/pruna', methods=['GET'])
def view_pruna():
	culoare = culoare_pruna()
	descriere = descriere_pruna() 
	
	ret = "<h1>Pruna</h1>"
	
	#Linkuri
	ret += f"<a href={url_for('index')}>[fructe]</a> | "
	ret += f"<a href={url_for('view_culoare_pruna')}>[culoare]</a> | "
	ret += f"<a href={url_for('view_descriere_pruna')}>[descriere]</a>"
	
	ret += "<h2>Descriere: </h2>"
	
	ret += descriere 
	
	ret += "<h2>Culoare: </h2>"
	ret += culoare
	
	
	
	return ret


@app.route('/pruna/culoare', methods=['GET'])
def view_culoare_pruna():
    culoare = culoare_pruna()  
    
    ret = "<h1>Culoarea pruna:</h1>"
    ret += f"<a href={url_for('index')}>[fructe]</a> | "
    ret += f"<a href={url_for('view_pruna')}>[pruna]</a> <br/> <br/>"
    ret += culoare
    
    return ret

@app.route('/pruna/descriere', methods=['GET'])
def view_descriere_pruna():
    descriere = descriere_pruna()  
    
    ret = "<h1>Descriere pruna:</h1>"
    ret += f"<a href={url_for('index')}>[fructe]</a> | "
    ret += f"<a href={url_for('view_pruna')}>[pruna]</a> <br/> <br/>"
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
