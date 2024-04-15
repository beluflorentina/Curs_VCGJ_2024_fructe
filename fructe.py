from flask import Flask, url_for

#from app.lib import network
#from app.lib import ubuntu
#from app.grafice.exemplu_func_grad_2 import valori_x, valori_y, genereaza_grafice

print('fructe')



app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    ret = "<h1>FRUCTE</h1>"


    ret += "<pre>"

    ret += " - test1\n"
    ret += " - test2"
    
    ret += "</pre>"
    
    ret += " - test3\n"
    ret += " - test4"
    
    return "fructe"
    
@app.cli.command()
def test():
    """
    Rulare 'unit tests'
    
    Apelare pytest din aplicatia systest, cu ajutorul comenzii flask.
    
    """
    import pytest
    sys.exit(pytest.main(["."]))
    

    
   
