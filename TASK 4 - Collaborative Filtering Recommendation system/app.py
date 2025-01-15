import streamlit as st
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Streaming the dataset
df = pd.read_csv("http://files.grouplens.org/datasets/movielens/ml-100k/u.data", sep='	', names=["user_id", "item_id", "rating", "timestamp"])

# Streaming the movie titles
movie_titles = pd.read_csv("http://files.grouplens.org/datasets/movielens/ml-100k/u.item", sep='|', encoding='latin-1', usecols=[0, 1], names=["item_id", "title"])

# Merge the ratings and titles
df = pd.merge(df, movie_titles, on="item_id")

# Aggregate ratings to remove duplicates
df = df.groupby(['user_id', 'title']).rating.mean().reset_index()

# Pivot the data to create a user-item matrix
pivot_table = df.pivot(index='user_id', columns='title', values='rating').fillna(0)

# Calculate similarity matrix
similarity_matrix = cosine_similarity(pivot_table)

# Streamlit app
st.title("Simple Movie Recommendation System")
st.write("Enter a User ID to get top similar users and recommended movies.")

user_id = st.number_input("Enter User ID:", min_value=1, max_value=pivot_table.shape[0])

if st.button("Get Recommendations"):
    try:
        user_index = pivot_table.index.get_loc(user_id)
        similarities = similarity_matrix[user_index]
        similar_users = (-similarities).argsort()[1:6]  # Top 5 similar users
        
        st.write("Top 5 Similar Users:")
        for i, similar_user in enumerate(similar_users, start=1):
            st.write(f"{i}. User ID: {pivot_table.index[similar_user]}")

        # Recommend items based on similar users
        recommended_items = pivot_table.iloc[similar_users].mean(axis=0).sort_values(ascending=False).head(10)
        st.write("Recommended Movies:")
        st.write(recommended_items.index.tolist())

    except KeyError:
        st.write("User ID not found. Please enter a valid User ID.")

