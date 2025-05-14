from ctypes import windll
from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain:QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzbaby")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score_label = Label(text="Score:0", bg=THEME_COLOR,pady=20, fg="white")
        self.score_label.grid(row=0, column=1)


        self.canvas = Canvas(width=300, height=250,)
        self.question_text = self.canvas.create_text(150,125,text="sometext",font=("Arial",20,"italic"), width=280)
        self.canvas.grid(row=1, column=0, columnspan=2)

        check_button = PhotoImage(file="images/true.png")
        cross_button = PhotoImage(file="images/false.png")
        self.check_button = Button(image=check_button, highlightthickness=0, command=self.true_pressed)
        self.cross_button = Button(image=cross_button, highlightthickness=0, command=self.false_pressed)
        self.check_button.grid(row=2, column=0, pady=20)
        self.cross_button.grid(row=2, column=1, pady=20)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():

            self.score_label.config(text=f"Score:{self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="you have completed the quiz")
            self.check_button.config(state="disabled")
            self.cross_button.config(state="disabled")

    def true_pressed(self):
        is_right = self.quiz.check_answer("true")
        self.give_feedback(is_right)

    def false_pressed(self):
        is_wrong = self.quiz.check_answer("false")
        self.give_feedback(is_wrong)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000,self.get_next_question)










