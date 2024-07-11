from marshmallow import Schema, fields

class RecipeSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    ingredients = fields.Str(required=True)

class ElixirSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    effects = fields.Str(required=True)

class ItemSchema(Schema):
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True)
    description = fields.Str(required=True)

recipe_schema = RecipeSchema()
elixir_schema = ElixirSchema()
item_schema = ItemSchema()
