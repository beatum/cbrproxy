import re

import requests
import xmltodict
from flask import Blueprint, request, jsonify, abort, make_response


api = Blueprint('api', __name__)


@api.route('/scripts/<path>', methods=['GET'])
def get_currency(path):

    if request.method == 'GET':

        if path != 'XML_daily.asp':
            return abort(400)
        else:
            date_req = request.args.get('date_req')
            match = re.search(r'[\d]{1,2}/[\d]{1,2}/[\d]{4}', date_req)
            if not match:
                return make_response(jsonify({'error': 'Bad Request'}), 400)

        url = f'http://www.cbr.ru/scripts/XML_daily.asp?date_req={date_req}'

        resp = requests.get(url)

        if not resp.raise_for_status():
            data = xmltodict.parse(resp.content)
            return jsonify(data)
        else:
            abort(400)
    else:
        abort(500)
