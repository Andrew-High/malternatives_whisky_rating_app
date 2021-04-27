class Review:
    def __init__(self, whisky, user, rating, date, description=None, id=None):
        self.whisky = whisky
        self.user = user
        self.rating = rating
        self.date = date
        self.description = description
        self.id = id