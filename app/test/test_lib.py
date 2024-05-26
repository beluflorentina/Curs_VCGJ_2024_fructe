import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

import sys
sys.path.append("../")

import lib.biblioteca_fructe as fructe



def test_culoare_corcoduse():
    culoare = fructe.culoare_corcoduse()

    if "verzi" in culoare:
        logger.info(f"Functia culoare_corcoduse functioneaza corect: {culoare}")
        assert True
    else:
        logger.error(f"Functia culoare_corcoduse NU functioneaza corect: {culoare}")
        assert False

def test_descriere_corcoduse():
    descriere = fructe.descriere_corcoduse()

    if "Corcodușele sunt bogate în vitamine" in descriere:
        logger.info(f"Functia descriere_corcoduse functioneaza corect:\n{descriere}")
        assert True
    else:
        logger.error(f"Functia descriere_corcoduse NU functioneaza corect:\n{descriere}")
        assert False 
