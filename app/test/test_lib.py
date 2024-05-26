import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

import sys
sys.path.append("../")

import lib.biblioteca_fructe as fructe



def test_culoare_pepene():
    culoare = fructe.culoare_pepene()

    if "red inside" in culoare:
        logger.info(f"Functia culoare_pepene functioneaza corect: {culoare}")
        assert True
    else:
        logger.error(f"Functia culoare_pepene NU functioneaza corect: {culoare}")
        assert False

def test_descriere_pepene():
    descriere = fructe.descriere_pepene()

    if "Absolutely brilliant on a hot summer" in descriere:
        logger.info(f"Functia descriere_pepene functioneaza corect:\n{descriere}")
        assert True
    else:
        logger.error(f"Functia descriere_pepene NU functioneaza corect:\n{descriere}")
        assert False 
