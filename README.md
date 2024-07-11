![Legend of Zelda Recipe API](src/Recipe%20API.png)

This is a Flask API that serves JSON information on The Legend of Zelda: Breath of the Wild (BotW) and Tears of the Kingdom (TotK) recipes, elixirs, and items.

## Setup

1. Install the dependencies:
    ```
    pip install -r requirements.txt
    ```

2. Seed the database:
    ```
    python seed.py
    ```

3. Run the application:
    ```
    python run.py
    ```

## API Endpoints

- **GET /recipes**: Returns a list of all recipes.
- **GET /elixirs**: Returns a list of all elixirs.
- **GET /items**: Returns a list of all items.
