from app import db
import time

DAYS = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

class Pharmacy(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=False)
    address = db.Column(db.String(256), unique=True)
    latitude = db.Column(db.String(16), unique=False)
    longitude = db.Column(db.String(16), unique=False)
    email = db.Column(db.String(64), unique=False)
    hours = db.relationship('Hours', backref='pharmacy', lazy='dynamic')
    inventory = db.relationship('Inventory', backref='pharmacy', lazy='dynamic')
    orders = db.relationship('Orders', backref='pharmacy', lazy='dynamic')

    def __repr__(self):
        return '<Pharmacy {} - {} ({}, {}, {}) - {}>'.format(self.id, self.name, self.address, self.latitude, self.longitude, self.email)

class Hours(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pharm_id = db.Column(db.Integer, db.ForeignKey('pharmacy.id'), unique=False)
    day_of_week = db.Column(db.Integer, unique=False)
    opening_time = db.Column(db.Integer, unique=False)
    closing_time = db.Column(db.Integer, unique=False)

    def __repr__(self):
        return '<Pharmacy {} - {} {} to {}>'.format(self.pharm_id, DAYS[self.day_of_week], self.min_to_24h(self.opening_time), self.min_to_24h(self.closing_time))

    def min_to_24h(self, minutes):
        return '{0}:{1:0>2}'.format(minutes/60, minutes%60)

class Orders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pharm_id = db.Column(db.Integer, db.ForeignKey('pharmacy.id'), unique=False)
    customer = db.Column(db.String(64), unique=False)
    medicine = db.Column(db.String(128), unique=False)
    quantity = db.Column(db.Integer, unique=False)
    price = db.Column(db.Float, unique=False)
    fulfilled = db.Column(db.Boolean, unique=False)
    timestamp = db.Column(db.Integer, unique=False)

    def __init__(self, customer_name, medicine_name, qty, pharmacy_id):
        self.pharm_id = pharmacy_id
        self.customer = customer_name
        self.medicine = medicine_name
        self.quantity = qty
        inv = Inventory.query.filter(Inventory.pharm_id == self.pharm_id).filter(Inventory.name == self.medicine).first()
        self.price = inv.price * qty
        self.fulfilled = False
        self.timestamp = int(time.time())

    def __repr__(self):
        return '<Order {} at {} - {} ({} for ${}) for {} at {} ({})'.format(self.id, self.pharm_id, self.medicine, self.quantity, self.price, self.customer, self.timestamp, 'Fulfilled' if self.fulfilled else 'Unfulfilled')

class Inventory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pharm_id = db.Column(db.Integer, db.ForeignKey('pharmacy.id'), unique=False)
    name = db.Column(db.String(128), unique=False)
    serial = db.Column(db.Integer, unique=False)
    price = db.Column(db.Float, unique=False)

    def __repr__(self):
        return '<Inventory {} - Pharmacy {} - {} ({}, ${})'.format(self.id, self.pharm_id, self.name, self.serial, self.price)
