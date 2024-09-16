class User:
    def __init__(self, username, password, favourite_recipes=[], is_admin=False):
        self.username = username
        self.password = password
        self.favourite_recipes = favourite_recipes
        self.my_recipes = []
        self.is_admin = is_admin

class Recipe:
    def __init__(self, user_id, image_id, name, preparation, ingredients, category):
        self.user = user_id
        self.image_id = image_id
        self.name = name
        self.preparation = preparation
        self.ingredients = ingredients
        self.category = category
        self.comments = []
        self.favourited_by = []

class Comment:
    def __init__(self, user_id, recipe_id, text):
        self.user_id = user_id
        self.recipe_id = recipe_id
        self.text = text