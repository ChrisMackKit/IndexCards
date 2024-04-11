import tkinter as tk

class GUI:

    def __init__(self) -> None:
        
        self.question = "Was ist die Hauptstadt von Deutschland?"
        self.answer = "Berlin"
        self.box = 1
        self.stats = [True, False, False, True]
        self.topics = ['Hauptstädte', 'Flüsse', 'Informatik']
        

        self.window = tk.Tk()
        self.window.geometry("800x400")
        self.window.title("Index Card Program")

        # Texts and labels
        self.questionLabel = tk.Label(self.window, text = self.question, font=('Arial', 18))
        self.questionLabel.pack(padx= 0, pady=20)

        self.answerText = tk.Text(self.window, height = 1)
        self.answerText.pack(padx = 0, pady = 10)

        self.answerLabel = tk.Label(self.window, text = "")
        self.answerLabel.pack(padx = 0, pady = 10)

        self.statsBox = tk.Label(self.window, text = self.stats, font=(14))
        self.statsBox.place(x = 300, y=240)
        
        # Button of the GUI
        self.showAnswer = tk.Button(self.window, text = "show answer", command = self.showAnswer, font=('Arial', 18))
        self.showAnswer.place(x= 90, y=120, height=30, width=200)
        
        self.correctAnswer = tk.Button(self.window, text = "correct answer", command = self.correctAnswer, font=('Arial', 18))
        self.correctAnswer.place(x= 300, y=120, height=30, width=200)
        
        self.wrongAnswer = tk.Button(self.window, text = "wrong answer", command = self.wrongAnswer, font=('Arial', 18))
        self.wrongAnswer.place(x= 510, y=120, height=30, width=200)
        
        self.addTopic = tk.Button(self.window, text = "add new topic", command = self.addTopic, font=('Arial', 18))
        self.addTopic.place(x= 90, y= 150, height=30, width=200)

        # Drop down menu
        self.clicked = tk.StringVar()
        self.clicked.set('Choose Topic')
        self.topicMenu = tk.OptionMenu(self.window, self.clicked, *self.topics)
        self.topicMenu.place(x=80, y= 300)

        self.window.mainloop()

    def showAnswer(self):
            #answerLabel.configure(text = answer)
            #show the answer in the window
            print("okay")
            self.answerLabel = tk.Label(self.window, text = self.answer, font=('Arial', 16)).place(x = 350, y = 200)

    def correctAnswer(self):
            #updates stats and goes to next question
            print("correct")
            self.stats.pop(0)
            self.stats.append(True)
            self.statsBox.destroy()
            self.statsBox = tk.Label(self.window, text = self.stats, font=(14))
            self.statsBox.place(x = 300, y=240)

    def wrongAnswer(self):
            #updates stats and goes to next question
            print("wrong")
            self.stats.pop(0)
            self.stats.append(False)
            self.statsBox.destroy()
            self.statsBox = tk.Label(self.window, text = self.stats, font=(14))
            self.statsBox.place(x = 300, y=240)

    def addTopic(self):
            #adds new topic to the JSON
            print("new topic created")
            self.addTopicWindow = tk.Toplevel(self.window)
            self.addTopicWindow.title('Add New Topic')
            self.addTopicWindow.geometry('500x150')
            
            
            self.addTopicText = tk.Label(self.addTopicWindow, text ='Enter the name for the new topic: ')
            self.addTopicText.pack()
            self.addTopicButton = tk.Button(self.addTopicWindow, text = "add topic", command = self.addTopic2, font=('Arial', 18))
            self.addTopicButton.place(x= 150, y=100, height=30, width=200)
            self.topicText = tk.Text(self.addTopicWindow, height = 1)
            self.topicText.pack(padx = 0, pady = 10)
            

    def addTopic2(self):
        topicName = self.topicText.get('1.0', tk.END)
        print('topic added: ' + topicName)

GUI()