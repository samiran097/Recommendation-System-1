## Function def
import os
import numpy as np
import pandas as pd

def prepare_data():
    """ This function is used to read the data from two csv files
    """

    credits = pd.read_csv("tmdb_5000_credits.csv")
    movies_df = pd.read_csv("tmdb_5000_movies.csv")
    print("Credits:",credits.shape)
    print("Movies Dataframe:",movies_df.shape)

    return credits,movies_df


def give_rec(title, sig=sig):
    # Get the index corresponding to original_title
    idx = indices[title]

    # Get the pairwsie similarity scores 
    sig_scores = list(enumerate(sig[idx]))

    # Sort the movies 
    sig_scores = sorted(sig_scores, key=lambda x: x[1], reverse=True)

    # Scores of the 10 most similar movies
    sig_scores = sig_scores[1:11]

    # Movie indices
    movie_indices = [i[0] for i in sig_scores]

    # Top 10 most similar movies
    return movies_cleaned_df['original_title'].iloc[movie_indices]


credits,movies_df = prepare_data()
print(credits.head(5))

credits_column_renamed = credits.rename(index=str, columns={"movie_id": "id"})
movies_df_merge = movies_df.merge(credits_column_renamed, on='id')

movies_cleaned_df = movies_df_merge.drop(columns=['homepage', 'title_x', 'title_y', 'status','production_countries'])
# movies_cleaned_df.head()