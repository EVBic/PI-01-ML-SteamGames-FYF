from fastapi import FastAPI, Query
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
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

@app.get(path = '/developer', 
          description = """ <font color="black">
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
          description = """ <font color="black">
                        INSTRUCTIONS<br>
                        1. Click on "Try it out".<br>
                        2. Enter the user_id in the box below.<br>
                        3. Scroll to "Resposes" to see the amount of money spent by the user, the percentage of recommendations made by the user and the number of items the user has.
                        </font>
                        """,
         tags=["General Inquiries"])

def userdata(user_id: str = Query(..., 
                                description="user_id", 
                                example="js41637")):
        
    return afdef.userdata(user_id)
    

@app.get("/UserForGenre/{genre}", 
         description = """ <font color="black">
                        1. Click on "Try it out".<br>
                        2. Enter the genre in the box below.<br>
                        3. Scroll to "Responses" to see the user with the most playtime for the given genre and their playtime by year.
                        </font>
                        """,
         tags=["General Inquiries"])
def UserForGenre(genre: str):
    return afdef.UserForGenre(genre)


@app.get("/best_developer_year/{year}", 
         description = """ <font color="blue">
                        INSTRUCTIONS<br>
                        1. Click on "Try it out".<br>
                        2. Enter the year in the box below.<br>
                        3. Scroll to "Responses" to see the result of the classification.
                        </font>
                        """,
         tags=["General Inquiries"])
def get_best_developer_year(year: int):
    return afdef.best_developer_year(year)

@app.get('/dev_reviews_analysis',
         description="""<font color="black">
                    INSTRUCTIONS<br>
                    1. Click on "Try it out".<br>
                    2. Enter the year in the box below.<br>
                    3. Scroll down to "Responses" to view the number of user review records categorized with sentiment analysis.
                    </font>
                    """,
         tags=["General Queries"])
def dev_reviews_analysis(year: str = Query(..., 
                                         description="Returns a dictionary with the developer's name", 
                                         example="Trion Worlds, Inc.")):
    return afdef.dev_reviews_analysis(developer)


@app.get('/game_recommendation',
         description=""" <font color="black">
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