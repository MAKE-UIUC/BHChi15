from flask import Flask, jsonify, request
from flask import render_template
from flask.ext.login import login_required, current_user
from app import app, db
from app.models import *
from util import haversine

# URL Routing
@app.route("/index.html")
def index():
    return render_template("index.html")

@app.route("/inventory.html")
def inventory():
    return render_template("inventory.html")

@app.route("/orders.html")
def orders():
    return render_template("orders.html")

        
# API
@app.route("/api/v1/pharmacy/inventory", methods=['GET'])
def get_pharmacy_inventory():
    address = request.args.get('address')
    if address is None:
        raise InvalidUsage('Invalid address provided', status_code=400)
    pharm = Pharmacy.query.filter(Pharmacy.address == address).first()
    inventory = Inventory.query.filter(Inventory.pharm_id == pharm.id).all()
    medicines = []
    for inv in inventory:
        medicines.append({'name': inv.name, 'serial': inv.serial})
    return jsonify(num_medicines=len(medicines), medicines=medicines)

@app.route("/api/v1/pharmacy/info", methods=['GET'])
def get_pharmacy_info():
    address = request.args.get('address')
    if address is None:
        raise InvalidUsage('Invalid address provided', status_code=400)
    pharm = Pharmacy.query.filter(Pharmacy.address == address).first()
    hours_res = Hours.query.filter(Hours.pharm_id == pharm.id).all()
    hours = []
    for h in hours_res:
        hours.append([h.day_of_week, h.opening_time, h.closing_time])
    return jsonify(location={"lat": pharm.latitude, "lng": pharm.longitude},
                    hours=hours,
                    name=pharm.name,
                    email=pharm.email)

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
    medicine_name = request.args.get('medicine_name')
    latitude = request.args.get('latitude')
    longitude = request.args.get('longitude')
    radius = request.args.get('radius')
    if medicine_name is None:
        raise InvalidUsage('Invalid medicine name provided', status_code=400)
    if latitude is None:
        raise InvalidUsage('Invalid latitude provided', status_code=400)
    if longitude is None:
        raise InvalidUsage('Invalid longitude provided', status_code=400)
    if radius is None:
        radius = 10
    inventory = Inventory.query.filter(Inventory.name == medicine_name).all()
    locations = []
    for inv in inventory:
        pharm = Pharmacy.query.filter(Pharmacy.id == inv.pharm_id).first()
        dist = haversine(pharm.latitude, pharm.longitude, latitude, longitude)
        if dist <= radius:
            locations.append({'name': pharm.name, 'approx_dist': dist, 'latitude': pharm.latitude, 'longitude': pharm.longitude, 'address': pharm.address})
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
