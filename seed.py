import json
from app import create_app
from app.database import db
from app.models import Recipe, Elixir, Item

app = create_app()

def load_data_from_json():
    with open('data/data.json') as file:
        data = json.load(file)
    return data

def seed_data(data):
    with app.app_context():
        db.create_all()

        # Add recipes
        recipes = [Recipe(name=recipe['name'], ingredients=recipe['ingredients']) for recipe in data['recipes']]
        
        # Add elixirs
        elixirs = [Elixir(name=elixir['name'], effects=elixir['effects']) for elixir in data['elixirs']]
        
        # Add items
        items = [Item(name=item['name'], description=item['description']) for item in data['items']]

        db.session.bulk_save_objects(recipes + elixirs + items)
        db.session.commit()
        print("Database seeded with JSON data!")

if __name__ == '__main__':
    data = load_data_from_json()
    seed_data(data)
