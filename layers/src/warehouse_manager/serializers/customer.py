from marshmallow import Schema, fields


class CustomerSerializer(Schema):
    id = fields.Int()
    name = fields.String()
    latitude = fields.Float()
    longitude = fields.Float()
