import logging

from flask import Flask, jsonify
from pyquocca.pgsql import FlaskPostgres

app = Flask(__name__)

db = FlaskPostgres()


@app.route("/")
def index():
    logging.info("Did a thing!")
    return jsonify(db.fetch_all("SELECT * FROM posts;"))


@app.route("/500")
def error():
    raise Exception("Oops!")


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
