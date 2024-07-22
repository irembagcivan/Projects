class Film():
    def __init__(self,title,director,release_year,review,rating):
        self.title = title
        self.director = director
        self.release_year = release_year
        self.review = review
        self.rating = rating

    def __str__(self):
            return f"Title: {self.title}, Director: {self.director}, Year: {self.release_year}, Rating: {self.rating}, Review: {self.review}"

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
        print("")
        self.films.append(film)

    def list_films(self):
        if not self.films:
            print("No films added yet!")
            print("")
            return
        else:
            for film in self.films:
                print(film)
                print("")

    def search_films_by_titles(self):
        title = input("Enter the title to search for: ")
        found_films =[]

        for film in self.films:
            if title.lower() in Film.title.lower():
                found_films.append(film)
        
        if found_films:
            for film in found_films:
                print(film)
                print("")
        else:
            print("No films found!")
            print("")

    def list_films_by_year(self):
        year = int(input("Enter the release year to list films: "))
        found_films = []

        for film in self.films:
            if film.release_year == year:
                found_films.append(film)
        
        if found_films:
            for film in found_films:
                print(film)
                print("")
        else:
            print("No films found for that year!")
            print("")
             
         
    def menu(self):
            while True:
                print("1. Add a film")
                print("2. List all films")
                print("3. Search films by title")
                print("4. List films by release year")
                print("5. Exit")
                choice = input("Choose an option: ")

                if choice == '1':
                    self.add_film()
                elif choice == '2':
                    self.list_films()
                elif choice == '3':
                    self.search_films_by_titles()
                elif choice == '4':
                    self.list_films_by_year()
                elif choice == '5':
                    print("Exiting the application.")
                    break
                else:
                    print("Invalid choice, please try again.")


if __name__ == "__main__":
    app = Film_Review()
    app.menu()