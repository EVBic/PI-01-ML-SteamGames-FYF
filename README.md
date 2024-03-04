
# <h1 align=center>  Find-Your-Fun <h1>
## <h4 align=center> **PROJECT Nº1**</h4>
### <h2 align=center> Machine Larning Steam Games <h2>
<p align="center"> img 
![Pandas](https://img.shields.io/badge/-Pandas-333333?style=flat&logo=pandas)>
![Numpy](https://img.shields.io/badge/-Numpy-333333?style=flat&logo=numpy)
![Matplotlib](https://img.shields.io/badge/-Matplotlib-333333?style=flat&logo=matplotlib)
![Seaborn](https://img.shields.io/badge/-Seaborn-333333?style=flat&logo=seaborn)
![Scikitlearn](https://img.shields.io/badge/-Scikitlearn-333333?style=flat&logo=scikitlearn)
![FastAPI](https://img.shields.io/badge/-FastAPI-333333?style=flat&logo=fastapi)
![Docker](https://img.shields.io/badge/-Docker-333333?style=flat&logo=docker)
![Render](https://img.shields.io/badge/-Render-333333?style=flat&logo=render)
</p>

<h2 align=center> Game Recommendation System</h2>
<h2 align=center>🎮 **Machine Learning Operations (MLOps)** 🎮</h2>
<h3 align=center> Henry's Labs</h3>
<h2 align=center> By Maria Eva Bichi</h2>

!(Find Your Fun Image) MLInt\Datasets\Images\FYF_Main.jpeg

## Project Overview:  :white_circle:

This project presents a game recommendation system based on game similarity. It utilizes game information to identify similar games and provides functionalities through API endpoints. The project includes a notebook for ETL, EDA, and endpoint function creation, a main.py file with API information, and a data folder containing the project's parquet and csv files.

This game recommendation system represents a valuable tool for gamers, researchers, and game developers. Its data-driven approach fosters personalized recommendations, facilitates game discovery, and offers valuable insights into the gaming landscape.

## Data Preprocessing: :white_circle:

The project employs a meticulous data cleaning process:

Unnesting Dictionaries: Embedded dictionaries within columns are meticulously unraveled to improve data accessibility.
Column Elimination: Superfluous columns are strategically removed to streamline the dataset and enhance focus on relevant information.
Date Formatting: Dates are meticulously converted to a uniform format, ensuring consistency and facilitating analysis.
Data Type Conversion: Specific columns undergo data type adjustments to optimize data representation and analytical operations.
Sentiment Analysis: Exclusively for the df_reviews dataset, the original reviews column is replaced with a new one generated through sentiment analysis. This new column categorizes reviews as negative, positive, or neutral, facilitating deeper insights into user sentiment.

## Project structure: :white_circle:

project with its file and folder structure.

![Alt text]()

The main files developed (the content of which will be described in detail and precisely in the following section) are:
- ETL_Games_ITems.ipynb
- ETL_Steam_Games.ipynb
- ETL_Games_Reviews.ipynb
- EDA.ipynb
- Functions_UserID.ipynb
- Functions_ProductId.ipynb
- main_F.py



## Data source: :white_circle:

**[Dataset](https://drive.google.com/drive/folders/1HqBG2-sUkz_R3h1dZU5F2uAzpRn7BSpj)**
<br/>

Three JSON files were provided for this project:

australian_user_reviews.json is a dataset that contains the comments that users made about the games they play, as well as additional data such as whether or not they recommend that game, funny emoticons, and statistics on whether or not the comment was useful to other users. It also presents the id of the commenting user with their profile url and the id of the commenting game.

australian_users_items.json is a dataset that contains information about the games played by all users, as well as the accumulated time each user played a given game.

output_steam_games.json is a dataset that contains data related to the games themselves, such as titles, developer, prices, technical characteristics, tags, among other data.

The details of each of the variables in the data sets are found in the Card_Index document.

## <h1 align=center> Steam Game Recommendation API</h1>

The Steam Game Recommendation API provides game recommendations based on user behavior and data from games available on the Steam platform.

## How It Works :white_circle:

The API employs a collaborative filtering algorithm based on similarity calculations between games. Here's the general process:

1. User Input: Users provide a game ID as a parameter in the URL when making a GET request to `/recomendacion_juego/{product_id}`.

2. Reference Game Data Retrieval: The API retrieves data for the reference game using the provided user ID from a CSV file containing information about Steam games.

3. Text Processing: The API combines tags and genres from the reference game into a single text string and creates a TF-IDF vectorizer.

4. Similarity Calculation: The API divides the workload into batches of games from the CSV file and calculates the cosine similarity between the reference game and each game in the batch using the TF-IDF vectorizer.

5. Game Recommendation: The API identifies similar games to provide recommendations.

## `userdata` Function :white_circle:

In addition to the main recommendation function, the project also includes a function that, given a user ID:

- Returns the amount of money spent.
- Calculates the percentage of recommended games.
- Provides the count of items.

## Other Functions

The API includes several other functions:

- `countreviews`: Given two dates, it returns the number of users who submitted reviews between those dates and the percentage of positive (True) recommendations they made.
- `genre`: Accepts a video game genre as a parameter and ranks it based on the total hours played.
- `userforgenre`: Given a genre, it lists the top 5 users with the most gameplay hours in that genre, along with their user IDs and profile URLs.
- `developer`: Takes a developer name and returns the number of items developed by that company and the percentage of free content relative to the total.
- `sentiment_analysis`: Given a game release year, it provides a list of review records categorized by sentiment (Negative, Neutral, Positive).
- `recomendacion_juego`: Given a game name, it returns 5 recommended games similar to the input.

## Support material :white_circle:

**[links de ayuda](https://raw.githubusercontent.com/pjr95/PI_ML_OPS/main/Material%20de%20apoyo.md)**
**[links de ayuda]
**[links de ayuda]
<br/>