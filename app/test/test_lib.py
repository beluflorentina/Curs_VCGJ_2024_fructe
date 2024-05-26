import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

import sys
sys.path.append("../")

import lib.biblioteca_fructe as fructe



def test_culoare_banana():
    culoare = fructe.culoare_banana()

    if "banana is mostly green" in culoare:
        logger.info(f"Functia culoare_banana functioneaza corect: {culoare}")
        assert True
    else:
        logger.error(f"Functia culoare_banana NU functioneaza corect: {culoare}")
        assert False

def test_descriere_banana():
    descriere = fructe.descriere_banana()

    if "widely consumed fruits in the world" in descriere:
        logger.info(f"Functia descriere_banana functioneaza corect:\n{descriere}")
        assert True
    else:
        logger.error(f"Functia descriere_banana NU functioneaza corect:\n{descriere}")
        assert False 
