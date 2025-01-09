import streamlit as st
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Load the ratings dataset
ratings_url = "http://files.grouplens.org/datasets/movielens/ml-100k/u.data"
df = pd.read_csv(ratings_url, sep='	', names=["user_id", "item_id", "rating", "timestamp"])

# Load the movies dataset
movies_url = "http://files.grouplens.org/datasets/movielens/ml-100k/u.item"
movies_df = pd.read_csv(movies_url, sep='|', encoding='latin-1', header=None, usecols=[0, 1], names=["item_id", "title"])

# Merge the datasets to map item IDs to movie titles
df = df.merge(movies_df, on="item_id")

# Pivot the data to create a user-item matrix
pivot_table = df.pivot(index='user_id', columns='title', values='rating').fillna(0)

# Calculate similarity matrix
similarity_matrix = cosine_similarity(pivot_table)

# Streamlit app
st.title("Movie Recommendation System")
st.write("Enter a User ID to get top similar users and recommended movies.")

# User input
user_id = st.number_input("Enter User ID:", min_value=1, max_value=pivot_table.index.max())

if st.button("Get Recommendations"):
    try:
        # Find the user index in the pivot table
        user_index = pivot_table.index.get_loc(user_id)

        # Calculate similarities for the given user
        similarities = similarity_matrix[user_index]

        # Get top 5 similar users (excluding the current user)
        similar_users = (-similarities).argsort()[1:6]

        # Display similar users
        st.write("Top 5 Similar Users:")
        for i, similar_user in enumerate(similar_users, start=1):
            st.write(f"{i}. User ID: {pivot_table.index[similar_user]}")

        # Recommend items based on similar users
        recommended_items = pivot_table.iloc[similar_users].mean(axis=0).sort_values(ascending=False).head(10)
        st.write("Recommended Movies:")
        st.write(recommended_items.index.tolist())

    except KeyError:
        st.write("User ID not found. Please enter a valid User ID.")
