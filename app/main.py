from flask import Flask, jsonify, abort, make_response, request
from mysql_utilities import *

app = Flask(__name__)


@app.errorhandler(404)
def not_found(error='Not found'):
    return make_response(jsonify({'error': str(error)}), 404)

@app.errorhandler(400)
def not_found(error="Bad request"):
    return make_response(jsonify({'error': str(error)}), 404)

@app.route('/api/v1/customers', methods=['POST'])
def create_customer():
    data = request.json
    if not data or 'name' not in data or 'email' not in data:
        abort(400, description="Missing email or name")
    create_customer_data(**data)
    return jsonify(get_customer_data(email=data['email'])), 201


@app.route('/api/v1/customers/<int:customer_id>', methods=['GET'])
def get_customer(customer_id):
    customer = get_customer_data(customer_id)
    if not customer:
        abort(404, description="Not found customer with id: {}".format(customer_id))
    return jsonify(customer)

@app.route('/api/v1/customers/<int:customer_id>', methods=['PUT'])
def update_customer(customer_id):
    customer = get_customer_data(customer_id)
    if not customer:
        abort(404)

    update_customer_data(customer_id, **request.json)
    return jsonify(get_customer_data(customer_id))

@app.route('/api/v1/customers/<int:customer_id>', methods=['delete'])
def delete_customer(customer_id):
    delete_customer_data(customer_id)
    return jsonify(get_customer_data(customer_id))

if __name__ == '__main__':
    create_tables()
    app.run(host='0.0.0.0', port=8001, debug=True)