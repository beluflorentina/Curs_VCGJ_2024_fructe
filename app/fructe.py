from flask import Flask, url_for
from lib.biblioteca_fructe import *

app = Flask(__name__)


@app.route('/', methods=['GET'])
def index():
    ret = "<h1>Fructe</h1>"
    ret += f"<a href={url_for('view_apple')}>Apple - Ana-Ioana Cristescu</a>"
    return ret


@app.route('/apple', methods=['GET'])
def view_apple():
    color = apple_color()
    description = apple_description()

    ret = "<h1>Apple</h1>"

    ret += f"<a href={url_for('view_apple_color')}>[view color]</a> | "
    ret += f"<a href={url_for('view_apple_description')}>[view description]</a>"
    ret += f"<br><br><a href={url_for('index')}>Go back home</a> | "

    return ret


@app.route('/apple/color', methods=['GET'])
def view_apple_color():
    ret = "<h1>Apple color:</h1>"
    ret += apple_color()
    ret += f"<br><br><a href={url_for('view_apple')}>[back]</a> |"
    ret += f"<a href={url_for('index')}>[home]</a>"
    return ret


@app.route('/apple/description', methods=['GET'])
def view_apple_description():
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


if __name__ == '__main__':
    app.run(host='127.0.0.1')
