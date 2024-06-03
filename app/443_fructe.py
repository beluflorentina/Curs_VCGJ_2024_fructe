"""
O aplicatie simpla in Flask pentru a prezenta fructul kiwi. 
Include rude catre pagini web cu informatii generale despre fruct
"""

from flask import Flask, url_for
from lib.biblioteca_fructe import culoare_kiwi, descriere_kiwi

app = Flask(__name__)



@app.route('/', methods=['GET'])
def index():
    """
    Pagina de acasa care contine linkuri catre toate fructele.
    """
    ret = "<h1>Fructe</h1>"
    ret += (
        f"<a href={url_for('view_kiwi')}>Kiwi -"
        "Paraschiv Robert-Marian</a> <br/>")
    return ret



@app.route('/kiwi', methods=['GET'])
def view_kiwi():
    """
    Pagina fructului kiwi.
    """
    culoare = culoare_kiwi()
    descriere = descriere_kiwi()

    ret = "<h1>Kiwi</h1>"
    #Linkuri
    ret += f"<a href={url_for('index')}>[fructe]</a> | "
    ret += f"<a href={url_for('view_culoare_kiwi')}>[culoare]</a> | "
    ret += f"<a href={url_for('view_descriere_kiwi')}>[descriere]</a>"

    ret += "<h2>Descriere: </h2>"
    ret += descriere
    ret += "<h2>Culoare: </h2>"
    ret += culoare
    return ret


@app.route('/kiwi/culoare', methods=['GET'])
def view_culoare_kiwi():
    """
    Pagina cu specificatii despre culoarea fructului kiwi.
    """
    culoare = culoare_kiwi()
    ret = "<h1>Culoarea kiwi:</h1>"
    ret += f"<a href={url_for('index')}>[fructe]</a> | "
    ret += f"<a href={url_for('view_kiwi')}>[kiwi]</a> <br/> <br/>"
    ret += culoare
    return ret

@app.route('/kiwi/descriere', methods=['GET'])
def view_descriere_kiwi():
    """
    Pagina cu specificatii despre descrierea fructului kiwi.
    """
    descriere = descriere_kiwi()
    ret = "<h1>Descriere kiwi:</h1>"
    ret += f"<a href={url_for('index')}>[fructe]</a> | "
    ret += f"<a href={url_for('view_kiwi')}>[kiwi]</a> <br/> <br/>"
    ret += descriere
    return ret



if __name__ == '__main__':
    app.run(host='127.0.0.1')
