class User:
    def __init__(self, name, reviews = [], wishlist = [], id = None):
        self.name = name
        self.reviews = reviews
        self.wishlist = wishlist
        self.id = id
