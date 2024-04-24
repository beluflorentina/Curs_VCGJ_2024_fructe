from flask import Flask, url_for
from lib.biblioteca_fructe import *

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    ret = "<h1>FRUCTE</h1>"

    ret +=f"<a href={url_for('view_guava')}>Guava - Grigoras Marin-Jan</a> <br/>" 

    return ret

@app.route('/guava',methods=['GET'])
def view_guava():
	culoare = culoare_guava()
	descriere = descriere_guava()
	
	ret = "<h1>Guava</h1>"

	#Links
	ret += f"<a href={url_for('index')}>[fructe]</a> | " 
	ret += f"<a href={url_for('view_culoare_guava')}>[culoare]</a> | " 
	ret += f"<a href={url_for('view_descriere_guava')}>[descriere]</a>" 


	ret += "<h2>Descriere: </h2>"

	ret += descriere

	ret += "<h2>Culoare: </h2>"

	ret+= culoare
	
	
	return ret

@app.route('/guava/culoare',methods=['GET'])
def view_culoare_guava():
	culoare = culoare_guava()

	ret = "<h1>Culoare Guava: </h1>"
	ret += f"<a href={url_for('index')}>[fructe]</a> | " 
	ret += f"<a href={url_for('view_guava')}>[culoare]</a>" 
	
	return ret;

@app.route('/guava/descriere',methods=['GET'])
def view_descriere_guava():
	descriere = descriere_guava()
	
	ret ="<h1>Descriere Guava:</h1>"

	#Links
	ret += f"<a href={url_for('index')}>[fructe]</a> | " 
	ret += f"<a href={url_for('view_guava')}>[culoare]</a>" 
	
	ret += descriere        
	return ret;

@app.cli.command()
def test():
    """
    Rulare 'unit tests'

    Apelare pytest din aplicatia systest, cu ajutorul comenzii flask.

     """
    import pytest
    sys.exit(pytest.main(["."]))



