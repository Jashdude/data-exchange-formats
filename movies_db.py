import json
# Please use pip install prettytable command to install this package.
from prettytable import PrettyTable

# Assignment Question List
question_list = [
                 "1. What is the total number of movies included the sample data?",
                 "2. Which movie summary contains the most characters?",
                 "3. How many actors were born after 1970 and what were their last names?",
                 "4. Which movie had the most actors?",
                 "5. Which actors played more than one role in a single movie?"
                 ]

# My Answer List
answer_list = []

# Required Variable List
title_list = []
actor_list = []
role_count = []
unique_list = []
summary_dict = {}
actr_brn_aftr_1970 = {}
most_actors = {}
played_more_role = {}
unique_actor_list = {}


# Ingest the .json file
with open("movies_db.json", "r") as read_file:
    movies = json.load(read_file)
    # Loop through each movie and pull required information.
    for movie in movies:
        title_list.append(movie['title'])
        summary = movie['summary']

        # Compute the count of summary without counting spaces, for each movie and save it in Summary_dict.
        summary_dict[movie['title']] = len(summary) - summary.count(' ')
        actors = movie['actors']
        most_actors.update({movie['title']: len(actors)})

        # Build an actor list.
        for actor in actors:
            actor_list.append(actor)

        list = {movie['title']: [actor['first_name'] + ' ' + actor['last_name'] for actor in actors]}
        role_count.append(list)

    # Below piece of code computes most actors and the role count of actors played for each movie..
    for row in role_count:
        for key, val in row.items():
            # find distinct list of actors for each movie.
            unique_actor_list.update({key : [unique_list.append(x) for x in val if x not in unique_list]})

            # find role count for each actor in the movie.
            k, a = key, set([x for x in val if val.count(x) > 1])
            if a:
                played_more_role.update({k : a})

    # Pull distinct actor count for each movie.
    movie_count = {}
    for k, v in unique_actor_list.items():
        movie_count.update({k: len(v)})

    # This variable is tackle if we have 2 largest numbers of same value.
    highest = max(movie_count.values())
    most_actors_final = [(k,v) for k, v in movie_count.items() if v == highest]

    # Solution for 1st question.
    answer_list.append(f"There are {len(movies)} movies listed in the sample data, the list is {title_list} ")

    # Solution for 2nd question.
    movie_key, max_char = max(summary_dict.items(), key=lambda x: x[1])
    print(summary_dict)
    answer_list.append(f"{movie_key} has the maximum characters totaling {max_char} characters without counting spaces "
                       f"({len(summary)} characters with spaces).")

    # Below piece of code identifies the actors born after 1970 and their last names.
    for actor in actor_list:
        if int(actor['birth_date']) > 1970:
            actr_brn_aftr_1970[actor['last_name']] = actor['birth_date']
    answer_list.append(f"{len(actr_brn_aftr_1970)} actors were born after 1970. "
                       f"Their last names and birth years are: {actr_brn_aftr_1970}")

    # Solution for question 4.
    answer_list.append(f"The movie(s) {most_actors_final} has the most actors in the sample data")

    # Solution for question 5.
    answer_list.append(f"Actor(s) {[v for v in played_more_role.values()]} "
                       f"played more than one role in the movie(s) {[k for k in played_more_role.keys()]}")


# Below piece of code helps pretty print the Questions and Answers in a tabular format using Pretty Table.
result_table = PrettyTable(['Assignment Questions', 'Answers'])
for x in range(len(question_list)):
    result_table.add_row([question_list[x], answer_list[x]])
    result_table.align = "l"

print(result_table)
