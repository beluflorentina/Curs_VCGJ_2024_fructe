import logging
import sys
import os
import lib.biblioteca_fructe as fructe

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../app')))
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../../app/lib')))

print("sys.path:", sys.path)  # Debugging
print("Current working directory:", os.getcwd())  # Debugging




def test_culoare_pitaya():
    culoare = fructe.culoare_pitaya()

    if "vibrantă de roz sau galben" in culoare:
        logger.info(f"Functia culoare_pitaya functioneaza corect: {culoare}")
        assert True
    else:
        logger.error(f"Functia culoare_pitaya NU functioneaza corect: {culoare}")
        assert False

def test_descriere_pitaya():
    descriere = fructe.descriere_pitaya()

    if "Pitaya, cunoscută și ca fructul dragonului" in descriere:
        logger.info(f"Functia descriere_pitaya functioneaza corect:\n{descriere}")
        assert True
    else:
        logger.error(f"Functia descriere_pitaya NU functioneaza corect:\n{descriere}")
        assert False

