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
medicines | dict(string->string, string->int) | The name and serial of each medication in stock
