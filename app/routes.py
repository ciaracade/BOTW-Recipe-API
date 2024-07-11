from flask import Blueprint, jsonify
from .models import Recipe, Elixir, Item
from .schemas import recipe_schema, elixir_schema, item_schema

bp = Blueprint('api', __name__)

@bp.route('/recipes', methods=['GET'])
def get_recipes():
    recipes = Recipe.query.all()
    return jsonify(recipe_schema.dump(recipes, many=True))

@bp.route('/elixirs', methods=['GET'])
def get_elixirs():
    elixirs = Elixir.query.all()
    return jsonify(elixir_schema.dump(elixirs, many=True))

@bp.route('/items', methods=['GET'])
def get_items():
    items = Item.query.all()
    return jsonify(item_schema.dump(items, many=True))
