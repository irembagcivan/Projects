class Film():
    def __init__(self,title,director,release_year,review,rating):
        self.title = title
        self.director = director
        self.release_year = release_year
        self.review = review
        self.rating = rating

    def __str__(self):
            return f"Title: {self.title}, Director: {self.director}, Year: {self.release_year}, Rating: {self.rating}\nReview: {self.review}"

class Film_Review():
    def __init__(self):
        self.films = []

    def add_film(self):
        title = input("Film Title: ")
        director = input("Director: ")
        release_year = int(input("Release Year: "))
        review = input("Review: ")
        rating = float(input("Rating: "))
        film = Film(title,director,release_year,review,rating)
        self.films.append(film)

    def list_films(self):
        if not self.films:
            print("No films added yet!")
            return
        else:
            for film in self.films:
                print(film)

    def search_films_by_titles(self):
        title = input("Enter the title to search for: ")

        found_films =[]

        for film in self.films:
            if title.lower() in Film.title.lower():
                found_films.append(film)
        
        if found_films:
            for film in found_films:
                print(film)
        else:
            print("No films found!")
                  
             
         
    def menu(self):
            while True:
                print("1. Add a film")
                print("2. List all films")
                print("3. Search films by title")
                print("6. Exit")
                choice = input("Choose an option: ")

                if choice == '1':
                    self.add_film()
                elif choice == '2':
                    self.list_films()
                elif choice == '3':
                    self.search_films_by_title()
                elif choice == '6':
                    print("Exiting the application.")
                    break
                else:
                    print("Invalid choice, please try again.")


if __name__ == "__main__":
    app = Film_Review()
    app.menu()