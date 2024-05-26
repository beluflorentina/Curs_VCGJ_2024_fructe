"""Fructe app"""
import sys

from flask import Flask, url_for
from app.lib.biblioteca_fructe import apple_color, apple_description

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    """Main page"""
    ret = "<h1>Fructe</h1>"
    ret += f"<a href={url_for('view_apple')}>Apple - Ana-Ioana Cristescu</a>"
    return ret


@app.route('/apple', methods=['GET'])
def view_apple():
    """View apple"""
    # commented to resolve pyplint error -  unused variables
    #color = apple_color()
    #description = apple_description()

    ret = "<h1>Apple</h1>"

    ret += f"<a href={url_for('view_apple_color')}>[view color]</a> | "
    ret += f"<a href={url_for('view_apple_description')}>[view description]</a>"
    ret += f"<br><br><a href={url_for('index')}>Go back home</a> | "

    return ret


@app.route('/apple/color', methods=['GET'])
def view_apple_color():
    """View apple colour"""
    ret = "<h1>Apple color:</h1>"
    ret += apple_color()
    ret += f"<br><br><a href={url_for('view_apple')}>[back]</a> |"
    ret += f"<a href={url_for('index')}>[home]</a>"
    return ret


@app.route('/apple/description', methods=['GET'])
def view_apple_description():
    """View apple description"""
    ret = "<h1>Apple description:</h1>"
    ret += apple_description()
    ret += f"<br><br><a href={url_for('view_apple')}>[back]</a> |"
    ret += f"<a href={url_for('index')}>[home]</a>"

    return ret


@app.cli.command()
def test():
    """
    Rulare 'unit tests'
    
    Apelare pytest din aplicatia systest, cu ajutorul comenzii flask.
    
    """
    import pytest
    sys.exit(pytest.main(["."]))
#    ************* Module app.fructe
#app/fructe.py:61:4: C0415: Import outside toplevel (pytest) (import-outside-toplevel)
#app/fructe.py:61:4: W0611: Unused import pytest (unused-import)


if __name__ == '__main__':
    app.run(host='127.0.0.1')
