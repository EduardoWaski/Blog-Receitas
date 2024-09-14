class User:
    def __init__(self, username, password, favourite_receipts=[], is_admin=False):
        self.username = username
        self.password = password
        self.favourite_receipts = favourite_receipts
        self.is_admin = is_admin

class Recipe:
    def __init__(self, image, name, preparation, ingredients, category):
        self.image = image
        self.name = name
        self.preparation = preparation
        self.ingredients = ingredients
        self.category = category
        self.comments = []
        self.favourited_by = []

class Comment:
    def __init__(self, user_id, receipt_id, text):
        self.user_id = user_id
        self.receipt_id = receipt_id
        self.text = text