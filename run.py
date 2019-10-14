from flask import Flask, make_response, jsonify
from api import api

app = Flask(__name__)
app.register_blueprint(api, url_prefix='/api')


@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)


if __name__ == '__main__':
    app.run(debug=True)
