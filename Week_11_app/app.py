import tkinter as tk
from tkinter import messagebox

QUESTIONS = [
    {
        "question": "What keyword defines a function in Python?",
        "choices": ["func", "def", "function", "define"],
        "answer": "def"
    },
    {
        "question": "In what year did Nigeria win the Olympic gold medal in men's football?",
        "choices": ["1992", "1996", "2000", "2004"],
        "answer": "1996"
    },
    {
        "question": "How many players are on the court for one team during a standard volleyball match?",
        "choices": ["5", "6", "7", "8"],
        "answer": "6"
    },
    {
        "question": "What is the chemical symbol for gold?",
        "choices": ["Go", "Gd", "Au", "Ag"],
        "answer": "Au"
    },
    {
        "question": "Which HTTP status code indicates a resource was not found?",
        "choices": ["400", "401", "403", "404"],
        "answer": "404"
    },
    {
        "question": "What is the largest desert in the world?",
        "choices": ["Sahara Desert", "Arabian Desert", "Gobi Desert", "Antarctic Desert"],
        "answer": "Antarctic Desert"
    },
    {
        "question": "In what year did Abuja officially become the capital of Nigeria?",
        "choices": ["1960", "1976", "1985", "1991"],
        "answer": "1991"
    },
    {
        "question": "Who is Nigeria's all-time leading men's international goalscorer?",
        "choices": ["Jay-Jay Okocha", "Nwankwo Kanu",   "Rashidi Yekini", "Victor Osimhen"],
        "answer": "Rashidi Yekini"
    },
    {
        "question": "Which continent has the largest number of countries?",
        "choices": ["Asia", "Europe", "Africa", "South America"],
        "answer": "Africa"
    },
    {
        "question": "In which country is Mount Everest primarily located?",
        "choices": ["India", "Nepal", "Bhutan", "Pakistan"],
        "answer": "Nepal"
    }
]


def check_answer(question, choice):
    return choice == question["answer"]


def get_feedback(score, total):
    if score == total:
        return "Perfect score! Great Job"
    elif score >= total / 2:
        return "Solid job! You try small"
    else:
        return "Nice try! Go again to do better"


current_index = 0
score = 0
answered_current = False

def on_submit():
    global score, answered_current

    player_name = name_entry.get().strip()
    choice = selected_choice.get()

    if player_name == "":
        messagebox.showerror("Name Missing", "Please enter your name first!")
        return

    if choice == "":
        messagebox.showerror("No Answer", "Please pick an answer before submitting!")
        return

    if  answered_current:
        return

    answered_current = True
    current_q = QUESTIONS[current_index]

    if check_answer(current_q, choice):
        score += 1
        feedback_label.config(
            text=f"Correct! | Score: {score} / {len(QUESTIONS)}",
            fg="#15803d"
        )
    else:
        feedback_label.config(
            text=f"Wrong! Answer: {current_q['answer']} | Score: {score} / {len(QUESTIONS)}",
            fg="#b91c1c"
        )


def on_next():
    global current_index, answered_current

    if not answered_current:
        messagebox.showerror("Calma!", "Please submit an answer before moving on")
        return

    current_index += 1
    answered_current = False
    selected_choice.set("")

    if current_index < len(QUESTIONS):
        next_q = QUESTIONS[current_index]
        question_label.config(text=f"Q{current_index + 1}: {next_q['question']}")
        for rb, choice_text in zip(radio_buttons, next_q["choices"]):
            rb.config(text=choice_text, value=choice_text)
        feedback_label.config(text=f"Score: {score} / {len(QUESTIONS)}", fg="#0f766e")
    else:
        player_name = name_entry.get().strip()
        final_msg = get_feedback(score, len(QUESTIONS))
        question_label.config(text=f"Quiz Complete, {player_name}!")
        feedback_label.config(
            text=f"Final Score: {score} / {len(QUESTIONS)} - {final_msg}",
            fg="#1d4ed8"
        )
        submit_btn.config(state="disabled")
        next_btn.config(state="disabled")

def on_restart():
    global current_index, score, answered_current

    current_index = 0
    score = 0
    answered_current = False

    name_entry.delete(0, tk.END)
    selected_choice.set("")

    first_q = QUESTIONS[0]
    question_label.config(text=f"Q1: {first_q['question']}")
    for rb, choice_text in zip(radio_buttons, first_q["choices"]):
        rb.config(text=choice_text, value=choice_text)

    feedback_label.config(text=f"Score: 0 / {len(QUESTIONS)}", fg="#0f766e")
    submit_btn.config(state="normal")
    next_btn.config(state="normal")
    

#  SETUP MY WINDOW
root = tk.Tk()
root.title("AKJ Trivia Quiz")
root.geometry("540x480")
root.config(bg="#f4f6f9")

#   INPUT PLAYER NAME
tk.Label(root, text="Player Name", font=("Arial", 11, "bold"), bg="#f4f6f9").pack(pady=(12, 2))
name_entry = tk.Entry(root, font=("Arial", 12), width=25)
name_entry.pack(pady=(0, 10))

# DISPLAY YOUR QUESTION
question_label = tk.Label(
    root,
    text=f"Q1: {QUESTIONS[0]['question']}",
    font=("Arial", 13, "bold"),
    wraplength=480,
    bg="#f4f6f9",
    fg="#1e293b"
)
question_label.pack(pady=10)

# FOUR RADIO BUTTONS FOR CHOICES
selected_choice = tk.StringVar(value="")
radio_buttons = []

for choice_text in QUESTIONS[0]["choices"]:
    rb = tk.Radiobutton(
        root,
        text=choice_text,
        variable=selected_choice,
        value=choice_text,
        font=("Arial", 12),
        bg="#f4f6f9",
        anchor="w",
        width=28
    )
    rb.pack(pady=2)
    radio_buttons.append(rb)

# FEEDBACK AND SCORE DISPLAY
feedback_label = tk.Label(root, text="Score: 0 / 10", font=("Arial", 12 , "bold"), bg="#f4f6f9", fg="#0f766e")
feedback_label.pack(pady=12)

# 5. Action Buttons (side-by-side in a Frame)
button_frame = tk.Frame(root, bg="#f4f6f9")
button_frame.pack(pady=10)

submit_btn = tk.Button(
    button_frame, text="Submit Answer", command=on_submit,
    font=("Arial", 11, "bold"), bg="#2563eb", fg="white", width=13
)
submit_btn.pack(side="left", padx=5)

next_btn = tk.Button(
    button_frame, text="Next Question", command=on_next,
    font=("Arial", 11, "bold"), bg="#0f766e", fg="white", width=13
)
next_btn.pack(side="left", padx=5)

restart_btn = tk.Button(
    button_frame, text="Restart", command=on_restart,
    font=("Arial", 11, "bold"), bg="#dc2626", fg="white", width=10
)
restart_btn.pack(side="left", padx=5)

# Bonus: Press Enter to submit & Footer credit
root.bind("<Return>", lambda event: on_submit())
tk.Label(root, text="Built by AKJ", font=("Arial", 9, "italic"), bg="#f4f6f9", fg="#64748b").pack(side="bottom", pady=8)

root.mainloop()


