import librarie.biblioteca_pomelo as bpomelo

def test_zona_pomelo():
    zona = bpomelo.zona_pomelo()
    if zona == "Asia" :
        assert True
    else: 
        assert False

def test_clasificare_pomelo():
    clasificare = bpomelo.clasificare_pomelo()
    if clasificare == "Fruct" :
        assert True
    else: 
        assert False
        

