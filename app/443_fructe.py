from flask import Flask, url_for
from lib.biblioteca_fructe import *

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    ret = "<h1>Fructe</h1>"
    
    ret += f"<a href={url_for('view_banana')}>Banana - Sandu Dan-Mihai</a> <br/>"

    return ret


    
@app.route('/banana', methods=['GET'])
def view_banana():
	culoare = culoare_banana()
	descriere = descriere_banana() 
	
	ret = "<h1>Banana</h1>"
	
	#Linkuri
	ret += f"<a href={url_for('index')}>[fructe]</a> | "
	ret += f"<a href={url_for('view_culoare_banana')}>[culoare]</a> | "
	ret += f"<a href={url_for('view_descriere_banana')}>[descriere]</a>"
	
	ret += "<h2>Descriere: </h2>"
	
	ret += descriere 
	
	ret += "<h2>Culoare: </h2>"
	ret += culoare
	
	
	
	return ret


@app.route('/banana/culoare', methods=['GET'])
def view_culoare_banana():
    culoare = culoare_banana()  
    
    ret = "<h1>Culoarea banana:</h1>"
    ret += f"<a href={url_for('index')}>[fructe]</a> | "
    ret += f"<a href={url_for('view_banana')}>[banana]</a> <br/> <br/>"
    ret += culoare
    
    return ret

@app.route('/banana/descriere', methods=['GET'])
def view_descriere_banana():
    descriere = descriere_banana()  
    
    ret = "<h1>Descriere banana:</h1>"
    ret += f"<a href={url_for('index')}>[fructe]</a> | "
    ret += f"<a href={url_for('view_banana')}>[banana]</a> <br/> <br/>"
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
