import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

import sys

sys.path.append("../")

import lib.biblioteca_fructe as fructe


def test_culoare_ananas():
    culoare = fructe.culoare_ananas()

    if "greenish-yellow fruit" in culoare:
        logger.info(f"Functia culoare_ananas functioneaza corect: {culoare}")
        assert True
    else:
        logger.error(f"Functia culoare_ananas NU functioneaza corect: {culoare}")
        assert False


def test_descriere_ananas():
    descriere = fructe.descriere_ananas()

    if "tropical and subtropical America" in descriere:
        logger.info(f"Functia descriere_ananas functioneaza corect:\n{descriere}")
        assert True
    else:
        logger.error(f"Functia descriere_ananas NU functioneaza corect:\n{descriere}")
        assert False
