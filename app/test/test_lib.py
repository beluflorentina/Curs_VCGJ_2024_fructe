import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

import sys
sys.path.append("../")

import lib.biblioteca_fructe as fructe



def test_culoare_durian():
    culoare = fructe.culoare_durian()

    if "also be red or green" in culoare:
        logger.info(f"Functia culoare_durian functioneaza corect: {culoare}")
        assert True
    else:
        logger.error(f"Functia culoare_durian NU functioneaza corect: {culoare}")
        assert False

def test_descriere_durian():
    descriere = fructe.descriere_durian()

    if "Durian grows in tropical" in descriere:
        logger.info(f"Functia descriere_durian functioneaza corect:\n{descriere}")
        assert True
    else:
        logger.error(f"Functia descriere_durian NU functioneaza corect:\n{descriere}")
        assert False 
