class Review:
    def __init__(self, whisky_id, user_id, rating, date, description=None, id=None):
        self.whisky_id = whisky_id
        self.user_id = user_id
        self.rating = rating
        self.date = date
        self.description = description
        self.id = id