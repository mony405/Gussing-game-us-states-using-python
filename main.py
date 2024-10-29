import turtle
import pandas as pd

scr=turtle.Screen()
scr.title("U.S. STATES GAME")
img="imges/blank_states_img.gif"
scr.addshape(img)
scr.setup(720,500)
turtle.shape(img)

data=pd.read_csv("Data/50_states.csv")
states_list=data["state"].to_list()
states_x=data["x"].to_list()
states_y=data["y"].to_list()

correct_ans=0
game_on=True
guessed_states=[]
missing_states=[]
while game_on:
    ans=""
    try:
        ans = scr.textinput(f"{correct_ans}/50 States Correct", "what another state's name? ").title()
    except AttributeError:
        game_on = False
    if ans=="Exit":
        for state in states_list:
            if state not in guessed_states:
                missing_states.append(state)
        missing_data=pd.DataFrame(missing_states)
        missing_data.to_csv("Data/missing.csv")
        game_on=False
    if ans in states_list:
        guessed_states.append(ans)
        s = turtle.Turtle()
        s.hideturtle()
        s.penup()
        index = states_list.index(ans)
        x=states_x[index]
        y=states_y[index]
        s.goto(x,y)
        s.write(ans,move= False,
        align= "center", font=("Arial", 8, "normal"))
        correct_ans+=1
        if correct_ans==50:
            game_on=False