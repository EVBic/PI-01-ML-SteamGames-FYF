from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse
from fastapi import FastAPI
from fastapi.responses import JSONResponse
import api_functions as afdef
import importlib


app = FastAPI()

# Functions
@app.get(path="/", response_class=HTMLResponse,
         tags=["Home"])

def home():
    '''
    Home Page Displaying a Presentation

    Returns:
    HTMLResponse: HTML response displaying the presentation.
    '''
    return afdef.presentation()

@app.get(path = '/developer', response_class=JSONResponse,
          description = """ <font color="white">
                        1. Click on "Try it out".<br>
                        2. Enter the developer's name in the box below.<br>
                        3. Scroll to "Resposes" to see the number of items and percentage of Free content per year from that developer.
                        </font>
                        """,
         tags=["General Inquiries"])

def developer(developer: str = Query(..., 
                            description="Developer", 
                            example='Laush Dmitriy Sergeevich')):
    return afdef.developer(developer)


@app.get(path = '/userdata',
          description = """ <font color="blue">
                        INSTRUCTIONS<br>
                        1. Click on "Try it out".<br>
                        2. Enter the user_id in the box below.<br>
                        3. Scroll to "Resposes" to see the amount of money spent by the user, the percentage of recommendations made by the user and the number of items the user has.
                        </font>
                        """,
         tags=["General Inquiries"])

def userdata(user_id: str = Query(..., 
                                description="Identificador único del usuario", 
                                example="js41637")):
        
    return afdef.userdata(user_id)
    
    
"""@app.get(path = '/genre',
          description =  <font color="blue">
                        1. Click on "Try it out".<br>
                        2. Enter the genre of the game in the box below. <br>
                        3. Scroll to "Resposes" to see where you are in the ranking.
                        </font>
                       
         tags=["General Inquiries"])
def genre(genero: str = Query(..., 
                            description="Video Game Genre", 
                            example='Simulation')):
    return af.genre(genero)
"""

@app.get(path = '/userForGenre',
          description = """ <font color="blue">
                        1. Click on "Try it out".<br>
                        2. Enter the gender in the box below.<br>
                        3. Scroll to "Resposes" to see Top 5 users with the most hours of play in the given genre, with their URL and user_id.
                        </font>
                        """,
         tags=["General Inquiries"])
def userForGenre(genre: str = Query(..., 
                            description="Video Game Genre", 
                            example='Indie')):
    return afdef.userForGenre(genre)


@app.get('/game_recommendation',
         description=""" <font color="pink">
                    INSTRUCTIONS<br>
                    1. Click on "Try it out".<br>
                    2. Enter the name of a game in box below.<br>
                    3. Scroll to "Resposes" to see recommended games.
                    </font>
                    """,
         tags=["Recommendation"])
def game_recommendation(item_id:int = Query(..., 
                                         description="Game from which the recommendation of other games is made", 
                                         example="Killing Floor")):
    return afdef.game_recommendation(item_id)