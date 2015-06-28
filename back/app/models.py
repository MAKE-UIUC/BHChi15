from app import db

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
        return '<Pharmacy {} - {} ({}, {}, {}) - {}>'.format(id, name, address, latitude, longitude, email)

class Hours(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pharm_id = db.Column(db.Integer, db.ForeignKey('pharmacy.id'), unique=False)
    day_of_week = db.Column(db.Integer, unique=False)
    opening_time = db.Column(db.Integer, unique=False)
    closing_time = db.Column(db.Integer, unique=False)

    DAYS = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']

    def __repr__(self):
        return '<Pharmacy {} - {} {} to {}>'.format(pharm_id, DAYS[day_of_week], min_to_24h(opening_time), min_to_24h(closing_time))

    def min_to_24h(minutes):
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

    def __repr__(self):
        return '<Order {} at {} - {} ({} for ${}) for {} at {} ({})'.format(id, pharm_id, medicine, quantity, price, customer, timestamp, 'Fulfilled' if fulfilled else 'Unfulfilled')

class Inventory(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    pharm_id = db.Column(db.Integer, db.ForeignKey('pharmacy.id'), unique=False)
    name = db.Column(db.String(128), unique=False)
    serial = db.Column(db.Integer, unique=False)

    def __repr__(self):
        return '<Inventory {} - Pharmacy {} - {} ({})'.format(id, pharm_id, name, serial)
