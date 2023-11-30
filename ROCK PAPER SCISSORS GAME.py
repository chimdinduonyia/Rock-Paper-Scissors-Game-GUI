
from tkinter import *
from random import shuffle
from PIL import ImageTk, Image

root = Tk()

# Player and Computer Scores
player_score = 0
computer_score = 0

# Player and computer choices
computer_choice = None
player_choice = None

# List of computers options to shuffle from
computer_list = ["Rock", "Paper", "Scissors"]

# What round out of the decided number of rounds (Best of 5 starts with game 1 out of 5 matches to be played)
game = 0
matches = 0

# Opens images as PhotoImage Objects
Rock = ImageTk.PhotoImage(Image.open(
    "C://Users/USER/Documents/PYTHON PROJECTS/Images/Rock Paper Scissors Game/Rock.png").resize((200, 200), Image.ANTIALIAS))
Paper = ImageTk.PhotoImage(Image.open(
    "C://Users/USER/Documents/PYTHON PROJECTS/Images/Rock Paper Scissors Game/Paper.png").resize((200, 200), Image.ANTIALIAS))
Scissors = ImageTk.PhotoImage(Image.open(
    "C://Users/USER/Documents/PYTHON PROJECTS/Images/Rock Paper Scissors Game/Scissors.png").resize((200, 200), Image.ANTIALIAS))
Placeholder = ImageTk.PhotoImage(Image.open(
    "C://Users/USER/Documents/PYTHON PROJECTS/Images/Rock Paper Scissors Game/Placeholder.png").resize((200, 200), Image.ANTIALIAS))

# Image variables cast to dictionary for easy indexing
game_dict = {"Rock": Rock, "Paper": Paper, "Scissors": Scissors}

# Functions


def remove_buttons():

    global input_label
    global rock_button
    global paper_button
    global scissors_button

    # Built to remove every player input button after the number of matches has been reached
    input_label.grid_forget()
    rock_button.grid_forget()
    paper_button.grid_forget()
    scissors_button.grid_forget()


def check_game():

    global game
    global matches

    # Checks if the number of rounds decided has been exhausted
    if game <= (matches - 1):
        # If it hasn't, then Pass
        pass

    else:
        # If it has, then remove player input buttons, check for the winner and provide an exit button
        remove_buttons()
        winner()
        Button(root, text="Leave", command=root.quit).grid(
            row=4, column=0, columnspan=3, pady=40)


def compare():

    # Compares the player and computer's choices as per Rock vs Paper, Paver vs Scissors
    global player_choice
    global computer_choice
    global player_score
    global computer_score
    global score_board
    global game

    if player_choice == Rock and computer_choice == Paper:
        computer_score += 1
    elif player_choice == Paper and computer_choice == Rock:
        player_score += 1
    elif player_choice == Scissors and computer_choice == Rock:
        computer_score += 1
    elif player_choice == Rock and computer_choice == Scissors:
        player_score += 1
    elif player_choice == Paper and computer_choice == Scissors:
        computer_score += 1
    elif player_choice == Scissors and computer_choice == Paper:
        player_score += 1
    elif player_choice == computer_choice:
        pass
    else:
        pass

        # Update scoreboard after comparison
    score_board = Label(
        root, text=f"Scoreboard\n{computer_score} | {player_score}", relief=SUNKEN, anchor=CENTER)
    score_board.grid(row=1, column=0, columnspan=3, pady=20)

    # Updates game variable to show a round has been completed
    game += 1

    # Checks if the number of decided rounds has been completed
    check_game()


def computer_choose():

    # Computer's turn to play
    global game_dict
    global computer_list
    global computer_choice
    global computer_label

    # Shuffle the computer list for randomised choices
    shuffle(computer_list)
    # Picks one and makes it computer's choice
    computer_choice = game_dict[computer_list[0]]
    # Displays the image based off the choice, as represented in the game_dict dictionary
    computer_label = Label(computer_frame, image=computer_choice)
    computer_label.grid(row=0, column=0, padx=20, pady=20)

    # Makes a comparison of the player's choice against the computer's choice
    compare()


def player_choose(text):

    # This is the functionality of the player buttons as they take in the value, option of the button and chooses that value
    global game_dict
    global player_choice
    global player_label

    # Checks game dictionary for the choice and assigns the choice to the player_choice variable
    player_choice = game_dict[text]

    # Displays Player choice
    player_label = Label(player_frame, image=player_choice)
    player_label.grid(row=0, column=0, padx=20, pady=20, columnspan=3)

    # Triggers the function for the computer to choose
    computer_choose()


def winner():

    # Chooses a winner by comparing the PLayer's score aganst the Computer's score
    global player_score
    global computer_score

    if computer_score > player_score:
        winner = Label(root, text="Computer Wins", anchor=CENTER)
        winner.grid(row=0, column=0, columnspan=3)
    elif computer_score < player_score:
        winner = Label(root, text="Player Wins", anchor=CENTER)
        winner.grid(row=0, column=0, columnspan=3)
    else:
        winner = Label(root, text="Tie!", anchor=CENTER)
        winner.grid(row=0, column=0, columnspan=3)


def display_game():

    # This function is called after the number of rounds has been decided to display both player and computer boards

    global player_frame
    global computer_frame
    global computer_label
    global player_label
    global score_board
    global input_label
    global rock_button
    global paper_button
    global scissors_button

    # Scoreboard, Computer board and Player board using Label and Frame
    score_board.grid(row=1, column=0, columnspan=3, pady=20)

    computer_frame.grid(row=2, column=0, padx=20)

    computer_label.grid(row=0, column=0, padx=20, pady=20)

    player_frame.grid(row=2, column=2, padx=20, pady=30)

    player_label.grid(row=0, column=0, padx=20, pady=20, columnspan=3)

    input_label.grid(row=1, column=0, columnspan=3)

    # Rock, Paper, Scissors buttons for Player Frame are gridded on to window frame
    rock_button.grid(row=2, column=0, pady=20)
    paper_button.grid(row=2, column=1, pady=20)
    scissors_button.grid(row=2, column=2, pady=20)


def start_game(number):

    # This function takes in the values from the buttons and makes that the number of rounds before discarding the buttons and displaying the game
    global matches
    global game
    global bo2
    global bo3
    global bo5

    matches = number

    bo2.grid_forget()
    bo3.grid_forget()
    bo5.grid_forget()

    display_game()


# Instantiates the scoreboard, Player board and Computer board
score_board = Label(
    root, text=f"Scoreboard\n{player_score} | {computer_score}", relief=SUNKEN, anchor=CENTER)

computer_frame = LabelFrame(root, text="Computer", relief=SUNKEN)

computer_label = Label(computer_frame, image=Placeholder)

player_frame = LabelFrame(root, text="Player", relief=SUNKEN)

player_label = Label(player_frame, image=Placeholder)

input_label = Label(player_frame, text="Rock, Paper, Scissors")

# Instantiates Round choice buttons (Best of 2, Best of 3, Best of 5) and positions them on the window
bo2 = Button(root, text="BEST OF 2",
             command=lambda: start_game(2), padx=20, pady=20)
bo2.grid(row=1, column=1, padx=20, pady=20)

bo3 = Button(root, text="BEST OF 3",
             command=lambda: start_game(3), padx=20, pady=20)
bo3.grid(row=1, column=2, padx=20, pady=20)

bo5 = Button(root, text="BEST OF 5",
             command=lambda: start_game(5), padx=20, pady=20)
bo5.grid(row=1, column=3, padx=20, pady=20)

# Instantiates Rock, Paper, Scissors Buttons
rock_button = Button(player_frame, text="Rock",
                     command=lambda: player_choose("Rock"), padx=20, pady=20)

paper_button = Button(player_frame, text="Paper",
                      command=lambda: player_choose("Paper"), padx=20, pady=20)

scissors_button = Button(player_frame, text="Scissors",
                         command=lambda: player_choose("Scissors"), padx=20, pady=20)

root.mainloop()
