import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

import sys
sys.path.append("../")

import lib.biblioteca_fructe as fructe



def test_culoare_ackee():
    culoare = fructe.culoare_ackee()

    if "deep red colored rind" in culoare:
        logger.info(f"Functia culoare_acai functioneaza corect: {culoare}")
        assert True
    else:
        logger.error(f"Functia culoare_acai NU functioneaza corect: {culoare}")
        assert False

def test_descriere_ackee():
    descriere = fructe.descriere_ackee()

    if "known as Blighia sapida" in descriere:
        logger.info(f"Functia descriere_acai functioneaza corect:\n{descriere}")
        assert True
    else:
        logger.error(f"Functia descriere_acai NU functioneaza corect:\n{descriere}")
        assert False 
