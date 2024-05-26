"""
O aplicatie simpla in Flask pentru a prezenta fructul acai. 
Include rude catre pagini web cu informatii generale despre fruct
"""

from flask import Flask, url_for
from lib.biblioteca_fructe import culoare_acai, descriere_acai

app = Flask(__name__)



@app.route('/', methods=['GET'])
def index():
    """
    Pagina de acasa care contine linkuri catre toate fructele.
    """
    ret = "<h1>Fructe</h1>"
    ret += (
        f"<a href={url_for('view_acai')}>Acai -"
        "Belu FLorentina-Alexandra</a> <br/>")
    return ret



@app.route('/acai', methods=['GET'])
def view_acai():
    """
    Pagina fructului acai.
    """
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
    """
    Pagina cu specificatii despre culoarea fructului acai.
    """
    culoare = culoare_acai()
    ret = "<h1>Culoarea acai:</h1>"
    ret += f"<a href={url_for('index')}>[fructe]</a> | "
    ret += f"<a href={url_for('view_acai')}>[acai]</a> <br/> <br/>"
    ret += culoare
    return ret

@app.route('/acai/descriere', methods=['GET'])
def view_descriere_acai():
    """
    Pagina cu specificatii despre descrierea fructului acai.
    """
    descriere = descriere_acai()
    ret = "<h1>Descriere acai:</h1>"
    ret += f"<a href={url_for('index')}>[fructe]</a> | "
    ret += f"<a href={url_for('view_acai')}>[acai]</a> <br/> <br/>"
    ret += descriere
    return ret



if __name__ == '__main__':
    app.run(host='127.0.0.1')
