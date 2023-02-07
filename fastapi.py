from typing import Union
from fastapi import FastAPI


app = FastAPI()


@app.post("/user/signUp/{user_id}")
def userSignUp(user_id: str):
    """
    Create profile for user
    """
    pass


@app.post("/user/signIn")
def userSignIn(user_id: str):
    """
    Activate account for usage
    """
    pass


@app.post("/getMatch/{user_id}")
def getMatch(user_id: str, preferences: Union[str, None] = None):
    """
    Find a match for user based on preferences
    """
    pass


@app.post("/chooseAlgo/{choice}")
def chooseAlgo(choice: str):
    """
    Chose an algo to predict recommendations
    """
    pass
