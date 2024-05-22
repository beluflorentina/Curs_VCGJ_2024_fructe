import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

import sys
sys.path.append("../")

import lib.biblioteca_fructe as fructe

def test_culoare_pruna():
    culoare = fructe.culoare_pruna()
    if "roșu-maroniu" in culoare:
        logger.info(f"Functia culoare_pruna functioneaza corect: {culoare}")
        assert True
    else:
        logger.error(f"Functia culoare_pruna NU functioneaza corect: {culoare}")
        assert False

def test_descriere_pruna():
    descriere = fructe.descriere_pruna()
    if "Prunus domestica" in descriere:
        logger.info(f"Functia descriere_pruna functioneaza corect:\n{descriere}")
        assert True
    else:
        logger.error(f"Functia descriere_pruna NU functioneaza corect:\n{descriere}")
        assert False

