import streamlit as st
from surprise import Dataset, Reader, SVD
from surprise.model_selection import train_test_split

# Load the data
import pandas as pd
df = pd.read_csv("http://files.grouplens.org/datasets/movielens/ml-100k/u.data", sep='\t', names=["user_id", "item_id", "rating", "timestamp"])
reader = Reader(rating_scale=(1, 5))
data = Dataset.load_from_df(df[['user_id', 'item_id', 'rating']], reader)

# Split into train/test sets
trainset, testset = train_test_split(data, test_size=0.25)

# Build the model
model = SVD()
model.fit(trainset)

# Streamlit app
st.title("Movie Recommendation System")
st.write("Enter a user ID and item ID to get a predicted rating.")

user_id = st.number_input("Enter User ID:", min_value=1, max_value=1000)
item_id = st.number_input("Enter Item ID:", min_value=1, max_value=1000)

if st.button("Predict Rating"):
    prediction = model.predict(user_id, item_id)
    st.write(f"Predicted Rating: {prediction.est:.2f}")
