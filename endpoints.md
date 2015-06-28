# Interfaces

### GET /api/v1/pharmacy/info

Get information about this pharmacy.

##### Request Parameters

Request parameter | Value type | Value
---|---|---
address | string | The address of this pharmacy (URL encoded)

##### Response

This method returns a JSON object containing the following key/value pairs:

Response | Value type | Value
---|---|---
location | dict(string->float, string->float) | Latitude ("lat") and longitude ("lng") of this pharmacy
hours | array(array(int, int, int)) | Array containing times this pharmacy is open. First int represents day of week (Sunday = 0), 2nd represents minutes after midnight that store opens, 3rd represents closing time.
name | string | Name of the pharmacy
email | string | Email of the pharmacy

### GET /api/v1/pharmacy/inventory

Grab the inventory of this pharmacy.

##### Request Parameters

Request parameter | Value type | Value
---|---|---
address | string | The address of this pharmacy (URL encoded)

##### Response

This method returns a JSON object containing the following key/value pairs:

Response | Value type | Value
---|---|---
num_medicines | int | The number of different medicines in stock at this pharmacy
medicines | dict(string->string, string->int, string->float) | The name, serial, and price of each medication in stock

### GET /api/v1/users/pharmacies

Grab a list of all pharmacies within a certain radius (default 10mi) that have this medication in stock.

##### Request Parameters

Request parameter | Value type | Value
---|---|---
medicine_name | string | The exact name of the medicine to search (URL encoded)
latitude | float | The user's current latitude
longitude | float | The user's current longitude
radius | float | (optional) The radius to search for pharmacies

##### Response

This method returns a JSON object containing the following key/value pairs:

Response | Value type | Value
---|---|---
num_locations | int | The number of different pharmacies meeting the search criteria
locations | array(dict) | An array of dictionaries containing the name, address, latitude/longitude, approximate distance of each pharmacy, as well as the name of the medication and its price

# TECHNOLOGY STACK
###Venmo (payment, ios interface)
###PayPal (payment, SMS interface)
###Twilio (SMS interface)
###swift
###obj-c
###python
###flask (backend for web architecture)
###javascript
###jquery/ajax
###html/css
###restful API
###SQL
###SQLALCHEMY
###HEROKU
###VPN
###Git
