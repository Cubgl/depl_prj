import os

from flask import Flask, url_for

app = Flask(__name__)


@app.route("/")
def index():
    return f'''Привет от приложения Flask Teacher <br>
           <img src="{url_for('static', filename='img/Колобок.png')}">'''


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)