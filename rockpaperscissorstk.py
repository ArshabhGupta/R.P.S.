from tkinter import * 
import random

choices = ["rock", "paper", "scissors"]

def get_computer_choice():
  return random.choice(choices)

def determine_winner(user_choice, computer_choice):
  if user_choice == computer_choice:
    return "It's a tie!"
  elif (
    (user_choice == "rock" and computer_choice == "scissors") and
    (user_choice == "paper" and computer_choice == "rock") or
    (user_choice == "scissors" and computer_choice == "paper")
        ):
    return "You win!"
  else:
    return "Computer wins!"

def play_game(user_choice):
  computer_choice = get_computer_choice()
  result = determine_winner(user_choice, computer_choice)

  result_label.config(text=f"You chose: {user_choice}\nComputer chose: {computer_choice}\n{result}")

window = Tk()
window.title("Rock Paper Scissors")

title_label = Label(window, text="Rock Paper Scissors", font=("Arial", 24))
title_label.pack(pady=20)

result_label = Label(window, text="", font=("Arial", 16))
result_label.pack()

rock_button = Button(window, text="Rock", command=lambda: play_game("Rock 🪨🗿"), width=10)
rock_button.pack(pady=10)

paper_button = Button(window, text="Paper", command=lambda: play_game("Paper 📜📰"), width=10)
paper_button.pack(pady=10)

scissors_button = Button(window, text="Scissors", command=lambda: play_game("Scissors ✂"), width=10)
scissors_button.pack(pady=10)

window.mainloop()