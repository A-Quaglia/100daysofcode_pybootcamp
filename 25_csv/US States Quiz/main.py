import turtle
from statesquiz import StatesQuiz


screen = turtle.Screen()
screen.title("U.S Stats Game")
image = "blank_states_img.gif"

screen.addshape(image)

turtle.shape(image)

# def get_mouse_cick_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_cick_coor)
quiz = StatesQuiz("50_states.csv")

answers = []
# total_states = len(quiz.states)
total_states=2
def get_user_input() -> str:
    right_answers = len(answers)
    answer_state = screen.textinput(title=f"{right_answers}/{total_states}Guess the State", prompt="What's another state's name?")
    return answer_state.title()

def check_win():
    right_answers = len(answers)
    return right_answers == total_states
        

def quizgame():
    state = get_user_input()
    resp = quiz.search_state(state)
    if resp and state not in answers:
        answers.append(resp.name)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.goto(resp.coor_x, resp.coor_y)
        t.write(resp.name)

    if not check_win():
        quizgame()

quizgame()

print("You Won")