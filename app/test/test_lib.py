import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

import sys
sys.path.append("../")

import lib.biblioteca_fructe as fructe



def test_culoare_guava():
    culoare = fructe.culoare_guava()

    if "vibrant green to golden yellow" in culoare:
        logger.info(f"Functia culoare_guava functioneaza corect:\n{culoare}")
        assert True
    else:
        logger.error(f"Functia culoare_guava NU functioneaza corect:\n{culoare}")
        assert False

def test_descriere_guava():
    descriere = fructe.descriere_guava()

    if "Psidium guajava (lemon guava, apple guava) is a small tree" in descriere:
        logger.info("Functia descriere_guava functioneaza corect:\n{descriere}")
        assert True
    else:
        logger.error(f"Functia descriere_guava NU functioneaza corect:\n{descriere}")
        assert False 
