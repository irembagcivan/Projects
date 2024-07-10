class Information():
    def __init__(self,title,director,release_year,review,rating):
        self.title = title
        self.director = director
        self.release_year = release_year
        self.review = review
        self.rating = rating

    def __str__(self):
        return f"Film Title: {self.title}\nDirector:{self.director}\nRelease Year: {self.release_year}\nReview: {self.review}\nRating: {self.rating}"