from flask import Flask, jsonify, request
from app import app, db
from app.models import *

@app.route("/")
def index():
    return "Hello world!"

@app.route("/api/v1/pharmacy/inventory", methods=['GET'])
def get_pharmacy_inventory():
    if request.args.get('address') is None:
        raise InvalidUsage('Invalid address provided', status_code=400)
    medicines = []
    medicines.append({'name': 'Claritin 200mg', 'serial': 1234})
    medicines.append({'name': 'Claritin 200mg', 'serial': 2345})
    medicines.append({'name': 'Claritin 200mg', 'serial': 3456})
    medicines.append({'name': 'Tylenol 200mg', 'serial': 4567})
    medicines.append({'name': 'Tylenol 300mg', 'serial': 5678})
    medicines.append({'name': 'Tylenol 400mg', 'serial': 6789})
    return jsonify(medicines=medicines)

@app.route("/api/v1/pharmacy/info", methods=['GET'])
def get_pharmacy_info():
    if request.args.get('address') is None:
        raise InvalidUsage('Invalid address provided', status_code=400)
    print request.args.get('address')
    print Pharmacy.query.filter(Pharmacy.address == request.args.get('address'))
    lat = '123.456'
    lng = '234.567'
    hours = []
    hours.append([0, 1439])
    hours.append([0, 1439])
    hours.append([0, 1439])
    hours.append([0, 1439])
    hours.append([0, 1439])
    hours.append([0, 1439])
    hours.append([0, 1439])
    name = "test pharmacy"
    email = "testpharmacy@example.com"
    return jsonify(location={"lat": lat, "lng": lng},
                    hours=hours,
                    name=name,
                    email=email)

@app.route("/api/v1/pharmacy/presentorders", methods=['GET'])
def get_pharmacy_present_orders():
    if request.args.get('address') is None:
        raise InvalidUsage('Invalid address provided', status_code=400)
    orders = []
    orders.append({'customer': 'John Doe', 'name': 'Claritin 200mg', 'quantity': 50, 'price': '3.99'})
    orders.append({'customer': 'Jane Doe', 'name': 'Claritin 200mg', 'quantity': 100, 'price': '7.49'})
    orders.append({'customer': 'John Smith', 'name': 'Claritin 200mg', 'quantity': 200, 'price': '12.99'})
    orders.append({'customer': 'Jane Smith', 'name': 'Tylenol 200mg', 'quantity': 100, 'price': '6.99'})
    orders.append({'customer': 'Weter Poo', 'name': 'Tylenol 300mg', 'quantity': 100, 'price': '7.99'})
    orders.append({'customer': 'Peter Woo', 'name': 'Tylenol 400mg', 'quantity': 100, 'price': '8.99'})
    return jsonify(num_orders=len(orders), orders=orders)

@app.route("/api/v1/pharmacy/pastorders", methods=['GET'])
def get_pharmacy_past_orders():
    if request.args.get('address') is None:
        raise InvalidUsage('Invalid address provided', status_code=400)
    orders = []
    orders.append({'name': 'Claritin 200mg', 'quantity': 50, 'price': '3.99'})
    orders.append({'name': 'Claritin 200mg', 'quantity': 100, 'price': '7.49'})
    orders.append({'name': 'Claritin 200mg', 'quantity': 200, 'price': '12.99'})
    orders.append({'name': 'Tylenol 200mg', 'quantity': 100, 'price': '6.99'})
    orders.append({'name': 'Tylenol 300mg', 'quantity': 100, 'price': '7.99'})
    orders.append({'name': 'Tylenol 400mg', 'quantity': 100, 'price': '8.99'})
    return jsonify(num_orders=len(orders), orders=orders)

@app.route("/api/v1/users/pharmacies", methods=['GET'])
def get_valid_pharmacies():
    if request.args.get('medicine_name') is None:
        raise InvalidUsage('Invalid medicine name provided', status_code=400)
    if request.args.get('latitude') is None:
        raise InvalidUsage('Invalid latitude provided', status_code=400)
    if request.args.get('longitude') is None:
        raise InvalidUsage('Invalid longitude provided', status_code=400)
    locations = []
    locations.append({'latitude': '123.456', 'longitude': '123.456'})
    locations.append({'latitude': '23.456', 'longitude': '23.456'})
    locations.append({'latitude': '3.456', 'longitude': '3.456'})
    return jsonify(num_locations=len(locations), locations=locations)

class InvalidUsage(Exception):
    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['error'] = self.message
        return rv

@app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response
