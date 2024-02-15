# Create a dictionary named movie-ratings with at least five movies as keys
# and their ratings (out of 10) as values. Ask the user for a movie title. 
# Write a function named recommend_movie that takes the movie_rating dictionary 
# and the movie title as arguments. The function should check if the movie is in 
# the dictionary and recommend the movie if it has a rating of 8 or higher. 
# Otherwise, suggest movie titles that have a rating of 8 or higher. 
# If the movie is not found in the dictionary, it should still recommend movies that 
# are rated 8 or higher.

movie_ratings={"Interstellar": 9.9,         #Populate movie ratings dict
               "The Accountant": 9.2,
               "The Shining": 6.9,
               "Titanic": 8.7,
               "Batman": 5.2,
               "Zombie Land": 6.2}
 
def recommend_movie(ratings, title):
    recommended_movies = [] ## Currently showing recommended movies even if movie is good??? Fix

    if title in movie_ratings:
        if movie_ratings[title] >= 8:
            print(f"We recommend watching {title}.")
        else:
            print(f"{title} is not highly rated. You might enjoy these highly rated movies instead:")
    else:
        print(f"{title} is not found in our database. However, you might enjoy these highly rated movies:")
    
    for title, rating in movie_ratings.items():
        if rating >= 8:
            recommended_movies.append(title)
    
    print("\nRecommended Movies:")
    for title in recommended_movies:
        print(f"- {title}")

#asks for users movie
input_movie = input("Please enter a movie title: ")

#passes movie input into recommend_movie
recommend_movie(movie_ratings, input_movie)