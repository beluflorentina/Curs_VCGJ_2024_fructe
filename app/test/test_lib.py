import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

import sys
sys.path.append("../")

import lib.biblioteca_fructe as fructe



def test_culoare_acai():
    culoare = fructe.culoare_acai()

    if "rich purple color" in culoare:
        logger.info(f"Functia culoare_acai functioneaza corect: {culoare}")
        assert True
    else:
        logger.error(f"Functia culoare_acai NU functioneaza corect: {culoare}")
        assert False

def test_descriere_acai():
    descriere = fructe.descriere_acai()

    if "scientifically known as Euterpe oleracea" in descriere:
        logger.info(f"Functia descriere_acai functioneaza corect:\n{descriere}")
        assert True
    else:
        logger.error(f"Functia descriere_acai NU functioneaza corect:\n{descriere}")
        assert False 
