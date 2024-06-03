import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

import sys
sys.path.append("../")

import lib.biblioteca_fructe as fructe



def test_culoare_kiwi():
    culoare = fructe.culoare_kiwi()

    if "fuzzy brown skin" in culoare:
        logger.info(f"Functia culoare_kiwi functioneaza corect: {culoare}")
        assert True
    else:
        logger.error(f"Functia culoare_kiwi NU functioneaza corect: {culoare}")
        assert False

def test_descriere_kiwi():
    descriere = fructe.descriere_kiwi()

    if "firm translucent green flesh" in descriere:
        logger.info(f"Functia descriere_kiwi functioneaza corect:\n{descriere}")
        assert True
    else:
        logger.error(f"Functia descriere_kiwi NU functioneaza corect:\n{descriere}")
        assert False 
