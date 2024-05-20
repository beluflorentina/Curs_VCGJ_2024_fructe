from flask import Flask, url_for
from lib.biblioteca_fructe import *

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    ret = "<h1>Fructe</h1>"
    
    ret += f"<a href={url_for('view_ackee')}>Ackee - Burlacel George</a> <br/>"

    return ret


    
@app.route('/ackee', methods=['GET'])
def view_ackee():
	culoare = culoare_ackee()
	descriere = descriere_ackee() 
	
	ret = "<h1>Ackee</h1>"
	
	#Linkuri
	ret += f"<a href={url_for('index')}>[fructe]</a> | "
	ret += f"<a href={url_for('view_culoare_ackee')}>[culoare]</a> | "
	ret += f"<a href={url_for('view_descriere_ackee')}>[descriere]</a>"
	
	ret += "<h2>Descriere: </h2>"
	
	ret += descriere 
	
	ret += "<h2>Culoare: </h2>"
	ret += culoare
	
	
	
	return ret


@app.route('/ackee/culoare', methods=['GET'])
def view_culoare_ackee():
    culoare = culoare_ackee()  
    
    ret = "<h1>Culoarea ackee:</h1>"
    ret += f"<a href={url_for('index')}>[fructe]</a> | "
    ret += f"<a href={url_for('view_ackee')}>[ackee]</a> <br/> <br/>"
    ret += culoare
    
    return ret

@app.route('/ackee/descriere', methods=['GET'])
def view_descriere_ackee():
    descriere = descriere_ackee()  
    
    ret = "<h1>Descriere ackee:</h1>"
    ret += f"<a href={url_for('index')}>[fructe]</a> | "
    ret += f"<a href={url_for('view_ackee')}>[ackee]</a> <br/> <br/>"
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
