import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

import sys
sys.path.append("../")

import lib.biblioteca_fructe as fructe



def test_culoare_grapefruit():
    culoare = fructe.culoare_grapefruit()

    if "pale yellow to dark pink/red" in culoare:
        logger.info(f"Functia culoare_grapefruit functioneaza corect: {culoare}")
        assert True
    else:
        logger.error(f"Functia culoare_grapefruit NU functioneaza corect: {culoare}")
        assert False

def test_descriere_grapefruit():
    descriere = fructe.descriere_grapefruit()

    if "Grapefruit is a citrus hybrid that originated in Barbados in the 18th century" in descriere:
        logger.info(f"Functia descriere_grapefruit functioneaza corect:\n{descriere}")
        assert True
    else:
        logger.error(f"Functia descriere_grapefruit NU functioneaza corect:\n{descriere}")
        assert False 
