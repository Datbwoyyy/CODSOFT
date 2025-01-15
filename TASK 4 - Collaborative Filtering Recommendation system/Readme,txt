# Movie Recommendation System

## Project Overview
This project is a **Movie Recommendation System** built using Python and deployed via **Streamlit**. The application allows users to enter a User ID to find similar users and get movie recommendations based on user preferences.

The project utilizes:
- **Pandas** for data manipulation
- **Cosine Similarity** from `sklearn` to calculate user similarities
- **Streamlit** to create a simple and interactive web application

---

## Features
- **Top 5 Similar Users**: The system identifies the top 5 users with the most similar movie preferences to the input user.
- **Recommended Movies**: The system recommends movies that the similar users have highly rated.

---

## How It Works
1. **Dataset**: The app uses the **MovieLens 100k dataset** provided by GroupLens Research.
   - `u.data`: Contains user ratings for different movies.
   - `u.item`: Contains movie titles corresponding to movie IDs.

2. **Data Processing**:
   - The datasets are loaded and merged to include both user ratings and movie titles.
   - The data is aggregated to remove duplicate entries.
   - A **User-Item Matrix** is created, and **Cosine Similarity** is applied to find similar users.

3. **Recommendations**:
   - The app identifies the top 5 similar users for the input user.
   - Based on the ratings of similar users, the app recommends the top 10 movies.

---

## How to Run the Application
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/movie-recommendation-system.git
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the Streamlit app:
   ```bash
   streamlit run app.py
   ```

---

## Requirements
- Python 3.7+
- Streamlit
- Pandas
- scikit-learn

---

## References
This project utilizes data and resources from the following sources:
1. **MovieLens Dataset**: Provided by [GroupLens Research](https://grouplens.org/datasets/movielens/)
   - License: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/)

2. **Streamlit Documentation**: [https://docs.streamlit.io/](https://docs.streamlit.io/)

3. **scikit-learn Documentation**: [https://scikit-learn.org/](https://scikit-learn.org/)

---

## Disclaimer
This project is for educational purposes only. The MovieLens dataset is owned by GroupLens Research. The project follows the dataset's licensing terms and is not intended for commercial use.

---

## Author
**Victor Egbo**
- LinkedIn: [Victor Egbo](https://www.linkedin.com/in/victor-egbo-9401b525b/)
- Email: theegbovictor@gmail.com

---

## License
This project is licensed under the **MIT License**. You are free to use, modify, and distribute this project, provided that appropriate credit is given.

