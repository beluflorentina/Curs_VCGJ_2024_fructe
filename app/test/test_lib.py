import logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

import sys
sys.path.append("../")

from app.lib.biblioteca_fructe import *



def test_apple_color():
    color = apple_color()
    assert "red" in color
    assert "green" in color
    assert "yellow" in color


def test_apple_description():
    description = apple_description()
    assert "round, edible" in description
    assert "fruit" in description
    assert "taste" in description
    assert "pie" in description
    assert "juice" in description
    assert "cider" in description

