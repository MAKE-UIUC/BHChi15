# Interfaces

### GET /api/v1/pharmacy/inventory

Grab the inventory of this pharmacy.

##### Request Parameters

Request body data | Value type | Value
---|---|---
address | string | The address of this pharmacy (URL encoded)

##### Response

This method returns a JSON object containing the following key/value pairs:

Response data | Value type | Value
---|---|---
location | dict(string->float) | Latitude ("lat") and longitude ("lng") of this pharmacy
hours | array(array(int, int, int)) | Array containing times this pharmacy is open. First int represents day of week (Sunday = 0), 2nd represents minutes after midnight that store opens, 3rd represents closing time.
name | string | Name of the pharmacy
email | string | Email of the pharmacy
