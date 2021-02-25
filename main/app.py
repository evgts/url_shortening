from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import request
from flask import jsonify
import logging
from db import url_model
from utils import code_util
from cfg import host, port, db_uri

logging.basicConfig(filename='../debug.log', level=logging.DEBUG)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
db = SQLAlchemy(app)


@app.route('/shorten', methods=['POST'])
def shorten():
    """
    :method: POST
    :payload: {"url": "https://www.google.com/blah"}
    :return: {"url": "https://www.google.com/blah", "short_url": "http://127.0.0.1:5000/shorturl/wIJOrQ99KWNC7aA7QhGH"}
    """
    content = request.json
    url = content["url"]
    url_code = code_util.code_gen()

    for _ in range(5):
        urls_in_db = url_model.Urls.query.filter_by(url_code=url_code).all()
        if len(urls_in_db) > 0:
            url_code = code_util.code_gen()
        else:
            break
    else:
        return jsonify({"error": "DB duplicate error"}), 500

    short_url = "http://" + host + ":" + str(port) + "/shorturl/" + str(url_code)
    new_url = url_model.Urls(url=url, url_code=url_code, short_url=short_url)

    try:
        db.session.add(new_url)
        db.session.commit()
    except:
        return jsonify({"error": "DB error"}), 500

    return jsonify({"url": "%s" % url, "short_url": "%s" % short_url})


@app.route('/shorturl/<path:url_code>', methods=['GET'])
def full_url(url_code):
    """
    :method: GET
    :request: http://127.0.0.1:5000/shorturl/wIJOrQ99KWNC7aA7QhGH
    :return: {"url": "https://www.google.com/blah", "short_url": "http://127.0.0.1:5000/shorturl/wIJOrQ99KWNC7aA7QhGH"}
    """

    url = url_model.Urls.query.filter_by(url_code=url_code).first_or_404()

    return jsonify({"url": "%s" % url.url, "short_url": "%s" % url.short_url})


if __name__ == '__main__':
    app.run(host=host, port=port,debug=True)
