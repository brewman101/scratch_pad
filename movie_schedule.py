current_movies ={'The God Father': '11:00 AM',
                 'Die Hard' : '1:00 PM',
                 'Toy Story': '2:00 PM'
}

print("We're showing the following movies:")
for showing in current_movies:
    print(showing)

movie=input("What movie would you like the showtime for? \n")

showtime=current_movies.get(movie)

if showtime:
    print(movie, "is showing at", showtime)
else:
    print("Your selection was incorrect, try again")