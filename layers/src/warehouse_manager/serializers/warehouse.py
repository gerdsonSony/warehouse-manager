from marshmallow import Schema, fields


class WarehouseSerializer(Schema):
    id = fields.Int()
    name = fields.String()
    latitude = fields.Float()
    longitude = fields.Float()
