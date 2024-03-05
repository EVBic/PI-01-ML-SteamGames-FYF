
# <h1 align=center>  Find-Your-Fun <h1>
## <h4 align=center> **PROJECT Nº1**</h4>
### <h2 align=center> Machine Larning Steam Games <h2>


<h2 align=center> Game Recommendation System</h2>
<h2 align=center>🎮 **Machine Learning Operations (MLOps)** 🎮</h2>
<h3 align=center> Henry's Labs</h3>
<h2 align=center> By Maria Eva Bichi</h2>
<h2 align=center> Try it out HERE==> [RenderLink](https://pi01-ml-render.onrender.com)</h2>

![Steam_Games](https://github.com/EVBic/PI-01-ML-SteamGames-FYF/blob/main/Images/FYF_Main.jpeg)

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

Project with its file and folder structure:


The main files developed (the content of which will be described in detail and precisely in the following section) are:
- ETL_Games_ITems.ipynb
- ETL_Steam_Games.ipynb
- ETL_Games_Reviews.ipynb
- EDA.ipynb
- Functions_DEF.ipynb
- Merge_DF.ipynb
- api.functions.py
- main.py


## Data source: :white_circle:

**[Dataset](https://drive.google.com/drive/folders/1HqBG2-sUkz_R3h1dZU5F2uAzpRn7BSpj)**
<br/>

Three JSON files were provided for this project:

australian_user_reviews.json is a dataset that contains the comments that users made about the games they play, as well as additional data such as whether or not they recommend that game, funny emoticons, and statistics on whether or not the comment was useful to other users. It also presents the id of the commenting user with their profile url and the id of the commenting game.

australian_users_items.json is a dataset that contains information about the games played by all users, as well as the accumulated time each user played a given game.

output_steam_games.json is a dataset that contains data related to the games themselves, such as titles, developer, prices, technical characteristics, tags, among other data.

The details of each of the variables in the data sets are found in the Card_Index document. [Index](https://github.com/EVBic/PI-01-ML-SteamGames-FYF/blob/main/Card_Index.md)


## <h1 align=center> Steam Game Recommendation API</h1>

The Steam Game Recommendation API provides game recommendations based on user behavior and data from games available on the Steam platform.

## How It Works :white_circle:

The API employs a collaborative filtering algorithm based on similarity calculations between games. Here's the general process:

1. User Input: Users provide a game ID as a parameter in the URL when making a GET request to `/game_recommendation/{item_id}`.

2. Reference Game Data Retrieval: The API retrieves data for the reference game using the provided user ID from a CSV file containing information about Steam games.

3. Text Processing: The API combines tags and genres from the reference game into a single text string and creates a TF-IDF vectorizer.

4. Similarity Calculation: The API divides the workload into batches of games from the CSV file and calculates the cosine similarity between the reference game and each game in the batch using the TF-IDF vectorizer.

5. Game Recommendation: The API identifies similar games to provide recommendations.


The API includes several other functions:


- `developer`: This function returns the number of items and the percentage of free content per year according to the developing company.

-  `User_Data`: This function returns the amount of money spent by the user, the percentage of recommendation based on `reviews.recommend`, and the quantity of items.
  
- `userforgenre`: Given a genre, returns the user who has played the most hours for the given genre and a list of the accumulation of hours played per year of release.
  
- `best_developer_year`:  This function returns the top 3 developers with the MOST recommended games by users for the given year. (reviews.recommend = True and positive comments).
  ![TopDev](https://github.com/EVBic/PI-01-ML-SteamGames-FYF/blob/main/Images/FYF_BestDev.jpeg)
  
- `dev_reviews_analysis`: This function returns a dictionary where the developer's name is the key, and the value is a list containing the total number of user review records categorized as positive or negative based on sentiment analysis.
  ![Reviews](https://github.com/EVBic/PI-01-ML-SteamGames-FYF/blob/main/Images/FYF_Reviews.jpeg)

  
## Other Functions

- `game_recommendation`: Given a game name, it returns 5 recommended games similar to the input.
  ![sentiment_analysis](https://github.com/EVBic/PI-01-ML-SteamGames-FYF/blob/main/Images/FYF_Sent_An1.jpeg)

## Support material :white_circle:

[links de ayuda](https://raw.githubusercontent.com/pjr95/PI_ML_OPS/main/Material%20de%20apoyo.md)

<br/>
