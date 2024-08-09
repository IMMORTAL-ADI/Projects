import random
from tkinter import *
from PIL import ImageTk
class Rpsgame:
    def __init__(self):
        root = Tk()
        self.root = root
        self.root.title("Rock-Paper-Scissor game")
        self.root.geometry("700x700+0+0")
        self.root.config(bg="white")

        # score var initialize
        self.player_score = 0
        self.comp_score = 0

        # photo image converter-player
        self.rock_1 = ImageTk.PhotoImage(file="C:/Aditya/CWH_Python_exercise/Exercise modules/exercise 5/rock1.jpeg")
        self.paper_1 = ImageTk.PhotoImage(file="C:/Aditya/CWH_Python_exercise/Exercise modules/exercise 5/paper1.png")
        self.scissor_1 = ImageTk.PhotoImage(
            file="C:/Aditya/CWH_Python_exercise/Exercise modules/exercise 5/scissor1.png")
        # photo image -computer
        self.rock_2 = ImageTk.PhotoImage(file="C:/Aditya/CWH_Python_exercise/Exercise modules/exercise 5/rock2.jpeg")
        self.paper_2 = ImageTk.PhotoImage(file="C:/Aditya/CWH_Python_exercise/Exercise modules/exercise 5/paper2.png")
        self.scissor_2 = ImageTk.PhotoImage(
            file="C:/Aditya/CWH_Python_exercise/Exercise modules/exercise 5/scissor2.png")

        # =========game heading============
        title = Label(self.root, text="Rock-Paper-Scissor", font=("times new roman", 30, "bold"), bg="white",
                      fg="black", anchor="center", padx=10, pady=10)
        title.place(x=160, y=10)

        # =========score frame============
        score_frame = Frame(self.root, bg="white")
        score_frame.place(x=100, y=100, width=500, height=30)

        self.player_label = Label(score_frame, text=f"Player : {self.player_score}", font=("times new roman", 16),
                                  bg="white", fg="black")
        self.player_label.place(x=50, y=0)

        self.comp_label = Label(score_frame, text=f"Computer : {self.comp_score}", font=("times new roman", 16),
                                bg="white", fg="black")
        self.comp_label.place(x=300, y=0)

        #======== display images ===========
        display_frame = Frame(self.root, bg="white")
        display_frame.place(x=25, y=150, width=650, height=300)

        self.player_img = Label(display_frame, image=self.rock_1)
        self.player_img.place(x=0, y=0)
        self.comp_img = Label(display_frame, image=self.rock_2)
        self.comp_img.place(x=350, y=0)

        #======== message box ===========
        self.message_label = Label(self.root, text="PLAY!!", font=("times new roman", 20, "bold"), relief="solid",
                                   borderwidth=3, bg="white", fg="black")
        self.message_label.place(x=150, y=470, width=400, height=50)

        #======== rock,paper,scissor btn ===========
        btns_frame = Frame(self.root, bg="white")
        btns_frame.place(x=75, y=540, width=550, height=40)

        btn_rock = Button(btns_frame, text="ROCK", font=("times new roman", 16), command=lambda: self.update_img(0),
                          bd=3, bg="Blue", fg="white", cursor="hand2")
        btn_rock.place(x=50, y=0)

        btn_paper = Button(btns_frame, text="PAPER", font=("times new roman", 16), command=lambda: self.update_img(1),
                           bd=3, bg="Blue", fg="white", cursor="hand2")
        btn_paper.place(x=220, y=0)

        btn_scissor = Button(btns_frame, text="SCISSOR", font=("times new roman", 16),
                             command=lambda: self.update_img(2), bd=3, bg="Blue", fg="white", cursor="hand2")
        btn_scissor.place(x=400, y=0)

        #======== quit button ===========
        btn_quit = Button(self.root, text="QUIT", font=("times new roman", 20), command=lambda: self.root.destroy(),
                          bd=5, bg="blue", fg="white", cursor="hand2")
        btn_quit.place(x=295, y=610)

        mainloop()

    # rock=0, paper=1, scissor=2
    def update_img(self, user):
        #for computer
        comp = random.randint(0, 2)
        if comp == 0:
            self.comp_img.config(image=self.rock_2)
        elif comp == 1:
            self.comp_img.config(image=self.paper_2)
        elif comp == 2:
            self.comp_img.config(image=self.scissor_2)

        #for player image
        if user == 0:
            self.player_img.config(image=self.rock_1)
        elif user == 1:
            self.player_img.config(image=self.paper_1)
        elif user == 2:
            self.player_img.config(image=self.scissor_1)

        self.update_score(comp, user)

    #scores and message box is updated
    def update_score(self, comp, user):
        if comp == user:
            self.message_label.config(text="It's a tie")

        elif (comp == 0 and user == 2):
            self.comp_score += 1
            self.message_label.config(text="Computer Win's")
            self.comp_label.config(text=f"Computer : {self.comp_score}")

        elif (comp == 1 and user == 0):
            self.comp_score += 1
            self.message_label.config(text="Computer Win's")
            self.comp_label.config(text=f"Computer : {self.comp_score}")

        elif (comp == 2 and user == 1):
            self.comp_score += 1
            self.message_label.config(text="Computer Win's")
            self.comp_label.config(text=f"Computer : {self.comp_score}")

        else:
            self.player_score += 1
            self.message_label.config(text="Player Win's")
            self.player_label.config(text=f"Player : {self.player_score}")


Rpsgame()
