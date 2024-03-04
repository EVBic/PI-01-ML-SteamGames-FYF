import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

df_reviews= pd.read_parquet(r"C:\Users\m_evi\OneDrive\Desktop\MLInt\Datasets\CleanDatasets\df_reviews_l.parquet")
df_genre_ranking = pd.read_parquet(r"C:\Users\m_evi\OneDrive\Desktop\MLInt\Datasets\CleanDatasets\df_genre_ranking.parquet")
df_playtime = pd.read_parquet(r"C:\Users\m_evi\OneDrive\Desktop\MLInt\Datasets\CleanDatasets\df_playtime.parquet")
df_funct_dev = pd.read_parquet(r"C:\Users\m_evi\OneDrive\Desktop\MLInt\Datasets\CleanDatasets\df_funct_dev.parquet")
df_expenses_items = pd.read_parquet(r"C:\Users\m_evi\OneDrive\Desktop\MLInt\Datasets\CleanDatasets\df_expenses_items.parquet")
df_recommendation= pd.read_csv(r"C:\Users\m_evi\OneDrive\Desktop\MLInt\Datasets\CleanDatasets\steam_games.csv")

def presentation():
    '''
     Home Page Displaying a Presentation

    Returns:
    HTMLResponse: HTML response displaying the presentation.
    '''
    return '''
    <html>
        <head>
            <title>API Steam Find Your Fun</title>
            <style>
                body {
                    font-family: Arial, sans-serif;
                    padding: 20px;
                }
                h1 {
                    color: #333;
                    text-align: center;
                }
                p {
                    color: white;
                    text-align: center;
                    font-size: 18px;
                    margin-top: 20px;
                    background-color: black;
                    padding: 10px;
                }
                .centered-button {
                background-color: black;
                color: white;
                padding: 10px 20px;
                border: none;
                border-radius: 5px; /* optional for rounded corners */
                display: block; /* Makes the button fill the available width */
                margin: 0 auto; /* Centers the button horizontally */
                cursor: pointer; /* Changes cursor to pointer on hover */
                }
            </style>
        </head>
        <body>
            <h1>FIND YOUR FUN</h1>
            <h1>Steam Video Game Queries API</h1>
            
            <p>Welcome to the Steam API, where you can make various queries related to the gaming platform.</p>
            <p><strong>INSTRUCTIONS:</strong></p>
            <p>Click the button below to interact with the API:</p>
            
            <button type="button" class="centered-button" onclick="window.location.href = window.location.href + 'docs'">API Docs</button>
            
            <p>Visit my profile on <a href="https://www.linkedin.com/in/maría-eva-bichi"><img alt="LinkedIn" src="https://img.shields.io/badge/LinkedIn-blue?style=flat-square&logo=linkedin"></a></p>
            <p>The development of this project is hosted on <a href="https://github.com/EVBic"><img alt="GitHub" src="https://img.shields.io/badge/GitHub-black?style=flat-square&logo=github"></a></p>
        </body>
    </html>
    '''

def developer(developer_name: str):
    # Filter games by the specified developer
    filtered_developer = df_funct_dev[df_funct_dev['developer'] == developer_name]

    # Count the number of games released per year
    game_count_by_year = filtered_developer.groupby('release_year')['item_id'].count()

    # Calculate the percentage of free games released per year
    free_games_percentage = (filtered_developer[filtered_developer['price'] == 0.0]
                             .groupby('release_year')['item_id']
                             .count() / game_count_by_year * 100).fillna(0).astype(int)

    # Create a DataFrame from the results dictionary
    results_df = pd.DataFrame({
        'Year': game_count_by_year.index,
        'Number of games': game_count_by_year.values,
        '% Free games': free_games_percentage.values
    })

    return results_df

def userdata(user_id):
    
    # Filter by the user of interest
    user = df_reviews[df_reviews['user_id'] == user_id]
    # Calculate the amount of money spent for the user of interest
    amount_money = df_expenses_items[df_expenses_items['user_id']== user_id]['price'].sum()
   
    # Search for the count_item for the user of interest    
    count_items = df_expenses_items[df_expenses_items['user_id']== user_id]['items_count'].iloc[0]
    
    # Calculate the total recommendations made by the user of interest
    total_recommendations = user['recommend'].sum()
    # Calculate the total reviews made by all users
    total_reviews = len(df_reviews['user_id'].unique())
    # Calculate the percentage of recommendations made by the user of interest
    percentage_recommendations = (total_recommendations / total_reviews) * 100
    
    return {
        'amount_money': amount_money,
        'percentage_recommendation': round(percentage_recommendations, 2),
        'total_items': count_items.astype(int)
    }

def userForGenre(genre):
    
    # Filter the dataframe by the genre of interest
    data_by_genre = df_playtime[df_playtime['genres'] == genre]
    # Group the filtered dataframe by user and sum the number of hours
    top_users = data_by_genre.groupby(['user_url', 'user_id'])['playtime_hours'].sum().nlargest(5).reset_index()
    
    # An empty dictionary is made to store the needed data
    top_users_dict = {}
    for index, row in top_users.iterrows():
        # User info goes through each row of the top 5 and saves it in the dictionary
        user_info = {
            'user_id': row['user_id'],
            'user_url': row['user_url']
        }
        top_users_dict[index + 1] = user_info
    
    return top_users_dict

def best_developer_year(year: int):
    # Replace non-numeric 'release_year' values with NaN
    df_reviews['release_year'] = pd.to_numeric(df_reviews['release_year'], errors='coerce')
    
    # Filter DataFrame by the given year and positive recommendations
    df_filtered = df_reviews[(df_reviews['release_year'] == year) & (df_reviews['recommend'] == True) & (df_reviews['sentiment_analysis'] == 2)]
    
    # Group by developer and count the recommendations
    df_grouped = df_filtered.groupby('developer').size()
    
    # Get the top 3 developers
    top_developers = df_grouped.nlargest(3).index.tolist()
    
    return {"Top 3 Developers": top_developers}

def dev_reviews_analysis(developer):
    # Filter the reviews for the specific developer
    reviews2 = df_reviews[df_reviews['developer'] == str(developer)]  # Convert developer name to a string
    
    # Initialize a dictionary to count the sentiment categories
    sentiment_counts = {'Negative': 0, 'Positive': 0}
    
    # Iterate through the reviews of the specified developer
    for index, row in reviews2.iterrows():
        sentiment = row['sentiment_analysis']
        sentiment_category = ''
        
        # Assign the corresponding sentiment category
        if sentiment == 0:
            sentiment_category = 'Negative'
        elif sentiment == 2:
            sentiment_category = 'Positive'
        else:
            # Skip reviews with missing or neutral sentiment
            continue
        
        # Increment the corresponding counter in the dictionary
        sentiment_counts[sentiment_category] += 1
    
    
    return {"developer": developer, "sentiment_counts": sentiment_counts}


import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def game_recommendation(item_id: int):

  
    # Filter games that match the given item ID
    filtered_game = df_recommendation[df_recommendation['item_id'] == item_id]

    # Get the genres of the given game
    game_genres = set(filtered_game['genres'].str.split(',').explode())

    # Filter games that share at least 1 genre with the given game
    recommended_games = df_recommendation[df_recommendation['genres'].apply(lambda x: len(set(x.split(',')).intersection(game_genres)) >= 1)]

    # Calculate cosine similarity between genre vectors of games
    recommended_games.loc[:, 'genres_vector'] = recommended_games['genres'].apply(lambda x: np.array([1 if genre in x else 0 for genre in game_genres]))
    filtered_game.loc[:, 'genres_vector'] = filtered_game['genres'].apply(lambda x: np.array([1 if genre in x else 0 for genre in game_genres]))
    recommended_games.loc[:, 'similarity'] = recommended_games.apply(lambda row: cosine_similarity([row['genres_vector']], [filtered_game['genres_vector'].iloc[0]])[0][0], axis=1)

    # Sort games by similarity and recommendation in descending order
    recommended_games = recommended_games.sort_values(['similarity'], ascending=[False])

    # Select the top 5 games with highest similarity and recommendation
    top_recommended_games = recommended_games.head(5)

    # Create a dictionary of recommended game names along with their developers
    recommended_games_dict = {}
    recommended_games_dict['Because you liked ' + filtered_game['item_name'].iloc[0] + ', you might also enjoy...'] = top_recommended_games[['item_name']].to_dict(orient='records')

    return recommended_games_dict