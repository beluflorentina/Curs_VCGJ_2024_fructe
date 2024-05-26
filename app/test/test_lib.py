import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

import sys
sys.path.append("../")

import app.lib.biblioteca_fructe as fructe



def test_istorie_caisa():
    istorie = fructe.istorie_caisa()

    if "Apricots are propagated by budding" in istorie:
        logger.info(f"Functia istorie_acai functioneaza corect: {istorie}")
        assert True
    else:
        logger.error(f"Functia istorie_acai NU functioneaza corect: {istorie}")
        assert False

def test_descriere_caisa():
    descriere = fructe.descriere_caisa()

    if "pricot, (Prunus armeniaca), economically important fruit tree," in descriere:
        logger.info(f"Functia descriere_caisa functioneaza corect:\n{descriere}")
        assert True
    else:
        logger.error(f"Functia descriere_caisa NU functioneaza corect:\n{descriere}")
        assert False 
