from flask import Flask

import librarie.biblioteca_pomelo


app = Flask(__name__)

print('443D_pomelo')

@app.route("/" , methods=['GET'])
def index():
    ret = "<h1>Informatii despre pomelo 443D</h1>"
    return ret

@app.route("/pomelo/", methods=['GET'])
def get_pomelo():
    ret = "<h1>pomelo<h1>"
    
    ret += "Zona: "
    ret += librarie.biblioteca_pomelo.zona_pomelo()
    ret += "<br>"
    
    ret += "Clasificare: "
    ret += librarie.biblioteca_pomelo.clasificare_pomelo()
    ret += "<br>"
    
    return ret
    
@app.route("/pomelo/zona", methods=['GET'])
def ia_zona_pomelo():
    ret = ""
    ret += librarie.biblioteca_pomelo.zona_pomelo()
    
    return ret
    
@app.route("/pomelo/clasificare", methods=['GET'])
def ia_clasificare_pomelo():
    ret = ""
    ret += librarie.biblioteca_pomelo.clasificare_pomelo()
    
    return ret
    
    
       
app.run(host = "127.0.0.1", port = 5001)
