from tkinter import *
names = [] #empty list for future list ie scoreboard 

class QuizStarter:
    def __init__(self, parent):#constructor, The init function is called automatically every time the class is being used to create a new object.
        
        background_color="Royal blue"#to set it as a background color for all the label widget
        
        #frame set up
        self.quiz_frame=Frame(parent, bg = background_color, padx=100, pady=100)
        #padx pady How many pixels to pad widget horizontally (x) and vertically (y), outside widget's borders.
        self.quiz_frame.grid()#this turns ya widget into a table structure hence grid.
        
        #label widget for the heading
        self.heading_label=Label(self.quiz_frame, text="STOOOPID QUIZ", font=("Times New Roman","18", "bold"),bg=background_color)
        self.heading_label.grid(row=0, padx=20)
        
        #holds value of radio buttons a single selection from a list of things
        self.var1=IntVar()
        
        #label for username
        self.user_label=Label (self.quiz_frame, text="GIMME YA NAME: ", font=("Tw Cen MT", "16"),bg=background_color)
        self.user_label.grid(row=1, padx=20, pady=20)

        #entry box
        self.entry_box=Entry(self.quiz_frame)
        self.entry_box.grid(row=2,padx=20, pady=20)
        
        
        #continue button
        self.continue_button= Button(self.quiz_frame, text="Continue", font=("Times New Roman", "13", "bold"), bg="Green", command=self.name_collection) 
        self.continue_button.grid(row=3, padx=20, pady=20)
        
    def name_collection(self):
        name=self.entry_box.get()
        names.append(name) #add name to names list declared at the beginning 
        self.quiz_frame.destroy() #bomb the starter window
        

if __name__ =="__main__":
    root = Tk()
    root.title("NZ Road Rules Quiz")
    quiz_instance= QuizStarter (root) #instantiation, making an instance of the class QuizStarter 
    root.mainloop() #so the window dont leave

    from tkinter import *
    import random

    names = []
    global questions_answers
    asked=[] #asked questions will have their number added to the list so randomiser() can check if number is already chosen
    ["What will you do when a cat runs across the road?", "speed up and run it over for ten points", "slow down so the cat dont get run over"]

