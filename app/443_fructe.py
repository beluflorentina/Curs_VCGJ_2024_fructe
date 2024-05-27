from flask import Flask, url_for
from lib.biblioteca_fructe import *

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    ret = "<h1>Fructe</h1>"
    
    ret += f"<a href={url_for('view_acai')}>Acai - Belu FLorentina-Alexandra</a> <br/>"
    
    ret += f"<a href={url_for('view_curmala')}>Curmala - Marinescu Aurora Cristina</a> <br/>"

    return ret
    
@app.route('/curmala', methods=['GET'])
def view_curmala():
	culoare = culoare_curmala()
	descriere = descriere_curmala() 
	
	ret = "<h1>Curmala</h1>"
	
	#Linkuri
	ret += f"<a href={url_for('index')}>[fructe]</a> | "
	ret += f"<a href={url_for('view_culoare_curmala')}>[culoare]</a> | "
	ret += f"<a href={url_for('view_descriere_curmala')}>[descriere]</a>"
	
	ret += "<h2>Descriere: </h2>"
	
	ret += descriere 
	
	ret += "<h2>Culoare: </h2>"
	ret += culoare
	
	
	
	return ret


@app.route('/curmala/culoare', methods=['GET'])
def view_culoare_curmala():
    culoare = culoare_curmala()  
    
    ret = "<h1>Culoarea curmalei:</h1>"
    ret += f"<a href={url_for('index')}>[fructe]</a> | "
    ret += f"<a href={url_for('view_curmala')}>[curmala]</a> <br/> <br/>"
    ret += culoare
    
    return ret

@app.route('/curmala/descriere', methods=['GET'])
def view_descriere_curmala():
    descriere = descriere_curmala()  
    
    ret = "<h1>Descriere curmala:</h1>"
    ret += f"<a href={url_for('index')}>[fructe]</a> | "
    ret += f"<a href={url_for('view_curmala')}>[curmala]</a> <br/> <br/>"
    ret += descriere
    
    return ret



    
@app.route('/acai', methods=['GET'])
def view_acai():
	culoare = culoare_acai()
	descriere = descriere_acai() 
	
	ret = "<h1>Acai</h1>"
	
	#Linkuri
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
