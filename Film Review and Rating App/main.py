from information import Information

def information():
    title = input("Film Title: ")
    director = input("Director: ")
    release_year = int(input("Release Year: "))
    review = input("Review: ")
    rating = float(input("Rating: "))

    new_movie = Information(title,director,release_year,review,rating)
    return new_movie

if __name__ == "__main__":
    new_movie = information()
    print(new_movie)

