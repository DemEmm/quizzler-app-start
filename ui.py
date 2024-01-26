import tkinter as tk
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_object: QuizBrain):
        self.quiz_object = quiz_object
        self.answer: bool = True
        self.page_my = tk.Tk()
        self.page_my.config(padx=20, pady=20, bg=THEME_COLOR)
        self.score = 0
        self.score_label = tk.Label(text=f"Score: {self.score}", bg=THEME_COLOR, font=("Ariel", 15, "bold"))
        self.score_label.grid(row=0, column=1)
        self.canvas_my = tk.Canvas(highlightthickness=0, height=300, width=300)
        self.canvas_text = self.canvas_my.create_text(150, 150, text="dfg", font=("Arial", 10, "bold"), width=280)
        self.canvas_my.grid(row=1, column=0, columnspan=2)

        self.image_true = tk.PhotoImage(file="images/true.png")
        self.image_false = tk.PhotoImage(file="images/false.png")

        self.true_button = tk.Button(height=100, width=100, highlightthickness=0, image=self.image_true, padx=200,
                                     command=self.is_true)
        self.true_button.grid(row=2, column=0)

        self.false_button = tk.Button(height=100, width=100, highlightthickness=0, image=self.image_false,
                                      command=self.is_false)
        self.false_button.grid(row=2, column=1, pady=20)
        self.next_question()
        self.page_my.mainloop()

    def next_question(self):
        self.canvas_my.config(bg="white")
        text = self.quiz_object.next_question()
        self.canvas_my.itemconfig(self.canvas_text, text=text)

    def is_true(self):
        self.answer = "True"
        self.quiz_object.check_answer(self.answer)
        self.score = self.quiz_object.score
        if self.quiz_object.still_has_questions():
            self.score_label.config(text=f"Score: {self.score}")
            self.page_my.after(1000, self.next_question)
        else:
            self.canvas_my.itemconfig(self.canvas_text, text=f"No more Questions Sorry : (")
        self.ui_screen_respond()

    def is_false(self):
        self.answer = "False"
        self.quiz_object.check_answer(self.answer)
        self.score = self.quiz_object.score
        if self.quiz_object.still_has_questions():
            self.score_label.config(text=f"Score: {self.score}")
            self.page_my.after(1000, self.next_question)
        else:
            self.canvas_my.itemconfig(self.canvas_text, text=f"No more Questions Sorry : (")
        self.ui_screen_respond()

    def ui_screen_respond(self):
        if self.quiz_object.user_answer_is:
            self.canvas_my.config(bg="green")

        else:
            self.canvas_my.config(bg="red")

    def turn_white(self):
        self.canvas_my.config(bg="white")
