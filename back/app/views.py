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
    pharm = Pharmacy.query.filter(Pharmacy.address.like('%{}%'.format(address))).first()
    if pharm is None:
        raise InvalidUsage('Invalid address provided', status_code=400)
    inventory = Inventory.query.filter(Inventory.pharm_id == pharm.id).all()
    medicines = []
    for inv in inventory:
        medicines.append({'name': inv.name, 'serial': inv.serial, 'price': inv.price})
    return jsonify(num_medicines=len(medicines), medicines=medicines)

@app.route("/api/v1/pharmacy/info", methods=['GET'])
def get_pharmacy_info():
    address = request.args.get('address')
    if address is None:
        raise InvalidUsage('Invalid address provided', status_code=400)
    pharm = Pharmacy.query.filter(Pharmacy.address.like('%{}%'.format(address))).first()
    if pharm is None:
        raise InvalidUsage('Invalid address provided', status_code=400)
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
    address = request.args.get('address')
    if address is None:
        raise InvalidUsage('Invalid address provided', status_code=400)
    pharm = Pharmacy.query.filter(Pharmacy.address.like('%{}%'.format(address))).first()
    if pharm is None:
        raise InvalidUsage('Invalid address provided', status_code=400)
    orders_res = Orders.query.filter(Orders.pharm_id == pharm.id).filter(Orders.fulfilled == False).all()
    orders = []
    for order in orders_res:
        orders.append({'customer': order.customer, 'medicine_name': order.medicine, 'quantity': order.quantity, 'price': order.price, 'timestamp': order.timestamp})
    return jsonify(num_orders=len(orders), orders=orders)

@app.route("/api/v1/pharmacy/pastorders", methods=['GET'])
def get_pharmacy_past_orders():
    address = request.args.get('address')
    if address is None:
        raise InvalidUsage('Invalid address provided', status_code=400)
    pharm = Pharmacy.query.filter(Pharmacy.address.like('%{}%'.format(address))).first()
    if pharm is None:
        raise InvalidUsage('Invalid address provided', status_code=400)
    orders_res = Orders.query.filter(Orders.pharm_id == pharm.id).filter(Orders.fulfilled == True).all()
    orders = []
    for order in orders_res:
        orders.append({'customer': order.customer, 'medicine_name': order.medicine, 'quantity': order.quantity, 'price': order.price, 'timestamp': order.timestamp})
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
    else:
        radius = float(radius)
    inventory = Inventory.query.filter(Inventory.name.like('%{}%'.format(medicine_name))).all()
    locations = []
    for inv in inventory:
        pharm = Pharmacy.query.filter(Pharmacy.id == inv.pharm_id).first()
        dist = haversine(pharm.latitude, pharm.longitude, latitude, longitude)
        if dist < radius:
            locations.append({'name': pharm.name, 'approx_dist': dist, 'latitude': pharm.latitude, 'longitude': pharm.longitude, 'address': pharm.address, 'medicine_name': inv.name, 'price': inv.price})
    return jsonify(num_locations=len(locations), locations=locations)

@app.route("/api/v1/users/order", methods=['POST'])
def make_order():
    json = request.get_json();
    customer_name = json['customer_name']
    medicine_name = json['medicine_name']
    quantity = json['quantity']
    pharm_id = json['pharmacy_id']
    if medicine_name is None:
        raise InvalidUsage('Invalid medicine name provided', status_code=400)
    if customer_name is None:
        raise InvalidUsage('Invalid customer name provided', status_code=400)
    if quantity is None:
        raise InvalidUsage('Invalid quantity provided', status_code=400)
    if pharm_id is None:
        raise InvalidUsage('Invalid pharmacy id provided', status_code=400)
    order = Orders(customer_name, medicine_name, quantity, pharm_id)
    db.session.add(order)
    db.session.commit()
    return jsonify(price=order.price)

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
