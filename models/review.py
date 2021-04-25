class Review:
    def __init__(self, whisky, rating, date, description=None, id=None):
        self.whisky = whisky
        self.rating = rating
        self.date = date
        self.description = description
        self.id = id